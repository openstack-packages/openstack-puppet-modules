
Name:           openstack-puppet-modules
Version:        2014.2.3
Release:        1%{?dist}
Summary:        Collection of Puppet modules for OpenStack deployment
License:        ASL 2.0 and GPLv2 and GPLv3

URL:            https://github.com/redhat-openstack

Source0:        https://github.com/redhat-openstack/openstack-puppet-modules/archive/%{version}.tar.gz

Patch0001: 0001-horizon-Change-default-documentation-URL.patch
Patch0002: 0002-rabbitmq-Don-t-manage-RabbitMQ-repos.patch
Patch0003: 0003-openstack-Set-default-charset-to-utf8.patch
Patch0004: 0004-heat-Implement-Keystone-domain-creation.patch
Patch0005: 0005-keystone-Add-manage_service-feature.patch
Patch0006: 0006-Fixed-firewalld-package-issue.patch
Patch0007: 0007-Configure-OVS-mechanism-agent-configs-in-its-config-.patch
Patch0008: 0008-Add-manage_service-feature.patch

BuildArch:      noarch
Requires:       rubygem-json

%description
A collection of Puppet modules which are required to install and configure
OpenStack via installers using Puppet configuration tool.


%prep
%setup

%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1
%patch0006 -p1
%patch0007 -p1
%patch0008 -p1

find %{_builddir}/%{name}-%{version}/ -type f -name ".*" -exec rm {} +
find %{_builddir}/%{name}-%{version}/ -size 0 -exec rm {} +
find %{_builddir}/%{name}-%{version}/ \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find %{_builddir}/%{name}-%{version}/ \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find %{_builddir}/%{name}-%{version}/ \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} + -exec sed -i "/^#!/{d;q}" {} +
find %{_builddir}/%{name}-%{version}/ \( -name spec -o -name ext \) | xargs rm -rf


%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/
cp -r apache %{buildroot}/%{_datadir}/openstack-puppet/modules/apache
cp -r ceilometer %{buildroot}/%{_datadir}/openstack-puppet/modules/ceilometer
cp -r certmonger %{buildroot}/%{_datadir}/openstack-puppet/modules/certmonger
cp -r cinder %{buildroot}/%{_datadir}/openstack-puppet/modules/cinder
cp -r common %{buildroot}/%{_datadir}/openstack-puppet/modules/common
cp -r concat %{buildroot}/%{_datadir}/openstack-puppet/modules/concat
cp -r firewall %{buildroot}/%{_datadir}/openstack-puppet/modules/firewall
cp -r galera %{buildroot}/%{_datadir}/openstack-puppet/modules/galera
cp -r glance %{buildroot}/%{_datadir}/openstack-puppet/modules/glance
cp -r gluster %{buildroot}/%{_datadir}/openstack-puppet/modules/gluster
cp -r haproxy %{buildroot}/%{_datadir}/openstack-puppet/modules/haproxy
cp -r heat %{buildroot}/%{_datadir}/openstack-puppet/modules/heat
cp -r horizon %{buildroot}/%{_datadir}/openstack-puppet/modules/horizon
cp -r inifile %{buildroot}/%{_datadir}/openstack-puppet/modules/inifile
cp -r keystone %{buildroot}/%{_datadir}/openstack-puppet/modules/keystone
cp -r memcached %{buildroot}/%{_datadir}/openstack-puppet/modules/memcached
cp -r module-data %{buildroot}/%{_datadir}/openstack-puppet/modules/module-data
cp -r mongodb %{buildroot}/%{_datadir}/openstack-puppet/modules/mongodb
cp -r mysql %{buildroot}/%{_datadir}/openstack-puppet/modules/mysql
cp -r n1k-vsm %{buildroot}/%{_datadir}/openstack-puppet/modules/n1k-vsm
cp -r nagios %{buildroot}/%{_datadir}/openstack-puppet/modules/nagios
cp -r neutron %{buildroot}/%{_datadir}/openstack-puppet/modules/neutron
cp -r nova %{buildroot}/%{_datadir}/openstack-puppet/modules/nova
cp -r nssdb %{buildroot}/%{_datadir}/openstack-puppet/modules/nssdb
cp -r openstack %{buildroot}/%{_datadir}/openstack-puppet/modules/openstack
cp -r openstacklib %{buildroot}/%{_datadir}/openstack-puppet/modules/openstacklib
cp -r pacemaker %{buildroot}/%{_datadir}/openstack-puppet/modules/pacemaker
cp -r puppet %{buildroot}/%{_datadir}/openstack-puppet/modules/puppet
cp -r qpid %{buildroot}/%{_datadir}/openstack-puppet/modules/qpid
cp -r rabbitmq %{buildroot}/%{_datadir}/openstack-puppet/modules/rabbitmq
cp -r rsync %{buildroot}/%{_datadir}/openstack-puppet/modules/rsync
cp -r sahara %{buildroot}/%{_datadir}/openstack-puppet/modules/sahara
cp -r ssh %{buildroot}/%{_datadir}/openstack-puppet/modules/ssh
cp -r staging %{buildroot}/%{_datadir}/openstack-puppet/modules/staging
cp -r stdlib %{buildroot}/%{_datadir}/openstack-puppet/modules/stdlib
cp -r swift %{buildroot}/%{_datadir}/openstack-puppet/modules/swift
cp -r sysctl %{buildroot}/%{_datadir}/openstack-puppet/modules/sysctl
cp -r tempest %{buildroot}/%{_datadir}/openstack-puppet/modules/tempest
cp -r vcsrepo %{buildroot}/%{_datadir}/openstack-puppet/modules/vcsrepo
cp -r vlan %{buildroot}/%{_datadir}/openstack-puppet/modules/vlan
cp -r vswitch %{buildroot}/%{_datadir}/openstack-puppet/modules/vswitch
cp -r xinetd %{buildroot}/%{_datadir}/openstack-puppet/modules/xinetd
cp Puppetfile %{buildroot}/%{_datadir}/openstack-puppet/Puppetfile
rm -f %{buildroot}/%{_datadir}/openstack-puppet/modules/nova/files/nova-novncproxy.init


