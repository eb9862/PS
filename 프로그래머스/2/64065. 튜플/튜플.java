

class Solution {
    
    public int[] solution(String s) {
        
        int size = calSize(s);
        System.out.println(size);
        
        int[] answer = new int[size];
        
        for (int i = 0; i < size; i++) {
            String[] set = getNSizeSet(s, i);
            if (i == 0) {
                answer[0] = Integer.parseInt(set[0]);
            }
            for (String str : set) {
                if (!isIncluded(str, answer, i)) {
                    answer[i] = Integer.parseInt(str);
                    break;
                }
            }
        }
        
        return answer;
    }
    
    static boolean isIncluded(String str, int[] answer, int checkSize) {
        for (int i = 0; i < checkSize; i++) {
            if (answer[i] == Integer.parseInt(str)) {
                return true;
            }
        }
        return false;
    }
    
    static String[] getNSizeSet(String s, int n) {
        char[] str = s.toCharArray();
        
        int r = 1;
        int l = 0;
        while (r < str.length - 1) {
            int numOfComma = 0;
            while (str[r] != '{') {
                r++;
            }
            l = r + 1;
            r++;
            while (str[r] != '}') {
                if (str[r] == ',') {
                    numOfComma++;
                }
                r++;
            }
            if (numOfComma == n) {
                break;
            }
        }
        return s.substring(l, r).split(",");
    }
    
    static int calSize(String s) {
        String[] strs = s.split(",");
        //System.out.println(Arrays.toString(strs));
        int size = 1;
        while (true) {
            int cnt = size * (size + 1) / 2;
            if (cnt == strs.length) {
                return size;
            }
            size++;
        }
    }
}