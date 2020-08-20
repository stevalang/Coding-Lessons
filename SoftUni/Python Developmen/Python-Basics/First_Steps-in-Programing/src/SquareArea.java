import java.util.Scanner;

public class SquareArea {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int a = Integer.parseInt(scan.nextLine());


        int squareArea = a * a;

        System.out.println(squareArea);
    }
}
