import static java.lang.Math.random;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Random;
import java.util.logging.Level;
import java.util.logging.Logger;
public class Toll {
    public static void main(String[] args) {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
        } catch (ClassNotFoundException ex) {
            Logger.getLogger(Toll.class.getName()).log(Level.SEVERE, null, ex);
        }
        try {
            // Establish connection to MySQL database
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/mysql", "root", "root");
            System.out.println("Connection established");

            // Create table toll_data if it does not exist
            Statement stmt = con.createStatement();
            String createTableQuery = "CREATE TABLE IF NOT EXISTS toll_data (number_plate INT, status VARCHAR(20), vehicle_type VARCHAR(20))";
            stmt.executeUpdate(createTableQuery);
            System.out.println("Table created successfully");

            // Generate and insert data into the table
            Random random = new Random();
            for (int i = 1; i <= 1000; ++i) {
                int randomInt = random.nextInt(2);
                String[] registrationStatus = {"registered", "not registered"};
                String status = registrationStatus[randomInt];
                int randomType = random.nextInt(4);
                String[] type = {"Car", "Bus", "Auto", "Truck"};
                String vehicle = type[randomType];

                // Insert data into the table
                String insertDataQuery = "INSERT INTO toll_data (number_plate, status, vehicle_type) VALUES (" + i + ", '" + status + "', '" + vehicle + "')";
                stmt.executeUpdate(insertDataQuery);
            }

            // Close connection
            stmt.close();
            con.close();
        } catch (SQLException ex) {
            Logger.getLogger(Toll.class.getName()).log(Level.SEVERE, null, ex);
        }
        }
    }
