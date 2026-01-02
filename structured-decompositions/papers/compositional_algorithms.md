# Compositional Algorithms on Compositional Data: Deciding Sheaves on Presheaves 

Ernst Althaus<br>Institute of Computer Science<br>Johannes Gutenberg-University<br>Staudingerweg 9 55128, Mainz, Germany<br>ernst.althaus@uni-mainz.de<br>Benjamin Merlin Bumpus*<br>Computer and Information Science and Engineering<br>University of Florida<br>432 Newell Drive, Gainesville, FL 32603, USA.<br>benjamin.merlin.bumpus@gmail.com<br>James Fairbanks ${ }^{\boldsymbol{\dagger}}$<br>Computer and Information Science and Engineering<br>University of Florida<br>432 Newell Drive, Gainesville, FL 32603, USA.<br>fairbanksj@ufl.edu<br>Daniel Rosiak<br>National Institute of Standards and Technology<br>100 Bureau Dr, Gaithersburg, MD 20899, USA<br>danielhrosiak@gmail.com

[^0]
#### Abstract

Algorithmicists are well-aware that fast dynamic programming algorithms are very often the correct choice when computing on compositional (or even recursive) graphs. Here we initiate the study of how to generalize this folklore intuition to mathematical structures writ large. We achieve this horizontal generality by adopting a categorial perspective which allows us to show that: (1) structured decompositions (a recent, abstract generalization of many graph decompositions) define Grothendieck topologies on categories of data (adhesive categories) and that (2) any computational problem which can be represented as a sheaf with respect to these topologies can be decided in linear time on classes of inputs which admit decompositions of bounded width and whose decomposition shapes have bounded feedback vertex number. This immediately leads to algorithms on objects of any C-set category; these include - to name but a few examples - structures such as: symmetric graphs, directed graphs, directed multigraphs, hypergraphs, directed hypergraphs, databases, simplicial complexes, circular port graphs and halfedge graphs.


Thus we initiate the bridging of tools from sheaf theory, structural graph theory and parameterized complexity theory; we believe this to be a very fruitful approach for a general, algebraic theory of dynamic programming algorithms. Finally we pair our theoretical results with concrete implementations of our main algorithmic contribution in the AlgebraicJulia ecosystem.

Keywords: Parameterized Complexity, Dynamic Programming, Sheaf Theory, Category Theory

## 1. Introduction

As pointed out by Abramsky and Shah [1], there are two main "organizing principles in the foundation of computation": these are structure and power. The first is concerned with compositionality and semantics while the second focuses on expressiveness and computational complexity.

So far these two areas have remained largely disjoint. This is due in part to mathematical and linguistic differences, but also to perceived differences in the research focus. However, we maintain that many of these differences are only superficial ones and that compositionality has always been a major focus of the "power" community. Indeed, although this has not yet formalized as such (until now), dynamic programming and graph decompositions are clear witnesses of the importance of compositionality in the field. Thus the main characters of the present story are:
(SC) the Structural compositionality arising in graph theory in the form of graph decompositions and graph width measures (whereby one decomposes graphs into smaller and simpler constituent parts $[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]$ ),
(AC) the Algorithmic compositionality embodied by the intricate dynamic programming routines found in parameterized complexity theory [22, 23, 24, 25, 26],
(RC) and the Representational compositionality ${ }^{1}$ arising in algebraic topology and virtually throughout the rest of mathematics in the form of sheaves [28,29,30] (whereby one systematically

[^1]assigns data to 'spaces' in such a way that one can easily keep track of how local data interacts with global data).

The study of graph decompositions and their associated 'width measures' has been an extremely active area of research which has generated a myriad of subtly different methods of decomposition $[6,7,4,23,22,2,31,12,13,14,15,16,18,19,20,21,11,17,32]$. From a computationally minded perspective, these notions are crucial for dynamic programming since they can be seen as data structures for graphs with compositional structure [22, 23, 25, 26].

Sheaves on the other hand supply the canonical mathematical structure for attaching data to spaces (or something "space-like"), where this further consists of restriction maps encoding some sort of local constraints or relationships between the data, and where the sheaf structure prescribes how compatible local data can be combined to supply global structure. As such, the sheaf structure lets us reason about situations where we are interested in tracking how compatible local data can be stitched together into a global data assignment. While sheaves were already becoming an established instrument of general application by the 1950s, first playing decisive roles in algebraic topology, complex analysis in several variables, and algebraic geometry, their power as a framework for handling all sorts of local-to-global problems has made them useful in a variety of areas and applications, including sensor networks, target tracking, dynamical systems (see the textbook by Rosiak [29] for many more examples and references).

Our contribution is to show how to use tools from both sheaf theory and category theory to bridge the chasm separating the "structure" and "power" communities. Indeed our main algorithmic result (Theorem 1.1) is a meta-theorem obtained by amalgamating these three perspectives. Roughly it states that any decision problem which can be formulated as a sheaf can be solved in linear time on classes of inputs which can built compositionally out of constituent pieces which have bounded internal complexity. In more concrete terms, this result yields linear (FPT-time) algorithms for problems such as $H$-coloring (and generalizations thereof) on a remarkably large class of mathematical structures; a few examples of these are: 1. databases, 2. simple graphs, 3. directed graphs, 4. directed multigraphs, 5. hypergraphs, 6. directed hypergraphs (i.e. Petri nets), 7. simplicial complexes, 8. circular port graphs [33] and 9. half-edge graphs.

To be able to establish (or even state) our main algorithmic result, one must first overcome two highly nontrivial hurdles. The first is that one needs to make sense of what it means for mathematical objects (which need not be graphs) to display compositional structure. The second is that, in order to encode computational problems as sheaves, one must first equip the input objects with a notion of a topology which moreover is expressive enough to encode the compositional structure of the input instances.

We overcome the first issue by abandoning the narrow notion of graph decompositions in favor of its broader, object-agnostic counterpart, namely structured decompositions. These are a recent category-theoretic generalization of graph decompositions to objects of arbitrary categories [34].

[^2]This shift from a graph-theoretic perspective to a category-theoretic one also allows us to overcome the second hurdle by thinking of decompositions as covers of objects in a category. More precisely we prove that structured decompositions equip categories of data (i.e. adhesive categories) with Grothendieck topologies. This is our main structural result (Corollary 3.8). It empowers us with with the ability to think of sheaves with respect to the decomposition topology as a formalization of the vague notion of 'computational problems whose compositional structure is compatible with that of their inputs'.

### 1.1. Roadmap

Throughout the paper we will built up all the necessary category theoretic formulations to make the following illustration a precise and formal commutative diagram (this will be Diagram 6).
![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-04.jpg?height=289&width=1524&top_left_y=991&top_left_x=179)

This diagram, whose arrows will be functors relating appropriate categories, relates structure and power by succinctly encoding all three forms of compositionality we identified earlier. The categories on the bottom row correspond to Structural Compositionality. The colored paths correspond to different algorithms:

1. the top path (in blue) corresponds to a brute-force algorithm,
2. the "middle path" crossing upwards (red then pink then blue) corresponds to a compositional algorithm, but a slow one and
3. the bottom path (in red) corresponds to a fast (FPT-time) dynamic programming algorithm.

The commutativity of the squares (and of the diagram of the whole) represents correctness of the algorithm since it implies that it is equivalent (in terms of its returned solution) to the brute force approach; this is Algorithmic Compositionality. The ingredient upon which all of our reasoning hinges is the assumption that the arrow labeled "GlobalSolSpace" is a sheaf. This is Representational Compositionality and it implies the commutativity of the whole diagram.

Algorithmic Compositionality on its own is interesting, but it is only useful when it is paired with running time guarantees. To that end, precise statements about the running time of subroutines of the algorithm can already be gleaned from Diagram 1. Indeed note that the arrow labeled "LocalSolSpace" (resp. "is empty (locally)?") corresponds to computing local solution spaces (resp. answering the decision problem locally) in order to turn decompositions of data into decompositions of solution spaces (resp. Booleans). These arrows correspond to local computations done a linear ${ }^{2}$ number of

[^3]times and thus one can intuit that the running time will be dominated by the arrow suggestively named "Algorithm". Most of our technical work will be devoted to proving the existence of this functor (Theorem 4.1) and in showing that it is efficiently computable (Theorem 1.1). This functor is not only a sensible choice, but it is also in some sense the canonical one: it is exactly what one comes to expect using standard category theoretic machinery ${ }^{3}$. All of these arguments will hinge on Representational Compositionality: they require 'GlobalSolSpace' to be a sheaf.

Given this context, we can now offer an informal statement of our main algorithmic contribution (Theorem 1.1). It states that, given any problem encoded as a sheaf with respect to the topology given by the decompositions of data, there is an algorithm which solves its associated decision problem in time that grows

1. linearly in the number of constituent parts of the decompositions and
2. boundedly (often exponentially) in terms of the internal complexity of the constituent parts.

Formally the theorem and the computational task it achieves read as follows. (Sections 2 and Section 3 are devoted to building up all of the necessary resources to make sense of this statement.)

C - SheafDecision
Input: a sheaf $\mathcal{F}: \mathrm{C} \rightarrow$ FinSet $^{o p}$ on the site ( $\mathrm{C}, \mathrm{Dcmp}$ ) where C is a small adhesively cocomplete category, an object $c \in \mathrm{C}$ and a $C$-valued structured decomposition $d$ for $c$.
Task: letting $\mathbf{2}$ be the two-object category $\perp \rightarrow \top$ and letting dec: FinSet $\boldsymbol{\rightarrow} \mathbf{2}$ be the functor taking a set to ⟂ if it is empty and to $T$ otherwise, compute $\operatorname{dec}^{o p} \mathcal{F} c$.

Theorem 1.1. Let $G$ be a finite, irreflexive, directed graph without antiparallel edges and at most one edge for each pair of vertices. Let D be a small adhesively cocomplete category, let $\mathcal{F}: \mathrm{D}^{o p} \rightarrow$ FinSet be a presheaf and let C be one of $\left\{\mathrm{D}, \mathrm{D}_{\text {mono }}\right\}$. If $\mathcal{F}$ is a sheaf on the site ( $\mathrm{C}, \mathrm{D}_{\mathrm{cmp}} \mid \mathrm{C}$ ) and if we are given an algorithm $\mathcal{A}_{\mathcal{F}}$ which computes $\mathcal{F}$ on any object $c$ in time $\alpha(c)$, then there is an algorithm which, given any C -valued structured decomposition $d: \int G \rightarrow \mathrm{C}$ of an object $c \in \mathrm{C}$ and a feedback vertex set $S$ of $G$, computes $\operatorname{dec} \mathcal{F} c$ in time

$$
\mathcal{O}\left(\max _{x \in V G} \alpha(d x)+\kappa^{|S|} \kappa^{2}\right)|E G|
$$

where $\kappa=\max _{x \in V G}|\mathcal{F} d x|$.
Theorem 1.1 enjoys three main strengths:

1. it allows us to recover some algorithmic results on graphs (for instance dynamic programming algorithms, for $H$-Coloring and for $H$-ReflColoring ${ }^{4}$ ) and

[^4]2. it allows us to generalize both decompositions and dynamic programming thereupon to other kinds of structures (not just graphs) and
3. it is easily implementable.

We shall now briefly expand on the last two of these points. Notice that, since Theorem 1.1 applies to any adhesive category, we automatically obtain algorithms on a host of other structures encoded as any category of C-sets [35, 36]. This is a remarkably large class of structures of which the following are but a few examples: 1. databases, 2. simple graphs, 3. directed graphs, 4. directed multigraphs, 5. hypergraphs, 6. directed hypergraphs, 7. simplicial complexes, 8. circular port graphs [33] and 9. half-edge graphs.

We note that categorical perspective allows us to pair - virtually effortlessly - our meta-theoretic results (specifically the special case relating to tree-shaped decompositions) with a practical, runnable implementation [37] in the AlgebraicJulia Ecosystem [38].

Finally, from a high-level view, our approach affords us another insight (already noted by Bodlaender and Fomin [39]): it is not the width of the decompositions of the inputs that matters; instead it is the width of the decompositions of the solutions spaces that is key to the algorithmic bounds.

Outline Our results rely on the following ingredients: 1. encoding computational problems as functors 2 . describing structural compositionality via diagrams (and in particular a special class thereof suited for algorithmic manipulation called structured decompositions), 3. proving that these give rise to Grothendieck topologies and finally 4. proving our main algorithmic result. In Section 2 we explain how to view computational problems as functors. In Section 3.1 we provide background on structured decompositions and we prove that they yield Grothendieck topologies (Corollary 3.8). We establish our algorithmic meta theorem (Theorem 1.1) in Section 4 and we provide a discussion of our practical implementation [37] of these results in AlgebraicJulia in Section 4.3. Finally we provide a discussion of our contributions and of opportunities for future work in Section 7.

Acknowledgements: The authors would like to thank Evan Patterson for thought-provoking discussions which influenced the development of this paper and for providing key insights that improved the implementation of structured decompositions in AlgebraicJulia [38].

### 1.2. Notation

Throughout the paper we shall assume familiarity with typical category theoretic notation as that found in Riehl's textbook [40]. We use standard notation from sheaf theory and for any notion not explicitly defined here or in Appendix A, we refer the reader to Rosiak's textbook [29]. Finally, for background on graph theory we follow Diestel's notation [3] while we use standard terminology and notions from parameterized complexity theory as found for example in the textbook by Cygan et al. [25].

