import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in)
        );

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int s = Integer.parseInt(st.nextToken());

        List<Integer> numbers = new ArrayList<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            int number = Integer.parseInt(st.nextToken());
            numbers.add(number);
        }

        List<Integer> prefixSums = new ArrayList<>();
        prefixSums.add(0);
        int sum = 0;
        for (int i = 0; i < n; i++) {
            int number = numbers.get(i);
            sum += number;
            prefixSums.add(sum);
        }

        int result = n + 1;
        for (int length = n; length > 0; length--) {
            boolean pass = false;
            for (
                int startIndex = 0;
                startIndex + length < n + 1;
                startIndex++
            ) {
                int subtotal =
                    prefixSums.get(startIndex + length) -
                    prefixSums.get(startIndex);
                if (subtotal >= s) {
                    result = length;
                    pass = true;
                    break;
                }
            }
            if (!pass) {
                break;
            }
        }
        if (result == n + 1) {
            System.out.println(0);
            return;
        }
        System.out.println(result);
    }
}
