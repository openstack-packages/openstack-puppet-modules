
%global apache_commit		bbf9278b24931444022aa67140d3505b748151da
%global ceilometer_commit	c2f41fb1eb776bcfdaab79c120ac509a861d0828
%global certmonger_commit	5fbf10fbbff4aed4db30e839c63c99b195e8425a
%global cinder_commit		57da044279780af66479c429e5803825a87b785e
%global common_commit		2c0ed2844c606fd806bde0c02e47e79c88fab4a9
%global concat_commit		031bf261289dcbb32e63b053ed5b3a82117698c0
%global firewall_commit		c147a624fb3dba7df625d0d7571b1b6669bcfca5
%global galera_commit		3f63bd5ffdd707b42ef37a0ead3c2cf7e803586f
%global glance_commit		cb0daf02d7a991be642e62294912d93b036c6a5a
%global gluster_commit		80c2b13448c97c70a4b4bc0e402e00ecb5d681d5
%global haproxy_commit		f381510e940ee11feb044c1c728ba2e5af807c79
%global heat_commit		    17736b2fd726858cb83590f8a8b1d594a087ea44
%global horizon_commit		bd1c31e87dd0564a8fab8de0516dbbe48241b09a
%global inifile_commit		fe9b0d5229ea37179a08c4b49239da9bc950acd1
%global keystone_commit		e61e4c2ab5c67150237e59dab25679ec739d3ebf
%global memcached_commit	49dbf102fb6eee90297b2ed6a1fa463a8c5ccee7
%global module_data_commit	159fc5e0e21ce9df96c777f0064b5eca88e29cae
%global mongodb_commit		3f392925710f1758a95f1775d700b5fb787a003d
%global mysql_commit		8d5fed32c22c5e4231d5a475cfe8060ce8b2ed0f
%global neutron_commit		66c436bc2f06c5a71d79c674697394a11ec227f9
%global nova_commit		    1e77a9d48a85a3ae6d30993b3c887f58e4a5973c
%global nssdb_commit		b3799a9a7c62c3b5b7968f9860220a885b45fb8a
%global openstack_commit	c20039004cb39e78c93cd00f154c3b9ba6404951
%global pacemaker_commit	2aa760c3497840ad2474f15737846e2ad95c54e5
%global puppet_commit		07ec49d1f67a498b31b4f164678a76c464e129c4
%global qpid_commit		    1f0c32b39ad17e7acbd440b50fb6f0875971f5e1
%global rabbitmq_commit		e7447851a60a419cd51a09ccf807964b36fdebac
%global rsync_commit		357d51f3a6a22bc3da842736176c3510e507b4fb
%global sahara_commit		f4e5681cfb289113be1ba49c12709145ecbad938
%global ssh_commit		    d6571f8c43ac55d20a6afd8a8ce3f86ac4b0d7a4
%global staging_commit		887275d8fb20e148c6f9eb327f1f6c8ea5ee280f
%global stdlib_commit		62e8c1d76902e6f22cb9f7b3abd43e757b4130a3
%global swift_commit		80ec3a7576efad5e13d37a8c760ed0ad7f36055f
%global sysctl_commit		c4486acc2d66de857dbccd8b4b945ea803226705
%global tempest_commit		792be887b61ad9c38706e968a21752cfb05c2381
%global vcsrepo_commit		6f7507a2a48ff0a58c7db026760a2eb84e382a77
%global vlan_commit		    c937de75c28e63fba8d8738ad6a5f2ede517e53d
%global vswitch_commit		a20f6355f048d2cb6206222b2d045b41ac875db4
%global xinetd_commit		6b02de8d4f30a819eb404048e4258e3a5e8023c8


Name:           openstack-puppet-modules
Version:        2014.1
Release:        18%{?dist}
Summary:        Puppet modules used to deploy OpenStack
License:        ASL 2.0 and GPLv2 and GPLv3

URL:            https://github.com/redhat-openstack

