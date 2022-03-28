import os
import app_constants as archiver
from app_exceptions import WatchlistNotFoundException

def watch(watched_path: str, watchlist_name: str):
    """Adds a path to a watchlist

    Parameters:
        watched_path (str): path of the file/directory that is going to be watched
        watchlist_name (str): name of the watchlist to add the watched_path

    Returns:
        None

    Raises:
        WatchlistNotFoundException: If a watchlist with $watchlist_name is not found 
    """
    pass


def unwatch(watched_path: str, watchlist_name: str):
    """Removes a path from a watchlist

    Parameters:
        watched_path (str): path of the file/directory that is going to be watched
        watchlist_name (str): name of the watchlist to add the watched_path

    Returns:
        None

    Raises:
        WatchlistNotFoundException: If a watchlist with $watchlist_name is not found 
    """
    pass


def create_watchlist(watchlist_name: str):
    """Creates a watchlist with a given name

    Parameters:
        watchlist_name (str): watchlist name to create

    Returns:
        None
    """
    pass


def delete_watchlist(watchlist_name: str):
    """Deletes a watchlist with a given name

    Parameters:
        watchlist_name (str): watchlist name to delete

    Returns:
        None
    """
    pass


def enumerate_watchlists():
    """Gets all the existent watchlists

    Returns:
        list: strings of existent watchlist names
    """
    pass


def enumerate_watched(watchlist_name: str):
    """Gets all the watched paths in a watchlist

    Parameters:
        watchlist_name (str): watchlist to search for watched files

    Returns:
        list: string of absolute paths of watched files
    """
    pass


def watched2disk(watchlist_name: str, backup_folder_apath: str, unwatch_deleted_paths: bool = True):
    """Explores the watched paths in a watchlist and creates copies on a backup folder

    Parameters:
        watchlist_name (str): watchlist to search for watched files
        backup_folder_apath (str): destination folder where it will be copied
        unwatch_deleted_paths (bool): if set to True, it will unwatch deleted paths
            if set to false, it will raise an Error if a path does not exist

    Returns:
        None

    Raises:
        FileNotFoundError: if unwatch_deleted_paths=False and a path was not found
    """
    pass
