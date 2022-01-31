# IMPORTANT: Run this script from the root of the repository

# Copy all Python files to the git hooks directory
cp ./src/*.py ./.git/hooks

# Remove the extension from the hook scripts (Git convention)
mv ./.git/hooks/commit-msg.py ./.git/hooks/commit-msg
mv ./.git/hooks/post-commit.py ./.git/hooks/post-commit

# Ensure that the hook scripts are executable
chmod +x ./.git/hooks/commit-msg
chmod +x ./.git/hooks/post-commit
