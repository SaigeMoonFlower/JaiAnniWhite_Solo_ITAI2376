class RAG:
    def __init__(self, docs):
        self.docs = [d.strip() for d in docs.split("\n") if d.strip()]

    def retrieve(self, query):
        query_words = set(query.lower().split())

        best_doc = ""
        best_score = 0

        for doc in self.docs:
            doc_words = set(doc.lower().split())
            score = len(query_words.intersection(doc_words))

            if score > best_score:
                best_score = score
                best_doc = doc

        if best_doc:
            return best_doc

        return "Computer science is the study of programming and problem solving."