Source0:	https://github.com/puppetlabs/puppetlabs-apache/archive/%{apache_commit}/apache-%{apache_commit}.tar.gz
Source1:	https://github.com/stackforge/puppet-ceilometer/archive/%{ceilometer_commit}/ceilometer-%{ceilometer_commit}.tar.gz
Source2:	https://github.com/rcritten/puppet-certmonger/archive/%{certmonger_commit}/certmonger-%{certmonger_commit}.tar.gz
Source3:	https://github.com/stackforge/puppet-cinder/archive/%{cinder_commit}/cinder-%{cinder_commit}.tar.gz
Source4:	https://github.com/purpleidea/puppet-common/archive/%{common_commit}/common-%{common_commit}.tar.gz
Source5:	https://github.com/ripienaar/puppet-concat/archive/%{concat_commit}/concat-%{concat_commit}.tar.gz
Source6:	https://github.com/puppetlabs/puppetlabs-firewall/archive/%{firewall_commit}/firewall-%{firewall_commit}.tar.gz
Source7:	https://github.com/rohara/puppet-galera/archive/%{galera_commit}/galera-%{galera_commit}.tar.gz
Source8:	https://github.com/stackforge/puppet-glance/archive/%{glance_commit}/glance-%{glance_commit}.tar.gz
Source9:	https://github.com/purpleidea/puppet-gluster/archive/%{gluster_commit}/gluster-%{gluster_commit}.tar.gz
Source10:	https://github.com/puppetlabs/puppetlabs-haproxy/archive/%{haproxy_commit}/haproxy-%{haproxy_commit}.tar.gz
Source11:	https://github.com/stackforge/puppet-heat/archive/%{heat_commit}/heat-%{heat_commit}.tar.gz
Source12:	https://github.com/stackforge/puppet-horizon/archive/%{horizon_commit}/horizon-%{horizon_commit}.tar.gz
Source13:	https://github.com/puppetlabs/puppetlabs-inifile/archive/%{inifile_commit}/inifile-%{inifile_commit}.tar.gz
Source14:	https://github.com/stackforge/puppet-keystone/archive/%{keystone_commit}/keystone-%{keystone_commit}.tar.gz
Source15:	https://github.com/saz/puppet-memcached/archive/%{memcached_commit}/memcached-%{memcached_commit}.tar.gz
#Source16:	https://github.com/ripienaar/puppet-module-data/archive/%{module_data_commit}/module-data-%{module_data_commit}.tar.gz
Source17:	https://github.com/puppetlabs/puppetlabs-mongodb/archive/%{mongodb_commit}/mongodb-%{mongodb_commit}.tar.gz
Source18:	https://github.com/packstack/puppetlabs-mysql/archive/%{mysql_commit}/mysql-%{mysql_commit}.tar.gz
Source19:	https://github.com/stackforge/puppet-neutron/archive/%{neutron_commit}/neutron-%{neutron_commit}.tar.gz
Source20:	https://github.com/stackforge/puppet-nova/archive/%{nova_commit}/nova-%{nova_commit}.tar.gz
Source21:	https://github.com/rcritten/puppet-nssdb/archive/%{nssdb_commit}/nssdb-%{nssdb_commit}.tar.gz
Source22:	https://github.com/stackforge/puppet-openstack/archive/%{openstack_commit}/openstack-%{openstack_commit}.tar.gz
Source23:	https://github.com/radez/puppet-pacemaker/archive/%{pacemaker_commit}/pacemaker-%{pacemaker_commit}.tar.gz
Source24:	https://github.com/purpleidea/puppet-puppet/archive/%{puppet_commit}/puppet-%{puppet_commit}.tar.gz
Source25:	https://github.com/dprince/puppet-qpid/archive/%{qpid_commit}/qpid-%{qpid_commit}.tar.gz
Source26:	https://github.com/puppetlabs/puppetlabs-rabbitmq/archive/%{rabbitmq_commit}/rabbitmq-%{rabbitmq_commit}.tar.gz
Source27:	https://github.com/puppetlabs/puppetlabs-rsync/archive/%{rsync_commit}/rsync-%{rsync_commit}.tar.gz
Source28:	https://github.com/stackforge/puppet-sahara/archive/%{sahara_commit}/sahara-%{sahara_commit}.tar.gz
Source29:	https://github.com/saz/puppet-ssh/archive/%{ssh_commit}/ssh-%{ssh_commit}.tar.gz
Source30:	https://github.com/nanliu/puppet-staging/archive/%{staging_commit}/staging-%{staging_commit}.tar.gz
Source31:	https://github.com/puppetlabs/puppetlabs-stdlib/archive/%{stdlib_commit}/stdlib-%{stdlib_commit}.tar.gz
Source32:	https://github.com/stackforge/puppet-swift/archive/%{swift_commit}/swift-%{swift_commit}.tar.gz
Source33:	https://github.com/puppetlabs/puppetlabs-sysctl/archive/%{sysctl_commit}/sysctl-%{sysctl_commit}.tar.gz
Source34:	https://github.com/stackforge/puppet-tempest/archive/%{tempest_commit}/tempest-%{tempest_commit}.tar.gz
Source35:	https://github.com/puppetlabs/puppetlabs-vcsrepo/archive/%{vcsrepo_commit}/vcsrepo-%{vcsrepo_commit}.tar.gz
Source36:	https://github.com/derekhiggins/puppet-vlan/archive/%{vlan_commit}/vlan-%{vlan_commit}.tar.gz
Source37:	https://github.com/stackforge/puppet-vswitch/archive/%{vswitch_commit}/vswitch-%{vswitch_commit}.tar.gz
Source38:	https://github.com/packstack/puppetlabs-xinetd/archive/%{xinetd_commit}/xinetd-%{xinetd_commit}.tar.gz

