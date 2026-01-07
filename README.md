# Automação de Checkout - SULTS

> Script de automação para controle de horários de abertura e fechamento do módulo de compras.

## Sobre o Projeto

Este projeto consiste em uma automação desenvolvida para solucionar uma demanda operacional do setor de TI.

Utilizamos o sistema **SULTS** para permitir que líderes de lojas e franqueados realizem a compra de insumos. Contudo, por regras de negócio, o checkout dessas compras deve permanecer aberto apenas em uma janela específica: **de segunda-feira às 09h até sexta-feira às 09h**.

Anteriormente, essa liberação e bloqueio eram feitos manualmente pela equipe de TI. Devido à alta demanda de outras tarefas, ocorriam atrasos ou esquecimentos ("perda do prazo"), impactando a operação das lojas.

**A Solução:**
Desenvolvi este bot em **Python** utilizando **Selenium**. Ele simula a navegação de um usuário administrador, realiza o login e altera o status (switch) das telas de compra automaticamente.

## Funcionalidades

- **Login Automático:** Acessa o painel administrativo com credenciais seguras.
- **Toggle Inteligente:** Identifica o botão de status via seletores robustos (CSS Selectors e Data Attributes) e realiza a alteração.
- **Modo Headless:** Executa em segundo plano, sem necessidade de interface gráfica ativa.
- **Auditoria (Logs):** Gera um arquivo `historico_auditoria.txt` registrando data, hora e resultado de cada execução (sucesso ou erro).
- **Tratamento de Erros:** Captura screenshots automáticos caso ocorra alguma falha na navegação, facilitando o debug.

## Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Selenium WebDriver](https://www.selenium.dev/)
- [Webdriver Manager](https://pypi.org/project/webdriver-manager/)
- Windows Task Scheduler (para agendamento)

## Pré-requisitos

Antes de começar, você precisará ter instalado em sua máquina:
- Python 3.8 ou superior
- Google Chrome

## Como usar

1. **Clone o repositório**
   ```bash
   git clone [https://github.com/seu-usuario/automacao-sults.git](https://github.com/seu-usuario/automacao-sults.git)

2. **Instale as dependências**
   ```bash
   pip install selenium webdriver-manager

3. **Configuração de Variáveis**
   > **Nota:** Por questões de segurança, as credenciais não estão no código. Crie um arquivo `.env` ou altere as variáveis no topo do script `main.py`:

   ```python
   LOGIN_URL = "[https://sua-url.sults.com.br/](https://sua-url.sults.com.br/)"
   USER = "seu-usuario"
   PASS = "sua-senha"

4. **Execução Manual**
   Para rodar o script uma vez:
   ```bash
   python main.py

##  Agendamento (Windows)

O projeto inclui um arquivo `on_off-tasker.bat` para facilitar a integração com o **Agendador de Tarefas do Windows**.

1. Configure o Agendador de Tarefas para iniciar o `on_off-tasker.bat`.
2. Defina os gatilhos (Triggers):
   - **Segunda-feira às 09:00** (Para abrir o checkout)
   - **Sexta-feira às 09:00** (Para fechar o checkout)

## 📝 Exemplo de Log

O sistema gera um arquivo de texto para auditoria:

<img width="1080" height="720" alt="image" src="https://github.com/user-attachments/assets/291ca9d6-e8a7-4130-8418-c93a18906744" />


```text
[07/01/2026 09:00:01] >>> INICIO DO PROCESSO DE BLOQUEIO
[07/01/2026 09:00:15] Login realizado com sucesso.
[07/01/2026 09:00:20] SUCESSO: Alteração realizada na URL final .../XXX
[07/01/2026 09:00:25] SUCESSO: Alteração realizada na URL final .../XXX
[07/01/2026 09:00:30] >>> FIM DO PROCESSO
--------------------------------------------------
```

**Desenvolvido por Gabriel Pereira.**
