import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class Main {

    static int nthIndex = 2;
    static int countPerTestCase = 10;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in)
        );

        int testCount = Integer.parseInt(br.readLine());

        for (int i = 0; i < testCount; i++) {
            String[] input = br.readLine().split(" ");
            List<Integer> testCase = new ArrayList<>();
            for (int j = 0; j < countPerTestCase; j++) {
                String number = input[j];
                testCase.add(Integer.valueOf(number));
            }
            testCase.sort(Comparator.reverseOrder());
            System.out.println(testCase.get(nthIndex));
        }
    }
}
