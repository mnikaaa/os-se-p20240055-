# Class Activity 5 - Semaphores

- **Student Name:** Thai Monika
- **Student ID:** p20240055
- **Programming Language Used:** Python

---

## Task 1A: Particle Pair Buffer Before Semaphores
- **What error appeared:** The program crashed instantly with "Pairs are incorrect" or "The packaging machine is broken".
- **Why did this happen:** Without semaphores protecting the list array, multiple worker threads tried changing things at the same time, shuffling the elements out of order.

## Task 1B: Particle Pair Buffer After Semaphores
- **Semaphores used:** empty_pairs, full_pairs, mutex
- **Did any error appear during normal operation?** No, it runs perfectly forever.

## Task 2A: HELLO Before Semaphores
- **Output before semaphore ordering:** Something messy like LLEHO or OLLEH.
- **Why:** The threads ran completely randomly depending on what the CPU decided to process first.

## Task 2B: HELLO After Semaphores
- **Final output:** HELLO