import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in)
        );
        StringTokenizer st = new StringTokenizer(br.readLine());

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        int result =
            calculateFirstToNth(b) -
            calculateFirstToNth(a) +
            calculateNthNumber(a);
        System.out.println(result);
    }

    static int calculateFirstToNth(int n) {
        int nthNumber = calculateNthNumber(n);
        int sum = 0;
        for (int i = 1; i < nthNumber + 1; i++) {
            sum += Math.pow(i, 2);
        }

        int lastIndexOfNthNumber = calculateOneToN(nthNumber);
        sum -= (lastIndexOfNthNumber - n) * nthNumber;
        return sum;
    }

    static int calculateNthNumber(int ordinalNumber) {
        int number = 1;
        while (true) {
            if (calculateOneToN(number) >= ordinalNumber) {
                break;
            }
            number++;
        }
        return number;
    }

    static int calculateOneToN(int n) {
        int sum = 0;
        for (int i = 1; i < n + 1; i++) {
            sum += i;
        }
        return sum;
    }
}
