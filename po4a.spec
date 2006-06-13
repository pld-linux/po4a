%include	/usr/lib/rpm/macros.perl
Summary:	Framework to translate documentation and other materials
Name:		po4a
Version:	0.25
Release:	0.1
License:	GPL
Group:		Development/Tools
Source0:	http://alioth.debian.org/download.php/1556/%{name}-%{version}.tar.gz
# Source0-md5:	e868a14e5e5212d1e1d78e0905f01fe5
URL:		http://alioth.debian.org/projects/po4a/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Po4a eases translation work, and in particular the maintenance of
translations, using gettext tools on areas where they were not
expected like documentation.

%prep
%setup -q

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README* TODO
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Locale/Po4a
%lang(ca) %{_mandir}/ca/man[137]/*
%lang(es) %{_mandir}/es/man[137]/*
%lang(fr) %{_mandir}/fr/man[137]/*
%lang(it) %{_mandir}/it/man[137]/*
%lang(pl) %{_mandir}/pl/man[137]/*
%{_mandir}/man[137]/*
