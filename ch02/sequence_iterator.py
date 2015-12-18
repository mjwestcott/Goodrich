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

class SequenceIterator:
  """An iterator for any of Python's sequence types."""

  def __init__(self, sequence):
    """Create an iterator for the given sequence."""
    self._seq = sequence          # keep a reference to the underlying data
    self._k = -1                  # will increment to 0 on first call to next

  def __next__(self):
    """Return the next element, or else raise StopIteration error."""
    self._k += 1                  # advance to next index
    if self._k < len(self._seq):
      return(self._seq[self._k])  # return the data element
    else:
      raise StopIteration()       # there are no more elements

  def __iter__(self):
    """By convention, an iterator must return itself as an iterator."""
    return self
