import sqlite3
from os import path


DEFAULT_DATABASE = path.join(path.dirname(__file__), "database.db")


def database_startup(location=DEFAULT_DATABASE):
    """Makes sure the database is in an appropritate state for the program

    Args:
      location: (optional) where on disk the database is
    """
    connection = sqlite3.connect(location)
    with connection as cursor:
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS Highscores \
            (id INTEGER PRIMARY KEY, \
             nickname TEXT, \
             score INTEGER);"
        )
    connection.close()


def database_enter_new_score(nickname, highscore, location=DEFAULT_DATABASE):
    """Adds a new score into the database

    Args:
      nickname: Name given by user for score
      highscore: score value
      location: (optional) where on disk the database is
    """

    connection = sqlite3.connect(location)
    with connection as cursor:
        cursor.execute(
            "INSERT INTO Highscores (nickname, score) VALUES (?, ?);",
            (nickname, highscore),
        )
    connection.close()


def database_get_top_scores(location=DEFAULT_DATABASE):
    """Returns ordered list of top ten high scores from database

    Args:
      location: (optional) where on disk the database is

    Returns:
      ordered list of top ten high scores as tuples (name, score)
    """

    connection = sqlite3.connect(location)
    with connection as cursor:
        values = cursor.execute(
            "SELECT nickname, score FROM Highscores \
             ORDER BY score DESC LIMIT 10;"
        )
        values = values.fetchall()
    connection.close()
    return values
