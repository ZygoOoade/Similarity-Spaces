import numpy as np
import os
from PIL import Image
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from keras.applications.vgg16 import VGG16, preprocess_input
from keras.preprocessing import image
from keras.models import Model
from keras.layers import GlobalAveragePooling2D
import shutil

# Charger le modèle VGG16 pré-entraîné sans les couches de classification
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Ajouter une couche de pooling globale
x = base_model.output
x = GlobalAveragePooling2D()(x)
model = Model(inputs=base_model.input, outputs=x)

# Fonction pour extraire les caractéristiques d'une image
def extract_features(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    features = model.predict(x)
    return features.flatten()

# Répertoire contenant les images
image_dir = '/content/cat-otter-Black&White'
image_files = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith('.png')]

# Extraire les caractéristiques de toutes les images
features = np.array([extract_features(img_path) for img_path in image_files])

# Déterminer le nombre de composants principaux en fonction du nombre d'échantillons ou de caractéristiques
n_components = min(len(image_files), features.shape[1])

# Réduction de la dimensionnalité avec PCA (optionnel)
pca = PCA(n_components=n_components)
features_reduced = pca.fit_transform(features)

# Appliquer le clustering K-means
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(features_reduced)

# Obtenir les labels de clustering
labels = kmeans.labels_

# Créer les dossiers pour chaque cluster
output_dir = '/content/clustered_images'
os.makedirs(output_dir, exist_ok=True)
for cluster in range(3):
    cluster_dir = os.path.join(output_dir, f'cluster_{cluster}')
    os.makedirs(cluster_dir, exist_ok=True)

# Copier les images dans les dossiers correspondants
for img_path, label in zip(image_files, labels):
    cluster_dir = os.path.join(output_dir, f'cluster_{label}')
    shutil.copy(img_path, cluster_dir)

print("Images clustered and saved in respective directories.")
