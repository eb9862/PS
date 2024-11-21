import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {

    static int maxValue = Integer.MAX_VALUE;
    static int minValue = Integer.MIN_VALUE;
    static int count;
    static List<Integer> numbers;
    static int[] operators;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in)
        );

        count = Integer.parseInt(br.readLine());

        String[] numberInput = br.readLine().split(" ");
        numbers = new ArrayList<>();
        for (int i = 0; i < count; i++) {
            int number = Integer.valueOf(numberInput[i]);
            numbers.add(number);
        }

        String[] operatorInput = br.readLine().split(" ");
        operators = new int[4];
        for (int i = 0; i < 4; i++) {
            operators[i] = Integer.parseInt(operatorInput[i]);
        }

        calculate(0, 0, operators);
        System.out.println(maxValue);
        System.out.println(minValue);
    }

    static void calculate(int turn, int calculatedValue, int[] operators) {
        if (turn == 0) {
            calculate(turn + 1, numbers.get(0), operators);
            return;
        }
        if (turn == count) {
            if (
                minValue == Integer.MIN_VALUE && maxValue == Integer.MAX_VALUE
            ) {
                minValue = calculatedValue;
                maxValue = calculatedValue;
            } else {
                if (calculatedValue < minValue) {
                    minValue = calculatedValue;
                }
                if (calculatedValue > maxValue) {
                    maxValue = calculatedValue;
                }
            }
            return;
        }
        for (int i = 0; i < 4; i++) {
            int value;
            if (i == 0 && operators[i] != 0) {
                value = calculatedValue + numbers.get(turn);
                int[] operatorsCopy = Arrays.copyOf(
                    operators,
                    operators.length
                );
                operatorsCopy[i] -= 1;
                calculate(turn + 1, value, operatorsCopy);
            }
            if (i == 1 && operators[i] != 0) {
                value = calculatedValue - numbers.get(turn);
                int[] operatorsCopy = Arrays.copyOf(
                    operators,
                    operators.length
                );
                operatorsCopy[i] -= 1;
                calculate(turn + 1, value, operatorsCopy);
            }
            if (i == 2 && operators[i] != 0) {
                value = calculatedValue * numbers.get(turn);
                int[] operatorsCopy = Arrays.copyOf(
                    operators,
                    operators.length
                );
                operatorsCopy[i] -= 1;
                calculate(turn + 1, value, operatorsCopy);
            }
            if (i == 3 && operators[i] != 0) {
                value = calculatedValue / numbers.get(turn);
                int[] operatorsCopy = Arrays.copyOf(
                    operators,
                    operators.length
                );
                operatorsCopy[i] -= 1;
                calculate(turn + 1, value, operatorsCopy);
            }
        }
    }
}
