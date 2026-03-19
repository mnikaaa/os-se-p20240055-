# OS Lab 1 Submission

- **Student Name:** Thai Monika
- **Student ID:** p20240055

---

## Task 1: Operating System Identification

I use VMWare to virtualize linux noble 23.04 LTS

![Task 1](images/task1.png)

---

## Task 2: Essential Linux File and Directory Commands

I create, read, update, and delete linux shell commands on file a and b and output them into text files.

<img width="1846" height="487" alt="Screenshot from 2026-03-17 23-43-55" src="https://github.com/user-attachments/assets/40243ece-c81d-42f1-b396-f7291d8c7351" />



---

## Task 3: Package Management Using APT
remove saves the configuration while purge remove all instances including the configuration of the package

<!-- Insert your screenshot for Task 3 below: -->
<!-- SCREENSHOT REQUIREMENT: Show the output of ls -ld /etc/mc after running apt-get remove (folder still exists) versus after running apt-get purge (folder is gone). -->
<img width="1300" height="231" alt="Screenshot from 2026-03-17 23-46-44" src="https://github.com/user-attachments/assets/056465dd-8fd2-4bbf-ba83-846f3b296291" />

---

## Task 4: Programs vs Processes (Single Process)

I ran the process, in this case sleep with 120 seconds as arg, in the background using the ampersand symbol `&` and I checked the processes running on my system with ps and output them into the `task4_process_list.txt`

<!-- Insert your screenshot for Task 4 below: -->
<!-- SCREENSHOT REQUIREMENT: Show the terminal where you ran sleep 120 & and the subsequent ps output showing the sleep process running. -->

<img width="1033" height="126" alt="Screenshot from 2026-03-17 23-48-17" src="https://github.com/user-attachments/assets/a6f68f55-57dd-4b21-b119-4cbda129d28f" />
<img width="1052" height="195" alt="Screenshot from 2026-03-18 00-03-59" src="https://github.com/user-attachments/assets/dbd38fe8-ac55-4cd7-9a75-ed95743e3953" />

---

## Task 5: Installing Real Applications & Observing Multitasking

I ran 3 background processes simulating multitasking and read the processes with `ps` again into `task5_multitasking.txt`

<!-- Insert your screenshot for Task 5 below: -->
<!-- SCREENSHOT REQUIREMENT: Show the terminal ps output capturing the multiple background tasks (sleep and python3 server) running at the same time. -->

<img width="1356" height="482" alt="Screenshot from 2026-03-17 23-49-47" src="https://github.com/user-attachments/assets/91b937bf-fa18-4328-9dc8-774b1d23bcaf" />

---

## Task 6: Virtualization and Hypervisor Detection

My system is running on a virtualization of the Linux through vmware with the hypervisor vendor from vmware as my host machine name is monika-thai

<!-- Insert your screenshot for Task 6 below: -->
<!-- SCREENSHOT REQUIREMENT: Show the terminal output of the systemd-detect-virt and lscpu commands. -->

<img width="1844" height="237" alt="Screenshot from 2026-03-17 23-56-22" src="https://github.com/user-attachments/assets/5aeb25d1-e013-4c79-91ca-1e2409d36bcc" />
