# -*- coding:utf-8 -*-

from models.visualizations import generate_visualization_document_size, generate_visualization
from models.euclidean_distance import EuclideanDistance


def create_file(file_name, content):

    file = open(file_name, 'w')
    file.write(content)
    file.close()


def generate_results(vocabulary, bag_of_words, document_size_in_tokens):

    create_file(file_name='results/initial_vocabulary.txt', content=str(vocabulary.token_list))
    create_file(file_name='results/vocabulary.txt', content=str(vocabulary.clean_token_list))
    create_file(file_name='results/document_size_in_tokens.txt', content=str(document_size_in_tokens))
    create_file(file_name='results/bag_of_words.txt', content=str(bag_of_words.generate_bag_of_words()))

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

    euclidian_distance = EuclideanDistance(bag_of_words=bag_of_words.bag_of_words)
    create_file(file_name='results/distances.txt', content=str(euclidian_distance.distances_list))

