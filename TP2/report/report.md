# TP 2
**OUALGHAZI Mohamed**
# Exercice 1:
![alt text](image.png)

# Exercice 2:
### Baseline text-to-image
![alt text](image-1.png)
Configuration :
- model_id: stable-diffusion-v1-5/stable-diffusion-v1-5
- scheduler: EulerA
- seed: 42
- steps: 30
- guidance: 7.5

Résultat : génération stable et reproductible d’une image produit (512×512).
# Exercice 3:
**Paramètres des expériences**

*   **Prompt**:
ultra-realistic product photo of a leather sneaker on a white background, studio lighting, soft shadow, 85mm lens, very sharp

*   **Seed**: 42

| Run ID           | Scheduler | Steps | Guidance (γ) | Objectif de l'expérience                     |
| :--------------- | :-------- | :---- | :----------- | :------------------------------------------- |
| `run01_baseline` | EulerA    | 30    | 7.5          | Référence de base                            |
| `run02_steps15`  | EulerA    | 15    | 7.5          | Évaluer l'effet de `steps` insuffisants      |
| `run03_steps50`  | EulerA    | 50    | 7.5          | Évaluer l'effet de `steps` élevés            |
| `run04_guid4`    | EulerA    | 30    | 4.0          | Évaluer l'effet d'une `guidance` faible      |
| `run05_guid12`   | EulerA    | 30    | 12.0         | Évaluer l'effet d'une `guidance` forte       |
| `run06_ddim`     | DDIM      | 30    | 7.5          | Comparer l'impact du `scheduler`             |



### Grille de Comparaison Visuelle

| Run 1: Baseline <br> (EulerA, 30 steps, γ=7.5) | Run 2: Steps bas <br> (15 steps) | Run 3: Steps hauts <br> (50 steps) |
| :---: | :---: | :---: |
| ![Baseline](../outputs/t2i_run01_baseline.png) | ![Steps 15](../outputs/t2i_run02_steps15.png) | ![Steps 50](../outputs/t2i_run03_steps50.png) |
| **Run 4: Guidance bas <br> (γ=4.0)** | **Run 5: Guidance haut <br> (γ=12.0)** | **Run 6: Scheduler DDIM** |
| ![Guidance 4](../outputs/t2i_run04_guid4.png) | ![Guidance 12](../outputs/t2i_run05_guid12.png) | ![DDIM](../outputs/t2i_run06_ddim.png) |

- Steps (15 → 30 → 50) : moins de steps réduit le temps mais peut dégrader la netteté ; 30 est un bon compromis ; 50 améliore parfois les détails avec un coût en temps plus élevé.
- Guidance/CFG (4.0 → 7.5 → 12.0) : CFG faible donne plus de liberté au modèle ; CFG élevé force la fidélité au prompt mais peut produire des artefacts ou un rendu trop contraint.
- Scheduler (EulerA vs DDIM) : EulerA produit souvent des textures plus contrastées, DDIM un rendu plus lisse et stable.
# Exercice 4:

### Grille de comparaison visuelle

| Image Source | Strength = 0.35 | Strength = 0.60 | Strength = 0.85 |
| :---: | :---: | :---: | :---: |
| ![Source](../inputs/product.jpg) | ![Strength 0.35](../outputs/i2i_run07_strength035.png) | ![Strength 0.60](../outputs/i2i_run08_strength060.png) | ![Strength 0.85](../outputs/i2i_run09_strength085.png) |


### Img2Img — Impact de strength (EulerA, seed=42, steps=30, CFG=7.5)

- **Strength 0.35** : conserve fortement la structure (cadrage, forme globale, identité du produit). Changements limités (texture/éclairage subtils).
- **Strength 0.60** : compromis : le produit reste reconnaissable mais davantage d’éléments changent (matière, détails, fond reconstruit).
- **Strength 0.85** : éloignement fort de l’image source : la structure peut être altérée (détails/proportions), le rendu devient plus “créatif”.
- **Utilisabilité e-commerce** : à strength élevé, génération d'une image trop différente du produit réel → moins acceptable pour une fiche produit (fidélité faible), utile plutôt pour concepts/variations.
