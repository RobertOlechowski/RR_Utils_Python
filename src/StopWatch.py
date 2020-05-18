import time


class StopWatch:
    def __init__(self, auto_start=True):
        self._start_time = None
        if auto_start:
            self.reset()

    def reset(self):
        self._start_time = time.time()

    def get_start_time(self):
        return self._start_time

    def compute_elapsed(self):
        delta = time.time() - self._start_time
        return delta


