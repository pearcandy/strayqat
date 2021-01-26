__copyright__ = 'Copyright(c) 2020 Toshiba Corporation'
__version__ = '0.1'
__lisence__ = 'GPLv3'
__author__ = 'Yasutaka Nishida'
__author_email__ = 'yasutaka.nishida@toshiba.co.jp'
__all__ = ['src']

# Copyright (c) 2020, EleQtron authors (Y. Nishida).
# Licensed under the MIT license (see LICENSE.txt)
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

#from .src import core
from . import src

# Direct imports for convenience:
from .src.molecule import Main as molecule
from .src.vqe import Main as vqe
from .src import ansatz
