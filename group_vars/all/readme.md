You can create an Ansible Vault encrypted file to store sensitive variables by using the `ansible-vault` command.

```console
ansible-vault create group_vars/all/vault.yml
```

You can edit this file like this:

```console
ansible-vault edit group_vars/all/vault.yml
```

With `EDITOR='code --wait'`, you can set VS Code to be the editor for Ansible vault files:

```console
EDITOR='code --wait' ansible-vault edit group_vars/all/vault.yml
```

The structure of this Ansible Vault file should be like in [`0_example_vars.yml`](0_example_vars.yml).

As long as your vault file is named alphabetically *after* `0_example_vars.yml`, it will override the variables defined in `0_example_vars.yml`.

See [Understanding variable precedence](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#understanding-variable-precedence) in the Ansible documentation for more information:

> Within any section, redefining a var overrides the previous instance. If multiple groups have the same variable, the last one loaded wins. If you define a variable twice in a play's `vars:` section, the second one wins.
