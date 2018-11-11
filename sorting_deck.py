#!/usr/bin/env python3
import argparse
import sys
import pyglet
from pyglet.window import key
from pyglet.gl import *


def do_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--algo', help='specify which algorithm to use for\
                       sorting among [bubble|insert|quick|merge],\
                        default bubble', type=str, default='bubble')
    parser.add_argument('--gui', help='visualise the algorithm in GUI mode',
                        action='store_true')
    parser.add_argument('N', help='an integer for the list to sort', type=int,
                        nargs='+')
    global args
    global lst
    args = parser.parse_args()
    lst = args.N
    return lst, args


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
    result.append(list(lst))
    for i in range(len(lst)):
        for j in range(0, len(lst) - 1 - i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                result.append(list(lst))
                print(' '.join(str(x) for x in lst))


def insertion_sort(lst):
    for i in range(1, len(lst)):
        cur = lst[i]
        nam = False
        while i > 0 and cur < lst[i - 1]:
                lst[i] = lst[i - 1]
                i -= 1
                nam = True
        lst[i] = cur
        if nam is True:
            print(' '.join(str(x) for x in lst))


def partition(lst, low, high):
    i = (low - 1)
    pivot = lst[high]
    for j in range(low, high):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    print('P:', pivot)
    print(' '.join(str(x) for x in lst))
    return (i + 1)


def quick_sort(lst, low, high):
    if low < high:
        pivot = partition(lst, low, high)
        quick_sort(lst, low, pivot-1)
        quick_sort(lst, pivot+1, high)


def merge_sort(lst):
    if len(lst) > 1:
        m = int(len(lst)/2)
        left = lst[:m]
        right = lst[m:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
        print(' '.join(str(x) for x in lst))


lst, args = do_argparse()
width = 1800
height = 800
window = pyglet.window.Window(width, height)
shirt_image = pyglet.image.load("resources/shirt3.png")
shirt_list = []
for i in range(len(lst)):
    shirt = pyglet.sprite.Sprite(img=shirt_image)
    shirt.x = i * window.width / len(lst)
    shirt.y = window.height // 8
    shirt.scale = 2 / len(lst)
    shirt_list.append(shirt)
campnou = pyglet.image.load("resources/campnou.jpg")
i = 0
labels = []


def update(dt):
    global i
    if i < len(result):
        for j in range(len(result[i])):
            label = pyglet.text.Label(str(result[i][j]),
                                      font_size=500 / len(lst),
                                      x=shirt_list[j].x + 480 * (2 / len(lst)),
                                      y=shirt_list[j].y + 480 * (2 / len(lst)),
                                      anchor_x='center', anchor_y='center')
            # change color if there is swap:
            if i > 0 and result[i][j] != result[i-1][j]:
                label.color = (29, 225, 50, 255)
            # change the final color when finish sorting:
            if i == len(result) - 1:
                label.color = (170, 255, 255, 255)
            labels.append(label)
        i += 1


@window.event
def on_draw():
    global labels
    if len(labels) > 0:
        campnou.blit(0, 0, width=window.width, height=window.height)
        for i in shirt_list:
            i.draw()
        for label in labels:
            label.draw()
    labels = []


def main():
    global result
    result = []
    lst, args = do_argparse()
    if args.gui and len(lst) > 15:
        too_large()
        exit()
    if check(lst) == 'Sorted':
        if args.algo == 'merge':
            merge_sort(lst)
        if args.algo == 'quick':
            quick_sort(lst, 0, len(lst) - 1)
        else:
            exit()
    else:
        if args.algo == 'bubble':
            bubble_sort(lst)
        if args.algo == 'insert':
            insertion_sort(lst)
        if args.algo == 'quick':
            quick_sort(lst, 0, len(lst) - 1)
        if args.algo == 'merge':
            merge_sort(lst)


if __name__ == '__main__':
    main()
    if args.gui:
        pyglet.clock.schedule_interval(update, 0.75)
        pyglet.app.run()
