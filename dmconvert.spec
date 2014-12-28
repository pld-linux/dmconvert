Summary:	dmconvert converts unencrypted filesystem to an encrypted one
Summary(pl.UTF-8):	Narzędzie do konwersji nieszyfrowanego systemu plików na szyfrowany
Name:		dmconvert
Version:	0.2
Release:	3
Epoch:		0
License:	GPL v2
Group:		Applications/System
Source0:	http://www.saout.de/misc/dm-crypt/%{name}-%{version}.tar.bz2
# Source0-md5:	0ce3b6c39d4f7cac664feb17d7b57ccd
URL:		http://www.saout.de/misc/dm-crypt/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	device-mapper-devel >= 1.01.01
BuildRequires:	gettext-tools
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dmconvert converts unencrypted filesystem to an encrypted one using
device-mapper. It can work on mounted device.

%description -l pl.UTF-8
Narzędzie do konwersji nieszyfrowanego systemu plików na szyfrowany.
Używa device-mappera i może pracować na zamontowanym urządzeniu.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	MKINSTALLDIRS='/usr/share/automake/mkinstalldirs' \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
