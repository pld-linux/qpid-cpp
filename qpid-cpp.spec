# $Revision: 1.8 $, $Date: 2011/07/23 06:34:38 $
# TODO:
# - qpidd user/group
# - qpidd init script
# - look at Fedora spec at: http://rrakus.fedorapeople.org/qpid-cpp.spec
#
# Conditional build:
%bcond_without	cman		# cman quorum service
%bcond_without	corosync	# CPG clustering
%bcond_without	rdma		# Remote DMA protocol
%bcond_without	static_libs	# static libraries
#
%include	/usr/lib/rpm/macros.perl
Summary:	C++ implementation of the AMQP protocol
Summary(pl.UTF-8):	Implementacja protokołu AMQP w C++
Name:		qpid-cpp
Version:	0.16
Release:	0.1
License:	Apache v2.0
Group:		Libraries
Source0:	http://www.us.apache.org/dist/qpid/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	0be857cfc7615763e9296955d33972d5
Patch0:		%{name}-boost.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-perl.patch
# https://reviews.apache.org/r/5593/
Patch3:		%{name}-qmf-broker.patch
URL:		http://qpid.apache.org/
BuildRequires:	acl-devel
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	boost-devel >= 1.33.1
%{?with_cman:BuildRequires:	cman-devel}
%{?with_corosync:BuildRequires:	corosync-devel}
BuildRequires:	cyrus-sasl-devel >= 2.0
BuildRequires:	doxygen
BuildRequires:	help2man
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	nspr-devel
BuildRequires:	nss-devel
BuildRequires:	perl-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	ruby-devel >= 1.8
BuildRequires:	swig-python >= 1.3.26
BuildRequires:	swig-ruby >= 1.3.26
BuildRequires:	xerces-c-devel
BuildRequires:	xqilla-devel
%if %{with rdma}
BuildRequires:	libibverbs-devel
BuildRequires:	librdmacm-devel
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qpid/C++ is a C++ implementation of the AMQP protcol described at
<http://amqp.org/>.

%description -l pl.UTF-8
Qpid/C++ to implementacja w C++ protokołu AMQP opisanego pod
<http://amqp.org/>.

%package client
Summary:	AMQP client modules and configuration
Summary(pl.UTF-8):	Klient AMQP - moduły i konfiguracja
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description client
Qpid/C++ is a C++ implementation of the AMQP protcol described at
<http://amqp.org/>. This package contains client modules and
configuration.

%description client -l pl.UTF-8
Qpid/C++ to implementacja w C++ protokołu AMQP opisanego pod
<http://amqp.org/>. Ten pakiet zawiera moduły oraz konfigurację
klienta.

%package server
Summary:	AMQP server
Summary(pl.UTF-8):	Serwer AMQP
Group:		Daemons
Requires:	%{name}-libs = %{version}-%{release}

%description server
Qpid/C++ is a C++ implementation of the AMQP protcol described at
<http://amqp.org/>. This package contains the server.

%description server -l pl.UTF-8
Qpid/C++ to implementacja w C++ protokołu AMQP opisanego pod
<http://amqp.org/>. Ten pakiet zawiera serwer.

%package libs
Summary:	AMQP runtime libraries
Summary(pl.UTF-8):	Biblioteki uruchomieniowe AMQP
Group:		Libraries

%description libs
Qpid/C++ is a C++ implementation of the AMQP protcol described at
<http://amqp.org/>. This package contains the runtime libraries.

%description libs -l pl.UTF-8
Qpid/C++ to implementacja w C++ protokołu AMQP opisanego pod
<http://amqp.org/>. Ten pakiet zawiera biblioteki uruchomieniowe.

%package devel
Summary:	Header files for Qpid/C++ libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek Qpid/C++
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for Qpid/C++ libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek Qpid/C++.

%package static
Summary:	Static Qpid/C++ libraries
Summary(pl.UTF-8):	Statyczne biblioteki Qpid/C++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Qpid/C++ libraries.

%description static -l pl.UTF-8
Statyczne biblioteki Qpid/C++.

%package qmfgen
Summary:	QMF code generator
Summary(pl.UTF-8):	Generator kodu QMF
Group:		Development/Tools
Requires:	python-modules

