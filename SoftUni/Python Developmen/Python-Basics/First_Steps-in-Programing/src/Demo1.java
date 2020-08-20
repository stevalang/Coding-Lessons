import java.util.Scanner;

public class Demo1 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int oddNumber = Integer.parseInt(scanner.nextLine());
        int evenNumber = Integer.parseInt(scanner.nextLine());

        System.out.println(oddNumber % 2);
        System.out.println(evenNumber % 2);
    }
}
