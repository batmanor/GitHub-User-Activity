# GitHub User Activity CLI

https://roadmap.sh/projects/github-user-activity

A simple command-line interface (CLI) tool that fetches and displays the recent public activity of a GitHub user using the GitHub API.

## Features

* Fetch recent public events for a GitHub user
* Display activity in a readable format (pushes, issues, stars, forks, etc.)
* Summarize event types with counts
* Handle errors such as invalid usernames or API failures
* Minimal dependencies (`requests` only)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/github-user-activity.git
```

### 2. Navigate into the project

```bash
cd github-user-activity
```

### 3. Install dependencies

```bash
pip install requests
```

## Usage

```bash
python main.py <username>
```

### Example

```bash
python main.py torvalds
```

## Example Output

```text
User: torvalds

Output:
- Pushed to torvalds/linux on refs/heads/master at 2025-01-01T12:00:00Z
- Opened an issue in torvalds/subsurface
- Starred torvalds/git

--------------------
PushEvent: 3
--------------------
IssuesEvent: 1
--------------------
WatchEvent: 1
--------------------
```

## Supported Event Types

* PushEvent
* IssuesEvent
* WatchEvent (stars)
* ForkEvent
* CreateEvent
* Other events (fallback message)

## Error Handling

* Displays an error if the user does not exist (404)
* Handles unexpected API errors
* Validates CLI arguments

## Help

```bash
python main.py --help
```

## Requirements

* Python 3.x
* `requests`

## Notes

* Only public GitHub activity is available
* Results are limited to the most recent events returned by the GitHub API
