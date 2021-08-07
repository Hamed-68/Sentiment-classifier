
# ============================= CHECK WORDS =============================
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


def strip_punctuation(word):
    """ check words, and if contain punctuation_chars delet that characters """
    for c in punctuation_chars:
        if c in word:
            word = word.replace(c, '')
    return word


# ============================= POSITIVE WORDS =============================
positive_words = []
with open('positive_words.txt', 'r') as pos:
    for line in pos.readlines():
        if line != '\n' and line[0] != ';' and len(line) < 29:
            positive_words.append(line.strip())


def get_pos(sentence):
    """ check if words in sentence are in positive_words list. then return
    number of words """
    count_pos = 0
    for w in sentence.split():
        word = strip_punctuation(w)
        if word in positive_words:
            count_pos += 1
    return count_pos


# ============================= NEGATIVE WORDS =============================
negative_words = []
with open('negative_words.txt', 'r') as neg:
    for line in neg.readlines():
        if line[0] != ';' and line != '\n':
            negative_words.append(line.strip())


def get_neg(sentence):
    """ check if words in sentence are in negative_words list. then return
    number of words """
    count_neg = 0
    for w in sentence.split():
        word = strip_punctuation(w)
        if word in negative_words:
            count_neg += 1
    return count_neg


# ============================= CLASSIFIER =============================
with open('project_twitter_data.csv', 'r') as twitter:
    lines = twitter.readlines()[1:]
    with open('resulting_data.csv', 'w') as res:
        header = res.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n')
        for line in lines:
            res.write(line.split(',')[1]+', ')
            res.write(line.strip().split(',')[2]+', ')
            res.write(str(get_pos(line.split(',')[0]))+', ')
            res.write(str(get_neg(line.split(',')[0]))+', ')
            res.write(str(get_pos(line.split(',')[0]) - get_neg(line.split(',')[0])))
            res.write('\n')
