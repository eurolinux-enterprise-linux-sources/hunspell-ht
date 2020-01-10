Name: hunspell-ht
Summary: Haitian Creole hunspell dictionaries
Version: 0.06
Release: 6%{?dist}
Group: Applications/Text
Source: http://extensions.services.openoffice.org/files/3247/3/%{name}-%{version}.oxt
URL: http://kok.logipam.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv3+
BuildArch: noarch

Requires: hunspell

%description
Haitian Creole hunspell dictionaries.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/ht_HT.* $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc dictionaries/README_ht_HT.txt LICENSES-en.txt
%{_datadir}/myspell/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.06-6
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 16 2009 Caolan McNamara <caolanm@redhat.com> - 0.06-1
- latest version

* Thu Dec 10 2009 Caolan McNamara <caolanm@redhat.com> - 0.05-1
- latest version

* Thu Nov 19 2009 Caolan McNamara <caolanm@redhat.com> - 0.03.3-1
- initial version

* Mon Nov 16 2009 Caolan McNamara <caolanm@redhat.com> - 0.02-1
- initial version
