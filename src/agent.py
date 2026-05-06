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

        return self.generator.generate(intent, context)


if __name__ == "__main__":
    agent = StudyAgent()

    print("CS Study Assistant Ready")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        print("Bot:", agent.run(user_input))