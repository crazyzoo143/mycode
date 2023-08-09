---
- name: Tuesday Challenge
  hosts: planet express
  gather_facts: yes

  tasks:
    - name: create a directory
      file:
        dest: challenge
        state: directory

    - name: creating a file
      copy:
        dest: challenge/challengefile.txt
        content: "Success!"
















