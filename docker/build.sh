#!/bin/bash

set -e

mock -r rocky+epel-8-$(arch) --spec SPECS/*.spec --sources SOURCES --addrepo https://packages.netxms.org/epel/8/$(arch)/stable
mock -r rocky+epel-9-$(arch) --spec SPECS/*.spec --sources SOURCES --addrepo https://packages.netxms.org/epel/9/$(arch)/stable
cp /var/lib/mock/*/result/*.rpm /result/
