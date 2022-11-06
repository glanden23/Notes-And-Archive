/*
Sources:
https://stackoverflow.com/questions/7070209/converting-integer-to-string-with-comma-for-thousands
https://www.w3schools.com/java/java_arrays.asp
*/
import java.text.NumberFormat;

public class HelloWorld {
    public static void main(String[] args) {
        int n = 0;
        while (true) {
            n=n+1;
            System.out.println("Hello World! x" + NumberFormat.getIntegerInstance().format(n));
        }
    }
}