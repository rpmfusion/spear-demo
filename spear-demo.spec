Name:           spear-demo
Version:        1
Release:        6%{?dist}
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
* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 26 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Mar 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 1-3
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 27 2010 Hans de Goede <hdegoede@redhat.com> 1-1
- Initial rpmfusion package
