import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int n = input.nextInt();
		input.nextLine();
		
		int[] scores = new int[n];
		int maxScore = 0;
		for (int i = 0; i < n; i++) {
			scores[i] = input.nextInt();
			if (maxScore < scores[i]) {
				maxScore = scores[i];
			}
		}

		double total = 0;
		for (int i = 0; i < n; i++) {
			double newScore = (double) scores[i] / maxScore * 100;
			total += newScore;
		}
		System.out.println(total / n);
	}
}