import { Component, input } from '@angular/core';
import { Livros } from './livros';

@Component({
  selector: 'app-livro',
  imports: [],
  templateUrl: './livro.html',
  styleUrl: './livro.css'
})
export class Livro {
  //como criar uma propriedade de entrada para que o componente receba informacoes vindas de fora. >> variavel local = entrada.requisicao obrigatoria<nome do export da interfac>()
  livro = input.required<Livros>()

  alternarFavorito(){
    //essa porrinha é uma funcao!!!!
    this.livro().favorito = !this.livro().favorito
  }
 
}
