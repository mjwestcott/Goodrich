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

from .sorted_table_map import SortedTableMap

class CostPerformanceDatabase:
  """Maintain a database of maximal (cost,performance) pairs."""

  def __init__(self):
    """Create an empty database."""
    self._M = SortedTableMap()             # or a more efficient sorted map

  def best(self, c):
    """Return (cost,performance) pair with largest cost not exceeding c.

    Return None if there is no such pair.
    """
    return self._M.find_le(c)

  def add(self, c, p):
    """Add new entry with cost c and performance p."""
    # determine if (c,p) is dominated by an existing pair
    other = self._M.find_le(c)              # other is at least as cheap as c
    if other is not None and other[1] >= p: # if its performance is as good,
        return                              # (c,p) is dominated, so ignore
    self._M[c] = p                          # else, add (c,p) to database
    # and now remove any pairs that are dominated by (c,p)
    other = self._M.find_gt(c)              # other more expensive than c
    while other is not None and other[1] <= p:
      del self._M[other[0]]
      other = self._M.find_gt(c)
