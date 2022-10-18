# RPM builder for Rust Web Server
You'll need to install rustup nightly:
> $ rustup toolchain install nightly

To build execute:
> $ rpmbuild -v -bb --clean SPECS/rws.spec
