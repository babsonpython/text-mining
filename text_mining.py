import urllib.request
from pprint import pprint
import random
import string

def get_text():
    """
    This will be a function that gets text from the gutenberg project webpage.
    """
    url = 'https://www.gutenberg.org/files/2130/2130-0.txt'
    with urllib.request.urlopen(url) as f:
        response = urllib.request.urlopen(url)
        data = response.read()  # a `bytes` object
        text = data.decode('utf-8')
    return text # for testing


def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding='UTF8')

    if skip_header:
        skip_gutenberg_header(fp)

    strippables = string.punctuation + string.whitespace

    for line in fp:
        if line.startswith('*** END OF THE PROJECT GUTENBERG EBOOK UTOPIA ***'):
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
        if line.startswith('*** START OF THE PROJECT GUTENBERG EBOOK UTOPIA ***'):
            break

def main():
    text = get_text()
    # print(text)
    hist = process_file(text, skip_header=True)
    print(hist)
    # print('Total number of words:', total_words(hist))
    # print('Number of different words:', different_words(hist))
    # print_most_common(hist, num =10)

    # t = most_common(hist, excluding_stopwords=True)
    # print('The most common words are:')
    # for freq, word in t[0:20]:
    #     print(word, '\t', freq)

    # words = process_file(text, skip_header=False)

    # diff = subtract(hist, words)
    # print("The words in the book that aren't in the word list are:")
    # for word in diff.keys():
    #     print(word, end=' ')

    # print("\n\nHere are some random words from the book")
    # for i in range(100):
    #     print(random_word(hist), end=' ')


if __name__ == '__main__':
    main()