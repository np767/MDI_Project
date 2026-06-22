1. CREATE PROJECT WEBSITE
quarto create-project --type website

2. INITIALIZE GIT
git init

3. ADD REMOTE CHANGES
git add .
git commit -m "initial commit"

4. PUSH REMOTE CHANGES
git remote add origin https://github.com/your-username/my-research-project.git
git branch -M main
git push -u origin main

5. GO LIVE ON GITHUB PAGES
quarto publish gh-pages