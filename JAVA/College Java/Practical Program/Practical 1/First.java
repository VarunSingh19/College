//Practical no 1  

// class Account {
//     int Acno;
//     float balance;

//     Account() {
//         Acno = 0;
//         balance = 0.0f;
//     }

//     float getBalance() {
//         return balance;
//     }

//     int getAcno() {
//         return Acno;
//     }

//     void deposit(float k) {
//         balance = balance + k;
//     }

//     void withdraw(int k) {
//         balance = balance - k;
//     }

// }

// ================================================================
// class First {

// public static void main(String[] args) {
// System.out.println("Welcome To Bank");
// Account ob = new Account();
// ob.deposit(1000);
// System.out.println(ob.getBalance());
// ob.deposit(2000);
// System.out.println(ob.getBalance());
// ob.withdraw(1200);
// System.out.println(ob.getBalance());
//         String text = "Hello, World";
//         int l = text.length();
//         char c = text.charAt(1);
//         String sub1 = text.substring(7);
//         int ind1 = text.indexOf("World");
//         System.out.print("\nLength is: " + l + "\t");
//         System.out.print("\nCHarAT is: " + c + "\t");
//         System.out.print("\nsubstring is: " + sub1 + "\t");
//         System.out.print("\nindexOF is: " + ind1 + "\t");

//     }
// }

// ================================================================
// class Animal {
//     String name;

//     Animal(String name) {
//         this.name = name;
//     }

//     void eat() {
//         System.out.println(name + " is eating.");
//     }
// }

// class Dog extends Animal {
//     String breed;

//     Dog(String name, String breed) {
//         super(name);
//         this.breed = breed;
//     }

//     void bark() {
//         System.out.println(name + " (a " + breed + " dog ) is barking.");
//     }

//     void showParentName() {
//         System.out.println("Parent's name "+ super.name);
//     }
// }

// class First {
//     public static void main(String[] args) {
//         Dog myDog = new Dog("Buddy", "Golden Retriever");
//         myDog.eat();
//         myDog.bark();
//         myDog.showParentName();
//     }
// }
// ================================================================
// import java.awt.Frame;

// public class First extends Frame {
//     public First() {
//         super("My AWT Frame");
//         setSize(400, 300);
//         setVisible(true);
//     }

//     public static void main(String[] args) {
//         new First();
//     }
// }

// ================================================================
// import java.awt.Button;
// import java.awt.Frame;

// public class First {
//     public static void main(String[] args) {
//         Frame frame = new Frame("Button Example");
//         Button button = new Button("Click Me");
//         button.setBounds(100, 100, 80, 30);
//         frame.add(button);
//         frame.setSize(300, 200);
//         frame.setLayout(null);
//         frame.setVisible(true);
//     }
// }

// ================================================================
// public class First {
//     // Method to add two integers
//     public int add(int num1, int num2) {
//         return num1 + num2;
//     }

//     // Method to add three integers
//     public int add(int num1, int num2, int num3) {
//         return num1 + num2 + num3;
//     }

//     // Method to add two double values
//     public double add(double num1, double num2) {
//         return num1 + num2;
//     }

//     public static void main(String[] args) {
//         First calculator = new First();
//         // Method overloading based on the number and types of arguments
//         int sum1 = calculator.add(5, 7); // Calls the first add method (int)
//         int sum2 = calculator.add(3, 8, 2); // Calls the second add method (int)
//         double sum3 = calculator.add(2.5, 3.7); // Calls the third add method (double)
//         System.out.println("Sum 1: " + sum1);
//         System.out.println("Sum 2: " + sum2);
//         System.out.println("Sum 3: " + sum3);
//     }
// }

// ================================================================

// public class First {  //Rectangle
//     private double width;
//     private double height;

//     public First(double width, double height) {
//         this.width = width;
//         this.height = height;
//     }

//     public double getArea() {
//         return width * height;
//     }

//     public double getPerimeter() {
//         return 2 * (width + height);
//     }

//     public static void main(String[] args) {
//         First myRectangle = new First(5.0, 3.0);
//         System.out.println("Rectangle Area: " + myRectangle.getArea());
//         System.out.println("Rectangle Perimeter: " + myRectangle.getPerimeter());
//     }
// }

// ================================================================

// public class First {  //Traffic light..
//     private String color;

//     public First(String initialColor) {
//         color = initialColor;
//     }

//     public void changeColor(String newColor) {
//         color = newColor;
//     }

//     public boolean isRed() {
//         return "red".equals(color);
//     }

//     public boolean isGreen() {
//         return "green".equals(color);
//     }

