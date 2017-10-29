#!/bin/bash
#
# Usage:
#       g query that you would like to search
#

q=""
i=0

for var in "$@"
do
   if [ "$i" -eq "0" ]
   then
      q+=$var
   else
      q+="+"$var
   fi
   i+=1
done

open -a safari http://www.google.com/search?q=$q
