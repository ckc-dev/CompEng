package com.example.aula1;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;


public class MainActivity extends AppCompatActivity {
    TextView tRes;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // buscando os camponentes no layout
        tRes = findViewById(R.id.tRes);

    }
    public void bCalc(View view) {
        int tamanhoArray = 20;
        calculaEX3 calc = new calculaEX3();

        tRes.setText("Resultado \n\n" + calc.calcula(tamanhoArray));

    }
    public void bLimpa(View view) {
        tRes.setText("Resultado");
    }
    public void bSair(View view) {
        // fechar o app
        finish();
    }
}