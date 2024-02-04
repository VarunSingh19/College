/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ClientandServer;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

/**
 *
 * @author varun
 */
public class Server {
    public static void main(String[] args) {
        try {
            ServerSocket ss = new ServerSocket(3000);
            Socket s = ss.accept();

            BufferedReader br = new BufferedReader(new InputStreamReader(s.getInputStream()));
            PrintWriter pw = new PrintWriter(s.getOutputStream(), true);
            Scanner key = new Scanner(System.in);

            while (true) {
                System.out.print("Send/Receive/Quit: ");
                String input = key.next();

                switch (input.charAt(0)) {
                    case 's':
                    case 'S':
                        System.out.print("Enter message to send: ");
                        String messageToSend = key.next();
                        pw.println(messageToSend);
                        break;
                    case 'r':
                    case 'R':
                        String receivedMessage = br.readLine();
                        System.out.println("Received message: " + receivedMessage);
                        break;
                    case 'q':
                    case 'Q':
                        System.exit(0);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
