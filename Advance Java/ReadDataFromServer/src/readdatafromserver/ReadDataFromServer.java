/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package readdatafromserver;

/**
 *
 * @author varun
 */
import java.net.*;
import java.io.*;

public class ReadDataFromServer {

    /**
     * @param args the command line arguments
     */
    
    public static void main(String[] args) {
        // TODO code application logic here
        try {
            InetAddress address = InetAddress.getByName("ucos.com.eg");
            System.out.println(address);

            URL url = new URL("http://www.ucos.eg/about us.html"); // Replace space with %20
            URLConnection connection = url.openConnection();
            InputStream inputStream = connection.getInputStream();

            // Use BufferedReader for efficient reading of text
            BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));

            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }

            // Close resources
            reader.close();
            inputStream.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }   
}