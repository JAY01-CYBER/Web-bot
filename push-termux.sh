#!/bin/bash
set -e

echo "📱 Termux push helper starting..."

# Ensure required packages
if ! command -v git &> /dev/null; then
    echo "⬇️ Installing git..."
    pkg install git -y
fi

if ! command -v gh &> /dev/null; then
    echo "⬇️ Installing GitHub CLI..."
    pkg install gh -y
fi

# Ask for storage access if not already granted
if [ ! -d "$HOME/storage" ]; then
    echo "⚠️ Storage not set up. Run: termux-setup-storage"
fi

# Check GitHub auth
if ! gh auth status &> /dev/null; then
    echo "🔑 You are not logged into GitHub CLI. Please run:"
    echo "    gh auth login"
    exit 1
else
    echo "✅ GitHub CLI authentication found."
fi

# Check if repo has a remote
if git remote get-url origin > /dev/null 2>&1; then
    REPO_URL=$(git remote get-url origin)
    echo "🔗 Found existing remote: $REPO_URL"
else
    echo "🔗 No remote found. Enter your GitHub repo URL (e.g. https://github.com/JAY01-CYBER/Web-bot.git):"
    read REPO_URL
    git remote add origin $REPO_URL
fi

# Ask for branch
echo "🌿 Enter branch name to push (default: main):"
read BRANCH
BRANCH=${BRANCH:-main}

echo "🚀 Preparing repo..."
git checkout -b $BRANCH || git checkout $BRANCH

echo "📦 Adding files..."
git add .

echo "💬 Committing..."
git commit -m '📱 Termux push: Updated project' || echo "⚠️ No changes to commit."

echo "⬆️ Pushing to GitHub..."
git push -u origin $BRANCH --force

echo "✅ Push completed from Termux!"
