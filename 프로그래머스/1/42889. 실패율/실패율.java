import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int[] solution(int N, int[] stages) {
        Map<Integer, Integer> playerCountByStage = findPlayerCountByStage(N, stages); 
        
        Map<Integer, Double> failureRateByStage = new LinkedHashMap<>();
        
        playerCountByStage.forEach((stage, playerCount) -> {
            int failedPlayerCount = countFailedPlayer(stage, stages);
            double failureRate = 0;
            if (playerCount != 0) {
                failureRate = (double) failedPlayerCount / playerCount;
            }
            failureRateByStage.put(stage, failureRate);
        });
        
        List<Integer> stageList = new ArrayList<>(failureRateByStage.keySet());
        stageList.sort((o1, o2) -> failureRateByStage.get(o2).compareTo(failureRateByStage.get(o1)));

        int answer[] = stageList
            .stream()
            .mapToInt(Integer::intValue)
            .toArray();
        return answer;
    }
    
    int countFailedPlayer(int stage, int[] stages) {
        int failedPlayerCount = 0;
        for (int currentStage : stages) {
            if (currentStage == stage) {
                failedPlayerCount++;
            }
        }
        return failedPlayerCount;
    }
    
    Map<Integer, Integer> findPlayerCountByStage(int N, int[] stages) {
        Map<Integer, Integer> playerCountByStage = new LinkedHashMap();
        
        for (int stage = 1; stage < N + 1; stage++) {
            int playerCount = 0;
            for (int currentStage : stages) {
                if (currentStage >= stage) {
                    playerCount++;
                }
            }
            playerCountByStage.put(stage, playerCount);
        }
        return playerCountByStage;
    }
}