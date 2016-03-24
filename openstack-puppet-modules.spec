%global milestone .0rc1

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           openstack-puppet-modules
Epoch:          1
Version:        8.0.0
Release:        0.1%{?milestone}%{?dist}
Summary:        Puppet modules used to deploy OpenStack
License:        ASL 2.0 and GPLv2 and GPLv3

URL:            https://github.com/redhat-openstack

Source0:        https://github.com/redhat-openstack/%{name}/archive/%{upstream_version}.tar.gz

BuildArch:      noarch
Requires:       rubygem-json

%description
A collection of Puppet modules used to install and configure OpenStack.


%prep
%setup -q -n %{name}-%{?upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +


%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/
cp -r $(grep ^mod Puppetfile |cut -d\' -f2) %{buildroot}/%{_datadir}/openstack-puppet/modules/
cp Puppetfile %{buildroot}/%{_datadir}/openstack-puppet/Puppetfile
rm -f %{buildroot}/%{_datadir}/openstack-puppet/modules/nova/files/nova-novncproxy.init


%files
%{_datadir}/openstack-puppet/


%changelog
* Thu Mar 24 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 1:8.0.0-0.1.0rc1%{?dist}
- Upstream 8.0.0.0rc1

