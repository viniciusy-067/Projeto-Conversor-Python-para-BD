# Conversor de Contatos para CSV

Aplicação web open-source para **padronização e conversão de listas de contatos** em um arquivo CSV simples e consistente, contendo apenas as colunas **Nome** e **Telefone**.

Desenvolvido em **Python (Flask)** com foco em automação, previsibilidade de saída e redução de erros de importação em sistemas de terceiros.

---

## Visão Geral

Este projeto tem como objetivo facilitar a conversão de planilhas de contatos provenientes de diferentes fontes (CRMs, sistemas legados, exports manuais) em um formato CSV padronizado e limpo.

Ele é indicado para **uso local**, estudos e automações simples.

---

## Funcionalidades

* Upload de arquivos via interface web
* Suporte aos formatos:

  * `.csv`
  * `.xls`
  * `.xlsx`
* Normalização automática de dados:

  * Capitalização adequada de nomes
  * Remoção de espaços e caracteres especiais
  * Telefones convertidos para apenas dígitos
  * Descarte de colunas não utilizadas

---

## Exemplo de Normalização

| Campo    | Entrada               | Saída             |
| -------- | --------------------- | ----------------- |
| Nome     | `Joazinho`            | `Joazinho       ` |
| Telefone | `+55 (67) 99999-8888` | `67999998888`     |
| Outros   | `email@teste.com`     | *(descartado)*    |

---

## Status do Projeto

**Versão:** Pré-Alpha

Projeto funcional para cenários controlados, **não recomendado para produção**.

---

## Requisitos

* Python 3.10+
* Git

---

## Instalação

```bash
git clone https://github.com/viniciusy-067/nome-do-repositorio.git
cd nome-do-repositorio
python -m venv venv

# Windows
venv\\Scripts\\activate

# Linux / macOS
source venv/bin/activate

python app.py
```

Acesse: `http://localhost:5000`

---

## Como Usar

1. Abra a aplicação no navegador
2. Faça upload do arquivo de contatos
3. Aguarde o processamento
4. O download do arquivo `contatos_padronizados.csv` será iniciado automaticamente

---

## Segurança e Privacidade

* Os arquivos são processados apenas durante a execução
* Nenhum dado é persistido
* Nenhuma informação é enviada para serviços externos

Execute apenas em ambientes confiáveis.

---

## Roadmap

* [ ] Validação de telefones via Regex
* [ ] Remoção de contatos duplicados
* [ ] Mapeamento dinâmico de colunas
* [ ] Testes automatizados (Pytest)
* [ ] Docker

---

## Licença

MIT License

Este projeto é distribuído "no estado em que se encontra", sem garantias.
