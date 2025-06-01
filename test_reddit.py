"""Testing the functions in reddit_project.py"""
import reddit_project
from reddit_project import recipes_subreddit


def test_gets_post():
    """
    Tests the gets_post function from reddit_project.py file
    """
    assert (reddit_project.gets_post("pie", recipes_subreddit) == "qzphy2"), \
        "Does not work for correct combination"
    assert (reddit_project.gets_post("pie", recipes_subreddit) != "12345"), \
        "Does not work for incorrect combination"


def test_gets_image():
    """
    Tests the gets_image function from reddit_project.py file
    """
    assert (reddit_project.gets_image("qzphy2", "pie") == "pie.jpg"), \
        "Failed the correct naming of download"
    assert (reddit_project.gets_image("qzphy2", "pie") != "not_pie.jpg"), \
        "Failed the incorrect naming of download"
