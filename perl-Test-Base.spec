#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Base
Summary:	Test::Base - A Data Driven Testing Framework
Summary(pl.UTF-8):	Test::Base - środowisko testów opartych na danych
Name:		perl-Test-Base
Version:	0.88
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ced0cd86b099f9fd2cd73df1f46ab5e9
URL:		http://search.cpan.org/dist/Test-Base/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.42
BuildRequires:	perl-Spiffy >= 0.40
BuildRequires:	perl-Test-Deep
BuildRequires:	perl-Test-Tester
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::Base - A Data Driven Testing Framework.

%description -l pl.UTF-8
Test::Base - środowisko testów opartych na danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Test/Base.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/Base.pm
%{perl_vendorlib}/Test/Base
%{_mandir}/man3/Test::Base*.3pm*
