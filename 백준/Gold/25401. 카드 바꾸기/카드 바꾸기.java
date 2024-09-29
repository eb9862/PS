import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int n, result;
    static int[] cards;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new InputStreamReader(System.in)
        );
        n = Integer.parseInt(br.readLine());
        cards = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            cards[i] = Integer.parseInt(st.nextToken());
        }

        result = 0;
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                int sub = (cards[j] - cards[i]) / (j - i); // j - i 괄호 안해줬었음..
                double doubleSub = (double) (cards[j] - cards[i]) / (j - i);
                if (doubleSub != sub) {
                    continue;
                }
                checkFromIdx(i, sub);
            }
        }
        System.out.println(n - result);
    }

    static void checkFromIdx(int idx, int sub) {
        int seq = 1;
        int prevValue = cards[idx] - sub;
        for (int j = idx; j > 0; j--) {
            if (cards[j - 1] == prevValue) {
                seq++;
            }
            prevValue -= sub;
        }
        int nextValue = cards[idx] + sub;
        for (int j = idx; j < n - 1; j++) {
            if (cards[j + 1] == nextValue) {
                seq++;
            }
            nextValue += sub;
        }
        if (result < seq) {
            result = seq;
        }
    }
}