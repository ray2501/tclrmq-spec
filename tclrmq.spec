%{!?directory:%define directory /usr}

%define buildroot %{_tmppath}/%{name}

Name:          tclrmq
Summary:       Pure Tcl Library for RabbitMQ
Version:       1.4.6
Release:       0
License:       BSD-3-Clause
Group:         Development/Libraries/Tcl
Source:        %{name}-%{version}.tar.gz
URL:           https://github.com/flightaware/tclrmq
BuildRequires: make
BuildRequires: tcl >= 8.6
Requires:      tcl >= 8.6
BuildRoot:     %{buildroot}

%description
Pure TCL RabbitMQ Library implementing AMQP 0.9.1

This library is completely asynchronous and makes no blocking calls.
It relies on TclOO and requires Tcl 8.6, 
but has no other dependencies (other than a RabbitMQ server).

%prep
%setup -q -n %{name}-%{version}

%build

%install
make PACKAGELIBDIR=%{buildroot}%tcl_noarchdir/%{name}%{version} install

%clean
rm -rf %buildroot

%files
%doc LICENSE README.md
%defattr(-,root,root)
%tcl_noarchdir/%{name}%{version}

%changelog

