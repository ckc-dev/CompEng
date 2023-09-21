package com.example.p1q1;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TableLayout;
import android.widget.TableRow;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private EditText inputEditText;
    private Button calculateButton;
    private TableLayout resultantTableLayout;
    private int[][] initialTable;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize views
        inputEditText = findViewById(R.id.inputEditText);
        calculateButton = findViewById(R.id.button);
        resultantTableLayout = findViewById(R.id.resultantTableLayout);

        // Generate initial random table
        initialTable = Utils.generateRandomTable();

        // Populate the initial table in the layout
        populateTable(initialTable, R.id.initialTableLayout);

        // Handle button click event
        calculateButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                calculateResultantTable();
            }
        });
    }

    private void calculateResultantTable() {
        String inputText = inputEditText.getText().toString();

        // Validate user input
        if (inputText.isEmpty()) {
            // Handle empty input (show a message or error)
            return;
        }

        int multiplier = Integer.parseInt(inputText);
        int[][] resultantTable = Utils.multiplyTable(initialTable, multiplier);

        // Clear existing rows in resultantTableLayout
        resultantTableLayout.removeAllViews();

        // Populate resultantTableLayout with the new data
        populateTable(resultantTable, R.id.resultantTableLayout);
    }

    private void populateTable(int[][] tableData, int tableLayoutId) {
        TableLayout tableLayout = findViewById(tableLayoutId);

        for (int i = 0; i < tableData.length; i++) {
            TableRow row = new TableRow(this);
            for (int j = 0; j < tableData[i].length; j++) {
                TextView textView = new TextView(this);
                textView.setText(String.valueOf(tableData[i][j]));
                textView.setPadding(8, 8, 8, 8);
                row.addView(textView);
            }
            tableLayout.addView(row);
        }
    }
}
