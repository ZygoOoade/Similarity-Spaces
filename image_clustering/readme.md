# Clustering d'images

On peut  utiliser des réseaux de neurones convolutifs comme VGG16 ou VGG19 pour clusteriser des ensembles d'images.
<br>

### Importer le modèle :

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

Paramétrer le clustering :

```
	def clustering(self):
		model = KMeans(n_clusters=self.n_clusters, n_jobs=-1, random_state=728)
		model.fit(self.images_new)
		predictions = model.predict(self.images_new)
		#print(predictions)
		for i in range(self.max_examples):
			shutil.copy2(self.folder_path+"\\"+self.image_paths[i], "output\cluster"+str(predictions[i]))
		print("\n Clustering complete! \n\n Clusters and the respective images are stored in the \"output\" folder.")

if __name__ == "__main__":

	print("\n\n \t\t START\n\n")

	number_of_clusters = 10 # cluster names will be 0 to number_of_clusters-1

	data_path = "data" # path of the folder that contains the images to be considered for the clustering (The folder must contain only image files)

	max_examples = 500 # number of examples to use, if "None" all of the images will be taken into consideration for the clustering
	# If the value is greater than the number of images present  in the "data_path" folder, it will use all the images and change the value of this variable to the number of images available in the "data_path" folder. 

	use_imagenets = False
	# choose from: "VGG16", "VGG19" and "False" -> Default is: False
	# you have to use the correct spelling! (case of the letters are irrelevant as the lower() function has been used)

	if use_imagenets == False:
		use_pca = False
	else:
		use_pca = False # Make it True if you want to use PCA for dimentionaity reduction -> Default is: False

	temp = image_clustering(data_path, number_of_clusters, max_examples, use_imagenets, use_pca)
	temp.load_images()
	temp.get_new_imagevectors()
	temp.clustering()

	print("\n\n\t\t END\n\n")
```


De nombreux codes importent aussi VGG16 et VGG19 afin de leur apprendre de nouvelles images, comme :

Apprendre au modèle à classifier des images dans des catégories de site e-commerce type Amazon : https://www.kaggle.com/code/thanhphongl/vgg19-image-classification

Apprendre au modèle à classifier des images dans des catégories de langage des signes hebreux : https://github.com/matannagar/SL-ImageClustering/blob/master/ResNet50%20vgg16%20vgg19.ipynb


