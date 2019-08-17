import java.io.Console;

public class Main {

    public static void main(String args[]) {
        System.out.println("Java hello world");

        Console c = System.console();
        c.format("\nPress ENTER to proceed.\n");
        c.readLine();
    }
}