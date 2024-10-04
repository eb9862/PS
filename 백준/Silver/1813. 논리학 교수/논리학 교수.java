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
        int[] contents = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        int maxValue = 0;
        for (int i = 0; i < n; i++) {
            contents[i] = Integer.parseInt(st.nextToken());
            if (maxValue < contents[i]) {
                maxValue = contents[i];
            }
        }

        int[] cnt = new int[maxValue + 1];
        for (int i = 0; i < n; i++) {
            int idx = contents[i];
            cnt[idx]++;
        }

        int result = -1;
        for (int i = 0; i < maxValue + 1; i++) {
            if (cnt[i] == i) {
                result = i;
            }
        }
        System.out.println(result);
    }
}