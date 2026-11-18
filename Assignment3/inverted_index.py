#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: inverted_index.py
# SPECIFICATION: description of the program
# FOR: CS 4250 - Assignment #3
# TIME SPENT: how long it took you to complete the assignment
#-------------------------------------------------------------------------

# Importing Python libraries
import string
from collections import Counter
from pymongo import MongoClient

# Connecting to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Accessing the database and collections
db = client["assignment3"]
documents = db["documents"]
inverted_index = db["inverted_index"]


#-------------------------------------------------------------------------
# FUNCTION: getTermFrequencies
# SPECIFICATION: receives a text and returns the frequency of each term
#-------------------------------------------------------------------------
def getTermFrequencies(text):

    # Converting text to lowercase
    text = text.lower()

    # Removing punctuation
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)

    # Splitting the text into terms
    terms = text.split()

    # Returning the term frequencies
    return Counter(terms)


#-------------------------------------------------------------------------
# FUNCTION: addPosting
# SPECIFICATION: adds a posting to an existing term or creates a new term
#-------------------------------------------------------------------------
def addPosting(term, docId, tf):

    # Searching for the term in the inverted index
    

    # Creating a new term if it does not exist


    # Adding a posting if the term already exists


#-------------------------------------------------------------------------
# FUNCTION: removePosting
# SPECIFICATION: removes a document posting from a term and deletes the
#                term if its postings list becomes empty
#-------------------------------------------------------------------------
def removePosting(term, docId):

    # Removing the posting from the term
    # --> add your Python code here


    # Retrieving the term after removing the posting
    # --> add your Python code here


    # Deleting the term if its postings list is empty
    # --> add your Python code here



#-------------------------------------------------------------------------
# FUNCTION: insertDocument
# SPECIFICATION: inserts a document and updates the inverted index
#-------------------------------------------------------------------------
def insertDocument(document):

    # Inserting the document into the documents collection
    # --> add your Python code here


    # Obtaining the term frequencies
    # --> add your Python code here


    # Updating the inverted index
    # --> add your Python code here



#-------------------------------------------------------------------------
# FUNCTION: updateDocument
# SPECIFICATION: updates a document and makes the corresponding changes
#                to the inverted index
#-------------------------------------------------------------------------
def updateDocument(docId, newText):

    # Retrieving the current document
    # --> add your Python code here


    # Obtaining the old and new term frequencies
    # --> add your Python code here


    # Processing terms that existed in the old document
    # --> add your Python code here


    # Processing terms that occur only in the new document
    # --> add your Python code here


    # Updating the document text
    # --> add your Python code here



#-------------------------------------------------------------------------
# FUNCTION: deleteDocument
# SPECIFICATION: deletes a document and removes all of its postings from
#                the inverted index
#-------------------------------------------------------------------------
def deleteDocument(docId):

    # Retrieving the document before deleting it
    # --> add your Python code here


    # Obtaining the terms contained in the document
    # --> add your Python code here


    # Removing the document from every corresponding posting list
    # --> add your Python code here


    # Deleting the document
    # --> add your Python code here



#-------------------------------------------------------------------------
# Executing the sequence of operations
#-------------------------------------------------------------------------

# Operation 1: document 1 is obtained
document1 = {
    "_id": 1,
    "text": "Summer rain is common in Florida."
}

insertDocument(document1)


# Operation 2: document 2 is obtained
document2 = {
    "_id": 2,
    "text": "Summer is hot in Arizona."
}

insertDocument(document2)


# Operation 3: document 1 is updated
updateDocument(
    1,
    "Summer rain is hot rain in Florida."
)


# Operation 4: document 3 is obtained
document3 = {
    "_id": 3,
    "text": "Hot summer rain in California."
}

insertDocument(document3)


# Operation 5: document 2 is deleted
deleteDocument(2)

# Operation 6: print the content of the documents and inverted_index collections
# --> add your Python code here