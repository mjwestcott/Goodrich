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

def toc_plain(T):
  for p in T.preorder():
    print(p.element())

def toc_indent_bad(T):
  for p in T.preorder():
    print(2*T.depth(p)*' ' + str(p.element()))  # beware of inefficiency

def preorder_indent(T, p, d):
  """Print preorder representation of subtree of T rooted at p at depth d."""
  print(2*d*' ' + str(p.element()))           # use depth for indentation
  for c in T.children(p):
    preorder_indent(T, c, d+1)                # child depth is d+1

def preorder_label(T, p, d, path):
  """Print labeled representation of subtree of T rooted at p at depth d."""
  label = '.'.join(str(j+1) for j in path)    # displayed labels are one-indexed
  print(2*d*' ' + label, p.element())
  path.append(0)                              # path entries are zero-indexed
  for c in T.children(p):
    preorder_label(T, c, d+1, path)           # child depth is d+1
    path[-1] += 1
  path.pop()

def parenthesize(T, p):
  """Print parenthesized representation of subtree of T rooted at p."""
  print(p.element(), end='')                  # use of end avoids trailing newline
  if not T.is_leaf(p):
    first_time = True
    for c in T.children(p):
      sep = ' (' if first_time else ', '      # determine proper separator
      print(sep, end='')        
      first_time = False                      # any future passes will not be the first
      parenthesize(T, c)                      # recur on child
    print(')', end='')                        # include closing parenthesis

def disk_space(T, p):
  """Return total disk space for subtree of T rooted at p."""
  subtotal = p.element().space()              # space used at position p
  for c in T.children(p):
    subtotal += disk_space(T, c)              # add child's space to subtotal
  return subtotal
