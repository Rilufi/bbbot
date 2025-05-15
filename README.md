# BBBot - Automatizador de Votos para o Big Brother Brasil

Bot para votação automatizada no site da Globo para o reality show Big Brother Brasil (BBB), com versões adaptadas para diferentes edições do programa.

## 📌 Visão Geral

Este repositório contém três versões do bot, cada uma adaptada para funcionar com o sistema de votação de diferentes anos do BBB:

1. **BBB 2020**: Usa Selenium para automação web tradicional
2. **BBB 2021**: Usa reconhecimento de imagem para simular cliques humanos
3. **BBB 2022**: Versão atualizada do bot de 2021 com pequenos ajustes

Cada ano teve mudanças no sistema de autenticação e votação do site da Globo, exigindo abordagens diferentes.

## 🛠 Instalação

### Requisitos Comuns
- Python 3.x
- pip (gerenciador de pacotes Python)

### Instalação por Ano

Cada pasta contém instruções específicas para sua versão. Consulte o README dentro de cada pasta (bbb20, bbb21, bbb22) para detalhes exatos.

#### Pacotes necessários (instale conforme o ano que deseja usar):
```bash
# Para BBB 2020:
pip install selenium

# Para BBB 2021 e 2022:
pip install pyautogui pillow opencv-python
