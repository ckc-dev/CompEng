package com.example.exercicio4;

import java.text.DecimalFormat;

public class Aluno {
    private String nome;
    private double nota1;
    private double nota2;
    private double media;
    private String situacao;

    public Aluno(String nome) {
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }

    public double getNota1() {
        return nota1;
    }

    public void setNota1(double nota1) {
        this.nota1 = nota1;
    }

    public double getNota2() {
        return nota2;
    }

    public void setNota2(double nota2) {
        this.nota2 = nota2;
    }

    public double getMedia() {
        return media;
    }

    public void setMedia(double media) {
        this.media = media;
    }

    public String getSituacao() {
        return situacao;
    }

    public void setSituacao(String situacao) {
        this.situacao = situacao;
    }

    //Essas duas funções servem para formatarem as notas do alunos como números decimais
    //com uma casa decima apenas apos a virgula evitando erro de numeros decimais imensos no
    //ListView
    public String nota1Formatada() {
        DecimalFormat df = new DecimalFormat("#.#");
        return df.format(nota1);
    }

    public String nota2Formatada() {
        DecimalFormat df = new DecimalFormat("#.#");
        return df.format(nota2);
    }

    public String mediaFormatada(){
        DecimalFormat df = new DecimalFormat("#.#");
        return  df.format(media);
    }

    @Override
    public String toString() {
        return "Aluno:" + nome + '\n' +
                "1ºProva:" + nota1Formatada() + '\n' +
                "2ºProva:" + nota2Formatada() + '\n' +
                "Média:" + mediaFormatada()+ '\n' +
                "Situacao:" + situacao;
    }
}

