Name:       xorg-macros
Version:    1.20.1
Release:    1%{?dist}
Summary:    GNU autoconf macros shared across X.Org projects
License:    MIT
URL:        https://gitlab.freedesktop.org/xorg/util/macros
Source0:    %{name}-%{version}.tar.bz2
BuildArch:  noarch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make

%description
Base package for %{name}.

%package devel
Summary:    GNU autoconf macros shared across X.Org projects

%description devel
This is a set of autoconf macros used by the configure.ac scripts in
other Xorg modular packages, and is needed to generate new versions
of their configure scripts with autoconf.

%prep
%autosetup -n %{name}-%{version}/upstream

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

%files devel
%license COPYING
%{_datadir}/aclocal/%{name}.m4
%{_datadir}/pkgconfig/%{name}.pc
%{_datadir}/util-macros/INSTALL
