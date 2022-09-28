# libexosip2 - rpm specs

## Build

```sh
ARCH=$(arch)
REL=8
CONF=rocky+epel-$REL-$ARCH

mock -r $CONF --spec SPECS/libexosip2.spec --sources SOURCES/libexosip2-5.3.0.tar.gz
rsync -avz /var/lib/mock/$CONF/result/*.rpm user@target:/location/epel/$REL/$ARCH/stable/Packages/
```
