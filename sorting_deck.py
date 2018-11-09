#!/usr/bin/env python3
import argparse
import sys
import random
import pyglet
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
    for i in range(len(lst)):
        for j in range(0, len(lst) - 1 - i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
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

# def quick_sort(lst):
#     if not lst:
#         return lst
#     pivot = lst[random.randint(0, len(lst) - 1)]
#     print(pivot)
#     head = quick_sort([elem for elem in lst if elem < pivot])
#     tail = quick_sort([elem for elem in lst if elem > pivot])
#     return head + [elem for elem in lst if elem == pivot] + tail


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print('P:', pivot)
    print(' '.join(str(x) for x in arr))
    return (i + 1)


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)


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


width = 1280
height = 720
window = pyglet.window.Window(width, height)
def make_object():
    
    shirt_image = pyglet.image.load("resources/shirt.jpeg")
    shirt = pyglet.sprite.Sprite(img=shirt_image)
    shirt.scale = 0.1
    shirts = pyglet.graphics.Batch()
    campnou = pyglet.image.load("resources/campnou.jpg")
    shirt_list = []
    for i in range(len(lst)):
        x, y = i * 10, 50
        print("ha")
        shirt_list.append(pyglet.sprite.Sprite(shirt_image, x, y, batch=shirts))
    for i in range(len(lst)):
        shirt_list[i].scale = 0.1
    print(shirt_list)
    return shirts, campnou, shirt

@window.event
def on_draw():
    shirts, campnou, shirt = make_object(lst)
    window.clear()
    # shirts.draw()
    campnou.blit(0, 0, width=window.width, height=window.height)

    shirts.draw()


def main():
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
    pyglet.app.run()
