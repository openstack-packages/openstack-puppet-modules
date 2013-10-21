 
%global glance_commit    850bca13c71e069dfca7dff3b633ca7f746ead61
%global neutron_commit   b6b50a97e060261ce66817ba8255ae4d710e0009
%global keystone_commit  6f54428601c673baba4e70049ecbc798bd9bad64
%global nova_commit      84303ef81cd17ce62cc991e019eb86c4373baa62
%global swift_commit     ee4a9d48599bce332d0d7bdf4f8c0bbb6d9c6f2e
%global cinder_commit    fa28def3fb63d1ca29b4030d229afaa2c8d3b017
%global horizon_commit   1dc40b2d4a8d27c5d0af6b7ad52efdc9b27d525d
%global tempest_commit   93b691f7cbfa67599ee199bd79baf82243c17568
%global openstack_commit a5f9a18c6819f39801bcee5f080e1ec27d30b718
%global rsync_commit     357d51f3a6a22bc3da842736176c3510e507b4fb
%global stdlib_commit    4d2558f383e18bbe322dd0feb073555491216ab4
%global sysctl_commit    c4486acc2d66de857dbccd8b4b945ea803226705
%global haproxy_commit   f381510e940ee11feb044c1c728ba2e5af807c79
%global inifile_commit   fe9b0d5229ea37179a08c4b49239da9bc950acd1
%global vcsrepo_commit   6f7507a2a48ff0a58c7db026760a2eb84e382a77
%global xinetd_commit    fa8edb134b538b9a929f7e85e8bf9667f9acab8b
%global apache_commit    fbab9a521dbd27a6cd77476327636003261d553c
%global mysql_commit     8a4f8c76e662b008bb30ce723a8b30ef494b21a1
%global vswitch_commit   6e6b9462695e383423462d1321b1c0865524a408
%global qpid_commit      fa4ec7ddb17f7c6e5a4b3dd63f4fadbe6b61c30d
%global vlan_commit      c937de75c28e63fba8d8738ad6a5f2ede517e53d
%global ssh_commit       d6571f8c43ac55d20a6afd8a8ce3f86ac4b0d7a4
%global memcached_commit 49dbf102fb6eee90297b2ed6a1fa463a8c5ccee7
%global firewall_commit  6106fb5404480ac7c883bddd503e0fc9f2698750
%global concat_commit    031bf261289dcbb32e63b053ed5b3a82117698c0


Name:           openstack-puppet-modules
Version:        2013.2
Release:        3%{?dist}
Summary:        Puppet modules used to deploy OpenStack
License:        ASL 2.0 and GPLv2 and GPLv3

URL:            https://github.com/redhat-openstack

