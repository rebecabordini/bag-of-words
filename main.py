import json

from models.document import Document
from models.vocabulary import Vocabulary


def create_file(file_name, content):
    file = open(file_name, 'w')
    file.write(content)
    file.close()


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

    create_file(file_name='vocabulary_with_token_list.txt', content=str(vocabulary.token_list))
    create_file(file_name='vocabulary.txt', content=str(vocabulary.clean_token_list))
