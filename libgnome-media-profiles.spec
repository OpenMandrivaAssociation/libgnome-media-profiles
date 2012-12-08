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

BuildRequires: gnome-doc-utils-devel
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



%changelog
* Thu Mar 01 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.0.0-1
+ Revision: 781677
- added p0 upstream for fix format string errors
- fixed find_lang
- imported package libgnome-media-profiles


* Thu Jun 16 2011 dmorgan <dmorgan> 3.0.0-8.mga2
+ Revision: 108134
- Obsolete gnome-media-devel
- Add conflict to help upgrade

* Wed Jun 15 2011 dmorgan <dmorgan> 3.0.0-6.mga2
+ Revision: 107919
- Remove wrong obsoletes

* Wed Jun 15 2011 dmorgan <dmorgan> 3.0.0-5.mga2
+ Revision: 107890
- Provides gnome-media-devel

* Wed Jun 15 2011 dmorgan <dmorgan> 3.0.0-3.mga2
+ Revision: 107772
- Add more provides / Obsoletes

* Wed Jun 15 2011 dmorgan <dmorgan> 3.0.0-2.mga2
+ Revision: 107762
- Add obsoletes to ease upgrade
  Use rpm macros
- Fix copy/paste

* Wed Jun 15 2011 dmorgan <dmorgan> 3.0.0-1.mga2
+ Revision: 107280
- Add gstreamer as buildrequire
- imported package libgnome-media-profiles


* Mon Apr 04 2011 Bastien Nocera <bnocera@redhat.com> 3.0.0-1
- Update to 3.0.0

* Thu Feb 10 2011 Matthias Clasen <mclasen@redhat.com> 2.91.2-15
- Rebuild for newer gtk

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.91.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Feb 05 2011 Bastien Nocera <bnocera@redhat.com> 2.91.2-13
- Really rebuild against newer gtk

* Wed Feb  2 2011 Matthias Clasen <mclasen@redhat.com> 2.91.2-12
- Rebuild against newer gtk

* Fri Jan  7 2011 Matthias Clasen <mclasen@redhat.com> 2.91.2-11
- Rebuild against new gtk

* Fri Dec  3 2010 Matthias Clasen <mclasen@redhat.com> 2.91.2-10
- Rebuild against new gtk

* Mon Nov 15 2010 Bastien Nocera <bnocera@redhat.com> 2.91.2-9
- Add distro to release number for the obsoletes because RPM's
  comparisons suck

* Fri Nov 12 2010 Bastien Nocera <bnocera@redhat.com> 2.91.2-8
- Fix wrongly versioned provides

* Fri Nov 12 2010 Bastien Nocera <bnocera@redhat.com> 2.91.2-7
- Add obsoletes for gnome-media-libs as well

* Fri Nov 12 2010 Yanko Kaneti <yaneti@declera.com> 2.91.2-6
- --disable-scrollkeeper and not BR it

* Thu Nov 11 2010 Yanko Kaneti <yaneti@declera.com> 2.91.2-5
- Add gnome-media-devel provides to devel

* Thu Nov 11 2010 Yanko Kaneti <yaneti@declera.com> 2.91.2-4
- Add gnome-media-devel obsoletes to devel

* Thu Nov 11 2010 Yanko Kaneti <yaneti@declera.com> 2.91.2-3
- Shorten the devel description.

* Thu Nov 10 2010 Yanko Kaneti <yaneti@declera.com> 2.91.2-2
- Add some BRs so that it actually builds in mock.

* Thu Nov 10 2010 Yanko Kaneti <yaneti@declera.com> 2.91.2-1
- First attempt for review.

