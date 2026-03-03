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

![alt text](image-2.png)

 # Exercice 3:
 # MLP :
 ![alt text](image-3.png)
# GCN :

![alt text](image-4.png)

| Modèle | Test Accuracy | Test Macro-F1 | Total Train Time (s) |
|--------|--------------:|--------------:|---------------------:|
| MLP    | 0.5790       | 0.5651       | 2.4951              |
| GCN    | 0.8030       | 0.7930       | 1.2979              |

### Pourquoi le GCN surpasse-t-il le MLP ici ?

Sur Cora, le graphe apporte un signal fort car le dataset est homophile : des nœuds reliés ont souvent le même label (mêmes thématiques d’articles). Le MLP ne voit que les features du nœud, alors que la GCN agrège les features des voisins, ce qui “débruite” et enrichit la représentation et améliore nettement la généralisation (ici ~0.80 vs ~0.58 en test_acc). En contrepartie, une GCN peut souffrir de lissage (over-smoothing) si on empile trop de couches : les embeddings deviennent trop similaires et la perf peut plafonner/baisser. Dans notre cas (2 couches), on profite du voisinage sans trop lisser. Si les features seules étaient déjà extrêmement discriminantes, l’écart MLP/GCN serait plus faible, voire en faveur du MLP.