import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static int n, result;
    static int[] numbers, newNumbers;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        numbers = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            numbers[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(numbers);
        //System.out.println(Arrays.toString(numbers));

        newNumbers = new int[n];
        int[] visited = new int[n];
        Arrays.fill(visited, -1);
        //System.out.println(Arrays.toString(visited));
        calPermutation(0, visited);
        //System.out.println(Arrays.toString(newNumbers));

        System.out.println(result);
    }

    static int calMax(int[] numbers) {
        int sumValue = 0;
        for (int i = 0; i < n - 1; i++) {
            sumValue += Math.abs(numbers[i] - numbers[i + 1]);
        }
        return sumValue;
    }

    static void calPermutation(int l, int[] visited) {
        if (l == n) {
            //System.out.println(Arrays.toString(newNumbers));
            int sumValue = calMax(newNumbers);
            if (result < sumValue) {
                result = sumValue;
            }
        }
        for (int i = 0; i < n; i++) {
            if (l == 0) {
                newNumbers[l] = numbers[i];
                visited[l] = i;
                calPermutation(l + 1, visited);
            } else {
                if (!isVisited(visited, i, l)) {
                    newNumbers[l] = numbers[i];
                    visited[l] = i;
                    calPermutation(l + 1, visited);
                }
            }
        }
    }

    static boolean isVisited(int[] visited, int idx, int l) {
        for (int i = 0; i < l; i++) {
            if (visited[i] == idx) {
                return true;
            }
        }
        return false;
    }
}