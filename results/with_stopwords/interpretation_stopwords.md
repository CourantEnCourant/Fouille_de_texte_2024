# KNN

## Observation
- J'ai testé sur k = 4 et le résultat est le même que ZeroR.

## Interprétation
- Visiblement le problème de "curse of dimentionality" existe encore parce que la liste de stopwords n'a enlevé que 37 attributs. On a encore 15253 dimensions. Il faut peut-être une liste de stopwords plus robuste.
- On peut penser à d'autres stratégies de réduire le nombre de dimensions comme la lemmatisation, la suppression des hapax, etc.



# Bayes Multinomial

## Observation 
- Bayes fonctionne significativement mieux avec les stopwords. Utiliser 12 folds c'est encore mieux.
- Par exemple, avec option de 10 folds, il y a 45 classicisme classés comme du romantisme. Avec stopwords, c'est 25 poèmes.

## Interprétation
- Les stopwords sont manifestement des bruits pour naive bayes.
- Les stopwords permettent notamment d'améliorer la précision du romantisme. Le classicisme et le romantisme sont tous les deux écrits en français standard. Donc la suppression des stopwords permettent de focaliser sur la différence lexicale.



# J48

## Observation
- Le résultat est ni meilleur, ni pire...

## Interprétation
- Je sais pas trop à vrai dire...
- Mais on observe qu'il n'y a plus de mots comme "le" dont le nombre d'occurence est proportionnel à la longueur du texte.



# SMO

## Observation
- Il produit à peu près le même résultat.

## Interprétation
- La liste de stopwords n'est pas significative pour SMO.



