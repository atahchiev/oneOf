import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from oneOf.porter import main, stemmer
main.DoAll(stemmer.Stemmer("milen"))