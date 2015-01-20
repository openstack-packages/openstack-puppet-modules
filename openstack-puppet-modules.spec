
Name:           openstack-puppet-modules
Version:        2014.2.9
Release:        2%{?dist}
Summary:        Collection of Puppet modules for OpenStack deployment
License:        ASL 2.0 and GPLv2 and GPLv3

URL:            https://github.com/redhat-openstack

Source0:        https://github.com/redhat-openstack/openstack-puppet-modules/archive/%{version}.tar.gz

Patch0001: 0001-horizon-Change-default-documentation-URL.patch
Patch0002: 0002-rabbitmq-Don-t-manage-RabbitMQ-repos.patch
Patch0003: 0003-openstack-Set-default-charset-to-utf8.patch
Patch0004: 0004-heat-Implement-Keystone-domain-creation.patch
Patch0005: 0005-keystone-Add-manage_service-feature.patch
Patch0006: 0006-Configure-OVS-mechanism-agent-configs-in-its-config-.patch
Patch0007: 0007-Add-manage_service-feature.patch
Patch0008: 0008-Fix-against-mongodb-2.6.5-from-epel.patch
Patch0009: 0009-Fix-support-for-Fedora-Rawhide.patch
Patch0010: 0010-Adds-filtering-for-BONDING-LACP.patch
Patch0011: 0011-JSON-was-invalid.patch
Patch0012: 0012-Configure-auth-via-conf-file-not-paste-file.patch
Patch0013: 0013-Set-control_exchange-in-the-main-config-file.patch
Patch0014: 0014-Support-Neutron.patch
Patch0015: 0015-Add-Ironic-support-into-nova-puppet-modules.patch
Patch0016: 0016-Fix-Ironic-modules-so-services-properly-run.patch
Patch0017: 0017-Deprecate-support-for-Fedora-18.patch
Patch0018: 0018-Automates-generation-of-NFS-config-file.patch

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
%patch0009 -p1
%patch0010 -p1
%patch0011 -p1
%patch0012 -p1
%patch0013 -p1
%patch0014 -p1
%patch0015 -p1
%patch0016 -p1
%patch0017 -p1
%patch0018 -p1

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
cp -r aviator %{buildroot}/%{_datadir}/openstack-puppet/modules/aviator
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
cp -r ipa %{buildroot}/%{_datadir}/openstack-puppet/modules/ipa
cp -r ironic %{buildroot}/%{_datadir}/openstack-puppet/modules/ironic
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
cp -r ntp %{buildroot}/%{_datadir}/openstack-puppet/modules/ntp
cp -r openstack %{buildroot}/%{_datadir}/openstack-puppet/modules/openstack
cp -r openstacklib %{buildroot}/%{_datadir}/openstack-puppet/modules/openstacklib
cp -r pacemaker %{buildroot}/%{_datadir}/openstack-puppet/modules/pacemaker
cp -r puppet %{buildroot}/%{_datadir}/openstack-puppet/modules/puppet
cp -r qpid %{buildroot}/%{_datadir}/openstack-puppet/modules/qpid
cp -r rabbitmq %{buildroot}/%{_datadir}/openstack-puppet/modules/rabbitmq
cp -r redis %{buildroot}/%{_datadir}/openstack-puppet/modules/redis
cp -r rsync %{buildroot}/%{_datadir}/openstack-puppet/modules/rsync
cp -r sahara %{buildroot}/%{_datadir}/openstack-puppet/modules/sahara
cp -r ssh %{buildroot}/%{_datadir}/openstack-puppet/modules/ssh
cp -r staging %{buildroot}/%{_datadir}/openstack-puppet/modules/staging
cp -r stdlib %{buildroot}/%{_datadir}/openstack-puppet/modules/stdlib
cp -r swift %{buildroot}/%{_datadir}/openstack-puppet/modules/swift
cp -r sysctl %{buildroot}/%{_datadir}/openstack-puppet/modules/sysctl
cp -r tempest %{buildroot}/%{_datadir}/openstack-puppet/modules/tempest
cp -r trove %{buildroot}/%{_datadir}/openstack-puppet/modules/trove
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
* Tue Jan 20 2015 Gael Chamoulaud <gchamoul@redhat.com> 2014.2.9-2
- Update to upstream 2014.2.9

* Mon Jan 19 2015 Gael Chamoulaud <gchamoul@redhat.com> - 2014.2.9-1
- Updated to release 2014.2.9
- ironic       9aab12eab342b313881de6af9cd0d4e7c7dcdcd6
- keystone     b65ddba19f5d89fe13bd0264e988ef702ba2b5c9
- glance       9fb3db4a693b6839c2caa45df4cd37f9c21451de
- cinder       f6af237764cca3319594e731b6b808a7c557cd4c
- redis        d72af9ab3c2911b6dc18c5cc12e700630ebdcfb2

* Fri Dec 19 2014 Lukas Bezdicka <lbezdick@redhat.com> - 2014.2.8-1
- Updated to release 2014.2.8
- ceilometer   953ce5032cb332bf8a15e78358ee8af6f14dd7f0
- keystone     71a9df884b7a81bf86b6e897c16171bf556f1ea4
- n1k-vsm      6ac71df4aa2bf806e35b83bd18ae9ea6b5605bc0
- neutron      c3dc52023dfdf7649080c1b5bc5eae3b43991db1
- nova         181991927131206d4ea59a679e8108e36dc86c77
- redis        f4ffa1b907281472c8572c7dbcee8d2f454f3e27
- trove        2ef93e8e90978915d166ed21fd53dab67f820fe7
- vswitch      a36332da0ddb9d419e1d3f9d170058284b144f06
- Configure-auth-via-conf-file-not-paste-file.patch
- Set-control_exchange-in-the-main-config-file.patch
- Support-Neutron.patch
- Add-Ironic-support-into-nova-puppet-modules.patch
- Fix-Ironic-modules-so-services-properly-run.patch
- Deprecate-support-for-Fedora-18.patch


