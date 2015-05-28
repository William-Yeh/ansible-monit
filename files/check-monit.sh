#!/bin/bash
# simple script to query the existance of specific monit version, if installed.
#
# @return: JSON string : { "found": true/false, "not_found": true/false }
#

VERSION_TEXT=$1


do_error_exit() {
  #echo "=== ERROR"
  echo '{ "found": false , "not_found": true  }'
  exit $RETVAL
}

trap 'RETVAL=$?;  do_error_exit '  ERR




line=$(monit -V 2> /dev/null)
#echo $line

match_count=$(echo $line | egrep $VERSION_TEXT | wc -l)

if [[ $match_count =~ 0 ]]; then
  echo '{ "found": false , "not_found": true  }'

else
  echo '{ "found": true  , "not_found": false }'

fi