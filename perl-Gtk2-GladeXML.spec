%include	/usr/lib/rpm/macros.perl

%define		_realname	Gtk2-GladeXML

Summary:	Provides mechinisms for instantiating and utilization of user interfaces created with Glade-2
Summary(pl):	Udostêpnia mechanizmy pozwalaj±ce na wykorzystywanie interfejsów stworzonych za pomoc± Glade-2
Name:		perl-Gtk2-GladeXML
Version:	0.26
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/%{_realname}-%{version}.tar.gz
# Source0-md5:	d25d2dde67a15b695ac6a1bc01584e9f
URL:		http://gtk2-perl-sourceforge.net/
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	perl-Gtk2 >= 0.95
BuildRequires:	perl-Glib >= 0.95
BuildRequires:	perl-devel >= 5.8.0
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
%setup -q -n %{_realname}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

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
%attr(755,root,root) %{perl_vendorarch}/auto/Gtk2/GladeXML/*.so
%{perl_vendorarch}/auto/Gtk2/GladeXML/*.bs
%{_mandir}/man3/*