## 2. Computational Problems as Functors

Computational problems are assignments of data - thought of as solution spaces - to some class of input objects. We think of them as functors $\mathcal{F}: \mathrm{C} \rightarrow$ Sol taking objects of some category C to objects of some appropriately chosen category Sol of solution spaces. Typically, since solution spaces are prohibitively large, rather than computing the entire solution space, one instead settles for more approximate representations of the problem in the form of decision or optimization or enumeration problems etc.. For instance one can formulate an $\mathcal{F}$-decision problem as a composite of the form

$$
\mathrm{C} \xrightarrow{\mathcal{F}} \mathrm{Sol} \xrightarrow{\mathrm{dec}} \mathbf{2}
$$

where dec is a functor into 2 (the walking arrow category) mapping solutions spaces to either ⟂ or ✓ depending on whether they witness yes- or no-instances to $\mathcal{F}$.

Some examples familiar to graph theorists are GaphColoring ${ }_{n}$, VertexCover ${ }_{k}$ and Odd Cycle Transversal (denoted OTC ${ }_{k}$ ) which can easily be encoded as contravariant functors into the category FinSet of finite sets, as we shall now describe.
$\operatorname{GraphCOLORING}_{n}$ is the easiest problem to define; it is simply the representable functor SimpFinGr $\left(-, K_{n}\right)$ : FinSet taking each graph $G$ to the set of all homomorphisms from $G$ to the n-vertex irreflexive complete graph. One turns this into decision problems by taking dec: FinSet $\boldsymbol{\rightarrow} \mathbf{2}$ to be functor which takes any set to ⟂ if and only if it is empty.

For VertexCover ${ }_{k}$ and $\mathrm{OTC}_{k}$ we will instead work with the subcategory

$$
\text { SimpFinGr }_{\text {mono }} \hookrightarrow \text { SimpFinGr }
$$

of finite simple graphs and monomorphisms (subgraphs) between them. Notice that, if $H^{\prime}$ is a subgraph of a graph $G^{\prime}$ - witnessed by the injection $g: H^{\prime} \hookrightarrow G^{\prime}$ - which satisfies some subgraph-closed property $P$ of interest and if $f: G \hookrightarrow G^{\prime}$ is any monomorphism, then the pullback of $g$ along $f$ will yield a subgraph of $G$ which also satisfies property $P$ (since $P$ is subgraph-closed). In particular this shows that, for any such subgraph-closed property $P$ (including, for concreteness, our two examples of being either a vertex cover or an odd cycle transversal of size at most $k$ ) the following is a contravariant 'functor by pullback' into the category of posets

$$
F_{P}: \text { SimpFinGr }{ }_{m o n o} \rightarrow \text { Pos. }
$$

Letting $U$ being the forgetful functor taking posets to their underlying sets, then we can state the corresponding decision problems (including, in particular VertexCOVER ${ }_{k}$ and $\mathrm{OCT}_{k}$ ) as the following composite

$$
\text { SimpFinGr }{ }_{\text {mono }}^{o p} \xrightarrow{F_{P}} \text { Pos } \xrightarrow{U} \text { FinSet } \xrightarrow{\text { dec }} \mathbf{2 .}
$$

## 3. Compositional Data \& Grothendieck Topologies

Parameterized complexity [25] is a two-dimensional framework for complexity theory whose main insight is that one should not analyze running times only in terms of the total input size, but also in
terms of other parameters of the inputs (such as measures of compositional structure [25]). Here we represent compositional structure via diagrams: we think of an object $c \in \mathrm{C}$ obtained as the colimit of a diagram $d: \mathrm{J} \rightarrow \mathrm{C}$ as being decomposed by $d$ into smaller constituent pieces. This section is split into two parts. In Section 3.1 we will show that diagrams yield Grothendieck topologies on adhesive categories. Then in Section 3.2 we focus on a special class of diagrams (suited for algorithmic manipulation) called structured decompositions [34]. Roughly they consist of a collection of objects in a category and a collection of spans which relate these objects (just like the edges in a graph relate its vertices).

### 3.1. Diagrams as Grothendieck Topologies

In this section we will need adhesive categories. We think of these as categories of data "in which pushouts of monomorphisms exist and «behave more or less as they do in the category of sets», or equivalently in any topos." [41] Adhesive categories encompass many mathematical structures raging from topological spaces (or indeed any topos) to familiar combinatorial structures such as: 1. databases, 2. simple graphs, 3. directed graphs, 4. directed multigraphs, 5. hypergraphs, 6. directed hypergraphs (i.e. Petri nets), 7. simplicial complexes, 8. circular port graphs [33] and 9. half-edge graphs.

Definition 3.1. (Adhesive category [36])
A category C is said to be adhesive if

1. C has pushouts along monomorphisms;
2. C has pullbacks;
3. pushouts along monomorphisms are van Kampen.

In turn, a pushout square of the form
![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-08.jpg?height=283&width=488&top_left_y=2016&top_left_x=699)
is said to be van Kampen if, for any commutative cube as in the following diagram which has the
above square as its bottom face,
![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-09.jpg?height=537&width=528&top_left_y=507&top_left_x=683)
the following holds: if the back faces are pullbacks, then the front faces are pullbacks if and only if the top face is a pushout.

We will concern ourselves with diagrams whose morphisms are monic; we call these submonic diagrams.

Definition 3.2. A submonic diagram in C of shape J is a diagram $d: \mathrm{J} \rightarrow \mathrm{C}$ which preserves monomorphisms and whose domain is a finite category with all arrows monic. We say that a category C is adhesively cocomplete if (1) it is adhesive and (2) every submonic diagram in C has a colimit.

The following result ([34, Lemma 5.10] restated here for convenience) states that we can associate - in a functorial way - to each object $c$ of an adhesively cocomplete category C the set of submonic diagrams whose colimit is $c$.

Lemma 3.3. ([34])
Let C be a small adhesively cocomplete category. For any arrow $f: x \rightarrow y$ in C and any diagram $d_{y}: \mathrm{J} \rightarrow \mathrm{C}$ whose colimit is $y$ we can obtain a diagram $d_{x}: \mathrm{J} \rightarrow \mathrm{C}$ whose colimit is $x$ by point-wise pullbacks of $f$ and the arrows of the colimit cocone $\Lambda$ over $d_{y}$.
![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-09.jpg?height=199&width=502&top_left_y=2022&top_left_x=693)

Note that we cannot do without requiring the diagrams to be monic in Lemma 3.3 since, although adhesive categories have all pushouts of monic spans, they need not have pushouts of arbitrary spans (see Definition 3.1).

As we shall now see, adhesively cocomplete categories have just enough structure for us to define a Grothendieck topologies where covers are given by colimits of monic subcategories ${ }^{5}$. We will use this result to prove (Corollary 3.8) that structured decompositions yield the desired Grothendieck topologies.

Theorem 3.4. If C is a small adhesively cocomplete category, then, denoting by $\Lambda_{d}$ the colimit cocone of any diagram $d$, the following is a functor by pullback.
subMon: $\mathrm{C}^{o p} \rightarrow$ Set
subMon: $c \mapsto\left\{\Lambda_{d} \mid d\right.$ a submonic diagram and colim $\left.d=c\right\}$

$$
\bigcup\{\{f\} \mid f: a \stackrel{\cong}{\rightrightarrows} c \text { an iso }\} .
$$

Furthermore we have that:

- for any such C the pair ( C , subMon) is a site and
- denoting by $\mathrm{C}_{\text {mono }}$ the subcategory of C having the same objects of C , but only the monomorphisms of C , we have that the following pair is a site

$$
\left(\mathrm{C}_{\text {mono }}, \text { subMon } \mid \mathrm{C}_{\text {mono }}\right) .
$$

## Proof:

The fact that subMon is a contravariant functor by pullback follows from the observation that pullbacks preserve isomorphisms together with Lemma 3.3.

Now notice that it suffices to show that subMon defines a Grothendieck pre-topology (Definition A.1) since it is known that every Grothendieck pre-topology determines a genuine Grothendieck topology [29]. We do this only for the first case (the second case is proved analogously) and to that end we proceed by direct verification of the axioms (consult Definition A. 1 in Appendix A). First of all note that Axiom ( PT1) holds trivially by the definition of subMon. It is also immediate that Axiom ( PT2) holds since we have just shown in the first part of this theorem that subMon is a contravariant "functor by pullback". Axiom ( PT3) is also easily established as follows:

- since a diagram of diagrams is a diagram, we have that a colimit of colimits is a colimit and thus the resulting colimit cocone is in the cover; and
- if we are given any singleton cover consisting of an isomorphism $\{f: b \xrightarrow{\cong} c\}$, then there are two cases: 1 . we are given another such cover $f^{\prime}: a \xrightarrow{\cong} b$ then the composite $f f^{\prime}$ is an isomorphism into $c$ and thus is in the coverage and 2 . if the cover on $b$ is a colimit cocone $\Lambda_{d}$ of submonic diagram $d$, then the composition of the components of the cocone (which are monomorphism) with isomorphism $f$ determines a diagram of subobjects of $c$ and this diagram will have $c$ as its colimit, as desired.

[^5] $\square$

Recall from Section 1 that some computational problems (e.g. VertexCover ${ }_{k}$ and $\operatorname{OCT}_{k}$ ) are stated on the category SimpFinGr ${ }_{\text {mono }}$ of finite simple graphs and the monomorphisms between them. Indeed note that, if we were to attempt to state these notions on the category SimpFinGr, then we would lose the ability to control the cardinalities of the vertex covers (resp. odd cycle transversals, etc.) since, although the pullback of a vertex cover along an epimorphism is still a vertex cover (resp. odd cycle transversals, etc.), the size of the resulting vertex cover obtained by pullback may increase arbitrarily. Thus, if we want to think of computational problems (the specific ones mentioned above, but also more generally) as sheaves, it is particularly helpful to be able to use structured decompositions as Grothendieck topologies on 'categories of monos' (i.e. $\mathrm{C}_{\text {mono }}$ for some adhesive C ) which will fail to have pushouts in general.

Tangential Remark Note that similar ideas to those of Theorem 3.4 and Corollary 3.8 can be used to define sheaves on 'synthetic spaces' (i.e. mixed-dimensional manifolds encoded as structured decompositions of manifolds). Here the idea is that one would like to define sheaves on topological spaces obtained by gluing manifolds of varying dimensions together while simultaneously remembering that the resulting object should be treated as a 'synthetic mixed-dimensional manifold' (i.e. structured decompositions of manifolds). The fact that one can use structured decompositions as topologies implies that one can speak of sheaves which are aware of the fact that the composite topological space needs to be regarded as a mixed-dimensional manifold. This is beyond the scope of the present paper, but it is a fascinating direction for further work.

### 3.2. Structured Decompositions

For our algorithmic purposes, it will be convenient to use structured decompositions, rather than arbitrary diagrams, to define Grothendieck topologies. This is for two reasons: (1) structured decompositions are a class of particularly nice diagrams which are easier to manipulate algorithmically when the purpose is to construct colimits via recursive algorithms and (2) although it is true that, given its colimit cone, one can always turn a diagram into a diagram of spans (as we argue in Corollary 3.8), this operation is computationally expensive (especially when, as we will address later, one is dealing with decompositions of prohibitively large objects such as solutions spaces).

Background on Structured Decompositions Structured decompositions [34] are category-theoretic generalizations of many combinatorial invariants - including, for example, tree-width [6, 7, 4], layered tree-width [19, 20], co-tree-width [42], $\mathcal{H}$-tree-width [21] and graph decomposition width [18] which have played a central role in graph theory and parameterized complexity.

Intuitively structured decompositions should be though of as generalized graphs: whereas a graph is a relation on the elements of a set, a structured decomposition is a generalized relation (a collection of spans) on a collection of objects of a category. For instance consult Figure 1 for a drawing of a graph-valued structured decomposition of shape $K_{3}$ (the complete graph on three vertices).

Formally, for any category C , one defines C -valued structured decompositions as certain kinds of diagrams in C as in the following definition. For the purposes of this paper, we will only need the

![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-12.jpg?height=926&width=1248&top_left_y=392&top_left_x=314)
Figure 1. A $\mathrm{Gr}_{\mathrm{H}}$-valued structured decomposition of shape $K_{3}$. The spans (which in the figure above are monic) are drawn (componentwise) dotted in red. The bags are highlighted in pink and the adhesions are highlighted in gray.

special case of structured decompositions given by diagrams whose arrows are all monic; however, for completeness, we note that the theory of structured decompositions does not rely on such a restriction. Thus, to ease legibility and since we will only work with monic structured decompositions in the present document, we will drop the adjective 'monic' and instead speak of structured decompositions (or simply 'decompositions').

## Definition 3.5. (Monic Structured Decomposition)

Given any finite graph $G$ viewed as a functor $G$ : GrSch → Set where GrSch is the two object category generated by

$$
E \underset{t}{\stackrel{s}{\rightrightarrows}} V
$$

one can construct a category $\int G$ with an object for each vertex of $G$ and an object from each edge of $G$ and a span joining each edge of $G$ to each of its source and target vertices. This construction is an instance of the more general notion of Grothendieck construction. Now, fixing a base category K we define a K-valued structured decomposition of shape $G$ (see Figure 1) as a diagram of the form

