from models.sentence import SentenceHelpers


class Document:
    def __init__(self, data):
        self.body = data.get('body', '')
        self.url = data.get('url', '')
        self.token_list = self.generate_token_list()
        self.token_list_size = len(self.token_list)
        self.clean_token_list = self.clean_token_list()
        self.clean_token_list_size = len(self.clean_token_list)

    def generate_token_list(self):
        token_list = self.body.replace('\n', ' ').split(' ')
        return token_list

    def clean_token_list(self):
        clean_token_list = SentenceHelpers.remove_punctuation_marks(self.body).split(' ')
        return SentenceHelpers.clean_token_list(clean_token_list)
