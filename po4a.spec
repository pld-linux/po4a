%include	/usr/lib/rpm/macros.perl
Summary:	Framework to translate documentation and other materials
Summary(pl.UTF-8):	Szkielet do tłumaczenia dokumentacji i innych materiałów
Name:		po4a
Version:	0.53
Release:	1
License:	GPL v2+
Group:		Development/Tools
# Source0Download: https://github.com/mquinson/po4a/releases
Source0:	https://github.com/mquinson/po4a/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	5f0728b762352edce650ad0165e6a173
URL:		https://po4a.org/
BuildRequires:	perl-Encode
BuildRequires:	perl-Locale-gettext >= 1.01
BuildRequires:	perl-Module-Build >= 0.42
BuildRequires:	perl-SGMLS
BuildRequires:	perl-Term-ReadKey
BuildRequires:	perl-Text-WrapI18N
BuildRequires:	perl-Unicode-LineBreak
BuildRequires:	perl-YAML-Tiny
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sed >= 4.0
%if %(locale -a | grep -q '^C\.utf8$'; echo $?)
BuildRequires:	glibc-localedb-all
%endif
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
	perl=%{__perl} \
	installdirs=vendor

LC_ALL=C.UTF-8 \
./Build

%install
rm -rf $RPM_BUILD_ROOT
./Build install \
	destdir=$RPM_BUILD_ROOT

%find_lang %{name}

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/po4a/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README README.maintainers TODO
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
%{_mandir}/man1/msguntypot.1*
%{_mandir}/man1/po4a.1*
%{_mandir}/man1/po4a-build.1*
%{_mandir}/man1/po4a-gettextize.1*
%{_mandir}/man1/po4a-normalize.1*
%{_mandir}/man1/po4a-translate.1*
%{_mandir}/man1/po4a-updatepo.1*
%{_mandir}/man1/po4aman-display-po.1*
%{_mandir}/man1/po4apod-display-po.1*
%{_mandir}/man3/Locale::Po4a::*.3*
%{_mandir}/man7/po4a.7*
%{_mandir}/man5/po4a-build.conf.5*
%{_mandir}/man7/po4a-runtime.7*
%lang(ca) %{_mandir}/ca/man[1357]/*
%lang(ca) %{_mandir}/de/man[1357]/*
%lang(es) %{_mandir}/es/man[1357]/*
%lang(fr) %{_mandir}/fr/man[1357]/*
%lang(it) %{_mandir}/it/man[1357]/*
%lang(pl) %{_mandir}/pl/man[1357]/*
%lang(pt_BR) %{_mandir}/pt_BR/man[1357]/*
%lang(ja) %{_mandir}/ja/man[1357]/*
%lang(pt) %{_mandir}/pt/man[1357]/*
%lang(ru) %{_mandir}/ru/man[1357]/*
%lang(uk) %{_mandir}/uk/man[1357]/*
