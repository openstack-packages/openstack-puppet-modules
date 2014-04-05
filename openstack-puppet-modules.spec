
%global apache_commit		a9017af0190bbfaf56cffbac042ca2a081198e89
%global ceilometer_commit	91045b3be907b074cb1e0165b269d439aee43a26
%global certmonger_commit	5fbf10fbbff4aed4db30e839c63c99b195e8425a
%global cinder_commit		164163a7a267ae4139e2d97bab1a385a6da2ac5f
%global concat_commit		031bf261289dcbb32e63b053ed5b3a82117698c0
%global firewall_commit		56fa4a46f4481dd5ac7d619b43b96d683ee4ac82
%global glance_commit		5557c224f37c22b058c951d7494448981cb484a2
%global gluster_commit		4b60e1f848d18b72c1ba959e1b2dd8708a30f605
%global haproxy_commit		f381510e940ee11feb044c1c728ba2e5af807c79
%global heat_commit		    6d2dc044e12c4c687647cff8bc60c981d9ed5312
%global horizon_commit		17ba6a73cec7f386922e6a914a120a829e225efc
%global inifile_commit		fe9b0d5229ea37179a08c4b49239da9bc950acd1
%global keystone_commit		688ff4379ed7437747ff8fdcd464096e24b4ebc6
%global memcached_commit	49dbf102fb6eee90297b2ed6a1fa463a8c5ccee7
%global mongodb_commit		3f392925710f1758a95f1775d700b5fb787a003d
%global mysql_commit		83abc4556bbf6745708c08375649c9d71b6f66db
%global neutron_commit		1cc2b42ceb39b199d96945eb4e6e972e6b32a2b8
%global nova_commit		    6c8a4bd5e1d67cce4c6e316c2ba43ed5a4dd4e59
%global nssdb_commit		b3799a9a7c62c3b5b7968f9860220a885b45fb8a
%global openstack_commit	c20039004cb39e78c93cd00f154c3b9ba6404951
%global pacemaker_commit	dd832b77b2c90d5ad08319483e2bd471373bc375
%global qpid_commit		    953028ba9abdf563bd95970ccf890237711072fb
%global rabbitmq_commit		015bd788ccb495051a2db48e344a3a6aa3381076
%global rsync_commit		357d51f3a6a22bc3da842736176c3510e507b4fb
%global ssh_commit		    d6571f8c43ac55d20a6afd8a8ce3f86ac4b0d7a4
%global staging_commit		887275d8fb20e148c6f9eb327f1f6c8ea5ee280f
%global stdlib_commit		4d2558f383e18bbe322dd0feb073555491216ab4
%global swift_commit		e9b69499c943bfbb16c895611ebd4e90c16b377c
%global sysctl_commit		c4486acc2d66de857dbccd8b4b945ea803226705
%global tempest_commit		44e258746cb0cf9a53f37122d510474aed39201e
%global vcsrepo_commit		6f7507a2a48ff0a58c7db026760a2eb84e382a77
%global vlan_commit		    c937de75c28e63fba8d8738ad6a5f2ede517e53d
%global vswitch_commit		b642b844db6d7df1ced6f11abd641a0982e06363
%global xinetd_commit		bba48fad94c6538384173e60900a17c6f7ef7ca3


Name:           openstack-puppet-modules
Version:        2014.1
Release:        5.6%{?dist}
Summary:        Puppet modules used to deploy OpenStack
License:        ASL 2.0 and GPLv2 and GPLv3

URL:            https://github.com/redhat-openstack

