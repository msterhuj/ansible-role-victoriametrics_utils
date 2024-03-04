Victoriametrics Utils
=========

This role install victoriametrics utilities on the target machine

- vmagent-prod (service and config ready)
- vmalert-prod WIP
- vmalert-tool-prod (its just a binary tools)
- vmauth-prod (service and config ready)
- vmbackup-prod (its just a binary tools)
- vmctl-prod (its just a binary tools)
- vmrestore-prod (its just a binary tools)

> By default this role will install every binary but you can change this by setting the variables in the `defaults/main.yml` to select which binaries you want to install.

Requirements
------------

You need to enable the gathering of facts in your playbook.

Role Variables
--------------

Variable can be found in `defaults/main.yml` and are as follows: [Click here](defaults/main.yml)

Dependencies
------------

This role does not have any dependencies.

Example Playbook
----------------

    - hosts: victoriametrics-servers
      roles:
         - { role: msterhuj.victoriametrics_utils }

License
-------

GNU GPLv3

Author Information
------------------

msterhuj
