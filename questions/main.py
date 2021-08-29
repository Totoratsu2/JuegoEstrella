import json
from typing import TypedDict
from os import path, getcwd, walk


def getQuestions() -> list[TypedDict]:
    directory = path.join(getcwd(), 'questions', 'all')
    questionFiles: list[TypedDict] = []

    for __, _, files in walk(directory):
        for file in files:
            questionFile = open(path.join(directory, file))
            data: TypedDict = json.load(questionFile)
            questionFile.close()

            questionFiles.append(data)

    return data