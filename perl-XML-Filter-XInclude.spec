#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	XML
%define		pnam	Filter-XInclude
%include	/usr/lib/rpm/macros.perl
Summary:	XML::Filter::XInclude - XInclude as a SAX filter
Summary(pl.UTF-8):	XML::Filter::XInclude - XInclude jako filtr SAX
Name:		perl-XML-Filter-XInclude
Version:	1.0
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6fd41f32027f3dbf6993fcef0ee81578
URL:		http://search.cpan.org/dist/XML-Filter-XInclude/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-URI
BuildRequires:	perl-XML-SAX >= 0.05
BuildRequires:	perl-XML-SAX-Writer
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The XML::Filter::XInclude Perl module implements a simple SAX filter
that provides XInclude support. It does NOT support XPointer.

%description -l pl.UTF-8
Moduł Perla XML::Filter::XInclude stanowi implementację filtra
obejmującego wsparcie dla XInclude. NIE wspiera on XPointer.

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
%{perl_vendorlib}/XML/*/*.pm
%{_mandir}/man3/*
