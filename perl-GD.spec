#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-GD
Version  : 2.83
Release  : 28
URL      : https://cpan.metacpan.org/authors/id/R/RU/RURBAN/GD-2.83.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RU/RURBAN/GD-2.83.tar.gz
Summary  : 'Perl interface to the libgd graphics library'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl Artistic-2.0 GPL-1.0
Requires: perl-GD-bin = %{version}-%{release}
Requires: perl-GD-license = %{version}-%{release}
Requires: perl-GD-man = %{version}-%{release}
Requires: perl-GD-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(ExtUtils::PkgConfig)
BuildRequires : perl(File::Which)
BuildRequires : perl(Test::Fork)
BuildRequires : perl(Test::NoWarnings)
BuildRequires : pkgconfig(gdlib)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
GD.pm -- A perl5 interface to Thomas Boutell's gd library.
ABSTRACT:
This is a autoloadable interface module for libgd, a popular library
for creating and manipulating PNG files.  With this library you can
create PNG images on the fly or modify existing files.  Features
include:

%package bin
Summary: bin components for the perl-GD package.
Group: Binaries
Requires: perl-GD-license = %{version}-%{release}

%description bin
bin components for the perl-GD package.


%package dev
Summary: dev components for the perl-GD package.
Group: Development
Requires: perl-GD-bin = %{version}-%{release}
Provides: perl-GD-devel = %{version}-%{release}
Requires: perl-GD = %{version}-%{release}

%description dev
dev components for the perl-GD package.


%package license
Summary: license components for the perl-GD package.
Group: Default

%description license
license components for the perl-GD package.


%package man
Summary: man components for the perl-GD package.
Group: Default

%description man
man components for the perl-GD package.


%package perl
Summary: perl components for the perl-GD package.
Group: Default
Requires: perl-GD = %{version}-%{release}

%description perl
perl components for the perl-GD package.


%prep
%setup -q -n GD-2.83
cd %{_builddir}/GD-2.83
pushd ..
cp -a GD-2.83 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-GD
cp %{_builddir}/GD-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-GD/a670a0f6bf54244e98000dac01027a0cf9c01ee2 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bdf2gdfont.pl

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/GD.3
/usr/share/man/man3/GD::Group.3
/usr/share/man/man3/GD::Image.3
/usr/share/man/man3/GD::Polygon.3
/usr/share/man/man3/GD::Polyline.3
/usr/share/man/man3/GD::Simple.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-GD/a670a0f6bf54244e98000dac01027a0cf9c01ee2

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/bdf2gdfont.pl.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
