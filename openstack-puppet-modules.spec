Name:           openstack-puppet-modules
Version:        2015.1.1
Release:        1%{?dist}
Summary:        Collection of Puppet modules for OpenStack deployment
License:        ASL 2.0 and GPLv2 and GPLv3

URL:            https://github.com/redhat-openstack

Source0:        https://github.com/redhat-openstack/%{name}/archive/%{version}.tar.gz

BuildArch:      noarch
Requires:       rubygem-json

%description
A collection of Puppet modules which are required to install and configure
OpenStack via installers using Puppet configuration tool.


%prep
%setup -q -n %{name}-%{version}


find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf


%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/
cp -r $(grep ^mod Puppetfile |cut -d\' -f2) %{buildroot}/%{_datadir}/openstack-puppet/modules/
cp Puppetfile %{buildroot}/%{_datadir}/openstack-puppet/Puppetfile
rm -f %{buildroot}/%{_datadir}/openstack-puppet/modules/nova/files/nova-novncproxy.init


%files
%{_datadir}/openstack-puppet/modules/*
%{_datadir}/openstack-puppet/Puppetfile


%changelog
* Wed May 13 2015 Gaël Chamoulaud <gchamoul@redhat.com> - 2015.1.1-1
-  Updated to release 2015.1.1

* Mon May 11 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 2015.1.0-2
- Add patch to fix TripleO support

* Thu Apr 30 2015 Alan Pevec <alan.pevec@redhat.com> 2015.1.0-1
- OpenStack Kilo release
