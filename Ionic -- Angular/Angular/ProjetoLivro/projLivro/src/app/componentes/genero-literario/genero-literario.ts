import { Component } from '@angular/core';
import { livros } from '../../modk-livro';
import { Livro } from "../livro/livro";

@Component({
  selector: 'app-genero-literario',
  imports: [Livro],
  templateUrl: './genero-literario.html',
  styleUrl: './genero-literario.css'
})
export class GeneroLiterario {
  // aqui voce vai exportar essa variavel para o html dessa pasta, fazendo assim a sua exibicao no templete, ao pressionar crtl+click voce sera redirecionado a onde esta localizado o modok que é uma 'API local', la foi tirado as informacoes dos livros e [0] porque ele é o começo do array e nessa declaração ela está apenas iniciando e que é um array. 
    livro = livros [0]

}
