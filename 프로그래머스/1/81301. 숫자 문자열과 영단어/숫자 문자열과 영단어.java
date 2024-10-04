import java.lang.StringBuilder;

public class Solution {

    public static void main(String[] args) {
        solution("1zerotwozero3");
    }

    public static int solution(String s) {
        StringBuilder sb = new StringBuilder();
        char[] sArr = s.toCharArray();
        int l = 0;
        int r = 0;
        while (r < s.length()) {
            while (r < s.length() && Character.isDigit(sArr[r])) {
                sb.append(sArr[r]);
                r++;
            }
            if (r == s.length()) {
                break;
            }
            l = r;
            r = Math.min(r + 3, s.length());
            int num = 0;
            do {
                String word = s.substring(l, r);
                //System.out.println("word = " + word);
                num = wordToNum(word);
                if (num == -1) {
                    r++;
                }
            } while (r < s.length() + 1 && num == -1);
            //System.out.println("num = " + num);
            sb.append(num);
        }
        int answer = Integer.parseInt(sb.toString());
        //System.out.println(answer);
        return answer;
    }

    static int wordToNum(String word) {
        int result =
            switch (word) {
                case "zero" -> 0;
                case "one" -> 1;
                case "two" -> 2;
                case "three" -> 3;
                case "four" -> 4;
                case "five" -> 5;
                case "six" -> 6;
                case "seven" -> 7;
                case "eight" -> 8;
                case "nine" -> 9;
                default -> -1;
            };
        return result;
    }
}
