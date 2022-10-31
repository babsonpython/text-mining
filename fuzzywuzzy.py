import fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

a = fuzz.ratio('wilson', 'Wilson')
print(a)