package com.example.p1q1;
import java.util.Random;

public class Utils {
    public static int[][] generateRandomTable() {
        int[][] table = new int[6][5];
        Random random = new Random();

        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 5; j++) {
                table[i][j] = random.nextInt(100);
            }
        }

        return table;
    }

    public static int[][] multiplyTable(int[][] table, int multiplier) {
        int rows = table.length;
        int cols = table[0].length;
        int[][] resultTable = new int[rows][cols];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                resultTable[i][j] = table[i][j] * multiplier;
            }
        }

        return resultTable;
    }
}
