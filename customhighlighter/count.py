#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import colorsys
import nltk
import re
import sys
from rikeripsum import rikeripsum

all_paragraphs = {}
paragraph_length_min = sys.maxint
paragraph_length_max = 0
paragraph_length_range = 0
paragraph_accumulated_length = 0
paragraph_length_average = 0.0
number_of_paragraphs = 0

all_sentences = {}
sentence_length_min = sys.maxint
sentence_length_max = 0
sentence_length_range = 0
sentence_accumulated_length = 0
sentence_length_average = 0.0
number_of_sentences = 0

all_words = {}
word_length_min = sys.maxint
word_length_max = 0
word_length_range = 0
word_accumulated_length = 0
word_length_average = 0.0
number_of_words = 0
words_rejected = []

hsv_blue = colorsys.rgb_to_hsv(0.5, 0.5, 1.0)
hsv_red = colorsys.rgb_to_hsv(1.0, 0.5, 0.5)
h_min = hsv_blue[0]
h_max = hsv_red[0]
h_range = h_max - h_min

text = u'He saîd: "No!" He saîd: "No!" and wàlked a-way.\n\nHe saîd: “No!” and wàlked a-way.\n\nHe asked: "Really?" He asked: "Really?" and wàlked a-way.\n\nHe asked: „Really?” and wàlked a-way. He asked: „Really?” and wàlked a-way. Hij heeft bureau- en kastladen, maar ook maandagochtend en -middag. Blah \'s-Hertogenbosch blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah,  blah blah blah blah blah blah blah.\n\nBlah \'s-Hertogenbosch blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah.'

of = codecs.open('test.html', 'w', 'utf-8')
of.write("""<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
<title>test</title>
</head>
<body>
""")

#of.write('<pre>%s</pre>\n' %text)

paragraphs = nltk.LineTokenizer().tokenize(text)
print 'Total paragraphs:', len(paragraphs)
for paragraph in paragraphs:
    paragraph_length = len(paragraph)
    paragraph_accumulated_length += paragraph_length
    if paragraph_length > paragraph_length_max:
        paragraph_length_max = paragraph_length
    if paragraph_length < paragraph_length_min:
        paragraph_length_min = paragraph_length
    number_of_paragraphs += 1

    if paragraph in all_paragraphs:
        data = all_paragraphs[paragraph]
        all_paragraphs[paragraph] = (data[0], data[1] + 1)
    else:
        all_paragraphs[paragraph] = (len(paragraph), 1)

    sentences = nltk.tokenize.sent_tokenize(paragraph)
    for sentence in sentences:
        sentence_length = len(sentence)
        sentence_accumulated_length += sentence_length
        if sentence_length > sentence_length_max:
            sentence_length_max = sentence_length
        if sentence_length < sentence_length_min:
            sentence_length_min = sentence_length
        number_of_sentences += 1

        if sentence in all_sentences:
            data = all_sentences[sentence]
            all_sentences[sentence] = (data[0], data[1] + 1)
        else:
            all_sentences[sentence] = (len(sentence), 1)

        print sentence
        words = nltk.tokenize.word_tokenize(sentence)#FIXME accepteer à etc als deel van een woord
#        pattern = r'''(?x)    # set flag to allow verbose regexps
#            ([A-Z]\.)+        # abbreviations, e.g. U.S.A.
#            | \w+(-\w+)*        # words with optional internal hyphens
#            | \$?\d+(\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
#            | \.\.\.            # ellipsis
#            | [][.,;"'?():-_`]  # these are separate tokens
#            '''
#        words = nltk.regexp_tokenize(sentence, pattern)
        
        print words
        for word in words:
            if re.match(u'^[\'-0-9A-Za-zÁáÀàÂâÄäÅåÉéÈèÊêËëÍíÎîÏïÓóÒòÔôÖöØøÚúÛûÜüÇçÑñ]+$', word):
                word_length = len(word)
                word_accumulated_length += word_length
                if word_length > word_length_max:
                    word_length_max = word_length
                if word_length < word_length_min:
                    word_length_min = word_length
                number_of_words += 1
    
                if word in all_words:
                    data = all_words[word]
                    all_words[word] = (data[0], data[1] + 1)
                else:
                    all_words[word] = (len(word), 1)
            else:
                if word not in words_rejected:
                    words_rejected.append(word)

