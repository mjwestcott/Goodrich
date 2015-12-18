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

# WARNING: this is a terribly inefficient algorithm
def unique3(S, start, stop):
  """Return True if there are no duplicate elements in slice S[start:stop]."""
  if stop - start <= 1: return True                # at most one item
  elif not unique(S, start, stop-1): return False  # first part has duplicate
  elif not unique(S, start+1, stop): return False  # second part has duplicate
  else: return S[start] != S[stop-1]               # do first and last differ?
