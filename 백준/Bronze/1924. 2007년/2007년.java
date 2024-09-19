import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		int x = input.nextInt();
		int y = input.nextInt();
		
		String[] days = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
		int result = 0;
		for (int i = 1; i < x; i++) {
			result += daysPerMonth(i);
		}
		result += y;
		System.out.println(days[result % 7]);
	}

	public static int daysPerMonth(int month) {
		int result = switch(month) {
			case 1, 3, 5, 7, 8, 10, 12 -> 31;
			case 2 -> 28;
			case 4, 6, 9, 11 -> 30;
			default -> throw new IllegalArgumentException("Invalid month");
		};
		return result;
	}
}