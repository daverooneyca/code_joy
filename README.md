# Code Joy
A port of [@DocOnDev's Code Joy](https://github.com/DocOnDev/team_joy) to Python

Example of git hooks for measuring code joy

The `commit-msg` hook will reject commits that do not have a quality rating

The `post-commit` hook will post the accepted commit to the specified HTTP endpoint

# Installation
## Linux, macOS
- copy the contents of the `src` directory to the `.git/hooks` directory in any repository for which you want to use these hooks
- rename `commit-msg.py` to `commit-msg`
- rename `post-commit.py` to `post-commit`
- ensure both of those scripts are executable by running:
	- `chmod +x commit-msg`
	- `chmod +x post-commit`

## Windows
- rename `commit-msg-windows.py` to `commit-msg`
- rename `post-commit-windows.py` to `post-commit`
- change the first line of each of those scripts, depending on the location of the Python executable on your system
	- the default is `#!%userprofile%\AppData\Local\Microsoft\WindowsApps\python.exe`
## Python Libraries
CodeJoy doesn’t require any libraries outside of core Python
