import math

class WordEvaluation:
    def __init__(self, word_name=None, word_frequency=0, docs_with_word=0):
        self.word_name = word_name
        self.word_frequency = self.calc_tf()
        self.tf = self.calc_tf()
        self.idf = self.calc_idf()
        self.tf_idf = self.tf*self.idf
        self.docs_with_word = docs_with_word

    def calc_tf(self):
        if self.word_frequency == 0:
            return 0
        elif self.word_frequency > 0:
            return 1 + math.log(self.word_frequency,10)

    def calc_idf(self, documents):
        return math.log(documents/self.word_frequency,10)


class ClassInfo:
    def __init__(self, d=None, tf=0, idf=0):
        pass