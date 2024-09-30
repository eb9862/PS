import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in)
        );

        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int grade1 = Integer.parseInt(st.nextToken());
            int grade2 = Integer.parseInt(st.nextToken());
            int totalPrize = getFirstPrize(grade1) + getSecondPrize(grade2);
            System.out.println(totalPrize);
        }
    }

    static int getFirstGrade(int grade1) {
        if (grade1 == 0) {
            return 0;
        }
        int grade = 1;
        for (int firstGrade = 1; firstGrade < 7; firstGrade++) {
            grade += firstGrade;
            if (grade1 < grade) {
                return firstGrade;
            }
        }
        return 0;
    }

    static int getFirstPrize(int grade1) {
        int prize =
            switch (getFirstGrade(grade1)) {
                case 1 -> 5000000;
                case 2 -> 3000000;
                case 3 -> 2000000;
                case 4 -> 500000;
                case 5 -> 300000;
                case 6 -> 100000;
                default -> 0;
            };
        return prize;
    }

    static int getSecondGrade(int grade2) {
        if (grade2 == 0) {
            return 0;
        }
        int secondGrade = 1;
        while (true) {
            if (grade2 < Math.pow(2, secondGrade)) {
                return secondGrade;
            }
            secondGrade++;
        }
    }

    static int getSecondPrize(int grade2) {
        int prize =
            switch (getSecondGrade(grade2)) {
                case 1 -> 5120000;
                case 2 -> 2560000;
                case 3 -> 1280000;
                case 4 -> 640000;
                case 5 -> 320000;
                default -> 0;
            };
        return prize;
    }
}
