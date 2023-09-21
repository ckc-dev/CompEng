package com.example.p1q2;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Utils {
    // Generate a random integer vector of a specified length
    public static int[] generateVector(int length) {
        Random random = new Random();
        int[] vector = new int[length];
        for (int i = 0; i < length; i++) {
            vector[i] = random.nextInt(100);
        }
        return vector;
    }

    // Generate a random integer matrix of specified dimensions
    public static int[][] generateMatrix(int rows, int columns) {
        Random random = new Random();
        int[][] matrix = new int[rows][columns];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                matrix[i][j] = random.nextInt(100);
            }
        }
        return matrix;
    }

    // Find the largest element in an integer vector
    public static int findLargestElement(int[] vector) {
        int max = Integer.MIN_VALUE;
        for (int num : vector) {
            if (num > max) {
                max = num;
            }
        }
        return max;
    }

    // Find the smallest element in an integer vector
    public static int findSmallestElement(int[] vector) {
        int min = Integer.MAX_VALUE;
        for (int num : vector) {
            if (num < min) {
                min = num;
            }
        }
        return min;
    }

    // Calculate the sum of even elements in each row of a matrix
    public static List<Integer> calculateSumOfEvenElementsInEachRow(int[][] matrix) {
        List<Integer> sums = new ArrayList<>();
        for (int[] row : matrix) {
            int sum = 0;
            for (int num : row) {
                if (num % 2 == 0) {
                    sum += num;
                }
            }
            sums.add(sum);
        }
        return sums;
    }


    // Count the number of elements between 1 and 5 in each column of a matrix
    public static List<Integer> countElementsBetween1And5(int[][] matrix) {
        List<Integer> counts = new ArrayList<>();
        for (int j = 0; j < matrix[0].length; j++) {
            int count = 0;
            for (int[] ints : matrix) {
                int num = ints[j];
                if (num >= 1 && num <= 5) {
                    count++;
                }
            }
            counts.add(count);
        }
        return counts;
    }

    // Multiply a matrix by a scalar
    public static int[][] multiplyMatrixByScalar(int[][] matrix, int scalar) {
        int rows = matrix.length;
        int columns = matrix[0].length;
        int[][] result = new int[rows][columns];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                result[i][j] = matrix[i][j] * scalar;
            }
        }
        return result;
    }

    // Add a value to each element of a matrix
    public static int[][] addValueToMatrix(int[][] matrix, int value) {
        int rows = matrix.length;
        int columns = matrix[0].length;
        int[][] result = new int[rows][columns];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                result[i][j] = matrix[i][j] + value;
            }
        }
        return result;
    }

    // Count the number of even numbers in vectors and matrices
    public static int countEvenNumbers(int[] vector1, int[] vector2, int[][]... matrices) {
        int count = 0;
        for (int num : vector1) {
            if (num % 2 == 0) {
                count++;
            }
        }
        for (int num : vector2) {
            if (num % 2 == 0) {
                count++;
            }
        }
        for (int[][] matrix : matrices) {
            for (int[] row : matrix) {
                for (int num : row) {
                    if (num % 2 == 0) {
                        count++;
                    }
                }
            }
        }
        return count;
    }
}
