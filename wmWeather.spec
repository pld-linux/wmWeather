%define name wmWeather
%define version 1.23
%define release 1

%define builddir $RPM_BUILD_DIR/%{name}-%{version}

Summary: Applet that displays the weather.

Name: %{name}
Version: %{version}
Release: %{release}
Group: X11/Utilities
Copyright: GPL
Packager: Rod Cordova <rcordova@ethernet.org>
Source0: %{name}-%{version}.tar.gz
Buildroot: /tmp/%{name}-%{version}-%{release}-root

%changelog


%description 
wmWeather is a WindowMaker dockapp that displays the current 
weather conditions for a given location, in an easy to read icon.

%prep

%setup

%build
cd $RPM_BUILD_DIR/%{name}-%{version}/%{name}
make

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT ; fi
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin $RPM_BUILD_ROOT/usr/X11R6/man/man1
strip %{builddir}/wmWeather/wmWeather
cp %{builddir}/%{name}/wmWeather $RPM_BUILD_ROOT/usr/X11R6/bin
cp %{builddir}/%{name}/GrabWeather $RPM_BUILD_ROOT/usr/X11R6/bin
cp %{builddir}/%{name}/wmWeather.1 $RPM_BUILD_ROOT/usr/X11R6/man/man1/wmWeather.1

%files
%doc HINTS BUGS CHANGES COPYING
%attr(755,root,root) /usr/X11R6/bin/wmWeather
%attr(755,root,root) /usr/X11R6/bin/GrabWeather
%attr(644,root,root) /usr/X11R6/man/man1/wmWeather.1

%clean
rm -r $RPM_BUILD_ROOT
rm -r %{builddir}
