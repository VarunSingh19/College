
import java.util.Random;

public class BirdFeedingSimulation {
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

// import java.util.Random;

// class BirdFeedingSimulation {
//     public static void main(String[] args) {
//         int totalWheat = 50;
//         int totalStones = 50;
//         int totalBirds = 25;
//         int birdsWith2Wheat = 0;
//         int birdsWith1WheatAnd1Stone = 0;
//         int birdsWithNothing = 0;
        
//         Random random = new Random();
        
//         while (totalBirds > 0) {
//             int birdsToVisit = Math.min(6, totalBirds);
//             int wheatEaten = 0;
//             int stonesEaten = 0;
            
//             for (int i = 0; i < birdsToVisit; i++) {
//                 int choice = random.nextInt(3); // 0 for 2 wheat, 1 for 1 wheat and 1 stone, 2 for nothing
                
//                 if (choice == 0 && totalWheat >= 2) {
//                     wheatEaten += 2;
//                     totalWheat -= 2;
//                 } else if (choice == 1 && totalWheat >= 1 && totalStones >= 1) {
//                     wheatEaten += 1;
//                     stonesEaten += 1;
//                     totalWheat -= 1;
//                     totalStones -= 1;
//                 } else {
//                     birdsWithNothing++;
//                 }
//             }
            
//             if (wheatEaten == 2 * birdsToVisit) {
//                 birdsWith2Wheat += birdsToVisit;
//             } else if (wheatEaten == birdsToVisit && stonesEaten == birdsToVisit) {
//                 birdsWith1WheatAnd1Stone += birdsToVisit;
//             }
            
//             totalBirds -= birdsToVisit;
//         }
        
//         System.out.println("Birds with 2 wheat: " + birdsWith2Wheat);
//         System.out.println("Birds with 1 wheat and 1 stone: " + birdsWith1WheatAnd1Stone);
//         System.out.println("Birds with nothing: " + birdsWithNothing);
//     }
// }
