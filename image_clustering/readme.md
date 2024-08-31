# Clustering d'images

On peut  utiliser des réseaux de neurones convolutifs comme VGG16 ou VGG19 pour clusteriser des ensembles d'images.
<br>

### Pour load le modèle

```
import tensorflow
from tensorflow.keras import applications
import keras
from keras.models import Sequential, Model
from keras.layers import Dense, Conv2D , MaxPool2D , Flatten , Dropout , MaxPooling2D, BatchNormalization
from tensorflow.keras.applications import VGG19,VGG16

	def load_images(self):
		self.images = []
		for image in self.image_paths:
			self.images.append(cv2.cvtColor(cv2.resize(cv2.imread(self.folder_path + "\\" + image), (224,224)), cv2.COLOR_BGR2RGB))
		self.images = np.float32(self.images).reshape(len(self.images), -1)
		self.images /= 255
		print("\n " + str(self.max_examples) + " images from the \"" + self.folder_path + "\" folder have been loaded in a random order.")
```

De nombreux codes importent aussi VGG16 et VGG19 afin de leur apprendre de nouvelles images, comme :

Apprendre au modèle à classifier des images dans des catégories de site e-commerce type Amazon : https://www.kaggle.com/code/thanhphongl/vgg19-image-classification

Apprendre au modèle à classifier des images dans des catégories de langage des signes hebreux : https://github.com/matannagar/SL-ImageClustering/blob/master/ResNet50%20vgg16%20vgg19.ipynb
