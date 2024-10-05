import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in)
        );

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] scores = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            scores[i] = Integer.parseInt(st.nextToken());
        }

        long maxScore = 0;
        int maxD = 0;
        for (int d = n; d > 0; d--) {
            long totalScore = 0;
            int share = n / d;
            for (int j = 1; j < share + 1; j++) {
                totalScore += scores[d * j];
            }
            if (maxScore <= totalScore) {
                maxScore = totalScore;
                maxD = d;
            }
        }
        BufferedWriter bw = new BufferedWriter(
            new OutputStreamWriter(System.out)
        );
        if (maxScore <= 0) {
            bw.write("0 0");
        } else {
            bw.write(maxD + " " + maxScore);
        }
        bw.flush();
        bw.close();
    }
}