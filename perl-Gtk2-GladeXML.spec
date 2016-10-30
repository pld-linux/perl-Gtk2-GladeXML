#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires X server)
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	Gtk2-GladeXML
Summary:	Mechanisms for instantiating and utilization of user interfaces created with Glade-2
Summary(pl.UTF-8):	Mechanizmy pozwalające na wykorzystywanie interfejsów stworzonych za pomocą Glade-2
Name:		perl-Gtk2-GladeXML
Version:	1.007
Release:	9
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	e6ca234e2a9f0221263acd2a593c583b
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	libglade2-devel >= 2.6.0
BuildRequires:	perl-ExtUtils-Depends
BuildRequires:	perl-ExtUtils-PkgConfig
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Glib >= 1.140
BuildRequires:	perl-Gtk2 >= 1.140
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Glib >= 1.140
Requires:	perl-Gtk2 >= 1.140
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
After designing an application with Glade-2 the layout and
configuration is saved in a XML formatted file. libglade is a library
to load and use files of this particular XML format at application run
time. This module is a set of mappings of libglade.

%description -l pl.UTF-8
Po zaprojektowaniu aplikacji korzystającej z Glade-2 jej wygląd i
konfiguracja są zapamiętywane w postaci plików w formacie XML.
libglade jest biblioteką służącą do odczytu i korzystania z tego
specyficznego formatu XML w czasie działania aplikacji. Ten moduł
stanowi zbiór odwzorowań biblioteki libglade.

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog
%{perl_vendorarch}/Gtk2/GladeXML.pm
%dir %{perl_vendorarch}/Gtk2/GladeXML
%dir %{perl_vendorarch}/auto/Gtk2/GladeXML
%attr(755,root,root) %{perl_vendorarch}/auto/Gtk2/GladeXML/*.so
%{perl_vendorarch}/Gtk2/GladeXML/Install
%{_mandir}/man3/*
