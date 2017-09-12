import json

from unidecode import unidecode
from stop_words import get_stop_words


class SentenceHelpers:
    stop_words = [unidecode(stop_word) for stop_word in get_stop_words('portuguese')]

    @classmethod
    def remove_punctuation_marks(cls, sentence):
        # Procurar expressao regular para melhorar
        return sentence \
            .replace('.', '') \
            .replace(',', '') \
            .replace('?', '') \
            .replace('!', '') \
            .replace(';', '') \
            .replace('[', '') \
            .replace(']', '') \
            .replace('(', '') \
            .replace(')', '') \
            .replace('{', '') \
            .replace('}', '') \
            .replace('/', '') \
            .replace('-', '') \
            .replace('_', '') \
            .replace(':', '') \
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


class Vocabulary:
    def __init__(self, documents):
        self.documents = documents
        self.token_list = self.generate_vocabulary(mode="full")
        self.token_list_size = len(self.token_list.keys())
        self.clean_token_list = self.generate_vocabulary(mode="clean")
        self.clean_token_list_size = len(self.clean_token_list.keys())

    def generate_vocabulary(self, mode):
        vocabulary = {}

        for document in self.documents:
            # Remove duplicated tokens
            if mode == "full":
                list_to_search = document.token_list
            else:
                list_to_search = document.clean_token_list

            for token in list_to_search:
                if vocabulary.has_key(token):
                    vocabulary[token] = vocabulary[token] + 1
                else:
                    vocabulary.update({token: 1})

        return vocabulary

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
