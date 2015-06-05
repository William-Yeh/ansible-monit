
williamyeh.monit for Ansible Galaxy
============

[![Circle CI](https://circleci.com/gh/William-Yeh/ansible-monit.svg?style=shield)](https://circleci.com/gh/William-Yeh/ansible-monit) [![Build Status](https://travis-ci.org/William-Yeh/ansible-monit.svg?branch=master)](https://travis-ci.org/William-Yeh/ansible-monit)



## Summary

Role name in Ansible Galaxy: **[williamyeh.monit](https://galaxy.ansible.com/list#/roles/3955)**

This Ansible role has the following features for Monit:

 - Install latest version.
 - Handlers for restart/reload/stop events;
 - Bare bone configuration (*real* configuration should be left to user's template files; see **Usage** section below).




## Role Variables

### Mandatory variables

None.




### Optional variables

User-installable configuration files (by Ansible's template system):


```yaml
# main conf template to be installed to "/etc/monitrc";
# relative to `playbook_dir`
monit_conf_main


# other conf templates to be installed to "{{ monit_config_path }}" directory;
# dict fields:
#   - key: memo for this conf
#   - value:
#     - src:  template file relative to `playbook_dir`
#     - dest: target file relative to `{{ monit_config_path }}/`
monit_conf_others
```


User-configurable defaults:


```yaml
# HTTP port for status report
monit_port:                 2812

# seconds for service checking
monit_interval_in_seconds:  60




# directory for the "monit" executable file
monit_install_path:      /usr/bin

# directory for per-application configuration
monit_config_path:       /etc/monit.d

# directory for runtime database
monit_db_path:           /var/lib/monit


# directory for temporary installation files
monit_download_path:     /tmp

# clean tarball when done?
monit_clean_tarball:     true



# use `service` command to start/restart monit daemon?
monit_use_service:  True
```


## Handlers

- `restart monit`

- `reload monit`

- `stop monit`



## Usage


### Step 1: add role

Add role name `williamyeh.monit` to your playbook file.


### Step 2: add variables

Set vars in your playbook file, if necessary.

Simple example:

```yaml
---
# file: simple-playbook.yml

- hosts: all
  sudo: True
  roles:
    - williamyeh.monit

  vars:
    monit_interval_in_seconds: 15
```


### Step 3: copy user's config files, if necessary


More practical example:

```yaml
---
# file: complex-playbook.yml

- hosts: all
  sudo: True
  roles:
    - williamyeh.monit

  vars:
    monit_conf_main: "templates/monitrc.j2"

    monit_conf_others:
      conf_template_for_app_1:
        src: "templates/app-1.j2"
        dest: app-1
      conf_template_for_app_2:
        src: "templates/app-2.j2"
        dest: app-2
```


## Dependencies

None.


## License

Apache License V2.0. See the [LICENSE file](LICENSE) for details.


## History

Rewritten from my pre-Galaxy version: [server-config-template](https://github.com/William-Yeh/server-config-template).
