# Lab 9: Quantum Vault Deadlock

**Student ID:** p20240055  
**Role:** Player B  
**Partner username:** se-chheng-kimter  

## Answers

1. Each `vault.lock` file represents exclusive access to a vault resource — like a key that only one process can hold at a time.

2. `flock` requires every script to lock the same shared file because coordination only works if both scripts compete over the exact same file. Different files mean no coordination.

3. `sync_up` held **Vault Alpha** and waited for **Vault Beta**.

4. `sync_down` held **Vault Beta** and waited for **Vault Alpha**.

5. The four deadlock conditions in Level 3 were: mutual exclusion, hold and wait, no preemption, and circular wait.

6. The Alpha-before-Beta rule breaks circular wait because if everyone must lock Alpha first, no process can hold Beta while waiting for Alpha — the cycle cannot form.

7. `flock -w` is useful because it makes scripts fail fast instead of hanging forever, allowing the system to recover and retry even if deadlock is not fully prevented.

8. Stuck processes still hold locks and will block any future scripts from running, so checking for them ensures a clean state before finishing.

## Screenshots
<img width="1083" height="417" alt="level1_vaults" src="https://github.com/user-attachments/assets/e9d9b490-ff0c-43ec-8862-f04734ec4f68" />
<img width="785" height="518" alt="level3_local_deadlock" src="https://github.com/user-attachments/assets/42fa6ce3-aadd-4c66-a413-aec8b2fe852f" />
<img width="741" height="482" alt="level4_cross_deadlock" src="https://github.com/user-attachments/assets/84b02706-b012-472a-845f-e7a6a89a64e7" />
<img width="741" height="482" alt="level5_ordering_patch" src="https://github.com/user-attachments/assets/805e4b6d-e488-4a18-af0f-df03ec78ccd8" />
<img width="708" height="348" alt="level5_ordering_patch2" src="https://github.com/user-attachments/assets/4638694e-797b-44a1-a1d0-c7ae179a3f04" />
<img width="716" height="155" alt="level6_timeout_recovery" src="https://github.com/user-attachments/assets/c27b6f66-65ca-42c9-99b6-490be783ef14" />
<img width="716" height="155" alt="level6_timeout_recovery2" src="https://github.com/user-attachments/assets/f4232eae-54ac-4e03-a611-b0f5d2b9071c" />
<img width="716" height="293" alt="level7_teardown" src="https://github.com/user-attachments/assets/0037bb97-2c8f-43c7-a98f-f5b95010724e" />
