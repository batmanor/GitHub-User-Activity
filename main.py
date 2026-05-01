import sys
import requests

def print_help():
    print(
"""GitHub Issues CLI

Usage:
  script.py <username> [repo]
  script.py --help

Examples:
  script.py torvalds
  script.py torvalds linux

Description:
  If no repository is provided, the script will fetch general user data.
  If a repository is provided, it will fetch issues for that repository.
""")
    sys.exit(0)
    
def check_for_args(args: list[str]):
    params = ("-h", "--help")
    if any(arg in params for arg in args):
         print_help()
    for arg in args:
        if arg[0] == '-' and arg not in params:
            print('param not known, use -h or --help to learn more.')
            sys.exit(0)
    
def get_input()-> str:
    '''Reads input from stdin and returns the second argument (GitHub user since the first argument is the script name) if it exists.'''
    args = sys.argv
    length: int = len(args)
    if length == 1:
        print_help()
    
    if length > 1:
        check_for_args(args)
        
    if length > 3:
        sys.exit("Too much arguments provided")

    return args[1]

def test(res):
    if res.status_code == 404:
        print("404 Error: Resource not found")
        sys.exit(1)

    if res.status_code != 200:
        print(f"Error: {res.status_code}")
        sys.exit(1)

def process_github_user(username: str):
    url = f'https://api.github.com/users/{username}/events'
    
    res = requests.get(url)
    test(res)

    data = res.json()

    print("Output:")
    counter = {}

    for event in data:
        handle_event(event, counter)
    
    return counter


def handle_event(event: dict, counter: dict):
    repo = event['repo']['name']
    etype = event['type']
    payload = event.get('payload', {})
    counter[etype] = counter.get(etype, 0) + 1

    if etype == "PushEvent":
        created_at = event.get('created_at', 'unknown time')
        ref = payload.get('ref', 'unknown branch')
        print(f"- Pushed to {repo} on {ref} at {created_at}")

    elif etype == "IssuesEvent":
        action = payload.get('action', 'did something')
        print(f"- {action.capitalize()} an issue in {repo}")

    elif etype == "WatchEvent":
        print(f"- Starred {repo}")

    elif etype == "ForkEvent":
        print(f"- Forked {repo}")

    elif etype == "CreateEvent":
        ref_type = payload.get('ref_type', 'item')
        print(f"- Created a {ref_type} in {repo}")

    else:
        print(f"- Did {etype} in {repo}")
    
def main():
    user:str = get_input()
    print('\nUser: '+user+'\n')
    events = process_github_user(user)
    
    print()
    print('-'*20)
    for key, val in events.items():
        print(f"{key}: {val}")
        print('-'*20)
    print()

if __name__ == "__main__":
    main()
