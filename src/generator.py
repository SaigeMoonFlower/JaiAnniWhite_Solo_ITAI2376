class Generator:
    def generate(self, task, context):

        task = task.lower()

        if "quiz" in task:
            return self.quiz(context)

        if "summarize" in task:
            return self.summarize(context)

        return self.answer(context)

    def answer(self, context):
        return f"Answer: {context}"

    def summarize(self, context):
        return (
            "Summary:\n"
            "- " + context + "\n"
            "- Key CS concept\n"
            "- Important for understanding programming"
        )

    def quiz(self, context):
        return (
            "Quiz:\n"
            f"What is the topic?\n"
            f"A. {context}\n"
            "B. Incorrect\n"
            "C. Unrelated\n"
            "D. None\n"
            "Answer: A"
        )