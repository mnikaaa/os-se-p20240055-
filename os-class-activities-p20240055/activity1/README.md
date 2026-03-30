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
The library version uses fopen() and fprintf() which are C standard library wrappers that handle buffering internally. The system call version uses open(), write(), and close() directly, which talk to the kernel with no buffering layer in between. The result in output.txt is the same, but the sys version gives more explicit control over permissions and I/O.

**Version A — Library Functions (`file_creator_lib.c`):**

<!-- Screenshot: gcc -o file_creator_lib file_creator_lib.c && ./file_creator_lib && cat output.txt -->

<img width="1156" height="98" alt="Screenshot from 2026-03-19 16-29-01" src="https://github.com/user-attachments/assets/6b962632-4633-4084-a4e4-b1999d21036d" />

**Version B — POSIX System Calls (`file_creator_sys.c`):**

<!-- Screenshot: gcc -o file_creator_sys file_creator_sys.c && ./file_creator_sys && cat output.txt -->

<img width="1072" height="142" alt="Screenshot from 2026-03-26 14-45-21" src="https://github.com/user-attachments/assets/0dd89c04-564a-4fef-ae77-5d2a1f44bc60" />

**Questions:**

1. **What flags did you pass to `open()`? What does each flag mean?**

O_WRONLY opens the file for writing only. O_CREAT creates the file if it does not already exist. O_TRUNC truncates the file to zero length if it already exists, so old content is replaced. All three together replicate what fopen("output.txt", "w") does internally.

2. **What is `0644`? What does each digit represent?**

0644 is an octal permission value. The leading 0 means octal. The first digit 6 (owner) = read + write (4+2). The second digit 4 (group) = read only. The third digit 4 (others) = read only. So the file owner can read and write, while everyone else can only read.

3. **What does `fopen("output.txt", "w")` do internally that you had to do manually?**

Internally fopen() calls open() with O_WRONLY | O_CREAT | O_TRUNC and a default permission of 0666 (before umask is applied). It also allocates a FILE struct in memory and sets up an internal I/O buffer. In the sys version I had to call open() myself with explicit flags and choose my own permission value like 0644.

### Part B — File Reader & Display

**Describe your implementation:** 
The library version uses fgets() inside a while loop which reads one line at a time into a buffer and stops at NULL. The system call version uses read() in a loop, reading raw bytes into a 256-byte buffer and writing them straight to stdout using write(1, ...) until read() returns 0 (end of file).

**Version A — Library Functions (`file_reader_lib.c`):**

<img width="1074" height="124" alt="Screenshot from 2026-03-26 14-58-04" src="https://github.com/user-attachments/assets/83480953-aba8-4e16-b473-c5edce0d0d0d" />

**Version B — POSIX System Calls (`file_reader_sys.c`):**

<img width="1074" height="124" alt="Screenshot from 2026-03-26 15-02-20" src="https://github.com/user-attachments/assets/2648b86b-c730-41e4-9b70-a4018743e7a5" />

**Questions:**

1. **What does `read()` return? How is this different from `fgets()`?**

 read() returns the number of bytes actually read as an integer, 0 at end of file, or -1 on error. fgets() returns a pointer to the buffer on success or NULL at end of file or on error. Unlike fgets(), read() does not stop at newlines — it reads raw bytes up to the buffer size, and does not add a null terminator.
 
2. **Why do you need a loop when using `read()`? When does it stop?**

Because read() may not read the entire file in one call — if the file is larger than the buffer, only sizeof(buffer) bytes are read at a time. The loop keeps reading the next chunk until read() returns 0, which means the end of the file has been reached. Without a loop, only the first 256 bytes would be displayed.
---

## Task 2: Directory Listing & File Info

**Describe your implementation:** 

Both versions use opendir(), readdir(), and stat() to walk the directory and get file sizes. The only difference is the output method — the library version uses printf() to format and print, while the sys version uses snprintf() to format into a buffer first, then write(1, buffer, len) to print to stdout, since write() cannot format on its own.

### Version A — Library Functions (`dir_list_lib.c`)

<img width="1070" height="401" alt="image" src="https://github.com/user-attachments/assets/c4b23a40-52bf-4d1d-8618-d338c9dcbf5c" />

### Version B — System Calls (`dir_list_sys.c`)

<img width="1071" height="430" alt="image" src="https://github.com/user-attachments/assets/eeb793df-4887-4ac2-aa06-e8e82d128b7b" />


### Questions

1. **What struct does `readdir()` return? What fields does it contain?**

readdir() returns a pointer to a struct dirent. Its main fields are: d_name (the filename as a string), d_ino (the inode number), d_type (file type, e.g. regular file or directory), d_reclen (record length), and d_off (offset to next entry). In this program we used d_name to get the filename and passed it to stat() for size.

2. **What information does `stat()` provide beyond file size?**

