import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int n = sc.nextInt();

        a = a % b;
        for (int i = 0; i < n; i++) {
            int remain = a % b;
            a = b > remain ? remain * 10 : remain;
        }
        System.out.println(a / b);
    }
}
