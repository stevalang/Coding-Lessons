import java.util.Scanner;

public class GreetingbyName {
    public static void main(String[] args) {
        Scanner scanner =  new Scanner(System.in);
        String  name = scanner.nextLine();
        String hello = "Hello, ";
        String punc = "!";
        System.out.println(hello  + name + punc);

    }
}
