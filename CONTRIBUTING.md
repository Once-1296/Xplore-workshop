🤝 CONTRIBUTING.md
# Contributing Guidelines

This guide explains how students should solve exercises and submit their solutions properly.

## 🛠️ Steps to Submit Your Solutions

### 1️⃣ Fork the Repository

Fork this repository to your own GitHub account.

### 2️⃣ Clone Your Fork
```
git clone https://github.com/<your-username>/CoC-git-python-workshop.git
cd CoC-git-python-workshop
```
### 3️⃣ Create Your Solutions Folder

Inside the repository, create a top-level folder named:
```
<githubid>_solutions
```
📌 Example:

`aswadekarb24-code_solutions/`

### 4️⃣ Copy the Playground

Copy the entire `test_playground` directory into your solutions folder:
```
<githubid>_solutions/
└── test_playground/
```

⚠️ Do not modify the original test_playground directory or any file/dircetory outside your copied directory.

### 5️⃣ Set Up Virtual Environment

Create a virtual environment using Python 3.12.0 (important to avoid conflicts):
```
python3.12 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```
Install dependencies:
```
pip install -r requirements.txt
```

### 6️⃣ Implement Your Fixes & Enhancements

- Make all changes only inside your `<githubid>_solutions` folder

- Fix bugs in the copied files

- You may also:

  - Add your own Python scripts

  - Showcase something new you learned

  - Implement alternative or improved solutions

7️⃣ Commit & Open a Pull Request

```
git add .
git commit -m "Fix: completed basics and intermediate exercises"
git push origin main
```

- Open a Pull Request (PR) to the upstream repository

- Follow the PR format provided in the repository

## ✅ Important Rules

- ❌ Do NOT edit original tutorial or playground files

- ✅ Work only inside your solutions folder

- ✅ Keep code clean and readable

- ✅ Use meaningful commit messages

## 🎉 Final Note

This repository is meant to help you:

- Learn Python deeply

- Improve debugging skills

- Gain confidence with real code

- 💡 Experiment, break things, fix them, and enjoy the process!

**Happy coding! 🐍✨**