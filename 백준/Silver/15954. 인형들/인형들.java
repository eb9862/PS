import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int[] dolls;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in)
        );
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        dolls = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            dolls[i] = Integer.parseInt(st.nextToken());
        }

        double result = Double.MAX_VALUE;
        for (int j = k; j < n + 1; j++) {
            for (int i = 0; i < n - j + 1; i++) {
                double variance = calVar(i, j);
                if (variance < result) {
                    result = variance;
                }
            }
        }
        double stdDeviation = Math.sqrt(result);
        System.out.println(stdDeviation);
    }

    static double calVar(int idx, int cnt) {
        double sumValue = 0;
        double avg = calAvg(idx, cnt);
        for (int i = idx; i < idx + cnt; i++) {
            double sub = dolls[i] - avg;
            sumValue += Math.pow(sub, 2);
        }
        return sumValue / cnt;
    }

    static double calAvg(int idx, int cnt) {
        double sumValue = 0;
        for (int i = idx; i < idx + cnt; i++) {
            sumValue += dolls[i];
        }
        return sumValue / cnt;
    }
}