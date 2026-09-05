#-------------------------------------------------------------------------
# AUTHOR: Jeannette Ruiz
# FILENAME: index.py
# SPECIFICATION: Read a document and return its inverted index
# FOR: CS 4250 - Assignment #1
# TIME SPENT: 1hr

#-------------------------------------------------------------------------

# Importing Python libraries
import pandas as pd
import re

# Reading the document collection
data = pd.read_csv("collection.csv")

# Defining the dictionary used for lemmatization
# --> add your Python code here
lemmas = {
    "homes" : "home",
    "increases" : "increase",
    "rising" : "rise",
    "increasing" : "increase",
    "sales" : "sale"
}

# Creating the data structure that will store the inverted index
invertedIndex = {}

# Processing each document in the collection
for i, row in data.iterrows():

    docID = row["Document"]
    text = row["Text"]

    # Applying surface-level normalization
    text = text.lower()
    text = re.sub(pattern = "[^\w\s]", repl ="", string = text)
    

    # Tokenizing the document
    tokens = text.split()


    # Applying lemmatization
    lemma_tokens = []

    for token in tokens:
        if token in lemmas:
            lemma_tokens.append(lemmas[token])
        else:
            lemma_tokens.append(token)


    # Building the inverted index
    for token in lemma_tokens:
        if token not in invertedIndex:
            invertedIndex[token] = [docID]
        elif docID not in invertedIndex[token]:
            invertedIndex[token].append(docID)
    


# Printing the inverted index with terms ordered alphabetically
# Expected format:
# term1 : ['Doc1', 'Doc2']
# term2 : ['Doc3']

for term in sorted(invertedIndex):
    print(f"{term} : {invertedIndex[term]}")