import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

    static int casesNumber = 1;
    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        N = Integer.parseInt(br.readLine());
        int rangeValue = N/2 + 1;
        for (int endNumber = rangeValue; endNumber > 0; endNumber--) {
            for (int startNumber = endNumber; startNumber > 0; startNumber--) {
                long sum = calculateSumOfContinuousNumbers(startNumber, endNumber);
                if (sum > N) {
                    break;
                }
                checkCondition(sum);
            }
        }
        if (N == 1 || N == 2) {
            bw.write("1");
        } else {
            bw.write(casesNumber + "");
        }
        bw.flush();
        bw.close();
    }

    static long calculateSumOfContinuousNumbers(int startNumber, int endNumber) {
        return calculateOneToN(endNumber) - calculateOneToN(startNumber - 1);
    }

    static long calculateOneToN(int n) {
        return (long) n * (n + 1) / 2;
    }

    static void checkCondition(long sumValue) {
        if (sumValue == N) {
            casesNumber++;
        }
    }
}