stat() fills a struct stat with: st_size (file size in bytes), st_mode (file type and permissions), st_uid / st_gid (owner and group IDs), st_atime / st_mtime / st_ctime (access, modification, and change timestamps), st_nlink (number of hard links), st_ino (inode number), and st_blocks (disk blocks allocated).

3. **Why can't you `write()` a number directly — why do you need `snprintf()` first?**

write() only accepts a raw byte buffer — it has no formatting ability at all. A number like 12288 stored as an integer is just binary data in memory (e.g. 0x00003000), not the characters "12288". snprintf() converts the integer into its human-readable ASCII string representation inside a buffer, and then write() can send those characters to the terminal.

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

The library version made significantly more system calls than the sys version. The library version had to load libc.so.6 using openat(), read(), and close() before doing any actual work, which added around 5 extra syscalls just for setup. The sys version went straight to the file operation with no overhead. It was surprising to see how much work fopen() triggers under the hood just to open one file.

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

Based on the strace -c output, the library version makes approximately 10–12 total system calls, while the sys version makes around 6–7. The library version has extra calls for loading the C runtime (openat, read, close for libc.so.6) that do not appear in the sys version.

2. **What extra system calls appear in the library version? What do they do?**

The library version includes extra openat() and read() calls to load /etc/ld.so.cache and /lib/x86_64-linux-gnu/libc.so.6 — these are the dynamic linker loading the C standard library. It may also include mmap() to map the library into memory and fstat() to check the file before buffering. None of these appear in the sys version.

3. **How many `write()` calls does `fprintf()` actually produce?**

In this program fprintf() produces a single write() syscall. The C library buffers the output internally and flushes it all at once when fclose() is called, so even though we called fprintf() once, only one actual write() syscall reaches the kernel.

4. **In your own words, what is the real difference between a library function and a system call?**
A library function like printf() or fopen() is regular C code that runs entirely in user space. It may do formatting, buffering, or error handling before eventually calling a system call. A system call like write() or open() is a direct request to the kernel — it crosses the user/kernel boundary, switches CPU mode, and asks the OS to perform a privileged operation on our behalf. Library functions are convenient wrappers; system calls are the actual interface to the OS.
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

/proc is a virtual filesystem — it does not exist on disk at all. It is created by the Linux kernel in memory at boot time and presents kernel data structures as readable files. When you read /proc/cpuinfo for example, the kernel generates that text on the fly. It is a way for the OS to expose internal information (processes, hardware, memory) to user space programs through normal file I/O.

2. **Monolithic kernel vs. microkernel — which type does Linux use?**

Linux uses a monolithic kernel, meaning the entire kernel — including device drivers, filesystem management, memory management, and process scheduling — runs as a single large program in kernel space. This is faster than a microkernel because components communicate through direct function calls rather than message passing, but it means a bug in any driver can crash the whole system.

3. **What memory regions do you see in `/proc/self/maps`?**

/proc/self/maps shows regions such as: the program's executable code (r-xp), read-only data segment (r--p), read-write data/heap (rw-p), the stack (rwxp or rw-p at high addresses), and memory-mapped shared libraries like libc.so.6 and ld-linux.so. Each line shows the virtual address range, permissions, and what file (if any) is mapped there.

4. **Break down the kernel version string from `uname -a`.**

Linux = OS name. monika-thai = hostname. 6.17.0 = kernel version (major 6, minor 17, patch 0). 19-generic = build/ABI number and flavour (generic = standard Ubuntu kernel). #19~24.04.2-Ubuntu = build number and distro tag. SMP = Symmetric Multi-Processing enabled (multiple CPU cores). PREEMPT_DYNAMIC = kernel supports dynamic preemption. Fri Mar 6 23:08:46 UTC 2 = build date/time. x86_64 x86_64 x86_64 = hardware arch, CPU mode, OS mode. GNU/Linux = OS type.

5. **How does `/proc` show that the OS is an intermediary between programs and hardware?**

/proc exposes hardware information (CPU model, memory size, device stats) as readable files, but none of that data comes from disk — the kernel reads real hardware registers and memory structures and translates them into text for user programs. When my C program reads /proc/cpuinfo, it never touches the CPU directly; the kernel acts as the intermediary, gathering the hardware data and delivering it safely to user space through the file abstraction.

---

## Reflection

What did you learn from this activity? What was the most surprising difference between library functions and system calls?
This activity made clear that library functions like fopen() and printf() are not magic — they are just C code that eventually calls the same open(), write(), and close() system calls I wrote myself. The most surprising thing was seeing in strace how many extra syscalls the library version makes just to load libc.so.6 before doing any real work. Writing the sys versions also helped me understand file descriptors properly: 0 is stdin, 1 is stdout, 2 is stderr, and every file you open gets the next available integer. The OS layers diagram also made it click that my programs never actually touch the hardware — everything goes through the kernel's system call interface, which then manages the CPU and memory on my behalf.
