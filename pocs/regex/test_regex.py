import unittest
import re


class MyTestCase(unittest.TestCase):
    def test_something(self):
        pattern = r"Cookie"
        sequence = "Cookie"

        re.match(pattern, sequence)
        self.assertNotEqual(None, re.match(pattern, sequence))

    def test_period(self):
        pattern = r"Co.k.e"
        sequence = "Abc Cookie z Cookie"

        x = re.search(pattern, sequence)
        y = re.search(pattern, sequence).group()
        self.assertEqual(re.search(pattern, sequence).group(), "Cookie")

    def test_a(self):
        print("Lowercase w:", re.search(r'Co\wk\we', 'Cookie').group())
        print("Lowercase w:", re.search(r'Co\w+k\we', 'Coooookie Coooookie').group())
        print("Lowercase w1:", re.search(r'Co\w+k\we', 'Co2kie Co1kie').group())

        ## Matches any character except single letter, digit or underscore
        print("Uppercase W:", re.search(r'C\Wke', 'C@ke').group())

        print("Lowercase s:", re.search(r'Eat\scake', 'Eat cake').group())
        print("Uppercase S:", re.search(r'cook\Se', "Let's eat cookie").group())

        # # Example for \t
        # print("\\t (TAB) example: ", re.search(r'Eat\ncake', r'Eatcake').group())

        # Example for \b
        print("\\b match gives: ", re.search(r'\b[A-E]ookie', 'Cookie').group())
        print("\\Z match gives: ", re.search(r'Cooki\s[A-Z]\Z', 'Cooki E').group())

    def test_repeat(self):
        print("\d{9,10} ", re.search(r'\d{9,10}', '0987654321').group())
        print("\d{9} ", re.search(r'\d{9}', '0987654321').group())
        print("\d{4,} ", re.search(r'\d{4}', '09a87654321').group())

    def test_group(self):
        statement = 'Please contact us at: support@datacamp.com'
        match = re.search(r'([\w\.-]+)(@)([\w\.-]+)', statement)
        if statement:
            print("Email address:", match.group())  # The whole matched text
            print("Username:", match.group(1))  # The username (group 1)
            print("@:", match.group(2))  # The @ (group 2)
            print("Host:", match.group(3))  # The host (group 3)
            print("group(1,2)", match.group(0, 1))

    def test_named_groups(self):
        statement = 'Please contact us at: support@datacamp.com'
        match = re.search(r'(?P<email>(?P<username>[\w\.-]+)@(?P<host>[\w\.-]+))', statement)
        if statement:
            print("Email address:", match.group('email'))
            print("Username:", match.group('username'))
            print("Host:", match.group('host'))

    def test_findall(self):
        statement = "Please contact us at: support@datacamp.com, xyz@datacamp.com"

        # 'addresses' is a list that stores all the possible match
        addresses = re.findall(r'[\w\.-]+@[\w\.-]+', statement)
        for address in addresses:
            print(address)

    def test_finditer(self):
        statement = "Please contact us at: support@datacamp.com, xyz@datacamp.com"
        # 'addresses' is a list that stores all the possible match
        addresses = re.finditer(r'[\w\.-]+@[\w\.-]+', statement)
        for address in addresses:
            print(address)
            print(address.group())

