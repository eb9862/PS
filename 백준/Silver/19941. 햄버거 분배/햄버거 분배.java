import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in)
        );
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        String loc = br.readLine();
        boolean[] canEat = new boolean[n];
        Arrays.fill(canEat, true);

        int result = 0;
        for (int i = 0; i < n; i++) {
            if (loc.charAt(i) == 'P') {
                if (checkLeft(loc, canEat, i, k) == 1) {
                    result++;
                } else {
                    if (checkRight(loc, canEat, i, k, n) == 1) {
                        result++;
                    }
                }
            }
        }
        System.out.println(result);
    }

    static int checkLeft(String loc, boolean[] canEat, int idx, int k) {
        int start = Math.max(idx - k, 0);
        int end = Math.max(idx - 1, 0);
        for (int i = start; i <= end; i++) {
            if (loc.charAt(i) == 'H' && canEat[i] == true) {
                canEat[i] = false;
                return 1;
            }
        }
        return 0;
    }

    static int checkRight(String loc, boolean[] canEat, int idx, int k, int n) {
        int start = Math.min(idx + 1, n - 1);  // loc.length()
        int end = Math.min(idx + k, n - 1);
        for (int i = start; i <= end; i++) {
            if (canEat[i] == true && loc.charAt(i) == 'H') {
                canEat[i] = false;
                return 1;
            }
        }
        return 0;
    }
}
