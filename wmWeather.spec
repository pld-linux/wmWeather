Summary:	Applet that displays the weather.
Summary(pl):	Aplet wy¶wietlaj±cy informacje o pogodzie
Name:		wmWeather
Version:	1.23
Release:	2
Copyright:	GPL
Group:          X11/Window Managers/Tools
Group(pl):      X11/Zarz±dcy Okien/Narzêdzia
Source0: 	%{name}-%{version}.tar.gz
Source1:        wmWeather.wmconfig
BuildPrereq:    XFree86-devel
BuildPrereq:    xpm-devel
Buildroot: 	/tmp/%{name}-%{version}-root

%description 
wmWeather is a WindowMaker dockapp that displays the current 
weather conditions for a given location, in an easy to read icon.

%description -l pl
wmWeather jest dokowalnym apletem dla WindowMakera, wy¶wietlaj±cym 
informacje o aktualnych warunkach atmosferycznych dla wybranego miejsca.

%prep
%setup -q

%build
make -C wmWeather clean
make -C wmWeather \
        CFLAGS="$RPM_OPT_FLAGS -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/X11/wmconfig,usr/X11R6/{bin,share/man/man1}}

install -s wmWeather/wmWeather $RPM_BUILD_ROOT/usr/X11R6/bin
install wmWeather/GrabWeather $RPM_BUILD_ROOT/usr/X11R6/bin
install wmWeather/wmWeather.1 $RPM_BUILD_ROOT/usr/X11R6/share/man/man1

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/wmWeather

gzip -9nf $RPM_BUILD_ROOT/usr/X11R6/share/man/man1/* \
	HINTS BUGS CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {HINTS,BUGS,CHANGES}.gz
%attr(755,root,root) /usr/X11R6/bin/wmWeather
%attr(755,root,root) /usr/X11R6/bin/GrabWeather
/usr/X11R6/share/man/man1/wmWeather.1.gz
/etc/X11/wmconfig/wmWeather

%changelog
* Mon May 10 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [1.23-2]
- modified spec file for PLD use,
- package is now FHS 2.0 compliant,

- based on spec file by Rod Cordova <rcordova@ethernet.org>.