* Fri Dec 12 2014 Lukas Bezdicka <lbezdick@redhat.com> 2014.2.7-3
- JSON was invalid

* Fri Dec 12 2014 Lukas Bezdicka <lbezdick@redhat.com> 2014.2.7-2
- Adds filtering for BONDING (LACP)
- Fixed issue with vlan on redhat provider

* Thu Dec 11 2014 Lukas Bezdicka <lbezdick@redhat.com> - 2014.2.7-1
- Fix support for Fedora Rawhide (rhbz#1170646)
- Updated to release 2014.2.7
- apache       1417312b493ea79f88f22cc8b961d8db08cb9273
- aviator      d308a263318399f0de7fd760826f8b98b2b59aba
- ceilometer   ee2f3cd4498b2ef3a6633991206b7185c1d32897
- horizon      168c206dfefa35abec48d7bce33ed469bf98cefb
- keystone     821cc4ada1f50b5a6c6244cd5c689a467d06d736
- openstacklib 999f7849a3e0653f46f7336ee0fa9c2e38630b7b
- sahara       66301097ee42840831f8c8c7cd0482e3e2325df5

* Tue Dec 02 2014 Lukas Bezdicka <lbezdick@redhat.com> 2014.2.6-3
- Updated to release 2014.2.6
- mongodb      fe562b86f388a6d107bb1f3cb3b32a3978f59c2a
- Fix against mongodb 2.6.5 from epel (rhbz#1167888)

* Tue Nov 25 2014 Lukas Bezdicka <lbezdick@redhat.com> - 2014.2.5-1
- Update to upstream 2014.2.5
- apache       769ff363a8a3c51e24f63a2494217d2d029289c6
- ceilometer   741e89ae5b59e6284d677dd1c3cdf4154902a378
- certmonger   3f86b9973fc30c14a066b0f215023d5f1398b874
- cinder       1ee8a6cab39da6beebf7a0b39207f0002368196f
- common       2c0ed2844c606fd806bde0c02e47e79c88fab4a9
- concat       644fb1b6dc8b64accc4d1208d6127b79a08a38b7
- firewall     6b308177c3d279083078955942969c92b145eba0
- galera       f7d4110886b643eb63dc5c347a0e8a06b09642e7
- glance       a243f89a52f7dd2dc16b36d1c9b79ec1616c6596
- gluster      6c962083d8b100dcaeb6f11dbe61e6071f3d13f0
- haproxy      f381510e940ee11feb044c1c728ba2e5af807c79
- heat         b1e9e9bd48c3da15be69c0797fb05e7ce0f6698f
- horizon      353c372d582167d5635b1b2ee9474cf6822db032
- inifile      fe9b0d5229ea37179a08c4b49239da9bc950acd1
- ipa          08e51e96ac2c9265499deec3485e396b792587d3
- keystone     38518cbcb3ef8ad3bb068730a21d790b27a29b74
- memcached    49dbf102fb6eee90297b2ed6a1fa463a8c5ccee7
- module-data  159fc5e0e21ce9df96c777f0064b5eca88e29cae
- mongodb      0518f864afcce2ebb79f1f2edab5de323c811af7
- mysql        40dd1805886aee56dc02860565f161c6e3b4c7e5
- n1k-vsm      69ff094069506f98431182c6097b3b6b9ea6fdb9
- nagios       56a1eee350c4600bb12e017d64238fb3f876abd4
- neutron      67abde86d53969329bce37725627c2c661e49765
- nova         181991927131206d4ea59a679e8108e36dc86c77
- nssdb        b3799a9a7c62c3b5b7968f9860220a885b45fb8a
- ntp          8f697e32bc279b36ada752273e6c788716b95315
- openstack    d81d2d86280d5739cc896a48b68d7309e765047a
- openstacklib e64e9c2a44833b25b602138b53a3187db49eaef8
- pacemaker    0ed9ee8a29c0f27e86727d415b39d2715332df7d
- puppet       bd467cae15eba9ca44274034d2593b0eaf30518d
- qpid         9ffb2788c536f1694980e07a43e8133ff85fa28c
- rabbitmq     4832bd61b5b1bfea7c9cc985508e65cd10081652
- redis        31ecbcace3cacf26ad85d90abc2409da8973e788
- rsync        357d51f3a6a22bc3da842736176c3510e507b4fb
- sahara       6b696cffcba6692975dbcfee144e81b6e90e5ecf
- ssh          d6571f8c43ac55d20a6afd8a8ce3f86ac4b0d7a4
- staging      887275d8fb20e148c6f9eb327f1f6c8ea5ee280f
- stdlib       62e8c1d76902e6f22cb9f7b3abd43e757b4130a3
- swift        68a9e8eecba4a280ea1ec18fba67069a8c7dfce4
- sysctl       c4486acc2d66de857dbccd8b4b945ea803226705
- tempest      7a3369949fc8af41e190dd8115391354a7575ecb
- vcsrepo      6f7507a2a48ff0a58c7db026760a2eb84e382a77
- vlan         c937de75c28e63fba8d8738ad6a5f2ede517e53d
- vswitch      51fd30c22b79d927fb0329e6e2b58fe67217ecee
- xinetd       6b02de8d4f30a819eb404048e4258e3a5e8023c8

* Wed Nov 12 2014 Lukas Bezdicka <lbezdick@redhat.com> 2014.2.4-1
- Update to upstream 2014.2.4

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
