import sys


class ConsoleLogger(object):
    def __init__(self):
        self.log_destination = [sys.stdout]

    def add_log_file(self, filename):
        self.log_destination.append(open(filename, "a"))

    def remove_last_log_file(self):
        if len(self.log_destination) <= 1:
            raise Exception()
        last = self.log_destination.pop()
        last.flush()
        last.close()

    def write(self, message):
        for item in self.log_destination:
            item.write(message)

    def flush(self):
        for item in self.log_destination:
            item.flush()
