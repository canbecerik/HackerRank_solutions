#!/bin/python3

import math
import os
import random
import re
import sys


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#


def sortedInsert(head, data):
    new_node = DoublyLinkedListNode(data)
    current_node = head
    # Search for the value as it is sorted
    while current_node.data < data:
        # Proceed if next node exists
        if current_node.next:
            current_node = current_node.next
        else:
            # No next node, add this as last node
            current_node.next = new_node
            new_node.prev = current_node
            return head
    # If not first node, insert in between the nodes
    if current_node.prev:
        current_node.prev.next = new_node
        new_node.prev = current_node.prev
    new_node.next = current_node
    current_node.prev = new_node
    # If inserted as first node, move head to back
    if head.prev:
        head = head.prev
    return head


if __name__ == '__main__':
    in_list = [1, 2, 3]
    dll = DoublyLinkedList()
    [dll.insert_node(i) for i in in_list]
    dll = sortedInsert(dll.head, 4)
    '''
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
'''
