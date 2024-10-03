import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in)
        );
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        Record[] records = new Record[n];
        int maxNation = 1;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int nation = Integer.parseInt(st.nextToken());
            if (nation != maxNation) {
                maxNation = nation;
            }
            int studentNum = Integer.parseInt(st.nextToken());
            int score = Integer.parseInt(st.nextToken());
            records[i] = new Record(nation, studentNum, score);
        }

        Comparator<Record> comparator = new Comparator<Record>() {
            @Override
            public int compare(Record a, Record b) {
                if (a.score != b.score) {
                    return (b.score - a.score);
                }
                return 0;
            }
        };

        Arrays.sort(records, comparator);
        int[] numsOfMedal = new int[maxNation + 1];
        int print = 0;
        for (int i = 0; i < n; i++) {
            int nationCode = records[i].nation;
            if (print < 3 && numsOfMedal[nationCode] < 2) {
                System.out.println(nationCode + " " + records[i].studentNum);
                print++;
                numsOfMedal[nationCode]++;
            }
        }
    }

    static class Record {

        int nation;
        int studentNum;
        int score;

        public Record(int nation, int studentNum, int score) {
            this.nation = nation;
            this.studentNum = studentNum;
            this.score = score;
        }
    }
}
