package com.example.exercicio4;

import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class MainActivity extends AppCompatActivity {

    public ListView listViewAlunos;
    public TextView textViewReprovados, textViewExame, textViewAprovados, textViewMedia;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        listViewAlunos = findViewById(R.id.listViewAlunos);
        textViewMedia = findViewById(R.id.textViewMedia);
        textViewReprovados = findViewById(R.id.textViewReprovados);
        textViewExame = findViewById(R.id.textViewExame);
        textViewAprovados = findViewById(R.id.textViewAprovados);

        List<Aluno> alunos = new ArrayList<>();

        // Gere dados aleatórios para os alunos (como no código original)
        for (String nome : nomes) {
            Aluno aluno = new Aluno(nome);
            Random rand = new Random();

            // Gerar notas aleatórias
            double nota1 = rand.nextDouble() * 10;
            double nota2 = rand.nextDouble() * 10;

            // Nota para cada aluno da lista
            aluno.setNota1(nota1);
            aluno.setNota2(nota2);

            // Média do aluno
            double media = (nota1 + nota2) / 2;
            aluno.setMedia(media);

            // Situação do aluno
            if (media < 4.5) {
                aluno.setSituacao("Reprovado");
            } else if ((media >= 4.5) && (media < 7)) {
                aluno.setSituacao("Exame");
            } else {
                aluno.setSituacao("Aprovado");
            }

            //Adicionar a uma nova lista aluno os nomes dos alunos, notas e situação academica
            alunos.add(aluno);
        }

        double alunosReprovados = calcularPercentual(alunos, "Reprovado");
        double alunosExame = calcularPercentual(alunos, "Exame");
        double alunosAprovados = calcularPercentual(alunos, "Aprovado");
        double mediaGeral = calcularMediaGeral(alunos);

        //Transformar a lista/array de alunos em um item de list para poder usar no ListView
        ArrayAdapter<Aluno> adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, alunos);
        listViewAlunos.setAdapter(adapter);

        textViewReprovados.setText("Reprovados: " + String.format("%.2f%%", alunosReprovados));
        textViewExame.setText("Exame: " + String.format("%.2f%%", alunosExame));
        textViewAprovados.setText("Aprovados: " + String.format("%.2f%%", alunosAprovados));
        textViewMedia.setText("Média Geral: " + String.format("%.1f%%",mediaGeral));
    }

    public double calcularMediaGeral(List<Aluno> alunos) {
        double somaDasMedias = 0;
        for (Aluno aluno : alunos) {
            somaDasMedias += aluno.getMedia();
        }
        return somaDasMedias / alunos.size();
    }


    //Filtra e conta a quantidade de alunos aprovados,reprovados e de exame
    private static double calcularPercentual(List<Aluno> alunos, String situacao) {
        long count = alunos.stream().filter(aluno -> aluno.getSituacao().equals(situacao)).count();
        return (count * 100.0) / alunos.size();
    }

    //Lista com nome dos 40 Alunos
    private String[] nomes = {
            "Maria Silva",
            "João Santos",
            "Ana Oliveira",
            "Pedro Pereira",
            "Sofia Rodrigues",
            "Miguel Costa",
            "Carolina Fernandes",
            "Tiago Martins",
            "Inês Sousa",
            "Daniel Alves",
            "Beatriz Gomes",
            "Luís Gonçalves",
            "Mariana Dias",
            "Guilherme Carvalho",
            "Leonor Ribeiro",
            "Francisco Ferreira",
            "Matilde Barbosa",
            "Rafael Coelho",
            "Catarina Neves",
            "Tomás Lima",
            "Clara Pinto",
            "Rodrigo Lopes",
            "Diana Correia",
            "André Almeida",
            "Helena Santos",
            "Diogo Oliveira",
            "Laura Fonseca",
            "Gustavo Miranda",
            "Camila Azevedo",
            "Lucas Pereira",
            "Isabella Costa",
            "Bernardo Santos",
            "Mariana Ferreira",
            "Henrique Rocha",

    };

}