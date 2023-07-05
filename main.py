#add interface to either type in the name of the desired file or print by difficulty
#
#
from os.path import dirname, basename, isfile, join
import glob



modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith("__init__.py")]

module = 'Reverse_Bits.py'

from Easy import Reverse_Bits as r

print(module.Solution().solve())