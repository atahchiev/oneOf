import collections

vowels = ("AEIOUaeiou")
consonants = ("BCDFGHJKLMNPQRSTVXWZbcdfghjklmnpqrstvxwz")

WXY = ("wxyWXY")

Y = ("Yy")

step1a = collections.OrderedDict([
    ("SSES", "SS"),
    ("sses", "ss"),
    ("IES", "I"),
    ("ies", "i"),
    ("SS", "SS"),
    ("ss", "ss"),
    ("S", ""),
    ("s", "")
]
)
step1b = collections.OrderedDict([
    ("EED", "EE"),  # (m>0)
    ("eed", "ee"),  # (m>0)
    ("ED", ""),     # (*v*)
    ("ed", ""),     # (*v*)
    ("ING", ""),    # (*v*)
    ("ing", "")     # (*v*)
])

step1b1 = collections.OrderedDict([
    ("AT", "ATE"),
    ("BL", "BLE"),
    ("IZ", "IZE"),
    ("at", "ate"),
    ("bl", "ble"),
    ("iz", "ize")

])

step1c = collections.OrderedDict([
    ("Y", "I"),  # (*v*)
    ("y", "i")
])

step2 = collections.OrderedDict([
    ("ATIONAL", "ATE"),    # (m>0)
    ("TIONAL",   "TION"),  # (m>0)
    ("ENCI", "ENCE"),      # (m>0)
    ("ANCI", "ANCE"),      # (m>0)
    ("IZER", "IZE"),       # (m>0)
    ("ABLI", "ABLE"),      # (m>0)
    ("ALLI", "AL"),        # (m>0)
    ("ENTLI", "ENT"),      # (m>0)
    ("ELI", "E"),          # (m>0)
    ("OUSLI", "OUS"),      # (m>0)
    ("IZATION", "IZE"),    # (m>0)
    ("ATION", "ATE"),      # (m>0)
    ("ATOR", "ATE"),       # (m>0)
    ("ALISM", "AL"),       # (m>0)
    ("IVENESS", "IVE"),    # (m>0)
    ("FULNESS", "FUL"),    # (m>0)
    ("OUSNESS", "OUS"),    # (m>0)
    ("ALITI", "AL"),       # (m>0)
    ("IVITI", "IVE"),      # (m>0)
    ("BILITI", "BLE"),     # (m>0)
    ("ational", "ate"),    # (m>0)
    ("tional",   "tion"),  # (m>0)
    ("enci", "ence"),      # (m>0)
    ("anci", "ance"),      # (m>0)
    ("izer", "ize"),       # (m>0)
    ("abli", "able"),      # (m>0)
    ("alli", "al"),        # (m>0)
    ("entli", "ent"),      # (m>0)
    ("eli", "e"),          # (m>0)
    ("ousli", "ous"),      # (m>0)
    ("ization", "ize"),    # (m>0)
    ("ation", "ate"),      # (m>0)
    ("ator", "ate"),       # (m>0)
    ("alism", "al"),       # (m>0)
    ("iveness", "ive"),    # (m>0)
    ("fulness", "ful"),    # (m>0)
    ("ousness", "ous"),    # (m>0)
    ("aliti", "al"),       # (m>0)
    ("iviti", "ive"),      # (m>0)
    ("biliti", "ble")      # (m>0)
])

step3 = collections.OrderedDict([
    ("ICATE", "IC"),  # m>0
    ("ATIVE", ""),    # m>0
    ("ALIZE", "AL"),  # m>0
    ("ICITI", "IC"),  # m>0
    ("ICAL", "IC"),   # m>0
    ("FUL", ""),      # m>0
    ("NESS", ""),     # m>0
    ("icate", "ic"),  # m>0
    ("ative", ""),    # m>0
    ("alize", "al"),  # m>0
    ("iciti", "ic"),  # m>0
    ("ical", "ic"),   # m>0
    ("ful", ""),      # m>0
    ("ness", "")      # m>0
])

step4 = collections.OrderedDict([
    ("AL", ""),     # (m>1)
    ("ANCE", ""),   # (m>1)
    ("ENCE", ""),   # (m>1)
    ("ER", ""),     # (m>1)
    ("IC", ""),     # (m>1)
    ("ABLE", ""),   # (m>1)
    ("IBLE", ""),   # (m>1)
    ("ANT", ""),    # (m>1)
    ("EMENT", ""),  # (m>1)
    ("MENT", ""),   # (m>1)
    ("ENT", ""),    # (m>1)
    ("ION", ""),    # (m>1 and (*S or *T))
    ("OU", ""),     # (m>1)
    ("ISM", ""),    # (m>1)
    ("ATE", ""),    # (m>1)
    ("ITI", ""),    # (m>1)
    ("OUS", ""),    # (m>1)
    ("IVE", ""),    # (m>1)
    ("IZE", ""),     # (m>1)
    ("al", ""),     # (m>1)
    ("ance", ""),   # (m>1)
    ("ence", ""),   # (m>1)
    ("er", ""),     # (m>1)
    ("ic", ""),     # (m>1)
    ("able", ""),   # (m>1)
    ("ible", ""),   # (m>1)
    ("ant", ""),    # (m>1)
    ("ement", ""),  # (m>1)
    ("ment", ""),   # (m>1)
    ("ent", ""),    # (m>1)
    ("ion", ""),    # (m>1 and (*s or *t))
    ("ou", ""),     # (m>1)
    ("ism", ""),    # (m>1)
    ("ate", ""),    # (m>1)
    ("iti", ""),    # (m>1)
    ("ous", ""),    # (m>1)
    ("ive", ""),    # (m>1)
    ("ize", "")     # (m>1)

])

step5a = collections.OrderedDict([
    ("E", ""),  # (m>1)
    ("e", ""),  # (m>1)
    ("E", ""),  # (m=1 and not *o)
    ("e", "")  # (m=1 and not *o)
])

step5b = collections.OrderedDict([
    ("L", ""),  # (m > 1 and *d and *L)
    ("l", "")  # (m > 1 and *d and *l)
])
