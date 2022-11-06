import java.util.Scanner;

public class JavaScanner {
    public static void main(String[] args) {
        Scanner ui = new Scanner(System.in);
        System.out.print("HEY. WHO ARE YOU???? >>> ");
        String output = ui.nextLine();
        System.out.println(output);
        output = null;
        ui.close();
    }
}