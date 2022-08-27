# Provision with Ansible

`ansible-pull -U https://github.com/pavelzw/ansible-provision.git -C test -i inventory --full --ask-become-pass playbook.yml`

`ansible-playbook playbook.yml -i inventory --ask-become-pass`