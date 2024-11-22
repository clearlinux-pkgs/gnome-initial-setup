#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v21
# autospec commit: 5424026
#
Name     : gnome-initial-setup
Version  : 47.2
Release  : 86
URL      : https://download.gnome.org/sources/gnome-initial-setup/47/gnome-initial-setup-47.2.tar.xz
Source0  : https://download.gnome.org/sources/gnome-initial-setup/47/gnome-initial-setup-47.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: gnome-initial-setup-data = %{version}-%{release}
Requires: gnome-initial-setup-libexec = %{version}-%{release}
Requires: gnome-initial-setup-license = %{version}-%{release}
Requires: gnome-initial-setup-locales = %{version}-%{release}
BuildRequires : accountsservice-dev
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : dconf-dev
BuildRequires : gdm-dev
BuildRequires : ibus-dev
BuildRequires : libpwquality-dev
BuildRequires : pkgconfig(accountsservice)
BuildRequires : pkgconfig(cheese)
BuildRequires : pkgconfig(cheese-gtk)
BuildRequires : pkgconfig(gdm)
BuildRequires : pkgconfig(geocode-glib-2.0)
BuildRequires : pkgconfig(gnome-desktop-3.0)
BuildRequires : pkgconfig(goa-1.0)
BuildRequires : pkgconfig(goa-backend-1.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(gweather4)
BuildRequires : pkgconfig(ibus-1.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(krb5)
BuildRequires : pkgconfig(libgeoclue-2.0)
BuildRequires : pkgconfig(libnm)
BuildRequires : pkgconfig(libnma-gtk4)
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : pkgconfig(pwquality)
BuildRequires : pkgconfig(webkitgtk-6.0)
BuildRequires : polkit-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
GNOME Initial Setup
===================
After acquiring or installing a new system there are a few essential things
to set up before use. Initial Setup aims to provide a simple, easy, and safe way
to prepare a new system. This should only include a few essential steps for
which we can't provide good defaults. The desired experience is that the system
boots straight into Initial Setup, and when the setup tasks are completed, we
smoothly transition into the user session for the newly-created user account.

%package data
Summary: data components for the gnome-initial-setup package.
Group: Data

%description data
data components for the gnome-initial-setup package.


%package libexec
Summary: libexec components for the gnome-initial-setup package.
Group: Default
Requires: gnome-initial-setup-license = %{version}-%{release}

%description libexec
libexec components for the gnome-initial-setup package.


%package license
Summary: license components for the gnome-initial-setup package.
Group: Default

%description license
license components for the gnome-initial-setup package.


%package locales
Summary: locales components for the gnome-initial-setup package.
Group: Default

%description locales
locales components for the gnome-initial-setup package.


%prep
%setup -q -n gnome-initial-setup-47.2
cd %{_builddir}/gnome-initial-setup-47.2
pushd ..
cp -a gnome-initial-setup-47.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1732298436
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dsystemd=false  builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dsystemd=false  builddiravx2
ninja -v -C builddiravx2

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-initial-setup
cp %{_builddir}/gnome-initial-setup-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gnome-initial-setup/4cc77b90af91e615a64ae04893fdffa7939db84c || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-initial-setup
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/applications/gnome-initial-setup.desktop
/usr/share/dconf/profile/gnome-initial-setup
/usr/share/gnome-initial-setup/initial-setup-dconf-defaults
/usr/share/gnome-session/sessions/gnome-initial-setup.session
/usr/share/gnome-shell/modes/initial-setup.json
/usr/share/polkit-1/rules.d/20-gnome-initial-setup.rules

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/gnome-initial-setup
/V3/usr/libexec/gnome-initial-setup-copy-worker
/usr/libexec/gnome-initial-setup
/usr/libexec/gnome-initial-setup-copy-worker

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-initial-setup/4cc77b90af91e615a64ae04893fdffa7939db84c

%files locales -f gnome-initial-setup.lang
%defattr(-,root,root,-)

