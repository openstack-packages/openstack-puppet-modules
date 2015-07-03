Name:           openstack-puppet-modules
Version:        2015.1.8
Release:        1%{?dist}
Summary:        Collection of Puppet modules for OpenStack deployment
License:        ASL 2.0 and GPLv2 and GPLv3

URL:            https://github.com/redhat-openstack

Source0:        https://github.com/redhat-openstack/%{name}/archive/%{version}.tar.gz

Patch0001: 0001-Change-default-documentation-URL.patch
Patch0002: 0002-Explicitly-say-that-ovs_redhat-parent-is-ovs.patch
Patch0003: 0003-Fix-support-for-puppet-4.patch
Patch0004: 0004-Rabbitmq-set-repos_ensure-to-false.patch
Patch0005: 0005-Revert-access-out-of-scope-variables-via-the-scope.l.patch
Patch0006: 0006-Fix-Heat-302-redirects.patch

BuildArch:      noarch
Requires:       rubygem-json

%description
A collection of Puppet modules which are required to install and configure
OpenStack via installers using Puppet configuration tool.


%prep
%setup -q -n %{name}-%{version}

%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1
%patch0006 -p1

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
* Fri Jul 03 2015 Gaël Chamoulaud <gchamoul@redhat.com> - 2015.1.8-1
- Update to upstream 2015.1.8
- Remove Unused patches
- Add 0006-Fix-Heat-302-redirects.patch

* Thu Jun 25 2015 Lukas Bezdicka <lbezdick@redhat.com> 2015.1.7-5
- Deliver fixes for tripleo
- Introduce param to enable use of clustercheck
- Use mode tcp for glance-registry balancing
- Add $verify_on_create ability for all resources.

* Thu Jun 25 2015 Lukas Bezdicka <lbezdick@redhat.com> 2015.1.7-4
- Revert "glance provider: pick os_region_name from DEFAULT"

* Thu Jun 25 2015 Iván Chavero <ichavero@redhat.com> 2015.1.7-3
- Add 0010-Install-only-required-libvirt-packages.patch

* Wed Jun 24 2015 Lukas Bezdicka <lbezdick@redhat.com> 2015.1.7-2
- Revert "access out-of-scope variables via the scope.lookupvar method"

* Tue Jun 23 2015 Lukas Bezdicka <lbezdick@redhat.com> 2015.1.7-1
- Update to upstream 2015.1.7

* Wed Jun 17 2015 Lukas Bezdicka <lbezdick@redhat.com> 2015.1.6-2
- [Rabbitmq] set repos_ensure to false
- Fix support for puppet 4
- Explicitly say that ovs_redhat parent is ovs

* Mon Jun 15 2015 Lukas Bezdicka <lbezdick@redhat.com> 2015.1.6-1
- Update to upstream 2015.1.6

* Thu Jun 11 2015 Ivan Chavero <ichavero@redhat.com> 2015.1.4-1
- Update to upstream 2015.1.4
- Bump glance to master

* Tue Jun 02 2015 Ivan Chavero <ichavero@redhat.com> 2015.1.3-1
- Update to upstream 2015.1.3

* Fri May 15 2015 Lukas Bezdicka <lbezdick@redhat.com> 2015.1.2-1
- Update to upstream 2015.1.2

* Wed May 13 2015 Gaël Chamoulaud <gchamoul@redhat.com> - 2015.1.1-1
-  Updated to release 2015.1.1

* Mon May 11 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 2015.1.0-2
- Add patch to fix TripleO support

* Thu Apr 30 2015 Alan Pevec <alan.pevec@redhat.com> 2015.1.0-1
- OpenStack Kilo release
