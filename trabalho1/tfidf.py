from collections import defaultdict
import re
from math import log

class TFIDF:
    """
    TF-IDF class: calculates the TF-IDF score of a term in a document.
    Atributes: documents, corpus, idf, tf, tfidf
        documents: list of documents
        corpus: dictionary of terms and their frequency in the corpus
        idf: dictionary of terms and their IDF score
        tf: dictionary of terms and their TF score
        tfidf: dictionary of terms and their TF-IDF score

    Methods: add_document, build, get_tfidf
        add_document(document): adds a document to the list of documents
        build(): calculates the IDF, TF and TF-IDF scores of the terms in the corpus
        get_tfidf(term): returns the TF-IDF score of
    """
    def __init__(self):
        self.documents = []
        self.corpus = defaultdict(int)
        self.idf = defaultdict(int)
        self.tf = defaultdict(int)
        self.tfidf = defaultdict(int)

    def add_document(self, document: str, file_name: str):
        document = document.replace("\n", " ")
        document = document.replace("(", "")
        document = document.replace(")", "")
        document = document.lower()
        self.documents.append((document, file_name))

    def build(self):
        
        for file_nm, document in self.documents:
            terms = set(re.findall(r'\w+', document.lower()))
            for term in terms:
                self.corpus[term] += 1

        for term in self.corpus:
            self.idf[term] = 1 + log(len(self.documents) / self.corpus[term])

        for document, file_name in self.documents:
            terms = re.findall(r'\w+', document.lower())
            for term in terms:
                self.tf[term] = terms.count(term) / len(terms)

        for term in self.tf:
            self.tfidf[term] = self.tf[term] * self.idf[term]

    def get_tfidf(self, term):
        return self.tfidf.get(term, 0.0001)  
    
    def get_tfidf(self, term):
        return self.get_tfidf(term)
    
    

    def rank(self, query: str):
        """
        Retorna uma lista ordenada de dicionários (documento, distância) baseada na query.
        A distância para cada documento é calculada com similaridade do cosseno.
        """
        query_terms = set(re.findall(r'\w+', query.lower()))
        query_vector = defaultdict(int)
        for term in query_terms:
            query_vector[term] = query.count(term) / len(query)
        
        ranked = []
        for  document, filename in self.documents:  # Usa o nome do arquivo
            document_terms = re.findall(r'\w+', document.lower())
            document_vector = defaultdict(int)
            for term in document_terms:
                document_vector[term] = document.count(term) / len(document)
            
            dot_product = sum(query_vector[term] * document_vector[term] for term in query_terms)
            
            query_norm = sum(value**2 for value in query_vector.values()) ** 0.5
            document_norm = sum(value**2 for value in document_vector.values()) ** 0.5
            
            if query_norm == 0 or document_norm == 0:
                distance = 0
            else:
                distance = dot_product / (query_norm * document_norm)
            
            ranked.append({'document': filename, 'distance': distance})  # Usa o nome do arquivo
        
        return sorted(ranked, key=lambda x: x['distance'], reverse=True)