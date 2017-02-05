from rules import *
from stemmer import *
from steps import *

import re
import collections


def DoAll(stemmer):
    DoStep1a(stemmer)
    DoStep1b(stemmer)
    DoStep1c(stemmer)
    DoStep2(stemmer)
    DoStep3(stemmer)
    DoStep4(stemmer)
    DoStep5a(stemmer)
    DoStep5b(stemmer)

# prying prying pry
# 133 subversion subvers subversion
if __name__ == "__main__":
    stemmer = Stemmer("subversion")
    print(stemmer.endsCVCNoWXY(WXY))
    print(stemmer.__dict__)
    DoAll(stemmer)
    print(stemmer.__dict__)
