import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('pkg', [
  'unzip',
  'java-1.8.0-openjdk-devel',
  'python2-pip'
])
def test_pkg(host, pkg):
    package = host.package(pkg)

    assert package.is_installed


@pytest.mark.parametrize('service', [
  'jboss-amq',
])
def test_systemd(host, service):
    systemd_service = host.service(service)

    assert systemd_service.is_enabled
    assert systemd_service.is_running


@pytest.mark.parametrize('directory', [
  '/opt/jboss/amq/brokers',
])
def test_host_directories(host, directory):
    host_directory = host.file(directory)

    assert host_directory.exists
    assert host_directory.is_directory
