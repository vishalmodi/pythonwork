import unittest
import re

class MyTestCase(unittest.TestCase):

    book_name = "2638-0.txt"
    # def setUpClass(cls) -> None:
    #     # with open("2638-0.txt",r) as book:
    #
    #
    # def tearDownClass(cls) -> None:
    #     pass

    # def test_something(self):
    #     self.assertEqual(True, False)

    def test_the_pronoun_count_raw(self):
        line_count = 0
        word_count = 0
        pattern = re.compile(r"The")

        with open(self.book_name, "r") as book:
            for no, line in enumerate(book):
                # matches = pattern.findall(line)
                matches = re.sub(pattern, "1The", line)
                print(matches)
                for match in matches:
                    word_count += 1
                    # print(match)
                line_count = no

        print('No of lines: ', line_count)
        print('No of word: ', word_count)

    def readInChunks(self, fileobj, chunksize=2048):
        """
        Lazy function to read a file piece by piece.
        Default chunk size: 2kB.

        """
        while True:
            data = fileobj.read(chunksize)
            if not data:
                break
            yield data

    def test_the_pronoun_count(self):
        pattern = re.compile(r"The")
        with open(self.book_name, "r") as book:
            line = book.readline()
            while line:
                # matches = re.finditer(pattern, line)
                matches = pattern.finditer(line)
                # print(len(matches))
                for match in matches:
                    print(match.group())
                line = book.readline()


if __name__ == '__main__':
    unittest.main()
