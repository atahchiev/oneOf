class WordEvaluation:
    def __init__(self, word_name=None, tf = 0, idf=0, tf_idf=0):
        self.word_name = word_name
        self.tf = tf
        self.idf = idf
        self.tf_idf = tf*idf


    def calc_tf(self):
        pass

    def calc_idf(self):
        pass

    # def pee

class ClassInfo:
    def __init__(self, d=None, tf = 0, idf = 0):
        pass