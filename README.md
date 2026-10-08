# Sistema de Gestão de Hotel (Módulo 11)

Este projeto é uma aplicação de linha de comandos (CLI) desenvolvida em Python para simular a gestão de um hotel. Foi criado no âmbito do Módulo 11 e foca-se na aplicação prática de Programação Orientada a Objetos (POO), incluindo Abstração, Encapsulamento, Polimorfismo e Herança Múltipla.

## ⚙️ Funcionalidades Principais

**Para Hóspedes:**
- Fazer check-in com atribuição de quartos livres (com validação de idade mínima de 18 anos).
- Cálculo automático do total da estadia (com taxas diferentes para quartos Simples e de Luxo).
- Realizar check-out para libertar o quarto e atualizar o sistema.

**Para Funcionários (Controlo por Cargos):**
- **Rececionistas:** Consultar listas de hóspedes ativos e estado dos quartos.
- **Gerentes:** Gerar relatórios detalhados com as informações da equipa.
- **Técnicos de Manutenção:** Registar histórico de reparos.
- **Técnicos de Receção:** Demonstram herança múltipla no código, acumulando as permissões de rececionista e técnico de manutenção.

## 🛠️ Tecnologias Utilizadas

- Python 3 (Forte foco no módulo `abc` para criação de Classes Abstratas)

## 🚀 Como Instalar e Executar

Apenas precisas de ter o Python instalado na tua máquina. Não há dependências externas.

1. Clona o repositório:
```bash
git clone https://github.com/teu-user/nome-do-repositorio.git