$$
d: \int G \rightarrow \mathrm{~K}
$$

whose arrows are all monic in K. Given any vertex $v$ in $G$, we call the object $d v$ in K the bag of $d$ indexed by $v$. Given any edge $e=x y$ of $G$, we call $d e$ the adhesion indexed by $e$ and we call the span $d x \leftarrow d e \rightarrow d y$ the adhesion-span indexed by $e$.

## Definition 3.6. (Morphisms of Structured Decompositions)

A morphism of K -valued structured decompositions from $d_{1}$ to $d_{2}$ is a pair

$$
(F, \eta):\left(\int G_{1} \xrightarrow{d_{1}} \mathrm{~K}\right) \rightarrow\left(\int G_{2} \xrightarrow{d_{2}} \mathrm{~K}\right)
$$

as in the following diagram where $F$ is a functor $F: \int G_{1} \rightarrow \int G_{2}$ and $\eta$ is a natural transformation $\eta: d_{1} \Rightarrow d_{2} F$ as in the following diagram.
![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-13.jpg?height=281&width=430&top_left_y=892&top_left_x=729)

The point of such abstraction is that one can now speak in a unified way about decompositions of many different kinds of objects. Indeed this is precisely our approach in this paper: we relate the compositional structure of the inputs of a computational problem to a corresponding compositional structure of the solutions spaces of the problem. To do so, we leverage the fact that the construction of the category of structured decompositions [34, Prop. 3.3] is functorial [34, Corol. 3.4]. In particular there is a functor

$$
\mathfrak{D}_{\mathrm{m}}: \text { Cat } \rightarrow \text { Cat }
$$

taking any category C to the category $\mathfrak{D}_{\mathrm{m}} \mathrm{C}$ of C -valued structured decompositions ${ }^{6}$; this is summarized in Definition 3.7 below.

## Definition 3.7. (The category of Structured Decompositions)

Category of Decompositions. Fixing a category K, K-valued structured decompositions (of any shape) and the morphisms between them (as in Definition 3.5) form a category $\mathfrak{D}_{\mathrm{m}}(\mathrm{K})$ called the category of K -valued structured decompositions. Furthermore, this construction is functorial: there is a functor $\mathfrak{D}_{\mathrm{m}}$ : Cat $\rightarrow$ Cat which takes any category K to the category $\mathfrak{D}_{\mathrm{m}}(\mathrm{K})$ and every functor $\Phi: \mathrm{K} \rightarrow \mathrm{K}^{\prime}$ to the functor $\mathfrak{D}_{\mathrm{m}}(\Phi): \mathfrak{D}_{\mathrm{m}}(\mathrm{K}) \rightarrow \mathfrak{D}_{\mathrm{m}}\left(\mathrm{K}^{\prime}\right)$ defined on objects as

$$
\mathfrak{D}_{\mathrm{m}}(\Phi):\left(\int G \xrightarrow{d} \mathrm{~K}\right) \mapsto\left(\mathfrak{D}_{\mathrm{m}}(\Phi) d: \int G \xrightarrow{d} \mathrm{~K} \xrightarrow{\Phi} \mathrm{~K}^{\prime}\right)
$$

and on arrows as
![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-13.jpg?height=237&width=891&top_left_y=2089&top_left_x=443)

[^6]The fact that $\mathfrak{D}_{\mathrm{m}}$ is a functor means that every functor $F: \mathrm{C} \rightarrow$ Sol which encodes some computational problem lifts to a functor

$$
\mathfrak{D}_{\mathrm{m} F}: \mathfrak{D}_{\mathrm{m}} \mathrm{C} \rightarrow \mathfrak{D}_{\mathrm{m}} \text { Sol }
$$

taking structured decompositions of the inputs to a computational problem (i.e. decompositions valued in C) to those valued in the solution spaces of the problem (i.e. decompositions valued in Sol) by evaluating $F$ on the bags and adhesions of the objects of $\mathfrak{D}_{\mathrm{m}} \mathrm{C}$. We will make use of this fact in Section 4 to easily encode local computations on the bags and adhesions of decompositions and for the implementations of our results (see Section 4.3).

Structured Decompositions as Grothendieck Topologies We are finally ready to show that structured decompositions yield Grothendieck topologies on adhesive categories. We will proceed in much the same way as we did for arbitrary submonic diagrams. Indeed observe [34, Corol. 5.11] that, for any small adhesively cocomplete category C, one can define (again by point-wise pullbacks as in Theorem 3.4) a subfunctor Dcmp of the functor subMon (defined in Theorem 3.4) as follows (where we once again denote by $\Lambda_{d}$ the set of arrows in the colimit cocone over $d$ ).

$$
\text { Dcmp: } \mathrm{C}^{o p} \rightarrow \mathbf{S e t}
$$

$$
\text { Dcmp: } c \mapsto\left\{\Lambda_{d} \mid \operatorname{colim} d=c \text { and } d \in \mathfrak{D}_{\mathrm{m}} \mathrm{C}\right\} \bigcup\{\{f\} \mid f: a \xrightarrow{\cong} c \text { an iso }\} .
$$

Corollary 3.8. The pairs ( C , Dcmp ) and ( $\mathrm{C}_{\text {mono }}$, $\left.\mathrm{Dcmp}\right|_{\mathrm{C}_{\text {mon }}}$ ) are sites where C is any small adhesively cocomplete category and Dcmp is the functor of Equation (2).

## Proof:

Every C-valued structured decomposition induces a diagram in C. Conversely, since C is adhesive, we have that colimit cocones of monic subcategories will consist of monic arrows. Thus, by taking pairwise pullbacks of the colimit arrows, one can recover a structured decomposition with the same colimit (because C is adhesive) and having all adhesions monic.

In the general case, there are going to be many distinct Grothendieck topologies that we could attach to a particular category, yielding different sites. In building a particular site, we have in mind the sheaves that will be defined with respect to it. It would be nice if we could use some relationship between sites to induce a relationship between the associated sheaves, and reduce our work by lifting the computation of sheaves with respect to one Grothendieck topology from the sheaves on another (appropriately related) Grothendieck topology. As it turns out, the collection of Grothendieck topologies on a category $C$ are partially ordered (by inclusion), and established results show us how to exploit this to push sheaves on one topology to sheaves on others.

We might first define maps between arbitrary coverings as follows.
Definition 3.9. A morphism of coverings from $\mathcal{V}=\left\{V_{j} \rightarrow V\right\}_{j \in J}$ to $\mathcal{U}=\left\{U_{i} \rightarrow U\right\}_{i \in I}$ is an arrow $V \rightarrow U$ together with a pair ( $\sigma, f$ ) comprised of

- a function $\sigma: J \rightarrow I$ on the index sets, and
- a collection of morphisms $f=\left\{f_{j}: V_{j} \rightarrow U_{\sigma(j)}\right\}_{j \in J}$ with
![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-15.jpg?height=181&width=245&top_left_y=515&top_left_x=866)
commuting for all $j \in J$.
With this notion of morphisms, we could define a category of the coverings on C. However, we will mostly be concerned with a particular case of such morphisms of coverings, namely where $V=U$ and $V \rightarrow U$ is just the identity map. In this case, we say that $\mathcal{V}$ is a refinement of $\mathcal{U}$.

Definition 3.10. Let C be a category and $\mathcal{U}=\left\{U_{i} \rightarrow U\right\}_{i \in I}$ be a family of arrows. Then a refinement $\mathcal{V}=\left\{V_{j} \rightarrow U\right\}_{j \in J}$ is a family of arrows such that for each index $j \in J$ there exists some $i \in I$ such that $V_{j} \rightarrow U$ factors through $U_{i} \rightarrow U$.

In sieve terms, we can simplify the above to say that, given $\mathcal{U}=\left\{U_{i} \rightarrow U\right\}$ and $\mathcal{V}=\left\{V_{j} \rightarrow U\right\}, \mathcal{V}$ is a refinement of $\mathcal{U}$ if and only if the sieve generated by $\mathcal{V}$ is contained in (a sub-sieve of) the sieve generated by $\mathcal{U}$.

Moreover, observe that any covering is a refinement of itself, and a refinement of a refinement is a refinement. As such, refinement gives us an ordering on the coverings of an object $U$. We can use this to define the following relation for Grothendieck topologies.

Definition 3.11. Let C be a category and $J, J^{\prime}$ two Grothendieck topologies on C . We say that $J$ is subordinate to $J^{\prime}$, denoted $J \leqslant J^{\prime}$, provided every covering in $J$ has a refinement that is a covering in $J^{\prime}$.

If $J \leqslant J^{\prime}$ and $J^{\prime} \leqslant J$, then $J$ and $J^{\prime}$ are equivalent.
This really says not just that any covering in $J$ is a covering in $J^{\prime}$-which makes us say that the topology $J^{\prime}$ is finer than $J$-but that for any covering in $J$, there exists a refinement among the coverings in $J^{\prime}$.

In sieve terms, $J \leqslant J^{\prime}$ just says that for any object $U$ and any sieve $S$ considered a covering sieve by $J$, there exists a sieve $S^{\prime}$ that is considered a covering sieve by $J^{\prime}$, where all arrows of $S$ are also in $S^{\prime}$. In particular, two topologies will be equivalent if and only if they have the same sieves.

Now we come to the point of these definitions. Using the main sheaf definition-i.e., a functor $F$ is a sheaf with respect to a topology $J$ if and only if for any sieve $S$ belonging to $J$ the induced map ${ }^{7}$

$$
F(U) \simeq \operatorname{Hom}\left(\mathbf{y}_{U}, F\right) \rightarrow \operatorname{Hom}(S, F)
$$

is a bijection-together with the previous definition (expressed in terms of sieves), we get the following result.

[^7]Proposition 3.12. Let $J, J^{\prime}$ be two Grothendieck topologies on a category C . If $J$ is subordinate to $J^{\prime}$, i.e., $J \leqslant J^{\prime}$, then every presheaf that satisfies the sheaf condition for $J^{\prime}$ also satisfies it for $J$.

In other words: if $J$ is subordinate to $J^{\prime}$, then we know that any sheaf for $J^{\prime}$ will automatically be a sheaf for $J$.

Proof:
We could show the result by deploying the notion of morphisms of sites (see Mac Lane and Moerdijk [30]) $f:(\mathrm{C}, J) \rightarrow(\mathrm{D}, K)$, as a certain "cover-preserving" morphism, where this is got by setting $\mathrm{D}=\mathrm{C}$ and $K=J^{\prime}$, and using the identity functor $\mathrm{C} \rightarrow \mathrm{C}$, taking any object to itself and any $J$-covering to itself as well. Precomposition with $f$ gives a functor between the category of presheaves (going the other way), and we then use the pushforward (or direct image) functor $f_{*}: \operatorname{Sh}\left(\mathrm{C}, J^{\prime}\right) \rightarrow \operatorname{Sh}(\mathrm{C}, J)$, where this is the restriction of the precomposition with $f$ down to sheaves, to push a sheaf with respect to $J^{\prime}$ to a sheaf $f_{*} F$ on $J$. Details can be found in the literature.

As a particular case, two equivalent topologies have the same sheaves.
The main take-away here is, of course, that if we can show that a particular presheaf is in fact a sheaf with respect to a topology $J^{\prime}$, and if $J$ is another topology which we can establish is subordinate to $J^{\prime}$, then we will get for free a sheaf with respect to $J$ (and with respect to any other subordinate topology, for that matter). Moreover, in particular, if there is a finest cover, verifying the sheaf axiom there will guarantee it for all covers.

Let's now connect these established results to the Grothendieck topologies that we defined in Theorem 3.4 and Corollary 3.8, namely subMon and Dcmp, where the latter is a subfunctor of the former. We can focus on showing how subMon relates to another Grothendieck topology of interest.

Proposition 3.13. Fix any adhesively cocomplete category C. The topology given by subMon on $\mathrm{C}_{\text {mono }}$ is subordinate to the subobject topology.

Proof:
The subobject topology just takes for coverings of an object $c$ (equivalence classes of) monomorphisms whose union is $c$. Need to show that any covering in the monic diagram topology can be refined by a covering in the subobject topology. This follows immediately from the definition of subMon in Corollary 3.8.

This, combined with Proposition 3.12, yields the following result which can be particularly convenient when proving that a given presheaf is indeed a sheaf with respect to the decomposition topology.

Proposition 3.14. Fix any adhesively cocomplete category C and any presheaf $\mathcal{F}$ : $\mathrm{C}^{o p} \rightarrow$ Set. If $\mathcal{F}$ is a sheaf on $(C)_{\text {mono }}$ with respect to the subobject topology, then it will automatically give us a sheaf on the site $\left(C_{\text {mono }},\left.D \mathrm{cmp}\right|_{C_{\text {mono }}}\right)$.

## 4. Deciding Sheaves

Adopting an algorithmically-minded perspective, the whole point of Thm 3.4 and Corollary 3.8 is to speak about computational problems which can be solved via compositional algorithms. To see this,
suppose we are given a sheaf $\mathcal{F}: \mathrm{C}^{o p} \rightarrow$ FinSet with respect to the site ( $\mathrm{C}, \mathrm{Dcmp}$ ). We think of this sheaf as representing a computational problem: it specifies which solutions spaces are associated to which inputs. We've already seen a concrete example of such a construction in Section 1; namely the coloring functor

