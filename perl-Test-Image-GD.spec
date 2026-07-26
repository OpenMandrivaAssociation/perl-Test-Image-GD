%define upstream_name    Test-Image-GD
Name:		perl-%{upstream_name}
Version:	0.03
Release:	6

Summary:	A module for testing images using GD
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(GD)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::Builder::Tester)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This module is meant to be used for testing custom graphics, it attempts to
"visually" compare the images, this means it ignores invisible differences
like color palettes and metadata. It also provides some extra functions to
check the size of the image.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.30.0-2mdv2011.0
+ Revision: 658887
- rebuild for updated spec-helper

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 405551
- rebuild using %0.03 Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.03-2mdv2009.0
+ Revision: 268735
- rebuild early 2009.0 package (before pixel changes)

* Mon Apr 28 2008 Olivier Thauvin <nanardon@mandriva.org> 0.03-1mdv2009.0
+ Revision: 198022
- import perl-Test-Image-GD


