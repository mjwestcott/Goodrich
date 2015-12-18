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

def LCS(X, Y):
  """Return table such that L[j][k] is length of LCS for X[0:j] and Y[0:k]."""
  n, m = len(X), len(Y)                      # introduce convenient notations
  L = [[0] * (m+1) for k in range(n+1)]      # (n+1) x (m+1) table
  for j in range(n):
    for k in range(m):
      if X[j] == Y[k]:                       # align this match
        L[j+1][k+1] = L[j][k] + 1            
      else:                                  # choose to ignore one character
        L[j+1][k+1] = max(L[j][k+1], L[j+1][k])
  return L

def LCS_solution(X, Y, L):
  """Return the longest common substring of X and Y, given LCS table L."""
  solution = []
  j,k = len(X), len(Y)
  while L[j][k] > 0:                   # common characters remain
    if X[j-1] == Y[k-1]:
      solution.append(X[j-1])
      j -= 1
      k -= 1
    elif L[j-1][k] >= L[j][k-1]:
      j -=1
    else:
      k -= 1
  return ''.join(reversed(solution))   # return left-to-right version
