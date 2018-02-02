#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC9D50845DE5519CB (arzhan@kinzhalin.com)
#
Name     : clrtrust
Version  : 0.0.6
Release  : 11
URL      : https://github.com/clearlinux/clrtrust/releases/download/v0.0.6/clrtrust-0.0.6.tar.gz
Source0  : https://github.com/clearlinux/clrtrust/releases/download/v0.0.6/clrtrust-0.0.6.tar.gz
Source99 : https://github.com/clearlinux/clrtrust/releases/download/v0.0.6/clrtrust-0.0.6.tar.gz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: clrtrust-bin
Requires: openssl
Requires: p11-kit
BuildRequires : bats
BuildRequires : openssl
BuildRequires : p11-kit

%description
# clrtrust: the Clear Trust Store Management tool
Clear Linux\* for IntelÂ® Architecture implements a centralized TLS Trust Store
for all its packages which use Transport Layer Security. The trust store
contains a set of trusted Root Certificate Authorities (CAs) which Clear Linux\*
should trust. `clrtrust` tool provides a front-end for the trust store
management: it allows viewing, adding (trusting), removing (distrusting) CAs. It
also provides some maitenance commands such as re-generating the trust store and
checking its consistency.

%package bin
Summary: bin components for the clrtrust package.
Group: Binaries

%description bin
bin components for the clrtrust package.


%prep
%setup -q -n clrtrust-0.0.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1514312344
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check

%install
export SOURCE_DATE_EPOCH=1514312344
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/clrtrust
