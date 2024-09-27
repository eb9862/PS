import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

    static int n;
    static char[][] candy;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in)
        );

        n = Integer.parseInt(br.readLine());
        candy = new char[n][n];
        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            candy[i] = s.toCharArray();
        }

        int result = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i != n - 1) {
                    verticalSwap(i, j);
                    int maxValue = Math.max(verticalMax(), horizontalMax());
                    verticalSwap(i, j);
                    if (maxValue > result) {
                        result = maxValue;
                    }
                }
                if (j != n - 1) {
                    horizontalSwap(i, j);
                    int maxValue = Math.max(verticalMax(), horizontalMax());
                    horizontalSwap(i, j);
                    if (maxValue > result) {
                        result = maxValue;
                    }
                }
            }
        }
        System.out.println(result);
    }

    static void verticalSwap(int row, int col) {
        char temp = candy[row][col];
        candy[row][col] = candy[row + 1][col];
        candy[row + 1][col] = temp;
    }

    static void horizontalSwap(int row, int col) {
        char temp = candy[row][col];
        candy[row][col] = candy[row][col + 1];
        candy[row][col + 1] = temp;
    }

    static int verticalMax() {
        int colMaxValue = 1;
        for (int i = 0; i < n; i++) {
            int thisLineValue = oneColMax(i);
            if (colMaxValue < thisLineValue) {
                colMaxValue = thisLineValue;
            }
        }
        return colMaxValue;
    }

    static int oneColMax(int col) {
        int total = 1;
        int result = 0;
        for (int i = 0; i < n - 1; i++) {
            if (candy[i][col] == candy[i + 1][col]) {
                total++;
            } else {
                if (result < total) {
                    result = total;
                }
                total = 1;
            }
        }
        if (result < total) {
            result = total;
        }
        return result;
    }

    static int horizontalMax() {
        int rowMaxValue = 1;
        for (int i = 0; i < n; i++) {
            int thisLineValue = oneRowMax(i);
            if (rowMaxValue < thisLineValue) {
                rowMaxValue = thisLineValue;
            }
        }
        return rowMaxValue;
    }

    static int oneRowMax(int row) {
        int total = 1;
        int result = 0;
        for (int i = 0; i < n - 1; i++) {
            if (candy[row][i] == candy[row][i + 1]) {
                total++;
            } else {
                if (result < total) {
                    result = total;
                }
                total = 1;
            }
        }
        if (result < total) {
            result = total;
        }
        return result;
    }
}
