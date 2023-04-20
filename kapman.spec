#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kapman
Version  : 23.04.0
Release  : 51
URL      : https://download.kde.org/stable/release-service/23.04.0/src/kapman-23.04.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.04.0/src/kapman-23.04.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.04.0/src/kapman-23.04.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0
Requires: kapman-bin = %{version}-%{release}
Requires: kapman-data = %{version}-%{release}
Requires: kapman-license = %{version}-%{release}
Requires: kapman-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libkdegames-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package bin
Summary: bin components for the kapman package.
Group: Binaries
Requires: kapman-data = %{version}-%{release}
Requires: kapman-license = %{version}-%{release}

%description bin
bin components for the kapman package.


%package data
Summary: data components for the kapman package.
Group: Data

%description data
data components for the kapman package.


%package doc
Summary: doc components for the kapman package.
Group: Documentation

%description doc
doc components for the kapman package.


%package license
Summary: license components for the kapman package.
Group: Default

%description license
license components for the kapman package.


%package locales
Summary: locales components for the kapman package.
Group: Default

%description locales
locales components for the kapman package.


%prep
%setup -q -n kapman-23.04.0
cd %{_builddir}/kapman-23.04.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1682030717
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1682030717
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kapman
cp %{_builddir}/kapman-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kapman/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/kapman-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kapman/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kapman-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kapman/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kapman-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kapman/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/kapman-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kapman/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
pushd clr-build
%make_install
popd
%find_lang kapman

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kapman

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kapman.desktop
/usr/share/icons/hicolor/128x128/apps/kapman.png
/usr/share/icons/hicolor/16x16/apps/kapman.png
/usr/share/icons/hicolor/22x22/apps/kapman.png
/usr/share/icons/hicolor/32x32/apps/kapman.png
/usr/share/icons/hicolor/48x48/apps/kapman.png
/usr/share/icons/hicolor/64x64/apps/kapman.png
/usr/share/kapman/defaultmaze.xml
/usr/share/kapman/themes/invisible.desktop
/usr/share/kapman/themes/invisible.svgz
/usr/share/kapman/themes/invisible_preview.png
/usr/share/kapman/themes/matches.desktop
/usr/share/kapman/themes/matches.svgz
/usr/share/kapman/themes/matches_preview.png
/usr/share/kapman/themes/mountain.copyright
/usr/share/kapman/themes/mountain.desktop
/usr/share/kapman/themes/mountain.svgz
/usr/share/kapman/themes/mountain_preview.png
/usr/share/kapman/themes/mummies_crypt.desktop
/usr/share/kapman/themes/mummies_crypt.svgz
/usr/share/kapman/themes/mummies_crypt_preview.png
/usr/share/kapman/themes/retro.desktop
/usr/share/kapman/themes/retro.svgz
/usr/share/kapman/themes/retro_preview.png
/usr/share/metainfo/org.kde.kapman.appdata.xml
/usr/share/sounds/kapman/bonus.ogg
/usr/share/sounds/kapman/energizer.ogg
/usr/share/sounds/kapman/gameover.ogg
/usr/share/sounds/kapman/ghost.ogg
/usr/share/sounds/kapman/levelup.ogg
/usr/share/sounds/kapman/life.ogg
/usr/share/sounds/kapman/pill.ogg

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kapman/config.png
/usr/share/doc/HTML/ca/kapman/index.cache.bz2
/usr/share/doc/HTML/ca/kapman/index.docbook
/usr/share/doc/HTML/ca/kapman/kapman.png
/usr/share/doc/HTML/de/kapman/config.png
/usr/share/doc/HTML/de/kapman/index.cache.bz2
/usr/share/doc/HTML/de/kapman/index.docbook
/usr/share/doc/HTML/de/kapman/kapman.png
/usr/share/doc/HTML/en/kapman/config.png
/usr/share/doc/HTML/en/kapman/index.cache.bz2
/usr/share/doc/HTML/en/kapman/index.docbook
/usr/share/doc/HTML/en/kapman/kapman.png
/usr/share/doc/HTML/es/kapman/index.cache.bz2
/usr/share/doc/HTML/es/kapman/index.docbook
/usr/share/doc/HTML/et/kapman/index.cache.bz2
/usr/share/doc/HTML/et/kapman/index.docbook
/usr/share/doc/HTML/fr/kapman/config.png
/usr/share/doc/HTML/fr/kapman/index.cache.bz2
/usr/share/doc/HTML/fr/kapman/index.docbook
/usr/share/doc/HTML/fr/kapman/kapman.png
/usr/share/doc/HTML/it/kapman/index.cache.bz2
/usr/share/doc/HTML/it/kapman/index.docbook
/usr/share/doc/HTML/nl/kapman/index.cache.bz2
/usr/share/doc/HTML/nl/kapman/index.docbook
/usr/share/doc/HTML/pl/kapman/config.png
/usr/share/doc/HTML/pl/kapman/index.cache.bz2
/usr/share/doc/HTML/pl/kapman/index.docbook
/usr/share/doc/HTML/pl/kapman/kapman.png
/usr/share/doc/HTML/pt/kapman/index.cache.bz2
/usr/share/doc/HTML/pt/kapman/index.docbook
/usr/share/doc/HTML/pt_BR/kapman/config.png
/usr/share/doc/HTML/pt_BR/kapman/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kapman/index.docbook
/usr/share/doc/HTML/pt_BR/kapman/kapman.png
/usr/share/doc/HTML/sv/kapman/index.cache.bz2
/usr/share/doc/HTML/sv/kapman/index.docbook
/usr/share/doc/HTML/uk/kapman/config.png
/usr/share/doc/HTML/uk/kapman/index.cache.bz2
/usr/share/doc/HTML/uk/kapman/index.docbook
/usr/share/doc/HTML/uk/kapman/kapman.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kapman/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kapman/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kapman/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/kapman/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kapman/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c

%files locales -f kapman.lang
%defattr(-,root,root,-)

