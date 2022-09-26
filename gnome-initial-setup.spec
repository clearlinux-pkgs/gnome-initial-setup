#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-initial-setup
Version  : 43.0
Release  : 59
URL      : https://download.gnome.org/sources/gnome-initial-setup/43/gnome-initial-setup-43.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-initial-setup/43/gnome-initial-setup-43.0.tar.xz
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
BuildRequires : pkgconfig(libadwaita-1)
BuildRequires : pkgconfig(libgeoclue-2.0)
BuildRequires : pkgconfig(libnm)
BuildRequires : pkgconfig(libnma-gtk4)
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : pkgconfig(pwquality)
BuildRequires : pkgconfig(rest-0.7)
BuildRequires : pkgconfig(rest-1.0)
BuildRequires : pkgconfig(webkit2gtk-5.0)
BuildRequires : polkit-dev

%description
GNOME Initial Setup
===================
After acquiring or installing a new system there are a few essential things
to set up before use. gnome-initial-setup aims to provide a simple, easy,
and safe way to prepare a new system.

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
%setup -q -n gnome-initial-setup-43.0
cd %{_builddir}/gnome-initial-setup-43.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664148876
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dsystemd=false  builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-initial-setup
cp %{_builddir}/gnome-initial-setup-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gnome-initial-setup/4cc77b90af91e615a64ae04893fdffa7939db84c || :
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-initial-setup

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/applications/gnome-initial-setup.desktop
/usr/share/gnome-session/sessions/gnome-initial-setup.session
/usr/share/gnome-shell/modes/initial-setup.json
/usr/share/polkit-1/rules.d/20-gnome-initial-setup.rules

%files libexec
%defattr(-,root,root,-)
/usr/libexec/gnome-initial-setup
/usr/libexec/gnome-initial-setup-copy-worker
/usr/libexec/gnome-initial-setup-goa-helper

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-initial-setup/4cc77b90af91e615a64ae04893fdffa7939db84c

%files locales -f gnome-initial-setup.lang
%defattr(-,root,root,-)

