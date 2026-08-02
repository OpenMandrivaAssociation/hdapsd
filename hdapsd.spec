Summary:	HDAPS (Hard Disk Active Protection System) daemon
Name:		hdapsd
Version:	20250908
Release:	1
License:	GPLv2+
Group:		System/Kernel and hardware
URL:		https://github.com/linux-thinkpad/hdapsd
Source0:	https://github.com/linux-thinkpad/hdapsd/releases/download/%{version}/hdapsd-%{version}.tar.gz
Source1:	hdapsd.event
Source2:	hdapsd.sysconfig
Source3:	99-hdapsd.rules
Patch0:		hdaps-20090401-fix-str-fmt.patch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
%description
hdapsd is a daemon that reads from the HDAPS (Hard Disk Active Protection
System) driver and protects the hard disk from sudden movements that may
harm it.

%prep
%setup -q -n %{name}-%{version}
%patch -P 0 -p1

%build
%configure2_5x
%make

%install
%makeinstall

mkdir -p %{buildroot}%{_sysconfdir}/event.d/
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig/
mkdir -p %{buildroot}%{_sysconfdir}/udev/rules.d/
cp -p %SOURCE1 %{buildroot}%{_sysconfdir}/event.d/hdapsd
cp -p %SOURCE2 %{buildroot}%{_sysconfdir}/sysconfig/hdapsd
cp -p %SOURCE3 %{buildroot}%{_sysconfdir}/udev/rules.d/
# remove docs installed by "make install", will be installed in proper dir by %doc
rm -rf %{buildroot}%{_defaultdocdir}/%{name}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_sbindir}/*
%config(noreplace) %{_sysconfdir}/udev/rules.d/*
%config(noreplace) %{_sysconfdir}/event.d/hdapsd
%config(noreplace) %{_sysconfdir}/sysconfig/hdapsd
%{_mandir}/man8/hdapsd.8.*
%doc AUTHORS
%doc COPYING
%doc ChangeLog
%doc README
