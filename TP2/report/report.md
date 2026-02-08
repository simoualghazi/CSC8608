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
| Run 1: Baseline <br> (EulerA, 30 steps, γ=7.5) | Run 2: Steps bas <br> (15 steps) | Run 3: Steps hauts <br> (50 steps) |
| :---: | :---: | :---: |
| ![Baseline](../outputs/t2i_run01_baseline.png) | ![Steps 15](../outputs/t2i_run02_steps15.png) | ![Steps 50](../outputs/t2i_run03_steps50.png) |
| **Run 4: Guidance bas <br> (γ=4.0)** | **Run 5: Guidance haut <br> (γ=12.0)** | **Run 6: Scheduler DDIM** |
| ![Guidance 4](../outputs/t2i_run04_guid4.png) | ![Guidance 12](../outputs/t2i_run05_guid12.png) | ![DDIM](../outputs/t2i_run06_ddim.png) |