%description qmfgen
QMF code generator.

%description qmfgen -l pl.UTF-8
Generator kodu QMF.

%package -n perl-%{name}
Summary:	Perl bindings for Qpid/C++ libraries
Summary(pl.UTF-8):	Wiązania Perla do bibliotek Qpid/C++
Group:		Development/Languges/Perl
Requires:	%{name}-libs = %{version}-%{release}

%description -n perl-%{name}
Perl bindings for Qpid/C++ libraries.

%description -n perl-%{name} -l pl.UTF-8
Wiązania Perla do bibliotek Qpid/C++.

%package -n python-%{name}
Summary:	Python bindings for Qpid/C++ libraries
Summary(pl.UTF-8):	Wiązania Pythona do bibliotek Qpid/C++
Group:		Libraries/Python
Requires:	%{name}-libs = %{version}-%{release}
Requires:	python-modules

%description -n python-%{name}
Python bindings for Qpid/C++ libraries.

%description -n python-%{name} -l pl.UTF-8
Wiązania Pythona do bibliotek Qpid/C++.

%package -n ruby-%{name}
Summary:	Ruby bindings for Qpid/C++ libraries
Summary(pl.UTF-8):	Wiązania języka Ruby do bibliotek Qpid/C++
Group:		Development/Languages
Requires:	%{name}-libs = %{version}-%{release}
Requires:	python-modules

%description -n ruby-%{name}
Ruby bindings for Qpid/C++ libraries.

%description -n ruby-%{name} -l pl.UTF-8
Wiązania języka Ruby do bibliotek Qpid/C++.

