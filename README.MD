# 📥 BB-Automation PDF Bot

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue"/>
  <img src="https://img.shields.io/github/license/FelipheMP/bb-automation-pdf-bot"/>
  <img src="https://img.shields.io/badge/Made%20with-%E2%9D%A4-red"/>
</p>

## 📌 Descrição

**BB-Automation PDF Bot** é um bot de automação para baixar **PDFs de extratos de conta corrente e investimentos** do Banco do Brasil diretamente pela interface do navegador, simulando interações humanas (cliques, digitação e scroll). Ele não usa APIs privadas, scraping de rede ou qualquer forma intrusiva: tudo é feito por reconhecimento visual e teclado/mouse simulado, ideal para tarefas repetitivas.

## 🚀 Funcionalidades

- 📄 Baixar PDFs de **Extratos** e **Investimentos**  
- 📅 Processa mês a mês com timeline ou campo de data  
- 🧠 Inteligência visual para encontrar botões na tela  
- 🖨️ Automatiza impressão e salvamento com nome padrão  
- 📁 Nome de arquivo formatado:
```text
  Conta <conta> — <tipo> — <ano>-<mes>.pdf
```

## 🛠️ Pré-requisitos

Antes de rodar:

✔️ **Linux com X11/Xorg** ativo (não funciona em Wayland/não testado)  
✔️ Python 3.10+  
✔️ Zoom do navegador em 100%  
✔️ Navegador já logado no Banco do Brasil  
✔️ Atualize as imagens `imgs/nome_campo.png` e `imgs/salvar.png` com imagens referência do gerenciador de arquivos da sua distro  
✔️ Pasta de screenshots (`imgs/`) com templates atualizados

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/FelipheMP/bb-automation-pdf-bot.git
cd bb-automation-pdf-bot
```

Crie e ative o ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

Instale dependências:

```bash
pip install --upgrade pip
pip install pyautogui opencv-python pillow
```

## ▶️ Uso

Rode o bot:

```bash
python main.py
```

O programa pedirá:

```
Conta:
TIPO (1-EXTRATO/2-INVESTIMENTO):
```

Foque a janela do navegador no tempo de 5 segundos e deixe o bot fazer o resto.

## ❓ Q&A (Perguntas Frequentes)

**🔹 O bot funciona com Firefox/Chrome?**  
Sim. O zoom precisa estar em 100% e a janela do navegador visível.

**🔹 Preciso estar logado no banco?**  
Sim. O bot interage com a interface, não com APIs públicas/privadas.

**🔹 E se o botão não for encontrado?**  
Você pode ajustar a imagem template ou reduzir o valor de `confidence` no script.

## 🤝 Contribuição

Contribuições são bem-vindas!

1. Faça um fork ✨
2. Crie sua branch: `git checkout -b feature/nova-feature`
3. Commit suas mudanças ✔️
4. Abra um Pull Request 🚀

## 📄 Licença

Este projeto está sob a **GPL-3.0 License**. Consulte o arquivo `LICENSE` para mais detalhes.

## 📬 Contato

Desenvolvido por **[FelipheMP](https://github.com/FelipheMP)**.  
Sinta-se à vontade para abrir issues ou pull requests.  
Link do repositório: [BB-Automation PDF Bot](https://github.com/FelipheMP/bb-automation-pdf-bot)
