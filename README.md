# Reddit Recipe Project

This Python project uses the Reddit API to search for recipes, extract instructions from comments, and downloads images from posts. It uses the Python Reddit API Wrapper (`praw`) and the `requests` library to interact with Reddit and handle HTTP requests.

## Features
1. **Search for Recipes**: Looks at the `recipes` subreddit for posts related to specific topics, filtering posts by the "Recipe" flair.
2. **Extract Instructions**: Fetches the oldest comment from a post, assuming it contains recipe instructions.
3. **Download Images**: Downloads images from the post if its URL points to a `.jpg`, `.jpeg`, or `.png` file.

## Prerequisites
- Python 3.8 or higher.
- A Reddit account with API credentials (client ID, client secret, username, and password).
- Installed Python libraries: `praw`, `requests`.
