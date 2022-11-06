import java.util.Scanner;
import java.util.ArrayList;

public class GPACalc {
    public static void main(String[] args) {
        ArrayList<String> courses = new ArrayList<String>();
        Scanner ui = new Scanner(System.in);
        System.out.println("Enter your courses... Type q to quit entering.");
        while (true) {
            System.out.print(">>> ");
            String output = ui.nextLine();
            if (output.equals("q")) {
                break;
            }else{
                courses.add(output);
            }
        }
        float average = 0f;
        System.out.println("Enter your course percents...");
        for (String i : courses) {
            System.out.print(i+"% >>> ");
            Float output = ui.nextFloat();
            average=average+output;
        }
        System.out.print("GPA >>> "+((average/courses.size())/20 - 1));
        ui.close();
    }
}