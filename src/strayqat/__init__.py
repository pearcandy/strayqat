__copyright__ = 'Copyright(c) 2020 PearCandy'
__version__ = '0.2'
__lisence__ = 'GPLv3'
__author__ = 'PearCandy'
__author_email__ = 'y.nishi1980@gmail.com'
__all__ = ['src']

# Licensed under the GPLv3
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from .molecule import Main as Molecule
from .vqe import Main as Vqe
from . import ansatz
