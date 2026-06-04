package task2_prevention;

import java.util.concurrent.Semaphore;

class Account {
    String name;
    int balance;
    Account(String name, int balance) {
        this.name = name;
        this.balance = balance;
    }
}

class TransferFixed {
    // This is our single security guard (Mutex)
    static Semaphore mutex = new Semaphore(1);

    static void transfer(Account from, Account to, int amount) {
        try {
            mutex.acquire(); // Ask guard for permission to enter
            
            System.out.println(Thread.currentThread().getName() + " executing transfer safely...");
            Thread.sleep(100);
            from.balance -= amount;
            to.balance += amount;

        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            System.out.println(Thread.currentThread().getName() + " finished and leaving.\n");
            mutex.release(); // Tell guard we are leaving
        }
    }
}

public class DeadlockFixed {
    public static void main(String[] args) throws InterruptedException {
        Account account1 = new Account("Account-1", 1000);
        Account account2 = new Account("Account-2", 1000);

        Thread t1 = new Thread(() -> TransferFixed.transfer(account1, account2, 100), "Worker-1");
        Thread t2 = new Thread(() -> TransferFixed.transfer(account2, account1, 200), "Worker-2");

        t1.start(); t2.start();
        t1.join(); t2.join();

        System.out.println("Final Account-1 Balance: " + account1.balance);
        System.out.println("Final Account-2 Balance: " + account2.balance);
        System.out.println("Total Balance: " + (account1.balance + account2.balance));
        System.out.println("No deadlock occurred");
    }
}