#
# spec file for package libopenshot-audio
#
# Copyright (c) 2020 UnitedRPMs.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://goo.gl/zqFJft
#

# 
%define _legacy_common_support 1

Name:           libopenshot-audio
Version:        0.2.0
Release:        7%{?dist}
Summary:        Audio library used by OpenShot

License:        GPLv3+
URL:            http://openshot.org/
Source0:  	https://github.com/OpenShot/%{name}/archive/22d5bec9b50e35682bd943e87690076c0682d86d.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake 
BuildRequires:	make
BuildRequires:  freetype-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  libX11-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXrandr-devel
BuildRequires:  gcc-c++

%description
OpenShot Audio Library (libopenshot-audio) is an open-source 
project powered by JUCE, and enables high-quality audio editing 
and playback for libopenshot.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-b28b4375ae61745af72341ccfae1358dd9c485ce -p1


%build
%cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed" .
make %{?_smp_mflags}


%install

%make_install


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS COPYING README.md
%{_libdir}/*.so.*

%files devel
%doc
%{_bindir}/openshot-audio-test-sound
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man1/*.1*


%changelog

* Wed Mar 11 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.2.0-7
- Updated to 0.2.0

* Mon Feb 10 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.1.9-7
- Updated to 0.1.9

* Wed Apr 10 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.1.8-7
- Updated to 0.1.8

* Thu Sep 20 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.1.7-1
- Updated to 0.1.7-1

* Sat Jun 30 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.1.6-1
- Updated to 0.1.6-1

* Thu Nov 16 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.1.5-1
- Updated to 0.1.5-1

* Thu May 25 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.1.4-1
- Updated to 0.1.4-1

* Wed Aug 31 2016 Pavlo Rudyi <paulcarroty at riseup.net> - 0.1.2-1
- Update to 0.1.2
- Change the source URL

* Fri Jul 08 2016 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.1.1-2
- Massive rebuild

* Fri Apr  8 2016 Richard Shaw <hobbes1069@gmail.com> - 0.1.1-1
- Update to latest upstream release.

* Mon Nov 16 2015 Richard Shaw <hobbes1069@gmail.com> - 0.0.6-1
- Update to latest upstream release.

* Thu Jun 25 2015 Sérgio Basto <sergio@serjux.com> - 0.0.4-2
- Fixed unused-direct-shlib-dependency in cmake with global optflags.

* Mon May 18 2015 Hans de Goede <j.w.r.degoede@gmail.com> - 0.0.4-1
- New upstream release 0.0.4

* Tue Jul 15 2014 Richard Shaw <hobbes1069@gmail.com> - 0.0.3-1
- Initial packaging.
