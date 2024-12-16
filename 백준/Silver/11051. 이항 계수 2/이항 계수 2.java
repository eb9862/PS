import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    private static int N, K;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in)
        );
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        long[][] pascalTriangle = new long[N + 1][N + 1];
        for (int i = 1; i < N + 1; i++) {
            for (int j = 0; j < i + 1; j++) {
                if (j == 1) {
                    pascalTriangle[i][j] = i;
                    continue;
                } else if (j == i || j == 0) {
                    pascalTriangle[i][j] = 1;
                    continue;
                }
                pascalTriangle[i][j] =
                    pascalTriangle[i - 1][j - 1] +
                    (pascalTriangle[i - 1][j] % 10007);
            }
        }
        System.out.println(pascalTriangle[N][K] % 10007);
    }
}
