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

from .molecule import Main as Molecule
from .vqe import Main as Vqe
from . import ansatz
