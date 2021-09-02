class Question:
    def __init__(self, question: str, options: list[str], correct: bool):
        self.question = question
        self.options = options
        self.correctAnswer = correct

    def show(self):
        lines = '\t' + ("-" * len(self.question)) + "----"
        print(f"\n\n{lines}\n\t| {self.question} |\n{lines}")

        for index, option in enumerate(self.options):
            optionTxt = option + "\t" if len(option) < int(
                len(self.question) * 0.75) else option + "\t\t" if len(
                    option) < int(len(self.question) * 0.4) else option

            print(f"\t|\t {index}. {optionTxt} \t\t|")

        print(lines + "\n\n")

    def verifyOption(self, option: int) -> bool:
        if option == self.correctAnswer:
            return True
        return False