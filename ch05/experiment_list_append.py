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

import sys
from time import time

try:
    maxN = int(sys.argv[1])
except:
    maxN = 10000000

from time import time            # import time function from time module
def compute_average(n):
  """Perform n appends to an empty list and return average time elapsed."""
  data = []
  start = time()                 # record the start time (in seconds)
  for k in range(n):
    data.append(None)
  end = time()                   # record the end time (in seconds)
  return (end - start) / n       # compute average per operation

n = 10
while n <= maxN:
  print('Average of {0:.3f} for n {1}'.format(compute_average(n)*1000000, n))
  n *= 10
