Summary:	Applet that displays the weather
Summary(pl.UTF-8):	Aplet wyświetlający informacje o pogodzie
Name:		wmWeather
Version:	1.31
Release:	6
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://nis-www.lanl.gov/~mgh/WindowMaker/%{name}-%{version}.tar.gz
# Source0-md5:	f04693aa86d22099162cff3d0b5c9275
Source1:	%{name}.desktop
Patch0:		%{name}-Makefile.patch
URL:		http://nis-www.lanl.gov/~mgh/WindowMaker/DockApps.shtml
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXpm-devel
Requires:	perl-modules
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
%patch0 -p1

%build
%{__make} -C Src \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/docklets

%{__make} -C Src install \
	DESTDIR="$RPM_BUILD_ROOT"

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