# stable patches
Patch0:     rdo-documentation.patch
Patch1:     rabbitmq-repo-manage.patch

# temporary patches
Patch100:   compute_driver.patch
Patch101:   openstack.patch
Patch102:   nova.patch
Patch103:   0001-Quickfix-to-remove-duplication-with-ceilometer-agent.patch
Patch104:   puppetlabs-firewall-pull-request-337.patch
Patch105:   puppetlabs-firewall-pull-request-365.patch
Patch106:   puppetlabs-firewall-pull-request-367.patch
Patch108:   0001-Implement-Keystone-domain-creation.patch
Patch109:   0001-Fixed-ovs-provider.patch
Patch110:   0002-Refacfored-a-more-suitable-ovs_redhat-provider.patch
Patch111:   0001-stop-puppet-from-breaking-neutron.patch
Patch112:   0001-Fixes-bridge-interface-name-check.patch
Patch113:   0003-Fixes-bridge-addition-error-if-interface-has-no-IP.patch
Patch114:   0001-Refresh-Neutron-server.patch
Patch115:   cinder-target-service.patch

BuildArch:      noarch
Requires:       rubygem-json

%description
A collection of Puppet modules used to install and configure OpenStack.


%prep
%setup -c -q -T -D -a 0
%setup -c -q -T -D -a 1
%setup -c -q -T -D -a 2
%setup -c -q -T -D -a 3
%setup -c -q -T -D -a 4
%setup -c -q -T -D -a 5
%setup -c -q -T -D -a 6
%setup -c -q -T -D -a 7
%setup -c -q -T -D -a 8
%setup -c -q -T -D -a 9
%setup -c -q -T -D -a 10
%setup -c -q -T -D -a 11
%setup -c -q -T -D -a 12
%setup -c -q -T -D -a 13
%setup -c -q -T -D -a 14
%setup -c -q -T -D -a 15
#%setup -c -q -T -D -a 16
%setup -c -q -T -D -a 17
%setup -c -q -T -D -a 18
%setup -c -q -T -D -a 19
%setup -c -q -T -D -a 20
%setup -c -q -T -D -a 21
%setup -c -q -T -D -a 22
%setup -c -q -T -D -a 23
%setup -c -q -T -D -a 24
%setup -c -q -T -D -a 25
%setup -c -q -T -D -a 26
%setup -c -q -T -D -a 27
%setup -c -q -T -D -a 28
%setup -c -q -T -D -a 29
%setup -c -q -T -D -a 30
%setup -c -q -T -D -a 31
%setup -c -q -T -D -a 32
%setup -c -q -T -D -a 33
%setup -c -q -T -D -a 34
%setup -c -q -T -D -a 35
%setup -c -q -T -D -a 36
%setup -c -q -T -D -a 37
%setup -c -q -T -D -a 38

# puppet-horizon patches
cd %{_builddir}/%{name}-%{version}/puppet-horizon-%{horizon_commit}
%patch0 -p1

# puppet-nova patches
cd %{_builddir}/%{name}-%{version}/puppet-nova-%{nova_commit}
%patch100 -p1
%patch102 -p1
%patch103 -p1

# puppet-heat patches
cd %{_builddir}/%{name}-%{version}/puppet-heat-%{heat_commit}
%patch108 -p1

