import sys
import pytest

from doubles import allow

# Adds the 'src' directory to the search path for modules
sys.path.insert(0, './src/')

from commit_message_handler import CommitMessageHandler, ExitCodes

rating_file = "./tests/rating_file"

def test_should_succeed_when_given_valid_rating():
    handler = CommitMessageHandler(rating_file)

    test_commit_file = "./tests/test_commit_file"
    test_commit_message = "-1- xyzzy"

    create_test_commit(test_commit_file, test_commit_message)

    result = handler.process_rating_in(test_commit_file)

    assert result == ExitCodes.SUCCESS

def test_should_succeed_when_rating_is_not_at_start_of_commit_message():
    handler = CommitMessageHandler(rating_file)

    test_commit_file = "./tests/test_commit_file"
    test_commit_message = "xyzzy -1-"

    create_test_commit(test_commit_file, test_commit_message)

    result = handler.process_rating_in(test_commit_file)

    assert result == ExitCodes.SUCCESS

def test_should_fail_when_no_rating_is_present():
    handler = CommitMessageHandler(rating_file)

    test_commit_file = "./tests/test_commit_file"
    test_commit_message = "xyzzy"

    create_test_commit(test_commit_file, test_commit_message)

    result = handler.process_rating_in(test_commit_file)

    assert result == ExitCodes.FAIL

def test_rating_should_be_removed_from_message_on_success():
    handler = CommitMessageHandler(rating_file)

    test_commit_file = "./tests/test_commit_file"
    test_commit_message = "-1- xyzzy"

    create_test_commit(test_commit_file, test_commit_message)

    result = handler.process_rating_in(test_commit_file)

    commit_message = handler.read_content_from(test_commit_file)

    assert result == ExitCodes.SUCCESS    
    assert commit_message == "xyzzy"

def create_test_commit(commit_file, message):
    with open(commit_file, 'w') as file:
        file.write(message)
        file.close()    
