import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_logdna_agent_is_existed(host):
    logdna_agent = host.file("/usr/bin/logdna-agent")
    assert logdna_agent.exists


def test_logdna_config_is_existed(host):
    logdna_config = host.file("/etc/logdna.conf")
    assert logdna_config.exists
