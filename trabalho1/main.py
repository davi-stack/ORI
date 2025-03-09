import sys
import os
from tfidf import TFIDF


def main():
    model = TFIDF()
    for file in os.listdir('docs'):
        with open(f'docs/{file}', 'r') as f:
            # print(f"Adding document {file}")
            model.add_document(f.read(), file)
    model.build()
    query = input("Digite a query: ")
    rank = model.rank(query)
    for i, doc in enumerate(rank):
        print(f"{i+1} - {doc['document']} - {doc['distance']}")





if __name__ == '__main__':
    main()