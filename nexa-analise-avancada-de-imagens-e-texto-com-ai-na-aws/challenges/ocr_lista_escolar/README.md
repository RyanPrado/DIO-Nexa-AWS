[Voltar](./../../README.md)
# Transcrevendo uma Imagem em Texto com AWS Textract

Neste projeto você verá como podemos utilizar o serviço [textract](https://aws.amazon.com/pt/textract/) , para extrair de uma imagem que representa uma lista de materiais, seus respectivos itens, alguns recursos são necessários para que se possa dar continuidade.

### Oque eu preciso ter?
* [UV](https://docs.astral.sh/uv/)
* [Amazon Web Service Account](https://aws.amazon.com/)
* [Amazon Web Service CLI](https://aws.amazon.com/pt/cli/)
### Como usar?
`(Opcional)` - Você pode executar a exclusão do arquivo `data/response.json` caso queria gerar uma nova consulta do Textract.
```pwsh
rm data/response.json # Linux
del data/response.json # Win
```

1º - Utilize o UV para instalar as dependencias
```pwsh
uv install
```
2º - Execute o codigo (lembre-se de estar logado no CLI da Amazon)
```pwsh
uv run main.py
```