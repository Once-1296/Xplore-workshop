CoC Python Workshop

This repository contains a set of Python exercises for students to
practice after studying Python fundamentals. Exercises are organized by
level in the top-level folders: `basics/`, `intermediate/`, `advanced/`,
and `miscellaneous/`.

How students should submit solutions

1. Fork this repository to your GitHub account.
2. Clone your fork locally.
3. In the fork, create a top-level folder named `<githubid>_solutions` (replace `<githubid>` with your GitHub username).
4. Copy all exercise folders (e.g. `basics/`, `intermediate/`, `advanced/`, `miscellaneous/`) into your `<githubid>_solutions/` folder.
5. Implement your fixes and solutions inside your copied folder only.
6. Commit your changes, push the branch, and open a PR against the upstream repository.

Notes for maintainers / instructors

- There is a small dataset generator at `assets/generate_datasets.py`. Run it to create sample CSVs used by some exercises:

    python assets/generate_datasets.py

- Student-facing files avoid leaking assistant-only comments. The original instructor notes were removed and replaced with short exercise descriptions and function stubs.

- Keep solution folders separate from upstream exercises. Example: `yourid_solutions/`.

Quick tips

- Use `python -m pip install -r requirements.txt` if you add dependencies. This repo intentionally uses only standard library code in the generator script so students can run it without installing packages.
- Encourage students to add unit tests in their `<githubid>_solutions` folder and to run them locally before opening a PR.

If you want, I can also:
- Add minimal unit tests for each exercise (happy path + one edge case).
- Add a GitHub Actions workflow that runs tests on PRs.

Have fun teaching and learning!
