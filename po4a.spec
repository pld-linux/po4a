%include	/usr/lib/rpm/macros.perl
Summary:	Framework to translate documentation and other materials
Summary(pl.UTF-8):	Szkielet do tłumaczenia dokumentacji i innych materiałów
Name:		po4a
Version:	0.41
Release:	1
License:	GPL
Group:		Development/Tools
# Source0Download: http://alioth.debian.org/frs/?group_id=30267
Source0:	http://alioth.debian.org/frs/download.php/3472/%{name}-%{version}.tar.gz
# Source0-md5:	93b3137502a749bdc3a059466f2a19d2
URL:		http://alioth.debian.org/projects/po4a/
BuildRequires:	perl-Locale-gettext >= 1.01
BuildRequires:	perl-Module-Build
BuildRequires:	perl-Text-WrapI18N
BuildRequires:	perl-YAML
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sed >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Po4a eases translation work, and in particular the maintenance of
translations, using gettext tools on areas where they were not
expected like documentation.

%description -l pl.UTF-8
po4a ułatwia pracę przy tłumaczeniu, a w szczególności utrzymywanie
tłumaczeń przy użyciu narzędzi gettexta w obszarach, gdzie nie były
przewidywane, jak na przykład dokumentacja.

%prep
%setup -q

# fix #!%{_bindir}/env perl -w -> #!%{__perl}:
%{__sed} -i -e '1s,^#!.*perl,#!%{__perl},' po4a* scripts/*

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT
./Build install

%find_lang %{name}

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/po4a/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README* TODO
%attr(755,root,root) %{_bindir}/msguntypot
%attr(755,root,root) %{_bindir}/po4a
%attr(755,root,root) %{_bindir}/po4a-build
%attr(755,root,root) %{_bindir}/po4a-gettextize
%attr(755,root,root) %{_bindir}/po4a-normalize
%attr(755,root,root) %{_bindir}/po4a-translate
%attr(755,root,root) %{_bindir}/po4a-updatepo
%attr(755,root,root) %{_bindir}/po4aman-display-po
%attr(755,root,root) %{_bindir}/po4apod-display-po
%{perl_vendorlib}/Locale/Po4a
%{_mandir}/man[1357]/*
%lang(ca) %{_mandir}/ca/man[1357]/*
%lang(es) %{_mandir}/es/man[1357]/*
%lang(fr) %{_mandir}/fr/man[1357]/*
%lang(it) %{_mandir}/it/man[1357]/*
%lang(pl) %{_mandir}/pl/man[1357]/*
%lang(ja) %{_mandir}/ja/man[1357]/*
%lang(ru) %{_mandir}/ru/man[1357]/*