Source0:        https://github.com/stackforge/puppet-glance/archive/%{glance_commit}/puppet-glance-%{glance_commit}.tar.gz
Source1:        https://github.com/stackforge/puppet-neutron/archive/%{neutron_commit}/puppet-neutron-%{neutron_commit}.tar.gz
Source2:        https://github.com/stackforge/puppet-keystone/archive/%{keystone_commit}/puppet-keystone-%{keystone_commit}.tar.gz
Source3:        https://github.com/stackforge/puppet-nova/archive/%{nova_commit}/puppet-nova-%{nova_commit}.tar.gz
Source4:        https://github.com/stackforge/puppet-swift/archive/%{swift_commit}/puppet-swift-%{swift_commit}.tar.gz
Source5:        https://github.com/stackforge/puppet-cinder/archive/%{cinder_commit}/puppet-cinder-%{cinder_commit}.tar.gz
Source6:        https://github.com/stackforge/puppet-horizon/archive/%{horizon_commit}/puppet-horizon-%{horizon_commit}.tar.gz
Source7:        https://github.com/stackforge/puppet-openstack/archive/%{openstack_commit}/puppet-openstack-%{openstack_commit}.tar.gz
Source8:        https://github.com/stackforge/puppet-tempest/archive/%{tempest_commit}/puppet-tempest-%{tempest_commit}.tar.gz
Source9:        https://github.com/puppetlabs/puppetlabs-rsync/archive/%{rsync_commit}/puppetlabs-rsync-%{rsync_commit}.tar.gz
Source10:       https://github.com/puppetlabs/puppetlabs-stdlib/archive/%{stdlib_commit}/puppetlabs-stdlib-%{stdlib_commit}.tar.gz
Source11:       https://github.com/puppetlabs/puppetlabs-sysctl/archive/%{sysctl_commit}/puppetlabs-sysctl-%{sysctl_commit}.tar.gz
Source12:       https://github.com/puppetlabs/puppetlabs-haproxy/archive/%{haproxy_commit}/puppetlabs-haproxy-%{haproxy_commit}.tar.gz
Source13:       https://github.com/puppetlabs/puppetlabs-inifile/archive/%{inifile_commit}/puppetlabs-inifile-%{inifile_commit}.tar.gz
Source14:       https://github.com/puppetlabs/puppetlabs-vcsrepo/archive/%{vcsrepo_commit}/puppetlabs-vcsrepo-%{vcsrepo_commit}.tar.gz
Source15:       https://github.com/packstack/puppetlabs-xinetd/archive/%{xinetd_commit}/puppetlabs-xinetd-%{xinetd_commit}.tar.gz
Source16:       https://github.com/packstack/puppetlabs-apache/archive/%{apache_commit}/puppetlabs-apache-%{apache_commit}.tar.gz
Source17:       https://github.com/packstack/puppetlabs-mysql/archive/%{mysql_commit}/puppetlabs-mysql-%{mysql_commit}.tar.gz
Source18:       https://github.com/packstack/puppet-vswitch/archive/%{vswitch_commit}/puppet-vswitch-%{vswitch_commit}.tar.gz
Source19:       https://github.com/packstack/puppet-qpid/archive/%{qpid_commit}/puppet-qpid-%{qpid_commit}.tar.gz
Source20:       https://github.com/derekhiggins/puppet-vlan/archive/%{vlan_commit}/puppet-vlan-%{vlan_commit}.tar.gz
Source21:       https://github.com/saz/puppet-ssh/archive/%{ssh_commit}/puppet-ssh-%{ssh_commit}.tar.gz
Source22:       https://github.com/saz/puppet-memcached/archive/%{memcached_commit}/puppet-memcached-%{memcached_commit}.tar.gz
Source23:       https://github.com/lstanden/puppetlabs-firewall/archive/%{firewall_commit}/puppetlabs-firewall-%{firewall_commit}.tar.gz
Source24:       https://github.com/ripienaar/puppet-concat/archive/%{concat_commit}/puppet-concat-%{concat_commit}.tar.gz


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

find %{_builddir} -type f -name ".*" -exec rm {} +
find %{_builddir} -size 0 -exec rm {} +
find %{_builddir} \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find %{_builddir} \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find %{_builddir} \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} + -exec sed -i "/^#!/{d;q}" {} +


%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/
cp -r puppet-glance-%{glance_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/glance
cp -r puppet-neutron-%{neutron_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/neutron
cp -r puppet-keystone-%{keystone_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/keystone
cp -r puppet-nova-%{nova_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/nova
cp -r puppet-swift-%{swift_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/swift
cp -r puppet-cinder-%{cinder_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/cinder
cp -r puppet-horizon-%{horizon_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/horizon
cp -r puppet-tempest-%{tempest_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/tempest
cp -r puppet-openstack-%{openstack_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/openstack
cp -r puppetlabs-rsync-%{rsync_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/rsync
cp -r puppetlabs-stdlib-%{stdlib_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/stdlib
cp -r puppetlabs-sysctl-%{sysctl_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/sysctl
cp -r puppetlabs-haproxy-%{haproxy_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/haproxy
cp -r puppetlabs-inifile-%{inifile_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/inifile
cp -r puppetlabs-vcsrepo-%{vcsrepo_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/vcsrepo
cp -r puppetlabs-xinetd-%{xinetd_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/xinetd
cp -r puppetlabs-apache-%{apache_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/apache
cp -r puppetlabs-mysql-%{mysql_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/mysql
cp -r puppet-vswitch-%{vswitch_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/vswitch
cp -r puppet-qpid-%{qpid_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/qpid
cp -r puppet-vlan-%{vlan_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/vlan
cp -r puppet-ssh-%{ssh_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/ssh
cp -r puppet-memcached-%{memcached_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/memcached
cp -r puppetlabs-firewall-%{firewall_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/firewall
cp -r puppetlabs-concat-%{concat_commit} %{buildroot}/%{_datadir}/openstack-puppet/modules/concat
rm -f %{buildroot}/%{_datadir}/openstack-puppet/modules/nova/files/nova-novncproxy.init


%files
%{_datadir}/openstack-puppet/modules/*


%changelog
* Sun Oct 20 2013 Ryan O'Hara <rohara@redhat.com> - 2013.2-3
- Install modules to openstack-puppet directory.

* Mon Oct 14 2013 Ryan O'Hara <rohara@redhat.com> - 2013.2-2
- Package review changes.

* Wed Sep 04 2013 Ryan O'Hara <rohara@redhat.com> - 2013.2-1
- Initial spec file.
