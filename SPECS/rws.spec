%define _topdir    /home/bohdan_tsap/git/rws-rpm-builder
%define name       rws
%define release    0
%define version    9.0.0
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
rust-web-server (rws) is a simple web-server written in Rust.

%global debug_package %{nil}

%prep
%setup -q

%build
cargo test

%install
rustup override set nightly
cargo build -Zunstable-options --release  --out-dir $RPM_BUILD_ROOT/usr/bin

%files
%defattr(-, root, root)
/usr/bin/rws

