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
- apache       455f7c82cc27298a49135f026d36a444d33af679
- aviator      9a3b74b0dbb655a3afcbc8bdee442f2143420b72
- ceilometer   69af03e1665e5eca2ef988ccaacf3623f7ace2af
- ceph         b6ab15b47c81d7694fdcfd75d8f2e0a0481ca40c
- certmonger   3f86b9973fc30c14a066b0f215023d5f1398b874
- cinder       d6ccce6554e85ee50d926bbc413c1a1ea2ddffbf
- common       165e2adc3ab559597f461e6eae3eb004967070f9
- concat       52d0f1d6809c9f1d8453f9e3ca10d792e67acc89
- corosync     8d725aea7a9d91d861929851a9da8da1e3519b21
- firewall     667a9f67a7ce8eb343c132feb1e00c6e2132d38a
- galera       92463ad0567c066796b7fac4a1466e6a60621f6c
- glance       0db42a6a60bd4952f795d61ea26ed299e8c35bc8
- gluster      3cefb34593f37c9c2c2e93fcb88bee07e335045e
- gnocchi      4ebe8a6b83a5c3a55f7ea9f61991917054c6b013
- haproxy      d89fad1c32cba514298c7eb2b82705a997f472f4
- heat         a974b0651c852fb693919b92bf3da648b41a156b
- horizon      e0fd95a693db6f1b2196c6497f999164b292d369
- inifile      3bfcceb17f35f53f58a1f018a388b74178c661f3
- ipa          4e634b31633bc956341e20980233107a6d5dc1f9
- ironic       0c859d8fc9a2fc790f20013e8668f520e01ef3a2
- keepalived   24d523691b3581d4d0f662ffd10f1458014a9829
- keystone     edf8c3e1753b5ad0eaf982f5932ce61c55a987bd
- manila       8c8b02b6f294a68544df96180b4c2dcfe3bdddf0
- memcached    e0e9c024dc4ed6f049d68ad3f2cc3ee9666e7277
- module-collectd 6a9f9492af6a3a59b74f043ce6bb8227909224b2
- module-data  0eead7f411f404b0a9a73bb161aac46c9fbe3219
- mongodb      1e6be5d3b0b920be9fee9873ab49609766d93e46
- mysql        030556162ef1b2a06629dad318fdb89925f737ea
- n1k_vsm      2a42723f5a9d7dbfa00edf944ac5dec2bff6d9ea
- nagios       56a1eee350c4600bb12e017d64238fb3f876abd4
- neutron      b29ee6f706bf7371f69b831f99727396ddb77cad
- nova         3cba5197cc5c4e7807d5c97d374fb175b47878c7
- nssdb        2e163a21fb80d828afede2d4be6214f1171c4887
- ntp          53570725fa40ae5bd7368cbaf47b549966d030f2
- openstack_extras 610313ca08ffc50c44b6d41000d25bd0274d57f0
- openstacklib 54f3a0be5c6a7893d179206e99ed0cd47a0d9d86
- pacemaker    52acfd9c31e0801cedf970929851d4bece5cf79b
- puppet       97b41d9fdadbe98f965d515b55c35a65da596ef2
- qpid         9ffb2788c536f1694980e07a43e8133ff85fa28c
- rabbitmq     5d71d50aadfa423b69fe2dfe6171a8ba25d8c0b2
- redis        20baca47f04586a2089bdcf64db1d6c7bfe014ec
- remote       35cc5571593d21408d625bd8ee35217345ec502a
- rsync        f8081918a503a7301772c93373eb70b90d399538
- sahara       704d1d812e89b88a49a8d3cf8f9502f47267b256
- snmp         64f1a6976830bb4e96176a7296e8d14f65df0cac
- ssh          5afa7d6cc30c129af66612928f3ab51f89ad7a26
- staging      a71e7d6261616fdba9f5c9109c4ad41c120d91be
- stdlib       35c77c7a7a3e9620b79833ba95ed0618bdc9492f
- swift        08f61073119f25033bf1bdc7e7c18cade837cc0c
- sysctl       c4486acc2d66de857dbccd8b4b945ea803226705
- tempest      b3d764809c1e20e4f20022c518b662ebe7d6b663
- timezone     734918982a512f51a3f1855396d2d7da3f37f53c
- tripleo      a388f84654701f5d6604e0833a6a8fe1b90fcfdd
- trove        19731ad8f1598106226617b7bd66a1ee1fd67ac2
- tuskar       8c28b3a40f2dba6f70dfa1cad13f2709173bc213
- vcsrepo      4cc3383f3e22edb31a03a3dad7817734529781ee
- vlan         c937de75c28e63fba8d8738ad6a5f2ede517e53d
- vswitch      58e807a42cf62890405c51d85a0f84b196faed60
- xinetd       902825112b383dc837acfdd326457f5ba2c5921b

* Mon May 11 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 2015.1.0-2
- Add patch to fix TripleO support

* Thu Apr 30 2015 Alan Pevec <alan.pevec@redhat.com> 2015.1.0-1
- OpenStack Kilo release
