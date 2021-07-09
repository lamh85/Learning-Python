import re

to_create = [
  "The quick brown fox jumped over",
  "The main in Spain",
  "How much wood could a woodchuck chuck if a woodchuck could chuck wood",
  "Come one come all",
  "Beauty is in the eye of the beholder",
  "Rome was not built in one day",
  "Oh the humanity",
  "Won't somebody please think of the children"
]

database_values = []

lookup_index = {}

def add_to_lookup_index(keyword, document_index):
  if (keyword not in lookup_index):
    lookup_index[keyword] = [document_index]
    return
    
  # The document index is already in the keyword's array
  if (document_index in lookup_index[keyword]):
    return
    
  lookup_index[keyword] = lookup_index[keyword] + [document_index]

def create_document(input):
  spaces_reduced = re.sub('\s{2,}', ' ', input)
  words_list = spaces_reduced.split(" ")
  database_values_length = len(database_values)
  
  for keyword in words_list:
    add_to_lookup_index(keyword, database_values_length)
    
  database_values.append(input)
  # replace extra spaces with single space
  # split the input into an array of words
  # add to the index:
    # if the key already exists, then append the document 
  
def create_documents(list_to_create):
  for to_create in list_to_create:
    create_document(to_create)

create_documents(to_create)

print(database_values)
print(lookup_index)
