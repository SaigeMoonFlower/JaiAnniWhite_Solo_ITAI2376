from intent_classifier import IntentClassifier
from rag import RAG
from generator import Generator


class StudyAgent:
    def __init__(self):
        with open("../data/knowledge_base.txt", "r", encoding="utf-8") as f:
            docs = f.read()

        self.intent = IntentClassifier()
        self.rag = RAG(docs)
        self.generator = Generator()

    def run(self, user_input):
        intent = self.intent.predict(user_input)
        context = self.rag.retrieve(user_input)

        if intent == "question":
            task = user_input

        elif intent == "quiz":
            task = "quiz"

        elif intent == "summarize":
            task = "summarize"

        else:
            task = user_input

        return self.generator.generate(task, context)


if __name__ == "__main__":
    agent = StudyAgent()

    print("CS Study Assistant Ready")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        print("Bot:", agent.run(user_input))