%define modname	Params-Classify
%define modver	0.015

Summary:	Argument type classification
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	4
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/Params::Classify
Source0:	http://www.cpan.org/modules/by-module/Params/%{modname}-%{modver}.tar.gz
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::CBuilder)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(parent)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(DynaLoader::Functions)
BuildRequires:	perl(Devel::CallChecker)
BuildRequires:	perl-devel

%description
This module provides various type-testing functions. These are intended for
functions that, unlike most Perl code, care what type of data they are
operating on. For example, some functions wish to behave differently
depending on the type of their arguments (like overloaded functions in
C++).

There are two flavours of function in this module. Functions of the first
flavour only provide type classification, to allow code to discriminate
between argument types. Functions of the second flavour package up the most
common type of type discrimination:	checking that an argument is of an
expected type. The functions come in matched pairs, of the two flavours,
and so the type enforcement functions handle only the simplest requirements
for arguments of the types handled by the classification functions.
Enforcement of more complex types may, of course, be built using the
classification functions, or it may be more convenient to use a module
designed for the more complex job, such as the Params::Validate manpage.

This module is implemented in XS, with a pure Perl backup version for
systems that can't handle XS.

%prep
%setup -qn %{modname}-%{modver}
%__perl Build.PL installdirs=vendor optimize="%{optflags}"

%build
./Build

%check
./Build test

%install
./Build install destdir="%{buildroot}"

%files
%doc Changes README
%{perl_vendorarch}/*
%{_mandir}/man3/*
