class Solution {
    
    static int turn, maxTurn;
    static String base;
    static StringBuilder baseNnum;
    
    public String solution(int n, int t, int m, int p) {
        
        base = getBase(n);
        //System.out.println("base = " + base);
        baseNnum = new StringBuilder("");
        
        turn = 1;
        maxTurn = m * (t-1) + p;
        int num = 0;
        
        if (isMyTurn(m, p)) {
            baseNnum.append(base.charAt(num % n));
        }
        turn++;
        
        while (turn <= maxTurn) {
            getBaseNnum(num, n, m, p);
            num++;
        }
        
        String answer = baseNnum.toString();
        return answer;
    }
    
    static void getBaseNnum(int i, int n, int m, int p) {
        if (i == 0) {
            return;
        }
        getBaseNnum(i / n, n, m, p);
        if (isMyTurn(m, p)) {
            baseNnum.append(base.charAt(i % n));
        }
        turn++;
    }
    
    static boolean isMyTurn(int m, int p) {
        if (m != p) {
            if (turn % m == p && turn <= maxTurn) {
                return true;
            }
            return false;
        } else {
            if (turn % m == 0 && turn <= maxTurn) {
                return true;
            }
            return false;
        }
        
    }
    
    static String getBase(int n) {
        StringBuilder sb = new StringBuilder("");
        int end = Math.min(n, 10);
        for (int i = 0; i < end; i++) {
            sb.append(i+"");
        }
        if (n > 10) {
            char c = 'A';
            for (int i = 0; i < n - 10; i++) {
                sb.append(c);
                c++;
            }
        }
        return sb.toString();
    }
}