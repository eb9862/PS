import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static Player[] players;
    static int n;
    static Queue<Integer> aliveIdx;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in)
        );

        n = Integer.parseInt(br.readLine());
        players = new Player[n];
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            players[i] = new Player();
            players[i].atk = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        aliveIdx = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            players[i].hp = Integer.parseInt(st.nextToken());
            aliveIdx.add(i);
        }

        int size = aliveIdx.size();
        long totalDmg = 0;
        int[] visited = new int[n];
        while (size > 1) {
            int i = aliveIdx.peek();
            long dmg = totalDmg - visited[i] * players[i].atk;
            if (players[i].hp - dmg > 0) {
                aliveIdx.add(i);
                aliveIdx.poll();
                totalDmg += players[i].atk;
                visited[i]++;
            } else {
                aliveIdx.poll();
                size--;
            }
        }
        System.out.println(aliveIdx.peek() + 1);
    }

    static class Player {

        int atk;
        long hp;
    }
}
