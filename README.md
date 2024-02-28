Role Name
=========

This role install victoriametrics utilities on the target machine but doesen't install the service (WIP)

- vmagent-prod
- vmalert-prod
- vmalert-tool-prod
- vmauth-prod
- vmbackup-prod
- vmctl-prod
- vmrestore-prod

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
