class IntentClassifier:
    def predict(self, text):
        text = text.lower()

        if "quiz" in text:
            return "quiz"
        elif "summarize" in text:
            return "summarize"
        else:
            return "question"