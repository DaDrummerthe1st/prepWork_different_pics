import pandas as pd
import numpy as np

from Dictionaries.DrawStreamlitPack.findFiles import SearchFilesToUse
from Dictionaries.DrawStreamlitPack import picture_chooser

first = SearchFilesToUse()
print(first.search_equivalent_files())