$$
\text { SimpFinGr }\left(-, K_{n}\right): \text { SimpFinGr }{ }^{o p} \rightarrow \text { FinSet }
$$

which takes each graph to the set of all $n$-colorings of that graph.
In this paper we focus on decision problems and specifically on the sheaf decision problem (defined in Section 1) which we recall below for ease of reference.

## C - SheafDecision

Input: a sheaf $\mathcal{F}: \mathrm{C} \rightarrow$ FinSet $^{o p}$ on the site ( $\mathrm{C}, \mathrm{Dcmp}$ ) where C is a small adhesively cocomplete category, an object $c \in \mathrm{C}$ and a $C$-valued structured decomposition $d$ for $c$.
Task: letting $\mathbf{2}$ be the two-object category $\perp \rightarrow \top$ and letting dec: FinSet $\boldsymbol{\rightarrow} \mathbf{2}$ be the functor taking a set to ⟂ if it is empty and to T otherwise, compute $\operatorname{dec}^{o p} \mathcal{F} c$.

In this section we will show that the sheaf decision problem lies in FPT under the dual parameterization of the width of the given structured decomposition and the feedback vertex number ${ }^{8}$ of the shape of the decomposition. Notice that, when the decomposition is tree-shaped, we recover parameterizations by our abstract analogue of tree-width (which, note, can be instantiated in any adhesive category, not just that of graphs).

To that end, notice that, if C has colimits, then, since sheaves on this site send colimits of decompositions to limits of sets [29], the following diagram will always commute (see Bumpus, Kocsis \& Master [34] for a reference).
![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-17.jpg?height=173&width=535&top_left_y=1595&top_left_x=539)

For concreteness, let us unpack what this means. The blue path corresponds to first gluing the constituent parts of the decomposition together (i.e. forgetting the compositional structure) and then solving the problem on the entire output. On the other hand the red path corresponds to a compositional solution: one first evaluates $\mathcal{F}$ on the constituent parts of the decomposition and then joins ${ }^{9}$ these solutions together to find a solution on the whole. Thus, since this diagram commutes for any sheaf $\mathcal{F}$, we have just observed that there is a compositional algorithm for SheafDecision.

Unfortunately the approach we just described is still very inefficient since for any input $c$ and no matter which path we take in the diagram, we always end-up computing all of $\mathcal{F}(c)$ which is very large in general (for example, the images of the coloring sheaf which we described above have cardinalities

[^8]![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-18.jpg?height=739&width=1097&top_left_y=394&top_left_x=390)
Figure 2. A structured decomposition $P_{3} \leftarrow \overline{K_{2}} \rightarrow P_{4}$ which decomposes a 5-cycle into two paths on 2 and 3 edges respectively

that grow exponentially in the size of the input graphs). One might hope to overcome this difficulty by lifting dec to a functor from FinSet ${ }^{o p}$-valued structured decompositions to $\mathbf{2}^{o p}$-valued structured decompositions as is shown in the following diagram.
![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-18.jpg?height=177&width=918&top_left_y=1607&top_left_x=485)

However, this too is to no avail: the right-hand square of the above diagram does not commute in general. To see why, consider the 2 -coloring sheaf $\operatorname{SimpFinGr}\left(-, K_{2}\right)$ and let $d$ be the structured decomposition $P_{3} \leftarrow \overline{K_{2}} \rightarrow P_{4}$ which decomposes a 5-cycle into two paths on 2 and 3 edges respectively (see Figure 2). The image of $d$ under $\mathfrak{D}_{\mathrm{m}} \operatorname{dec}^{o p} \circ \mathfrak{D}_{\mathrm{m}} \mathcal{F}$ is $\dagger \leftarrow \top \rightarrow \top$ (since the graphs $P_{3}, \overline{K_{2}}$ and $P_{4}$ are all 2-colorable) and the colimit of this diagram in $\mathbf{2}^{o p}$ (i.e. a limit in 2; i.e. a conjunction) is T . However, 5-cycles are not 2-colorable.

Although this counterexample might seem discouraging, we will see that the approach we just sketched is very close to the correct idea. Indeed in the rest of this section we will show (Theorem 4.1) that there is an endofunctor

$$
\mathcal{A}: \mathfrak{D}_{\mathrm{m}} \text { FinSet }^{o p} \rightarrow \mathfrak{D}_{\mathrm{m}} \text { FinSet }^{o p}
$$

which makes the following diagram commute.
![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-19.jpg?height=176&width=1089&top_left_y=495&top_left_x=396)

Moreover we will show that this functor $\mathcal{A}$ can be computed efficiently (this is Theorem 1.1, which we mentioned in the introduction).

When C fails to have colimits. Before we move on to defining the object and morphism maps of $\mathcal{A}$ (which - as we shall prove in Theorem 4.1 - assemble into a functor), we will briefly note how the entire discussion mentioned above can be applied even to sheaves defined on the site $\left(\mathrm{C}_{\text {mono }},\left.\operatorname{Dcmp}\right|_{\mathrm{C}_{\text {mon }}}\right)$. Recall from Sections 2 and 3 that there are many situations in which we would like to speak of computational problems defined on the category $\mathrm{C}_{\text {mono }}$ having the same objects of C , but only those morphisms in C which are monos. In this case, since $\mathrm{C}_{\text {mono }}$ will fail to have colimits in general, we trivially cannot deduce the commutativity of the 'square of compositional algorithms' (Diagram 3) since one no longer has the colimit functor (namely colim which is marked in blue in Diagram 3). However, note that in either case - i.e. taking any $\mathrm{K} \in\left\{\mathrm{C}, \mathrm{C}_{\text {mono }}\right\}-$ if $\mathcal{F}$ is a sheaf with respect to the site ( $\mathrm{K}, \mathrm{Dcmp}$ ), then we always have that, for any covering

$$
(\kappa \in \mathrm{K}, d \in \text { Дстрк })
$$

we always have that

$$
\left(\operatorname{dec}^{o p} \circ \mathcal{F}\right)(\kappa)=\left(\operatorname{dec}^{o p} \circ \operatorname{const} \circ \mathfrak{D}_{\mathrm{m}} \mathcal{F}\right)(d) .
$$

To state this diagrammatically, we can invoke the Grothendieck construction ${ }^{10}$. For convenience we spell-out the definition of the category $\int$ Dcmp; it is defined as having

- objects given by pairs ( $c, d$ ) with $c \in \mathrm{C}$ and $d \in \operatorname{Dcmp}(c)$
- arrows from ( $c, d$ ) to ( $c^{\prime}, d^{\prime}$ ) are given by morphisms in C of the form $f_{0}: c \rightarrow c^{\prime}$ such that $\operatorname{Dcmp}(f)\left(d^{\prime}\right)=d$.

Notice that this allows us to restate Equation (5) as the commutativity of the following diagram.
![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-19.jpg?height=309&width=1012&top_left_y=1984&top_left_x=437)

[^9]where fst and snd are the evident projection functors, whose object maps are respectively fst: $(c, d) \mapsto c$ and snd: $(c, d) \mapsto d$. The point of all of this machinery is that it allows us to restate our algorithmic goal (namely Diagram (4) - whose commutativity we shall prove in Theorem 4.1) in the following manner when our category $C$ of inputs does not have colimits. (Notice that the following diagram is the formal version of Diagram 1 which we used to sketch our 'roadmap' in Section 1.)
![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-20.jpg?height=355&width=1312&top_left_y=715&top_left_x=290)

All that remains to be done is to establish that the functor $\mathcal{A}$ in Diagram 6. As we shall see, we will define this functor by making use of the monad $\mathcal{T}$ defined as follows. Recall that, for any category K with pullbacks and colimits, there is the following adjunction [34] (which is a special case of the analogous adjunction in categories of diagrams)
![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-20.jpg?height=150&width=252&top_left_y=1331&top_left_x=818)
where the functor const takes objects of K to trivial decompositions (having a single bag) and the functor colim takes decompositions to their colimits. Now, taking $\mathrm{K}=$ FinSet $^{\text {op }}$, we shall denote by $\mathcal{T}$ the monad

$$
\begin{aligned}
& \mathcal{T}: \mathfrak{D}_{\mathrm{m}} \text { FinSet }^{o p} \rightarrow \mathfrak{D}_{\mathrm{m}} \text { FinSet }^{o p} \\
& \mathcal{T}: d \mapsto(\text { const } \circ \text { colim })(d)
\end{aligned}
$$

given by this adjunction. In the proof of the following theorem we will make use of this monad to finally establish the existence of the desired functor $\mathcal{A}$.

Theorem 4.1. There is a functor $\mathcal{A}: \mathfrak{D}_{\mathrm{m}}$ FinSet ${ }^{o p} \rightarrow \mathfrak{D}_{\mathrm{m}}$ FinSet ${ }^{o p}$ such that:
(A1) there is a natural isomorphism
![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-20.jpg?height=259&width=615&top_left_y=2161&top_left_x=685)
(A2) there are natural transformations $\alpha^{1}$ and $\alpha^{2}$ which factor the unit of $\eta$ of the monad $\mathcal{T}$ - see Functor (7) - as in the following diagram
![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-21.jpg?height=188&width=501&top_left_y=560&top_left_x=743)
(A3) and the following diagram (which is Diagram (6), restated) commutes
![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-21.jpg?height=317&width=1180&top_left_y=878&top_left_x=402)

One should think of the functor $\mathcal{A}$ of Theorem 4.1 as a pre-processing routine by which one filters-out those local solutions which cannot be extended to global solutions. Furthermore, notice that there is a sense in which $\mathcal{A}$ is canonical since it arises from the monad $\mathcal{T}$. Indeed as we shall see, although most of the proof is focused on the derivation of $\mathcal{A}$, none of the steps in this derivation are ad-hoc: they are the 'obvious steps' which are completely determined by the properties of the monad $\mathcal{T}$. We find this to be a great benefit of our categorical approach.

### 4.1. Proof of Theorem 4.1

The proof is structured as follows: we shall begin by making use of the monad $\mathcal{T}$ to define the functor $\mathcal{A}: \mathfrak{D}_{\mathrm{m}}$ FinSet ${ }^{o p} \rightarrow \mathfrak{D}_{\mathrm{m}}$ FinSet ${ }^{o p}$; then we will point out how various facts accumulated through the derivation of $\mathcal{A}$ easily imply the points (A1), (A2) and (A3) listed in the statement of the theorem.

### 4.1.1. Gathering Intuition

Notice that, if we momentarily disregard any consideration of efficiency of computation, then it is easy to find a candidate for the desired functor $\mathcal{A}$. To see this, consider what happens when we pass a FinSet ${ }^{o p}$-valued structured decomposition $d$ through the monad $\mathcal{T}$. We will have that $\mathcal{T} d$ consists of a structured decomposition of shape $K_{1}$ (the one-vertex complete graph) whose bag consists of the solution space we seek to evaluate (namely the colimit of $d$ in FinSet ${ }^{o p}$ ). Thus we will clearly have that Diagram (4) commutes if we replace $\mathcal{A}$ by $\mathcal{T}$.

Although $\mathcal{T}$ is not efficiently computable (since, as we mentioned earlier, the set colim $d$ might be very large) we will see that the unit $\eta$ of the monad $\mathcal{T}$ given by the adjunction const $\vdash$ colim is the crucial ingredient needed to specify (up to isomorphism) the desired functor $\mathcal{A}$ (shown to be efficiently computable later in this section.) Thus, towards defining $\mathcal{A}$, we will first spell-out the definition of $\eta$.

Notice that $\eta$ yields a morphism of structured decompositions

$$
\eta_{d}: d \rightarrow \mathcal{T} d
$$

which by definition consists of a pair $\left(\eta_{d}^{0}, \eta_{d}^{1}\right)$ where $\eta_{d}^{0}: \int G \rightarrow \int K_{1}$ is a functor and $\eta_{d}^{1}: d \Rightarrow \mathcal{T}(d) \eta_{d}^{0}$ is a natural transformation as in the following diagram.
![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-22.jpg?height=269&width=516&top_left_y=701&top_left_x=685)

Now notice that the diagram above views $d$ and $\mathcal{T} d$ as FinSet ${ }^{o p}$-valued structured decompositions. Instead, in the interest of convenience and legibility, we will "slide the op" in Diagram (9) so as to think of $\eta_{d}$ as a morphism of FinSet-valued structured co-decompositions (i.e. contravariant structured decompositions); in other words we will rewrite Diagram (9) as follows.
![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-22.jpg?height=267&width=604&top_left_y=1231&top_left_x=644)

For clarity, we will take a moment to spell out what this change of perspective entails. First of all observe that FinSet-valued co-decompositions associate to each edge of $G$ a cospan of sets whose legs are epimorphisms (since they are monomorphisms in FinSet ${ }^{o p}$ ). The natural transformation $\lambda^{d}$ is simply the transformation $\eta_{d}^{1}$ when its components are viewed not as morphisms in FinSet ${ }^{o p}$, but as morphisms of FinSet (we choose to denote it $\lambda^{d}$ simply to avoid notational confusion). The components of $\lambda^{d}$ are functions (projections) from the single bag of $\mathcal{T} d$ to each one the bags of $d$ as shown below.

$$
\lambda_{x}^{d}: \mathcal{T} d \rightarrow d x .
$$

In particular these are given by the limit cone ${ }^{11}$ sitting above $d$ with apex $\mathcal{T} d$.

