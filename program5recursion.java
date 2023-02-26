import java.util.Scanner;

public class StringReverseRecursion {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the string:");
        String str = scanner.nextLine();
        String reversedStr = reverse(str);
        System.out.println("Reversed string: " + reversedStr);
    }

    public static String reverse(String str) {
        if (str.isEmpty()) {
            return str;
        }
        return reverse(str.substring(1)) + str.charAt(0);
    }

}
