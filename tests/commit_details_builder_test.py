import sys
import pytest
import doubles

sys.path.insert(0, './src/')

from commit_details_builder import CommitDetailsBuilder

rating_file = "./tests/rating_file"

def test_build_commit_details():
    test_rating = "2"
    create_test_rating_file(test_rating)

    builder = CommitDetailsBuilder(rating_file);

    commit_details = builder.build()

    assert commit_details is not None
    assert commit_details["id"] == "c9b597a53f9a8cf569d3144db1faa5d8e79cad63"

    assert commit_details["rating"] == test_rating
    assert commit_details["branch"] == "main"
    assert commit_details["git_location"] == "git@github.com:daverooneyca/code_joy.git"
    assert commit_details["location"] == "https://github.com/daverooneyca/code_joy/"
    assert commit_details["files"] == ["README.md", "src/post_commit_handler.py"]

def test_fetch_rating_with_known_value_should_equal_that_value():
    assert create_test_rating_with("2") == "2"
    assert create_test_rating_with("3") == "3"
    assert create_test_rating_with("4") == "4"

def test_git_to_https_should_convert_to_usable_url():
    git_location = "git@github.com:daverooneyca/code_joy.git"

    builder = CommitDetailsBuilder(rating_file)

    https_location = builder.git_to_https_for(git_location)

    assert https_location == "https://github.com/daverooneyca/code_joy/"

def create_test_rating_with(value):
    create_test_rating_file(value)

    builder = CommitDetailsBuilder(rating_file)

    return builder.fetch_rating()

def create_test_rating_file(rating="3"):
    with open(rating_file, 'w') as file:
        file.write(rating)
        file.close()    
