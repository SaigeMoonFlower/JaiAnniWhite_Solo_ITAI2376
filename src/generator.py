class Generator:
    def __init__(self):
        pass

    def generate(self, task, context=None):
        task_clean = task.lower().strip()

        # QUESTION HANDLING
        if (
            "what is" in task_clean
            or "who is" in task_clean
            or task_clean.endswith("?")
            or task_clean.startswith("explain")
        ):
            return self._answer(context)

        # QUIZ HANDLING
        if "quiz" in task_clean:
            return self._quiz()

        # SUMMARY HANDLING
        if "summarize" in task_clean:
            return (
                "Artificial intelligence is a field of computer science focused on building systems "
                "that can perform tasks requiring human intelligence such as learning, reasoning, and problem solving."
            )

        return "I can help with questions, quizzes, and summaries."

    def _answer(self, context):
        if context and context.strip():
            return context
        return "I could not find relevant information in the knowledge base."

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