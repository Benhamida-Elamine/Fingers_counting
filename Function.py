import cv2
import mediapipe 

class handDetector:
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        # Convertir l'image en RGB
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Traiter l'image pour détecter les mains
        self.results = self.hands.process(imgRGB)

        # Vérifier si des mains ont été détectées
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    # Dessiner les points de repère et les connexions entre eux
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        
        return img  # Retourner l'image avec les dessins si demandé

    def findPosition(self, img, handNo=0, draw=True):
        lmList = []  # Liste pour stocker les coordonnées des points de repère

        # Vérifier si des mains ont été détectées
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]  # Sélectionner la main spécifiée

            # Itérer à travers les points de repère de la main
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape  # Obtenir les dimensions de l'image
                cx, cy = int(lm.x * w), int(lm.y * h)  # Convertir les coordonnées normalisées en pixels

                lmList.append([id, cx, cy])  # Ajouter les coordonnées à la liste

                if draw:
                    # Dessiner un cercle sur le point de repère
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        return lmList 