%prep
%setup -q -n qpidc-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p2

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_static_libs:--enable-static} \
	--with-cpg%{!?with_corosync:=no} \
	--with-cman%{!?with_cman:=no} \
	--with-rdma%{!?with_rdma:=no} \
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/*.la \
	$RPM_BUILD_ROOT%{ruby_sitearchdir}/*.la \
	$RPM_BUILD_ROOT%{_libdir}/qpid/{client,daemon}/*.la
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/qpid/{client,daemon}/*.a
%endif
%{__rm} -r $RPM_BUILD_ROOT%{_libdir}/qpid/tests

install -d $RPM_BUILD_ROOT%{_examplesdir}
mv $RPM_BUILD_ROOT%{_datadir}/qpidc/examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files client
%defattr(644,root,root,755)
%dir %{_sysconfdir}/qpid
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/qpid/qpidc.conf
%dir %{_libdir}/qpid/client
%attr(755,root,root) %{_libdir}/qpid/client/rdmaconnector.so
%attr(755,root,root) %{_libdir}/qpid/client/sslconnector.so

%files server
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/qpidd.conf
%config(noreplace) %verify(not md5 mtime size) /etc/sasl2/qpidd.conf
%attr(755,root,root) %{_sbindir}/qpidd
%attr(755,root,root) %{_libdir}/qpid/qpidd_watchdog
%dir %{_libdir}/qpid/daemon
%attr(755,root,root) %{_libdir}/qpid/daemon/acl.so
%attr(755,root,root) %{_libdir}/qpid/daemon/cluster.so
%attr(755,root,root) %{_libdir}/qpid/daemon/ha.so
%attr(755,root,root) %{_libdir}/qpid/daemon/rdma.so
%attr(755,root,root) %{_libdir}/qpid/daemon/replicating_listener.so
%attr(755,root,root) %{_libdir}/qpid/daemon/replication_exchange.so
%attr(755,root,root) %{_libdir}/qpid/daemon/ssl.so
%attr(755,root,root) %{_libdir}/qpid/daemon/watchdog.so
%attr(755,root,root) %{_libdir}/qpid/daemon/xml.so
%{_mandir}/man1/qpidd.1*
%attr(755,qpidd,qpidd) %dir /var/lib/qpidd

%files libs
%defattr(644,root,root,755)
%doc NOTICE README.txt RELEASE_NOTES SSL
%attr(755,root,root) %{_libdir}/libqmf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqmf.so.1
%attr(755,root,root) %{_libdir}/libqmf2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqmf2.so.1
%attr(755,root,root) %{_libdir}/libqmfconsole.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqmfconsole.so.2
%attr(755,root,root) %{_libdir}/libqmfengine.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqmfengine.so.1
%attr(755,root,root) %{_libdir}/libqpidbroker.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqpidbroker.so.2
%attr(755,root,root) %{_libdir}/libqpidclient.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqpidclient.so.2
%attr(755,root,root) %{_libdir}/libqpidcommon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqpidcommon.so.2
%attr(755,root,root) %{_libdir}/libqpidmessaging.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqpidmessaging.so.2
%attr(755,root,root) %{_libdir}/libqpidtypes.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqpidtypes.so.1
%attr(755,root,root) %{_libdir}/librdmawrap.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librdmawrap.so.2
%attr(755,root,root) %{_libdir}/libsslcommon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsslcommon.so.2
%dir %{_libdir}/qpid

%files devel
%defattr(644,root,root,755)
%doc DESIGN
%attr(755,root,root) %{_libdir}/libqmf.so
%attr(755,root,root) %{_libdir}/libqmf2.so
%attr(755,root,root) %{_libdir}/libqmfconsole.so
%attr(755,root,root) %{_libdir}/libqmfengine.so
%attr(755,root,root) %{_libdir}/libqpidbroker.so
%attr(755,root,root) %{_libdir}/libqpidclient.so
%attr(755,root,root) %{_libdir}/libqpidcommon.so
%attr(755,root,root) %{_libdir}/libqpidmessaging.so
%attr(755,root,root) %{_libdir}/libqpidtypes.so
%attr(755,root,root) %{_libdir}/librdmawrap.so
%attr(755,root,root) %{_libdir}/libsslcommon.so
%{_libdir}/libqmf.la
%{_libdir}/libqmf2.la
%{_libdir}/libqmfconsole.la
%{_libdir}/libqmfengine.la
%{_libdir}/libqpidbroker.la
%{_libdir}/libqpidclient.la
%{_libdir}/libqpidcommon.la
%{_libdir}/libqpidmessaging.la
%{_libdir}/libqpidtypes.la
%{_libdir}/librdmawrap.la
%{_libdir}/libsslcommon.la
%{_includedir}/qmf
%{_includedir}/qpid
%{_pkgconfigdir}/qmf2.pc
%{_pkgconfigdir}/qpid.pc
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libqmf.a
%{_libdir}/libqmf2.a
%{_libdir}/libqmfconsole.a
%{_libdir}/libqmfengine.a
%{_libdir}/libqpidbroker.a
%{_libdir}/libqpidclient.a
%{_libdir}/libqpidcommon.a
%{_libdir}/libqpidmessaging.a
%{_libdir}/libqpidtypes.a
%{_libdir}/librdmawrap.a
%{_libdir}/libsslcommon.a

%files qmfgen
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qmf-gen
%dir %{py_sitescriptdir}/qmfgen
%{py_sitescriptdir}/qmfgen/*.py[co]
%{py_sitescriptdir}/qmfgen/management-types.xml
%{py_sitescriptdir}/qmfgen/templates

%files -n perl-%{name}
%defattr(644,root,root,755)
%{perl_vendorarch}/cqpid_perl.pm
%dir %{perl_vendorarch}/auto/cqpid_perl
%{perl_vendorarch}/auto/cqpid_perl/cqpid_perl.bs
%attr(755,root,root) %{perl_vendorarch}/auto/cqpid_perl/cqpid_perl.so

%files -n python-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_cqmf2.so
%attr(755,root,root) %{py_sitedir}/_cqpid.so
%attr(755,root,root) %{py_sitedir}/_qmfengine.so
%{py_sitescriptdir}/cqmf2.py[co]
%{py_sitescriptdir}/cqpid.py[co]
%{py_sitescriptdir}/qmf.py[co]
%{py_sitescriptdir}/qmf2.py[co]
%{py_sitescriptdir}/qmfengine.py[co]

%files -n ruby-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{ruby_sitearchdir}/cqmf2.so
%attr(755,root,root) %{ruby_sitearchdir}/cqpid.so
%attr(755,root,root) %{ruby_sitearchdir}/qmfengine.so
%{ruby_sitelibdir}/qmf.rb
%{ruby_sitelibdir}/qmf2.rb
