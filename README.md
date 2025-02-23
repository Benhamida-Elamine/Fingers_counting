# fingers_counting

Ce projet utilise la détection des mains en temps réel pour compter les doigts levés d'une main, à l'aide d'images de doigts levés et de la bibliothèque OpenCV.

## Description

L'application utilise une webcam pour capturer des images de la main, puis détermine le nombre de doigts levés en fonction de la position des points de repère sur la main. Une série d'images représentant les doigts levés de 0 à 5 est utilisée pour afficher l'index correspondant aux doigts levés. Le projet utilise également la bibliothèque `mediapipe` pour la détection des mains et `opencv` pour le traitement des images.

## Structure du projet

- `main.py` : Script principal pour exécuter le projet. Ce fichier contient la logique pour capturer la vidéo en temps réel et compter les doigts levés.
- `Function.py` : Contient la classe `handDetector` pour la détection des mains, avec des méthodes pour trouver la position des points de repère et dessiner les résultats.
- `png/` : Dossier contenant des images des doigts levés (de 0 à 5) utilisées pour afficher le nombre de doigts levés.
  
## Dépendances

Ce projet nécessite les bibliothèques suivantes :

- `opencv-python`
- `mediapipe`
- `matplotlib`


