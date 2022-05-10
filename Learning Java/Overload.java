public class Overload {
    
    void ov1Demo(){
        System.out.println("No parameters");
    }
    void ov1Demo(int a) {
        System.out.println("One parameters");
    }

    int ov1Demo(int a, int b) {
        System.out.println("One parameters");
        return a + b;
    }

    double ov1Demo(double a, double b) {
        System.out.println("Two double parameters");
        return a + b;
    }
}
