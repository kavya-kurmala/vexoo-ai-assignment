from ingestion import sliding_window
from pyramid import KnowledgePyramid
from retriever import retrieve

# Load text
with open("sample.txt", "r") as f:
    text = f.read()

# Step 1: Chunking
chunks = sliding_window(text)

# Step 2: Build pyramid
kp = KnowledgePyramid()
pyramid = kp.build(chunks)

# Step 3: Query
query = input("Ask something: ")
result = retrieve(query, pyramid)

print("\nBest Answer:")
print(result)
