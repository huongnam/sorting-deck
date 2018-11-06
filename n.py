#!/usr/bin/env python3
import argparse
import sys
import random


def check(lst):
    boolist = []
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            boolist.append('Right')
        else:
            boolist.append('Wrong')
    if 'Wrong' not in boolist:
        return 'Sorted'


def too_large():
    print('Input too large')


def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(0, len(lst) - 1 - i):
            if lst[j] > lst[j+1] :
                lst[j], lst[j+1] = lst[j+1], lst[j]
                for item in lst:
                    sys.stdout.write(str(item) + ' ')
                sys.stdout.write('\n')


def insertion_sort(lst):
    for i in range(1, len(lst)):
        cur = lst[i]
        nam = False
        while i > 0 and cur < lst[i - 1]:
                lst[i] = lst[i - 1]
                i -= 1
                nam = True
        lst[i] = cur
        if nam == True:
            for item in lst:
                sys.stdout.write(str(item) + ' ')
            sys.stdout.write('\n')


def quick_sort(lst):
    if not lst:
        return lst
    pivot = lst[random.randint(0, len(lst) - 1)]
    print(pivot)
    head = quick_sort([elem for elem in lst if elem < pivot])
    tail = quick_sort([elem for elem in lst if elem > pivot])
    return head + [elem for elem in lst if elem == pivot] + tail


def main():

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

    if args.gui and len(lst) > 15:
        too_large()
        exit()
    if check(lst) == 'Sorted':
        print()
        exit()
    else:
        if args.algo == 'bubble':
            bubble_sort(lst)
        if args.algo == 'insert':
            insertion_sort(lst)
        if args.algo == 'quick':
            print(quick_sort(lst))
main()
