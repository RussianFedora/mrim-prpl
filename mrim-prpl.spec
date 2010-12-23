%define libdirpart lib
%ifarch x86_64
%define libdirpart lib64
%endif

Name:		mrim-prpl
Version:	0.1.26
Release:	1%{?dist}
Summary:	Mail.ru Aganet protocol plugin for Pidgin (libpurple)
Summary(ru):	плагин к Pidgin и libpurple реализующий протокол MMP(Mail.RU) 

Group:		Applications/Communications
License:	GPLv2
URL:		http://code.google.com/p/mrim-prpl
Source0:	http://mrim-prpl.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	glib2-devel
BuildRequires:	libpurple-devel
Requires:	pidgin
Requires:	libpurple

%description
This is a Mail.ru Aganet protocol plugin for Pidgin (libpurple)

%description -l ru
prpl-ostin-mrim - это реализация протокола MMP (MailRu) для Pidgin и libpurple.

%prep
%setup -q -n %{name}
chmod 0644 *.c *.h pixmaps/*.png
chmod 0644 ChangeLog LICENSE Makefile README TODO

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


%changelog
* Thu Nov 18 2010 Alexei Panov <elemc@atisserv.ru> - 0.1.26-1
- Initial build