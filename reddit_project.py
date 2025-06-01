# pylint: disable=import-error
"""
Imports the necessary libraries for the project:
praw: Python Reddit API Wrapper, used to interact with Reddit's API
requests: A library for making HTTP requests, used for downloading images from Reddit post URLs
"""
import praw
import requests

reddit = praw.Reddit(
    client_id="uozn3OB7ghyx5gWOLG3YaQ",
    client_secret="aIRFp6lY5yHXBXeNMpwiMpIr6E5F7w",
    password="Straberry1",
    user_agent="macOS:reddit_project:1.0 (by /u/drexj10)",
    username="drexj10",
)
reddit_topics = ["christmas", "fruitcake", "meatloaf", "new year's", "pie"]
recipes_subreddit = reddit.subreddit("recipes")


def gets_post(topic, subreddit):
    """
    Searches for a post in the specified subreddit related to the given topic.

    Parameters:
        topic (str): The topic or keyword to search for in the subreddit.
        subreddit (praw.models.Subreddit): The subreddit object where the search is performed.

    Returns:
        str: The ID of the first post found with the "Recipe" flair.
        NoneType: Returns 'None' if no post are found with a 'Recipe' flair.
    """
    posts = subreddit.search(topic, limit=5)
    for post in posts:
        if post.link_flair_text == "Recipe":
            print("Found recipe:", post.title)
            print("URL:", post.url)
            return post.id
    return None


def gets_recipe_instructions(post_id):
    """
    Searches for the oldest comment from the specified post

        Parameters:
            post_id(str): The ID of the Reddit post to fetch.

        Returns:
            str: The Body of the oldest comment.
    """
    submission = reddit.submission(id=post_id)
    submission.comments.replace_more(limit=0)
    comments = submission.comments.list()
    sorted_comments = sorted(comments, key=lambda comment: comment.created_utc)
    oldest_comment = sorted_comments[0]
    return oldest_comment.body


def gets_image(post_id, topic):
    """ Downloads the image from a Reddit post if the post URL links to an image file.

    Parameters:
        post_id (str): The ID of the Reddit post to fetch.
        topic (str): The topic or keyword used to name the saved image file.

    Returns:
        str: The filename of the saved image if successful.
        NoneType: Returns 'None' if no image is found.
    """
    post = reddit.submission(id=post_id)
    if post.url.endswith(('.jpg', '.jpeg', '.png')):
        file_name = topic + ".jpg"
        post_image = requests.get(post.url)
        with open(file_name, 'wb') as file:
            file.write(post_image.content)
        return file_name
    print("No image found for post:" + post.title)
    return None

def main():
    """
    The main function of the project.
    """
    for topic in reddit_topics:
        print()
        print("#" * 50)
        print()
        print("Topic:", topic)
        post_id = gets_post(topic, recipes_subreddit)
        if not post_id:
            print("No valid post found for topic:" + topic)
        else:
            print(gets_recipe_instructions(post_id))
            print("Image downloaded as: " + gets_image(post_id, topic))

if __name__ == "__main__":
    main()
