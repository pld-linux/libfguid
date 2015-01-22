Summary:	Library to support GUID/UUID format
Summary(pl.UTF-8):	Biblioteka obsługująca format GUID/UUID
Name:		libfguid
Version:	20150104
Release:	1
License:	LGPL v3+
Group:		Libraries
Source0:	https://github.com/libyal/libfguid/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	e19ab864a5338182003f71389fa2d042
Patch0:		%{name}-system-libs.patch
URL:		https://github.com/libyal/libfguid/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	libcerror-devel >= 20120425
BuildRequires:	libcstring-devel >= 20120425
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	libcerror >= 20120425
Requires:	libcstring >= 20120425
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libfguid is a library to support GUID/UUID format.

%description -l pl.UTF-8
libfguid to biblioteka obsługująca format GUID/UUID.

%package devel
Summary:	Header files for libfguid library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libfguid
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libcerror-devel >= 20120425
Requires:	libcstring-devel >= 20120425

%description devel
Header files for libfguid library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libfguid.

%package static
Summary:	Static libfguid library
Summary(pl.UTF-8):	Statyczna biblioteka libfguid
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libfguid library.

%description static -l pl.UTF-8
Statyczna biblioteka libfguid.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__sed} -i -e 's/ po\/Makefile.in//' configure.ac
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libfguid.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libfguid.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfguid.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfguid.so
%{_includedir}/libfguid
%{_includedir}/libfguid.h
%{_pkgconfigdir}/libfguid.pc
%{_mandir}/man3/libfguid.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libfguid.a
