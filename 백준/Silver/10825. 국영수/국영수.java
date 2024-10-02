import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in)
        );
        BufferedWriter bw = new BufferedWriter(
            new OutputStreamWriter(System.out)
        );
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        GookYoungSoo[] students = new GookYoungSoo[n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            int gook = Integer.parseInt(st.nextToken());
            int young = Integer.parseInt(st.nextToken());
            int soo = Integer.parseInt(st.nextToken());
            students[i] = new GookYoungSoo(name, gook, young, soo);
        }

        Comparator<GookYoungSoo> comparator = new Comparator<GookYoungSoo>() {
            @Override
            public int compare(GookYoungSoo a, GookYoungSoo b) {
                if (a.gook != b.gook) {
                    return b.gook - a.gook;
                } else if (a.young != b.young) {
                    return a.young - b.young;
                } else if (a.soo != b.soo) {
                    return b.soo - a.soo;
                } else {
                    return a.name.compareTo(b.name);
                }
            }
        };

        Arrays.sort(students, comparator);
        for (int i = 0; i < n; i++) {
            bw.write(students[i].name);
            bw.newLine();
        }
        bw.flush();
        bw.close();
    }

    static class GookYoungSoo {

        String name;
        int gook;
        int young;
        int soo;

        GookYoungSoo(String name, int gook, int young, int soo) {
            this.name = name;
            this.gook = gook;
            this.young = young;
            this.soo = soo;
        }
    }
}
