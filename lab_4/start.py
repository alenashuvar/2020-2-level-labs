"""
Text generation implementation starter
"""

from lab_4.main import WordStorage, encode_text, LikelihoodBasedTextGenerator, decode_text
from lab_4.ngrams.ngram_trie import NGramTrie

if __name__ == '__main__':
    corpus = ('i', 'have', 'a', 'parrot', '<END>',
              'his', 'name', 'is', 'john', '<END>',
              'i', 'have', 'a', 'chinchilla', 'too', '<END>',
              'his', 'name', 'is', 'taylor', '<END>',
              'her', 'name', 'is', 'taylor', 'too', '<END>')

    storage = WordStorage()
    storage.update(corpus)

    encoded = encode_text(storage, corpus)

    trie = NGramTrie(3, encoded)

    context = (storage.get_id('i'),
               storage.get_id('have'),)

    generator = LikelihoodBasedTextGenerator(storage, trie)

    generated_text = generator.generate_text(context, 3)
    RESULT = decode_text(storage, generated_text)

    assert RESULT == ('I have a parrot',
                      'His name is taylor',
                      'Her name is taylor'), 'Text generator does not work'
