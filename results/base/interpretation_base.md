# ZeroR : 

## Observation : 
- C'est un baseline. On a un résultat de 33% de précision pour la classe classicisme. C'est normal.



# KNN : 

## Observation : 
- J'ai testé avec k = 4 et k = 8. Les résultats sont similaires et plus k est grand plus le résultat est proche de ZeroR.

## Interprétation : 
- Plus k est grand, plus il va être influencé par la classe majoritaire, et plus il va ressembler à un ZeroR.
- Le fait que KNN produise un résultat similaire de ZeroR est peut-être dû à "curse of dimentionality". Avec 450 instances, nous avons 15,290 attributs. Il faut donc réduire le nombre d'attributs avec la liste des stopwords pour que KNN puisse fonctionner.



# J48:

## Observation :
- Les résultats sont assez bons.

## Interprétation
- Si on regarde les décisions, on dirait que la classification pourrait être influencée par la longueur du texte. La première décision est si le nombre de "l'" est-il supérieur à 6. Mais le nombre de "le", étant un déterminant, est proportionnel à la longueur du texte.
- Il y a encore pas mal de stopwords dans les arbres.
- Il faut donc peut-être enlever les stopwords.



# Naïve bayes multinomial

## Observation :
- Les résultats sont vraiment très bons !

## Interprétation : 
- J'ai essayé 10 folds et 12 folds. Les résultats de 12 sont sont bien meilleurs concernant la classe du classicisme. 
- Cela montre que on pourrait s'attendre à un meilleur résultat si on prend un corpus plus large.



# SMO

## Observation :
- Les résultats sont très très très très bons !

## Interprétation : 
- C'est le meilleur algo pour l'instant. On veut voir si c'est amélioré si on ajoute d'autres options.


