from pyexcel_ods3 import get_data
from itertools import chain
from collections import OrderedDict
from pathlib import Path
import os
from lxml import html

def strip_html(s):
    return str(html.fromstring(s).text_content())

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

entryNum = len(senList)
semSentences = get_data("subtask5b_en_allwords_train.ods", start_column=3, column_limit=1)
semSenList = list(chain.from_iterable(semSentences['subtask5b_en_allwords_train']))

semCategory = get_data("subtask5b_en_allwords_train.ods", start_column=1, column_limit=1)
semCatLiist = list(chain.from_iterable(semCategory['subtask5b_en_allwords_train']))

semType = get_data("subtask5b_en_allwords_train.ods", start_column=2, column_limit=1)
semTypeList = list(chain.from_iterable(semType['subtask5b_en_allwords_train']))

for counter in range(len(semSenList)):
    entryNum += 1
    curType = semTypeList[counter]
    folderName = ""
    if curType == "literally":
        folderName = "none"
    elif curType == "both":
        continue
    else:
        folderName = semCatLiist[counter]

    if not os.path.exists(folderName):
        os.makedirs(folderName)

    curSentence = strip_html(semSenList[counter])

    curPath = folderName + "/" + str(entryNum) + ".txt"
    curFile = open(curPath, 'w')
    curFile.write(curSentence)
    curFile.close()
