from rules import *


def DoStep1a(stemmer):
    for key in step1a:
        currentKey = stemmer.getKey(key)
        stemmer.setStem(key)
        if currentKey:
            stemmer.substitution(key, step1a)
            break


def DoStep1b1(stemmer):
    for key in step1b1:
        currentKey = stemmer.getKey(key)
        if currentKey:
            stemmer.update(currentKey)
            if currentKey.lower() in ("at", "bl", "iz"):
                stemmer.substitution(currentKey, step1b1)
            break
    stemmer.stem = stemmer.word
    stemmer.setcvStem(stemmer.stem)
    stemmer.setGroups()
    if stemmer.endsDoubleC(consonants):
        if not stemmer.endsDoubleC("LSZ"):
            stemmer.append(stemmer.stem[:-1])
    elif not stemmer.endsCVCNoWXY(WXY) and stemmer.MsCount == 1:
        if stemmer.stem[0] == stemmer.stem[0].lower():
            stemmer.append(stemmer.stem+"e")
        elif stemmer.stem[0] == stemmer.stem[0].upper():
            stemmer.append(stemmer.stem+"E")


def DoStep1b(stemmer):
    for key in step1b:
        currentKey = stemmer.getKey(key)
        if currentKey:
            stemmer.update(currentKey)
            if currentKey.lower() == "eed":
                if stemmer.MsCount > 0:
                    stemmer.substitution(currentKey, step1b)
                break
            elif stemmer.containsLetters(vowels):
                stemmer.substitution(currentKey, step1b)
                DoStep1b1(stemmer)
            break


def DoStep1c(stemmer):
    for key in step1c:
        currentKey = stemmer.getKey(key)
        if currentKey:
            stemmer.update(currentKey)
            if stemmer.containsLetters(vowels):
                stemmer.substitution(currentKey, step1c)
            break


def DoStep2(stemmer):
    for key in step2:
        currentKey = stemmer.getKey(key)
        if currentKey:
            stemmer.update(currentKey)
            # print(stemmer.__dict__, currentKey)
            if stemmer.MsCount > 0:
                stemmer.substitution(currentKey, step2)
            break


def DoStep3(stemmer):
    for key in step3:
        currentKey = stemmer.getKey(key)
        if currentKey:
            stemmer.update(currentKey)
            if stemmer.MsCount > 0:
                stemmer.substitution(currentKey, step3)
            break


def DoStep4(stemmer):
    for key in step4:
        currentKey = stemmer.getKey(key)
        if currentKey:
            stemmer.update(currentKey)
            # print(stemmer.endsWithC("t") or not stemmer.endsWithC("s"))
            if stemmer.MsCount > 1:
                if currentKey.lower() != "ion":
                    stemmer.substitution(currentKey, step4)
                elif currentKey.lower() == "ion" and\
                        (stemmer.endsWithC("t") or stemmer.endsWithC("s")):
                    stemmer.substitution(currentKey, step4)
                
            break


def DoStep5a(stemmer):
    for key in step5a:
        currentKey = stemmer.getKey(key)
        if currentKey:
            stemmer.update(currentKey)
            # print(stemmer.MsCount == 1 and stemmer.endsCVCNoWXY(WXY))
            if stemmer.MsCount > 1 or\
                    (stemmer.MsCount == 1 and stemmer.endsCVCNoWXY(WXY)):
                stemmer.substitution(currentKey, step5a)
            break


def DoStep5b(stemmer):
    for key in step5b:
        currentKey = stemmer.getKey(key)
        if currentKey:
            stemmer.update(currentKey)
            if stemmer.MsCount > 1 and stemmer.endsWithC("l"):
                stemmer.substitution(currentKey, step5b)
            break
