#!/usr/bin/python -tt

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
##
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys

email_list=[]
emails=open('emails', 'r').readlines()
for email in emails[0].split(';'):
    email_list.append(email)

group_list=[email_list[i:i + 10] for i in xrange(0, len(email_list), 10)]

for list1 in group_list:
    print '----'
    for item in list1:
        sys.stdout.write(item + ', ')
    sys.stdout.write('\n')
