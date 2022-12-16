# RPM builder for Rust Web Server
You'll need to install rustup nightly:
> rustup toolchain install nightly

Steps to build:
- Update rust toolchain
> rustup update
- Update [spec](SPECS/rws.spec) accordingly to requirements
- Download source tarball from Releases or Tags page
- Unpack source tarball
> tar -xvf rust-web-server-_version_.tar.gz
- Rename folder
> mv rust-web-server-_version_ rws-_version_
- Create new source tarball
> tar -czvf rws-_version_.tar.gz rws-_version_/
- Copy created tarball to SOURCES folder
> cp rws-_version_.tar.gz _path-to-sources_/SOURCES/

To build execute:
> rpmbuild -v -bb --clean SPECS/rws.spec

Check RPM package at RPMS/x86_64 folder.

To install execute:
> sudo rpm -i --force rws-_YOUR_VERSION_.rpm

To check installation:
> rws

Note: you may build almost any rust project by updating 
spec like this. As an example this template is used for 
building Rust TLS Server.

## Community
Use GitHub discussions, issues and pull requests.

There is Rust Web Server [Discord](https://discord.gg/zaErjtr5Dm) where you can ask questions and share ideas.

Follow the [Rust code of conduct](https://www.rust-lang.org/policies/code-of-conduct).

## Donations
If you appreciate my work and want to support it, feel free to do it via [PayPal](https://www.paypal.com/donate/?hosted_button_id=7J69SYZWSP6HJ).

## Links
1. [Rust Web Server](https://github.com/bohdaq/rust-web-server)
1. [Rust TLS Server](https://github.com/bohdaq/rust-tls-server)
1. [http-to-https-letsencrypt](https://github.com/bohdaq/rust-http-to-https-letsencrypt-acme)
1. [Rust Web Framework](https://github.com/bohdaq/rust-web-framework/)
1. [Create Debian Package](https://github.com/bohdaq/rws-create-deb)
1. [Homebrew Formula Rust TLS Server](https://github.com/bohdaq/homebrew-rust-tls-server)
1. [Homebrew Formula Rust Web Server](https://github.com/bohdaq/homebrew-rust-web-server)
