import java.util.Random;

public class BirdFeedingSimulation {
    public static void main(String[] args) {
        int totalWheat = 50;
        int totalStones = 50;
        int totalBirds = 25;
        int birdsWith2Wheat = 0;
        int birdsWith1WheatAnd1Stone = 0;
        int birdsWithNothing = 0;
        
        Random random = new Random();
        
        while (totalBirds > 0) {
            int birdsToVisit = Math.min(6, totalBirds);
            int wheatEaten = 0;
            int stonesEaten = 0;
            
            for (int i = 0; i < birdsToVisit; i++) {
                int choice = random.nextInt(3); // 0 for 2 wheat, 1 for 1 wheat and 1 stone, 2 for nothing
                
                if (choice == 0 && totalWheat >= 2) {
                    wheatEaten += 2;
                    totalWheat -= 2;
                } else if (choice == 1 && totalWheat >= 1 && totalStones >= 1) {
                    wheatEaten += 1;
                    stonesEaten += 1;
                    totalWheat -= 1;
                    totalStones -= 1;
                } else {
                    birdsWithNothing++;
                }
            }
            
            if (wheatEaten == 2 * birdsToVisit) {
                birdsWith2Wheat += birdsToVisit;
            } else if (wheatEaten == birdsToVisit && stonesEaten == birdsToVisit) {
                birdsWith1WheatAnd1Stone += birdsToVisit;
            }
            
            totalBirds -= birdsToVisit;
        }
        
        System.out.println("Birds with 2 wheat: " + birdsWith2Wheat);
        System.out.println("Birds with 1 wheat and 1 stone: " + birdsWith1WheatAnd1Stone);
        System.out.println("Birds with nothing: " + birdsWithNothing);
    }
}
