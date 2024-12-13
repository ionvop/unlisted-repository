package src; 
import java.util.*;

public class Ionvop {
    public static void print(Object message) {
        System.out.println(message);
    }

    public static void print(int message) {
        System.out.println(message);
    }

    public static void print(double message) {
        System.out.println(message);
    }
    public static void print(String message) {
        System.out.println(message);
    }

    public static void print(int[] message) {
        System.out.println(Arrays.toString(message));
    }

    public static void print(double[] message) {
        System.out.println(Arrays.toString(message));
    }

    public static void print(String[] message) {
        System.out.println(Arrays.toString(message));
    }

    public static void print(int[][] message) {
        String[] result = new String[message.length];

        for (int i = 0; i < result.length; i++) {
            result[i] = Arrays.toString(message[i]);
        }

        System.out.println(Arrays.toString(result));
    }

    public static void print(double[][] message) {
        String[] result = new String[message.length];

        for (int i = 0; i < result.length; i++) {
            result[i] = Arrays.toString(message[i]);
        }

        System.out.println(Arrays.toString(result));
    }

    public static void print(String[][] message) {
        String[] result = new String[message.length];

        for (int i = 0; i < result.length; i++) {
            result[i] = Arrays.toString(message[i]);
        }

        System.out.println(Arrays.toString(result));
    }

    public static void breakpoint(Object message) {
        print(message);
        System.exit(0);
    }

    public static void breakpoint(int message) {
        print(message);
        System.exit(0);
    }

    public static void breakpoint(double message) {
        print(message);
        System.exit(0);
    }

    public static void breakpoint(String message) {
        print(message);
        System.exit(0);
    }

    public static void breakpoint(int[] message) {
        print(message);
        System.exit(0);
    }

    public static void breakpoint(double[] message) {
        print(message);
        System.exit(0);
    }

    public static void breakpoint(String[] message) {
        print(message);
        System.exit(0);
    }

    public static void breakpoint(int[][] message) {
        print(message);
        System.exit(0);
    }

    public static void breakpoint(double[][] message) {
        print(message);
        System.exit(0);
    }

    public static void breakpoint(String[][] message) {
        print(message);
        System.exit(0);
    }

    public static int[] push(int[] input, int pushItem) {
        int[] result = new int[input.length + 1];

        for (int i = 0; i < input.length; i++) {
            result[i] = input[i];
        }

        result[input.length] = pushItem;
        return result;
    }

    public static double[] push(double[] input, double pushItem) {
        double[] result = new double[input.length + 1];

        for (int i = 0; i < input.length; i++) {
            result[i] = input[i];
        }

        result[input.length] = pushItem;
        return result;
    }

    public static String[] push(String[] input, String pushItem) {
        String[] result = new String[input.length + 1];

        for (int i = 0; i < input.length; i++) {
            result[i] = input[i];
        }

        result[input.length] = pushItem;
        return result;
    }

    public static int[][] push(int[][] input, int pushItem[]) {
        int[][] result = new int[input.length + 1][];

        for (int i = 0; i < input.length; i++) {
            result[i] = input[i];
        }

        result[input.length] = pushItem;
        return result;
    }

    public static double[][] push(double[][] input, double[] pushItem) {
        double[][] result = new double[input.length + 1][];

        for (int i = 0; i < input.length; i++) {
            result[i] = input[i];
        }

        result[input.length] = pushItem;
        return result;
    }

    public static String[][] push(String[][] input, String[] pushItem) {
        String[][] result = new String[input.length + 1][];

        for (int i = 0; i < input.length; i++) {
            result[i] = input[i];
        }

        result[input.length] = pushItem;
        return result;
    }

    public static int[] pop(int[] input) {
        int[] result = new int[input.length - 1];

        for (int i = 0; i < result.length; i++) {
            result[i] = input[i];
        }

        return result;
    }

    public static double[] pop(double[] input) {
        double[] result = new double[input.length - 1];

        for (int i = 0; i < result.length; i++) {
            result[i] = input[i];
        }

        return result;
    }

    public static String[] pop(String[] input) {
        String[] result = new String[input.length - 1];

        for (int i = 0; i < result.length; i++) {
            result[i] = input[i];
        }

        return result;
    }

    public static int[][] pop(int[][] input) {
        int[][] result = new int[input.length - 1][];

        for (int i = 0; i < result.length; i++) {
            result[i] = input[i];
        }

        return result;
    }

    public static double[][] pop(double[][] input) {
        double[][] result = new double[input.length - 1][];

        for (int i = 0; i < result.length; i++) {
            result[i] = input[i];
        }

        return result;
    }

    public static String[][] pop(String[][] input) {
        String[][] result = new String[input.length - 1][];

        for (int i = 0; i < result.length; i++) {
            result[i] = input[i];
        }

        return result;
    }
}