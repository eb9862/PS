import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static String s;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(
            new InputStreamReader(System.in)
        );
        s = bf.readLine();

        int i = 0;
        while (i < s.length()) {
            if (isCanPronounce(i) > 0) {
                i += isCanPronounce(i);
            } else {
                System.out.println("NO");
                return;
            }
        }
        System.out.println("YES");
    }

    static int isCanPronounce(int idx) {
        String twoLetters = s.substring(idx, Math.min(idx + 2, s.length()));
        String threeLetters = s.substring(idx, Math.min(idx + 3, s.length()));
        if (twoLetters.equals("pi") || twoLetters.equals("ka")) {
            return 2;
        } else if (threeLetters.equals("chu")) {
            return 3;
        } else {
            return -1;
        }
    }
}
