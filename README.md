This project is inspired by the theory of conceptual spaces, and specifically by [Douven et al. (2023)](https://doi.org/10.3389/fpsyg.2023.1234483) .

# Procedure

## Data Collection
Before constructing a similarity space, it is first necessary to obtain data on the similarity of the 𝑛 elements to be represented in it. A large language model (LLM) can be asked to estimate the similarity between all possible pairs with these 𝑛 elements.
Here, the LLM prompt explicitly asks for a similarity value set between 0 and 100, where 0 corresponds to maximum dissimilarity and 100 to identity. We assume that the similarity relation satisfies the following two constraints:
  * **Identity** For any element _i_, the similarity of _i_ to itself is maximal :
    $$∀i \quad Similarity(i,i)=100 $$
    
  * **Symetry** For any pair of distinct elements _i_ and _j_, the similarity of _i_ with _j_ is equal to the similarity of _j_ with _i_.
     $$i.e. \quad ∀i,j \quad Similarity(i,j) = Similarity(j,i)$$.

Thus, in total, $`\left(\begin{matrix}n\\2\end{matrix}\right) = \frac{n(n-1)}{2}`$ different similarity judgment requests are sent serially to the LLM via an API. 

### Data formatting
We arrange these data in a $n \times n$ _similarity matrix_ . This matrix reflects the similarity judgements between these elements: each cell $`(i,j)`$ of the matrix contains the similarity of 𝑖 with 𝑗.
Following the identity constraint, for any integer _i_ up to _n_, all cells _(i,i)_ of the matrix will be equal to 100. 
Following the symmetry constraint, $`(j,i)=(i,j)`$ for all i and j, and it's a symmetric matrix.
Since there are $`n^2`$ cells in all, the _n_ diagonal elements have been set to 100, and we only need to calculate half of the remaining values, we find $`\frac{n^2 - n}{2} = \frac{n(n-1)}{2}`$

  
## Dimensionality reduction
_Multidimensional Scaling_ (MDS)  makes it possible to project these _n_ elements into a lower-dimensional space, while preserving the initial similarity relationships as far as possible. More specifically, it involves minimising a cost function called _Stress_, which measures the difference between the initial similarities and the distances in the projected space. The quality of a spatial representation obtained by an MDS can be visualised in a graph called a Shepard diagram.

In order to apply multidimensional scaling, the **similarity matrix** is converted into a **dissimilarity matrix** with :
```
dissimilarity_matrix = 1 - (similarity_matrix / 100)
```

From the previous properties it is clear that this dissimilarity matrix is also symmetrical and that all its diagonal elements are 0.

We apply a multidimensional scaling on this dissimilarity matrix with :
```
mds = MDS(n_components=2, dissimilarity='precomputed', random_state=42)
coordinates = mds.fit_transform(dissimilarity_matrix)
```




The pyton codes presented will be used to construct similarity spaces, such as the one below, obtained with Gemini-1.5-Pro :

![téléchargé (2)](https://github.com/user-attachments/assets/124be0d5-a801-4168-9a24-3f63d0158592)

References :



In the python code, we also apply hierarchical clustering, which provides a further visualization of the order in which the distance measurements come from.



Shepard diagram : More precisely, a Shepard diagram represents the relationship between the initial similarities in the matrix and the distances obtained in the space after application of the MDS. The similarity relationships of the initial data are plotted on the x-axis, while the distances between pairs of elements are plotted on the y-axis of the Shepard Diagram. Ideally, if the distances in the projected space correspond perfectly to the initial similarities, the points in a Shepard diagram should lie exactly on a monotonically decreasing line. Conversely, the less faithful the space is to the initial dissimilarities, the further these points will deviate from this straight line. In general, low-dimensional spaces are more interpretable, but risk being less faithful to the data. Conversely, high-dimensional spaces are more faithful to the data, but less interpretable.

