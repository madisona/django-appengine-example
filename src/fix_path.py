
import sys
from os.path import abspath, dirname, join

# add third party directory to path.
LIB_DIR = abspath(join(dirname(__file__), 'lib'))
if LIB_DIR not in sys.path:
    sys.path.insert(0, LIB_DIR)
