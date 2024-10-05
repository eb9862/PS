import java.util.Queue;
import java.util.LinkedList;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        
        Queue <String> cache = new LinkedList<>();
        int l = 0;
        for (String city : cities) {
            String target = city.toLowerCase();
            if (cache.contains(target)) {
                cache.remove(target);
                cache.add(target);
                answer++;
            } else {
                if (l < cacheSize) {
                    cache.add(target);
                    l++;
                } else {
                    if (cacheSize != 0) {
                        cache.poll();
                        cache.add(target);
                    }
                }
                answer += 5;
            }
        }
        System.out.println(answer);
        
        return answer;
    }
}