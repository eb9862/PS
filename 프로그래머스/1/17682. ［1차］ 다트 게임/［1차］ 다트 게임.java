class Solution {
    
    static char[] str;
    static int i;
    
    public int solution(String dartResult) {
        int[] scores = new int[3];
        
        int scoreIdx = 0;
        i = 0;
        str = dartResult.toCharArray();
        while (i < str.length) {
    
            scores[scoreIdx] = checkScore();
            
            if (i < str.length && !Character.isDigit(str[i])) {
                if (str[i] == '*') {
                    scores[scoreIdx] *= 2;
                    if (scoreIdx != 0) {
                        scores[scoreIdx - 1] *= 2;
                    }
                } else if (str[i] == '#') {
                    scores[scoreIdx] *= -1;
                }
                i++;
            }
            scoreIdx++;
        }
        
        int answer = 0;
        for (int score : scores) {
            answer += score;
        }
        System.out.println(answer);
        return answer;
    }
                
    static int checkScore() {
        int score;
        if (i < str.length - 1 && str[i+1] == '0') {
            score = 10;
            i += 2;
        } else {
            score = str[i] - '0';
            i++;
        }
        
        if (i < str.length) {
            score = checkZone(score);
            i++;
        }
        
        return score;
    }
    
    static int checkZone(int score) {
        if (str[i] == 'S') {
            return score;
        } else if (str[i] == 'D') {
            return (int) Math.pow(score, 2);
        } else {
            return (int) Math.pow(score, 3);
        }
    }
}