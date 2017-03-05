""" A generator for random books"""

import os
import sys
import termios


import random
import string


class BooksReader:

    """BooksReader"""

    def __init__(self):
        pass

    def read_books(self, book_path="book", buffer=4096):

        """read_books"""

        for root, _, files in os.walk(book_path):

            for file_name in files:
                with open('{}/{}'.format(root, file_name)) as file_fd:

                    while True:
                        parts = file_fd.read(buffer)

                        if parts:
                            yield parts

                        else:
                            break

                file_fd.close()

    # http://stackoverflow.com/questions/983354/how-do-i-make-python-to-wait-for-a-pressed-key/34956791#34956791
    def wait_key(self):

        """ Wait for a key press on the console and return it. """

        file_fd = sys.stdin.fileno()

        oldterm = termios.tcgetattr(file_fd)
        newattr = termios.tcgetattr(file_fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(file_fd, termios.TCSANOW, newattr)

        try:

            result = sys.stdin.read(1)
            result = True if result == ' '  else False

        except IOError:
            pass

        finally:
            termios.tcsetattr(file_fd, termios.TCSAFLUSH, oldterm)

        return result

    def display_books(self):

        """display_books"""

        for content in self.read_books():

            print(content)
            print('\n--- Press "space" to scroll down or any other keys to quit ---')

            space_key = self.wait_key()

            if space_key is True:
                continue
            else:
                break


class BooksGenerator:

    """BooksGenerator"""

    def __init__(self, chapters_count: int, chapter_words_range: tuple) -> None:
        """__init__

        :param chapters_count:
        :type chapters_count: int
        :param chapter_words_range:
        :type chapter_words_range: tuple

        :rtype: None
        """

        self.chapters_count = chapters_count
        self.w_start, self.w_stop = chapter_words_range

        self.w_trashhold = 11

    def _get_range(self, start: int, stop: int) -> int:

        """get_words_range

        :param start:
        :type start: int
        :param stop:
        :type stop: int

        :rtype: int
        """
        return random.randrange(start, stop)

    def _get_words_per_chapter(self):

        """get_total_words
        will generate random number of words per chapter
        """
        return [self._get_range(self.w_start, self.w_stop) for x in range(self.chapters_count)]

    def _get_alphabet(self):

        """get_alphabet"""

        return string.ascii_lowercase

    def _get_shuffled_alpha_population(self):

        """_get_shuffled_alpha_population"""

        population = list(self._get_alphabet()) * 1000
        random.shuffle(population)

        return population

    def _get_words_per_line(self):
        """_get_line_range"""
        return self._get_range(12, 16)

    def _get_words_range(self, words_chapter: list) -> list:
        """_get_words_range

        :param words_chapter:
        :type words_chapter: list

        :rtype: list
        """

        for x in words_chapter:
            temp = []
            for y in range(x):
                temp.append(self._get_range(1, 10))
            yield temp

    def process(self):

        """process"""

        population = self._get_shuffled_alpha_population()

        words_per_chapter = self._get_words_per_chapter()
        words_range = self._get_words_range(words_per_chapter)

        # words loop

        for w_range in words_range:

            counter = 0

            chapter_buffer = list()

            with open('book/emoov-book.txt', 'a') as file_fd:

                for _range in w_range:
                    word = ''.join(random.sample(population, _range))

                    if counter == 0:
                        word = '{}{}{}'.format('# ', word, '\n')

                    counter += 1
                    chapter_buffer.append(word)

                    if len(chapter_buffer) >= self.w_trashhold:

                        if len(chapter_buffer) >= self._get_words_per_line():
                            line = ' '.join(chapter_buffer).lstrip()+'\n'

                            file_fd.write(line)
                            chapter_buffer = list()

                file_fd.write('\n\n')
            file_fd.close()

