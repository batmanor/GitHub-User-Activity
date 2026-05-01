[text](https://roadmap.sh/projects/github-user-activity)# GitHub User Activity

A simple command-line interface (CLI) application that fetches and displays the recent activity of a GitHub user using the GitHub API.

## Features

- Fetch recent public events for a specific GitHub user.
- Display activity in a readable format (e.g., "Pushed 3 commits to repository-name").
- Handle errors such as invalid usernames or API connection issues.

## How to Use

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/github-user-activity.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd github-user-activity
   ```
3. **Run the application:**
   ```bash
   # Example for Node.js
   node index.js <username>
   
   # Example for Python
   python main.py <username>
   ```

## Example Output

```text
$ github-activity kamranahmedse
- Pushed 3 commits to kamranahmedse/gopher-konf-2023
- Opened a new issue in kamranahmedse/developer-roadmap
- Starred kamranahmedse/tooling-report
```

## Project Requirements

- No external libraries for HTTP requests (use built-in modules like `http` in Node.js or `urllib` in Python).
- Proper error handling for non-existent users.
- Clean and modular code structure.