### 4.1.2. Defining the object map of $\mathcal{A}$.

With these observations in mind, we can now define the object map

$$
\mathcal{A}_{0}:\left(\left(\int G\right)^{o p} \xrightarrow{d} \text { FinSet }\right) \mapsto\left(\left(\int G\right)^{o p} \xrightarrow{\mathcal{A}_{0} d} \text { FinSet }\right)
$$

[^10]$$
G \cong K_{2} \quad d:\left(\int G\right)^{o p} \rightarrow \text { FinSet } \quad \mathcal{T} d \quad \mathcal{A}_{0} d:\left(\int G\right)^{o p} \rightarrow \text { FinSet }
$$

![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-23.jpg?height=302&width=1150&top_left_y=519&top_left_x=215)
Figure 3. A visualisation of the definition (Equations (11) and (12)) of the object map of $\mathcal{A}$ on a structured decomposition $d$ of shape $\vec{K}_{2}$ (the directed edge). The unit of the monad given by $\mathcal{T}$ yields a morphism $\left(\eta_{d}^{0}, \eta_{d}^{1}\right): d \rightarrow \mathcal{T} d$. The components of $\eta_{d}^{1}$ (namely $\eta_{d}^{1}(x)$ and $\eta_{d}^{1}(y)$ ) are morphisms in FinSet ${ }^{o p}$; when viewed as morphisms in FinSet, we denote them as $\lambda_{x}^{d}$ and $\lambda_{y}^{d}$. These morphisms are given by the limit cone over $d$ (viewed as a diagram in FinSet).

of the functor $\mathcal{A}$ which we are seeking to establish. It maps $d$ to the decomposition obtained by restricting all of the bags and adhesions of $d$ to the images of the legs of the limit cone with apex $\mathcal{T} d$ (we encourage the reader to consult Figure 3 for a visual aid). Spelling this out formally, the map $\mathcal{A}_{0}$ takes a structured co-decomposition $d:\left(\int G\right)^{o p} \rightarrow$ FinSet to the structured co-decomposition $\mathcal{A}_{0} d:\left(\int G\right)^{o p} \rightarrow$ FinSet which has the same shape as $d$ and which is defined as follows:

$$
\begin{aligned}
& \mathcal{A}_{0} d:\left(x \in \int G\right) \mapsto \operatorname{Im} \lambda_{x}^{d} \\
& \mathcal{A}_{0} d:\left(e \stackrel{f_{x, e}}{\leftarrow} x \in \operatorname{Mor}\left(\int G\right)^{o p}\right) \mapsto\left(\operatorname{Im} \lambda_{e}^{d} \stackrel{\left.f_{x, e}\right|_{\operatorname{lm} \lambda_{x}^{d}}}{\leftarrow} \operatorname{Im} \lambda_{x}^{d}\right)
\end{aligned}
$$

### 4.1.3. Preliminaries of the definition of the morphism map of $\mathcal{A}$.

Now, towards defining the morphism map $\mathcal{A}_{1}$, observe that, by the definition of $\mathcal{A}_{0}$ via the unit $\eta$ of $\mathcal{T}$, we have that $\eta$ factors as
![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-23.jpg?height=166&width=764&top_left_y=1863&top_left_x=564)
where, for any $x \in \int G$, the maps $\mathfrak{a}_{d}^{1}$ and $\mathfrak{a}_{\mathcal{A} d}^{2}$ shown below
![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-23.jpg?height=269&width=800&top_left_y=2145&top_left_x=544)
are respectively defined by restriction and corestriction ${ }^{12}$ of $\lambda^{d}$. Spelling this out, these maps are defined as the following morphisms in FinSet

$$
\begin{array}{ll}
\mathfrak{a}_{d}^{1}(x):= & \mathcal{A} d x \xrightarrow{\stackrel{\left.\mathrm{id}_{d x}\right|_{\operatorname{Im} \lambda_{x}^{d}}}{\longrightarrow}} d x \\
\mathfrak{a}_{\mathcal{A} d}^{2}(x):= & \mathcal{T} d K_{1} \xrightarrow{\left.\lambda_{x}^{d}\right|^{\ln \lambda_{x}^{d}}} \mathcal{A} d x
\end{array}
$$

### 4.1.4. Defining the morphism map of $\mathcal{A}$.

Given any morphism $q=\left(q^{0}, q^{1}\right)$ of FinSet-valued structured co-decompositions as in the following diagram
![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-24.jpg?height=271&width=602&top_left_y=993&top_left_x=644)
we have, by Diagram (13) and the functoriality of the monad $\mathcal{T}$ and the naturality of its unit, that the following diagram commutes.
![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-24.jpg?height=422&width=817&top_left_y=1422&top_left_x=539)

Recall that each of the morphisms in the above diagram are themselves morphisms in a category of diagrams consisting of a functor and a natural transformation where the natural transformation points "backwards" (for example as in Diagram (15)). For instance recall that the morphism $\eta_{d}: d \rightarrow \mathcal{T} d$ (drawn in Diagram (9)) corresponds to the limit cone over $d$.

We are seeking to prove the existence of a morphism $\mathcal{A}_{0} d \rightarrow \mathcal{A}_{0} d^{\prime}$ which commutes with Diagram (16). This will follow from the commutativity of Diagram (16). However, it deserves to be unpacked as follows.

Consider Diagram (16). The morphism $\mathcal{T} q$ represents a function from the limit of $d^{\prime}$ to the limit of $d$. The morphisms $\eta_{d}$ and $\eta_{d^{\prime}}$ represent the limit cones sitting above $d$ and $d^{\prime}$ respectively. The

[^11]morphism $q$ (defined in Diagram (15)) corresponds to assigning to each object $x \in \operatorname{dom} d$ a morphism
$$
q_{x}^{1}:\left(q^{0} x \in \operatorname{dom} d^{\prime}\right) \rightarrow(x \in \operatorname{dom} d) .
$$

The commutativity of Diagram (16) amounts to stating the following: for each $x \in \operatorname{dom} d$ and each component $q_{x}^{1}$ of $q_{1}$, the range of $q_{x}^{1}$ is completely contained in the images of the leg $\lambda_{x}^{d}: \mathcal{T} d \rightarrow d x$ of the limit cone $\lambda^{d}$ at $x$. But then, this means that, by restricting $q_{x}^{1}$ to the image of $\lambda^{d^{\prime}} x$, we obtain the desired morphism shown below (where recall $\alpha_{d^{\prime}}^{1}:=\left(\operatorname{id}_{\left(\int G\right)^{o p}}, \mathfrak{a}_{d^{\prime}}^{1}\right)$.
![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-25.jpg?height=257&width=592&top_left_y=809&top_left_x=648)

In summary, this derivation allowed us to define the desired morphism $\mathcal{A} q: \mathcal{A}_{0} d \rightarrow \mathcal{A}_{0} d^{\prime}$ given by

$$
\mathcal{A}_{1}:\left(\left(q_{0}, q_{1}\right): d \rightarrow d^{\prime}\right) \mapsto\left(\left(q_{0}, \mathfrak{a}_{d^{\prime}}^{1} \circ q^{1}\right)\right) .
$$

### 4.1.5. Completing the proof

The functoriality of $\mathcal{A}$ is immediate: it clearly preserves identities and, since $\mathcal{T}$ is a functor, one can see that $\mathcal{A}$ preserves composition by inspection of Diagram (16). On the other hand Point (A1) can be seen to follow by the definition of $\mathcal{A}_{0}$ and the properties of limits in FinSet (namely that, if $X_{1} \stackrel{\pi_{1}}{\leftrightarrows} X_{1} \times_{S} X_{2} \xrightarrow{\pi_{2}} X_{2}$ is the pullback of a span $X_{1} \xrightarrow{f_{1}} S \stackrel{f_{2}}{\leftrightarrows} X_{2}$, then $X_{1} \times_{S} X_{2}$ will also be isomorphic to the pullback object of the span $\operatorname{Im} \pi_{1} \xrightarrow{f_{1} \|_{\operatorname{Im} \pi_{1}}} S \stackrel{\left.f_{2}\right|_{\operatorname{Im} \pi_{1}}}{\longleftrightarrow} \operatorname{Im} \pi_{2}$ ). Since the naturality of $\alpha^{1}$ and $\alpha^{2}$ is evident, Point (A2) just amounts to the commutativity of Diagram (13). Finally, to show Point (A3), observe that, by the definition of the object map $\mathcal{A}_{0}$ and since the only set with a morphism to the empty set is the empty set, we have that $\wedge \circ \mathfrak{D}_{\mathrm{m}} \operatorname{dec}^{o p} \circ \mathcal{A}=\operatorname{dec}^{o p} \circ$ colim .

### 4.2. An Algorithm for Computing $\mathcal{A}$

Recall that one should think of the functor $\mathcal{A}$ of Theorem 4.1 as a pre-processing routine which filtersout those local solutions which cannot be extended to global solutions. This intuition suggests the following local filtering algorithm according to which one filters pairs of bags locally by taking pullbacks along adhesions and then retaining only those local solutions which are in the image of the projection maps of the pullbacks.

Recursive applications of Algorithm 1 allow us to obtain the following algorithm for sheaf decision on tree-shaped structured decompositions.

Lemma 4.2. There is an algorithm (namely Algorithm 2) which correctly computes $\mathcal{A d}$ on any input FinSet-valued structured co-decomposition $d:\left(\int G\right)^{o p} \rightarrow$ FinSet in time $O\left(\kappa^{2}\right)|E G|$ where $\kappa= \max _{x \in V G}|d x|$ whenever $G$ is a finite, irreflexive, directed tree.

```
Algorithm 1 Filtering
    Input: a FinSet-valued structured co-decomposition $d:\left(\int G\right)^{o p} \rightarrow$ FinSet and an edge $e=x y$ in $G$.
    - compute the pullback $d x \stackrel{\pi_{x}}{\stackrel{\text { r }}{\leftarrow}} d x \times_{d e} d y \xrightarrow{\pi_{y}} d y$ of the cospan $d x \xrightarrow{f_{x}} d e_{x, y} \stackrel{f_{y}}{\leftarrow} d y$ associated to each
    edge $e=x y$ in $G$
    - let $d_{e}$ be the decomposition obtained by replacing the cospan associated to $e$ in $d$ by the the cospan
        $\operatorname{Im} \pi_{x} \xrightarrow{f_{x} \|_{\operatorname{lm} \pi_{x}}} d e_{x, y} \stackrel{f_{y} \|_{\operatorname{lm} \pi_{y}}}{\longleftrightarrow} \operatorname{Im} \pi_{y}$,
    return $d_{e}$.
```


## Proof:

Fixing any enumeration $e_{1}, \ldots, e_{m}$ of the edges of $G$, we will show that that following recursive procedure (Algorithm 2) satisfies the requirements of the lemma when called on inputs $\left(d,\left(e_{1}, \ldots, e_{m}\right)\right)$. Notice that in Algorithm 1 we always have an injection $\operatorname{Im} \pi_{x} \hookrightarrow d x$. By this fact and since Algorithm 2

```
Algorithm 2 Recursive filtering
    Input: a FinSet ${ }^{o p}$-valued structured decomposition $d:\left(\int G\right)^{o p} \rightarrow$ FinSet and a list $\ell$ of edges of $G$.
    if $\ell$ is empty then
        return $d$
    else
        - split $\ell$ into its head-edge $e$ and its tail $\ell^{\prime}$
        - let $d_{e}$ be the output of Algorithm 1 on inputs ( $d, e$ )
        - recursively call Algorithm 2 on inputs ( $d_{e}, \ell^{\prime}$ ).
    end if
```

amounts to computing $|E G|$ pullbacks in FinSet and hence the running time bound is evident. Now suppose the input decomposition is tree-shaped (i.e. suppose that $G$ is a tree); we will proceed by induction to show that the output of Algorithm 1 is isomorphic to $\mathcal{A} d$. If $G \cong K_{1}$ (the one-vertex complete graph), then the algorithm terminates immediately (since $G$ has no edges) and returns $d$. This establishes the base-case of the induction since $A d \cong d$ whenever $G \cong K_{1}$. Now suppose $|E G|>0$ and let $e=x_{1} x_{2}$ be the last edge of the tree $G$ over which Algorithm 2 iterates upon. The removal of $e$ splits $G$ into two sub-trees $T_{1} \hookrightarrow G$ and $T_{2} \hookrightarrow G$ containing the nodes $x_{1}$ and $x_{2}$ respectively. In turn these two trees induce two sub-decompositions $\mathrm{t}_{i}: d_{i} \hookrightarrow d$ of $d$; these are given by the following composite functors:

$$
d_{1}:\left(\int T_{1}\right)^{o p} \hookrightarrow\left(\int G\right)^{o p} \rightarrow \text { FinSet } \quad \text { and } \quad d_{2}:\left(\int T_{2}\right)^{o p} \hookrightarrow\left(\int G\right)^{o p} \rightarrow \text { FinSet. }
$$

By the induction hypothesis we have that, for each $i \in\{1,2\}$, running Algorithm 1 on $d_{i}$ yields an object $\delta_{i}$ isomorphic to $\mathcal{A} d_{i}:\left(\int T_{i}\right)^{o p} \rightarrow$ FinSet. Thus, by Point (A2) of Theorem 4.1, the span of
structured decompositions $d_{1} \stackrel{l_{1}}{\hookrightarrow} d \stackrel{l_{2}}{\rightleftharpoons} d_{2}$ yields the following commutative diagram.
![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-27.jpg?height=541&width=800&top_left_y=517&top_left_x=548)

Now consider the cospan $d x_{1} \xrightarrow{e_{x_{1}}} d e \stackrel{e_{x_{1}}}{\longleftrightarrow} d x_{2}$. Passing it through the functor const to obtain morphisms

$$
\operatorname{const} e_{x_{1}}: \operatorname{const} d^{\prime} \rightarrow d_{i}
$$

such that the following commutes.
![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-27.jpg?height=543&width=1134&top_left_y=1404&top_left_x=376)

These observations imply that the following is a pullback diagram in FinSet.
![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-27.jpg?height=325&width=817&top_left_y=2087&top_left_x=535)

We can factor this diagram further as follows (where $\lambda_{i}$ is the leg of the cone with apex $\lim d_{i}$ ).
![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-28.jpg?height=584&width=1038&top_left_y=515&top_left_x=425)

From which we observe that all that remains to be shown is that the unique pullback arrow $u$ shown in the following diagram
![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-28.jpg?height=583&width=1040&top_left_y=1309&top_left_x=425)
is a surjection. To see why this suffices, notice that, if $u$ is surjective, then the entire claim will follow since we would have

$$
\lambda_{i} \rho_{i}=\pi_{i} u \Longrightarrow \operatorname{Im} \lambda_{i} \rho_{i}=\operatorname{Im} \pi_{i} u=\left.\operatorname{Im} \pi_{i}\right|_{\operatorname{Im} u}=\operatorname{Im} \pi_{i} .
$$

But then this concludes the proof since the surjectivity of $u$ is immediate once we recall that $\mathcal{A} d_{i} x_{i}$ was defined as $\operatorname{Im} \lambda_{i}$ and that $\lim d=\lim d_{1} \times_{d e} \lim d_{2}$ (as established in Diagram 19).

Notice that Lemma 4.2 does not naïvely lift to decompositions of arbitrary shapes. For instance
consider the following example of a cyclic decomposition of a 5 -cycle graph with vertices $\left\{x_{1}, \ldots, x_{5}\right\}$.
![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-29.jpg?height=396&width=872&top_left_y=471&top_left_x=507)

Passing this decomposition through the two-coloring sheaf $\operatorname{SimpFinGr}\left(-, K_{2}\right)$ (i.e. applying the functor $\mathfrak{D}_{\mathrm{m}}$ SimpFinGr $\left(-, K_{2}\right)$ ) we obtain a structured co-decomposition $\delta$ valued in FinSet and whose bags are all two element sets corresponding to the two proper colorings of any edge. Now notice that, since odd cycles are not two-colorable at least one of the bags of $\mathcal{A} \boldsymbol{\delta}$ will be empty. In contrast, it is easy to verify that the output of Algorithm 1 on $\delta$ is isomorphic to $\delta$ itself.

Although these observations might seem to preclude us from obtaining algorithmic results on decompositions that are not tree-shaped, if we are willing to accept slower running times (which are still FPT-time, but under a double parameterization rather than the single parameterization of Lemma 4.2), then we can efficiently solve the sheaf decision problem on decompositions of other shapes as well. This is Theorem 1.1 which we are finally ready to prove. For clarity, we wish to point out that the following result is exactly the same as Lemma 4.2 when we are given a decomposition whose shape is a tree: trees trivially have feedback vertex number zero.

## Theorem 4.3. (Theorem 1.1 restated)

Let $G$ be a finite, irreflexive, directed graph without antiparallel edges and at most one edge for each pair of vertices. Let D be a small adhesively cocomplete category, let $\mathcal{F}: \mathrm{D}^{o p} \rightarrow$ FinSet be a presheaf and let C be one of $\left\{\mathrm{D}, \mathrm{D}_{\text {mono }}\right\}$. If $\mathcal{F}$ is a sheaf on the site ( $\mathrm{C}, \mathrm{D}_{\mathrm{cmp}} \mid \mathrm{C}$ ) and if we are given an algorithm $\mathcal{A}_{\mathcal{F}}$ which computes $\mathcal{F}$ on any object $c$ in time $\alpha(c)$, then there is an algorithm which, given any C -valued structured decomposition $d: \int G \rightarrow \mathrm{C}$ of an object $c \in \mathrm{C}$ and a feedback vertex set $S$ of $G$, computes $\operatorname{dec} \mathcal{F} c$ in time

$$
\mathcal{O}\left(\max _{x \in V G} \alpha(d x)+\kappa^{|S|} \kappa^{2}\right)|E G|
$$

where $\kappa=\max _{x \in V G}|\mathcal{F} d x|$.

## Proof:

[Proof of Theorem 1.1] Recall that, by Point (A3) of Theorem 4.1 the following diagram commutes.
![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-29.jpg?height=345&width=1308&top_left_y=2079&top_left_x=292)

Our proof will will rely on this fact together with the following claim.
Claim 4.4. Consider the image of $d$ under $\mathfrak{D}_{\mathrm{m}} \mathcal{F}$ and view it as a FinSet-valued structured co-decomposition $\mathfrak{D}_{\mathrm{m} \mathcal{F}} d:\left(\int G\right)^{o p} \rightarrow$ FinSet, fix any vertex $x \in V G$ and any enumeration $\ell=\left(e_{1}, \ldots, e_{n}\right)$ of the edges incident with $x$. Let $\gamma_{s}$ be the output of Algorithm 2 when applied to the input $\left(\mathfrak{D}_{\mathrm{m} \mathcal{F}} d, \ell\right)$ and, letting $G^{\prime} \hookrightarrow G$ be the subgraph of $G$ obtained by removing all edges incident with $x$, define $\delta_{s}$ to be the decomposition $\delta_{s}:\left(\int G^{\prime}\right)^{o p} \hookrightarrow\left(\int G\right)^{o p} \xrightarrow{\gamma_{s}}$ FinSet.
If $\mathfrak{D}_{\mathrm{m} \mathcal{F}} d(x)$ is a singleton, then $\left.\wedge \circ \operatorname{dec}^{o p} \circ \mathcal{A} \circ \mathfrak{D}_{\mathrm{m} \mathcal{F}}\right)(d)=\left(\wedge \circ \operatorname{dec}^{o p} \circ \mathcal{A}\right)\left(\delta_{s}\right)$.

