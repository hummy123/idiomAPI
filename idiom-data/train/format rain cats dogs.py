from pyexcel_ods3 import get_data
from itertools import chain
from collections import OrderedDict
from pathlib import Path
import os

sentences = get_data("training dataset.ods", start_column=0, column_limit=1)
senList = list(chain.from_iterable(sentences['Sheet1']))

category = get_data("training dataset.ods", start_column=1, column_limit=1)
catList = list(chain.from_iterable(category['Sheet1']))

for counter in range(len(senList)):
    if not os.path.exists(catList[counter]):
        os.makedirs(catList[counter])
    curPath = catList[counter] + "/" + str(counter) + ".txt"
    curFile = open(curPath, "w")
    curFile.write(senList[counter])
    curFile.close()