import java.lang.StringBuilder;

class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        
        int[] preAnswer = new int[n];
        for (int i = 0; i < n; i++) {
            preAnswer[i] = arr1[i] | arr2[i];
        }
        
        String[] answer = new String[n];
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            int bit = 1 << n - 1;
            while (bit != 0) {
                if ((preAnswer[i] & bit) == 0) {
                    sb.append(" ");
                } else {
                    sb.append("#");
                }
                bit >>= 1;
            }
            answer[i] = sb.toString();
            sb = new StringBuilder();
        }
        
        return answer;
    }
}