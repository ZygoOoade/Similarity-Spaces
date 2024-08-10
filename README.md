This project is inspired by the theory of conceptual spaces, and specifically by [Douven et al. (2023)](https://doi.org/10.3389/fpsyg.2023.1234483) .

Our procedure is as follows:

* **Data collection** Before constructing a similarity space, it is first necessary to obtain data on the similarity of the 𝑛 elements to be represented in it. A large language model (LLM) can be asked to estimate the similarity between all possible pairs with these 𝑛 elements.

* **Data formatting** The data is arranged in a _similarity matrix_ . This matrix reflects the similarity judgements between these elements: each cell (𝑖,𝑗) of the matrix contains the similarity of 𝑖 with 𝑗.
  
* **Dimensionality reduction** : _Multidimensional Scaling_ (MDS)  makes it possible to project these _n_ elements into a lower-dimensional space, while preserving the initial similarity relationships as far as possible. More specifically, it involves minimising a cost function called _Stress_, which measures the difference between the initial similarities and the distances in the projected space. The quality of a spatial representation obtained by an MDS can be visualised in a graph called a Shepard diagram.

* We also apply hierarchical clustering, which provides a further visualization of the order in which the distance measurements come from.

The pyton codes presented will be used to construct similarity spaces, such as the one below, obtained with Gemini-1.5-Pro :

![téléchargé (2)](https://github.com/user-attachments/assets/124be0d5-a801-4168-9a24-3f63d0158592)

Shepard diagram : More precisely, a Shepard diagram represents the relationship between the initial similarities in the matrix and the distances obtained in the space after application of the MDS. The similarity relationships of the initial data are plotted on the x-axis, while the distances between pairs of elements are plotted on the y-axis of the Shepard Diagram. Ideally, if the distances in the projected space correspond perfectly to the initial similarities, the points in a Shepard diagram should lie exactly on a monotonically decreasing line. Conversely, the less faithful the space is to the initial dissimilarities, the further these points will deviate from this straight line. In general, low-dimensional spaces are more interpretable, but risk being less faithful to the data. Conversely, high-dimensional spaces are more faithful to the data, but less interpretable.

