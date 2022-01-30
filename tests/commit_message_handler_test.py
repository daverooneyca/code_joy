# Copyright © 2022 Dave Rooney
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute, 
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
# LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

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
