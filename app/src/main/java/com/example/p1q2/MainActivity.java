package com.example.p1q2;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.LinearLayout;
import android.widget.TableLayout;
import android.widget.TableRow;
import android.widget.TextView;
import java.util.List;
import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Get references to layouts
        LinearLayout vector1Layout = findViewById(R.id.vector1Layout);
        LinearLayout vector2Layout = findViewById(R.id.vector2Layout);
        TableLayout initialMatrixTableLayout = findViewById(R.id.initialMatrixTableLayout);
        TableLayout resultingMatrixTableLayout = findViewById(R.id.resultingMatrixTableLayout);

        // Generate vectors and matrix
        int[] vector1 = Utils.generateVector(5);
        int[] vector2 = Utils.generateVector(10);
        int[][] initialMatrix = Utils.generateMatrix(4, 3);

        // Populate Vector Layouts
        populateVectorLayout(vector1Layout, vector1);
        populateVectorLayout(vector2Layout, vector2);

        // Populate initial matrix TableLayout
        populateMatrixTableLayout(initialMatrixTableLayout, initialMatrix);

        // Calculate the product of the largest element in Vector 1 and the smallest element in Vector 2
        int product = Utils.findLargestElement(vector1) * Utils.findSmallestElement(vector2);

        // Calculate the Resulting Matrix by adding the product to each element of the Initial Matrix
        int[][] resultingMatrix = Utils.addValueToMatrix(initialMatrix, product);

        // Populate Resulting Matrix TableLayout
        populateMatrixTableLayout(resultingMatrixTableLayout, resultingMatrix);

        // Populate answers for the questions
        List<String> answers = calculateAnswers(vector1, vector2, initialMatrix, resultingMatrix);

        // Set the answers to TextViews
        setAnswersToTextViews(answers);
    }

    private void populateVectorLayout(LinearLayout layout, int[] vector) {
        for (int i = 0; i < vector.length; i++) {
            TextView textView = new TextView(this);
            textView.setText(String.valueOf(vector[i]));
            if (i < vector.length - 1) {
                textView.append(", "); // Add comma for all but the last element
            }
            layout.addView(textView);
        }
    }

    private void populateMatrixTableLayout(TableLayout layout, int[][] matrix) {
        for (int[] rowValues : matrix) {
            TableRow row = new TableRow(this);
            for (int value : rowValues) {
                TextView textView = new TextView(this);
                textView.setText(String.valueOf(value));
                textView.setPadding(16, 0, 16, 0); // Add padding for better formatting
                if (value != rowValues[rowValues.length - 1]) {
                    textView.append(", "); // Add comma for all but the last element
                }
                row.addView(textView);
            }
            layout.addView(row);
        }
    }

    private List<String> calculateAnswers(int[] vector1, int[] vector2, int[][] initialMatrix, int[][] resultingMatrix) {
        List<String> answers = new ArrayList<>();
        int product = Utils.findLargestElement(vector1) * Utils.findSmallestElement(vector2);
        answers.add(String.valueOf(product));

        List<Integer> sumOfEvenElements = Utils.calculateSumOfEvenElementsInEachRow(resultingMatrix);
        answers.add(sumOfEvenElements.toString());

        List<Integer> countElementsBetween1And5 = Utils.countElementsInRangeInEachColumn(resultingMatrix, 1, 5);
        answers.add(countElementsBetween1And5.toString());

        int countEvenNumbers = Utils.countEvenNumbers(vector1, vector2, initialMatrix, resultingMatrix);
        answers.add(String.valueOf(countEvenNumbers));
        return answers;
    }

    private void setAnswersToTextViews(List<String> answers) {
        int[] answerTextViewIds = {
            R.id.answer1, R.id.answer2, R.id.answer3, R.id.answer4
        };
        for (int i = 0; i < answerTextViewIds.length && i < answers.size(); i++) {
            TextView answerTextView = findViewById(answerTextViewIds[i]);
            answerTextView.setText(answers.get(i));
        }
    }
}