# puppet-openstack patches
cd %{_builddir}/%{name}-%{version}/puppet-openstack-%{openstack_commit}
%patch101 -p1

# puppetlabs-firewall patches
cd %{_builddir}/%{name}-%{version}/puppetlabs-firewall-%{firewall_commit}
%patch104 -p1
%patch105 -p1
%patch106 -p1

# puppet-neutron patches
cd %{_builddir}/%{name}-%{version}/puppet-neutron-%{neutron_commit}
%patch111 -p1
%patch114 -p1

# puppet-vswitch patches
cd %{_builddir}/%{name}-%{version}/puppet-vswitch-%{vswitch_commit}
%patch109 -p1
%patch110 -p1
%patch112 -p1
%patch113 -p1

# puppetlabs-rabbitmq patches
cd %{_builddir}/%{name}-%{version}/puppetlabs-rabbitmq-%{rabbitmq_commit}
%patch1 -p1

# puppet-cinder patches
cd %{_builddir}/%{name}-%{version}/puppet-cinder-%{cinder_commit}
%patch115 -p1

find %{_builddir}/%{name}-%{version}/ -type f -name ".*" -exec rm {} +
find %{_builddir}/%{name}-%{version}/ -size 0 -exec rm {} +
find %{_builddir}/%{name}-%{version}/ \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find %{_builddir}/%{name}-%{version}/ \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find %{_builddir}/%{name}-%{version}/ \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} + -exec sed -i "/^#!/{d;q}" {} +


%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/
cp -r puppetlabs-apache-%{apache_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/apache
cp -r puppet-ceilometer-%{ceilometer_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/ceilometer
cp -r puppet-certmonger-%{certmonger_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/certmonger
cp -r puppet-cinder-%{cinder_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/cinder
cp -r puppet-common-%{common_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/common
cp -r puppetlabs-concat-%{concat_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/concat
cp -r puppetlabs-firewall-%{firewall_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/firewall
cp -r puppet-galera-%{galera_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/galera
cp -r puppet-glance-%{glance_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/glance
cp -r puppet-gluster-%{gluster_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/gluster
cp -r puppetlabs-haproxy-%{haproxy_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/haproxy
cp -r puppet-heat-%{heat_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/heat
cp -r puppet-horizon-%{horizon_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/horizon
cp -r puppetlabs-inifile-%{inifile_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/inifile
cp -r puppet-keystone-%{keystone_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/keystone
cp -r puppet-memcached-%{memcached_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/memcached
#cp -r puppet-module-data-%{module_data_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/module-data
cp -r puppetlabs-mongodb-%{mongodb_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/mongodb
cp -r puppetlabs-mysql-%{mysql_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/mysql
cp -r puppet-neutron-%{neutron_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/neutron
cp -r puppet-nova-%{nova_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/nova
cp -r puppet-nssdb-%{nssdb_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/nssdb
cp -r puppet-openstack-%{openstack_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/openstack
cp -r puppet-pacemaker-%{pacemaker_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/pacemaker
cp -r puppet-puppet-%{puppet_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/puppet
cp -r puppet-qpid-%{qpid_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/qpid
cp -r puppetlabs-rabbitmq-%{rabbitmq_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/rabbitmq
cp -r puppetlabs-rsync-%{rsync_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/rsync
cp -r puppet-sahara-%{sahara_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/sahara
cp -r puppet-ssh-%{ssh_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/ssh
cp -r puppet-staging-%{staging_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/staging
cp -r puppetlabs-stdlib-%{stdlib_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/stdlib
cp -r puppet-swift-%{swift_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/swift
cp -r puppetlabs-sysctl-%{sysctl_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/sysctl
cp -r puppet-tempest-%{tempest_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/tempest
cp -r puppetlabs-vcsrepo-%{vcsrepo_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/vcsrepo
cp -r puppet-vlan-%{vlan_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/vlan
cp -r puppet-vswitch-%{vswitch_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/vswitch
cp -r puppetlabs-xinetd-%{xinetd_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/xinetd
rm -f %{buildroot}/%{_datadir}/openstack-puppet/modules/nova/files/nova-novncproxy.init


%files
%{_datadir}/openstack-puppet/modules/*


%changelog
* Wed Jun 26 2014 Martin Mágr <mmagr@redhat.com> - 2014.1-18
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
