# Git Hooks for Measuring Code Joy
NOTE: This is a port of [@DocOnDev's Code Joy](https://github.com/DocOnDev/team_joy) to Python

[Doc Norton](https://onbelay.co/) created a tool that allowed developers to indicate the "joy" they felt (or didn't feel) while working in a particular piece of code. This is done by adding a *_rating_* to the message when making a commit. [For background on why this is important, please read Doc's article on the topic.](https://www.scrumexpert.com/knowledge/measuring-joy-for-software-developers/)

The format for the commit message is:

`-(rating value)- Your commit message`

Example:

`git commit -m "-3- Added more tests to the prepare method"`

The rating is on a scale from 0 to 5:
- 0 - I may leave the software profession due to this code
- 1 - My eyes are bleeding and I don't know why this code works
- 2 - This is a tangled mess and caused physical pain while working in it
- 3 - I've seen worse, but I've seen better
- 4 - I'm pretty happy with this code
- 5 - This is the most clear, expressive and elegant code I've ever encountered

Obviously, we want to see 3's and up!

Please note that, after processing, the rating is removed from the commit message and not stored in git or Gitlab.


# The Hooks
The `commit-msg` hook will reject commits that do not have a quality rating

The `post-commit` hook will post the accepted commit to the configured repository. Current only NOOP and HTTP repositories are available.

# Installation
## Common
- Ensure that Python 3.7 or higher is installed on the machine
- Copy the contents of the `src` directory of this repo to the `.git/hooks` directory in any repository for which you want to use these hooks

## Linux, macOS
- Rename `commit-msg.py` to `commit-msg`
- Rename `post-commit.py` to `post-commit`
- Ensure both of those scripts are executable by running:
	- `chmod +x commit-msg`
	- `chmod +x post-commit`

## Windows
- Rename `commit-msg-windows.py` to `commit-msg`
- Rename `post-commit-windows.py` to `post-commit`
- Change the first line of each of those scripts, depending on the location of the Python executable on your system
	- the default is `#!%userprofile%\AppData\Local\Microsoft\WindowsApps\python.exe`

## Python Libraries
### Runtime
CodeJoy doesn’t require any libraries outside of core Python

### Development
To run the tests, you need to install PyTest and Doubles

`pip install -U pytest`

`pip install -U doubles`

To run the tests, from the root directory of the project simply run `pytest`.

For all PyTest command line options, run `pytest -h`.
