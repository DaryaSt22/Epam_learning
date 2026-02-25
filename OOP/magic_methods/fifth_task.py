# Create a context manager TempDir (Use Context Manager protocol - methods __enter__, __exit__):
#
# When entering the context, a new temporary directory is created with random, unique name. Use os.mkdir to create the directory.
# Until exiting this context the new created directory becomes current one and all actions are executed in scope of this new directory.
# When exiting this context, the temporary directory is removed with all files in it. Use rmtree from shutil to remove whole directory.
# The new working directory becomes the same as before entering context.


import os
import shutil

class TempDir:
    pass
    # TODO: please ad your code here