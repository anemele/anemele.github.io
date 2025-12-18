@echo off

git checkout -b main
git merge dev
git push origin main
git checkout -b dev
