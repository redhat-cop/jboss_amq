Ansible JBoss AMQ Role [![Build Status](https://travis-ci.org/redhat-cop/jboss_amq.svg)](https://travis-ci.org/rhtconsulting/jboss_amq)
=================

A role to install JBoss AMQ on RHEL7. Intended to be used with [JBoss Middleware Playbooks](https://github.com/redhat-cop/ansible-middleware-playbooks)

Transfer Method
------------

This role supports a few different mechanism for transferring the product zip files to the target host. These are documented on [the main playbooks README](https://github.com/redhat-cop/ansible-middleware-playbooks), as the methods are supported across a variety of roles.


Dependencies
------------

- ansible 2.5
- java
- unzip
- jmespath

Our playbooks provide these dependencies in a [common role](https://github.com/redhat-cop/ansible-middleware-playbooks/tree/master/roles/common), but this there is no explicitly ansible dependency to allow end users more options. Passwords are on the defaults/main.yml and require "" if using special characters.
Inventory
---------

This role requires the following vars in the inventory file

```
amq-host1    amq_broker_name=broker-master
amq-host2    amq_broker_name=broker-backup1    amq_broker_slave=True
amq-host3    amq_broker_name=broker-backup2    amq_broker_slave=True
amq-host4    amq_broker_name=broker-backup3    amq_broker_slave=True
```

Example Playbooks
----------------

- [JBoss AMQ 7.2 on RHEL 7](https://github.com/redhat-cop/ansible-middleware-playbooks/blob/master/amq7.2-rhel7.yml)

Requirements
License
-------

[LICENSE](./LICENSE)

Authors Information
------------------

* [Andrew Block](https://github.com/sabre1041)
* [Christian Polizzi](https://github.com/cpolizzi)
* [Jonathan Lozada De La Matta](https://github.com/jlozadad)
