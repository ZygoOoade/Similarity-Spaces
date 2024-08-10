This project is a continuation of [Douven et al. (2023)](https://doi.org/10.3389/fpsyg.2023.1234483) .

The steps followed are as follows:

* **Data collection** Before constructing a similarity space, it is first necessary to obtain data on the similarity of the 𝑛 elements to be represented in it. LLM can be asked to estimate the similarity between all possible pairs with these 𝑛 elements.

* **Data formatting** The data is arranged in a _similarity matrix_ . This matrix reflects the similarity judgements between these elements: each cell (𝑖,𝑗) of the matrix contains the similarity of 𝑖 with 𝑗.
  
* **Dimensionality reduction** _Multidimensional Scaling_ makes it possible to project these elements into a lower-dimensional space, while preserving the initial similarity relationships as far as possible. More specifically, it involves minimising a cost
function called Stress, which measures the difference between the initial similarities and the distances in the projected space. The quality of a spatial representation obtained by an MDS can be visualised in a graph called a Shepard diagram (which is not used in the present python code). 
