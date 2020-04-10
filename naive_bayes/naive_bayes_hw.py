

import pandas as pd

filename = 'C:/Users/Mig/Desktop/SMSSpamCollection.csv'

df = pd.read_csv(
    filename,
    sep='\t',
    encoding='utf8',
    header=None,
    names=['class', 'sms_text']
)

df.head(3)

num_objects, num_features = df.shape
print(num_objects, num_features)

df['class']

SPAM_CLASS = 'spam'
NOT_SPAM_CLASS = 'ham'

df['class'] == SPAM_CLASS

spam_sms_num = (df['class'] == SPAM_CLASS).sum()
notspam_sms_num = (df['class'] == NOT_SPAM_CLASS).sum()

print(spam_sms_num, notspam_sms_num)

# априорная вероятность класса спам
p_spam = spam_sms_num / num_objects

# априорная вероятность класса не спам
p_notspam = notspam_sms_num / num_objects

print(f'{p_spam:.4f}, {p_notspam:.4f}')

test_word = 'Free'.lower()

print(test_word)

sms_example = df['sms_text'].values[0]

print(sms_example)

# априорная вероятность класса спам
print(p_spam)

m = spam_sms_num / num_objects

# априорная вероятность класса не спам
p_notspam = notspam_sms_num / num_objects

print(f'{p_spam:.4f}, {p_notspam:.4f}')

# удаляем знаки препинания
import string

print(string.punctuation)

sms_example = ''.join([
    char
    for char in sms_example
    if char not in string.punctuation
])

print(sms_example)

# приводим слова к нижнему регистру


# .lower()
sms_example = ' '.join([
    word.lower()
    for word in sms_example.split(sep=' ')
])

sms_example


def text_preprocess(sms_text: str):
    """Преобразование текста для анализа"""
    text_no_punctuation = ''.join([
        char
        for char in sms_text
        if char not in string.punctuation
    ])
    text_lowercase = ' '.join([
        word.lower()
        for word in text_no_punctuation.split(sep=' ')
    ])

    return text_lowercase


sms_example = df['sms_text'].values[0]

print(text_preprocess(sms_example))

df = df.assign(
    processed_text=df['sms_text'].apply(text_preprocess)
)

df.head()

# вероятность встретить слово в спам смс

spam_test_word_entries = df[
    df['class'] == SPAM_CLASS
    ]['processed_text'].apply(
    lambda row: test_word in row
).sum()

# вероятность встретить слово в не-спам смс
notspam_test_word_entries = df[
    df['class'] == NOT_SPAM_CLASS
    ]['processed_text'].apply(
    lambda row: test_word in row
).sum()

print(f'P(word="{test_word}"|class=spam)={spam_test_word_entries/spam_sms_num:.4f}')
print(f'P(word="{test_word}"|class=not_spam)={notspam_test_word_entries/notspam_sms_num:.4f}')



sentences = df['processed_text'].str.split(" ")
#print(sentences)

from collections import defaultdict
from math import log

def train(classes, sentences):
    category, freq = defaultdict(lambda :0), defaultdict(lambda :0)
    i = 0
    for label in classes:
        category[label] += 1
        for word in sentences[i]:
            freq[label, word] += 1
        i = i + 1

    for label, word in freq:
        freq[label, word] /= category[label]

    return freq

def classify(freq, feats):
    words = text_preprocess(feats)
    result_spam = 0
    result_ham = 0
    words = words.split(" ")
    for word in words:
        result_spam += log(freq['spam', word] + 10**(-7))
        result_ham += log(freq['ham', word] + 10**(-7))

    spam = log(spam_sms_num/spam_sms_num+notspam_sms_num) + result_spam
    ham = log(notspam_sms_num/spam_sms_num+notspam_sms_num) + result_ham

    if (spam > ham):
        return "spam"
    else:
        return "ham"



freq = train(df['class'], sentences)
print(classify(freq, "Had your contract mobile 11 Mnths? Latest Motorola, Nokia etc. all FREE! Double Mins & Text on Orange tariffs. TEXT YES for callback, no to remove from records."))

print(df.values[1][1])


trainSpamSum = 0
trainHamSum = 0

for sentence in df.values:
    if(classify(freq, sentence[1]) == "spam"):
        trainSpamSum = trainSpamSum + 1
    else:
        trainHamSum = trainHamSum + 1

print(trainSpamSum/spam_sms_num)
print(trainHamSum/notspam_sms_num)


