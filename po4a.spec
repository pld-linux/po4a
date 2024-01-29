Summary:	Framework to translate documentation and other materials
Summary(pl.UTF-8):	Szkielet do tłumaczenia dokumentacji i innych materiałów
Name:		po4a
Version:	0.70
Release:	1
License:	GPL v2+
Group:		Development/Tools
# Source0Download: https://github.com/mquinson/po4a/releases
Source0:	https://github.com/mquinson/po4a/files/14077820/%{name}-%{version}.tar.gz
# Source0-md5:	c9a1851f5c7adba77d76466dc97608fd
URL:		https://po4a.org/
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl-nons
BuildRequires:	perl-Encode
BuildRequires:	perl-Locale-gettext >= 1.01
BuildRequires:	perl-Module-Build >= 0.42
BuildRequires:	perl-Pod-Parser
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
%{__sed} -i -e '1s,/usr/bin/env perl,%{__perl},' msguntypot po4a* scripts/msgsearch

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

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/po4a/.packlist

# unify dir names
%{__mv} $RPM_BUILD_ROOT%{_mandir}/{sr_Cyrl,sr}
%{__mv} $RPM_BUILD_ROOT%{_mandir}/{zh_Hans,zh_CN}
%{__mv} $RPM_BUILD_ROOT%{_mandir}/{zh_Hant,zh_TW}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{sr_Cyrl,sr}
# zh_TW already exists
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/zh_Hant

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README.maintainers README.md TODO
%attr(755,root,root) %{_bindir}/msguntypot
%attr(755,root,root) %{_bindir}/po4a
%attr(755,root,root) %{_bindir}/po4a-display-man
%attr(755,root,root) %{_bindir}/po4a-display-pod
%attr(755,root,root) %{_bindir}/po4a-gettextize
%attr(755,root,root) %{_bindir}/po4a-normalize
%attr(755,root,root) %{_bindir}/po4a-translate
%attr(755,root,root) %{_bindir}/po4a-updatepo
%{perl_vendorlib}/Locale/Po4a
%{_mandir}/man1/msguntypot.1*
%{_mandir}/man1/po4a.1*
%{_mandir}/man1/po4a-display-man.1*
%{_mandir}/man1/po4a-display-pod.1*
%{_mandir}/man1/po4a-gettextize.1*
%{_mandir}/man1/po4a-normalize.1*
%{_mandir}/man1/po4a-translate.1*
%{_mandir}/man1/po4a-updatepo.1*
%{_mandir}/man3/Locale::Po4a::*.3*
%{_mandir}/man7/po4a.7*
%lang(ca) %{_mandir}/ca/man[137]/*
%lang(de) %{_mandir}/de/man[137]/*
%lang(eo) %{_mandir}/eo/man[137]/*
%lang(es) %{_mandir}/es/man[137]/*
%lang(fr) %{_mandir}/fr/man[137]/*
%lang(it) %{_mandir}/it/man[137]/*
%lang(ja) %{_mandir}/ja/man[137]/*
%lang(nb) %{_mandir}/nb/man[137]/*
%lang(nl) %{_mandir}/nl/man[137]/*
%lang(pl) %{_mandir}/pl/man[137]/*
%lang(pt) %{_mandir}/pt/man[137]/*
%lang(pt_BR) %{_mandir}/pt_BR/man[137]/*
%lang(ru) %{_mandir}/ru/man[137]/*
%lang(sr) %{_mandir}/sr/man[137]/*
%lang(uk) %{_mandir}/uk/man[137]/*
%lang(zh_CN) %{_mandir}/zh_CN/man[137]/*
%lang(zh_TW) %{_mandir}/zh_TW/man[137]/*
