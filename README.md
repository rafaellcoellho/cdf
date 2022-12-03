# cdf

Minha caixa de ferramentas (cdf), um conjunto de mini aplicativos para ajudar no dia a dia.

# Desenvolvimento

#### Configurando ambiente local

Instalar versão do python. Eu utilizo o [asdf](https://asdf-vm.com/), com o plugin
[asdf-python](https://github.com/asdf-community/asdf-python) para fazer isso:

```
$ asdf install python 3.10.4
```

O arquivo `.tool-versions` vai reconhecer que nessa pasta utilizo a versão correta:

```
$ python --version
Python 3.10.4
```

Para criar e iniciar o ambiente virtual:

```
$ virtualenv venv
[...]
$ . venv/bin/activate
```

Instalar as dependências de desenvolvimento:

```
$ pip install -r requirements-dev.txt
```

Instalar a configuração do pre-commit:

```
$ pre-commit install
```

#### Como rodar testes

```
TODO
```
