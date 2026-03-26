# Class Activity 1 — System Calls in Practice

- **Student Name:** Thai Monika
- **Student ID:** p20240055
- **Date:** 26/03/2026

---

## Warm-Up: Hello System Call

Screenshot of running `hello_syscall.c` on Linux:

<img width="1104" height="659" alt="Screenshot from 2026-03-19 10-56-22" src="https://github.com/user-attachments/assets/e01d6316-7ae0-44fc-aadf-a845b4c99633" />


Screenshot of running `hello_winapi.c` on Windows (CMD/PowerShell/VS Code):

<img width="946" height="122" alt="image" src="https://github.com/user-attachments/assets/be1a609c-c67f-45c7-9624-ae6a8612b71b" />


Screenshot of running `copyfilesyscall.c` on Linux:

<img width="1196" height="93" alt="Screenshot from 2026-03-19 16-13-53" src="https://github.com/user-attachments/assets/997aa237-3dc6-47d1-9f37-9eda415a0f28" />


---

## Task 1: File Creator & Reader

### Part A — File Creator

**Describe your implementation:** [What differences did you notice between the library version and the system call version?]

**Version A — Library Functions (`file_creator_lib.c`):**

<!-- Screenshot: gcc -o file_creator_lib file_creator_lib.c && ./file_creator_lib && cat output.txt -->

<img width="1156" height="98" alt="Screenshot from 2026-03-19 16-29-01" src="https://github.com/user-attachments/assets/6b962632-4633-4084-a4e4-b1999d21036d" />

**Version B — POSIX System Calls (`file_creator_sys.c`):**

<!-- Screenshot: gcc -o file_creator_sys file_creator_sys.c && ./file_creator_sys && cat output.txt -->

<img width="1072" height="142" alt="Screenshot from 2026-03-26 14-45-21" src="https://github.com/user-attachments/assets/0dd89c04-564a-4fef-ae77-5d2a1f44bc60" />

**Questions:**

1. **What flags did you pass to `open()`? What does each flag mean?**

   > [Your answer]

2. **What is `0644`? What does each digit represent?**

   > [Your answer]

3. **What does `fopen("output.txt", "w")` do internally that you had to do manually?**

   > [Your answer]

### Part B — File Reader & Display

**Describe your implementation:** [Your notes]

**Version A — Library Functions (`file_reader_lib.c`):**

<img width="1074" height="124" alt="Screenshot from 2026-03-26 14-58-04" src="https://github.com/user-attachments/assets/83480953-aba8-4e16-b473-c5edce0d0d0d" />

**Version B — POSIX System Calls (`file_reader_sys.c`):**

<img width="1074" height="124" alt="Screenshot from 2026-03-26 15-02-20" src="https://github.com/user-attachments/assets/2648b86b-c730-41e4-9b70-a4018743e7a5" />

**Questions:**

1. **What does `read()` return? How is this different from `fgets()`?**

   > [Your answer]

2. **Why do you need a loop when using `read()`? When does it stop?**

   > [Your answer]

---

## Task 2: Directory Listing & File Info

**Describe your implementation:** [Your notes]

### Version A — Library Functions (`dir_list_lib.c`)

<img width="1070" height="401" alt="image" src="https://github.com/user-attachments/assets/c4b23a40-52bf-4d1d-8618-d338c9dcbf5c" />

### Version B — System Calls (`dir_list_sys.c`)

<img width="1071" height="430" alt="image" src="https://github.com/user-attachments/assets/eeb793df-4887-4ac2-aa06-e8e82d128b7b" />


### Questions

1. **What struct does `readdir()` return? What fields does it contain?**

   > [Your answer]

2. **What information does `stat()` provide beyond file size?**

   > [Your answer]

3. **Why can't you `write()` a number directly — why do you need `snprintf()` first?**

   > [Your answer]

---

## Optional Bonus: Windows API (`file_creator_win.c`)

Screenshot of running on Windows:

![Task 1 - Windows](screenshots/task1_win.png)

### Bonus Questions

1. **Why does Windows use `HANDLE` instead of integer file descriptors?**

   > [Your answer]

2. **What is the Windows equivalent of POSIX `fork()`? Why is it different?**

   > [Your answer]

3. **Can you use POSIX calls on Windows?**

   > [Your answer]

---

## Task 3: strace Analysis

**Describe what you observed:** [What surprised you about the strace output? How many more system calls did the library version make?]

### strace Output — Library Version (File Creator)

