import os

import linguistica as lxa

data_dir = os.path.join(os.path.dirname(__file__), 'data')
corpus_path = os.path.join(data_dir, 'english-brown.txt')

lxa_object = lxa.read_corpus(corpus_path, max_word_tokens=50000)


def test_words_to_neighbors():
    test_object = lxa_object.words_to_neighbors()

    expected_object_path = os.path.join(data_dir, 'words_to_neighbors.txt')
    expected_object = eval(open(expected_object_path).read())

    for word in test_object.keys():
        assert test_object[word] == expected_object[word]


def test_words_to_contexts():
    test_object = lxa_object.words_to_contexts()

    expected_object_path = os.path.join(data_dir, 'words_to_contexts.txt')
    expected_object = eval(open(expected_object_path).read())
    assert test_object == expected_object


def test_contexts_to_words():
    test_object = lxa_object.contexts_to_words()

    expected_object_path = os.path.join(data_dir, 'contexts_to_words.txt')
    expected_object = eval(open(expected_object_path).read())
    assert test_object == expected_object
