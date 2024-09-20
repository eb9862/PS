import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        for (int i = 0; i < n; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            int gcd = calGcd(a, b);
            int lcm = gcd * (a / gcd) * (b / gcd);
            System.out.println(lcm);
        }
    }

    public static int calGcd(int a, int b) {
        int remain;
        if (a > b) {
            remain = a % b;
            if (remain == 0) {
                return b;
            }
            return calGcd(b, remain);
        } else {
            remain = b % a;
            if (remain == 0) {
                return a;
            }
            return calGcd(a, remain);
        }
    }
}