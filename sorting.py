#!/usr/bin/env python3
import pyglet
import argparse
import time


def swap_next(pos, lst):
    lst[pos], lst[pos + 1] = lst[pos + 1], lst[pos]


def bubble_sort(lst, display_list):
    for _ in lst:
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                swap_next(i, lst)
                print(' '.join(str(x) for x in lst))
                display_list.append(list(lst))


def insert_sort(lst, display_list):
    # Insertion Sort Type II
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            for j in range(i + 1):
                if lst[i + 1] <= lst[j]:
                    lst.insert(j, lst[i + 1])
                    del(lst[i + 2])
                    print(' '.join(str(x) for x in lst))
                    break


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


def quick_sort(arr, low, high, display_list):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)


def merge_sort(lst, display_list):
    if len(lst) > 1:
        m = int(len(lst)/2)
        L = lst[:m]
        R = lst[m:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lst[k] = L[i]
                i += 1
            else:
                lst[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            lst[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            lst[k] = R[j]
            j += 1
            k += 1
        print(' '.join(str(x) for x in lst))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('N', nargs='+', action='store', type=int,
                        help='an integer for the list to sort')
    parser.add_argument('--algo', metavar='ALGO', default='bubble',
                        help='specify which algorithm to use for sorting among\
                        [bubble|insert|quick|merge], default bubble')
    parser.add_argument('--gui', action='store_true',
                        help='visualise the algorithm in GUI mode')
    args = parser.parse_args()

    display_list.append(list(args.N))

    # Sorting
    if args.algo == 'bubble':
        bubble_sort(args.N, display_list)
    elif args.algo == 'insert':
        insert_sort(args.N, display_list)
    elif args.algo == 'quick':
        quick_sort(args.N, 0, len(args.N) - 1, display_list)
    elif args.algo == 'merge':
        merge_sort(args.N, display_list)


##############################################################################
if __name__ == '__main__':
    display_list = []
    main()
    print(display_list)
##############################################################################
# Making window
platform = pyglet.window.get_platform()
display = platform.get_default_display()
screen = display.get_default_screen()
gui_window = pyglet.window.Window(width=screen.width,
                                  height=480,
                                  resizable=True,
                                  caption='Sorting GUI')
# Reindex resource path
# pyglet.resource.path = ['../resources']
# pyglet.resource.reindex()

i = 0
labels = []

def update(dt):
    global i
    if i < len(display_list):
        # Making labels
        pos_x = (gui_window.width // len(display_list[i])) // 3
        for j in range(len(display_list[i])):
            label = pyglet.text.Label(str(display_list[i][j]),
                                      font_size=(gui_window.width // len(display_list[i])) // 3,
                                      anchor_x='center',
                                      x=pos_x, y=gui_window.height // 2.3)
            if i > 0 and display_list[i][j] != display_list[i-1][j]:
                label.color = (0, 255, 0, 255)
            labels.append(label)
            pos_x += gui_window.width // len(display_list[i])
        i += 1


@gui_window.event
def on_draw():
    global labels
    if len(labels) > 0:
        gui_window.clear()
        for label in labels:
            label.draw()
    labels = []


pyglet.clock.schedule_interval(update, 0.5)
pyglet.app.run()
