# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from ..ch07.linked_queue import LinkedQueue

def merge(S1, S2, S):
  """Merge two sorted queue instances S1 and S2 into empty queue S."""
  while not S1.is_empty() and not S2.is_empty():
    if S1.first() < S2.first():
      S.enqueue(S1.dequeue())
    else:
      S.enqueue(S2.dequeue())
  while not S1.is_empty():            # move remaining elements of S1 to S
    S.enqueue(S1.dequeue())
  while not S2.is_empty():            # move remaining elements of S2 to S
    S.enqueue(S2.dequeue())

def merge_sort(S):
  """Sort the elements of queue S using the merge-sort algorithm."""
  n = len(S)
  if n < 2:
    return                            # list is already sorted
  # divide
  S1 = LinkedQueue()                  # or any other queue implementation
  S2 = LinkedQueue()
  while len(S1) < n // 2:             # move the first n//2 elements to S1
    S1.enqueue(S.dequeue())
  while not S.is_empty():             # move the rest to S2
    S2.enqueue(S.dequeue())
  # conquer (with recursion)
  merge_sort(S1)                      # sort first half
  merge_sort(S2)                      # sort second half
  # merge results
  merge(S1, S2, S)                    # merge sorted halves back into S
