# -*- coding:utf-8 -*-

import json

from models.document import Document
from models.results import generate_results

from models.vocabulary import Vocabulary
from models.bag_of_words import BagOfWords


if __name__ == '__main__':
    with open('./datasets/dataset_g1.json') as documents_json:
        data = json.load(documents_json)
    hits = data.get('hits', {}).get('hits', [])

    document_list = []
    document_size_in_tokens = []
    for hit in hits:
        data = hit.get('_source')
        document = Document(data=data)
        document_list.append(document)
        document_size_in_tokens.append(document.clean_token_list_size)

    vocabulary = Vocabulary(documents=document_list)
    bag_of_words = BagOfWords(documents=document_list)

    generate_results(vocabulary, bag_of_words, document_size_in_tokens)
