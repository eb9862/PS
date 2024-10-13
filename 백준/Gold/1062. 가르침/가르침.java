import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static boolean[] alpha;
    static String[] words;
    static int n, k;
    static int result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in)
        );
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        words = new String[n];
        for (int i = 0; i < n; i++) {
            words[i] = br.readLine();
            words[i] = words[i].substring(4, words[i].length() - 4);
        }

        if (k < 5) {
            System.out.println(0);
            return;
        }

        alpha = new boolean[26]; // boolean initial value = false
        initAlpha();

        result = 0;
        selectAlpha(0, 0);
        System.out.println(result);
    }

    static void initAlpha() {
        alpha['a' - 'a'] = true;
        alpha['n' - 'a'] = true;
        alpha['t' - 'a'] = true;
        alpha['i' - 'a'] = true;
        alpha['c' - 'a'] = true;
    }

    /*static boolean canRead(String s) {
        char[] chars = s.toCharArray();
        for (char c : chars) {
            if (!alpha[c - 'a']) {
                return false;
            }
        }
        return true;
    }*/

    static void selectAlpha(int idx, int l) {
        if (l == k - 5) {
            int readValue = 0;
            for (String s : words) {
                boolean flag = true;
                for (int i = 0; i < s.length(); i++) {
                    if (!alpha[s.charAt(i) - 'a']) {
                        flag = false;
                    }
                }
                if (flag) {
                    readValue++;
                }
            }
            if (readValue > result) {
                result = readValue;
            }
            return;
        }
        for (int i = idx; i < 26; i++) {
            if (alpha[i] == false) {
                alpha[i] = true;
                selectAlpha(i + 1, l + 1);
                alpha[i] = false;
            }
        }
    }
}
