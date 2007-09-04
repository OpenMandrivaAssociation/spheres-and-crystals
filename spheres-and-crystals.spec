Name: 		spheres-and-crystals
Version: 0.7
Release: %mkrel 6
Summary: 	Spheres and Crystals SVG theme
Group: 		Graphical desktop/GNOME
License: 	LGPL
URL:		http://librsvg.sf.net
Source: 	http://librsvg.sf.net/releases/%{version}/src/%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-%{version}-root
BuildArch: noarch
Requires:	librsvg >= 2.2.2
BuildRequires: 	libgtk+2.0-devel 
BuildRequires: 	librsvg-devel >= 2.2.2
BuildRequires:  libart_lgpl-devel >= 2.1.3

%description

Spheres and Crystals is a metatheme for GNOME. It is meant to show the
possibilities for using SVG icons all over in GNOME.

%prep
%setup -q

%build
export CFLAGS="%optflags"
./configure --prefix=%_prefix --libdir=%_libdir
%make

%install  
rm -rf %buildroot
%makeinstall_std
touch %buildroot%_datadir/icons/SphereCrystal/icon-theme.cache

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache SphereCrystal
%postun
%clean_icon_cache SphereCrystal


%files
%defattr(-, root, root)
%doc AUTHORS README TODO ChangeLog
%{_datadir}/themes/SphereCrystal/
%dir %{_datadir}/icons/SphereCrystal/
%{_datadir}/icons/SphereCrystal/*/
%{_datadir}/icons/SphereCrystal/index.theme
%ghost %_datadir/icons/SphereCrystal/icon-theme.cache
%dir %{_datadir}/backgrounds/
%dir %{_datadir}/backgrounds/scalable/
%{_datadir}/backgrounds/scalable/tiger.svg
