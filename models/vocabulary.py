class Vocabulary:
    def __init__(self, documents):
        self.documents = documents
        self.token_list = self.generate_vocabulary(mode='full')
        self.token_list_size = len(self.token_list.keys())
        self.clean_token_list = self.generate_vocabulary(mode='clean')
        self.clean_token_list_size = len(self.clean_token_list.keys())

    def generate_vocabulary(self, mode):
        vocabulary = {}

        for document in self.documents:
            # Remove duplicated tokens
            if mode == 'full':
                list_to_search = document.token_list
            else:
                list_to_search = document.clean_token_list

            for token in list_to_search:
                if vocabulary.has_key(token):
                    vocabulary[token] = vocabulary[token] + 1
                else:
                    vocabulary.update({token: 1})

        return vocabulary