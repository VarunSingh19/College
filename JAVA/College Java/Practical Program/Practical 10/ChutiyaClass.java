import java.lang.Math;

class Missile {
    private double distance; // total distance between America and Iraq
    private double speed; // speed of the missile
    private double altitude; // current altitude of the missile

    public Missile(double distance, double speed) {
        this.distance = distance;
        this.speed = speed;
        this.altitude = 0.0;
    }

    public void launch() {
        double time = distance / speed; // time taken to travel the distance
        altitude = 10 * time; // altitude reached assuming constant acceleration
    }

    public double getAltitude() {
        return altitude;
    }
}

class ChutiyaClass {
    public static void main(String[] args) {
        double distance = 2000.0;
        double iraqSpeed = 10.0; // km/sec
        double americaSpeed = 15.0; // km/sec
        double iraqTime = distance / iraqSpeed;

        Missile iraqMissile = new Missile(distance, iraqSpeed);
        iraqMissile.launch();

        Missile americaMissile = new Missile(iraqMissile.getAltitude(), americaSpeed);
        americaMissile.launch();

        double americaTime = (distance + americaMissile.getAltitude()) / americaSpeed;
        double totalTime = iraqTime + americaTime;

        System.out.println("Total time taken: " + totalTime + " seconds");
        System.out.println("Altitude of America missile: " + americaMissile.getAltitude() + " km");
    }
}