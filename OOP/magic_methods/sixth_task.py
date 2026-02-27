# Create a context manager Cd which changes the current directory to pointed one. For example:
#
# with Cd('/home')
# When entering the context you need to save the previous directory and when you exit you need to restore it.
# During context manager initialization check that the passed directory is a directory and exists.
# If the passed directory is not a directory or does not exist raise ValueError.
# Use the following functions from the os module: getcwd, chdir, path.isdir

import os


class Cd:
    pass

    # TODO: please add your code here

    def __init__(self, path):
        self.path = path
        if os.path.isdir(path):
            self.path = os.path.abspath(path)
        else:
            raise ValueError

    def __enter__(self):
        self._new_dir = self.path
        self._previous_dir = os.getcwd()
        os.chdir(self._new_dir)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self._previous_dir)