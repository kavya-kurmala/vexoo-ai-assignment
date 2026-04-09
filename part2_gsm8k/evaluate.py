def evaluate(predictions, references):
    correct = 0

    for p, r in zip(predictions, references):
        if p.strip() == r.strip():
            correct += 1

    accuracy = correct / len(predictions)
    return accuracy
