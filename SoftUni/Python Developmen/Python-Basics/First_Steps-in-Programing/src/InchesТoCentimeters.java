import java.util.Scanner;

public class InchesТoCentimeters {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double a = Double.parseDouble(scanner.nextLine());
        double inches = a * 2.54;
        System.out.println(inches);
    }

}

