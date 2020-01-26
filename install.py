import os
import shutil

home = os.path.expanduser('~/')

shutil.copytree("./cats", "{}.cats".format(home))
