Summary:	Applet that displays the weather
Summary(pl):	Aplet wy¶wietlaj±cy informacje o pogodzie
Name:		wmWeather
Version:	1.31
Release:	3
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://nis-www.lanl.gov/~mgh/WindowMaker/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://nis-www.lanl.gov/~mgh/WindowMaker/DockApps.shtml
Requires:	perl-modules
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6
%define 	_mandir 	%{_prefix}/man

%description
wmWeather is a WindowMaker dockapp that displays the current weather
conditions for a given location, in an easy to read icon.

%description -l pl
wmWeather jest dokowalnym apletem dla WindowMakera, wy¶wietlaj±cym
informacje o aktualnych warunkach atmosferycznych dla wybranego
miejsca.

%prep
%setup -q

%build
%{__make} -C Src \
        CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
        $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

install Src/%{name} $RPM_BUILD_ROOT%{_bindir}
install Src/GrabWeather $RPM_BUILD_ROOT%{_bindir}
install Src/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

#install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

gzip -9nf HINTS BUGS CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/GrabWeather
%{_mandir}/man1/*
#%{_applnkdir}/DockApplets/wmWeather.desktop
