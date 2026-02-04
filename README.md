# ⚡ Conversor de Contatos para CSV

Aplicação web focada em **padronização e conversão de listas de contatos**. Transforme arquivos complexos em um CSV limpo, consistente e pronto para importação.

---

<div align="center">

![GitHub repo size](https://img.shields.io/github/repo-size/viniciusy-067/projeto-conversor-python-para-bd?style=for-the-badge&color=indigo)
![GitHub language count](https://img.shields.io/github/languages/count/viniciusy-067/projeto-conversor-python-para-bd?style=for-the-badge&color=indigo)
![MIT License](https://img.shields.io/badge/license-MIT-informational?style=for-the-badge)

<br />

### 🔗 Acesse o Projeto Online
[![Deploy on Render](https://img.shields.io/badge/Live_Demo-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://projeto-conversor-python-para-bd.onrender.com)

</div>
---

Nota: Como o projeto está hospedado no plano gratuito do Render, o primeiro carregamento pode levar cerca de 50 segundos para iniciar o servidor.

---


## 📖 Visão Geral

Desenvolvido com **Python (Flask)**, este projeto soluciona o problema comum de incompatibilidade entre planilhas de contatos (CRMs, sistemas legados) e ferramentas de automação que exigem um formato estrito de **Nome e Telefone**.

> **Nota:** Ideal para desenvolvedores que buscam uma ferramenta rápida de sanitização de dados sem persistência em banco de dados.

## 🛠️ Tecnologias e Ferramentas

* **Backend:** Python 3.10+ (Flask)
* **Frontend:** HTML5, Tailwind CSS (Modern UI)
* **Processamento de Dados:** Pandas / Openpyxl
* **Hospedagem:** Render (Cloud PaaS)

## ✨ Funcionalidades

* **Upload Inteligente:** Suporte para `.csv`, `.xls` e `.xlsx`.
* **Normalização Automática:**
    * Capitalização inteligente de nomes.
    * Sanitização de strings (remoção de caracteres especiais).
    * Extração de dígitos numéricos para telefones.
    * Filtragem de colunas irrelevantes.
* **Interface Minimalista:** Design responsivo e focado na experiência do usuário.

## 📊 Exemplo de Processamento

| Campo    | Entrada (Suja)         | Saída (Sanitizada) |
| :------- | :--------------------- | :----------------- |
| **Nome** | `  viniCIUS taveira `  | `Vinicius Taveira` |
| **Tel** | `+55 (67) 99999-8888`  | `67999998888`      |
| **Meta** | `id: 001 / status: ok` | *(Descartado)* |

## 🚀 Instalação e Execução Local

```bash
# Clone o repositório
git clone [https://github.com/viniciusy-067/projeto-conversor-python-para-bd.git](https://github.com/viniciusy-067/projeto-conversor-python-para-bd.git)

# Entre na pasta
cd projeto-conversor-python-para-bd

# Configure o ambiente
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# Instale dependências e rode
pip install -r requirements.txt
python app.py
