#!/bin/bash
# Manually publish the qDiff site to the gh-pages branch.

set -e

echo "Building qDiff website..."

mkdir -p temp_deploy
cd temp_deploy

echo "Building documentation..."
cd ..
pnpm docs:build
cd temp_deploy

if [ ! -d "../docs/.vitepress/dist" ]; then
        echo "Build failed: dist directory missing"
        exit 1
fi

echo "Preparing gh-pages branch..."
ORIGIN_URL=$(git -C .. remote get-url origin 2>/dev/null || true)
if [ -n "$ORIGIN_URL" ]; then
    git clone --depth 1 -b gh-pages --single-branch "$ORIGIN_URL" gh-pages || git clone "$ORIGIN_URL" gh-pages
    cd gh-pages
else
    git init gh-pages
    cd gh-pages
    git checkout -b gh-pages
fi

git config user.name "GitHub Actions"
git config user.email "actions@github.com"

echo "Cleaning previous build..."
rm -rf $(find . -maxdepth 1 ! -name .git ! -name .)

echo "Copying built files..."
cp -rf ../../docs/.vitepress/dist/* .
echo "qdiff.w3cub.com" > CNAME

git add -A .
if git diff --staged --quiet; then
        echo "No changes to commit"
else
        git commit -m "Deploy qDiff website

Built from $(git -C .. rev-parse --short HEAD 2>/dev/null || echo local)
Deployed on $(date -u +'%Y-%m-%d %H:%M:%S UTC')"
fi

if [ -n "$ORIGIN_URL" ]; then
        echo "Pushing to gh-pages..."
        git push origin gh-pages
else
        echo "No remote origin found; add one and push gh-pages manually."
fi

cd ../..
rm -rf temp_deploy

echo "Done: https://qdiff.w3cub.com/"
