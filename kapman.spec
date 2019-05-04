#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kapman
Version  : 19.04.0
Release  : 7
URL      : https://download.kde.org/stable/applications/19.04.0/src/kapman-19.04.0.tar.xz
Source0  : https://download.kde.org/stable/applications/19.04.0/src/kapman-19.04.0.tar.xz
Source99 : https://download.kde.org/stable/applications/19.04.0/src/kapman-19.04.0.tar.xz.sig
Summary  : A clone of the well known game Pac-Man
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: kapman-bin = %{version}-%{release}
Requires: kapman-data = %{version}-%{release}
Requires: kapman-license = %{version}-%{release}
Requires: kapman-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : libkdegames-dev
BuildRequires : qtbase-dev mesa-dev

%description
EXTENDED

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
%setup -q -n kapman-19.04.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557001145
mkdir -p clr-build
pushd clr-build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1557001145
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kapman
cp COPYING %{buildroot}/usr/share/package-licenses/kapman/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/kapman/COPYING.DOC
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
/usr/share/kxmlgui5/kapman/kapmanui.rc
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
/usr/share/package-licenses/kapman/COPYING
/usr/share/package-licenses/kapman/COPYING.DOC

%files locales -f kapman.lang
%defattr(-,root,root,-)

