# cdf

Minha caixa de ferramentas (cdf), um conjunto de mini aplicativos para ajudar no dia a dia.

## Desenvolvimento

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

Instalar a configuração do pre-commit:

```
$ pre-commit install
```

Para gerenciar as dependências do projeto eu utilizo o
[pip-tools](https://github.com/jazzband/pip-tools), sendo assim:

```
$ pip install --upgrade pip-tools pip setuptools
```

Agora só instala as dependencias usando pip:

```
$ pip install -r dependencias/requirements.txt -r dependencias/requirements-dev.txt
```

Para fazer o upgrade de todas as libs do projeto:

```
pip-compile \
  --upgrade \
  --resolver=backtracking \
  --generate-hashes \
  --output-file dependencias/requirements.txt \
  dependencias/requiremetns.in
```

Obviamente, para fazer o mesmo para libs de desenvolvimento, basta mudar o nome
do arquivo. Para fazer o upgrade de uma dependência específica:

```
pip-compile --upgrade-package <pacote>==<versao>
```

Caso seja necessário fazer upgrade do pacote para uma versão específica, basta
omitir `=<versao>`.

#### Como rodar testes

```
TODO
```
