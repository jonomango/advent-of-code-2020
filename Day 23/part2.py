import math
import copy
from functools import reduce
from collections import deque


class Node:
  value = None
  flink = None
  blink = None

  def __init__(self, v, f=None, b=None):
    self.value = v
    self.flink = f
    self.blink = b

# had to make a doubly linked list fuck you aoc
class DLinkedList:
  head = None
  back = None
  fastmap = None

  def __init__(self, values):
    # allocated Nodes
    self.fastmap = [None for _ in range(len(values) + 1)]

    self.head = Node(values[0])
    self.fastmap[values[0]] = self.head
    curr = self.head

    for v in values[1:]:
      n = Node(v, None, curr)
      self.fastmap[v] = n

      curr.flink = n
      curr = n

    self.back = curr

  # print every value
  def p(self):
    curr = self.head

    while curr:
      print(curr.value, end=' ')
      curr = curr.flink

    print()

  def popleft(self, count=1):
    if count == 1:
      v = self.head.value
      self.head = self.head.flink
      return v

    v = []

    while count > 0:
      v.append(self.head.value)
      self.head = self.head.flink
      count -= 1

    return v

  def insert_back(self, values):
    curr = self.back

    for v in values:
      #n = Node(v, None, curr)
      n = self.fastmap[v]
      n.flink = None
      n.blink = curr

      curr.flink = n
      curr = n

    self.back = curr

  def find_and_append(self, search, values):
    curr = self.fastmap[search]

    # insert each value
    for v in values:
      #n = Node(v, curr.flink, curr)
      n = self.fastmap[v]
      n.flink = curr.flink
      n.blink = curr

      # insert into list
      if curr.flink != None:
        curr.flink.blink = n

      curr.flink = n
      curr = n

    if curr.flink == None:
      self.back = curr

  def get(self, search, count=1):
    curr = self.head

    while curr != None:
      # insert here
      if curr.value == search:
        values = []

        while count > 0:
          curr = curr.flink
          values.append(curr.value)

          count -= 1

        return values

      curr = curr.flink

    return -1


def normalize(dest):
  if dest < 1:
    dest = 1000000
  return dest

with open("input.txt", "r") as file:
  cups = DLinkedList(list(map(int, file.read().strip())) + list(range(10, 1000000 + 1)))
  count = 10000000

  for i in range(count):
    selected = cups.popleft(1)
    cups.insert_back([selected])
    picked = cups.popleft(3)

    dest = normalize(selected - 1)
    while dest in picked:
      dest = normalize(dest - 1)
    
    cups.find_and_append(dest, picked)
    
    if i % 100000 == 0:
      print(i // 100000, "%", sep="")

  first, second = cups.get(1, 2)
  print("solution:", first * second)