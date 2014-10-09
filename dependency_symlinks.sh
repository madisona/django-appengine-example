#!/bin/bash

# get directory name of script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
mkdir -p $DIR/src/lib

echo "loading dependencies"
pip install -r $DIR/requirements/base.txt
echo "dependencies loaded..."


PROJECTS=(
    'appengine_utils'
    'django'
    'memcache.py'
)

# loop through and symlink directories
count=0
while [ "x${PROJECTS[count]}" != "x" ]
do
    echo linking ${PROJECTS[count]}
    ln -sFh $VIRTUAL_ENV/lib/python2.7/site-packages/${PROJECTS[count]} $DIR/src/lib/${PROJECTS[count]}
    count=$(( $count + 1 ))
done

echo "Dependencies loaded and complete! Enjoy"
