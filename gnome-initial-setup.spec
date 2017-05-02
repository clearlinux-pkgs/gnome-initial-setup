#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-initial-setup
Version  : 3.24.0
Release  : 3
URL      : http://ftp.gnome.org/pub/gnome/sources/gnome-initial-setup/3.24/gnome-initial-setup-3.24.0.tar.xz
Source0  : http://ftp.gnome.org/pub/gnome/sources/gnome-initial-setup/3.24/gnome-initial-setup-3.24.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: gnome-initial-setup-bin
Requires: gnome-initial-setup-data
Requires: gnome-initial-setup-locales
BuildRequires : e2fsprogs-dev
BuildRequires : gettext
BuildRequires : intltool
BuildRequires : krb5-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(accountsservice)
BuildRequires : pkgconfig(gdm)
BuildRequires : pkgconfig(geocode-glib-1.0)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gnome-desktop-3.0)
BuildRequires : pkgconfig(goa-1.0)
BuildRequires : pkgconfig(goa-backend-1.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(gweather-3.0)
BuildRequires : pkgconfig(ibus-1.0)
BuildRequires : pkgconfig(iso-codes)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libgeoclue-2.0)
BuildRequires : pkgconfig(libnm)
BuildRequires : pkgconfig(libnm-glib)
BuildRequires : pkgconfig(libnm-gtk)
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : pkgconfig(pwquality)
BuildRequires : pkgconfig(rest-0.7)
BuildRequires : pkgconfig(webkit2gtk-4.0)
Patch1: 0001-pages-Use-the-stateless-os-release-file-vendor-only.patch

%description
GNOME initial setup
===================
After acquiring or installing a new system there are a few essential things
to set up before use. gnome-initial-setup aims to provide a simple, easy,
and safe way to prepare a new system.

%package bin
Summary: bin components for the gnome-initial-setup package.
Group: Binaries
Requires: gnome-initial-setup-data

%description bin
bin components for the gnome-initial-setup package.


%package data
Summary: data components for the gnome-initial-setup package.
Group: Data

%description data
data components for the gnome-initial-setup package.


%package locales
Summary: locales components for the gnome-initial-setup package.
Group: Default

%description locales
locales components for the gnome-initial-setup package.


%prep
%setup -q -n gnome-initial-setup-3.24.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1493741734
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1493741734
rm -rf %{buildroot}
%make_install
%find_lang gnome-initial-setup

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/libexec/gnome-initial-setup
/usr/libexec/gnome-initial-setup-copy-worker
/usr/libexec/gnome-welcome-tour

%files data
%defattr(-,root,root,-)
/usr/share/gdm/greeter/applications/gnome-initial-setup.desktop
/usr/share/gdm/greeter/applications/setup-shell.desktop
/usr/share/gnome-session/sessions/gnome-initial-setup.session
/usr/share/gnome-shell/modes/initial-setup.json
/usr/share/polkit-1/rules.d/20-gnome-initial-setup.rules

%files locales -f gnome-initial-setup.lang
%defattr(-,root,root,-)

