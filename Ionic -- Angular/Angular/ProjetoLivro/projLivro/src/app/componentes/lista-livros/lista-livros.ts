import { Component, OnInit } from '@angular/core';
import { GeneroLiterario } from '../genero-literario/genero-literario';
import { Livros } from '../livro/livros';
import { map } from 'rxjs';
import { livros } from '../../modk-livro';

@Component({
  selector: 'app-lista-livros',
  imports: [],
  templateUrl: './lista-livros.html',
  styleUrl: './lista-livros.css'
})
export class ListaLivros implements OnInit{
  genero: GeneroLiterario [] = []
  livrosPorGenero: Map<string, Livros> = new Map() // aqui vai fazer uma especie de pesquisa usando o metodo map() nos livros atraves de key-value (chave (id) e valor (o livro)), -estrutura: variavel local: funcao map <chave , valor> = new map() =>aqui ele ta inicializando essa pesquisa.

  //pre redenrizacao
  ngOninit(){
    this.livrosPorGenero = new Map()
    
    livros.forEach((livros)) => {

    }
  }
}
