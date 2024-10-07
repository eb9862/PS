import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int t = Integer.parseInt(st.nextToken());
        for (int i = 0; i < t; i++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int[] heights = new int[n];
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                heights[j] = Integer.parseInt(st.nextToken());
            }
            Arrays.sort(heights);
            Deque<Integer> dq = new ArrayDeque<>();
            for (int j = n - 1; j >= 0; j--) {
                if (j % 2 == 0) {
                    dq.addFirst(heights[j]);
                } else {
                    dq.add(heights[j]);
                }
            }

            int maxValue = 0;
            Integer[] arr = dq.toArray(new Integer[0]);
            for (int j = 0; j < n; j++) {
                int sub = (j == n - 1) ? Math.abs(arr[j] - arr[0]) : Math.abs(arr[j] - arr[j+1]);
                if (sub > maxValue) {
                    maxValue = sub;
                }
            }
            System.out.println(maxValue);
        }
    }
}