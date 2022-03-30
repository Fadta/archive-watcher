import os
from io import FileIO


def ensure_default_watchlist():
    """Ensures that a default watchlist exists,
    creating it if it doesn't exist

    Returns:
        (bool): True if it existed, False if it was created

    Raises:
        FileNotFoundError: if file didn't exist and couldn't be created
    """
    pass


def expand_path(path: str) -> str:
    """ensures a path is absolute

    Parameters:
        path (str): path, can be absolute or relative

    Returns:
        (str): if $path is already absolute returns $path,
            else it will try to expand it as a relative path,
            if it fails raises an exception

    Raises:
        PathNotFoundException: if the expanded relative path does not exist

    Complexity:
        Temporal: O(1)
    """
    if(os.path.isabs(path)):
        return path
    else:
        return os.path.abspath(
            os.path.join(
                os.getcwd(), path
            )
        )        


def search_and_delete_line(file: str, to_delete: str):
    """Create a temporal copy of $file were all lines will be
    copied BUT the line that is $to_delete.
    Once all data is copied the temporal file is dumped in $file
    and it is deleted (the temporal file)

    Parameters:
        file (str): filepath where to search and remove
        to_delete (str): text to remove in $file

    Returns:
        None

    Complexity:
        Temporal: O(n) to $file
    """
    tmp_file = file + ".tmp"
    with open(file, "r") as fin:
        with open(tmp_file, "w") as fout:
            for line in fin:
                if line.strip("\n") != to_delete:
                    fout.write(line)

    os.replace(tmp_file, file)
    os.remove(tmp_file)
