#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Base
Summary:	Test::Base - A Data Driven Testing Framework
Summary(pl.UTF-8):	Test::Base - środowisko testowe w oparciu o dane
Name:		perl-Test-Base
Version:	0.60
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7d839807da66d69db32fc4b22994f9e4
URL:		http://search.cpan.org/dist/Test-Base/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.42
BuildRequires:	perl-Spiffy >= 0.30
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::Base - A Data Driven Testing Framework

%description -l pl.UTF-8
Test::Base - środowisko testowe w oparciu o dane

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/*.pm
%{perl_vendorlib}/Test/Base
%{perl_vendorlib}/Module/Install/TestBase.pm
%{_mandir}/man3/*