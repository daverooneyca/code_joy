# Code Joy
A port of [@DocOnDev's Code Joy](https://github.com/DocOnDev/team_joy) to Python

Example of git hooks for measuring code joy

The `commit-msg` hook will reject commits that do not have a quality rating

The `post-commit` hook will post the accepted commit to the specified HTTP endpoint

# Installation
## Common
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
