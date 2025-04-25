package com.example.aula1;
import java.util.Random;

public class calculaEX3 {
    String Msg;


    Random random = new Random();
    String vetor="";
    int pares=0;

    public String calcula(int tamanhoArray) {
        int[] numeros = new int[tamanhoArray];
        for (int i=0;i<tamanhoArray;i++) {
            numeros[i] = random.nextInt(100);
            if(numeros[i]%2==0){
                pares++;
            }
            vetor=vetor+" | "+numeros[i];
        }
        vetor = vetor+"\nPares:"+pares+"\nÍmpares:"+(20-pares);
        Msg=vetor;
        return Msg;
    }
}
