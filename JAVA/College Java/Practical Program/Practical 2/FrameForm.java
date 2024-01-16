// import java.awt.*;
// class Frame1 extends Frame {
//     Panel p;
//     Label l1, l2;
//     TextField t1, t2;
//     Button b;

//     Frame1(String s) {
//         super(s);
//         p = new Panel();
//         l1 = new Label("First No:");
//         l2 = new Label("Second No:");
//         t1 = new TextField(5);
//         t2 = new TextField(5);
//         b = new Button("Add");
//         p.add(l1);
//         p.add(t1);
//         p.add(l2);
//         p.add(t2);
//         p.add(b);

//     }
// }

// public class FrameForm {
//     public static void main(String[] args) {
//         Frame1 f1 = new Frame1("Form");
//         f1.setSize(300, 400);//set size of frame
//         f1.setVisible(true);

//     }

// }
import java.util.Random;

public class FrameForm {
    public static void main(String[] args) {
        int totalGrains = 50;
        int totalStones = 50;
        Random random = new Random();
        int sparrowsWith2Grains = 0;
        int sparrowsWith1GrainAnd1Stone = 0;
        int sparrowsWith2Stones = 0;
        int totalSparrows = 0;

        while (sparrowsWith2Grains + sparrowsWith1GrainAnd1Stone + sparrowsWith2Stones < 50) {
            int grainsTaken = 0;
            int stonesTaken = 0;
            int sparrowCount = 0;

            while (sparrowCount < 6) {
                // Allow sparrows to pick items
                for (int k = 0; k < 2; k++) {
                    int randomChoice = random.nextInt(2); // Generate a random number (0 or 1)
                    if (randomChoice == 0 && totalGrains > 0) {
                        grainsTaken = grainsTaken + 1;
                        totalGrains = totalGrains - 1;
                    } else if (randomChoice == 1 && totalStones > 0) {
                        stonesTaken = stonesTaken + 1;
                        totalStones = totalStones - 1;
                    }
                }
                // Increase the sparrow count
                sparrowCount++;
            }

            if (grainsTaken == 2) {
                sparrowsWith2Grains = sparrowsWith2Grains + 1;
            } else if (grainsTaken == 1 && stonesTaken == 1) {
                sparrowsWith1GrainAnd1Stone = sparrowsWith1GrainAnd1Stone + 1;
            } else if (stonesTaken == 2) {
                sparrowsWith2Stones = sparrowsWith2Stones + 1;
            }

            // Reset the sparrow count
            sparrowCount = 0;

            // Increment the total sparrow count
            totalSparrows++;
        }

        System.out.println("Sparrows with 2 grains: " + sparrowsWith2Grains);
        System.out.println("Sparrows with 1 grain and 1 stone: " + sparrowsWith1GrainAnd1Stone);
        System.out.println("Sparrows with 2 stones: " + sparrowsWith2Stones);
        System.out.println("Total number of sparrows: " + totalSparrows);
    }
}

