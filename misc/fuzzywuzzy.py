import fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

a = fuzz.ratio('wilson', 'Wilson')
print(a)

#ImportError: cannot import name 'fuzz' from partially initialized module 'fuzzywuzzy' (most likely due to a circular import)