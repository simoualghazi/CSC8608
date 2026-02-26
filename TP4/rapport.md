# TP 4: Deep learning pour audio
**OUALGHAZI Mohamed**
# Exercice 1:    
![alt text](image.png)

**Sortie du smoke test**
![alt text](image-1.png)

# Exercice 2:

**train_mask :** mesure la perf sur les nœuds utilisés pour optimiser (surveille underfit/overfit et la progression réelle de l’apprentissage).

**val_mask :**sert à choisir les hyperparamètres / décider d’un early stopping sans “tricher” sur le test.

**test_mask :**estimation finale “neutre” de la généralisation, à regarder une fois le modèle choisi.

Séparer évite de surestimer la perf : si on tune sur le test, on biaise les résultats.
