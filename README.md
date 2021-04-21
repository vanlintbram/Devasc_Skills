Task 1 -- GitHub Skills Test ***

-----------------Preparation

Installed the DEVASCVM

-----------------Implementation

First created a new repository on Github where i invited our instructor.
Then we did a "git init" on the newly created "Devasc_Skills" directory. Created a "README.md" file and added the remote repository through "git remote add origin https://github.com/vanlintbram/Devasc_Skills.git". Afterwards created a main branch "git branch -M main" and pushed the code: "git push -u origin main"

-----------------Troubleshooting

Tried to push the changes without having pointed the remote repository.

-----------------Verification

View changes on Github.
/
/
/
/
/
/
Task 2 -- Ansible Skills Test ***

-----------------Preparation

Install Ansible and create, ansible.cfg, hosts, and ios_status.yml.

-----------------Implementation

Make the ansible.cfg point to the hosts file. In hosts specify the CSR1000v host with username, password and ip-address. In ios_status.yml build the playbook based upon the provided URL.

-----------------Troubleshooting

Lenghty problem at 2.C: clear counters. Command worked on the cli but not through Ansible. First tried to put the command and prompt in extra ''. But that did not work. Eventually only using [confirm] from ''Clear "show interface" counters on all interfaces [confirm]'' did the trick.

NETCONF port didnt seem to work?

-----------------Verification


https://tinyimg.io/i/oVT2IY9.PNG
/
/
/
/
/
/
Task 4 -- REST API & RESTCONF

-----------------Preparation

Read the documentation provided.Checked if restconf was running on the local CSR1000v

-----------------Implementation

Tried the Sandbox for a long time but all my connections got refused. Eventually used the local CSR1000V. First tested all the commands in Postman. There was some refactoring to do and eventually got the commands correct for my installation. Afterwards implemented in a Python script.

-----------------Troubleshooting

Got a variety of errors back in the RESTCONF response, eg; "uri keypath not found". These got solved by changing the URI and not forgetting to check the headers in Postman.

-----------------Verification

https://tinyimg.io/i/FtCboYB.png

Task 5 – pyATS ***

-----------------Preparation

Created a venv

-----------------Implementation
Did a pip install pyats[full]. Created a testbed file for the CSR1kv. And than ran genie parse "show inventory" --testbed-file yaml/testbed.yml --devices CSR1kv

-----------------Troubleshooting

Except "Segmentation fault (core dumped)" No troubles encountered.

-----------------Verification

View verify_showInventory and next screenshot.
