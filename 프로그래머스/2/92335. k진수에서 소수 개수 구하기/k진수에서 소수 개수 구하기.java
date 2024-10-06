import java.lang.StringBuilder;

class Solution {
    
    static StringBuilder sb;
    
    public int solution(int n, int k) {
        sb = new StringBuilder();
        knary(n, k);
        String knary = sb.toString();
        char[] knaryArr = knary.toCharArray();
        
        int l = 0;
        int r = 0;
        int answer = 0;
        while (r < knaryArr.length) {
            while (r < knaryArr.length && knaryArr[r] - '0' == 0) {
                r++;
            }
            l = r;
            while (r < knaryArr.length && knaryArr[r] - '0' != 0) {
                r++;
            }
            if (l != r) {
                long checkNum = Long.parseLong(knary.substring(l, r));
                if (isPrimary(checkNum)) {
                    answer++;
                }
            }
            
        }
        // int answer = 0;
        // String[] nums = knary.split("0");
        // for (String num : nums) {
        //     if (!num.equals("")) {
        //         int checkNum = Integer.parseInt(num);
        //         if (isPrimary(checkNum)) {
        //         answer++;
        //         }
        //     }  
        // }
        return answer;
    }
    
    static void knary(int num, int k) {
        if (num == 0) {
            return;
        }
        knary(num / k, k);
        sb.append(num % k);
    }
    
    static boolean isPrimary(long num) {
        if (num == 0 || num == 1) {
            return false;
        }
        
        int end = (int) Math.sqrt(num) + 1;
        for (int i = 2; i < end; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}