from unidecode import unidecode
from stop_words import get_stop_words


class SentenceHelpers:
    stop_words = [unidecode(stop_word) for stop_word in get_stop_words('portuguese') + [' ', '']]

    @classmethod
    def remove_punctuation_marks(cls, sentence):
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
            .replace('_', '') \
            .replace(':', '') \
            .replace('\n', ' ') \
            .replace('\t', ' ') \
            .replace('"', '') \


    @classmethod
    def clean_token_list(cls, tokens):
        new_token_list = []
        for token in tokens:
            # Removes accent and transforms all tokens in lower case
            new_token = unidecode(token.lower())
            # Removes stop-words
            if new_token not in cls.stop_words:
                new_token_list.append(new_token)
        return new_token_list