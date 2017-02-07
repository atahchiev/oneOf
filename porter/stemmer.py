from rules import vowels, consonants, WXY, Y
import re


class Stemmer:

    def __init__(self, word):
        self.word = word
        self.stem = word
        self.cvStem = self.setcvStem(word)
        self.groups = self.setGroups()
        if self.groups:
            self.ms = self.groups.group(2)
            self.MsCount = len(self.ms)//2
        self.evolution = [self.word]

    def setGroups(self):
        groups = re.search('(C)?((VC)*)(V)?', self.cvStem)
        if groups:
            self.ms = groups.group(2)
            self.MsCount = len(self.ms)//2

        return re.search('(C)?((VC)*)(V)?', self.cvStem)

    def setcvStem(self, word):
        if word == "":
            cvString = ""
            self.cvStem = cvString
            return cvString
        cvString = ""
        if word[0] in ("Y", "y"):
            cvString += "C"
        elif word[0] in vowels:
            cvString += "V"
        elif word[0] in consonants:
            cvString += "C"

        for i in word[1:]:
            if i in vowels and cvString[-1] != "V":
                cvString += "V"
            elif i in consonants and cvString[-1] != "C":
                cvString += "C"
            elif i in ("y", "Y") and cvString[-1] == "V":
                cvString += "C"
            elif i in ("y", "Y") and cvString[-1] == "C":
                cvString += "V"
        self.cvStem = cvString
        return cvString

    def __repr__(self):
        return repr(self.evolution)

    def endsWithC(self, consonant):
        if re.search(consonant.lower() + "$", self.stem.lower()):
            return True
        else:
            return False

    def containsLetters(self, letters):
        for i in letters:
            if re.search("v", self.cvStem.lower()):
                return True
        return False

    def endsDoubleC(self, letters):
        # print(letters)
        for i in letters:
            if re.search(2*i.lower()+"$", self.stem.lower()):
                return True
        return False

    def endsCVCNoWXY(self, letters):
        searchRegex = "[" + consonants + Y + "]" +\
            "[" + vowels + Y + "]" + "[" + consonants + Y + "]$"
        if not re.search("["+WXY+"]$", self.stem.lower()) and\
                re.search(searchRegex, self.stem):
            return False
        return True

    def setStem(self, key):
        if re.search(key+"$", self.evolution[-1]):
            self.stem = self.evolution[-1][:-len(key)]
            return self.stem

    def getKey(self, key):
        if re.search(key+"$", self.evolution[-1]):
            return key

    def substitution(self, key, rules):
        word = self.evolution[-1]
        searchRegex = re.compile(key+'$')
        endsWithLetter = re.search(searchRegex, word)
        if endsWithLetter:
            word = re.sub(searchRegex, rules[key], word)
            self.evolution.append(word)
            self.word = self.evolution[-1]

    def append(self, element):
        self.evolution.append(element)

    def update(self, currentKey):
        self.setStem(currentKey)
        self.setcvStem(self.stem)
        self.setGroups()
