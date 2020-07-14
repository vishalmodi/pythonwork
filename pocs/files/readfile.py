import re


class ReadFile:
    def __init__(self, filename):
        self.filename = filename

    def get_line_count(self):
        with open(self.filename, "r") as file:
            count = 0
            for _ in file:
                count += 1
            return count

    def get_urls(self):
        unique_ips = set()
        # pattern = re.compile("(https?)://(www).?((\w)*)\.(\w)*")
        # pattern = re.compile("(?P<url>((http[s]?))://(www\.)?)+(?P<domain>((\w+)*))\.(\w)*/([\w\-\.])+")
        pattern = re.compile("(?P<url>((http[s]?))://(www\.)?)+(?P<domain>((\w+)*))\.(\w)*")
        with open(self.filename, "r") as log:
            for _, line in enumerate(log):
                matches = pattern.finditer(line)
                for match in matches:
                    unique_ips.add(match.group('domain'))
        print("Unique Ips len :", len(unique_ips))
        print("Unique Ips :", unique_ips)

    def update_url(self):
        callback = lambda pat: pat.group().upper()
        pattern = re.compile("(?P<url>((http[s]?))://(www\.)?)+(?P<domain>((\w+)*))\.(\w)*")
        with open(self.filename, "r") as log:
            for _, line in enumerate(log):
                print(re.sub(pattern, callback, line))

    def get_ips(self):
        unique_ips = set()
        # pattern = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
        pattern = re.compile("(\d{1,3}\.){3}(\d{1,3})")
        with open(self.filename, "r") as log:
            for _, line in enumerate(log):
                matches = pattern.finditer(line)
                for match in matches:
                    unique_ips.add(match.group())
                    # print(match.group())
        print("Unique Ips len :", len(unique_ips))
        print("Unique Ips :", unique_ips)


readfile = ReadFile("../external/webserver_small.log")
readfile.update_url()
