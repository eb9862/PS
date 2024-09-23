import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(bf.readLine());

        for (int i = 0; i < t; i++) {
            int l, r, s, step;
            step = 1;
            StringTokenizer st = new StringTokenizer(bf.readLine());
            l = Integer.parseInt(st.nextToken());
            r = Integer.parseInt(st.nextToken());
            s = Integer.parseInt(st.nextToken());

            while (true) {
                switch (step % 2) {
                    case 0 -> s -= step;
                    case 1 -> s += step;
                };
                step++;
                if (s == l || s == r) {
                    break;
                }
            }
            System.out.println(step);
        }
    }
}