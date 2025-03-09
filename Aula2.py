from collections import defaultdict
import re
documents = {
    1: "The quick brown fox jumps over the lazy dog",
    2: "A brown fox is fast and the dog is lazy",
    3: "The sun is shining, and the weather is warm",
}

def preprocess(text):
    text = text.lower()
    tokens = re.findall(r'\w+', text)
    return set(tokens)

inverted_index = defaultdict(set)

for doc_id, text in documents.items():
    term = preprocess(text)
    for word in term:
        inverted_index[word].add(doc_id)
def query(query_text):
    terms = preprocess(query_text)
    results = set(doc_id for term in terms for doc_id in inverted_index.get(term, []))
    return results

query_result = query("brown fox")
print("Documents containing 'brown' and 'fox':", query_result)
