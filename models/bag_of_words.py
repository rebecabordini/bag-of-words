from sklearn.feature_extraction.text import CountVectorizer


class BagOfWords:
    def __init__(self, documents):
        self.documents = documents
        self.bag_of_words = self.generate_bag_of_words()

    def generate_bag_of_words(self):
        doc=[]

        for document in self.documents:
            doc.append(document.body)

        vectorizer = CountVectorizer()
        return vectorizer.fit_transform(doc).todense()