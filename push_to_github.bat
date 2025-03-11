@echo off
echo Pushing changes to GitHub repository...

git add -A
git commit -m "Complete project reorganization with enhanced documentation and Web UI (v1.1.0)"
git push origin master

echo Done!
pause
