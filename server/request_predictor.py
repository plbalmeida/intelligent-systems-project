#!/usr/bin/python
# -*- coding: utf-8 -*-


# sys and data processing libs
import os
import sys
import nltk
import re
import json
import pickle

# nlp data corpus and libs
nltk.data.path.append(os.getenv('NLTK_DIR_PATH'))
nltk.download('punkt', download_dir= os.getenv('NLTK_DIR_PATH'))
nltk.download('stopwords', download_dir= os.getenv('NLTK_DIR_PATH'))
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from string import punctuation
from nltk.probability import FreqDist

# Data modeling and data transform
from scipy import sparse as sp_sparse
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np

class requestPredictor:

    def __init__(self, df):
        self.request_data = df
        self.predict = self.getPredict()


    def joinStringColumns(self):
        '''
        join qyery, title and concatened_tags columns
        '''

        f_join_strings = lambda row: row['query'] + ' ' + row['title'] \
            + ' ' + row['concatenated_tags']

        return self.request_data.assign(full_text=f_join_strings)


    def normalizeFullText(self):
        """
        Data normalization.
        """


        def normalize_text(s):
            """
            Lower text and remove punctuation, articles and extra whitespace.
            """


            def compost_words(text):
                text = re.sub('[/]', ' ', str(text))
                text = re.sub('[-]', ' ', str(text))
                return text


            def white_space_fix(text):
                return ' '.join(text.split())


            def remove_punc(text):
                exclude = set(punctuation)
                return ''.join(ch for ch in text if ch not in exclude)


            def lower(text):
                return text.lower()


            def remove_stop_words(text):
                # this import in this part of the code was necessary to not give an error
                from nltk.corpus import stopwords
                stopwords = set(stopwords.words('portuguese')
                                + list(punctuation) + list('/'))
                palavras = word_tokenize(text)
                palavras_sem_stopwords = [palavra for palavra in
                        palavras if palavra not in stopwords]
                return ' '.join(palavras_sem_stopwords)

            return remove_stop_words(white_space_fix(remove_punc(lower(compost_words(s)))))

        normalized_request_data = self.joinStringColumns()

        normalized_request_data['full_text'] = list(map(normalize_text,
                list(normalized_request_data['full_text'])))

        return normalized_request_data


    def getBagOfWordsSparse(self):
        '''
        represent words in a corpus in a numeric format for multilabel classification.
        '''


        def my_bag_of_words(text, words_to_index, dict_size):
            """
            text: a string
            dict_size: size of the dictionary
            return a vector which is a bag-of-words representation of 'text'
            """

            result_vector = np.zeros(dict_size)
            for word in text.split(' '):
                if word in words_to_index:
                    result_vector[words_to_index[word]] += 1
            return result_vector

        request_data = self.normalizeFullText()
        DICT_SIZE = int(os.getenv('DICT_OF_WORDS_SIZE'))
        WORDS_TO_INDEX = pickle.load(open(os.getenv('WORDS_TO_INDEX'),
                'rb'))

        request_mybag = \
            sp_sparse.vstack([sp_sparse.csr_matrix(my_bag_of_words(text,
                             WORDS_TO_INDEX, DICT_SIZE)) for text in
                             request_data.full_text])

        return request_mybag


    def getPredict(self):
        '''
        return json with predictions
        '''


        def from_array_to_labels(request_predicted):
            '''
            predicted arrays to string.
            ex.
                [1,0,0,0,0,0] -> 'Bebê'
            '''

            request_predicted = list(map(np.argmax, request_predicted.tolist())) 
            return [eval(os.getenv('LABELS_LIST'))[x] for x in request_predicted]

        request_data = self.getBagOfWordsSparse()
        classifier = pickle.load(open(os.getenv('MODEL_PATH'), 'rb'))
        request_predicted = classifier.predict(request_data)
        request_predicted = from_array_to_labels(request_predicted)

        return {"categories": request_predicted}
