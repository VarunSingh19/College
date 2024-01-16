
class Person {
    String name;
    String adddress;

    Person(String n, String a) {
        name = n;
        adddress = a;
        System.out.println("Person");
    }

    String getName() {
        return name;
    }

    String getAddress() {
        return adddress;
    }

    void setName(String n) {
        name = n;
    }

    void setAddress(String a) {
        adddress = a;
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
public class Fourth {
    public static void main(String[] args) {
        
    }
}

