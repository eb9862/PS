import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static int n, result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in)
        );

        n = Integer.parseInt(br.readLine());

        if (n < 10) {
            System.out.println(n);
            System.exit(0);
        }

        result = 9;
        for (int l = 2; l <= 10; l++) {
            long num = 0;              // 마지막 감소하는 수인 '9876543210'은 int 범위를 초과
            bt(num, 0, l);
        }
        System.out.println(-1);
    }

    static void bt(long num, int nowLen, int l) {
        if (nowLen == l) {
            result++;
            //System.out.println(result + "th : " + num);
            if (result == n) {
                System.out.println(num);
                System.exit(0);
            }
            return;
        }
        for (int i = 0; i < 10; i++) {
            if (nowLen == 0 && i != 0) {
                bt(num + i, nowLen + 1, l);
            }
            if (num % 10 > i) {
                bt(num * 10 + i, nowLen + 1, l);
            }
        }
    }
}