Source0:	https://github.com/puppetlabs/puppetlabs-apache/archive/%{apache_commit}/apache-%{apache_commit}.tar.gz
Source1:	https://github.com/stackforge/puppet-ceilometer/archive/%{ceilometer_commit}/ceilometer-%{ceilometer_commit}.tar.gz
Source2:	https://github.com/rcritten/puppet-certmonger/archive/%{certmonger_commit}/certmonger-%{certmonger_commit}.tar.gz
Source3:	https://github.com/stackforge/puppet-cinder/archive/%{cinder_commit}/cinder-%{cinder_commit}.tar.gz
Source4:	https://github.com/ripienaar/puppet-concat/archive/%{concat_commit}/concat-%{concat_commit}.tar.gz
Source5:	https://github.com/puppetlabs/puppetlabs-firewall/archive/%{firewall_commit}/firewall-%{firewall_commit}.tar.gz
Source6:	https://github.com/stackforge/puppet-glance/archive/%{glance_commit}/glance-%{glance_commit}.tar.gz
Source7:	https://github.com/redhat-openstack/puppet-openstack-storage/archive/%{gluster_commit}/gluster-%{gluster_commit}.tar.gz
Source8:	https://github.com/puppetlabs/puppetlabs-haproxy/archive/%{haproxy_commit}/haproxy-%{haproxy_commit}.tar.gz
Source9:	https://github.com/packstack/puppet-heat/archive/%{heat_commit}/heat-%{heat_commit}.tar.gz
Source10:	https://github.com/stackforge/puppet-horizon/archive/%{horizon_commit}/horizon-%{horizon_commit}.tar.gz
Source11:	https://github.com/puppetlabs/puppetlabs-inifile/archive/%{inifile_commit}/inifile-%{inifile_commit}.tar.gz
Source12:	https://github.com/stackforge/puppet-keystone/archive/%{keystone_commit}/keystone-%{keystone_commit}.tar.gz
Source13:	https://github.com/saz/puppet-memcached/archive/%{memcached_commit}/memcached-%{memcached_commit}.tar.gz
Source14:	https://github.com/puppetlabs/puppetlabs-mongodb/archive/%{mongodb_commit}/mongodb-%{mongodb_commit}.tar.gz
Source15:	https://github.com/packstack/puppetlabs-mysql/archive/%{mysql_commit}/mysql-%{mysql_commit}.tar.gz
Source16:	https://github.com/stackforge/puppet-neutron/archive/%{neutron_commit}/neutron-%{neutron_commit}.tar.gz
Source17:	https://github.com/stackforge/puppet-nova/archive/%{nova_commit}/nova-%{nova_commit}.tar.gz
Source18:	https://github.com/rcritten/puppet-nssdb/archive/%{nssdb_commit}/nssdb-%{nssdb_commit}.tar.gz
Source19:	https://github.com/stackforge/puppet-openstack/archive/%{openstack_commit}/openstack-%{openstack_commit}.tar.gz
Source20:	https://github.com/radez/puppet-pacemaker/archive/%{pacemaker_commit}/pacemaker-%{pacemaker_commit}.tar.gz
Source21:	https://github.com/dprince/puppet-qpid/archive/%{qpid_commit}/qpid-%{qpid_commit}.tar.gz
Source22:	https://github.com/puppetlabs/puppetlabs-rabbitmq/archive/%{rabbitmq_commit}/rabbitmq-%{rabbitmq_commit}.tar.gz
Source23:	https://github.com/puppetlabs/puppetlabs-rsync/archive/%{rsync_commit}/rsync-%{rsync_commit}.tar.gz
Source24:	https://github.com/saz/puppet-ssh/archive/%{ssh_commit}/ssh-%{ssh_commit}.tar.gz
Source25:	https://github.com/nanliu/puppet-staging/archive/%{staging_commit}/staging-%{staging_commit}.tar.gz
Source26:	https://github.com/puppetlabs/puppetlabs-stdlib/archive/%{stdlib_commit}/stdlib-%{stdlib_commit}.tar.gz
Source27:	https://github.com/stackforge/puppet-swift/archive/%{swift_commit}/swift-%{swift_commit}.tar.gz
Source28:	https://github.com/puppetlabs/puppetlabs-sysctl/archive/%{sysctl_commit}/sysctl-%{sysctl_commit}.tar.gz
Source29:	https://github.com/stackforge/puppet-tempest/archive/%{tempest_commit}/tempest-%{tempest_commit}.tar.gz
Source30:	https://github.com/puppetlabs/puppetlabs-vcsrepo/archive/%{vcsrepo_commit}/vcsrepo-%{vcsrepo_commit}.tar.gz
Source31:	https://github.com/derekhiggins/puppet-vlan/archive/%{vlan_commit}/vlan-%{vlan_commit}.tar.gz
Source32:	https://github.com/stackforge/puppet-vswitch/archive/%{vswitch_commit}/vswitch-%{vswitch_commit}.tar.gz
Source33:	https://github.com/packstack/puppetlabs-xinetd/archive/%{xinetd_commit}/xinetd-%{xinetd_commit}.tar.gz

