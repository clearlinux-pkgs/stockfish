#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : stockfish
Version  : 10
Release  : 2
URL      : https://github.com/official-stockfish/Stockfish/files/2629657/sf_10.tar.gz
Source0  : https://github.com/official-stockfish/Stockfish/files/2629657/sf_10.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: stockfish-bin = %{version}-%{release}
Requires: stockfish-license = %{version}-%{release}

%description
### Overview
[![Build Status](https://travis-ci.org/official-stockfish/Stockfish.svg?branch=master)](https://travis-ci.org/official-stockfish/Stockfish)
[![Build Status](https://ci.appveyor.com/api/projects/status/github/official-stockfish/Stockfish?svg=true)](https://ci.appveyor.com/project/mcostalba/stockfish)

%package bin
Summary: bin components for the stockfish package.
Group: Binaries
Requires: stockfish-license = %{version}-%{release}

%description bin
bin components for the stockfish package.


%package license
Summary: license components for the stockfish package.
Group: Default

%description license
license components for the stockfish package.


%prep
%setup -q -n Stockfish-sf_10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567003583
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
pushd src
make  %{?_smp_mflags} build ARCH=x86-64-bmi2 COMP=gcc
popd


%install
export SOURCE_DATE_EPOCH=1567003583
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/stockfish
cp Copying.txt %{buildroot}/usr/share/package-licenses/stockfish/Copying.txt
pushd src
%make_install PREFIX=%{buildroot}/usr
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/stockfish

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/stockfish/Copying.txt
