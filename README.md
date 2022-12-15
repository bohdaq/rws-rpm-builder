# RPM builder for Rust Web Server
You'll need to use Rust v1.65+.


1. Download source tarball from Releases or Tags page.
1. Put source code tarball named as per [spec](SPECS/rws.spec) _name_-_version_.tar.gz
1. Update [spec](SPECS/rws.spec) accordingly.

To build execute:
> $ rpmbuild -v -bb --clean SPECS/rws.spec

Check RPM package at RPMS/x86_64 folder.