**1. Como você definiria o aprendizado de máquina?**
O aprendizado de maquina é a capacidade do algoritmo de aprender a partir de um conjunto de dados. Ou seja, melhorar em alguma tarefa considerando alguma metrica de desempenho
**2. Você pode citar quatro tipos de problemas que se destacam?**
Classificação (ex: identificar spam).
Regressão (ex: prever preços de imóveis).
Clustering (ex: segmentação de clientes).
Aprendizado por reforço (ex: robô aprendendo a caminhar).
**3. O que é um conjunto de treinamento rotulado?**
Conjunto de dados onde cada um tem uma resposta conhecida, ée o conjunto de dados utilizado para treinar modelos supervisionados
**4. Quais são as duas tarefas supervisionadas mais comuns?**
Classificação e regressão
**5. Você pode nomear quatro tarefas comuns não supervisionadas?**
Clustering (agrupar dados similares).
Redução de dimensionalidade (simplificar dados mantendo estrutura).
Detecção de anomalias (identificar padrões raros).
Associação (descobrir relações entre variáveis, ex: regras de mercado).
**6. Que tipo de algoritmo de aprendizado de máquina você usaria para permitir que um robô caminhar em vários terrenos desconhecidos?**
Aprendizado por reforço, o robô aprende por tentativa e erro(recompensas e punições)
**7. Que tipo de algoritmo você usaria para segmentar seus clientes em múltiplos grupos?**
Algoritmos de clusterização(k-means e DBSCAN são exemplos)
**8. Você enquadraria o problema da detecção de spam como um problema de aprendizado supervisionado em ou um problema de aprendizado não supervisionado?**
Supervisionado, requer o rotulo para exemplos de emails que são spam
**9. O que é um sistema de aprendizado on-line?**
Processa dados por incremento, atualiza o modelo em tempo real com a entrada de novos dados
**10. O que é aprendizado out-of-core?**
Treina modelos com grndes volumes de dados que não cabem na memoria separando-os em pequenos lotes.
**11. Que tipo de algoritmo de aprendizado depende de uma medida de similaridade para fazer predições?**
K-NN, pois classifica instancias com base nas amostras mais proximas
**12. Qual é a diferença entre um parâmetro modelo e um algoritmo de aprendizado Hyperparameter?**
**13. O que os algoritmos de aprendizado baseados em modelo pesquisam? Qual é o mais comumEstratégia que eles usam para ter sucesso? Como eles fazem previsões?**
**14. Você pode citar quatro dos principais desafios do aprendizado de máquina?**
**15. Se o seu modelo tiver um excelente desempenho nos dados de treinamento, mas generaliza mal a novo Instâncias, o que está acontecendo? Você pode citar três soluções possíveis?**
O modelo esta memorizando os dados de treino, soluções:
-Regularização (ex: L1/L2).
-Coletar mais dados.
-Reduzir complexidade do modelo.
**16. O que é um conjunto de testes e por que você deseja usá-lo?**
Pode ser utilizado para avaliar o desempenho final do modelo apos o treino.
**17. Qual é o objetivo de um conjunto de validação?**
Ajustar hiperparâmetros e selecionar a melhor versão do modelo sem usar o conjunto de teste, evitando otimismo indevido.
**18. O que pode dar errado se você ajustar os hiperparâmetros usando o conjunto de testes?**
**19. O que é validação cruzada e por que você prefere isso a um conjunto de validação?**
Divide os dados em k partes, treinando k modelos (cada um usa k-1 partes para treino e 1 para validação). Vantagens:
-Melhor uso dos dados (ideal para conjuntos pequenos).
-Reduz variabilidade na avaliação comparado a um único conjunto de validação.
