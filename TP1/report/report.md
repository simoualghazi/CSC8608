# TP1: Modern Computer Vision

OUALGHAZI Mohamed

## Dépôt du projet:
    https://github.com/simoualghazi/CSC8608/

## Arboresence TP1:



## Environnement d’exécution:
- Environnement conda : deeplearning

- Exécution : nœud GPU via SLURM (arcadia-slurm-node-2)

-Preuve CUDA :

![alt text](image.png)
### segment_anything fonctionne
![alt text](image-1.png)


### Streamlit:

UI accessible via SSH tunnel :
## Exercice 2:
![alt text](image-3.png)

image1.png   — objet unique bien isolé, cas de segmentation simple.

image2.png — forme régulière et contraste élevé.

image4.png — scène très chargée avec de nombreux objets.

image10.png — structure fine et répétitive, segmentation délicate.

image8.png — occlusions multiples (mains, filet, ballon).
### Cas simple:
![alt text](../data/images/image2.png)
### Cas complexe:
![alt text](../data/images/image8.png)

## Exercice 3:

- Modèle choisi : vit_h
- Checkpoint utilisé : sam_vit_h_4b8939.pth (stocké dans TP1/models/, non commité)

![alt text](image-2.png)

Le modèle SAM se charge correctement sur GPU (cuda). La fonction bbox→masque renvoie un masque binaire de même taille que l’image et un score flottant élevé (~0.96), ce qui indique une segmentation cohérente pour cette image. Le masque n’est pas vide (mask_sum=2566). Un avertissement PyTorch sur torch.load apparaît, mais il n’empêche pas l’exécution et provient du chargement du checkpoint.

## Exercice 4:
