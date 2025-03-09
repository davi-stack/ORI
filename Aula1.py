import math
import pandas as pd
import sklearn as sk


def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bowCount)
    return tfDict

def calculaIDF(docList):
    import math
    idfDict = {}
    N = len(docList)
    
    idfDict = dict.fromkeys(docList[0].keys(), 0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] += 1
                
    for word, val in idfDict.items():
        idfDict[word] = math.log10(N / float(val))
        
    return idfDict

def calculaTDIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val * idfs[word]
    return tfidf


frase1 = "Data Science is the sexisest job of the 21st century"
frase2 = "machine learning is the key for data science"
frase3 = "math is the only way to learn data science"
frase4 = "software engineering is one of the best jobs of the 21st century"
frase5 = "computational vision is one of the most important areas of machine learning"
frase6 = "the more important thing in data science is to learn math"
frase7 = "data science is the only way to learn machine learning"
frase8 = "system embedded is other thing you can do without data science"

#tirar minusculas
frase1 = frase1.lower()
frase2 = frase2.lower()
frase3 = frase3.lower()
frase4 = frase4.lower()
frase5 = frase5.lower()
frase6 = frase6.lower()
frase7 = frase7.lower()
frase8 = frase8.lower()

frase1 = frase1.split(" ")
frase2 = frase2.split(" ")
frase3 = frase3.split(" ")
frase4 = frase4.split(" ")
frase5 = frase5.split(" ")
frase6 = frase6.split(" ")
frase7 = frase7.split(" ")
frase8 = frase8.split(" ")

total = set(frase1).union(set(frase2)).union(set(frase3)).union(set(frase4)).union(set(frase5)).union(set(frase6)).union(set(frase7)).union(set(frase8))


wordDictA = dict.fromkeys(total, 0)
wordDictB = dict.fromkeys(total, 0)
wordDictC = dict.fromkeys(total, 0)
wordDictD = dict.fromkeys(total, 0)
wordDictE = dict.fromkeys(total, 0)
wordDictF = dict.fromkeys(total, 0)
wordDictG = dict.fromkeys(total, 0)
wordDictH = dict.fromkeys(total, 0)

for word in frase1:
    wordDictA[word] += 1
for word in frase2:
    wordDictB[word] += 1
for word in frase3:
    wordDictC[word] += 1
for word in frase4:
    wordDictD[word] += 1
for word in frase5:
    wordDictE[word] += 1
for word in frase6:
    wordDictF[word] += 1
for word in frase7:
    wordDictG[word] += 1
for word in frase8:
    wordDictH[word] += 1

dt = pd.DataFrame([wordDictA, wordDictB, wordDictC, wordDictD, wordDictE, wordDictF, wordDictG, wordDictH])

tfs = [computeTF(wordDictA, frase1), computeTF(wordDictB, frase2), computeTF(wordDictC, frase3), computeTF(wordDictD, frase4), computeTF(wordDictE, frase5), computeTF(wordDictF, frase6), computeTF(wordDictG, frase7), computeTF(wordDictH, frase8)]
idfs = calculaIDF([wordDictA, wordDictB, wordDictC, wordDictD, wordDictE, wordDictF, wordDictG, wordDictH])
tfidfs = [calculaTDIDF(tf, idfs) for tf in tfs]

def calculaSimilaridade(vetor1, vetor2):
    somatorio = 0
    for i in range(len(vetor1)):
        somatorio += vetor1[i] * vetor2[i]
    return somatorio

def searchSimilarity(vetor, vetores):
    similaridades = []
    for i in range(len(vetores)):
        similaridades.append(calculaSimilaridade(vetor, vetores[i]))
    return similaridades


s = input("Digite a frase: ")
s = s.split(" ")


