from . import *
from porter.stemmer import *
from porter.steps import *

import re
import collections


def DoAll(stemmer):
    while(True):
        stem = stemmer.stem
        DoStep1a(stemmer)
        DoStep1b(stemmer)
        DoStep1c(stemmer)
        DoStep2(stemmer)
        DoStep3(stemmer)
        DoStep4(stemmer)
        DoStep5a(stemmer)
        DoStep5b(stemmer)
        if stem == stemmer.stem:
            break
        # print(stemmer)
    return stemmer\

