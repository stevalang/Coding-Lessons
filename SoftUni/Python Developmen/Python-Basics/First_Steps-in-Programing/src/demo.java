import java.util.Scanner;

public class demo {
    public static void main(String[] args) {
        Scanner scanner= new Scanner(System.in);

        String firstName =scanner.nextLine();
        String secoundtName =scanner.nextLine();
        String ageInput =scanner.nextLine();
        int age = Integer.parseInt(ageInput);

        String resultMessage = firstName + " " + secoundtName + "@" + (age + 1);
        String resultMessage2 = firstName + " " + secoundtName + "@" + ageInput;

        System.out.println(resultMessage);
        System.out.println(resultMessage2);



    }
}
