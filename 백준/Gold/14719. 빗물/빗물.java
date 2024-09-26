import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int h, w;
    static int[] heights;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in)
        );
        StringTokenizer st = new StringTokenizer(br.readLine());
        h = Integer.parseInt(st.nextToken());
        w = Integer.parseInt(st.nextToken());
        heights = new int[w];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < w; i++) {
            heights[i] = Integer.parseInt(st.nextToken());
        }

        if (h == 1 && w == 1) {
            System.out.println(0);
            return;
        }

        int idx = 0;
        int result = 0;
        while (idx < w) {
            int hOfWall = Math.min(leftMax(idx), rightMax(idx));
            if (heights[idx] < hOfWall) {
                result += hOfWall - heights[idx];
            }
            idx++;
        }
        System.out.println(result);
    }

    static int leftMax(int currentIdx) {
        int maxValue = heights[0];
        if (currentIdx == 0) {
            return 0;
        } else {
            for (int i = 1; i < currentIdx; i++) {
                if (maxValue < heights[i]) {
                    maxValue = heights[i];
                }
            }
            return maxValue;
        }
    }

    static int rightMax(int currentIdx) {
        int maxValue = heights[heights.length - 1];
        if (currentIdx == heights.length - 1) {
            return 0;
        } else {
            for (int i = currentIdx + 1; i < heights.length - 1; i++) {
                if (maxValue < heights[i]) {
                    maxValue = heights[i];
                }
            }
            return maxValue;
        }
    }
}
