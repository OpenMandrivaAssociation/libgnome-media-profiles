%define Werror_cflags %nil

%define major 0
%define libname %mklibname gnome-media-profiles %major

%define develname %mklibname -d gnome-media-profiles

%define oldlib    %mklibname gnome-media 0
%define olddevel  %mklibname -d gnome-media

%define schemas gnome-media-profiles

Name:           libgnome-media-profiles
Version:        3.0.0
Release:        %mkrel 8
Summary:        GNOME Media Profiles library

Group:          Graphical desktop/GNOME 
License:        LGPLv2+
URL:            http://git.gnome.org/browse/libgnome-media-profiles
Source0:        http://download.gnome.org/sources/%{name}/3.0/%{name}-%{version}.tar.bz2

BuildRequires: gtk+3-devel >= 2.99.0
BuildRequires: libGConf2-devel glib2-devel
BuildRequires: intltool
BuildRequires: gnome-doc-utils
BuildRequires: gstreamer0.10-devel

Conflicts:     gnome-media < 2.91.2

Requires(pre): GConf2
Requires(post): GConf2
Requires(preun): GConf2

%description
The GNOME Media Profiles library provides prebuilt GStreamer pipelines
for applications aiming to support different sound formats.

%preun
%preun_uninstall_gconf_schemas %{schemas}

%files -f libgnome-media-profiles.lang -f gnome-audio-profiles.lang
%defattr(-,root,root,-)
%doc COPYING README
%{_bindir}/gnome-audio-profiles-properties
%{_sysconfdir}/gconf/schemas/gnome-media-profiles.schemas
%{_datadir}/libgnome-media-profiles
%{_datadir}/omf/gnome-audio-profiles/

#--------------------------------------------------------------------

%package -n %{libname}
Summary:        Library for the %name
Group:          System/Libraries

%description -n %{libname}
Library for the %name

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/libgnome-media-profiles-3.0.so.%{major}*

#--------------------------------------------------------------------

%package        -n %develname
Summary:        Development files for %{name}
Group:          Development/GNOME and GTK+ 
Requires:       %{name} = %{version}-%{release}
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Obsoletes:      %{olddevel} < %{version}-%{release}

%description    -n %develname
The %{name}-devel package contains libraries and header files
for developing applications that use %{name}.

%files -n %develname
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libgnome-media-profiles-3.0.pc

#--------------------------------------------------------------------

%prep
%setup -q


%build
%configure --disable-static --disable-schemas-install --disable-scrollkeeper
%make


%install
%makeinstall_std
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%find_lang libgnome-media-profiles
%find_lang gnome-audio-profiles --with-gnome



