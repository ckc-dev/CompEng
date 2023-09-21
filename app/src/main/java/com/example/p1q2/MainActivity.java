package com.example.p1q2;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.Gravity;
import android.widget.LinearLayout;
import android.widget.TableLayout;
import android.widget.TableRow;
import android.widget.TextView;
import android.view.ViewGroup.LayoutParams;
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

        // Populate Vector 1 LinearLayout
        for (int i = 0; i < vector1.length; i++) {
            TextView textView = new TextView(this);
            textView.setText(String.valueOf(vector1[i]));
            if (i < vector1.length - 1) {
                textView.append(", "); // Add comma for all but the last element
            }
            vector1Layout.addView(textView);
        }

        // Populate Vector 2 LinearLayout
        for (int i = 0; i < vector2.length; i++) {
            TextView textView = new TextView(this);
            textView.setText(String.valueOf(vector2[i]));
            if (i < vector2.length - 1) {
                textView.append(", "); // Add comma for all but the last element
            }
            vector2Layout.addView(textView);
        }

        // Populate initial matrix TableLayout
        for (int[] ints : initialMatrix) {
            TableRow row = new TableRow(this);
            for (int j = 0; j < ints.length; j++) {
                TextView textView = new TextView(this);
                textView.setText(String.valueOf(ints[j]));
                textView.setPadding(16, 0, 16, 0); // Add padding for better formatting
                if (j < ints.length - 1) {
                    textView.append(", "); // Add comma for all but the last element
                }
                row.addView(textView);
            }
            initialMatrixTableLayout.addView(row);
        }

        // Calculate the product of the largest element in Vector 1 and the smallest element in Vector 2
        int product = Utils.findLargestElement(vector1) * Utils.findSmallestElement(vector2);

        // Calculate the Resulting Matrix by adding the product to each element of the Initial Matrix
        int[][] resultingMatrix = Utils.addValueToMatrix(initialMatrix, product);

        /* note from ckc: My mistake, I read the requirements wrong and thought I had to do the
                          scalar product. Then I realized it's not the case. Whoops. I'll leave it
                          as an option either way. */
        // Calculate the Resulting Matrix by multiplying the Initial Matrix by the product
        // int[][] resultingMatrix = Utils.multiplyMatrixByScalar(initialMatrix, product);

        // Populate Resulting Matrix TableLayout
        for (int i = 0; i < resultingMatrix.length; i++) {
            TableRow row = new TableRow(this);
            for (int j = 0; j < resultingMatrix[i].length; j++) {
                TextView textView = new TextView(this);
                textView.setText(String.valueOf(resultingMatrix[i][j]));
                textView.setPadding(16, 0, 16, 0); // Add padding for better formatting
                if (j < resultingMatrix[i].length - 1) {
                    textView.append(", "); // Add comma for all but the last element
                }
                row.addView(textView);
            }
            resultingMatrixTableLayout.addView(row);
        }

        // Populate answers for the questions
        List<String> answers = calculateAnswers(vector1, vector2, initialMatrix, resultingMatrix);

        // Find the TextViews for answers by their IDs and set their text
        TextView answer1 = findViewById(R.id.answer1);
        answer1.setText(answers.get(0));

        TextView answer2 = findViewById(R.id.answer2);
        answer2.setText(answers.get(1));

        TextView answer3 = findViewById(R.id.answer3);
        answer3.setText(answers.get(2));

        TextView answer4 = findViewById(R.id.answer4);
        answer4.setText(answers.get(3));
    }

    private List<String> calculateAnswers(int[] vector1, int[] vector2, int[][] initialMatrix, int[][] resultingMatrix) {
        List<String> answers = new ArrayList<>();

        // Calculate and add answers to the list
        int product = Utils.findLargestElement(vector1) * Utils.findSmallestElement(vector2);
        answers.add(String.valueOf(product));

        List<Integer> sumOfEvenElements = Utils.calculateSumOfEvenElementsInEachRow(resultingMatrix);
        answers.add(sumOfEvenElements.toString());

        List<Integer> countElementsBetween1And5 = Utils.countElementsBetween1And5(resultingMatrix);
        answers.add(countElementsBetween1And5.toString());

        int countEvenNumbers = Utils.countEvenNumbers(vector1, vector2, initialMatrix, resultingMatrix);
        answers.add(String.valueOf(countEvenNumbers));

        return answers;
    }
}
