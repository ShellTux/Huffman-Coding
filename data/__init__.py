from .data import Data
from numpy import uint16
import os

root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
file_path = os.path.join(root, 'assets', 'CarDataset.xlsx')
DATA = Data(file_path, dataType = uint16)
