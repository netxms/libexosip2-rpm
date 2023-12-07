#!/bin/bash

set -e

for V in 8 9; do
   mock -r rocky+epel-$V-$(arch) --spec SPECS/*.spec --sources SOURCES \
      --addrepo https://packages.netxms.org/epel/$V/$(arch)/stable \
      --addrepo https://packages.netxms.org/devel/epel/$V/$(arch)/stable
done

for V in 37 38 39; do
   mock -r fedora-$V-$(arch) --spec SPECS/*.spec --sources SOURCES \
      --addrepo https://packages.netxms.org/fedora/$V/$(arch)/stable \
      --addrepo https://packages.netxms.org/devel/fedora/$V/$(arch)/stable
done

cp /var/lib/mock/*/result/*.rpm /result/
