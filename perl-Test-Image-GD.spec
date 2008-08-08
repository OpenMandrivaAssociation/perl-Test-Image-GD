
%define realname   Test-Image-GD
%define version    0.03
%define release    %mkrel 2

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    A module for testing images using GD
Source:     http://www.cpan.org/modules/by-module/Test/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(File::Spec)
BuildRequires: perl(GD)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::Builder)
BuildRequires: perl(Test::Builder::Tester)
BuildRequires: perl(Test::More)

BuildArch: noarch

%description

This module is meant to be used for testing custom graphics, it attempts to
"visually" compare the images, this means it ignores invisible differences
like color palettes and metadata. It also provides some extra functions to
check the size of the image.





%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*



