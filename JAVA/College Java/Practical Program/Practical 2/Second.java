class Person {
    String name;
    String address;

    Person(String n, String a) {
        name = n;
        address = a;
    }

    // Getters and setters
    String getName() {
        return name;
    }

    String getAddress() {
        return address;
    }

    void setName(String n) {
        name = n;
    }

    void setAddress(String a) {
        address = a;
    }
}

class BankAccount {
    int accountNumber;
    float balance;

    BankAccount(int acno) {
        accountNumber = acno;
        balance = 0.0f;
    }

    float getBalance() {
        return balance;
    }

    int getAccountNumber() {
        return accountNumber;
    }

    void deposit(float amount) {
        if (amount > 0) {
            balance += amount;
        }
    }

    void withdraw(float amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
        } else {
            System.out.println("Insufficient balance");
        }
    }
}

class Second {
    public static void main(String[] args) {
         System.out.println("Welcome To Bank");
        BankAccount account = new BankAccount(12345);
        Person ob1 = new Person("Varun Singh", "Madad West");

        System.out.println("Account Number : " + account.getAccountNumber());
        System.out.println("Name: " + ob1.getName());
        System.out.println("Address: " + ob1.getAddress());

        account.deposit(1000);
        System.out.println("Balance: " + account.getBalance());

        account.deposit(2000);
        System.out.println("Balance: " + account.getBalance());

        account.withdraw(1200);
        System.out.println("Balance: " + account.getBalance());
    }
}
