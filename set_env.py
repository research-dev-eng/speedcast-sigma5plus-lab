import argparse

# This script sets the hosts.ini file for the Ansible inventory. The user will populate the file with the IPs of the hosts they want to use.
# The script will set the environment variable ANSIBLE_INVENTORY to the path of the hosts.ini file.
# Then the script will create the ssh key pair from the Ansible control node to the target hosts.