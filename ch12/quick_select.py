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

import random

def quick_select(S, k):
  """Return the kth smallest element of list S, for k from 1 to len(S)."""
  if len(S) == 1:
    return S[0]
  pivot = random.choice(S)             # pick random pivot element from S
  L = [x for x in S if x < pivot]      # elements less than pivot
  E = [x for x in S if x == pivot]     # elements equal to pivot
  G = [x for x in S if pivot < x]      # elements greater than pivot
  if k <= len(L):
    return quick_select(L, k)          # kth smallest lies in L
  elif k <= len(L) + len(E):
    return pivot                       # kth smallest equal to pivot
  else:
    j = k - len(L) - len(E)            # new selection parameter
    return quick_select(G, j)          # kth smallest is jth in G
