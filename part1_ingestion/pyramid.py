class KnowledgePyramid:
    def __init__(self):
        self.data = []

    def summarize(self, text):
        return text[:80]  # simple placeholder

    def categorize(self, text):
        text = text.lower()
        if "ai" in text or "model" in text:
            return "Technology"
        elif "finance" in text:
            return "Finance"
        return "General"

    def distill(self, text):
        words = text.split()
        return list(set(words))[:8]

    def build(self, chunks):
        for chunk in chunks:
            entry = {
                "raw": chunk,
                "summary": self.summarize(chunk),
                "category": self.categorize(chunk),
                "distilled": self.distill(chunk)
            }
            self.data.append(entry)

        return self.data
