import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in)
        );
        int n = Integer.parseInt(br.readLine());
        int[] cards = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            cards[i] = Integer.parseInt(st.nextToken());
        }

        int result = 0;
        for (int i = 0; i < n - 1; i++) {
            int sub = cards[i + 1] - cards[i];
            int nextValue = cards[i] + sub;
            int seq = 1;
            //System.out.println("sub = " + sub);
            for (int j = i; j < n - 1; j++) {
                if (cards[j + 1] == nextValue) {
                    seq++;
                }
                nextValue += sub;
            }
            //System.out.println("seq = " + seq);
            if (result < seq) {
                result = seq;
            }
            //System.out.println("----------------");
        }
        System.out.println(n - result);
    }
}