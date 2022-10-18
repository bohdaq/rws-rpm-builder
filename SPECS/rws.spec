%define _topdir    /home/bohdaq/rws-rpm-builder
%define name       rws
%define release    0
%define version    0.0.28
%define buildroot  %{_topdir}/%{name}-%{version}-root

BuildRoot:         %{buildroot}
Summary:           Rust Web Server
License:           MIT
Name:              %{name}
Version:           %{version}
Release:           %{release}
Source:            %{name}-%{version}.tar.gz
Prefix:            /usr
Group:             Development/Tools

%description
rust-web-server (rws) is a simple web-server written in Rust. The rws server can serve static content inside the directory it is started.

%prep
%setup -q

%build
cargo test

%install
rustup override set nightly
cargo build -Zunstable-options --release  --out-dir $RPM_BUILD_ROOT/usr/local/bin

%files
%defattr(-, root, root)
/usr/local/bin/rws