//     public static void main(String[] args) {
//         First trafficLight = new First("red");
//         System.out.println("Current Color: " + trafficLight.color);
//         System.out.println("Is it Red? " + trafficLight.isRed());
//         System.out.println("Is it Green? " + trafficLight.isGreen());
//         trafficLight.changeColor("green");
//         System.out.println("Updated Color: " + trafficLight.color);
//         System.out.println("Is it Red? " + trafficLight.isRed());
//         System.out.println("Is it Green? " + trafficLight.isGreen());
//     }
// }

// ================================================================

// public class First {  //Employee
//     private String name;
//     private String jobTitle;
//     private double salary;

//     public First(String name, String jobTitle, double salary) {
//         this.name = name;
//         this.jobTitle = jobTitle;
//         this.salary = salary;
//     }

//     public void updateSalary(double percentageIncrease) {
//         salary += salary * (percentageIncrease / 100);
//     }

//     public String toString() {
//         return "Name: " + name + "\nJob Title: " + jobTitle + "\nSalary: $" + salary;
//     }

//     public static void main(String[] args) {
//         First employee = new First("John Doe", "Software Engineer", 60000.0);
//         System.out.println("Employee Information:");
//         System.out.println(employee);
//         double salaryIncreasePercentage = 10.0;
//         employee.updateSalary(salaryIncreasePercentage);
//         System.out.println("\nAfter a " + salaryIncreasePercentage + "% salary increase:");
//         System.out.println(employee.salary);
//     }
// }

// ================================================================

// public class First{  //Person
//     private String name;
//     private int age;

//     public First(String name, int age) {
//         this.name = name;
//         this.age = age;
//     }

//     public String getName() {
//         return name;
//     }

//     public int getAge() {
//         return age;
//     }

//     public static void main(String[] args) {
//         // Create two instances of the Person class
//         First person1 = new First("Alice", 30);
//         First person2 = new First("Bob", 25);
//         // Print the attributes of the first person
//         System.out.println("Person 1 - Name: " + person1.getName() + ", Age: " +
//                 person1.getAge());
//         // Print the attributes of the second person
//         System.out.println("Person 2 - Name: " + person2.getName() + ", Age: " +
//                 person2.getAge());
//     }
// }

// ================================================================

// public class First {  //ExceptionExample
//     public static void main(String[] args) {
//         try {
//             // Code that may throw an exception
//             int numerator = 10;
//             int denominator = 0;
//             int result = numerator / denominator; // This will throw an ArithmeticException
//         } catch (ArithmeticException e) {
//             // Code to handle the exception
//             System.out.println("An arithmetic exception occurred: " + e.getMessage());
//         }
//         System.out.println("Program continues after the exception handling");
//     }
// }

// ================================================================

// public class First { // WordCount
//     public static void main(String[] args) {
//         String inputString = "Don’t trouble trouble otherwise trouble will trouble you";
//         inputString = inputString.toLowerCase();
//         String wordToFind = "trouble";
//         String[] words = inputString.split(" ");
//         int count = 0;
//         for (String word : words) {
//             if (word.equals(wordToFind)) {
//                 count++;
//             }
//         }
// System.out.println("The word '" + wordToFind + "' occurs " + count + " times in the given string.");
//     }
// }



// ================================================================


// import java.awt.*;
// public class First { //UserForm
//     public static void main(String[] args) {
//         Frame frame = new Frame("User Information");
//         // Create panels for organization
//         Panel inputPanel = new Panel(new GridLayout(3, 2));
//         Panel buttonPanel = new Panel(new FlowLayout());
//         // Create Labels
//         Label firstNameLabel = new Label("First Name:");
//         Label lastNameLabel = new Label("Last Name:");
//         Label birthDateLabel = new Label("Birth Date (YYYY-MM-DD):");
//         // Create TextFields
//         TextField firstNameField = new TextField(20);
//         TextField lastNameField = new TextField(20);
//         TextField birthDateField = new TextField(20);
//         // Create Buttons
//         Button submitButton = new Button("Submit");
//         Button resetButton = new Button("Reset");
//         // Add components to inputPanel
//         inputPanel.add(firstNameLabel);
//         inputPanel.add(firstNameField);
//         inputPanel.add(lastNameLabel);
//         inputPanel.add(lastNameField);
//         inputPanel.add(birthDateLabel);
//         inputPanel.add(birthDateField);
//         // Add buttons to buttonPanel
//         buttonPanel.add(submitButton);
//         buttonPanel.add(resetButton);
//         // Add inputPanel and buttonPanel to the frame
//         frame.setLayout(new BorderLayout());
//         frame.add(inputPanel, BorderLayout.NORTH);
//         frame.add(buttonPanel, BorderLayout.SOUTH);
//         // Set frame size and make it visible
//         frame.setSize(400, 200);
//         frame.setVisible(true);
//     }
// }



// ================================================================

// public class First { //Animal
//     private double avW
//     public static void main(String[] args) {
        
//     }
// }