## Proof:

[Proof of Claim 4.4] If the bag $\mathfrak{D}_{\mathrm{m} \mathcal{F}} d x$ has precisely one section, let's call it $\xi$, then every matching family for $\mathcal{F}$ on $d$ must involve $\xi$. Notice that we trivially have that $\lim \mathfrak{D}_{\mathrm{m} \mathcal{F}} d=\lim \gamma_{s}$ since the local pullbacks performed by Algorithm 1 (and hence Algorithm 2 cannot change the overall limit) and hence we have

$$
\left(\wedge \circ \operatorname{dec}^{o p} \circ \mathcal{A} \circ \mathfrak{D}_{\mathrm{m} \mathcal{F}}\right)(d)=\left(\wedge \circ \operatorname{dec}^{o p} \circ \mathcal{A}\right)\left(\gamma_{s}\right) .
$$

But now notice that, since $\mathfrak{D}_{\mathrm{m} \mathcal{F}} d x$ is a singleton, any collection of sections $\left(\zeta \in \delta_{s}(z)\right)_{z \in V G^{\prime}}$ must give rise to a matching family for $d$ since, by the construction of $\delta_{s}$, we have that each such section $\zeta$ in the family must agree with $\xi$. But then, as desired, we have proven that

$$
\left(\wedge \circ \operatorname{dec}^{o p} \circ \mathcal{A} \circ \mathfrak{D}_{\mathrm{m} \mathcal{F}}\right)(d)=\left(\wedge \circ \operatorname{dec}^{o p} \circ \mathcal{A}\right)\left(\delta_{s}\right) .
$$

In light of this result, notice that, if $\mathcal{F} d s$ is a singleton for each $s \in S$ (where recall that $S$ is a feedback vertex set in $G$ ), then, by repeatedly applying Claim 4.4 until the output decomposition is a forest and then applying the algorithm of Lemma 4.2, we can correctly solve the sheaf decision problem in time $O\left(\max _{x \in V G} \alpha(d x)+\kappa^{2}\right)|E G|$ (since this entire procedure amounts to one call to algorithm $\mathcal{A}_{\mathcal{F}}$ in order to compute $\mathfrak{D}_{\mathrm{m} \mathcal{F}} d$ and $O(|E G|)$-calls to the edge-filtering algorithm - i.e. Algorithm 1).

Now, at an intuitive level, if there exists $s \in S$ such that $\mathcal{F} d s$ is not a singleton, then we can simply repeat the above procedure once for each section in $\mathcal{F} d s$. Stating this more formally, define for each $\sigma \in \prod_{s \in S} \mathcal{F} d s$ the FinSet-valued structured co-decomposition $\omega_{\sigma}:\left(\int G\right)^{o p} \rightarrow$ FinSet by replacing all bags of the form $\mathfrak{D}_{\mathrm{m} \mathcal{F}} d s$ in $\mathfrak{D}_{\mathrm{m} \mathcal{F}} d$ with the bag $\omega_{\sigma} s:=\left\{\sigma_{s}\right\}$ (where $\sigma_{s}$ is the section at index $s$ in the tuple $\sigma$ ). Then, since $\mathcal{F}$ is a sheaf, it follows that

$$
\operatorname{dec}^{o p} \mathcal{F} c=\bigvee_{\sigma \in \prod_{s \in S} \mathcal{F} d s}\left(\wedge \circ \mathfrak{D}_{\mathrm{m}} \operatorname{dec}^{o p} \circ \mathcal{A}\right)\left(\omega_{\sigma}\right)
$$

This will have the desired running time since it corresponds to first computing $\mathfrak{D}_{\mathrm{m} \mathcal{F}} d$ (which we can do in time $\mathcal{O}\left(\max _{x \in V G} \alpha(d x)\right)$ using algorithm $\mathcal{A}_{\mathcal{F}}$ ) and then running Algorithm 2 (whose correctness and running time are established by Claim 4.4 and Lemma 4.2) at most $\left(\left|\prod_{s \in S} \mathcal{F} d s\right| \in O\left(k^{|S|}\right)\right)$-many times.

The reader might notice that we have so far avoided mentioning notions of width of the input decompositions and that indeed these considerations do not appear in the statements of the algorithms
of Lemma 4.2 or Theorem 1.1. This is for good reason: one should observe that it is not the width of the decompositions of the inputs that matters; instead it is the width of the decompositions of the solutions spaces that is key to the algorithmic bounds. In categories (such as that of graphs, say) where objects come equipped with natural notions of 'size', then one might expect that it would be convenient to state the running time of the algorithm in terms of the maximum bag size in the input decomposition. However, we maintain (in accordance with observations previously made by Bodlaender and Fomin [39]) that quantifying the running time of the algorithm in terms of the width of the decompositions of the inputs is misleading. To see why, consider the very simple, but concrete case of algorithms for coloring on tree decompositions. In this situation, it is perfectly fine to admit very large bags in our decomposition so long as the following two conditions are met: 1. the local solution spaces (which are sets) associated to these bags are small and 2 . these solution spaces can be determined in a bounded amount of time. A trivial, but illuminating example of this phenomenon is the case in which we allow large bags (of unbounded size) in our decomposition as long as they consist of complete graphs: for such graphs we have only one proper coloring up to isomorphism and this can be determined in linear time.

### 4.3. Implementation

Compared to the traditional, combinatorial definition of graph decompositions [6, 7, 4], our category theoretic formulation of structured decompositions has two advantages which we have already encountered.

1. Object agnosticism Structured decompositions allow us to describe decompositions of objects of any adhesive category and thus one doesn't need to define ad-hoc decompositions on a case-by-case basis whenever one encounters a new kind of combinatorial data.
2. Functorial Algorithmics The functoriality of $\mathfrak{D}_{\mathrm{m}}$ (i.e. of categories of structured decompositions) allows us to make explicit use of solution spaces and decompositions thereof. This allows us to state the correctness of algorithmic results as the commutativity of appropriate diagrams (e.g. Diagram (4)) from which one can moreover infer running time bottlenecks.

However, there is a further, more practical benefit of our category-theoretic perspective: it allows for a very smooth transition from mathematics to implementation. Indeed, our theoretical algorithmic results of Section 4 can be easily paired with corresponding implementations [37] in the AlgebraicJulia ecosystem [38]. As a proof of concept, we have implemented structured decompositions and Algorithm 2 for SheafDecision on tree-shaped decompositions which demonstrates the seamless transition from mathematics to code which one can experience one category theory is embraced as the core theoretical abstraction. We encourage the reader to consult the relevant repository [37] for further details of the implementation.

## 5. An Open Problem on the Shapes of the Decompositions