<!-- Screenshot: strace -e trace=openat,read,write,close ./file_creator_lib -->
<!-- IMPORTANT: Highlight/annotate the key system calls in your screenshot -->
<img width="860" height="278" alt="image" src="https://github.com/user-attachments/assets/9a3ef38f-2e1c-4d38-9b14-9d9ec439fa16" />


### strace Output — System Call Version (File Creator)

<!-- Screenshot: strace -e trace=openat,read,write,close ./file_creator_sys -->
<!-- IMPORTANT: Highlight/annotate the key system calls in your screenshot -->
<img width="851" height="246" alt="image" src="https://github.com/user-attachments/assets/11ea19b1-0f35-4e4f-87b2-37ac7f1a3ee1" />


### strace Output — Library Version (File Reader or Dir Listing)

<img width="868" height="279" alt="image" src="https://github.com/user-attachments/assets/d224f5e3-3904-4666-874a-8ef8f7f459e5" />


### strace Output — System Call Version (File Reader or Dir Listing)

<img width="868" height="279" alt="image" src="https://github.com/user-attachments/assets/0bd9e7ce-08d2-4611-ab0d-30c389de6b28" />


### strace -c Summary Comparison

<!-- Screenshot of `strace -c` output for both versions -->
<img width="1046" height="246" alt="image" src="https://github.com/user-attachments/assets/5ad2675f-cbce-427c-90b3-5e02c22bfb09" />

<img width="1046" height="399" alt="image" src="https://github.com/user-attachments/assets/7a7198a6-23e4-41a0-aa66-681afc35cb52" />


### Questions

1. **How many system calls does the library version make compared to the system call version?**

   > [Your answer — use the `strace -c` counts]

2. **What extra system calls appear in the library version? What do they do?**

   > [Your answer — mention `brk`, `mmap`, `fstat`, etc.]

3. **How many `write()` calls does `fprintf()` actually produce?**

   > [Your answer]

4. **In your own words, what is the real difference between a library function and a system call?**

   > [Your answer]

---

## Task 4: Exploring OS Structure

### System Information

> 📸 Screenshot of `uname -a`, `/proc/cpuinfo`, `/proc/meminfo`, `/proc/version`, `/proc/uptime`:

<img width="1074" height="488" alt="Screenshot from 2026-03-26 15-57-56" src="https://github.com/user-attachments/assets/3fa56d21-bc5c-4ddc-96bd-f0d949c640d1" />

<img width="1072" height="331" alt="Screenshot from 2026-03-26 15-58-10" src="https://github.com/user-attachments/assets/6da86c14-a0f4-4071-acb1-3dbe2ab9c614" />


### Process Information

> 📸 Screenshot of `/proc/self/status`, `/proc/self/maps`, `ps aux`:

<img width="1072" height="367" alt="Screenshot from 2026-03-26 15-59-19" src="https://github.com/user-attachments/assets/09d3bbcb-94c7-4fd4-88fd-f09e797b8f93" />

<img width="1072" height="364" alt="Screenshot from 2026-03-26 15-59-49" src="https://github.com/user-attachments/assets/5240e643-758b-47fc-83b5-9b7777a0428b" />

<img width="1072" height="364" alt="Screenshot from 2026-03-26 16-00-01" src="https://github.com/user-attachments/assets/2ecfb88e-0834-4eae-8f73-d8f6e27f6012" />


### Kernel Modules

> 📸 Screenshot of `lsmod` and `modinfo`:

<img width="931" height="364" alt="Screenshot from 2026-03-26 16-06-09" src="https://github.com/user-attachments/assets/566345ae-cf01-49bc-8851-b9985f57aaf8" />

<img width="931" height="637" alt="Screenshot from 2026-03-26 16-06-21" src="https://github.com/user-attachments/assets/932d85ed-d7a8-4838-98f1-5d6b69c4895e" />


### OS Layers Diagram

> 📸 Your diagram of the OS layers, labeled with real data from your system:

<img width="668" height="496" alt="image" src="https://github.com/user-attachments/assets/ab66a11c-3e8f-4779-b0ca-2250d7fba9b5" />


### Questions

1. **What is `/proc`? Is it a real filesystem on disk?**

   > [Your answer]

2. **Monolithic kernel vs. microkernel — which type does Linux use?**

   > [Your answer]

3. **What memory regions do you see in `/proc/self/maps`?**

   > [Your answer]

4. **Break down the kernel version string from `uname -a`.**

   > [Your answer]

5. **How does `/proc` show that the OS is an intermediary between programs and hardware?**

   > [Your answer]

---

## Reflection

What did you learn from this activity? What was the most surprising difference between library functions and system calls?

> [Write your reflection here]
