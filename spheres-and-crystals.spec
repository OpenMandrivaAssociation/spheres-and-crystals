Name: 		spheres-and-crystals
Version: 0.7
Release:9
Summary: 	Spheres and Crystals SVG theme
Group: 		Graphical desktop/GNOME
License: 	LGPL
URL:		https://librsvg.sf.net
Source: 	http://librsvg.sf.net/releases/%{version}/src/%{name}-%{version}.tar.bz2
BuildArch: noarch
Requires:	librsvg >= 2.2.2
BuildRequires: 	pkgconfig(gdk-2.0)
BuildRequires: 	pkgconfig(librsvg-2.0) >= 2.2.2
BuildRequires: 	pkgconfig(libart-2.0) >= 2.1.3

%description
Spheres and Crystals is a meta-theme for GNOME. It is meant to show the
possibilities for using SVG icons all over in GNOME.

%prep
%setup -q

%build
export CFLAGS="%optflags"
./configure --prefix=%_prefix --libdir=%_libdir
%make

%install  
%makeinstall_std
touch %buildroot%_datadir/icons/SphereCrystal/icon-theme.cache

%post
%update_icon_cache SphereCrystal
%postun
%clean_icon_cache SphereCrystal

%files
%doc AUTHORS README TODO ChangeLog
%{_datadir}/themes/SphereCrystal/
%dir %{_datadir}/icons/SphereCrystal/
%{_iconsdir}/SphereCrystal/scalable/*/*
%{_datadir}/icons/SphereCrystal/index.theme
%ghost %_datadir/icons/SphereCrystal/icon-theme.cache
%dir %{_datadir}/backgrounds/
%dir %{_datadir}/backgrounds/scalable/
%{_datadir}/backgrounds/scalable/tiger.svg


