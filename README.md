Task 1 -- GitHub Skills Test ***

!!!!!!!!Preparation

Installed the DEVASCVM

!!!!!!!!Implementation

First created a new repository on Github where i invited our instructor.
Then we did a "git init" on the newly created "Devasc_Skills" directory. Created a "README.md" file and added the remote repository through "git remote add origin https://github.com/vanlintbram/Devasc_Skills.git". Afterwards created a main branch "git branch -M main" and pushed the code: "git push -u origin main"

!!!!!!!!Troubleshooting

Tried to push the changes without having pointed the remote repository.

!!!!!!!!Verification

View changes on Github.






Task 2 -- Ansible Skills Test ***

!!!!!!!!Preparation

Install Ansible and create, ansible.cfg, hosts, and ios_status.yml.

!!!!!!!!Implementation

Make the ansible.cfg point to the hosts file. In hosts specify the CSR1000v host with username, password and ip-address. In ios_status.yml build the playbook based upon the provided URL.

!!!!!!!!Troubleshooting

Lenghty problem at 2.C: clear counters. Command worked on the cli but not through Ansible. First tried to put the command and prompt in extra ''. But that did not work. Eventually only using [confirm] from ''Clear "show interface" counters on all interfaces [confirm]'' did the trick.

NETCONF port didnt seem to work?

!!!!!!!!Verification



