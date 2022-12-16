# RPM builder for Rust Web Server
You'll need to use Rust v1.65+.

1. Update [spec](SPECS/rws.spec) accordingly.
1. Download source tarball from Releases or Tags page.
1. Unpack and create new source tarball named as per 
[spec](SPECS/rws.spec) _name_-_version_.tar.gz with Cargo.toml 
at the directory root level.

To build execute:
> rpmbuild -v -bb --clean SPECS/rws.spec

Check RPM package at RPMS/x86_64 folder.

To install execute:
> sudo rpm -i --force rws-_YOUR_VERSION_.rpm

## Community
Use GitHub discussions, issues and pull requests.

There is Rust Web Server [Discord](https://discord.gg/zaErjtr5Dm) where you can ask questions and share ideas.

Follow the [Rust code of conduct](https://www.rust-lang.org/policies/code-of-conduct).

## Donations
If you appreciate my work and want to support it, feel free to do it via [PayPal](https://www.paypal.com/donate/?hosted_button_id=7J69SYZWSP6HJ).

## Links
1. [Rust Web Server](https://github.com/bohdaq/rust-web-server)
1. [http-to-https-letsencrypt](https://github.com/bohdaq/rust-http-to-https-letsencrypt-acme)
1. [Rust Web Framework](https://github.com/bohdaq/rust-web-framework/)
1. [Create Debian Package](https://github.com/bohdaq/rws-create-deb)
1. [Create RPM Package](https://github.com/bohdaq/rws-rpm-builder)
1. [Homebrew Formula](https://github.com/bohdaq/homebrew-rust-tls-server)
