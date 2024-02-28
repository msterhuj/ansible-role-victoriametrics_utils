Role Name
=========

This role install victoriametrics utilities on the target machine.

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