of.write('<h1>Paragraph length</h1>\n')
paragraph_length_average = float(paragraph_accumulated_length) / number_of_paragraphs
paragraph_length_range = paragraph_length_max - paragraph_length_min
print 'minimum paragraph length', paragraph_length_min
print 'maximum paragraph length', paragraph_length_max
print 'average paragraph length', paragraph_length_average

for paragraph in all_paragraphs.keys():
    data = all_paragraphs[paragraph]
    h = h_min + ((float(data[0]) - paragraph_length_min) / paragraph_length_range * h_range)
    c = colorsys.hsv_to_rgb(h, hsv_blue[1], hsv_blue[2])
    c_hex = '%02x%02x%02x' %(int(c[0]*255), int(c[1]*255), int(c[2]*255))
    data = (data[0], data[1], c_hex)
    all_paragraphs[paragraph] = data
    print all_paragraphs[paragraph]

for paragraph in nltk.LineTokenizer().tokenize(text):
    of.write('<p><span style="background-color:#%s;">%s</span></p>\n' %(all_paragraphs[paragraph][2], paragraph))

of.write('<h1>Sentence length</h1>\n')
sentence_length_average = float(sentence_accumulated_length) / number_of_sentences
sentence_length_range = sentence_length_max - sentence_length_min
print 'minimum sentence length', sentence_length_min
print 'maximum sentence length', sentence_length_max
print 'average sentence length', sentence_length_average

for sentence in all_sentences.keys():
    data = all_sentences[sentence]
    h = h_min + ((float(data[0]) - sentence_length_min) / sentence_length_range * h_range)
    c = colorsys.hsv_to_rgb(h, hsv_blue[1], hsv_blue[2])
    c_hex = '%02x%02x%02x' %(int(c[0]*255), int(c[1]*255), int(c[2]*255))
    data = (data[0], data[1], c_hex)
    all_sentences[sentence] = data
    print all_sentences[sentence]
    of.write('<span style="background-color:#%s;">%s</span><br/>\n' %(c_hex, sentence))

of.write('<h1>Word length</h1>\n')
of.write('<table>\n')
of.write('<tr><th>length</th><th>frequency</th><th>word</th></tr>\n')
word_length_average = float(word_accumulated_length) / number_of_words
word_length_range = word_length_max - word_length_min
print 'minimum word length', word_length_min
print 'maximum word length', word_length_max
print 'average word length', word_length_average

for word in all_words.keys():
    data = all_words[word]
    h = h_min + ((float(data[0]) - word_length_min) / word_length_range * h_range)
    c = colorsys.hsv_to_rgb(h, hsv_blue[1], hsv_blue[2])
    c_hex = '%02x%02x%02x' %(int(c[0]*255), int(c[1]*255), int(c[2]*255))
    data = (data[0], data[1], c_hex)
    all_words[word] = data
    print word, all_words[word]
    of.write('<tr><td>%s</td><td>%s</td><td><span style="background-color:#%s;">%s</span></td></tr>\n' %(data[0], data[1], c_hex, word))

of.write('<table>\n')

print 'Rejected:', ' '.join(words_rejected)

of.write("""</body>
</html>""")

#'%s\n' %line.decode('utf-8'))#om utf te schrijven





#print 'total sentences:', len(re.findall(r'[\.\!\?]+', a))
#print 'total words:', len(re.findall(r'\w+', a))+1
#ps = re.split(r'\w*\n+\w*', a)
#print ps
#print 'total paragraphs:', len(ps)
#  ss = re.split(r'\. ', p)
#  print 'sentences:', len(ss)
#  for s in ss:
#    w = re.findall(r'\w+', ss)
#    print 'words:', len(w)
#[^.!?\s][^.!?]*(?:[.!?](?!['"]?\s|$)[^.!?]*)*[.!?]?['"]?(?=\s|$)

#    punkt_param = nltk.tokenize.punkt.PunktParameters()
#    punkt_param.abbrev_types = set(['dr', 'vs', 'mr', 'mrs', 'prof', 'inc'])
#    sentence_splitter = nltk.tokenize.punkt.PunktSentenceTokenizer(punkt_param)
#    sentences = sentence_splitter.tokenize(paragraph)
  
#    print 'Total sentences in paragraph:', len(sentences)

print rikeripsum.generate_paragraph()