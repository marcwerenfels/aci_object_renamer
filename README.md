# ACI Object renamer

This tool is to rename objects in ACI like EPG or BD objects.

## Folder Structure
Currently only the ansible folder content is usable. Terraform is not a good tool to use with brownfield approaches.
So directly go to ansible/.

## Prerequisits
You need to have ansible installed https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html
<br/>
You need to have collection installed:
```bas
ansible-galaxy collection install cisco.aci
```
## Usage
- Clone this repo:
    - chmod 764 ansible/initialize.sh
    - run ./initialize.sh (only creates two folders list & raw)
    - next...
```bash
ansible-playbook collector.yml
```