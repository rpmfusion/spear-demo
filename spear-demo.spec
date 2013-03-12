Name:           spear-demo
Version:        1
Release:        3%{?dist}
Summary:        Spear of Destiny Demo
Group:          Amusements/Games
License:        Distributable
URL:            http://www.idsoftware.com/games/wolfenstein/spear/
Source0:        ftp://ftp.padua.org/pub/msdos/dos/games/local/soddemo.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       wolf4sdl-spear-demo

%description
This package contains the demo of id Software's first-person shooter
Wolfenstein 3D: Spear of Destiny.

%prep
%setup -q -c -T
unzip -L %{SOURCE0}
sed -i.orig 's|\r||g' sod.doc
touch -r sod.doc.orig sod.doc


%build
# nothing to build data files only

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/spear/demo
install -p -m 644 *.sdm $RPM_BUILD_ROOT%{_datadir}/spear/demo


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc sod.doc
%{_datadir}/spear


%changelog
* Tue Mar 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 1-3
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 27 2010 Hans de Goede <hdegoede@redhat.com> 1-1
- Initial rpmfusion package
