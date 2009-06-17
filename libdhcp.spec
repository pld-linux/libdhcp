Summary:	A library for network interface configuration with DHCP
Summary(pl.UTF-8):	Biblioteka do konfiguracji interfejsów sieciowych przy użyciu DHCP
Name:		libdhcp
Version:	1.99.8
Release:	2
License:	GPL v2+
Group:		Libraries
Source0:	http://dcantrel.fedorapeople.org/libdhcp/%{name}-%{version}.tar.bz2
# Source0-md5:	f9ba27f85a10d9c57727b909c099ed0e
#Patch0:		%{name}-libnl.patch
URL:		http://dcantrel.fedorapeople.org/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	dhcp-devel
BuildRequires:	libdhcp4client-devel >= 4:4.0.0-4
BuildRequires:	libdhcp6client-devel >= 1.0.4
BuildRequires:	libnl-devel >= 1.0-0.pre5.1
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdhcp enables programs to invoke and control the Dynamic Host
Configuration Protocol (DHCP) clients: the Internet Software
Consortium (ISC) IPv4 DHCP client library, libdhcp4client, and the
IPv6 DHCPv6 client library, libdhcp6client, and provides Network
Interface Configuration (NIC) services for network parameter
autoconfiguration with DHCP.

%description -l pl.UTF-8
libdhcp pozwala programom wywoływać i sterować klientami DHCP (Dynamic
Host Configuration Protocol): biblioteką kliencką ISC (Internet
Software Consortium) IPv4 DHCP - libdhcp4client oraz biblioteką
kliencką IPv6 DHCPv6 - libdhcp6client; udostępnia usługi NIC (Network
Interface Configuration) do automatycznej konfiguracji parametrów
sieci przy użyciu DHCP.

%package devel
Summary:	C header files for development with libdhcp
Summary(pl.UTF-8):	Pliki nagłówkowe C do programowania z użyciem libdhcp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libdhcp4client-devel >= 4:3.0.4-18
Requires:	libdhcp6client-devel >= 0.10-38
Requires:	libnl-devel >= 1.0-0.pre5.1

%description devel
C header files for development with libdhcp.

%description devel -l pl.UTF-8
Pliki nagłówkowe C do programowania z użyciem libdhcp.

%package static
Summary:	Static libdhcp library
Summary(pl.UTF-8):	Statyczna biblioteka libdhcp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libdhcp library.

%description static -l pl.UTF-8
Statyczna biblioteka libdhcp.

%prep
%setup -q
#%%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README COPYING ChangeLog TODO
%attr(755,root,root) %{_libdir}/libdhcp-*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdhcp-*.so.?

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdhcp.so
%{_libdir}/libdhcp.la
%{_includedir}/libdhcp
%{_pkgconfigdir}/libdhcp.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libdhcp.a
