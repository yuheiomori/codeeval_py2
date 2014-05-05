# coding=utf-8
import Queue
import sys
import time


class Time(object):
    def __init__(self, epoch, start=True):
        self.epoch = epoch
        self.start = start

    def is_start(self):
        return self.start


class TimeList(object):
    def __init__(self):
        self.time_list = []

    def add(self, s, e):
        self.time_list.append(Time(s, True))
        self.time_list.append(Time(e, False))

    def calc_total_months(self):

        self.time_list = sorted(self.time_list, key=lambda e: e.epoch)

        all_months = 0
        queue = Queue.LifoQueue()

        for t in self.time_list:
            if t.is_start():
                queue.put_nowait(t)
            else:
                end_time = queue.get_nowait()
                if queue.qsize() == 0:
                    months_diff = round(((t.epoch - end_time.epoch) / 3.15569e7 * 12) + 1)
                    all_months += months_diff

        return all_months

    def calc_total_years(self):
        return int(self.calc_total_months() / 12)


def solve(spans):
    tl = TimeList()
    for span in spans:
        s, e = [int(time.mktime(time.strptime(e, "%b %Y"))) for e in span.split("-")]
        tl.add(s, e)

    print tl.calc_total_years()


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    line = test.rstrip()
    solve([elem.strip() for elem in line.split(";")])

test_cases.close()