Theorem 1.1 yields FPT-time algorithms for problems encoded as sheaves on adhesive categories. When instantiated, this allows us to obtain algorithmic results on many mathematical objects of algo-
rithmic interest such as: 1. databases, 2. simple graphs, 3. directed graphs, 4. directed multigraphs, 5. hypergraphs, 6. directed hypergraphs, 7. simplicial complexes, 8. circular port graphs [33] and 9. half-edge graphs. However one should note that these parameterizations are only useful if: (1) not all objects in this class have bounded structured decomposition width and (2) only if the feedback vertex number of the class of decomposition shapes is bounded. Notice that it is easy to verify that, for all the examples mentioned above, not all objects have bounded tree-shaped decompositions. However, when it comes to decomposition shapes that are not trees, the question of whether all objects have bounded width with respect to a fixed class of decomposition shapes, it not obvious. Indeed, this will motivate Open Problem 6 which will arise naturally by the end of this section in which we will enquire about how our algorithmic results - which involve arbitrary decomposition shapes - compare to more traditional results in graph theory which solely make use of tree-shaped decompositions. In particular we will now briefly argue that, for the case of graph decomposition width (as defined by Carmesin [18]), our results end up yielding FPT algorithms only on classes of graphs which have bounded tree-width. Determining whether these observations can be carried over to more general classes of objects is a fascinating new direction for work (see Open Problem 6).

To see this, first of all note that, for any FinGr-valued decomposition $d: \int H \rightarrow$ FinGr of a graph $G$, it is easy to see that the treewidth $\operatorname{tw}(H)$ of our shape graph $H$ is at most its feedback vertex number. Furthermore, if the shape graph $H$ has treewidth at most $t_{H}$ and the input graph $G$ has $H$ width at most $t_{G}$, then we can easily build a tree decomposition of $G$ of width $t_{H} \cdot t_{G}$, implying that we only compute on graphs with bounded treewidth. Since we are now only dealing with graphs, it will be convenient to switch to Carmesin's [18] more combinatorial notation ${ }^{13}$. Let $\mathcal{T}^{T}=\left(T,\left(X_{t}\right)_{t \in V(T)}\right)$ be a tree decomposition of $H$ and $\mathcal{T}^{G}=\left(H,\left(Y_{t}\right)_{t \in V(H)}\right)$ be a $H$-decomposition of $G$. We claim that $\mathcal{T}=\left(T,\left(\cup_{t^{\prime} \in X_{t}} Y_{t^{\prime}}\right)_{t \in V(T)}\right.$ is a tree decomposition of $G$. Coverage is easy as each bag of $\mathcal{T}^{H}$ is contained in at least one bag of $\mathcal{T}$ as all bags are covered in $\mathcal{T}^{G}$. For the coherence, we argue as follows. Assume a vertex $v \in V(G)$ is in two bags $t, t^{\prime} \in V(\mathcal{T})$, but not in a bag $t^{\prime \prime}$ on the path in $\mathcal{T}$ from $t$ to $t^{\prime}$. By the construction of the bags of $\mathcal{T}$, there is a vertex $u \in Y_{t}$ whose bag contains $v$ and similarly a vertex $u^{\prime} \in Y_{t^{\prime}}$ containing $v$. By the coherence of $\mathcal{T}^{H}$, there has to be a path $p$ between $u$ and $u^{\prime}$ in $\mathcal{T}^{H}$ such that $v$ is in all bags $Y_{\tilde{t}}$ for $\tilde{t} \in V(p)$ (the subgraph of $H$ induced by the bags containing $v$ is connected). As $v$ is not in the bag of $t^{\prime \prime}$ of $\mathcal{T}$, no vertex of $V(p)$ is in $X_{t^{\prime \prime}}$ (of $\mathcal{T}^{T}$ ), which contradicts that the removal of $X_{t^{\prime \prime}}$ separates $u \in X_{t} \backslash X_{t^{\prime \prime}}$ from $X_{t^{\prime}} \backslash X_{t^{\prime \prime}} \ni u^{\prime}$.

Hence, if the treewidth of the graphs of the class $\mathcal{H}$ allowed for the shape of the structured decomposition is bounded, the graphs with bounded $\mathcal{H}$-width have bounded treewidth. Hence, to obtain new FPT algorithms the treewdith of the graphs of the class $\mathcal{H}$ should not be bounded. On the other hand, the class $\mathcal{H}$ has to be quite restricted, as otherwise each graph will have bounded $\mathcal{H}$-width. For example, if $\mathcal{H}$ contains the $n \times n$-grid, every $n$-vertex graph was width 1 in the class, as we can see as follows. Consider the $n \times n$-grid $H$ and let $v_{i, j}$ for $1 \leq i, j \leq n$ be such that $v_{i-1, j} v_{i, j} \in E(H)$ for $2 \leq i \leq n$ and $v_{i, j-1} v_{i, j} \in E(H)$ for $2 \leq j \leq n$. We claim that $\left(H,(\{i, j\})_{v_{i, j} \in V(H)}\right)$ is a $H$-decomposition of every graph with vertex set $\{1, \ldots, n\}$. Coverage is easy to see as for each $1 \leq i, j \leq n$, we constructed a bag containing $i$ and $j$ and hence the complete graph over $\{1, \ldots, n\}$ is covered. For the coherence, notice that a vertex $k$ is contained in the bags $X_{k, j}$ for $1 \leq j \leq n$ and $X_{i, k}$ for $1 \leq i \leq n$,

[^12]which build a cross in the grid $H$ and hence these bags are connected.
This construction can be generalized to graphs having the $n \times n$-grid as a minor by making the bag of a vertex contracted with $v_{i, j}$ equal to the bag $X_{v_{i, j}}$ and making all bags of vertices that are removed empty. Hence, all graphs have planar-width at most one. This motivates the following fascinating open problem.

Open Problem 6. Does there exists an adhesive category C such that there is a class $\chi$ of objects in C and a graph class $\mathcal{G}$ of bounded feedback vertex number such that the following two conditions hold simultaneously?

- The class $\chi$ has unbounded tree-shaped structured decomposition width and
- the class $\chi$ has bounded $\mathcal{G}$-shaped structured decomposition width.


## 7. Discussion