%files
%{_datadir}/openstack-puppet/modules/*
%{_datadir}/openstack-puppet/Puppetfile


%changelog
* Mon Nov 03 2014 Lukas Bezdicka <lbezdick@redhat.com> 2014.2.3-1
- Update to upstream 2014.2.3

* Fri Oct 31 2014 Lukas Bezdicka <lbezdick@redhat.com> 2014.2.2-2
- Fix sources url

* Fri Oct 31 2014 Lukas Bezdicka <lbezdick@redhat.com> 2014.2.2-1
- Update to upstream 2014.2.2

* Fri Oct 24 2014 Lukas Bezdicka <lbezdick@redhat.com> 2014.2.1-0.5
- Fixed firewalld package issue

* Mon Oct 06 2014 Martin Mágr <mmagr@redhat.com> 2014.2.1-0.4
- Update to upstream 2014.2.1

* Thu Oct 2 2014 Martin Mágr <mmagr@redhat.com> - 2014.2-0.3.1
- Added 0001-Update-deprecated-Glance-CLI.patch (rhbz#1148346)

* Wed Sep 10 2014 Lukas Bezdicka <lbezdick@redhat.com> - 2014.2-0.3
- fixed o-p-m master module versions

* Mon Sep 08 2014 Iván Chavero <ichavero@redhat.com> - 2014.2-0.2
- Updated to latest puppet modules
- Added nagios module
- Added openstacklib module
- Removed 0001-Remove-ability-to-manage-the-nova-uid-gid.patch
- Removed mariadb.patch
- Removed nova.patch

* Wed Sep 03 2014 Iván Chavero <ichavero@redhat.com> - 2014.2-0.1
- Updated to #20 0001-Refacfored-a-more-suitable-ovs_redhat-provider.patch
  (rhbz#1133446)
- Added 0001-vlan-is-not-the-same-as-vlan_start.patch (rhbz#1135079)
- Added manage_service-neutron.patch (rhbz#1134000)
- Updated puppet-galera module (rhbz#1129397)
- Added manage_service-ceilometer.patch (rhbz#1129410)
- Added manage_service-heat.patch (rhbz#1129407)
- Added manage_service-horizon.patch (rhbz#1129408)
- Added manage_service-keystone.patch (rhbz#1129399)
- Added manage_service-swift.patch (rhbz#1129409)
- Added manage_service-glance.patch (rhbz#1129404)

* Mon Aug 18 2014 Iván Chavero <ichavero@redhat.com> - 2014.1-20.1
- Added missing patches

* Mon Aug 18 2014 Iván Chavero <ichavero@redhat.com> - 2014.1-20
- Updated 0001-Refacfored-a-more-suitable-ovs_redhat-provider.patch to patchset 17 (rhbz#1130657)
- Bump Pacemaker to the latest version (rhbz#1120584)
- Add 0001-Fixes-plugin.ini-error.patch (rhbz#1114739)

* Wed Jul 30 2014 Iván Chavero <icahvero@redhat.com> - 2014.1-19.3
- Fixed sources upload

* Wed Jul 30 2014 Iván Chavero <icahvero@redhat.com> - 2014.1-19.2
- Updated sources file

* Wed Jul 30 2014 Iván Chavero <icahvero@redhat.com> - 2014.1-19.1
- Updated sources file

* Wed Jul 30 2014 Iván Chavero <icahvero@redhat.com> - 2014.1-19
- Bump to the latest stable puppet modules
- Removed puppetlabs-firewall-pull-request-367.patch
- Add puppetlabs-firewall-pull-request-367-2.patch
- Removed 0002-Refacfored-a-more-suitable-ovs_redhat-provider.patch
- Removed 0003-Fixes-bridge-addition-error-if-interface-has-no-IP.patch
- Add 0001-Refacfored-a-more-suitable-ovs_redhat-provider.patch
- Removed 0001-Refresh-Neutron-server.patch
- Add 0001-Remove-ability-to-manage-the-nova-uid-gid.patch
- Add 0001-Install-ceph-client-libraries-when-using-rbd.patch
- Add 0001-Configure-OVS-mechanism-agent-configs-in-its-config-.patch

* Thu Jun 26 2014 Martin Mágr <mmagr@redhat.com> - 2014.1-18
- Updated modules to redhat-openstack/openstack-puppet-modules-2014.1-18
- Added 0001-Refresh-Neutron-server.patch (rhbz#1110281)
- Added rabbitmq-repo-manage.patch (rhbz#1112853)
- Added cinder-target-service.patch
- Removed swift-restorecon.patch

* Wed Jun 25 2014 Martin Mágr <mmagr@redhat.com> - 2014.1-17
- Updated modules to redhat-openstack/openstack-puppet-modules-2014.1-17
- Added rdo-documentation.patch
- Added 0001-stop-puppet-from-breaking-neutron.patch
- Added 0001-Fixes-bridge-interface-name-check.patch
- Added 0001-Fixed-ovs-provider.patch, 0002-Refacfored-a-more-suitable-ovs_redhat-provider.patch,
        0003-Fixes-bridge-addition-error-if-interface-has-no-IP.patch (rhbz#1109894)

* Wed Jun 18 2014 Martin Mágr <mmagr@redhat.com> - 2014.1-16
- Updated modules to redhat-openstack/openstack-puppet-modules-2014.1-16
- Removed keystone.patch and 0001-Fixes-agent_notification_service_name.patch
- Disabled puppet-module-data module because it breaks O-F-I

* Wed Jun 11 2014 Martin Mágr <mmagr@redhat.com> - 2014.1-15
- Updated modules to redhat-openstack/openstack-puppet-modules-2014.1-15
- Added puppetlabs-firewall-pull-request-367.patch and swift-restorecon.patch and 0001-Implement-Keystone-domain-creation.patch
- Removed cinder.patch and 0001-Use-lioadm-as-iscsi-helper-on-RHEL-7.patch

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014.1-14.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jun 04 2014 Martin Mágr <mmagr@redhat.com> - 2014.1-13.2
- Fixed 0001-Fixes-agent_notification_service_name.patch

* Fri May 30 2014 Martin Mágr <mmagr@redhat.com> - 2014.1-13.1
- Added puppetlabs-firewall-pull-request-365.patch

* Fri May 30 2014 Martin Mágr <mmagr@redhat.com> - 2014.1-13
- Synchronized modules with current master branch of redhat-openstack/openstack-puppet-modules
- Added 0001-Fixes-agent_notification_service_name.patch

* Fri May 23 2014 Martin Mágr <mmagr@redhat.com> - 2014.1-12
- Synchronized modules with current master branch of redhat-openstack/openstack-puppet-modules
- Removed glance.patch since the changes are now upstream

* Fri May 16 2014 Martin Mágr <mmagr@redhat.com> - 2014.1-11.1
- Added missing puppetlabs-firewall-pull-request-337.patch

* Wed May 14 2014 Martin Mágr <mmagr@redhat.com> - 2014.1-11
- Synchronized modules with current master branch of redhat-openstack/openstack-puppet-modules

* Mon May 12 2014 Martin Mágr <mmagr@redhat.com> - 2014.1-10.1
- Added 0001-Quickfix-to-remove-duplication-with-ceilometer-agent.patch

* Mon May 12 2014 Martin Mágr <mmagr@redhat.com> - 2014.1-10
- Synchronized modules with current master branch of redhat-openstack/openstack-puppet-modules

* Wed May 7 2014 Martin Mágr <mmagr@redhat.com> - 2014.1-9.1
- Added rubyjem-json requirement

* Wed Apr 30 2014 Martin Mágr <mmagr@redhat.com> - 2014.1-9
- Synchronized modules with current master branch of redhat-openstack/openstack-puppet-modules
- Switched puppet-gluster for puppet-openstack-storage
- Added modules required by puppet-gluster: puppet-common, puppet-keepalived, puppet-puppet
- Updated modules: puppetlabs-apache, puppetlabs-mysql, puppet-neutron, puppet-pacepaker, puppetlabs-stdlib, puppet-vswitch
- Removed unnecessary patches: apache24.patch, mariadb.patch, neutron.patch, 0001-Fix-neutron-subnets-with-empty-values.patch

* Fri Apr 25 2014 Iván Chavero <ichavero@redhat.com> - 2014.1-8
- Added patches for neutron, cinder and nova

* Tue Apr 8 2014 Martin Mágr <mmagr@redhat.com> - 2014.1-7
- Synchronized modules with current master branch of redhat-openstack/openstack-puppet-modules

* Mon Apr 7 2014 Martin Mágr <mmagr@redhat.com> - 2014.1-6
- Synchronized modules with current master branch of redhat-openstack/openstack-puppet-modules

* Wed Apr 2 2014 Iván Chavero <ichavero@redhat.com> - 2014.1-5.6
- Synchronized pacemaker with current master branch of redhat-openstack/openstack-puppet-modules

* Wed Apr 2 2014 Martin Mágr <mmagr@redhat.com> - 2014.1-5.5
- Added 0001-Fix-network_vlan_ranges-parameter-for-OVS-plugin.patch (rhbz#1066549)
- Added 0002-Change-dhcp_lease_duration-to-Havana-default-of-8640.patch (rhbz#1082505)
- Added 0003-Do-not-create-symblic-link-for-cisco-plugin.patch (rhbz#1080442)

* Mon Mar 31 2014 Iván Chavero <ichavero@redhat.com> - 2014.1-5.4
- Added cinder.patch, nova.patch and keystone.patch utf8 charset patches

* Wed Mar 26 2014 Iván Chavero <ichavero@redhat.com> - 2014.1-5.3
- Added openstack.patch

* Wed Mar 26 2014 Iván Chavero <ichavero@redhat.com> - 2014.1-5.2
- Added heat.patch and neutron.patch

* Mon Mar 24 2014 Martin Mágr <mmagr@redhat.com> - 2014.1-5.1
- Added glance.patch

* Fri Mar 21 2014 Martin Mágr <mmagr@redhat.com> - 2014.1-5
- Synchronized modules with current master branch of redhat-openstack/openstack-puppet-modules

* Thu Mar 20 2014 Martin Mágr <mmagr@redhat.com> - 2014.1-4
- Added mariadb.patch, apache24.patch

* Mon Mar 17 2014 Martin Mágr <mmagr@redhat.com> - 2014.1-3
- Added compute_driver.patch (rhbz#1044606)

* Tue Mar 11 2014 Martin Mágr <mmagr@redhat.com> - 2014.1-2
- Synchronized modules with current master branch of redhat-openstack/openstack-puppet-modules

* Wed Feb 12 2014 Martin Mágr <mmagr@redhat.com> - 2014.1-1
- Synchronized modules with current master branch of Packstack
  and openstack-puppet-modules-repo (https://github.com/redhat-openstack/openstack-puppet-modules)

* Thu Dec 05 2013 Ben Nemec <bnemec@redhat.com> - 2013.2-7
- Added puppet-openstack-storage
- Synchronized modules with current state in package packstack-modules-puppet

* Wed Dec 04 2013 Ben Nemec <bnemec@redhat.com> - 2013.2-6
- Synchronized modules with current state in package packstack-modules-puppet

* Fri Nov 15 2013 Ben Nemec <bnemec@redhat.com> - 2013.2-5
- Added puppet-certmonger and puppet-nssdb
- Synchronized modules with current state in package packstack-modules-puppet

* Fri Oct 25 2013 Martin Mágr <mmagr@redhat.com> - 2013.2-4
- Added puppet-ceilometer, puppetlabs-mongodb, puppet-heat and puppet-pacemaker
- Synchronized modules with current state in package packstack-modules-puppet

* Sun Oct 20 2013 Ryan O'Hara <rohara@redhat.com> - 2013.2-3
- Install modules to openstack-puppet directory.

* Mon Oct 14 2013 Ryan O'Hara <rohara@redhat.com> - 2013.2-2
- Package review changes.

* Wed Sep 04 2013 Ryan O'Hara <rohara@redhat.com> - 2013.2-1
- Initial spec file.
