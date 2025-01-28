[Voltar](./../../README.md)
# Detectando Celebridades em Imagens

Neste projeto utilizamos o [rekognition](https://aws.amazon.com/pt/rekognition/), para fazer a detecção de celebridades em uma foto, além da própria detecção em sí, também desenhamos uma bounding box (caixa delimitadora), para saber aonde exatamente está a celebridade na foto, e também apresentamos seu nome.

### Oque eu preciso ter?
* [UV](https://docs.astral.sh/uv/)
* [Amazon Web Service Account](https://aws.amazon.com/)
* [Amazon Web Service CLI](https://aws.amazon.com/pt/cli/)
### Como usar?
1º - Utilize o UV para instalar as dependências
```pwsh
uv install
```
2º - Execute o código (lembre-se de estar logado no CLI da Amazon)
```pwsh
uv run main.py
```