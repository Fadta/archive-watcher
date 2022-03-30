class ArchiverException(BaseException):
    pass

class WatchlistException(ArchiverException):
    pass

class PathException(ArchiverException):
    pass

class WatchlistNotFoundException(WatchlistException):
    pass

class WatchlistExistsException(WatchlistException):
    pass

class PathNotFoundException(PathException):
    pass

class UnwatchablePathException(PathException):
    pass
