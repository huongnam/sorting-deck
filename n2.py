#!/usr/bin/env python3
import argparse
import sys
import random
import pyglet
from pyglet.window import key
from pyglet.gl import *
import time


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
    global result
    result = []
    result.append(' '.join(str(x) for x in lst))
    for i in range(len(lst)):
        for j in range(0, len(lst) - 1 - i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                result.append(' '.join(str(x) for x in lst))
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

lst, args = do_argparse()
width = 1280
height = 720
window = pyglet.window.Window(width, height)
shirt_image = pyglet.image.load("resources/shirt3.png")
shirt_list = []
for i in range(len(lst)):
    shirt = pyglet.sprite.Sprite(img=shirt_image)
    shirt.x = i * 180
    shirt.y = window.height // 4
    shirt.scale = 1 / 7
    shirt_list.append(shirt)
# batch = pyglet.graphics.Batch()
# group0 = pyglet.graphics.OrderedGroup(0)
# group1 = pyglet.graphics.OrderedGroup(1)
shirts = pyglet.graphics.Batch()
texts = pyglet.graphics.Batch()
campnou = pyglet.image.load("resources/campnou.jpg")
# shirt_list2 = []
# zoom = (1 / len(lst))
# print(zoom)
# for i in range(len(lst)):
#     x, y = i * 180, window.height // 4
#     shirt_list2.append(pyglet.sprite.Sprite(shirt_image, x, y, batch=shirts))
# for i in range(len(lst)):
#     shirt_list2[i].scale = zoom
print(width // len(lst))
print("ha")
text_list = []
for i in range(len(lst)):
    text = pyglet.text.Label(text="%s" % lst[i], x=i * 180 + 65,
                                 y=window.height // 2.8, color = (255,255,255,255),
                                 font_size = 35, anchor_x='center', anchor_y='center')

    text_list.append(text)
#
# for i in range(len(lst)):
#     text_list.append(pyglet.text.Label(text="%s" % lst[i], x=i * 180 + 65,
#                                  y=window.height // 2.8, color = (255,255,255,255),
#                                  font_size = 35, anchor_x='center', anchor_y='center', batch=texts))
print(text_list)
# old_lst = lst
def press_key(symbol):
   if symbol == key.SPACE:
       print('Nam 7')




def update(dt):
    global text_list
    if args.algo == 'bubble':
        bubble_sort(lst)
    print("nam")
    # print(old_lst)
    print("nam")
    if result != []:
        print(result)
        count = 0
        for j in range(len(result) - 1):
            print('Step {}'.format(count))
            print('========================')
            count += 1
            result[j] = result[j].split()
            old_line = result[j]
            new_line = result[j+1].split()
            print('Old line:')
            print(old_line)
            print("New line: ")
            print(new_line)

            for i in range(len(old_line)):
                if old_line[i] != new_line[i]:
                    print(old_line[i])

                    print(new_line[i])
                    item1 = old_line[i]
                    item2 = new_line[i]
                    print('Item 1')
                    print(item1)
                    print("Item 2")
                    print(item2)
                    ind = old_line.index(item2)
                    print(ind)

                    # while text_list[old_line.index(item1)].y < window.height // 2:
                    #     text_list[old_line.index(item1)].y += 10
                    #     text_list[old_line.index(item2)].y += 10
                    #
                    # x1 = text_list[old_line.index(item1)].x
                    # x2 = text_list[old_line.index(item2)].x
                    #
                    # while text_list[old_line.index(item1)].x < x2:
                    #     text_list[old_line.index(item1)].x += 10

                    # x1 = text_list[old_line.index(item1)].x
                    # x2 = text_list[old_line.index(item2)].x
                    # text_list[old_line.index(item1)].x = x2
                    # text_list[old_line.index(item2)].x = x1
                    # text_list[old_line.index(item1)].y = window.height // 2.8
                    # text_list[old_line.index(item2)].y = window.height // 2.8

                    text_list[old_line.index(item1)].y = window.height // 2
                    text_list[old_line.index(item2)].y = window.height // 2
                    x1 = text_list[old_line.index(item1)].x
                    x2 = text_list[old_line.index(item2)].x
                    text_list[old_line.index(item1)].x = x2
                    text_list[old_line.index(item2)].x = x1
                    text_list[old_line.index(item1)].y = window.height // 2.8
                    text_list[old_line.index(item2)].y = window.height // 2.8

                    # # text_list[old_line.index(item1)].y = window.height // 2.8
                    # text_list[old_line.index(item2)].y = window.height // 2.8
                    # print("nam8")
                    # print(text_list)
                    # print("nam8")
                    # text_list = str(text_list)
                    # text_list.rsplit(sep=',')
                    # text_list
                    # print(text_list)
                    flag = True
                    break
            if flag:
                break

@window.event
def on_draw():
    window.clear()

    campnou.blit(0, 0, width=window.width, height=window.height)
    shirts.draw()
    texts.draw()
    # batch.draw()
    shirt.draw()
    for i in shirt_list:
        i.draw()
    for i in text_list:
        i.draw()
    # time.sleep(1)
@window.event
def on_key_press(symbol, modifiers):
    press_key(symbol)

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
        # if args.algo == 'bubble':
        #     bubble_sort(lst)
        if args.algo == 'insert':
            insertion_sort(lst)
        if args.algo == 'quick':
            quick_sort(lst, 0, len(lst) - 1)
        if args.algo == 'merge':
            merge_sort(lst)


if __name__ == '__main__':
    main()
    pyglet.clock.schedule_interval(update, 1)
    pyglet.app.run()
