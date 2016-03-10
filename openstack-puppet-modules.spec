Name:           openstack-puppet-modules
Epoch:          1
Version:        7.0.14
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
%{_datadir}/openstack-puppet/


%changelog
* Thu Mar 10 2016 Jason Guiditta <jguiditt@redhat.com> 1:7.0.14-1
- Update to 7.0.14

* Tue Mar 08 2016 Jason Guiditta <jguiditt@redhat.com> 1:7.0.13-1
- Update to 7.0.13

* Mon Feb 29 2016 Jason Guiditta <jguiditt@redhat.com> 1:7.0.11-1
- Update to upstream 7.0.11

* Tue Feb 23 2016 Jason Guiditta <jguiditt@redhat.com> 1:7.0.9-1
- Update to upstream 7.0.9

* Mon Feb 22 2016 Alan Pevec <alan.pevec@redhat.com> 1:7.0.7-1
- Update to 7.0.7

* Thu Feb 04 2016 Lukas Bezdicka <lbezdick@redhat.com> 1:7.0.6-1
- Update to upstream 7.0.6

* Tue Oct 20 2015 Lukas Bezdicka <lbezdick@redhat.com> 1:7.0.1-1
- Update to upstream 7.0.1

* Tue Oct 13 2015 Lukas Bezdicka <lbezdick@redhat.com> 7.0.0-1
- Update to upstream 7.0.0

* Sat Oct 10 2015 Alan Pevec <alan.pevec@redhat.com> 2015.2.0-0.1
- OpenStack Liberty RC
