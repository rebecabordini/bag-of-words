# -*- coding:utf-8 -*-

import redis

from Queue import Queue
from threading import Thread


def memoize(f):
    """ Memoization decorator for functions taking one or more arguments. """
    class memodict(dict):
        def __init__(self, f):
            self.f = f

        def __call__(self, *args):
            return self[args]

        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)


@memoize
def squared(a):
    return a * a


def distance_between_documents(document_1, document_2):
    distance_squared = 0
    for idx in range(len(document_1)):
        distance = document_1[idx] - document_2[idx]
        distance_squared = distance_squared + squared(distance)
    return distance_squared


class EuclideanDistance:
    def __init__(self, bag_of_words):
        self.bag_of_words = bag_of_words.tolist()
        self.distances_list = self.calculate_distance()

    q = Queue()
    num_worker_threads = 4
    distances = []
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    HASH_NAME = 'euclidean_distances'

    def worker(self):
        while True:
            item = self.q.get()
            distance = distance_between_documents(item[0], item[1])
            key = '{idx}+{idy}'.format(idx=item[2], idy=item[3])
            self.r.hset(self.HASH_NAME, key, distance)
            self.q.task_done()

    def calculate_distance(self):
        distances = []

        for i in range(self.num_worker_threads):
            t = Thread(target=self.worker)
            t.daemon = True
            t.start()

        for idx in range(len(self.bag_of_words)):
            document_1 = self.bag_of_words[idx]
            for idy in range(idx + 1, len(self.bag_of_words)):
                document_2 = self.bag_of_words[idy]
                self.q.put([document_1, document_2, idx, idy])

        return distances