Our main contribution is to bridge the "structure" and "power" communities by proving an algorithmic meta-theorem (Theorem 1.1) which informally states that decision problems encoded as sheaves (Representational Compositionality) can be solved by dynamic programming (Algorithmic Compositionality) in linear time on classes of inputs which admit structured decompositions of bounded width and whose decomposition shape has bounded feedback vertex number (Structural Compositionality). Our results thus bridge the mathematical and linguistic differences of these two communities - of "structure" and "power" - by showing how to use category theory and sheaf theory to amalgamate three kinds of compositionality found in mathematics and theoretical computer science. This is summarized at a very high level via the following diagram (i.e. Diagram 1 which was formalized as Diagram 6).
![](https://cdn.mathpix.com/cropped/7725892f-4f60-46c2-b17c-44b82aa218e0-33.jpg?height=287&width=1524&top_left_y=1684&top_left_x=235)

Future work. Other than Open Problem 6, directions for further work abound. Here we mention but a few obvious, yet exciting candidates. First of all it is clear that, although our meta-theoretic results achieve a remarkable degree of horizontal generality (in terms of the kinds of mathematical structures to which they apply), their vertical generality (the breadth of problems which can be solved) is still surpassed by more traditional results such as Courcelle's theorem [23]. It is a fascinating direction for further work to understand the connection between these model-theoretic approaches and our category- and sheaf-theoretic ones. Furthermore, we provide the following two more concrete lines of future work.

1. Studying the connections between other kinds of topologies (such as those generated by more permissive containment relations such as graph minors) and the topologies given by structured decompositions.
2. For other problems - such as vertex cover or Hamilton Path - we need more tools since, although they can be presented as presheaves, they fail to be sheaves. Indeed, note that this failure of compositionality "on the nose" is not specific to our approach and it exists in algorithmics as well: when solving Hamilton path by dynamic programming on a tree decomposition, one does not map the bags of the decomposition to local Hamilton Paths, but instead to disjoint collections of paths (see Flum and Grohe [24] for details). The seasoned algorithmicist will point out that there is a template which can be often followed in order to choose the correct partial solutions: consider a global solution, induce it locally on the bags and then use this information to determine the obstructions to algorithmic compositionality. From our perspective this looks a lot like asking: "what are the obstructions to the problem being a sheaf and how can we systematically track that information?" Fortunately there are many powerful and welldeveloped tools from sheaf cohomology which appear to be appropriate for this task. This is an exciting new direction for research which we are already actively exploring.

## References

[1] Abramsky S, Shah N. Relating structure and power: Comonadic semantics for computational resources. Journal of Logic and Computation, 2021. 31(6):1390-1428. URL https://doi.org/10.1093/logcom/ exab048.
[2] Diestel R. Graph Decompositions: a study in infinite graph theory. Oxford University Press, 1990.
[3] Diestel R. Graph theory. Springer, 2010. ISBN:9783642142789.
[4] Robertson N, Seymour PD. Graph minors. II. Algorithmic aspects of tree-width. Journal of Algorithms, 1986. 7(3):309-322. doi:10.1016/0196-6774(86)90023-4.
[5] Robertson N, Seymour PD. Graph minors X. Obstructions to tree-decomposition. Journal of Combinatorial Theory, Series B, 1991. 52(2):153-190. doi:https://doi.org/10.1016/0095-8956(91)90061-N.
[6] Bertelè U, Brioschi F. Nonserial dynamic programming. Academic Press, Inc., 1972. doi:https://doi.org/ 10.1016/s0076-5392(08)x6010-2. ISBN:9780124109827.
[7] Halin R. S-functions for graphs. Journal of Geometry, 1976. 8(1-2):171-186. doi:10.1007/BF01917434.
[8] i Oum S. Graphs of Bounded Rank-width. Ph.D. thesis, Princeton University, 2005. URL https: //mathsci.kaist.ac.kr/~sangil/pdf/thesis.pdf.
[9] Geelen J, j Kwon O, McCarty R, Wollan P. The Grid Theorem for vertex-minors. Journal of Combinatorial Theory, Series B, 2020. URL https://doi.org/10.1016/j.jctb.2020.08.004.
[10] Robertson N, Seymour P. Graph Minors. XX. Wagner's conjecture. Journal of Combinatorial Theory, Series B, 2004. 92(2):325-357. doi:https://doi.org/10.1016/j.jctb.2004.08.001.
[11] Wollan P. The structure of graphs not admitting a fixed immersion. Journal of Combinatorial Theory, Series B, 2015. 110:47-66. URL https://doi.org/10.1016/j.jctb.2014.07.003.
[12] Johnson T, Robertson N, Seymour PD, Thomas R. Directed tree-width. Journal of combinatorial theory. Series B, 2001. 82(1):138-154. URL https://doi.org/10.1006/jctb.2000.2031.
[13] Berwanger D, Dawar A, Hunter P, Kreutzer S, Obdržálek J. The DAG-width of directed graphs. Journal of Combinatorial Theory, Series B, 2012. 102(4):900-923. doi:https://doi.org/10.1016/j.jctb.2012.04.004.
[14] Hunter P, Kreutzer S. Digraph Measures: Kelly Decompositions, Games, and Orderings. Theoretical Computer Science (TCS), 2008. 399. doi:https://doi.org/10.1016/j.tcs.2008.02.038.
[15] Safari MA. D-width: A more natural measure for directed tree width. In: International Symposium on Mathematical Foundations of Computer Science. Springer, 2005 pp. 745-756. doi:https://doi.org/10.1007/ 11549345_64.
[16] Kreutzer S, Kwon Oj. Digraphs of Bounded Width. In: Classes of Directed Graphs, pp. 405-466. Springer, 2018. doi:https://doi.org/10.1007/978-3-319-71840-8_9.
[17] Bumpus BM, Meeks K, Pettersson W. Directed branch-width: A directed analogue of tree-width. arXiv preprint arXiv:2009.08903, 2020. URL https://doi.org/10.48550/arXiv.2009.08903.
[18] Carmesin J. Local 2-separators. Journal of Combinatorial Theory, Series B, 2022. 156:101-144. doi: https://doi.org/10.1016/j.jctb.2022.04.005.
[19] Dujmović V, Morin P, Wood DR. Layered separators in minor-closed graph classes with applications. Journal of Combinatorial Theory, Series B, 2017. 127:111-147. URL https://doi.org/10.1016/j. jctb.2017.05.006.
[20] Shahrokhi F. New representation results for planar graphs. arXiv preprint arXiv:1502.06175, 2015. URL https://doi.org/10.48550/arXiv.1502.06175.
[21] Jansen BMP, de Kroon JJH, Włodarczyk M. Vertex Deletion Parameterized by Elimination Distance and Even Less. In: Proceedings of the 53rd Annual ACM SIGACT Symposium on Theory of Computing, STOC 2021. Association for Computing Machinery, New York, NY, USA. ISBN 9781450380539, 2021 p. 1757-1769. doi:10.1145/3406325.3451068. URL https://doi.org/10.1145/3406325.3451068.
[22] Grohe M. Descriptive Complexity, Canonisation, and Definable Graph Structure Theory, Cambridge University Press, Cambridge, 2017, x + 544 pp. The Bulletin of Symbolic Logic, 2017. 23(4):493-494. ISBN:1079-8986.
[23] Courcelle B, Engelfriet J. Graph structure and monadic second-order logic: a language-theoretic approach, volume 138. Cambridge University Press, 2012. doi:https://doi.org/10.1017/CBO9780511977619.
[24] Flum J, Grohe M. Parameterized Complexity Theory. 2006. Texts Theoret. Comput. Sci. EATCS Ser, 2006. doi:https://doi.org/10.1007/3-540-29953-X. ISBN:978-3-540-29952-3.
[25] Cygan M, Fomin FV, Kowalik Ł, Lokshtanov D, Marx D, Pilipczuk M, Pilipczuk M, Saurabh S. Parameterized algorithms. Springer, 2015. doi:https://doi.org/10.1007/978-3-319-21275-3. ISBN:978-3-319-21275-3.
[26] Downey RG, Fellows MR. Fundamentals of parameterized complexity, volume 4. Springer, 2013. URL https://doi.org/10.1007/978-1-4471-5559-1.
[27] Leray J. Lanneau dhomologie dune reprsentation. CR Acad. Sci. Paris, 1946. 222:13661368.
[28] Gray JW. Fragments of the history of sheaf theory. In: Applications of Sheaves: Proceedings of the Research Symposium on Applications of Sheaf Theory to Logic, Algebra, and Analysis, Durham, July 9-21, 1977. Springer, 1966 pp. 1-79. URL https://doi.org/10.1007/BFb0061812.
[29] Rosiak D. Sheaf Theory through Examples. The MIT Press, 2022. ISBN 9780262370424. URL 10. 7551/mitpress/12581.001.0001.
[30] MacLane S, Moerdijk I. Sheaves in geometry and logic: A first introduction to topos theory. Springer Science \& Business Media, 2012. URL https://doi.org/10.1007/978-1-4612-0927-0.
[31] Oum Si, Seymour PD. Approximating clique-width and branch-width. Journal of Combinatorial Theory, Series B, 2006. 96(4):514-528. doi:https://doi.org/10.1016/j.jctb.2005.10.006.
[32] Bumpus BM, Meeks K. Edge exploration of temporal graphs. Algorithmica, 2022. pp. 1-29. URL https://doi.org/10.1007/s00453-022-01018-7.
[33] Libkind S, Baas A, Patterson E, Fairbanks J. Operadic modeling of dynamical systems: mathematics and computation. arXiv preprint arXiv:2105.12282, 2021. URL https://doi.org/10.48550/arXiv. 2105.12282.
[34] Bumpus BM, Kocsis ZA, Master JE. Structured Decompositions: Structural and Algorithmic Compositionality. arXiv preprint arXiv:2207.06091, 2022. URL https://doi.org/10.48550/arXiv. 2207. 06091.
[35] Patterson E, Lynch O, Fairbanks J. Categorical data structures for technical computing. arXiv preprint arXiv:2106.04703, 2021.
[36] Lack S, Sobocinski P. Adhesive Categories. In: Walukiewicz I (ed.), Foundations of Software Science and Computation Structures. Springer Berlin Heidelberg, Berlin, Heidelberg. ISBN 978-3-540-24727-2, 2004 pp. 273-288. doi:https://doi.org/10.1007/978-3-540-24727-2_20.
[37] AlgebraicJulia/StructuredDecompositions.jl. Accessed: 2023-02-10, URL https://github.com/ AlgebraicJulia/StructuredDecompositions.jl.
[38] Patterson E, other contributors. AlgebraicJulia/Catlab.jl: v0.10.0. doi:10.5281/zenodo.4394460. URL https://zenodo.org/record/4394460.
[39] Bodlaender HL, Fomin FV. Tree decompositions with small cost. In: Algorithm Theory-SWAT 2002: 8th Scandinavian Workshop on Algorithm Theory Turku, Finland, July 3-5, 2002 Proceedings 8. Springer, 2002 pp. 378-387.
[40] Riehl E. Category theory in context. Courier Dover Publications, 2017. ISBN:048680903X.
[41] Adhesive Categories. https://ncatlab.org/nlab/show/adhesive+category. Accessed: 2023-0602.
[42] Duarte GL, de Oliveira Oliveira M, Souza US. Co-Degeneracy and Co-Treewidth: Using the Complement to Solve Dense Instances. In: Bonchi F, Puglisi SJ (eds.), 46th International Symposium on Mathematical Foundations of Computer Science, MFCS 2021, August 23-27, 2021, Tallinn, Estonia, volume 202 of LIPIcs. Schloss Dagstuhl - Leibniz-Zentrum für Informatik, 2021 pp. 42:1-42:17. URL https://doi. org/10.4230/LIPICS.MFCS.2021.42.

## A. Notions from Sheaf Theory

Here we collect basic sheaf-theoretic definitions which we use throughout the document. We refer the reader to Rosiak's textbook [29] for an introduction to sheaf theory which is suitable for beginners.

Definition A.1. Let C be a category with pullbacks and let $K$ be a function assigning to each object $c$ in C a family of sets of morphisms with codomain $c$ called a family of covering sets. We call $K$ a a Grothendieck pre-topology on C if the following three conditions hold for all $c \in C$.
(PT1) If $f: c^{\prime} \rightarrow c$ is an isomorphism, then $\{f\} \in K(c)$.
(PT2) If $S \in K(c)$ and $g: b \rightarrow c$ is a morphism in $C$, then the pullback of $S$ and $g$ is a covering set for $b$; i.e. $\left\{g \times_{c} f \mid f \in S\right\} \in K(b)$.
(PT3) If $\left\{f_{i}: c_{i} \rightarrow c \mid i \in I\right\} \in K(c)$, then, whenever we are given

$$
\left\{g_{i j}: b_{i j} \rightarrow c_{i} \mid j \in J_{i}\right\} \in K\left(c_{i}\right)
$$

for all $i \in I$, we must have

$$
\left\{f_{i} \circ g_{i j}: b_{i j} \rightarrow c_{i} \rightarrow c \mid i \in I, j \in J_{i}\right\} \in K(c)
$$

Definition A.2. A sieve on an object $c \in \mathrm{C}$ is a family $S_{c}$ of morphisms with codomain $c$ which is closed under pre-composition.

Sieves are essentially what happens when we decide to just use those families that are "saturated" (in the sense that they are closed under pre-composition with morphisms in C); they are introduced in order to present the definition of a Grothendieck topology (see A.3), a revision of A.1.

Observe that (at least when C is locally small) sieves can be identified with subfunctors of the representable hom-functor hom $(-, c)=y_{c}$ (note that the category $\mathbf{S e t}^{\mathrm{C}^{o p}}$ of presheaves on C has pullbacks, letting us drop, via this sieve approach, the assumption on C itself). Note also that if $S \subseteq \operatorname{hom}$ (-,$- c$ ) is a sieve on $c$ and $f: b \rightarrow c$ is any morphism to $c$, then the pullback sieve along $f$

$$
f^{*}(S)=\{g \mid \operatorname{cod}(g)=b, f \circ g \in S\}
$$

is a sieve on $b$.
Typically, the definition of a Grothendieck topology is then given in terms of a function $J$ assigning sieves to the objects of C such that three axioms (maximal sieve, stability under base change, and transitivity) are satisfied. But really the stability axiom - requiring that if $S \in J(c)$, then $f^{*}(S) \in J(b)$ for any arrow $f: b \rightarrow c$-just amounts to requiring that $J$ is in fact a functor $J: C^{o p} \rightarrow$ Set, i.e., an object in the presheaf category Set $^{\text {Cop }^{o p}}$. If we let Sieve : C $^{o p} \rightarrow$ Set be the functor which takes objects $c$ of a small category C to the set of all sieves on $c$, and for any morphism $f: x \rightarrow y$ in C use the map

$$
f^{*}:(S \in \operatorname{Sieve}(y)) \mapsto(\{g: w \rightarrow x \mid(f g: w \rightarrow x \rightarrow y) \in S\} \in \operatorname{Sieve}(x)),
$$

then we can give a somewhat condensed definition of a Grothendieck topology (by already building the usual stability axiom into the characterization of $J$ as a particular functor), as follows.

Definition A.3. Let C be a category and consider a subfunctor $J$ of Sieve : $\mathrm{C}^{o p} \rightarrow$ Set of "permissible sieves". We call $J$ a Grothendieck topology on $C$ if it satisfies the following two conditions:
(Gt1) the maximal sieve is always permissible; i.e. $\{f \in \operatorname{Mor}(\mathrm{C}) \mid \operatorname{cod}(f)=c\} \in J(c)$ for all $c \in \mathrm{C}$
(Gt2) for any sieve $R$ on some object $c \in \mathrm{C}$, if there is a permissible sieve $S \in J(c)$ on $c$ such that for all $(h: b \rightarrow c) \in S$ the sieve $h^{*}(R)$ is permissible on $b$ (i.e. $h^{*}(R) \in J(b)$ ), then $R$ is itself permissible on $c$ (i.e. $R \in J(c)$ ).

For any $c \in \mathrm{C}$ we call the elements $S \in J(c) J$-covers or simply covers, if $J$ is understood from context. A site is a pair ( $\mathrm{C}, J)$ consisting of a category C and a Grothendieck topology on C .

Definition A.4. Let $(\mathrm{C}, J)$ be a site, $S$ be a $J$-cover of an object $c \in \mathrm{C}$ and $P: C^{o p} \rightarrow$ Set be a presheaf. Then a matching family of sections of $P$ with respect to the cover $S$ is a morphism (natural transformation) of presheaves $\chi: S \Rightarrow P$.

Definition A.5. Let $P: C^{o p} \rightarrow$ Set be a presheaf on a site $(C, J)$. Then we call $P$ a sheaf with respect to $J$ (or a $J$-sheaf) if for all $c \in \mathrm{C}$ and for all covering sieves $\left(\imath: S \Rightarrow y_{c}\right) \in J(c)$ of $c$ each matching family $\chi: S \Rightarrow P$ has a unique extension to the morphism $\mathcal{E}: y_{c} \Rightarrow P$.


[^0]:    Address for correspondence: Computer \& Information Science \& Engineering, University of Florida, 432 Newell Drive, Gainesville, FL 32603, USA.
    *DARPA ASKEM and Young Faculty Award programs through grants HR00112220038 and W911NF2110323
    ${ }^{\dagger}$ DARPA ASKEM and Young Faculty Award programs through grants HR00112220038 and W911NF2110323

[^1]:    ${ }^{1}$ We choose the term "representational" as a nod to Leray's [27] 1946 understanding of what sheaf theory should be: "Nous nous proposons d'indiquer sommairement comment les méthodes par lesquelles nous avons etudié la topologie d'un espace

[^2]:    peuvent être adaptées à l'étude de la topologie d'une représentation" (in English: "We propose to indicate briefly how the methods by which we have studied the topology of a space can be adapted to the study of the topology of a representation"). As Gray [28] points out, this is "the first place in which the word 'faisceau' is used with anything like its current mathematical meaning".

[^3]:    ${ }^{2}$ (linear in the number of component pieces of the decomposition)

[^4]:    ${ }^{3}$ The functor arises via the monad given by the colim $\dashv$ const adjunction of diagrams
    ${ }^{4}$ Here, given a fixed graph $H$, one is asked to determine whether a given graph $G$ admits a reflexive homomorphism onto $H$ (where a reflexive homomorphism is a vertex map $f: V G \rightarrow V H$ such that, for all vertex pairs $(x, y)$ in $G$, if $f(x) f(y) \in E H$, then $x y \in E G$.

[^5]:    ${ }^{5}$ For the reader concerned with size issues, observe that: (1) given categories C and D , the functor category $[C, D]$ is small whenever C and D also are; and (2) since we are concerned with diagrams whose domains have finitely many objects and morphisms, one has that the collection of diagrams which yield a given object as a colimit is indeed a set.

[^6]:    ${ }^{6}$ In order to maintain notational consistency with the prequel [34] and in order to remind the reader that we are only working throughout with monic structured decompositions, we will keep the subscript $m$ in the notation of the category $\mathfrak{D}_{\mathrm{m}} \mathrm{C}$.

[^7]:    ${ }^{7}$ Here we write $\mathbf{y}_{U}$ to denote the Yoneda embedding at $U$.

[^8]:    ${ }^{8}$ A feedback vertex set in a graph $G$ is a vertex subset $S \subseteq V(G)$ of $G$ whose removal from $G$ yields an acyclic graph. The feedback vertex number of a graph $G$ is the minimum size of a feedback vertex set in $G$.
    ${ }^{9}$ Note that the colimit functor colim : $\mathfrak{D}_{\mathrm{m}}$ FinSet ${ }^{o p} \rightarrow$ FinSet $^{o p}$ - which is in red in Diagram 3 - is a limit of sets; we invite the reader to keep this in mind throughout.

[^9]:    ${ }^{10}$ Recall that the Grothendieck construction produces from any functor $F: \mathrm{A} \rightarrow \mathrm{B}$ a category denoted $\int F$. For details on the construction and its properties, we refer the reader to Riehl's textbook [40]

[^10]:    ${ }^{11}$ Once again we remind the reader that taking the colimit in FinSet ${ }^{o p}$ of a FinSet ${ }^{o p}$-valued decomposition $d: \int G \rightarrow$ FinSet ${ }^{o p}$ will yield the same result as first viewing $d$ as a FinSet-valued co-decomposition $d:\left(\int G\right)^{o p} \rightarrow$ FinSet and evaluating its limit in FinSet.

[^11]:    ${ }^{12}$ Dually to the notation used for restrictions, for any function $f: A \rightarrow B$, we denote the corestriction of $f$ to its image as $\left.f\right|^{\operatorname{lm} f}$.

[^12]:    ${ }^{13}$ We refer the reader to Bumpus, Kocis and Master [34] for details of how to choose a graph-theoretic instantiation of our categorical notation which neatly corresponds to that of Carmesin's notation of graph decompositions [18].

