import java.io.*;

public class Main {

    static int n;
    static BufferedWriter bw;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        n = Integer.parseInt(br.readLine());

        makeNum(0, 0);
        bw.flush();
        bw.close();
    }

    static void makeNum(int num, int l) throws IOException {
        if (!isPrime(num)) {
            return;
        } else {
            if (l == n) {
                bw.write(num + "\n");
                return;
            }
        }
        num *= 10;
        for (int i = 0; i < 10; i++) {
            if (l == 0) {
                if (i != 0) {
                    makeNum(num + i, l + 1);
                }
            } else {
                makeNum(num + i, l + 1);
            }

        }
    }

    static boolean isPrime(int num) {
        if (num == 1) {
            return false;
        }
        int end = (int) Math.sqrt(num) + 1;
        for (int i = 2; i < end; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}