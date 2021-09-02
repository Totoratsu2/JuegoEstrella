import json
from typing import TypedDict
from questions.Question import Question

from os import path, getcwd, walk


def organizeQuestions(raw: TypedDict):
    questionList = []

    for _, values in raw.items():
        question = Question(values["question"], values["options"],
                            values["correctAnswer"])
        questionList.append(question)

    return questionList


def getQuestions() -> list[Question]:
    directory = path.join(getcwd(), 'questions', 'all')
    questionList = []

    for __, _, files in walk(directory):
        for file in files:
            questionFile = open(path.join(directory, file), encoding='utf-8')
            data: TypedDict = json.load(questionFile)
            questionFile.close()

            questionList.extend(organizeQuestions(data))

    return questionList
