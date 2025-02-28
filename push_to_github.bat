@echo off
echo Pushing changes to GitHub repository...

git add .
git commit -m "Enhanced OmnitrAIce with agent customization UI and comprehensive documentation"
git push origin main

echo Done!
pause