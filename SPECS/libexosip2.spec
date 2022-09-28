Name:		libexosip2
Version:	5.3.0
Release:	1%{?dist}_netxms
Summary:	eXosip is a library that hides the complexity of using the SIP protocol for mutlimedia session establishement.

License:	BSD
URL:		https://savannah.nongnu.org/projects/exosip
Source0: https://download.savannah.nongnu.org/releases/exosip/%{name}-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	openssl-devel
BuildRequires:	libosip2 = %{version}-%{release}

%description
eXosip is a library that hides the complexity of using the SIP protocol
for mutlimedia session establishement. This protocol is mainly to be used
by VoIP telephony applications (endpoints or conference server) but
might be also usefull for any application that wish to establish sessions
like multiplayer games. 
This distribution is built specifically for NetXMS packaging.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure --disable-rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -f %{buildroot}/%{_libdir}/*.la

%files
%exclude %{_bindir}/sip_*

%{_libdir}/libeXosip2.so.*
#%{_libdir}/libjemalloc.so.*
#%{_bindir}/jemalloc.sh
#%doc COPYING README VERSION

%files devel
%{_libdir}/libeXosip2.a
%{_libdir}/libeXosip2.so
%{_includedir}/eXosip2/*

%ldconfig_scriptlets

%changelog
