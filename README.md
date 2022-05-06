# DEPRECATED - This repository is no longer maintained

**Capabilities provided by this repository have migrated to the [ansible-middleware](https://github.com/ansible-middleware) project and specifically the [amq](https://github.com/ansible-middleware/amq) repository.**

# Ansible Red Hat AMQ Role [![Build Status](https://travis-ci.org/redhat-cop/jboss_amq.svg)](https://travis-ci.org/redhat-cop/jboss_amq)

A role to install Red Hat AMQ on CentOS, RHEL7 or RHEL8. Intended to be used with [JBoss Middleware Playbooks](https://github.com/redhat-cop/ansible-middleware-playbooks)

## Transfer Method

This role supports a few different mechanism for transferring the product zip files to the target host. These are documented on [the main playbooks README](https://github.com/redhat-cop/ansible-middleware-playbooks), as the methods are supported across a variety of roles.

## Dependencies

- ansible 2.5
- java
- unzip
- jmespath

Our playbooks provide these dependencies in a [common role](https://github.com/redhat-cop/ansible-role-jboss-common), but this there is no explicitly ansible dependency to allow end users more options. Passwords are on the defaults/main.yml and require "" if using special characters.

## Inventory

This role requires the following vars in the inventory file

```txt
amq-host1
amq-host2
amq-host3
amq-host4
```

## Example Playbooks

- [Red Hat AMQ 7.1 on RHEL 7](https://github.com/redhat-cop/ansible-middleware-playbooks/blob/master/amq7.1-rhel7.yml)
- [Red Hat AMQ 7.2 on RHEL 7](https://github.com/redhat-cop/ansible-middleware-playbooks/blob/master/amq7.2-rhel7.yml)
- [Red Hat AMQ 7.6 on RHEL 8](https://github.com/redhat-cop/ansible-middleware-playbooks/blob/master/amq7.6-rhel8.yml)

## Requirements License

[LICENSE](./LICENSE)

## Authors Information

- [Andrew Block](https://github.com/sabre1041)
- [Christian Polizzi](https://github.com/cpolizzi)
- [Jonathan Lozada De La Matta](https://github.com/jlozadad)
