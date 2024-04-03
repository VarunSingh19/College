import java.io.IOException;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.ServletContext; // Import correct ServletContext class
import java.net.InetSocketAddress;
import com.sun.net.httpserver.HttpServer;

public class PotatoProcessingServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;
    private ServletContext servletContext; // Add ServletContext instance variable

    public void init() throws ServletException {
        super.init();
        servletContext = getServletContext(); // Initialize ServletContext in init() method
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html");

        // Initialize components
        ConveyorBelt conveyorBelt = new ConveyorBelt();
        Peeler peeler = new Peeler(conveyorBelt);
        ChipCutter chipCutter = new ChipCutter(conveyorBelt);
        Fryer fryer = new Fryer(conveyorBelt);
        Packer packer = new Packer(conveyorBelt);
        Truck truck = new Truck(5000, conveyorBelt);

        // Start processing threads
        peeler.start();
        chipCutter.start();
        fryer.start();
        packer.start();

        // Load trucks
        truck.loadTruck();

        // Set initial status
updateStatus(request, "Peeling", "Waiting");
updateStatus(request, "ChipCutting", "Waiting");
updateStatus(request, "Frying", "Waiting");
updateStatus(request, "Packing", "Waiting");

        // Forward request to JSP for interface
        request.getRequestDispatcher("potatoProcessing.jsp").forward(request, response);
    }

    // Method to update status
   public void updateStatus(HttpServletRequest request, String step, String status) {
    // Set status as request attribute
    request.setAttribute(step.toLowerCase() + "Status", status);
}
        public static void main(String[] args) throws Exception {
        // Create HTTP server on port 8080
        HttpServer server = HttpServer.create(new InetSocketAddress(8081), 0);
        // Create a context for the servlet
//        server.createContext("/potatoProcessing", new PotatoProcessingHandler());
        // Start the server
        server.start();
        System.out.println("Server started on port 8081...");
    }
}
