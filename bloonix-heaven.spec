Summary: Bloonix Heaven
Name: bloonix-heaven
Version: 0.14
Release: 1%{dist}
License: Commercial
Group: Utilities/System
Distribution: RHEL and CentOS

Packager: Jonny Schulz <js@bloonix.de>
Vendor: Bloonix

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Source0: http://download.bloonix.de/sources/%{name}-%{version}.tar.gz
Requires: bloonix-core >= 0.23
Requires: bloonix-fcgi
Requires: perl-JSON-XS
Requires: perl(JSON)
Requires: perl(Log::Handler)
Requires: perl(Getopt::Long)
AutoReqProv: no

%description
bloonix-heaven is a mvc web framework.

%prep
%setup -q -n %{name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
%{__perl} Build

%install
%{__perl} Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -name .packlist -exec %{__rm} {} \;
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find %{buildroot} -type d -depth -exec rmdir {} 2>/dev/null ';'
%{_fixperms} %{buildroot}/*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog INSTALL LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Mar 29 2016 Jonny Schulz <js@bloonix.de> - 0.14-1
- Extra release because the gpg key of bloonix is updated.
* Mon Nov 16 2015 Jonny Schulz <js@bloonix.de> - 0.13-1
- Added regexp to validate ipv4 and ipv6 addresses with network.
- Moved Bloonix::Validator to the core package and renamed it to
  Bloonix::Validate.
* Thu Aug 06 2015 Jonny Schulz <js@bloonix.de> - 0.12-1
- Bloonix::Validator: added a postcheck method.
* Thu May 07 2015 Jonny Schulz <js@bloonix.de> - 0.11-1
- Bloonix::Validator: new constraint param_value
- Bloonix::Validator: fixed duplicate entries
* Wed Apr 15 2015 Jonny Schulz <js@bloonix.de> - 0.10-1
- Bloonix::Validator can now return mandatory and optional parameters.
* Sat Mar 21 2015 Jonny Schulz <js@bloonix.de> - 0.9-1
- ProcManager and FCGI were splittet into 2 modules.
* Thu Dec 18 2014 Jonny Schulz <js@bloonix.de> - 0.8-1
- Now views are not processed if a redirect is active.
* Fri Dec 12 2014 Jonny Schulz <js@bloonix.de> - 0.7-1
- New accessor text() added.
* Thu Dec 11 2014 Jonny Schulz <js@bloonix.de> - 0.6-1
- Regex for E-Mail addresses extended. The sign "=" is now allowed.
* Mon Dec 08 2014 Jonny Schulz <js@bloonix.de> - 0.5-1
- Fixed collection process size statistics. /proc/$pid/statm
  is not available on other operation systems.
- Implemented include and wrapper for Heaven/Template.pm.
- Making the template cache persistent.
- Added argument cache_enabled to enable/disable the template
  cache.
- Fixed undefined values warning in templates. Added // ''.
- Added line numbers to the template code.
* Mon Nov 03 2014 Jonny Schulz <js@bloonix.de> - 0.4-1
- Updated the license information.
* Fri Oct 24 2014 Jonny Schulz <js@bloonix.de> - 0.3-1
- Disable die_on_errors by default so that the logger
  does not die on errors.
* Thu Oct 16 2014 Jonny Schulz <js@bloonix.de> - 0.2-1
- Improved the error handling.
- Added parameter "minimal" to validate().
- Deleted ModelLoader.pm.
* Mon Aug 25 2014 Jonny Schulz <js@bloonix.de> - 0.1-1
- Initial release.
