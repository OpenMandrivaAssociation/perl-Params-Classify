%define upstream_name    Params-Classify
%define upstream_version 0.013

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Argument type classification
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Params/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(parent)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides various type-testing functions. These are intended for
functions that, unlike most Perl code, care what type of data they are
operating on. For example, some functions wish to behave differently
depending on the type of their arguments (like overloaded functions in
C++).

There are two flavours of function in this module. Functions of the first
flavour only provide type classification, to allow code to discriminate
between argument types. Functions of the second flavour package up the most
common type of type discrimination: checking that an argument is of an
expected type. The functions come in matched pairs, of the two flavours,
and so the type enforcement functions handle only the simplest requirements
for arguments of the types handled by the classification functions.
Enforcement of more complex types may, of course, be built using the
classification functions, or it may be more convenient to use a module
designed for the more complex job, such as the Params::Validate manpage.

This module is implemented in XS, with a pure Perl backup version for
systems that can't handle XS.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Sun Nov 28 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.13.0-1mdv2011.0
+ Revision: 602384
- update to new version 0.013

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.12.0-1mdv2011.0
+ Revision: 596637
- update to 0.012

* Sat Aug 28 2010 Shlomi Fish <shlomif@mandriva.org> 0.11.0-1mdv2011.0
+ Revision: 573815
- import perl-Params-Classify

