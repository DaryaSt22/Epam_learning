# Implement a custom dictionary that will memorize the 5 latest changed keys. Using method "get_history" return these keys.
#
# Example:
#
# >>> d = HistoryDict({"foo": 42})
# >>> d.set_value("bar", 43)
# >>> d.get_history()
#
# ["bar"]

class HistoryDict:

    def __init__(self, *args, **kwargs):
        self._data = {}
        self._history = []
        if args or kwargs:
            self._data.update(*args, **kwargs)

    def set_value(self, key, value):
        self._data[key] = value
        self._history.append(key)
        if len(self._history) > 5:
            self._history.pop(0)

    def get_history(self):
        return self._history