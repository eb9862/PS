import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();

            int l = ba(a, b);
            int c = l;
            int h = ab(a, b);
            
            while (l % h != 0) {
                l += c;
            }
            System.out.println(l);
        }
    }

    public static int ab(int a, int b) {

        if (a >= b)
            return a;
        return b;
    }

    public static int ba(int a, int b) {

        if (a > b)
            return b;
        return a;
    }
}
