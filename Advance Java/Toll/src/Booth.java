import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.HashMap;
import java.util.Random;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Booth {
    public static void main(String[] args) {
        int total = 0;
        int carCount = 0;
        int truckCount = 0;
        int busCount = 0;
        int autoCount = 0;
        HashMap<String, Integer> dictionary = new HashMap<>();
        dictionary.put("Car", 50);
        dictionary.put("Truck", 200);
        dictionary.put("Bus", 300);
        dictionary.put("Auto", 100);
        String sql = "SELECT status, vehicle_type FROM toll_data WHERE number_plate = ?;";
        
        try (            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/mysql", "root", "root");
             PreparedStatement statement = con.prepareStatement(sql)) {
            System.out.println("Connection established");
            
            Random random = new Random();
            
            for (int i = 1; i <= 1000; ++i) {
                int randomPlate = random.nextInt(1000);                
                statement.setInt(1, randomPlate);
                try (ResultSet resultSet = statement.executeQuery()) {
                    while (resultSet.next()) {
                        String status = resultSet.getString("status");
                        String type = resultSet.getString("vehicle_type");
                        if ("Car".equals(type)) {
                            carCount++;
                        } else if ("Truck".equals(type)) {
                            truckCount++;
                        } else if ("Bus".equals(type)) {
                            busCount++;
                        } else if ("Auto".equals(type)) {
                            autoCount++;
                        }
                        int Bamount = dictionary.getOrDefault(type, 0);
                        if("registered".equals(status)){
                            total += Bamount;
                            int returning = random.nextInt(2);
                            if (returning == 1){
                                total += Bamount;
                            }
                            else
                            {}
                        }else {
                            total += Bamount*2;
                            int returning = random.nextInt(2);
                            if (returning == 1){
                                total += Bamount;
                            }
                            else
                            {}
                        }
                }
                }
            }
            System.out.println("Vehicle Counts:");
            System.out.println("Car: " + carCount);
            System.out.println("Truck: " + truckCount);
            System.out.println("Bus: " + busCount);
            System.out.println("Auto: " + autoCount);
            System.out.println("Total amount collected: " + total);
        } catch (SQLException ex) {
            Logger.getLogger(Booth.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
