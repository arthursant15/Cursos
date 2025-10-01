from wsgiref.simple_server import make_server     #função de  uma biblioteca que usa um modulo padrao do python para executar em um servidor web

def aplicacao(environ, start_response): 
#1- e como um dicionario gigantesco, ele recebe todas as requiricoes do servidor e armazena nele. 2- e uma funcao que vai execultar antes do retorno do servidor dizendo informacoes para com o servidor e o browser(navegador)
    produtos = [
        {'nome': 'Computador', 'valor': 6000.00},
        {'nome': 'TV', 'valor': 2300.00},
        {'nome': 'Maquina de lavar', 'valor': 850},
        {'nome': 'Aspirador de po', 'valor': 600}
    ]
    lista_html = '' #iniciei a variavel que ira ser usada posteriormente 
    for produto in produtos: #um for para que se percorra a lista produtos
        linha_html += f'<li> {produto['nome'] } - R$ {produto['valor']} </li>' #aqui a variavel linha vai receber ela mesma + f'' == siginifica voce usar variaveis dentro de uma string, o <li> e a parte da lista que sera adicionada no html e o {produto['nome'] } e justamente a variavel que esta sendo indicada no espaco nome e ele ira mostrar o atributo em que esta la dentro dele

    start_response('200 ok', [('Content_type', 'text/html;charset=utf-8')]) #1- Qual o status ao browser pedir sua requisicao ao servidor. 2-qual o tipo de conteudo vai usar (no caso o html)
    #no html ele ira retornar todo o valor que estiver nas haspas triplas, e sera convertido em bytes.
    with open('index.html', 'r', encoding='utf-8') as file: #essa funcao vai buscar o arquivo index.html, 1-onde esta, 2- r == read, 3- sera ultilizado o utf-8 para decodificacao, 4- as file == um arquivo
        html = file.read() #a variavel html ira receber o arquivo e o .read significa que ele ira ler o arquivo em questao 
    
    html_final = html.replace('{{PRODUTOS}}', linhas_html) #o html final ira receber uma funcao em que meio que serve para realocar no html no espaco produtos e o segundo parametro e qual a variavel que ira ser colocada 

    return [html.encode('utf-8')] #aqui ira retornar o html com a decodificacao utf-8

make_server('', 5000, aplicacao).serve_forever() #1- o host, 2- a porta do local host (nesse caso ne), 3- a funcao da aplicacao. --.serve_forever(): e uma funcao em que se e rodada 'para sempre' ate voce decidir parar  