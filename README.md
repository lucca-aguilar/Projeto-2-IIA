# Análise de Desempenho do YOLOv11 para Detecção de Copas de Árvores

![Licença](https://img.shields.io/badge/licen%C3%A7a-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen.svg)

Este repositório contém o código e os resultados do projeto de pesquisa para a disciplina de Introdução à Inteligência Artificial, que avalia o desempenho da arquitetura YOLOv11 na tarefa de detecção de copas de árvores individuais em imagens aéreas de alta resolução.

---

## 📜 Sumário

* [Contexto do Projeto](#-contexto-do-projeto)
* [Principais Destaques](#-principais-destaques)
* [Conjunto de Dados](#-conjunto-de-dados)
* [Resultados](#-resultados)
* [Licença](#-licença)

---

## 🎯 Contexto do Projeto

Este projeto foi desenvolvido como parte da avaliação da disciplina de Introdução à Inteligência Artificial da Universidade de Brasília (UnB).

O objetivo é expandir o trabalho de benchmark de **Zamboni et al. (2021)**, que comparou 21 detectores de objetos para a detecção de copas de árvores. A proposta inicial sugeria a utilização do modelo **YOLO-MS**. No entanto, durante a fase de implementação, foram encontradas incompatibilidades técnicas que dificultaram o treinamento com a base de dados fornecida.

Diante disso, tomou-se a decisão metodológica de pivotar para a arquitetura **YOLOv11**, uma alternativa mais moderna, bem-documentada e que não havia sido avaliada no artigo de referência, tornando esta análise uma contribuição original para a área.

Foram conduzidos experimentos sistemáticos com as variantes **YOLOv11n (nano)** e **YOLOv11s (small)** para analisar o trade-off entre eficiência e performance.

---

## ✨ Principais Destaques

* **Novo Estado da Arte:** O modelo YOLOv11s treinado por 50 épocas alcançou uma **AP@0.50 de 74.9%**, superando o melhor modelo do benchmark original.
* **Análise de Overfitting:** O estudo revelou um claro comportamento de overfitting em treinamentos mais longos (>50 épocas), uma descoberta crucial para futuras implementações práticas.
* **Comparativo de Variantes:** Análise detalhada do desempenho comparativo entre as arquiteturas YOLOv11n e YOLOv11s.

---

## 🌳 Conjunto de Dados

Utilizamos o conjunto de dados público "Individual Urban Tree Crown Detection" disponibilizado por Zamboni et al. em seu artigo. O dataset contém 220 imagens aéreas de alta resolução (10 cm GSD) com 3.382 copas de árvores anotadas.

➡️ **Acesse e baixe o dataset original aqui:** [pedrozamboni/individual\_urban\_tree\_crown\_detection](https://github.com/pedrozamboni/individual_urban_tree_crown_detection)

Para usar com o YOLO, as anotações precisam ser convertidas para o formato `.txt` e o dataset deve ser estruturado conforme as instruções na seção [Como Usar](#-como-usar).

---

## 📊 Resultados

Foram realizados 6 experimentos, testando as variantes `YOLOv11n` e `YOLOv11s` com 50, 100 e 150 épocas. A tabela abaixo resume os resultados de performance (AP@0.50) no conjunto de teste.

| Modelo   | Épocas | AP@0.50 | Precisão | Recall |
| :------- | :----: | :-----: | :------: | :----: |
| YOLOv11n | 50     |  0.744  |  0.760   | 0.686  |
| YOLOv11n | 100    |  0.741  |  0.763   | 0.682  |
| YOLOv11n | 150    |  0.732  |  0.804   | 0.651  |
| **YOLOv11s** | **50** | **0.749** | **0.799** | **0.654** |
| YOLOv11s | 100    |  0.735  |  0.804   | 0.651  |
| YOLOv11s | 150    |  0.717  |  0.751   | 0.671  |

**Conclusão Principal:** O melhor resultado (**AP@0.50 de 74.9%**) foi obtido pelo **YOLOv11s com 50 épocas**. Treinamentos mais longos levaram a uma queda de performance, indicando um forte efeito de **overfitting**, que se tornou um ponto central da análise no relatório final. Mesmo com este comportamento, o resultado de pico superou o estado da arte do benchmark original.

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
