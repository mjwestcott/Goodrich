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

def quick_sort(S):
  """Sort the elements of queue S using the quick-sort algorithm."""
  n = len(S)
  if n < 2:
    return                            # list is already sorted
  # divide
  p = S.first()                       # using first as arbitrary pivot
  L = LinkedQueue()
  E = LinkedQueue()
  G = LinkedQueue()
  while not S.is_empty():             # divide S into L, E, and G
    if S.first() < p:
      L.enqueue(S.dequeue())
    elif p < S.first():
      G.enqueue(S.dequeue())
    else:                             # S.first() must equal pivot
      E.enqueue(S.dequeue())
  # conquer (with recursion)
  quick_sort(L)                       # sort elements less than p
  quick_sort(G)                       # sort elements greater than p
  # concatenate results
  while not L.is_empty():
    S.enqueue(L.dequeue())
  while not E.is_empty():
    S.enqueue(E.dequeue())
  while not G.is_empty():
    S.enqueue(G.dequeue())
