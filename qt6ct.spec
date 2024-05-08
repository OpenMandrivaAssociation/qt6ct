Name:           qt6ct
Version:        0.9
Release:        1
Summary:        Qt6 Configuration Tool
License:        BSD-2-Clause
Group:          System/GUI/Other
URL:            https://github.com/trialuser02/qt6ct
Source:         https://github.com/trialuser02/qt6ct/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  qt6-qtsvg

Requires:  qt6-qtsvg

%description
This program allows users to configure Qt6 settings (theme, font, icons, etc.)
under DE/WM without Qt integration.

%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/colors
%dir %{_datadir}/%{name}/qss
%{_datadir}/%{name}/colors/*.conf
%{_datadir}/%{name}/qss/*.qss
%dir %{_qt6_pluginsdir}/platformthemes
%dir %{_qt6_pluginsdir}/styles
%{_qt6_pluginsdir}/platformthemes/lib%{name}.so
%{_qt6_pluginsdir}/styles/lib%{name}-style.so
%{_libdir}/libqt6ct-common.so*
