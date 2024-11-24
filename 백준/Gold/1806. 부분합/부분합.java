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

        int sum = numbers.get(0);
        int startIndex = 0;
        int endIndex = 0;
        int result = n + 1;
        while (endIndex < n) {
            if (sum < s) {
                endIndex++;
                if (endIndex < n) {
                    sum += numbers.get(endIndex);
                }
                continue;
            }
            int length = endIndex - startIndex + 1;
            if (result > length) {
                result = length;
            }
            sum -= numbers.get(startIndex);
            startIndex++;
        }

        if (result == n + 1) {
            System.out.println(0);
            return;
        }
        System.out.println(result);
    }
}
