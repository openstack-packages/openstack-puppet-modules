#!/bin/bash

# Script to download all referenced sources to the ~/rpmbuild/SOURCES folder
# Requires wget to be installed

for i in `grep Source openstack-puppet-modules.spec | awk '{print $2}'`
do
   key=`echo $i | sed -r 's/.*\{([a-z_]*)\}.tar.gz/\1/g'`
   commit=`grep "%global $key" openstack-puppet-modules.spec | awk '{print $3}'`
   url=`echo $i | sed -r "s/%\{[a-z_]*\}/$commit/g"`
   filename=`basename $url`
   pushd ~/rpmbuild/SOURCES
   if [ ! -f $filename ]
   then
      wget $url
   fi
   popd
done

