/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/JSP_Servlet/Servlet.java to edit this template
 */

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 *
 * @author varun
 */
public class factorial extends HttpServlet {

   
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
        throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
       try (PrintWriter out = response.getWriter()) {
            out.println("<html>");
            out.println("<head>");
            out.println("<title>Factorial Calculation</title>");
            out.println("</head>");
            out.println("<body>");

            String s = request.getParameter("t1");

            if (s != null && !s.isEmpty()) {
                try {
                    int k = Integer.parseInt(s);
                    int fact = 1;

                    out.println("<table border='1'>");
                    out.println("<tr><th>Number</th><th>Factorial</th></tr>");

                    for (int i = 1; i <= k; ++i) {
                        out.println("<tr><td>" + i + "</td>");
                        fact = fact * i;
                        out.println("<td>" + fact + "</td></tr>");
                    }

                    out.println("</table>");
                } catch (NumberFormatException e) {
                    out.println("<p>Please enter a valid number.</p>");
                }
            } else {
                out.println("<p>Please enter a number.</p>");
            }

            out.println("</body>");
            out.println("</html>");
        }
    }
    

}
