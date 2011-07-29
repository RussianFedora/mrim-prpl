%define libdirpart lib
%ifarch x86_64
%define libdirpart lib64
%endif

Name:		mrim-prpl
Version:	0.1.28
Release:	2%{?dist}.R
Summary:	Mail.ru Aganet protocol plugin for Pidgin (libpurple)
Summary(ru):	плагин к Pidgin и libpurple реализующий протокол MMP(Mail.RU) 

Group:		Applications/Communications
License:	GPLv2
URL:		http://code.google.com/p/mrim-prpl
Source0:	http://mrim-prpl.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	glib2-devel gtk2-devel
BuildRequires:	libpurple-devel gettext
Requires:	pidgin
Requires:	libpurple

%description
This is a Mail.ru Aganet protocol plugin for Pidgin (libpurple)

%description -l ru
prpl-ostin-mrim - это реализация протокола MMP (MailRu) для Pidgin и libpurple.

%prep
%setup
./configure --gtk

%build
make %{?_smp_mflags} LIBDIR=%{libdirpart}

%install
rm -rf %{buildroot}
make LIBDIR=%{libdirpart} DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog LICENSE README TODO
%{_libdir}/purple-2/*.so
%{_datadir}/pixmaps/pidgin/protocols/*/mrim.png
%{_datadir}/locale/*

%changelog
* Sat Jul 16 2011 Alexei Panov <elemc@atisserv.ru> - 0.1.28-2.R
- added gettext in BuildRequires
* Sat Jul 16 2011 Alexei Panov <elemc@atisserv.ru> - 0.1.28-1
- New version
* Thu Nov 18 2010 Alexei Panov <elemc@atisserv.ru> - 0.1.26-1
- Initial build
