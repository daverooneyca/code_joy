import sys
import pytest

from doubles import allow

sys.path.insert(0, './src/')

from commit_details_builder import CommitDetailsBuilder
from git_command_runner import GitCommandRunner

rating_file = "./tests/rating_file"

def test_build_full_commit_details_from_known_data():
    sample_rating = "2"
    create_test_rating_file(sample_rating)

    runner = GitCommandRunner()

    sample_raw_commit = '{"id":"xyzzy-1","shortId":"xyzzy-2","authorName":"John Smith","committerName":"John Smith","committerEmail":"jsmith@somewhere.com","subject":"xyzzy","body":"xyzzy"}'
    sample_branch = "xyzzy"
    sample_git_location = "git@github.com:xyzzy/xyzzy.git"
    sample_https_location = "https://github.com/xyzzy/xyzzy/"
    sample_files = "file1\nfile2"

    # Stub the command runner calls to allows specifying the return values
    allow(runner).fetch_last_commit.and_return(sample_raw_commit)
    allow(runner).fetch_current_branch.and_return(sample_branch)
    allow(runner).fetch_location.and_return(sample_git_location)
    allow(runner).fetch_commit_files.and_return(sample_files)

    builder = CommitDetailsBuilder(rating_file, runner);

    expected_files = ["file1", "file2"]

    commit_details = builder.build()

    assert commit_details["id"] == "xyzzy-1"
    assert commit_details["shortId"] == "xyzzy-2"
    assert commit_details["rating"] == sample_rating
    assert commit_details["branch"] == sample_branch
    assert commit_details["git_location"] == sample_git_location
    assert commit_details["location"] == sample_https_location
    assert commit_details["files"] == expected_files

def test_fetch_rating_with_known_value_should_equal_that_value():
    assert create_test_rating_with("2") == "2"
    assert create_test_rating_with("3") == "3"
    assert create_test_rating_with("4") == "4"

def test_git_to_https_should_convert_to_usable_url():
    git_location = "git@github.com:xyzzy/xyzzy.git"
    expected_https_location = "https://github.com/xyzzy/xyzzy/"

    builder = CommitDetailsBuilder(rating_file)

    https_location = builder.git_to_https_for(git_location)

    assert https_location == expected_https_location

def create_test_rating_with(value):
    create_test_rating_file(value)

    builder = CommitDetailsBuilder(rating_file)

    return builder.fetch_rating()

def create_test_rating_file(rating="3"):
    with open(rating_file, 'w') as file:
        file.write(rating)
        file.close()    
