#reverse a string using recursion in java
public class ReverseString {
public static String reverse(String str) {
        // base case
        if (str.isEmpty()) {
            return str;
        }
        // recursive case
        else {
            return reverse(str.substring(1)) + str.charAt(0);
        }
    }
    public static void main(String[] args) {
        String str = "hello world";
        System.out.println(reverse(str)); // prints "dlrow olleh"
    }
}
