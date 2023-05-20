%define major 5
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define git 20230520

Name: kmenuedit
Version:	5.240.0
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/kmenuedit/-/archive/master/kmenuedit-master.tar.bz2#/kmenuedit-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
%endif
Summary: KDE Plasma 6 Menu Editor
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6Sonnet)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Xml)

%description
KDE Plasma 6 Menu Editor.

%prep
%autosetup -p1 -n kmenuedit-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang kmenuedit --with-html

%files -f kmenuedit.lang
%{_datadir}/qlogging-categories6/kmenuedit.categories
%{_bindir}/kmenuedit
%{_datadir}/applications/org.kde.kmenuedit.desktop
%{_datadir}/icons/*/*/*/kmenuedit*
%{_datadir}/kmenuedit
%{_datadir}/kxmlgui6/kmenuedit
%{_libdir}/kconf_update_bin/kmenuedit_globalaccel
%{_datadir}/metainfo/org.kde.kmenuedit.appdata.xml
