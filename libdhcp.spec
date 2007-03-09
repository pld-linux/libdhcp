Summary:	A library for network interface configuration with DHCP
Summary(pl.UTF-8):	Biblioteka do konfiguracji interfejsów sieciowych przy użyciu DHCP
Name:		libdhcp
Version:	1.20
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://people.redhat.com/dcantrel/libdhcp/%{name}-%{version}.tar.bz2
# Source0-md5:	02376447afa1130ff2427dfead1a2daf
Patch0:		%{name}-opt.patch
URL:		http://people.redhat.com/dcantrel/
BuildRequires:	dhcp-devel
BuildRequires:	libdhcp4client-devel >= 12:3.0.4-18
BuildRequires:	libdhcp6client-devel >= 0.10-38
BuildRequires:	libnl-devel >= 1.0-0.pre5.1
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
Requires:	libdhcp4client-devel >= 12:3.0.4-18
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
%patch0 -p1

%build
rm -rf $RPM_BUILD_ROOT

%{__make} \
	OPTFLAGS="%{rpmcflags}" \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	pkgcfgdir=${RPM_BUILD_ROOT}%{_libdir}/pkgconfig

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README COPYING ChangeLog TODO
%attr(755,root,root) %{_libdir}/libdhcp.so.*

%files devel
%defattr(644,root,root,755)
%doc examples
%attr(755,root,root) %{_libdir}/libdhcp.so
%{_includedir}/libdhcp
%{_pkgconfigdir}/libdhcp.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libdhcp.a
