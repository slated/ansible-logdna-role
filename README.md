[![Build Status](https://travis-ci.org/slated/ansible-logdna-role.svg?branch=master)](https://travis-ci.org/slated/ansible-logdna-role)

Role Name
=========

Install logdna_agent and add logfile, logdir

Requirements
------------
    molecule

Role Variables
--------------

    logdna_agent_install: true
    logdna_api_key: PUT_YOUR_KEY_HERE

Dependencies
------------

Example Playbook
----------------

    - hosts: servers
      - import_role:
          name: logdna
        vars:
            logdna_agent_install: true
            logdna_api_key: PUT_YOUR_KEY_HERE
