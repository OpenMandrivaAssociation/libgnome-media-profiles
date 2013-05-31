%define url_ver %(echo %{version}|cut -d. -f1,2)

%define gstapi	1.0
%define api	3.0
%define major	0
%define libname	%mklibname gnome-media-profiles %{api} %{major}
%define devname	%mklibname -d gnome-media-profiles

Summary:        GNOME Media Profiles library
Name:           libgnome-media-profiles
Version:        3.0.0
Release:        2
Group:          Graphical desktop/GNOME 
License:        LGPLv2+
Url:            http://git.gnome.org/browse/libgnome-media-profiles
Source0:        http://ftp.gnome.org/pub/GNOME/sources/libgnome-media-profiles/%{url_ver}/%{name}-%{version}.tar.bz2
# upstream 	1451acdacb11fdc2eb23fce10a9affa844f9527c
Patch0:		libgnome-media-profiles-3.0.0_fix_format_string.patch
# from ubuntu
Patch1:		02-gstreamer-1.0.patch

BuildRequires: intltool
BuildRequires: pkgconfig(gconf-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gnome-doc-utils)
BuildRequires: pkgconfig(gstreamer-plugins-base-%{gstapi})
BuildRequires: pkgconfig(gtk+-3.0)
Requires(pre,post,preun): GConf2
Conflicts:     gnome-media < 2.91.2

%description
The GNOME Media Profiles library provides prebuilt GStreamer pipelines
for applications aiming to support different sound formats.

%package -n %{libname}
Summary:	Library for the %{name}
Group:          System/Libraries

%description -n %{libname}
Library for the %{name}

%package -n	%{devname}
Summary:        Development files for %{name}
Group:          Development/GNOME and GTK+ 
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
%rename		%{_lib}gnome-media-devel

%description -n %{devname}
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

%find_lang libgnome-media-profiles gnome-audio-profiles --with-gnome libgnome-media-profiles.lang

%files -f libgnome-media-profiles.lang
%doc COPYING README
%{_bindir}/gnome-audio-profiles-properties
%{_sysconfdir}/gconf/schemas/gnome-media-profiles.schemas
%{_datadir}/libgnome-media-profiles

%files -n %{libname}
%{_libdir}/libgnome-media-profiles-%{api}.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

