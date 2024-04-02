import java.util.ArrayList;
import java.util.List;

public class Threads {
    public static void main(String[] args) {
        ConveyorBelt conveyorBelt = new ConveyorBelt();
        Truck truck = new Truck(10, conveyorBelt);
        truck.loadTruck();

        Peeler peeler = new Peeler(conveyorBelt);
        ChipCutter chipCutter = new ChipCutter(conveyorBelt);
        Fryer fryer = new Fryer(conveyorBelt);
        Packer packer = new Packer(conveyorBelt);

        peeler.start();
        chipCutter.start();
        fryer.start();
        packer.start();
    }
}

// Define Potato class
// Define Potato class
class Potato {
    private int id;
    private String type;

    public Potato() {
        // Default constructor
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setType(String type) {
        this.type = type;
    }

    public int getId() {
        return id;
    }

    public String getType() {
        return type;
    }

    // Additional methods can be added as needed
}



// Define ConveyorBelt class
class ConveyorBelt {
    private List<Potato> potatoes = new ArrayList<>();

    public synchronized void addPotato(Potato potato) {
        potatoes.add(potato);
        notifyAll();
    }

    public synchronized Potato getPotato() {
        while (isEmpty()) {
            try {
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        return potatoes.remove(0);
    }

    public synchronized boolean isEmpty() {
        return potatoes.isEmpty();
    }
}

// Define Peeler class
class Peeler extends Thread {
    private ConveyorBelt conveyorBelt;

    public Peeler(ConveyorBelt conveyorBelt) {
        this.conveyorBelt = conveyorBelt;
    }

    @Override
    public void run() {
        while (true) {
            synchronized (conveyorBelt) {
                while (conveyorBelt.isEmpty()) {
                    try {
                        conveyorBelt.wait();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
                Potato potato = conveyorBelt.getPotato();
            }

            // Peel the potato
            try {
                Thread.sleep(2000); // Simulating peeling process
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("Potato peeled");
        }
    }
}

// Define ChipCutter class
class ChipCutter extends Thread {
    private ConveyorBelt conveyorBelt;

    public ChipCutter(ConveyorBelt conveyorBelt) {
        this.conveyorBelt = conveyorBelt;
    }

    @Override
    public void run() {
        while (true) {
            synchronized (conveyorBelt) {
                while (conveyorBelt.isEmpty()) {
                    try {
                        conveyorBelt.wait();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
                Potato potato = conveyorBelt.getPotato();
            }

            // Cut the potato into chips
            try {
                Thread.sleep(2000); // Simulating chip cutting process
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("Potato cut into chips");
        }
    }
}

// Define Fryer class
class Fryer extends Thread {
    private ConveyorBelt conveyorBelt;

    public Fryer(ConveyorBelt conveyorBelt) {
        this.conveyorBelt = conveyorBelt;
    }

    @Override
    public void run() {
        while (true) {
            synchronized (conveyorBelt) {
                while (conveyorBelt.isEmpty()) {
                    try {
                        conveyorBelt.wait();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
                Potato potato = conveyorBelt.getPotato();
            }

            // Fry the chips
            try {
                Thread.sleep(6000); // Simulating frying process
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("Chips fried");
        }
    }
}

// Define Packer class
class Packer extends Thread {
    private ConveyorBelt conveyorBelt;

    public Packer(ConveyorBelt conveyorBelt) {
        this.conveyorBelt = conveyorBelt;
    }

    @Override
    public void run() {
        while (true) {
            synchronized (conveyorBelt) {
                while (conveyorBelt.isEmpty()) {
                    try {
                        conveyorBelt.wait();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
                Potato potato = conveyorBelt.getPotato();
            }

            // Pack the chips
            try {
                Thread.sleep(4000); // Simulating packing process
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("Chips packed");
        }
    }
}

// Define Truck class
class Truck {
    private int capacity;
    private ConveyorBelt conveyorBelt;

    public Truck(int capacity, ConveyorBelt conveyorBelt) {
        this.capacity = capacity;
        this.conveyorBelt = conveyorBelt;
    }

    public void loadTruck() {
        for (int i = 0; i < capacity; i++) {
            Potato potato = new Potato();
            conveyorBelt.addPotato(potato);
        }
        System.out.println("Truck loaded with potatoes");
    }
}
