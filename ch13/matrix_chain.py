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

def matrix_chain(d):
  """Return solution to the matrix chain problem.

  d is a list of n+1 numbers describing the dimensions of a chain of
  n matrices such that kth matrix has dimensions d[k]-by-d[k+1].
 
  Return an n-by-n table such that N[i][j] represents the minimum number of
  multiplications needed to compute the product of Ai through Aj inclusive.
  """
  n = len(d) - 1                       # number of matrices
  N = [[0] * n for i in range(n)]      # initialize n-by-n result to zero
  for b in range(1, n):                # number of products in subchain
    for i in range(n-b):               # start of subchain
      j = i + b                        # end of subchain
      N[i][j] = min(N[i][k] + N[k+1][j] + d[i]*d[k+1]*d[j+1] for k in range(i,j))
  return N
