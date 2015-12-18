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

from .positional_list import PositionalList

class FavoritesList:
  """List of elements ordered from most frequently accessed to least."""

  #------------------------------ nested _Item class ------------------------------
  class _Item:
    __slots__ = '_value', '_count'             # streamline memory usage
    def __init__(self, e):
      self._value = e                          # the user's element
      self._count = 0                          # access count initially zero

  #------------------------------- nonpublic utilities -------------------------------
  def _find_position(self, e):
    """Search for element e and return its Position (or None if not found)."""
    walk = self._data.first()
    while walk is not None and walk.element()._value != e:
      walk = self._data.after(walk)
    return walk

  def _move_up(self, p):
    """Move item at Position p earlier in the list based on access count."""
    if p != self._data.first():                      # consider moving...
      cnt = p.element()._count
      walk = self._data.before(p)
      if cnt > walk.element()._count:                # must shift forward
        while (walk != self._data.first() and
               cnt > self._data.before(walk).element()._count):
          walk = self._data.before(walk)
        self._data.add_before(walk, self._data.delete(p))   # delete/reinsert
  
  #------------------------------- public methods -------------------------------
  def __init__(self):
    """Create an empty list of favorites."""
    self._data = PositionalList()                 # will be list of _Item instances

  def __len__(self):
    """Return number of entries on favorites list."""
    return len(self._data)

  def is_empty(self):
    """Return True if list is empty."""
    return len(self._data) == 0

  def access(self, e):
    """Access element e, thereby increasing its access count."""
    p = self._find_position(e)                    # try to locate existing element
    if p is None:
      p = self._data.add_last(self._Item(e))      # if new, place at end
    p.element()._count += 1                       # always increment count
    self._move_up(p)                              # consider moving forward

  def remove(self, e):
    """Remove element e from the list of favorites."""
    p = self._find_position(e)                    # try to locate existing element
    if p is not None:
      self._data.delete(p)                        # delete, if found 

  def top(self, k):
    """Generate sequence of top k elements in terms of access count."""
    if not 1 <= k <= len(self):
      raise ValueError('Illegal value for k')
    walk = self._data.first()
    for j in range(k):
      item = walk.element()                       # element of list is _Item
      yield item._value                           # report user's element
      walk = self._data.after(walk)

  def __repr__(self):
    """Create string representation of the favorites list."""
    return ', '.join('({0}:{1})'.format(i._value, i._count) for i in self._data)

if __name__ == '__main__':
  fav = FavoritesList()
  for c in 'hello. this is a test of mtf':        # well, not the mtf part...
    fav.access(c)
    k = min(5, len(fav))
    print('Top {0}) {1:25} {2}'.format(k, [x for x in fav.top(k)], fav))
