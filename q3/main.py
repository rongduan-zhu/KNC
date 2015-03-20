#!/usr/bin/env python

def is_valid(first, last, rolling_range):
    if first < 1 or first > last:
        return False
    if rolling_range < 0:
        return False
    return True

def pre_ellipsis(rolling_range):
    if rolling_range[0] == 1:
        return ""
    elif rolling_range[0] == 2:
        return "1 "
    else:
        return "1 ... "

def post_ellipsis(rolling_range, last):
    if rolling_range[-1] == last:
        return ""
    elif rolling_range[-1] == last - 1:
        return " " + str(last)
    else:
        return " ... " + str(last)


def solve_line(line):
    first, last, rolling = map(int, line.split(','))
    if not is_valid(first, last, rolling):
        return "ERR"

    rolling_range_head = first - rolling if first - rolling > 0 else 1
    rolling_range_tail = first + rolling if first + rolling <= last else last

    rolling_range = range(rolling_range_head, rolling_range_tail + 1)

    output_head = pre_ellipsis(rolling_range)
    output_tail = post_ellipsis(rolling_range, last)
    output_middle = " ".join(map(str, rolling_range))

    return output_head + output_middle + output_tail


def output(text):
    pass

if __name__ == '__main__':
    f = open('Website-content-paging-control_InputForSubmission_1.txt')
    output = ""
    for line in f:
        print solve_line(line)
