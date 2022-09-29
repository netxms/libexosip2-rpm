# libexosip2 - rpm specs

## Build

```sh
git clone https://github.com/netxms/libexosip2-rpm && cd libexosip2-rpm

ARCH=$(arch)
REL=8
CONF=rocky+epel-$REL-$ARCH

mock -r $CONF --spec SPECS/libexosip2.spec --sources SOURCES/libexosip2-5.3.0.tar.gz --addrepo https://packages.netxms.org/epel/$REL/$ARCH/stable
rsync -avz /var/lib/mock/$CONF/result/*.rpm $TARGET_USER@$TARGET_HOST:$TARGET_LOCATION/epel/$REL/$ARCH/stable/Packages/
```
