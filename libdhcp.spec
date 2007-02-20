Summary:	A library for network interface configuration with DHCP
Name:		libdhcp
Version:	1.20
Release:	1
License:	GPL
Group:		Development/Libraries
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

%package devel
Summary:	C header files for development with libdhcp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libdhcp4client-devel
Requires:	libdhcp6client-devel
Requires:	libnl-devel

%description devel
C header files for development with libdhcp.

%package static
Summary:	Static libdhcp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libdhcp.

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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

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
