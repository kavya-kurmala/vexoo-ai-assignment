def sliding_window(text, window_size=150, overlap=50):
    chunks = []
    start = 0

    while start < len(text):
        end = start + window_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += window_size - overlap

    return chunks
