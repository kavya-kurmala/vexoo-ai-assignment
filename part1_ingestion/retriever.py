from difflib import SequenceMatcher

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

def retrieve(query, pyramid):
    best_score = 0
    best_answer = ""

    for item in pyramid:
        for key in item:
            value = str(item[key])
            score = similarity(query.lower(), value.lower())

            if score > best_score:
                best_score = score
                if key == "raw" or key == "summary":
                    best_answer = value


    return best_answer
