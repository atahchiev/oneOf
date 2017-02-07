from rules import *
from stemmer import *
from steps import *
from main import DoAll
from test_lower import english_vocabulary
from test_capital import ENGLISH_VOCABULARY

import re
import collections

import unittest


class TestStringMethods(unittest.TestCase):

    def test_step1a(self):
        for stemmer, result in (("caresses", "caress"), ("ponies", "poni"),
                                ("ties", "ti"), ("caress", "caress"), ("cats", "cat")):
            stemmer = Stemmer(stemmer)
            DoStep1a(stemmer)
            self.assertEqual(stemmer.evolution[-1], result)

    def test_step1b(self):
        for stemmer, result in (("feed", "feed"), ("AGREED", "AGREE"), ("plastered", "plaster"),
                                ("bled", "bled"), ("motoring",
                                                   "motor"), ("sing", "sing"),
                                ("afas", "afa")):
            stemmer = Stemmer(stemmer)
            DoStep1a(stemmer)
            DoStep1b(stemmer)
            self.assertEqual(stemmer.evolution[-1], result)

    def test_step1b1(self):
        for stemmer, result in (("conflated", "conflate"), ("troubled", "trouble"),
                                ("sized", "size"), ("hopping", "hop"),
                                ("tanned", "tan"), ("falling", "fall"),
                                ("hissing", "hiss"), ("fizzed", "fizz"),
                                ("failing", "fail"), ("filing", "file")):
            stemmer = Stemmer(stemmer)
            DoStep1a(stemmer)
            DoStep1b(stemmer)
            self.assertEqual(stemmer.evolution[-1], result)

    def test_step1c(self):
        for stemmer, result in (("happy", "happi"), ("skying", "sky")):
            stemmer = Stemmer(stemmer)
            DoStep1a(stemmer)
            DoStep1b(stemmer)
            DoStep1c(stemmer)
            self.assertEqual(stemmer.evolution[-1], result)

    def test_step2(self):
        for stemmer, result in (("relational", "relate"), ("conditional", "condition"),
                                ("valenci", "valence"), ("hesitanci", "hesitance"), 
                                ("digitizer", "digitize"), ("conformabli", "conformable"), 
                                ("radicalli", "radical"), ("differentli", "different"),
                                ("vileli", "vile"), ("analogousli", "analogous"), 
                                ("vietnamization", "vietnamize"), ("predication", "predicate"), 
                                ("operator","operate"), ("feudalism", "feudal"), ("decisiveness", "decisive"), 
                                ("hopefulness", "hopeful"), ("callousness", "callous"),
                                ("formaliti", "formal"), ("sensitiviti", "sensitive"), 
                                ("sensibiliti", "sensible")):
            stemmer = Stemmer(stemmer)
            DoStep1a(stemmer)
            DoStep1b(stemmer)
            DoStep1c(stemmer)
            DoStep2(stemmer)
            self.assertEqual(stemmer.evolution[-1], result)

    def test_step3(self):
        for stemmer, result in (("triplicate", "triplic"), ("formative", "form"),
                                ("formalize", "formal"), ("electriciti",
                                                          "electric"), ("electrical", "electric"),
                                ("hopeful", "hope"), ("goodness", "good")):
            stemmer = Stemmer(stemmer)
            DoStep1a(stemmer)
            DoStep1b(stemmer)
            DoStep1c(stemmer)
            DoStep2(stemmer)
            DoStep3(stemmer)
            self.assertEqual(stemmer.evolution[-1], result)

    def test_step4(self):
        for stemmer, result in (("revival", "reviv"), ("allowance", "allow"), 
                                ("inference", "infer"), ("airliner", "airlin"), 
                                ("gyroscopic","gyroscop"), ("adjustable", "adjust"),
                                ("defensible", "defens"), ("irritant","irrit"), 
                                ("replacement", "replac"),("adjustment", "adjust"), 
                                ("dependent", "depend"), ("adoption", "adopt"), 
                                ("homologou", "homolog"), ("communism", "commun"), 
                                ("activate", "activ"),("angulariti", "angular"), 
                                ("homologous","homolog"), ("effective", "effect"), 
                                ("bowdlerize", "bowdler"), ("adoplion", "adoplion"),
                                ("armament", "armament")):
            stemmer = Stemmer(stemmer)
            DoStep1a(stemmer)
            DoStep1b(stemmer)
            DoStep1c(stemmer)
            DoStep2(stemmer)
            DoStep3(stemmer)
            DoStep4(stemmer)
            self.assertEqual(stemmer.evolution[-1], result)

    def test_step5a(self):
        for stemmer, result in (("probate", "probat"), ("rate", "rate"), ("cease", "ceas")):
            stemmer = Stemmer(stemmer)
            DoStep1a(stemmer)
            DoStep1b(stemmer)
            DoStep1c(stemmer)
            DoStep2(stemmer)
            DoStep3(stemmer)
            DoStep4(stemmer)
            DoStep5a(stemmer)
            self.assertEqual(stemmer.evolution[-1], result)

    def test_step5b(self):
        for stemmer, result in (("controll", "control"), ("roll", "roll")):
            stemmer = Stemmer(stemmer)
            DoStep1a(stemmer)
            DoStep1c(stemmer)
            DoStep2(stemmer)
            DoStep3(stemmer)
            DoStep4(stemmer)
            DoStep5a(stemmer)
            DoStep5b(stemmer)
            self.assertEqual(stemmer.evolution[-1], result)

    def test_all(self):
        for stemmer, result in ( ("slave", "slave"), ("rate", "rate")):
            stemmer = Stemmer(stemmer)
            DoAll(stemmer)
            self.assertEqual(stemmer.evolution[-1], result)

    def test_small(self):
        i = 0
        for stemmer in english_vocabulary:
            result = english_vocabulary[stemmer]
            stemmer1 = stemmer[:]
            stemmer = Stemmer(stemmer)
            DoAll(stemmer)
            if  stemmer.evolution[-1] != result:
                i += 1
                print(i, stemmer1, result, stemmer.evolution[-1])

    def test_big(self):
        i = 0
        for stemmer in ENGLISH_VOCABULARY:
            result = ENGLISH_VOCABULARY[stemmer]
            stemmer1 = stemmer[:]
            stemmer = Stemmer(stemmer)
            DoAll(stemmer)
            if  stemmer.evolution[-1] != result:
                i += 1
                print(i, stemmer1, result, stemmer.evolution[-1])
if __name__ == '__main__':
    unittest.main()
# 1 yare yare yar
# 2 yoked yoke yok
# 3 eli eli 
# 4 allied alli al
# 5 ely eli 
# 6 ally alli al
# 7 es e 
# 8 yoke yoke yok
# 9 yarely yare yar
# 10 yokes yoke yok
# 11 yore yore yor
# 12 allies alli 
# 13 ates at 
# 14 fulness ful 