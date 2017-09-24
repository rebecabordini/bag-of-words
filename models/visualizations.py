# -*- coding:utf-8 -*-

import operator

from matplotlib import pylab, pyplot


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
