Summary:	Applet that displays the weather.
Summary(pl):	Aplet wy¶wietlaj±cy informacje o pogodzie
Name:		wmWeather
Version:	1.31
Release:	2
Copyright:	GPL
Group:          X11/Window Managers/Tools
Group(pl):      X11/Zarz±dcy Okien/Narzêdzia
Source0: 	%{name}-%{version}.tar.gz
Source1:        wmWeather.desktop
BuildRequires:    XFree86-devel
BuildRequires:    xpm-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix	/usr/X11R6
%define _mandir %{_prefix}/man

%description 
wmWeather is a WindowMaker dockapp that displays the current 
weather conditions for a given location, in an easy to read icon.

%description -l pl
wmWeather jest dokowalnym apletem dla WindowMakera, wy¶wietlaj±cym 
informacje o aktualnych warunkach atmosferycznych dla wybranego miejsca.

%prep
%setup -q

%build
make -C Src \
        CFLAGS="$RPM_OPT_FLAGS -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
        $RPM_BUILD_ROOT/usr/X11R6/share/applnk/DockApplets

install -s Src/%{name} $RPM_BUILD_ROOT%{_bindir}
install Src/GrabWeather $RPM_BUILD_ROOT%{_bindir}
install Src/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT/usr/X11R6/share/applnk/DockApplets

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	HINTS BUGS CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {HINTS,BUGS,CHANGES}.gz
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/GrabWeather
%{_mandir}/man1/*
/usr/X11R6/share/applnk/DockApplets/wmWeather.desktop
