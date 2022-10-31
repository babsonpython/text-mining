# text-mining

Please read the [instructions](instructions.md).

Project Overview:
    When I first approached this project I was very interested in the Markov's analysis and its text synthesis which is why I chose William Shakespeare as the source and I wanted to create sentences or paragraphs in Shakespearian English. When I first searched the William Shakespeare in the Gutenberg library, I found a collection of all his works on there so I thought it would be perfect in trying to get a huge sample size of his works and doing some analysis on what words he use most. So I downloaded the plain text version of the collection and used text file to run them in vscode. So by defining a function process file, I could analyze multiple number of Shakespeare's works by simply changing adding the string of the name of the text file I want to analyze. (e.g. romeo.txt)

Implementation:
    So after I downloaded different texts from Gutenberg, I used the proess_file function to strip all the unnecessary components we don't need to analyze the book. The function returns a dictionary of words and integer pair that indicates the frequency a word has shown up in the text. Using dictionary here is the most acceptable because it provides us with the best data structure to represent a key-value pair in order to count the number of words in a text.

    After getting a dictionary of key-value pair which is defined as hist, I wanted to find out the total number of words and the most common words in the text. So for total number its simply the sum of all the frequencies of the words in the hist dictionary and the most common words basically creating a list of words and its frequency in a descending order. However, when I returned the result, I realized that there were lots of words such as 'the','and','i' that are generic so i decided to filter out these generic words by creating a new dictionary of stopwords. By doing this, I can figure out what are some unique words Shakespeare uses in his writings. I also created a random sentence generator that simply takes 100 random words from the keys of the dictionary and combines them in a list. However, the result of the sentence is very unreadable because it makes zero grammatical sense. This is why I wanted to try and utilize the Markov's analysis in creating sentences or phrases that make sense.

Results:
    In terms of general stastical results on the entire collection of Shakespeare, Hamlet, and Romeo and Juliet respectively:
        Total Number of words in the entire collection of Shakespeare: 963318 words, 32068 words, 26082 words
        Total Number of different words: 32461 words, 4957 words, 3844 words
    
    In terms of top 20 most common words:
        In the entire collection of Shakespeare:
            thou     5840
            will     5281
            thy      4337
            shall    3844
            thee     3386
            lord     3155
            now      2997
            sir      2977
            good     2971
            king     2964
            come     2630
            enter    2474
            o        2472
            well     2377
            love     2311
            let      2226
            hath     2052
            like     2028
            one      1958
            man      1940
        In Hamlet:
            hamlet   459
            lord     220
            king     194
            will     169
            horatio  154
            polonius 120
            shall    114
            o        110
            good     106
            come     105
            laertes  104
            thou     102
            now      98
            let      94
            thy      86
            ophelia  86
            like     83
            rosencrantz 78
            well     75
        In Romeo & Juliet:
            romeo    298
            thou     277
            juliet   178
            thy      170
            o        149
            will     148
            capulet  141
            love     139
            thee     135
            shall    110
            lady     109
            friar    104
            come     94
            good     84
            mercutio 83
            enter    81
            now      80
            benvolio 79
            go       76
    From the most common unique words in the entire collection of Shakespeare's, we can see that the use of old english is prevalent, such as 'thou', 'thee','shall' which are words that we would use if we wrote in Shakespearian English. And unsurprisingly, the most common unique word in Hamlet is 'hamlet' and in Romeo & Juliet it's 'romeo'. And we can see that the word 'thou' is used the most in his writings.

    In terms of randomly generated sentences, here is an example: "heaven exeter arabia my cause my son day doublet it give to i child me public me i’ll and as for this let at many yet in for squar’d will hell point a you a shall kissed—the is impediment trembling within suddenly that near or worst blood is you of"... which does not make much sense.

    However, after using the Markov's code provided by the professor, I managed to create some interesting phrases such as: ’tis time you were so pleased that hast slaine The Sith-tuskd Bore; that with patience to us, call my father had a husband I have need of thee!’ and by thy patient’s side, And fall something into a quarrel openly? Full well hath prayed, and prove a jolly march; Bear." It does not make much sense but definitely sounds more sophisticated with the prefix and suffixes in the right places.

Reflection:
    Overall I think this was a really good real life exercise to see some of the real life implementations of python that we can do. However, I wish I knew more about the different programs such as fuzzywuzzy or nltk before starting this assignment because I spent a lot of time trying to install those and eventually broke my pip install thing which I still need to consult you about. I feel like its through these exercises and assignments to find out what my flaws and weaknesses are. For example, I learned so much from my mistakes while completing this assignment such as making simple mistakes like not saving a text file before running it. Even though the code itself wasn't the hardest (except for Markov), it really requires me to pay attention to every aspect of my code within the module or even outside of it. Even though I didn't get a chance to try NLTK or Fuzzywuzzy, I really liked how to use these external modules to do cool things with the data. Overall, I think this was a valuable exercise where the process_file function I could use anytime in the future.




