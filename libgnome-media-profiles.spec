#define Werror_cflags %nil

%define api 3.0
%define major 0
%define libname %mklibname gnome-media-profiles %{api} %{major}
%define develname %mklibname -d gnome-media-profiles

Name:           libgnome-media-profiles
Version:        3.0.0
Release:        1
Summary:        GNOME Media Profiles library
Group:          Graphical desktop/GNOME 
License:        LGPLv2+
URL:            http://git.gnome.org/browse/libgnome-media-profiles
Source0:        http://download.gnome.org/sources/%{name}/3.0/%{name}-%{version}.tar.bz2
# upstream 	1451acdacb11fdc2eb23fce10a9affa844f9527c
Patch0:			libgnome-media-profiles-3.0.0_fix_format_string.patch

BuildRequires: gnome-doc-utils
BuildRequires: intltool
BuildRequires: pkgconfig(gconf-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires: pkgconfig(gtk+-3.0)
Conflicts:     gnome-media < 2.91.2
Requires(pre,post,preun): GConf2

%description
The GNOME Media Profiles library provides prebuilt GStreamer pipelines
for applications aiming to support different sound formats.

%package -n %{libname}
Summary:	Library for the %{name}
Group:          System/Libraries

%description -n %{libname}
Library for the %{name}

%package -n	%{develname}
Summary:        Development files for %{name}
Group:          Development/GNOME and GTK+ 
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
%rename			%{_lib}gnome-media-devel

%description -n %{develname}
The %{name}-devel package contains libraries and header files
for developing applications that use %{name}.

%prep
%setup -q
%apply_patches
autoreconf

%build
%configure \
	--disable-static \
	--disable-schemas-install \
	--disable-scrollkeeper
%make

%install
%makeinstall_std
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%find_lang libgnome-media-profiles gnome-audio-profiles --with-gnome libgnome-media-profiles.lang

%files -f libgnome-media-profiles.lang
%doc COPYING README
%{_bindir}/gnome-audio-profiles-properties
%{_sysconfdir}/gconf/schemas/gnome-media-profiles.schemas
%{_datadir}/libgnome-media-profiles

%files -n %{libname}
%{_libdir}/libgnome-media-profiles-%{api}.so.%{major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

