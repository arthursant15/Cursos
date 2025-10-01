export interface Livros{
    titulo: string
    favorito: boolean
    genero: GeneroLiterario
    autoria: string
    imagem: string
}
export interface GeneroLiterario{
    id: string
    value: string
    livros: Livros[]
}