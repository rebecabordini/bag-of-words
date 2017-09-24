
class EuclideanDistance:
    def __init__(self, bagOfWords):
        self.bagOfWords = bagOfWords.tolist()
        self.distances_list = self.calculating_distance()

    def calculating_distance(self):
        distances = []
        distance = 0
        par1 = 0
        par2 = 1
        for bagofword in self.bagOfWords[::2]:
            print par1, par2
            for p1 in self.bagOfWords[par1]:
              for p2 in self.bagOfWords[par2]:
                 distance = distance +(pow((p1 - p2), 2))
            distances.append(distance)
            par1 = par1+1
            par2 = par2+1
            distance = 0
        print distances