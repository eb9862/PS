import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int n, m, result;
    static int[][] maps;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in)
        );
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        maps = new int[n][m];

        st = new StringTokenizer(br.readLine());
        int firstY = Integer.parseInt(st.nextToken());
        int firstX = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                maps[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        Robotcleaner rc = new Robotcleaner(d, firstX, firstY);
        rc.startClean();
        System.out.println(result);
    }

    static class Robotcleaner {

        int d;
        int x, y;
        boolean on;

        public Robotcleaner(int d, int x, int y) {
            this.d = d;
            this.x = x;
            this.y = y;
            this.on = false;
        }

        void startClean() {
            this.on = true;

            while (this.on) {
                if (maps[this.y][this.x] == 0) {
                    maps[this.y][this.x] = 2;
                    result++;
                }
                if (surroundCheck()) {
                    if (canMoveBack()) {
                        continue;
                    } else {
                        this.on = false;
                        break;
                    }
                } else {
                    do {
                        if (this.d == 0) {
                            this.d = 3;
                        } else {
                            this.d--;
                        }
                    } while (!cleanFrontTile());
                }
            }
        }

        boolean cleanFrontTile() {
            int frontX = this.x;
            int frontY = this.y;

            if (this.d == 0) {
                frontY -= 1;
            } else if (this.d == 1) {
                frontX += 1;
            } else if (this.d == 2) {
                frontY += 1;
            } else {
                frontX -= 1;
            }

            if (maps[frontY][frontX] == 0) {
                this.x = frontX;
                this.y = frontY;
                return true;
            }
            return false;
        }

        boolean canMoveBack() {
            int backX = this.x;
            int backY = this.y;

            if (this.d == 0) {
                backY += 1;
            } else if (this.d == 1) {
                backX -= 1;
            } else if (this.d == 2) {
                backY -= 1;
            } else {
                backX += 1;
            }

            if (maps[backY][backX] != 1) {
                this.x = backX;
                this.y = backY;
                return true;
            }
            return false;
        }

        boolean isValidCoor(int x, int y) {
            if ((x >= 0 && x < m) && (y >= 0 && y < n)) {
                return true;
            }
            return false;
        }

        boolean surroundCheck() {
            int presentX = this.x;
            int presentY = this.y;
            if (maps[presentY][presentX - 1] == 0) {
                return false;
            }
            if (maps[presentY][presentX + 1] == 0) {
                return false;
            }
            if (maps[presentY - 1][presentX] == 0) {
                return false;
            }
            if (maps[presentY + 1][presentX] == 0) {
                return false;
            }
            return true;
        }
    }
}