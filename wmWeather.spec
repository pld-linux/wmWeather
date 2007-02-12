Summary:	Applet that displays the weather
Summary(pl.UTF-8):   Aplet wyświetlający informacje o pogodzie
Name:		wmWeather
Version:	1.31
Release:	5
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://nis-www.lanl.gov/~mgh/WindowMaker/%{name}-%{version}.tar.gz
# Source0-md5:	f04693aa86d22099162cff3d0b5c9275
Source1:	%{name}.desktop
URL:		http://nis-www.lanl.gov/~mgh/WindowMaker/DockApps.shtml
Requires:	perl-modules
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
wmWeather is a WindowMaker dockapp that displays the current weather
conditions for a given location, in an easy to read icon.

%description -l pl.UTF-8
wmWeather jest dokowalnym apletem dla WindowMakera, wyświetlającym
informacje o aktualnych warunkach atmosferycznych dla wybranego
miejsca.

%prep
%setup -q

%build
%{__make} -C Src \
	CFLAGS="%{rpmcflags} -Wall" \
	LIBDIR="-L/usr/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_desktopdir}/docklets

install Src/%{name} $RPM_BUILD_ROOT%{_bindir}
install Src/GrabWeather $RPM_BUILD_ROOT%{_bindir}
install Src/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HINTS BUGS CHANGES
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/GrabWeather
%{_mandir}/man1/*
%{_desktopdir}/docklets/wmWeather.desktop
