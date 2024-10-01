import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        char[] s = br.readLine().toCharArray();
        StringBuilder result = new StringBuilder();

        int i = 0;
        int numOfX = 0;
        while (i < s.length) {
            while (i < s.length && s[i] != 'X') {
                result.append(".");
                i++;
            }
            numOfX = 0;
            while (i < s.length && s[i] == 'X') {
                numOfX++;
                i++;
            }
            if (numOfX % 2 == 1) {
                System.out.println(-1);
                return;
            } else {
                for (int j = 0; j < numOfX / 4; j++) {
                    result.append("AAAA");
                }
                numOfX %= 4;
                for (int j = 0; j < numOfX / 2; j++) {
                    result.append("BB");
                }
            }
        }

        System.out.println(result);

    }
}
