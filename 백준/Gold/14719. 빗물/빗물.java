// import java.io.BufferedReader;
// import java.io.IOException;
// import java.io.InputStreamReader;
// import java.util.StringTokenizer;

// public class Main {

//     static int n;
//     static int k;

//     public static void main(String[] args) throws IOException {
//         BufferedReader br = new BufferedReader(
//             new InputStreamReader(System.in)
//         );
//         StringTokenizer st = new StringTokenizer(br.readLine());

//         n = Integer.parseInt(st.nextToken());
//         k = Integer.parseInt(st.nextToken());

//         int sumValue = oneToK();
//         if (k > n || sumValue > n) {
//             System.out.println(-1);
//             return;
//         } else {
//             if ((n - sumValue) % k == 0) {
//                 System.out.println(k - 1);
//             } else {
//                 System.out.println(k);
//             }
//         }
//     }

//     static int oneToK() {
//         return (k * (k + 1)) / 2;
//     }
// }

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

        if ((h == 1 && w == 1) || w == 2) {
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
            for (int i = 0; i < currentIdx; i++) {
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
            for (int i = currentIdx + 1; i < heights.length; i++) {
                if (maxValue < heights[i]) {
                    maxValue = heights[i];
                }
            }
            return maxValue;
        }
    }
}
