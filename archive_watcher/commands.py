import os
import os.path
import app_constants as archiver
import utils
from app_exceptions import WatchlistNotFoundException, UnwatchablePathException, WatchlistExistsException

def watch(watched_path: str, watchlist_name: str=archiver.DEFAULT_WATCHLIST):
    """Adds a path to a watchlist

    Parameters:
        watched_path (str): path of the file/directory that is going to be watched
        watchlist_name (str): name of the watchlist to add the watched_path

    Returns:
        None

    Raises:
        WatchlistNotFoundException: If a watchlist with $watchlist_name is not found 
        UnwatchablePathException: If $watched_path does not exist

    Complexity:
        Temporal: O(1)
    """
    watchlist_path = utils.get_watchlist_path(watchlist_name)
    watched_path = utils.expand_path(watched_path)

    if(not os.path.exists(watchlist_path)):
        raise WatchlistNotFoundException(f"watchlist {watchlist_name} does not exist")

    elif not os.path.exists(watched_path):
        raise UnwatchablePathException(f"Path {watched_path} does not exist")

    else:
        path_to_append = watched_path + "\n"
        with open(watchlist_path, "a") as watchlist:
            watchlist.write(path_to_append)

def unwatch(watched_path: str, watchlist_name: str=archiver.DEFAULT_WATCHLIST):
    """Removes a path from a watchlist

    Parameters:
        watched_path (str): path of the file/directory that is going to be watched
        watchlist_name (str): name of the watchlist to add the watched_path

    Returns:
        None

    Raises:
        WatchlistNotFoundException: If a watchlist with $watchlist_name is not found 

    Complexity:
        Temporal: O(n)
    """
    watchlist_path = utils.get_watchlist_path(watchlist_name)
    watched_path = utils.expand_path(watched_path)

    if(not os.path.exists(watchlist_path)):
        raise WatchlistNotFoundException(f"watchlist {watchlist_name} does not exist")

    elif not os.path.exists(watched_path):
        raise UnwatchablePathException(f"Path {watched_path} does not exist")

    else:
        # O(n)
        utils.search_and_delete_line(watchlist_path, watched_path)


def create_watchlist(watchlist_name: str):
    """Creates a watchlist with a given name

    Parameters:
        watchlist_name (str): watchlist name to create

    Returns:
        None

    Raises:
        WatchlistExistsException: if the given name is already taken by other watchlist

    Complexity:
        Temporal: O(1)
    """
    watchlist_path = utils.get_watchlist_path(watchlist_name)

    if os.path.exists(watchlist_path):
        raise WatchlistExistsException(f"{watchlist_name} already exists")

    open(watchlist_path, "a").close()
    
    


def delete_watchlist(watchlist_name: str):
    """Deletes a watchlist with a given name

    Parameters:
        watchlist_name (str): watchlist name to delete

    Returns:
        None

    Raises:
        WatchlistNotFoundException: If a watchlist with $watchlist_name is not found 
        
    Complexity:
        Temporal: O(1)
    """
    watchlist_path = utils.get_watchlist_path(watchlist_name)

    if not os.path.exists(watchlist_path):
        raise WatchlistNotFoundException(f"{watchlist_name} does not exist")

    os.remove(watchlist_name)


def enumerate_watchlists() -> list[str]:
    """Gets all the existent watchlists 

    Returns:
        list[str]: strings of existent 0-depth files at $WATCHLIST_FOLDER

    Complexity:
        Temporal: O(n)
    """
    # O(n)
    watchlists = [watchlist for _, _, watchlist in os.walk(archiver.WATCHLIST_FOLDER)]

    surface_watchlists = watchlists[0]

    return surface_watchlists


def enumerate_watched(watchlist_name: str=archiver.DEFAULT_WATCHLIST) -> list[str]:
    """Gets all the watched paths in a watchlist

    Parameters:
        watchlist_name (str): watchlist to search for watched files

    Returns:
        list: string of absolute paths of watched files

    Raises:
        WatchlistNotFoundException: if a watchlist with the given name doesn't exist

    Complexity:
        Temporal: O(n)
    """
    watchlist_path = utils.get_watchlist_path(watchlist_name)

    if(os.path.exists(watchlist_path)):
        lines = []

        with open(watchlist_path, "r") as watchlist:
            # O(n)
            lines = [x.strip("\n") for x in watchlist.readlines()]

        return lines

    else:
        raise WatchlistNotFoundException(f"Watchlist {watchlist_name} doesn't exist")


def watched2disk(watchlist_name: str, backup_folder_apath: str, unwatch_deleted_paths: bool=False):
    """Explores the watched paths in a watchlist and creates copies on a backup folder

    Parameters:
        watchlist_name (str): watchlist to search for watched files
        backup_folder_apath (str): destination folder where copies will go
        unwatch_deleted_paths (bool): if set to True, it will unwatch deleted paths
            if set to false, it will raise an Error if a path does not exist

    Returns:
        None

    Raises:
        FileNotFoundError: if unwatch_deleted_paths=False and a path was not found
    """
    pass
