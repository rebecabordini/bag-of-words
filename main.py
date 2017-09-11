import json

from unidecode import unidecode
from stop_words import get_stop_words


class SentenceHelpers:
    stop_words = [unidecode(stop_word) for stop_word in get_stop_words('portuguese')]

    @classmethod
    def remove_punctuation_marks(cls, sentence):
        return sentence \
            .replace('.', '') \
            .replace(',', '') \
            .replace('?', '') \
            .replace('!', '') \
            .replace(';', '') \
            .replace('\n', ' ')

    @classmethod
    def clean_token_list(cls, tokens):
        new_token_list = []
        for token in tokens:
            # Remove acentos e transforma tudo para lower case
            new_token = unidecode(token.lower())
            # Remove stop-words
            if new_token not in cls.stop_words:
                new_token_list.append(new_token)
        return new_token_list


class Document:
    def __init__(self, data):
        self.body = data.get('body', '')
        self.url = data.get('url', '')
        self.token_list = self.generate_token_list()
        self.token_list_size = len(self.token_list)
        self.clean_token_list = self.clean_token_list()
        self.clean_token_list_size = len(self.clean_token_list)

    def generate_token_list(self):
        token_list = SentenceHelpers.remove_punctuation_marks(self.body).split(' ')
        return token_list

    def clean_token_list(self):
        return SentenceHelpers.clean_token_list(self.token_list)


if __name__ == '__main__':
    with open('./dataset_g1_min.json') as documents_json:
        data = json.load(documents_json)
    hits = data.get('hits', {}).get('hits', [])

    documents_list = []

    for hit in hits:
        data = hit.get('_source')
        document = Document(data=data)
        documents_list.append(document)
