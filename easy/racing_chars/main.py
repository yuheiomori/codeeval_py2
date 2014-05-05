# coding=utf-8
import sys


PASSING_TYPE_STRAIGHT = '|'
PASSING_TYPE_LEFT_TURN = '\\'
PASSING_TYPE_RIGHT_TURN = '/'

ROAD_TYPE_GATE = '_'
ROAD_TYPE_CHECKPOINT = 'C'


class RacingChars(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.last_pos = -1
        self.next_pos = -1
        self.next_type = ''

    def run(self):
        test_cases = open(self.file_name, 'r')
        for line in test_cases:
            if not bool(line):
                continue
            self.pass_by(line)
        test_cases.close()

    def pass_by(self, line):
        self.find_next(line)
        way_of_passing = self.decide_way_of_passing()
        self.last_pos = self.next_pos

        line = line.replace(self.next_type, way_of_passing)
        print line.rstrip()

    def find_next(self, s):
        gate_pos, checkpoint_pos = s.find("_"), s.find("C")

        if checkpoint_pos != -1:
            self.next_pos = checkpoint_pos
            self.next_type = ROAD_TYPE_CHECKPOINT
        else:
            self.next_pos = gate_pos
            self.next_type = ROAD_TYPE_GATE

    def decide_way_of_passing(self):
        way_of_passing = PASSING_TYPE_STRAIGHT
        if self.last_pos != -1:
            if self.next_pos > self.last_pos:
                way_of_passing = PASSING_TYPE_LEFT_TURN
            elif self.next_pos < self.last_pos:
                way_of_passing = PASSING_TYPE_RIGHT_TURN
        return way_of_passing


def main():
    RacingChars(sys.argv[1]).run()


if __name__ == '__main__':
    main()
