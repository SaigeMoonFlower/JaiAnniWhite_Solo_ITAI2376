class Generator:
    def __init__(self):
        pass

    def generate(self, task, context=None):
        task = task.lower()

        if "explain" in task or "what is" in task:
            return self._answer(context)

        if "quiz" in task:
            return self._quiz()

        if "summarize" in task:
            return (
                "Artificial intelligence is a field of computer science focused on building systems "
                "that can perform tasks requiring human intelligence such as learning, reasoning, and problem solving."
            )

        return "I can help with questions, quizzes, and summaries."

    def _answer(self, context):
        if context:
            return context
        return "I do not have enough information to answer that."

    def _quiz(self):
        return """
What is Python commonly used for?

A. Artificial intelligence, web development, and automation  
B. Only hardware repair  
C. Video editing only  
D. Network cabling only  

Correct answer: A


Which of the following is a Python data type?

A. String  
B. Screen  
C. Mouse  
D. Monitor  

Correct answer: A


What does AI stand for?

A. Artificial Intelligence  
B. Automated Interface  
C. Active Internet  
D. Advanced Input  

Correct answer: A
"""