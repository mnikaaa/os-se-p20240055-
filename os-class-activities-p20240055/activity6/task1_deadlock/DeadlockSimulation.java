package task1_deadlock;

import java.util.concurrent.Semaphore;

class Account {
    String name;
    int balance;
    Semaphore lock = new Semaphore(1);

    Account(String name, int balance) {
        this.name = name;
        this.balance = balance;
    }
}

class Transfer {
    static boolean progressMade = false;

    static void transfer(Account from, Account to, int amount) {
        try {
            System.out.println(Thread.currentThread().getName() + " trying to lock FROM " + from.name);
            from.lock.acquire();
            System.out.println(Thread.currentThread().getName() + " locked FROM " + from.name);

            // This intentional pause causes the deadlock
            Thread.sleep(100);

            System.out.println(Thread.currentThread().getName() + " trying to lock TO " + to.name);
            to.lock.acquire();
            
            from.balance -= amount;
            to.balance += amount;
            progressMade = true;

            to.lock.release();
            from.lock.release();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

public class DeadlockSimulation {
    public static void main(String[] args) {
        Account account1 = new Account("Account-1", 1000);
        Account account2 = new Account("Account-2", 1000);

        Thread t1 = new Thread(() -> Transfer.transfer(account1, account2, 100), "Worker-1");
        Thread t2 = new Thread(() -> Transfer.transfer(account2, account1, 200), "Worker-2");

        // Watchdog thread that checks if things are frozen
        Thread watchdog = new Thread(() -> {
            try {
                Thread.sleep(2000);
                if (!Transfer.progressMade) {
                    System.out.println("\n###########################################");
                    System.out.println("Deadlock detected: transactions are stuck");
                    System.out.println("Worker-1 is waiting for " + account2.name);
                    System.out.println("Worker-2 is waiting for " + account1.name);
                    System.out.println("###########################################");
                    System.exit(1);
                }
            } catch (InterruptedException e) {}
        });
        watchdog.setDaemon(true);
        watchdog.start();

        t1.start();
        t2.start();
    }
}