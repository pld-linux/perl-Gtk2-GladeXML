#
# Conditional build:
%bcond_with tests       # perform "make test" (requires X server)
#
%include        /usr/lib/rpm/macros.perl
%define pnam    Gtk2-GladeXML
Summary:	Mechanisms for instantiating and utilization of user interfaces created with Glade-2
Summary(pl):	Mechanizmy pozwalaj±ce na wykorzystywanie interfejsów stworzonych za pomoc± Glade-2
Name:		perl-%{pnam}
Version:	0.94
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	3784c11601b433fec7bc7412194c2f2c
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	perl-Gtk2 >= 1.00
BuildRequires:	perl-Glib >= 1.00
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
After designing an application with Glade-2 the layout and
configuration is saved in a XML formatted file. libglade is a library
to load and use files of this particular XML format at application run
time. This module is a set of mappings of libglade.

%description -l pl
Po zaprojektowaniu aplikacji korzystaj±cej z Glade-2 jej wygl±d i
konfiguracja s± zapamiêtywane w postaci plików w formacie XML.
libglade jest bibliotek± s³u¿±c± do odczytu i korzystania z tego
specyficznego formatu XML w czasie dzia³ania aplikacji. Ten modu³
stanowi zbiór odwzorowañ biblioteki libglade.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
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
%{perl_vendorarch}/auto/Gtk2/GladeXML/*.bs
%{_mandir}/man3/*
