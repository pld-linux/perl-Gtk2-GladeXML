#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires X server)
#
%define		pnam	Gtk2-GladeXML
Summary:	Mechanisms for instantiating and utilization of user interfaces created with Glade-2
Summary(pl.UTF-8):	Mechanizmy pozwalające na wykorzystywanie interfejsów stworzonych za pomocą Glade-2
Name:		perl-Gtk2-GladeXML
Version:	1.008
Release:	5
License:	LGPL
Group:		Development/Languages/Perl
Source0:	https://downloads.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	e4eba9d654198eb5bc4da7418d93d30a
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	perl-ExtUtils-Depends >= 0.300
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.000
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Glib-devel >= 1.140
BuildRequires:	perl-Gtk2-devel >= 1.140
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
Requires:	libglade2 >= 1:2.6.0
Requires:	perl-Glib >= 1.140
Requires:	perl-Gtk2 >= 1.140
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
After designing an application with Glade-2 the layout and
configuration is saved in a XML formatted file. libglade is a library
to load and use files of this particular XML format at application run
time. This module is a set of mappings of libglade.

Note: this module is deprecated and no longer maintained.

%description -l pl.UTF-8
Po zaprojektowaniu aplikacji korzystającej z Glade-2 jej wygląd i
konfiguracja są zapamiętywane w postaci plików w formacie XML.
libglade jest biblioteką służącą do odczytu i korzystania z tego
specyficznego formatu XML w czasie działania aplikacji. Ten moduł
stanowi zbiór odwzorowań biblioteki libglade.

Uwaga: ten moduł jest przestarzały i nie jest już utrzymywany.

%package devel
Summary:	Development files for Perl Gtk2-GladeXML bindings
Summary(pl.UTF-8):	Pliki programistyczne wiązań Gtk2-GladeXML dla Perla
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Requires:	libglade2-devel >= 1:2.6.0
Requires:	perl-Cairo-devel
Requires:	perl-Glib-devel >= 1.120
Requires:	perl-Gtk2-devel >= 1.121

%description devel
Development files for Perl Gtk2-GladeXML bindings.

%description devel -l pl.UTF-8
Pliki programistyczne wiązań Gtk2-GladeXML dla Perla.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog
%{perl_vendorarch}/Gtk2/GladeXML.pm
%dir %{perl_vendorarch}/Gtk2/GladeXML
%dir %{perl_vendorarch}/auto/Gtk2/GladeXML
%attr(755,root,root) %{perl_vendorarch}/auto/Gtk2/GladeXML/GladeXML.so
%{_mandir}/man3/Gtk2::GladeXML*.3pm*

%files devel
%defattr(644,root,root,755)
%{perl_vendorarch}/Gtk2/GladeXML/Install
