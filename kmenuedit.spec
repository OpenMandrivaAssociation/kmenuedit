%define major 5
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)

Name: kmenuedit
Version: 5.4.1
Release: 2
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Summary: KDE Plasma 5 Menu Editor
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5DNSSD)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5KHtml)
BuildRequires: cmake(KF5Solid)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Xml)

%description
KDE Plasma 5 Menu Editor.

%prep
%setup -qn %{name}-%{plasmaver}
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/kmenuedit
%{_libdir}/libkdeinit5_kmenuedit.so
%{_datadir}/applications/org.kde.kmenuedit.desktop
%{_datadir}/icons/*/*/*/kmenuedit*
%{_datadir}/kmenuedit
%{_datadir}/kxmlgui5/kmenuedit
%doc %{_docdir}/HTML/*/kmenuedit
