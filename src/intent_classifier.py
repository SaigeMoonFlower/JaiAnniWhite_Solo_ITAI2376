class IntentClassifier:
    def predict(self, text):
        text = text.lower()

        if "quiz" in text:
            return "quiz"

        if "summarize" in text:
            return "summarize"

        if "what is" in text or "who is" in text or "?" in text:
            return "question"

        return "other"