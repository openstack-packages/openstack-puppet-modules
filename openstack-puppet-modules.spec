Name:           openstack-puppet-modules
Epoch:          1
Version:        7.0.1
Release:        1%{?dist}
Summary:        Collection of Puppet modules for OpenStack deployment
License:        ASL 2.0 and GPLv2 and GPLv3

URL:            https://github.com/redhat-openstack

# 2015.2.0 https://github.com/redhat-openstack/openstack-puppet-modules/commit/bf329c9115ea08c3f1cfc254fba058777fedd3c4
# timestamp 2015-10-09 03:14 UTC
Source0:        https://github.com/redhat-openstack/%{name}/archive/%{version}.tar.gz

Patch0001: 0001-Change-default-documentation-URL.patch
Patch0002: 0002-Fix-support-for-puppet-4.patch
Patch0003: 0003-Rabbitmq-set-repos_ensure-to-false.patch
Patch0004: 0004-Setup-SELinux-booleans-if-running-in-httpd.patch
Patch0005: 0005-Remove-trove-ubuntu-package-hack.patch
Patch0006: 0006-Install-service-packages-on-api-nodes.patch
Patch0007: 0007-Remove-installation-of-pm-utils.patch
Patch0008: 0008-Explicitly-say-that-ovs_redhat-parent-is-ovs.patch
Patch0009: 0009-Add-support-for-swift-object-expirer-service.patch
Patch0010: 0010-Simplify-rpc_backend-parameter.patch
Patch0011: 0011-Drop-nova_admin_tenant_id_setter.patch

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
%patch0007 -p1
%patch0008 -p1
%patch0009 -p1
%patch0010 -p1
%patch0011 -p1

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
* Tue Oct 20 2015 Lukas Bezdicka <lbezdick@redhat.com> 1:7.0.1-1
- Update to upstream 7.0.1

* Tue Oct 13 2015 Lukas Bezdicka <lbezdick@redhat.com> 7.0.0-1
- Update to upstream 7.0.0

* Sat Oct 10 2015 Alan Pevec <alan.pevec@redhat.com> 2015.2.0-0.1
- OpenStack Liberty RC
