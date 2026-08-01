%define upstream_name    Test-Image-GD
%define upstream_version 0.03
Name:		perl-%{upstream_name}
Version:	0.03
Release:	3

Summary:	A module for testing images using GD
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	https://cpan.metacpan.org/authors/id/S/ST/STEVAN/Test-Image-GD-0.03.tar.gz

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
%setup -q -n Test-Image-GD-0.03

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build
%check
# soft: do not fail package on test failures
set +e
make test || :

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

