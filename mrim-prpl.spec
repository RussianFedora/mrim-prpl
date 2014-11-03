%define libdirpart lib
%ifarch x86_64
%define libdirpart lib64
%endif

Name:		    mrim-prpl
Version:	    0.2.0
Release:	    1%{?dist}
Summary:	    Mail.ru Aganet protocol plugin for Pidgin (libpurple)
Summary(ru):	плагин к Pidgin и libpurple реализующий протокол MMP(Mail.RU) 

Group:		    Applications/Communications
License:	    GPLv2
URL:		    http://code.google.com/p/mrim-prpl
Source0:        http://repo.elemc.name/sources/%{name}/%{name}-%{version}.tar.xz
Patch100:       http://repo.elemc.name/sources/mrim-prpl/mrim-prpl-0.2.0-cmake-lib64.patch
BuildRoot:	    %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	glib2-devel gtk2-devel cmake
BuildRequires:	libpurple-devel gettext
Requires:	    libpurple

%description
This is a Mail.ru Aganet protocol plugin for Pidgin (libpurple)

%description -l ru
prpl-ostin-mrim - это реализация протокола MMP (MailRu) для Pidgin и libpurple.

%prep
%setup

%patch100 -p1 -b .cmake-lib64

mkdir -p build

pushd build
%cmake ..
popd

%build
pushd build
make %{?_smp_mflags} LIBDIR=%{libdirpart}
popd

%install
rm -rf %{buildroot}
pushd build
make LIBDIR=%{libdirpart} DESTDIR=%{buildroot} install
popd

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING README TODO
%{_libdir}/purple-2/*.so
%{_datadir}/pixmaps/pidgin/protocols/*/mrim.png
%{_datadir}/locale/*

%changelog
* Mon Nov 03 2014 Alexei Panov <me AT elemc DOT name> 0.2.0-1
- Update to git version 0.2.0

* Sun Jul 14 2013 Alexei Panov <me AT elemc DOT name> 0.1.28-4
- Rebuild for Fedora 19

* Thu Apr  5 2012 Alexei Panov <me AT elemc DOT name> - 0.1.28-3
- fix require pidgin (remove it) and remove .R from release string

* Sat Jul 16 2011 Alexei Panov <elemc@atisserv.ru> - 0.1.28-2.R
- added gettext in BuildRequires
* Sat Jul 16 2011 Alexei Panov <elemc@atisserv.ru> - 0.1.28-1
- New version
* Thu Nov 18 2010 Alexei Panov <elemc@atisserv.ru> - 0.1.26-1
- Initial build
