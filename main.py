# -*- coding:utf-8 -*-

import json
import operator

from matplotlib import pylab

from models.document import Document
from models.vocabulary import Vocabulary


def create_file(file_name, content):
    file = open(file_name, 'w')
    file.write(content)
    file.close()


def cumulative_frequencies(data):
    cf = 0.0
    for sample in data:
        cf += sample[1]
        yield cf


def generate_visualization(data):
    ordered_data = sorted(data.items(), key=operator.itemgetter(1), reverse=True)
    most_common = ordered_data[:50]
    frequencies = list(cumulative_frequencies(most_common))
    ylabel = u"Distribuição acumulada"

    pylab.grid(True, color="silver")
    pylab.plot(frequencies)
    pylab.xticks(range(len(most_common)), [sample[0] for sample in most_common], rotation=90)
    pylab.xlabel("Tokens")
    pylab.ylabel(ylabel)
    pylab.show()


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

    create_file(file_name='results/initial_vocabulary.txt', content=str(vocabulary.token_list))
    create_file(file_name='results/vocabulary.txt', content=str(vocabulary.clean_token_list))
    create_file(file_name='results/document_size_in_tokens.txt', content=str(document_size_in_tokens))

    generate_visualization(vocabulary.clean_token_list)
