class Question:
    def __init__(self, question: str, options: list[str], correct: bool):
        self.question = question
        self.options = options
        self.correctAnswer = correct

    def show(self):
        lines = '\t' + ("-" * len(self.question)) + "----"
        print(f"{lines}\n\t| {self.question} |\n{lines}")

        for  index,option in enumerate(self.options):
            print(f"\t| {index}. {option} \t\t|")
    
        print(lines)

    def verifyOption(self, option: int) -> bool:
        if option == self.correctAnswer:
            return True
        return False