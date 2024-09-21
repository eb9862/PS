import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[][] nations = new int[n][4];
        int[] target = new int[4];
        for (int i = 0; i < n; i++) {
            String in = br.readLine();
            String[] info = in.split(" ");
            for (int j = 0; j < 4; j++) {
                if (nations[i][0] == k) {
                    target[j] = Integer.parseInt(info[j]);
                }
                nations[i][j] = Integer.parseInt(info[j]);
            }
        }
        
        Arrays.sort(nations, (o1, o2) -> {
            if (o1[1] != o2[1]) {
                return o2[1] - o1[1];
            } else if (o1[2] != o2[2]) {
                return o2[2] - o1[2];
            } else {
                return o2[3] - o1[3];
            }
        });

        for (int i = 0; i < n; i++) {
            if (isSameScore(nations[i], target)) {
                System.out.println(i+1);
                return;
            }
        }
    }

    static boolean isSameScore(int[] nation, int[] target) {
        for (int i = 1; i < 4; i++) {
            if (nation[i] != target[i]) {
                return false;
            }
        }
        return true;
    }
}
