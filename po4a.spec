%include	/usr/lib/rpm/macros.perl
Summary:	Framework to translate documentation and other materials
Summary(pl):	Szkielet do t³umaczenia dokumentacji i innych materia³ów
Name:		po4a
Version:	0.29
Release:	1
License:	GPL
Group:		Development/Tools
#Source0Download: http://alioth.debian.org/frs/?group_id=30267
Source0:	http://alioth.debian.org/frs/download.php/1798/%{name}-%{version}.tar.gz
# Source0-md5:	522c94f4c25e0d18bb00f33d209fe2a8
URL:		http://alioth.debian.org/projects/po4a/
BuildRequires:	perl-Locale-gettext >= 1.01
BuildRequires:	perl-Module-Build
BuildRequires:	perl-Text-WrapI18N
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Po4a eases translation work, and in particular the maintenance of
translations, using gettext tools on areas where they were not
expected like documentation.

%description -l pl
po4a u³atwia pracê przy t³umaczeniu, a w szczególno¶ci utrzymywanie
t³umaczeñ przy u¿yciu narzêdzi gettexta w obszarach, gdzie nie by³y
przewidywane, jak na przyk³ad dokumentacja.

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
%{_mandir}/man[137]/*
%lang(ca) %{_mandir}/ca/man[137]/*
%lang(es) %{_mandir}/es/man[137]/*
%lang(fr) %{_mandir}/fr/man[137]/*
%lang(it) %{_mandir}/it/man[137]/*
%lang(pl) %{_mandir}/pl/man[137]/*
