import unittest
import re


class TestLogSummary(unittest.TestCase):
    log = r"""03/22 08:51:01 INFO   :...config file: Specified configuration file: system.conf
      03/22 08:51:01 INFO   :.main: Using log level 611
      03/22 08:51:01 EXCEPTION   :..getip: Get TCP images rc - EDC8112I Operation not supported on socket.
      03/22 08:51:01 ERROR   :..getip: Associate with TCP/IP image name = TCPCS 
      03/22 08:51:02 INFO   :..set request: registering process with the system
      03/22 08:51:02 ERROR   :..set request: attempt OS/390 registration
      03/22 08:51:02 INFO   :..set request: return from registration rc=0"""

    def test_log_type_summary(self):
        print('output:', read_log(self.log))


def log_parser(log_line, output):
    # pattern = re.compile("INFO\s+:|ERROR\s+:|EXCEPTION\s+:")
    pattern = re.compile("(INFO|ERROR|EXCEPTION)+(\s+:)")

    matches = pattern.finditer(log_line)
    for match in matches:
        output[match.group(1)] += 1


def read_log(log):
    output = dict()
    output['INFO'] = 0
    output['ERROR'] = 0
    output['EXCEPTION'] = 0

    # loop through the entire log, line by line
    log_lines = log.split('\n')

    for log_line in enumerate(log_lines):
        log_parser(log_line[1], output)

    max_log_types = []
    max_log_type = max(output.items(), key=lambda item: item[1])

    for log_type_key, count in output.items():
        if count == max_log_type[1]:
            max_log_types.append((log_type_key, count))

    # return max log type and its count
    return max_log_types

