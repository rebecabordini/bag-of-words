# -*- coding:utf-8 -*-

import json
import operator

from matplotlib import pylab, pyplot

from models.document import Document
from models.vocabulary import Vocabulary
from models.bag_of_words import BagOfWords
from models.euclidean_distance import EuclideanDistance


def create_file(file_name, content):
    file = open(file_name, 'w')
    file.write(content)
    file.close()


def cumulative_frequencies(data):
    cf = 0.0
    for sample in data:
        cf += sample[1]
        yield cf


def generate_plot(data, xlabel, file_name, cumulative=True):
    if cumulative:
        frequencies = list(cumulative_frequencies(data))
        ylabel = u"Frequência acumulada"
    else:
        frequencies = [sample[1] for sample in data]
        ylabel = u"Frequência"

    pylab.grid(True, color="silver")
    pylab.plot(frequencies)
    pylab.xticks(range(len(data)), [sample[0] for sample in data], rotation=90)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)

    pylab.savefig(file_name)
    pyplot.close()


def generate_visualization(data, file_name, cumulative=True):
    ordered_data = sorted(data.items(), key=operator.itemgetter(1), reverse=True)
    most_common = ordered_data[:50]
    generate_plot(most_common, 'Tokens', file_name, cumulative)


def slugify(url):
    return url.split('.')[-2].split('/')[-1][:30] + '...'


def generate_visualization_document_size(documents_list, file_name, cumulative=True):
    data = {}
    for document in documents_list:
        sample = {slugify(document.url): document.clean_token_list_size}
        data.update(sample)

    ordered_data = sorted(data.items(), key=operator.itemgetter(1), reverse=True)
    top_documents = ordered_data[:50]
    generate_plot(top_documents, 'Slug dos documentos', file_name, cumulative)


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

    create_file(file_name='results/initial_vocabulary.txt', content=str(vocabulary.token_list))
    create_file(file_name='results/vocabulary.txt', content=str(vocabulary.clean_token_list))
    create_file(file_name='results/document_size_in_tokens.txt', content=str(document_size_in_tokens))
    create_file(file_name='results/dbag_of_words.txt', content=str(bag_of_words.generate_bag_of_words()))

    generate_visualization_document_size(vocabulary.documents,
                                         file_name='results/distribuicao_tamanho_documentos_em_tokens.png',
                                         cumulative=False)

    generate_visualization_document_size(vocabulary.documents,
                                         file_name='results/distribuicao_tamanho_documentos_em_tokens_acumulada.png',
                                         cumulative=True)

    generate_visualization(vocabulary.clean_token_list,
                           file_name='results/distribuicao_frequencia_tokens_acumulada.png',
                           cumulative=True)
    generate_visualization(vocabulary.clean_token_list,
                           file_name='results/distribuicao_frequencia_tokens.png',
                           cumulative=False)

    euclidian_distance = EuclideanDistance(bagOfWords= bag_of_words.bag_of_words)
    euclidian_distance.distances_list

