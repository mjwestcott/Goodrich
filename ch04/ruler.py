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

def draw_line(tick_length, tick_label=''):
  """Draw one line with given tick length (followed by optional label)."""
  line = '-' * tick_length
  if tick_label:
    line += ' ' + tick_label
  print(line)

def draw_interval(center_length):
  """Draw tick interval based upon a central tick length."""
  if center_length > 0:                   # stop when length drops to 0
    draw_interval(center_length - 1)      # recursively draw top ticks
    draw_line(center_length)              # draw center tick
    draw_interval(center_length - 1)      # recursively draw bottom ticks

def draw_ruler(num_inches, major_length):
  """Draw English ruler with given number of inches and major tick length."""
  draw_line(major_length, '0')            # draw inch 0 line
  for j in range(1, 1 + num_inches):
    draw_interval(major_length - 1)       # draw interior ticks for inch
    draw_line(major_length, str(j))       # draw inch j line and label


if __name__ == '__main__':
  draw_ruler(2,4)
  print('='*30)
  draw_ruler(1,5)
  print('='*30)
  draw_ruler(3,3)
