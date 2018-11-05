#!/usr/bin/env python3
import argparse
import sys


parser = argparse.ArgumentParser()
parser.add_argument('--algo', help='specify which algorithm to use for\
                   sorting among [bubble|insert|quick|merge], default bubble',
                   type=str, default='bubble')
parser.add_argument('--gui', help='visualise the algorithm in GUI mode',
                   action='store_true')
parser.add_argument('N', help='an integer for the list to sort', type=int,
                   nargs='+')
args = parser.parse_args()
lst = args.N
algo = args.algo

def too_large():
    print('Input too large')


def check(lst):
    boolist = []
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            boolist.append('Right')
        else:
            boolist.append('Wrong')
    if 'Wrong' not in boolist:
        return 'Sorted'


def bubble_sort(lst):
    if check(lst) == 'Sorted':
        exit()
    else:
        for i in range(len(lst)):
            for j in range(0, len(lst)-i-1):
                if lst[j] > lst[j+1] :
                    lst[j], lst[j+1] = lst[j+1], lst[j]
                    for item in lst:
                        sys.stdout.write(str(item) + ' ')
                    sys.stdout.write('\n')


def insertion_sort(lst):
    if check(lst) == 'Sorted':
        exit()
    else:
        for i in range(1, len(lst)):
            cur = lst[i]
            while i > 0 and cur < lst[i - 1]:
                    lst[i] = lst[i - 1]
                    i -= 1
            lst[i] = cur
            print(lst)


if args.gui and len(lst) > 15:
    too_large()
    exit()    
if args.algo == 'bubble':
    bubble_sort(lst)
if args.algo == 'insert':
    insertion_sort(lst)
