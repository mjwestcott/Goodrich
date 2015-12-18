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

def is_matched(expr):
  """Return True if all delimiters are properly match; False otherwise."""
  lefty = '({['                               # opening delimiters
  righty = ')}]'                              # respective closing delims
  S = ArrayStack()
  for c in expr:
    if c in lefty:
      S.push(c)                               # push left delimiter on stack
    elif c in righty:
      if S.is_empty():
        return False                          # nothing to match with
      if righty.index(c) != lefty.index(S.pop()):
        return False                          # mismatched
  return S.is_empty()                         # were all symbols matched?
