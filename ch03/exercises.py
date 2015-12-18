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

def example1(S):
  """Return the sum of the elements in sequence S."""
  n = len(S)
  total = 0
  for j in range(n):             # loop from 0 to n-1
    total += S[j]
  return total

def example2(S):
  """Return the sum of the elements with even index in sequence S."""
  n = len(S)
  total = 0
  for j in range(0, n, 2):       # note the increment of 2
    total += S[j]
  return total
  
def example3(S):
  """Return the sum of the prefix sums of sequence S."""
  n = len(S)
  total = 0
  for j in range(n):            # loop from 0 to n-1
    for k in range(1+j):        # loop from 0 to j
      total += S[k]
  return total

def example4(S):
  """Return the sum of the prefix sums of sequence S."""
  n = len(S)
  prefix = 0
  total = 0
  for j in range(n):
    prefix += S[j]
    total += prefix
  return total

def example5(A, B):           # assume that A and B have equal length
  """Return the number of elements in B equal to the sum of prefix sums in A."""
  n = len(A)                  
  count = 0
  for i in range(n):          # loop from 0 to n-1
    total = 0
    for j in range(n):        # loop from 0 to n-1
      for k in range(1+j):    # loop from 0 to j
        total += A[k]
    if B[i] == total:
      count += 1
  return count
