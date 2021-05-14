# buppy
With this module you can make a backup copy of your main file in which you write code.
https://pypi.org/project/buppy/

# install
pip install buppy

# update
pip install buppy --upgrade

# use
from buppy import Backup

(your code)

Backup.result("filename", "extension")

# definitions
filename - file name without extension

extension - backup file extension(txt, ini, py)
