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
            StringTokenizer st = new StringTokenizer(bf.readLine());
            l = Integer.parseInt(st.nextToken());
            r = Integer.parseInt(st.nextToken());
            s = Integer.parseInt(st.nextToken());

            step = 1;
            if ((s - l) < (r - s)) {
                step += (s - l) * 2;
            } else {
                step += (r - s) * 2 - 1;
            }
            System.out.println(step);
        }
    }
}