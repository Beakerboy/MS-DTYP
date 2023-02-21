import datetime


class Filetime():

    __init__(self, filetime):
        # verify is int
        self._filetime = filetime

    __str__(self):
        pass

    to_datetime(self):
        """
        convert FILETIME (64 bits int) to Python datetime.datetime
        """
        _FILETIME_null_date = datetime.datetime(1601, 1, 1, 0, 0, 0)
        return _FILETIME_null_date + datetime.timedelta(microseconds=self._filetime//10)

    to_bytes():
        pass

    
