# -*- coding:utf-8 -*-


class EuclideanDistance:
    def __init__(self, bag_of_words):
        self.bag_of_words = bag_of_words.tolist()
        self.distances_list = self.calculate_distance()

    @staticmethod
    def distance_between_documents(document_1, document_2):
        distance_squared = 0
        for idx in range(len(document_1)):
            distance = (document_1[idx] - document_2[idx])
            distance_squared = distance_squared + (distance * distance)
        return distance_squared

    def calculate_distance(self):
        distances = []
        for idx in range(len(self.bag_of_words)):
            document_1 = self.bag_of_words[idx]
            for idy in range(idx + 1, len(self.bag_of_words)):
                document_2 = self.bag_of_words[idy]
                print idx, idy
                text = 'Documento 1: {documento1}, Documento 2: {documento2}, Dist: {distancia}'.format(
                    documento1=idx,
                    documento2=idy,
                    distancia=self.distance_between_documents(document_1, document_2))
                distances.append(text)

        return distances
