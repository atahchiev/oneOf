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
<<<<<<< HEAD
    return stemmer

# prying prying pry
# 133 subversion subvers subversion
if __name__ == "__main__":
    stemmer = Stemmer("conflatededed")
    # print(stemmer.endsCVCNoWXY(WXY))
    print(stemmer.__dict__)
    DoAll(stemmer)
    print(stemmer.__dict__)
=======
    return stemmer\

>>>>>>> 5af9a09c4567b4675eb3d6c9f9c4a52ff72a3b73
