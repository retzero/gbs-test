Name:           alsa-utils
Version:        1.0.29
Release:        1
License:        GPL-2.0
Summary:        Advanced Linux Sound Architecture (ALSA) utilities
Url:            http://www.alsa-project.org/
Group:          Applications/Multimedia
Source0:        ftp://ftp.alsa-project.org/pub/utils/%{name}-%{version}.tar.bz2
Source1001:     alsa-utils.manifest
BuildRequires:  libasound-devel

%description
This package contains command line utilities for the Advanced Linux Sound
Architecture (ALSA).

%package doc
Summary:        Man pages for alsa-utils
Group:          Documentation
Requires:       %{name} = %{version}

%description doc
Man pages for alsa-utils

%prep
%setup -q
cp %{SOURCE1001} .


%build
export CFLAGS+=" -fPIC -pie"

%configure \
    --disable-static \
    --disable-nls \
    --disable-xmlto \
    --disable-alsamixer \
    --disable-alsatest \
    --with-udev-rules-dir=/lib/udev/rules.d

%__make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}/var/lib/alsa
%if "%{tizen_profile_name}" == "tv"
rm -rf %{buildroot}%{_bindir}/speaker-test
%endif

%remove_docs

%files
%manifest %{name}.manifest
%license COPYING
%{_bindir}/*
%{_sbindir}/*
%exclude %{_sbindir}/alsaconf
%exclude %{_sbindir}/alsa-info.sh
%{_datadir}/alsa/*
%{_datadir}/sounds/*
/lib/udev/rules.d/90-alsa-restore.rules
