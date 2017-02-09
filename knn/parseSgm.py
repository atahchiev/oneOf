from bs4 import BeautifulSoup, Comment
import os
import lxml
import pickle
import sys
import string
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "\\porter")
print(sys.path)
# from porter import doall

sys.path.insert(0, '../')
# from porter import rules
sys.setrecursionlimit(100000)

def parse_dir(folder):
    return {document: parse_document(document, folder) for document in os.listdir(folder) if document.endswith('.sgm')}

def parse_document(document, folder):
    with open(os.path.join(folder, document), 'r') as f:
        raw = f.read()
    print(document)
    return BeautifulSoup(raw, 'html.parser')

# def stem_document(document):
#     stemDocument = ""
#     for line in document:
#         for word in line.split():
#             word = word.translate(str.maketrans('','',string.punctuation))
#             stemDocument += " " + (parser.doall(word))
#     return stemDocument

# print(stem_document("Milen, kamenov, ivanov"))

def slice_soup(soup):
    for i in pickletje:
        pass


def make_pickles(dir_path):
    # print(dir_path)    
    bs = parse_dir(dir_path)
    # print(len(bs))
    # print(type(bs))
    for i, (document, ast) in enumerate(bs.items()):
        print(i, document)
        # pickle.dumps(ast)
        pickle.dump(ast, open(os.path.join('documents', 'save' + str(i) + '.p'), 'wb'))

    



    

  
dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))  
# xml_doc = '<topic><s>z</s></topic>'
# htmlToDict(xml_doc)
dir_path = os.path.join(dir_path, 'reuters21578')
make_pickles(dir_path)
# check_pickle()
# print([bs[1].find_all()])
# print(bs[0].__dict__.keys())