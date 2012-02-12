# $Revision: 1.23 $, $Date: 2004/12/10 21:26:13 $
#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires database and interaction)
#
%define		pdir	DBD
%define		pnam	InterBase
Summary:	DBD::InterBase - DBI driver for Firebird and InterBase RDBMS server
Name:		perl-DBD-InterBase
Version:	0.48
Release:	1
License:	GPLv2+
Group:		Development/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	70d0142378ab928d9a75e465426d2437
Patch0:		%{name}-libsonly.patch
Patch1:		perl-DBD-InterBase-0.48-alt-dbdimp.patch
BuildRequires:	firebird-devel
BuildRequires:	perl-DBI >= 1.08
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-rpm-build-perl

%description
DBD::InterBase is a Perl module which works with the DBI module to
provide access to Firebird and InterBase databases.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1
%patch1 -p1 -b .perl514~

%build
echo %{_includedir}| perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorarch}/DBD/InterBase.pm
%dir %{perl_vendorarch}/DBD/InterBase
%{perl_vendorarch}/DBD/InterBase/*
%dir %{perl_vendorarch}/auto/DBD/InterBase
%{perl_vendorarch}/auto/DBD/InterBase/*
%{perl_vendorarch}/Bundle/DBD/*
#attr(755,root,root) %{perl_vendorarch}/auto/DBD/InterBase/InterBase.so
%{_mandir}/man3/DBD*
%{_mandir}/man3/Bundle*

