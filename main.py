from pickle import TRUE
import urllib.request
from pprint import pprint
from unicodedata import category
import string
import random

def get_text(url):
    """
    This will be a function that gets text from the gutenberg project webpage and store it as a string of texts.
    """
    response = urllib.request.urlopen(url)
    data = response.read()  # a `bytes` object
    text = data.decode('utf-8')
    return text


def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding = 'UTF-8')

    if skip_header:
        skip_gutenberg_header(fp)

    # strippables = ''.join([chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]) #from professor's analyze_book solutions
    strippables = string.punctuation + string.whitespace

    for line in fp:
        if line.startswith('*** END OF THE PROJECT GUTENBERG EBOOK'):
            break

        line = line.replace('-', ' ')

        for word in line.split():
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1

    return hist

def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.
    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THE PROJECT GUTENBERG EBOOK'):
            break

def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    total = 0
    for freq in hist.values():
        total += freq
    return total


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)


def most_common(hist, excluding_stopwords=False):
    """Makes a list of word-freq pairs(tuples) in descending order of frequency.
    hist: map from word to frequency
    excluding_stopwords: a boolean value. If it is True, do not include any stopwords in the list.
    returns: list of (frequency, word) pairs
    """
    most = list()
    stopwords = open('data/stopwords.txt', encoding = 'utf8')
    d = dict()
    for line in stopwords:
        for word in line.split():
            d[word] = 1+ d.get(word,0)
    stops = list(d.keys())
    # print(stopwords)
    for word, freq in hist.items():
        if excluding_stopwords:
            if word in stops:
                continue

        most.append((freq, word))
    most.sort(reverse=True)
    return most

def random_word(hist):
    """Chooses a random word from a histogram.
    The probability of each word is proportional to its frequency.
    """
    t = []
    for word, freq in hist.items():
        t.extend([word] * freq)
    return random.choice(t)


def main():
    # text = get_text('https://www.gutenberg.org/cache/epub/100/pg100.txt')
    # print(text)
    hist = process_file('data/shakespeare.txt', skip_header=True)
    # print(hist)
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))

    most = most_common(hist, excluding_stopwords=True)
    # print(most)
    print('The most common words are:')
    for freq, word in most[0:20]:
        print(word, '\t', freq)

    print("\n\nHere are some random words from the book: ")
    for i in range(50):
        print(random_word(hist), end=' ')


if __name__ == '__main__':
    main()