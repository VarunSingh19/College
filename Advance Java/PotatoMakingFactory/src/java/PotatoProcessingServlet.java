import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class PotatoProcessingServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

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
        updateStatus("Peeling", "Waiting");
        updateStatus("ChipCutting", "Waiting");
        updateStatus("Frying", "Waiting");
        updateStatus("Packing", "Waiting");

        // Forward request to JSP for interface
        request.getRequestDispatcher("potatoProcessing.jsp").forward(request, response);
    }

    // Method to update status
    public static void updateStatus(String step, String status) {
        // Set status as request attribute
        getServletContext().setAttribute(step.toLowerCase() + "Status", status);
    }
}
