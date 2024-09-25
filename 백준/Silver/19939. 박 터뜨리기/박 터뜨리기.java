import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int n;
    static int k;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in)
        );
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        int sumValue = oneToK();
        if (k > n || sumValue > n) {
            System.out.println(-1);
            return;
        } else {
            if ((n - sumValue) % k == 0) {
                System.out.println(k - 1);
            } else {
                System.out.println(k);
            }
        }
    }

    static int oneToK() {
        return (k * (k + 1)) / 2;
    }
}
