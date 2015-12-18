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

from .binary_search_tree import TreeMap

class SplayTreeMap(TreeMap):
  """Sorted map implementation using a splay tree."""

  #--------------------------------- splay operation --------------------------------
  def _splay(self, p):
    while p != self.root():
      parent = self.parent(p)
      grand = self.parent(parent)
      if grand is None:
        # zig case
        self._rotate(p)
      elif (parent == self.left(grand)) == (p == self.left(parent)):
        # zig-zig case
        self._rotate(parent)             # move PARENT up
        self._rotate(p)                  # then move p up
      else:
        # zig-zag case
        self._rotate(p)                  # move p up
        self._rotate(p)                  # move p up again

  #---------------------------- override balancing hooks ----------------------------
  def _rebalance_insert(self, p):
    self._splay(p)

  def _rebalance_delete(self, p):
    if p is not None:
      self._splay(p)                     

  def _rebalance_access(self, p):
    self._splay(p)
