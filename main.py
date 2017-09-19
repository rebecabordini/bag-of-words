import json

from models.document import Document
from models.vocabulary import Vocabulary


if __name__ == '__main__':
    with open('./dataset_g1.json') as documents_json:
        data = json.load(documents_json)
    hits = data.get('hits', {}).get('hits', [])

    document_list = []
    for hit in hits:
        data = hit.get('_source')
        document = Document(data=data)
        document_list.append(document)

    vocabulary = Vocabulary(documents=document_list)

    # Creating a file with token list
    file = open("vocabulary_with_token_list.txt", "w")
    file.write("Vocabulary size {size}".format(size=vocabulary.token_list_size))
    file.write(str(vocabulary.token_list))
    file.close()

    # Creating a file with cleantoken list
    file = open("vocabulary.txt", "w")
    file.write("Vocabulary size {size}".format(size=vocabulary.clean_token_list_size))
    file.write(str(vocabulary.clean_token_list))
    file.close()
