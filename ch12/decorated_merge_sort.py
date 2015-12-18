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

from .merge_array import merge_sort

class _Item:
  """Lightweight composite to store decorated value for sorting."""
  __slots__ = '_key', '_value'

  def __init__(self, k, v):
    self._key = k
    self._value = v

  def __lt__(self, other):
    return self._key < other._key    # compare items based on their keys

def decorated_merge_sort(data, key=None):
  """Demonstration of the decorate-sort-undecorate pattern."""
  if key is not None:
    for j in range(len(data)):
      data[j] = _Item(key(data[j]), data[j])          # decorate each element
  merge_sort(data)                                    # sort with existing algorithm
  if key is not None:
    for j in range(len(data)):
      data[j] = data[j]._value                        # undecorate each element
