# Desafio Dev Cross Commerce

## Plataforma

O projeto foi feito em Python 3.7 utilizando PyCharm como IDE.

## Dependências

Foi gerado um arquivo _requirements.txt_ com todas as dependências necessárias.
Aconselho fortemente utilizar um ambiente virtual do Python (venv) para instalar as dependências.

Em Windows
```
python37 -m venv
venv/Scripts/activate.bat
pip install -r requirements.txt
```

Em Linux

```
python37 -m venv
source venv/bin/activate
pip install -r requirements.txt
```

Ou usar seu ambiente de desenvolvimento (como o PyCharm) para executar essa tarfa.

## Esclarecimentos

### Configurações

Todas as configurações do sistema estão no arquivo ```config.py```: mensagens, URLs, número de _threads_, número máximo de retentativas, tempos de espera entre tentativas, etc.

### Logs

O sistema faz _log_ de tudo que faz (exceto na ordenação, pois isso impactaria muito no desempenho).
Assim é mais fácil de verificar o funcionamento dele, especialmente em operações demoradas. Os _logs_ pararecem tanto na linha de comando como ficam nos arquivos.
A cada execução é gerado um novo arquivo em _logs_.

### Extração

No caso do _extract_ eu tive de usar asyncio (daí um Python superior ao 3.5) devido ao elevado númeor de páginas para poder executar várias chamadas simultâneamente.
Senão demoraria muito para obter os dados. A extração está resistente aos _internal server erros_ que ocorrem e a uns eventuais _timeouts_ quando o número de _threads_ paralelas deixa o servidor lento, quando isso ocorre eu dou uma pausa maior antes de prossegir para evitar derrubar o servidor ou deixá-lo lento.

### Transformação (ordenação)

O algoritmo de ordenação que eu usei não é nenhum dos clássicos.
Como o desafio pedia para fazer tudo do zero criei um.
Como eu não queria tomar muito do meu tempo, optei por um recursivo, assim ele é fácil de entender e escrever.
O desempenho dele é razoável: para 1 milhão de entradas ele leva uns 25 a 30 segundos.
Como ele divide a lista duas partes de cada vez acredito que ele tenha complexidade _O(n * log(n))_ o que o torna próximo do heapsort e do quicksort.

### Load (web API)

A API pedida é similar a original, a diferença é que o parâmetro da página é passado por GET assim:

```
http://192.168.1.10:8003/numbers/<page>
```

Onde ```<page>```  é o número da página.

Números de página inválidos reornarão um JSON com a mensagem de erro:

```
{"error":"Invalid page parameter: 'aaaaa'"}
```

Números de página válidos, mas de páginas inexistentes retornarão uma lista vazia:

```
{"numbers":[]}
```

### Comentários

Todos os comentários e mensagens estão em inglês, como é procedimento padrão na imensa maioria das companhias.

### Unit tests

Os _unit tests_ estão em ```tests```.

Como o serviço fornecedor não altera nenhum dado optei por não fazer um _moc_ dele.

### Pontos de entrada

Cada um dos arquivos ```.py``` tem a própria entrada em geral com um teste.
A exceção é a entrada principal do sistema é a API _web_ que é uma aplicação Flask.
Pode-se executar os _unit tests_  com um _runner_ , mas eu optei por fazer o arquivo do _unit test_ autocontido, asssim basta executar cada um.

### Disponibilidade

Coloquei no GitHub mas o repositório é privado, me avisem e eu abro para quem quiser ver.
Acho melhor já que não queremos que alguém ache a resposta do teste no GitHub depois nem que _trolls_ fiquem fazendo DDNS no _endpoint_.

### Limitações e compromissos (aka desculpas esfarrapadas)

Por questão de simplicidade eu obtenho todos os dados e **DEPOIS** subo o serviço da API.
Eu gostaria de fazer ela mostra o _status_ da extração, não ficou claro para mim se isso era pedido, e como só se pode ordenar depois de ter todos os números, deixei assim.

Eu poderia ter sofisticado muito mais tudo, mas creio que o tempo também é um fator de avaliação assim optei por parar por aqui.
Como num sistema real eu listo estas possibilidades no _TODO list_.

Num sistema real, eu separaria a extração e a API em _containers_ separados, e salvaria os valores em uma base.
Mas isso é uma questão de _deploy_ e não de desenvolvimento e tornaria mais complexo testar minha solução.

## Todo list

Isso é para o meu controle:

* tornar a parte da aplicação Flask assíncrona enquanto obtém od dados a fornecer, de modo a char a API e mostrar a progressão da extração e transformação;
* criar um _mock_ para emular o teste da extração, do jeito que está hoje ele é um teste de integração e não um _unit test_;
* os testes em ```tests/transform_test.py``` e ```tests/extract_transform.py``` tem um método _helper_ repetido, extrair para uma classe separada mas manter os testes dela;
