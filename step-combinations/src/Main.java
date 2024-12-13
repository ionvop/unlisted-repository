package src;
import java.util.*;
import static src.Ionvop.*;

public class Main {
    public static void main(String[] args) {
        int[] allowed = {3, 5};
        int test = stepsCombinations(allowed, 5);
        breakpoint(test);
    }

    public static int stepsCombinations(int[] stepsAllowed, int length) {
        int[] steps = new int[length];

        for (int i = 0; i < steps.length; i++) {
            steps[i] = stepsAllowed[0];
        }

        int[][] stepsDone = new int[0][];
        int[][] stepsConfirmed = new int[0][];

        while (true) {
            int pos = 0;
            int[] stepsTaken = new int[0];

            for (int i = 0; i < steps.length; i++) {
                pos += steps[i];
                stepsTaken = push(stepsTaken, steps[i]);

                if (pos > length) {
                    pos -= steps[i];
                    stepsTaken = pop(stepsTaken);
                    
                    if (isStepsDone(stepsTaken, stepsDone) == false && (length - pos) < stepsAllowed[0]) {
                        print(Arrays.toString(stepsTaken) + " Remainder: " + (length - pos));
                    }

                    break;
                } else if (pos == length) {
                    if (isStepsDone(stepsTaken, stepsDone) == false) {
                        //print(stepsTaken);
                        stepsConfirmed = push(stepsConfirmed, stepsTaken);
                    }

                    break;
                }
            }

            stepsDone = push(stepsDone, stepsTaken);

            if (isLastSteps(steps, stepsAllowed)) {
                break;
            }

            steps = updateSteps(steps, stepsAllowed);
        }

        for (int i = 0; i < stepsConfirmed.length; i++) {
            print(stepsConfirmed[i]);
        }

        return stepsConfirmed.length;
    }

    public static int[] updateSteps(int[] steps, int[] stepsAllowed) {
        int[] stepsIndex = new int[steps.length];

        for (int i = 0; i < stepsIndex.length; i++) {
            stepsIndex[i] = indexOf(stepsAllowed, steps[i]);
        }

        stepsIndex[steps.length - 1]++;

        for (int i = steps.length - 1; i >= 0; i--) {
            if (stepsIndex[i] >= stepsAllowed.length) {
                stepsIndex[i] = 0;

                if (i - 1 < 0) {
                    break;
                }

                stepsIndex[i - 1]++;
                continue;
            }

            break;
        }

        for (int i = 0; i < steps.length; i++) {
            steps[i] = stepsAllowed[stepsIndex[i]];
        }

        return steps;
    }

    public static int indexOf(int[] input, int find) {
        for (int i = 0; i < input.length; i++) {
            if (input[i] == find) {
                return i;
            }
        }

        return -1;
    }

    public static boolean isStepsDone(int[] steps, int[][] stepsDone) {
        for (int i = 0; i < stepsDone.length; i++) {
            if (Arrays.equals(stepsDone[i], steps)) {
                return true;
            }
        }

        return false;
    }

    public static boolean isLastSteps(int[] steps, int[] stepsAllowed) {
        for (int i = 0; i < steps.length; i++) {
            if (steps[i] != stepsAllowed[stepsAllowed.length - 1]) {
                return false;
            }
        }

        return true;
    }
}