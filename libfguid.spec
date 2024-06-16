# m4/libcerror.m4
%define		libcerror_ver	20120425
Summary:	Library to support GUID/UUID format
Summary(pl.UTF-8):	Biblioteka obsługująca format GUID/UUID
Name:		libfguid
Version:	20240415
Release:	1
License:	LGPL v3+
Group:		Libraries
#Source0Download: https://github.com/libyal/libfguid/releases
Source0:	https://github.com/libyal/libfguid/releases/download/%{version}/%{name}-alpha-%{version}.tar.gz
# Source0-md5:	1c9094a238cff6495a72c19ed2761f0d
URL:		https://github.com/libyal/libfguid/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.21
BuildRequires:	libcerror-devel >= %{libcerror_ver}
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
Requires:	libcerror >= %{libcerror_ver}
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
Requires:	libcerror-devel >= %{libcerror_ver}

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

%build
%{__gettextize}
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