Patch0:     mariadb.patch
Patch1:     apache24.patch
Patch2:     compute_driver.patch
Patch3:     glance.patch
Patch4:     heat.patch
Patch5:     neutron.patch
Patch6:     openstack.patch
Patch7:     cinder.patch
Patch8:     keystone.patch
Patch9:     nova.patch
Patch10:    0001-Fix-network_vlan_ranges-parameter-for-OVS-plugin.patch
Patch11:    0002-Change-dhcp_lease_duration-to-Havana-default-of-8640.patch
Patch12:    0003-Do-not-create-symblic-link-for-cisco-plugin.patch
Patch13:    puppet-neutron-vlan_ranges.patch

BuildArch:      noarch


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
%setup -c -q -T -D -a 16
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

# puppetlabs-apache patches
cd %{_builddir}/%{name}-%{version}/puppetlabs-apache-%{apache_commit}
%patch1 -p1

# puppetlabs-mysql patches
cd %{_builddir}/%{name}-%{version}/puppetlabs-mysql-%{mysql_commit}
%patch0 -p1

# puppet-nova patches
cd %{_builddir}/%{name}-%{version}/puppet-nova-%{nova_commit}
%patch2 -p1

# puppet-glance patches
cd %{_builddir}/%{name}-%{version}/puppet-glance-%{glance_commit}
%patch3 -p1

# puppet-heat patches
cd %{_builddir}/%{name}-%{version}/puppet-heat-%{heat_commit}
%patch4 -p1

# puppet-neutron patches
cd %{_builddir}/%{name}-%{version}/puppet-neutron-%{neutron_commit}
%patch5 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

# puppet-openstack patches
cd %{_builddir}/%{name}-%{version}/puppet-openstack-%{openstack_commit}
%patch6 -p1

# puppet-cinder patches
cd %{_builddir}/%{name}-%{version}/puppet-cinder-%{cinder_commit}
%patch7 -p1

# puppet-keystone patches
cd %{_builddir}/%{name}-%{version}/puppet-keystone-%{keystone_commit}
%patch8 -p1

# puppet-nova patches
cd %{_builddir}/%{name}-%{version}/puppet-nova-%{nova_commit}
%patch9 -p1

find %{_builddir} -type f -name ".*" -exec rm {} +
find %{_builddir} -size 0 -exec rm {} +
find %{_builddir} \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find %{_builddir} \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find %{_builddir} \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} + -exec sed -i "/^#!/{d;q}" {} +


%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/
cp -r puppetlabs-apache-%{apache_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/apache
cp -r puppet-ceilometer-%{ceilometer_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/ceilometer
cp -r puppet-certmonger-%{certmonger_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/certmonger
cp -r puppet-cinder-%{cinder_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/cinder
cp -r puppetlabs-concat-%{concat_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/concat
cp -r puppetlabs-firewall-%{firewall_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/firewall
cp -r puppet-glance-%{glance_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/glance
cp -r puppet-openstack-storage-%{gluster_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/gluster
cp -r puppetlabs-haproxy-%{haproxy_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/haproxy
cp -r puppet-heat-%{heat_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/heat
cp -r puppet-horizon-%{horizon_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/horizon
cp -r puppetlabs-inifile-%{inifile_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/inifile
cp -r puppet-keystone-%{keystone_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/keystone
cp -r puppet-memcached-%{memcached_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/memcached
cp -r puppetlabs-mongodb-%{mongodb_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/mongodb
cp -r puppetlabs-mysql-%{mysql_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/mysql
cp -r puppet-neutron-%{neutron_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/neutron
cp -r puppet-nova-%{nova_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/nova
cp -r puppet-nssdb-%{nssdb_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/nssdb
cp -r puppet-openstack-%{openstack_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/openstack
cp -r puppet-pacemaker-%{pacemaker_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/pacemaker
cp -r puppet-qpid-%{qpid_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/qpid
cp -r puppetlabs-rabbitmq-%{rabbitmq_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/rabbitmq
cp -r puppetlabs-rsync-%{rsync_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/rsync
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
