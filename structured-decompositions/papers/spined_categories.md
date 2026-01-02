# Spined categories: generalizing tree-width beyond graphs 

Benjamin Merlin Bumpus * \& Zoltan A. Kocsis ${ }^{\dagger}$

Wednesday $22^{\text {nd }}$ June, 2022


#### Abstract

Tree-width is an invaluable tool for computational problems on graphs. But often one would like to compute on other kinds of objects (e.g. decorated graphs or even algebraic structures) where there is no known tree-width analogue. Here we define an abstract analogue of tree-width which provides a uniform definition of various tree-width-like invariants including graph tree-width, hypergraph treewidth, complemented tree-width and even new constructions such as the tree-width of modular quotients. We obtain this generalization by developing a general theory of categories that admit abstract analogues of both tree decompositions and tree-width; we call these pseudo-chordal completions and the triangulation functor respectively.


## 1 Introduction

Divide and conquer algorithms are nearly ubiquitous in computer science. Indeed, already in the 1980s, Johnson [19] compiled a list of graph classes satisfying the following properties:

- their members admit recursive decompositions into smaller and simpler pieces,
- many NP-hard problems can be solved in polynomial time by using these structural decompositions as data structures for dynamic programming.

Some examples from Johnson's list are: trees, partial $k$-trees, chordal graphs, series parallel graphs, split graphs and co-graphs.

Today we are equipped with a vast literature on how to go about decomposing graphs into smaller parts and how to exploit these decompositions for algorithmic purposes. Indeed, many important graph classes which admit powerful algorithmic meta-theorems

[^0]are described by measuring the width of smallest 'structural decompositions' of their members (e.g. classes of bounded tree-width or clique-width).

Due to a plethora of algorithmic and theoretical applications, significant amounts of research effort are spent on introducing and studying new sorts of decompositions (along with corresponding width measures) that capture specific classes of objects and/or structural correspondences. These include e.g. modular decompositions [15], partitive families [8, 11], clique-width decomposition trees [10, 9], branch decompositions [29] and rank decompositions [26].

Featuring most prominently among these graph parameters is indubitably tree-width: it has played a key part in the proof of the celebrated Robertson-Seymour graph minor theorem [27] and it is a powerful hammer in the parameterized complexity toolbox [14, 12].

This paper is motivated by the long-term ambition of extending the aforementioned decomposition methods to other kinds of mathematical structures. The specific question which we address is that of finding a uniform and abstract definition of both tree decompositions and tree-width which can then be applied to structures other than finite simple graphs. Our answer to this problem requires a change in perspective: we shift from a graph-theoretic point of view to one which is category-theoretic. This approach leads us to obtain a vast generalization of tree-width - called the triangulation functor - which is defined for all objects of special kinds of categories which we call spined categories (we delay a detailed overview our our contributions to end of this section).

The question of generalizing notions such as tree-width to new settings is as natural as it is challenging. Indeed it is often the case that in practice one needs to compute not on graphs, but on other kinds of objects (such as decorated graphs or perhaps algebraic structures). Unfortunately, we so far do not have a wealth of decomposition methods for such objects and neither do we have structured, formulaic ways of finding such generalizations.

The difficulty of generalization to which we refer already rears its head when one tries to lift the definition of tree-width from graphs to directed graphs. Indeed, this has been a challenging (and ongoing) research question that has captivated the research community since the 1990s [22] and which has led to the definition of a myriad of subtly different directed analogues of tree-width [20, 4, 17, 30, 22].

When one is interested in obtaining tree-width analogues even further afield from the familiar settings of graphs and directed graphs, further challenges arise due to the fact that most of the aforementioned decomposition methods are defined explicitly in terms of the internal structure of the decomposed object (think, for example of the definition of tree-width or of clique-width decomposition trees, which use a formal grammar to specify how to construct a given graph from smaller ones). This makes it arduous to generalize a given notion of decomposition to different classes of objects especially if we wish to place as few restrictions as possible on such classes (for example, it could be that the objects we wish to decompose might not even come equipped with obvious analogues of the notions of 'vertex' or 'edge' or 'connectivity' which, of course, tend to feature prominently in graph-theoretic definitions).

One of the points that we make in this paper is that some of the difficulties of transfer-
ring a given decomposition notion to a more general setting can sidestepped by finding a characteristic property which: (1) defines the decomposition of an object $X$ independently of the internal structure of $X$ and (2) which is formulated purely in terms of the category inhabited by the objects we wish to decompose. Such category-theoretic characterizations have already proven successful in other fields (see e.g. Leister's work on categorial characterizations of ultraproducts [24] and more recently Lebesgue integration [25]).

Contributions. We introduce Spined categories. These are categories $\mathcal{C}$ equipped with sufficient additional structure to admit both

1. an abstract analogue of tree decompositions (which we call pseudo-chordal completions) and
2. a categorial generalization of tree-width (we call this the triangulation functor) exhibited as as a special kind of functor (which we call $S$-functors) from $\mathcal{C}$ to the poset of natural numbers.

When instantiated in the category of graphs and subgraphs, our construction agrees with the graph-thereotic one: denoting by $\Delta_{\mathbf{G r}}$ the triangulation functor (i.e. our abstract analogue of tree-width) in the category of graphs, we have $\Delta_{\mathbf{G r}}(G)=\mathbf{t w}(G)+1$ for any graph $G$ (furthermore, this statement holds true even when we replace 'graph' by 'hypergraph' throughout).

The list of examples of spined categories is not restricted to just these familiar cases; other examples include categories having as objects: natural numbers, posets and even vertex-labeling functions.

Our abstract analogue of tree-width is defined via the notion of an $S$-functor. This constitutes a vast generalization of Halin's S-functions [16] (which are graph invariants of the form ( $G \in$ Graphs) $\mapsto(n \in \mathbb{N})$ which share several properties with the Hadwiger number, modified chromatic number ${ }^{1}$ and the modified connectivity number ${ }^{2)}$ ). Indeed our main theorem (Theorem 4.10) can also be seen as a generalization of Halin's definition of tree-width as the maximal S-function out of the (point-wise ordered) poset of all S-functions.

Our construction of triangulation functors is uniform on all spined categories and thus allows one to define new tree-width-like parameters (such as widths for new types of combinatorial objects, or notions of graph width that respect stricter notions of structural correspondence than ordinary graph isomorphism) simply by collecting the relevant objects into a spined category.

Outline. To accommodate readers from different backgrounds, Section 2 consists of short review of the graph- and category-theoretic background required for this paper. In Section 3 we introduce spined categories (Definition 3.1) and the corresponding notion of morphisms, spinal functors (Definition 3.5). Section 4 contains the proof of our main result (Theorem 4.10) on the existence of spinal functors called triangulation

[^1]functors which generalize tree-width-like invariants used in combinatorics. In Section we describe a way of constructing new spined categories from previously known ones and illustrate the applications of such constructions with some examples. Section 7 briefly discusses open questions and directions for future research.

Acknowledgements: we would like to thank Steven Noble and Gramoz Goranci for their detailed feedback on the preliminary version of this article; furthermore we extend our thanks to Karl Heuer, Kitty Meeks, Ambroise Lafont, Johannes Carmesin and Bart Jansen for their comments, suggestions and discussions which helped in consolidating and maturing the ideas in this paper as well as improving their exposition.

## 2 Background

For any graph-theoretic notation not defined here, we refer the reader to Diestel's textbook [13] while, for category-theoretic terminology not mentioned here, we refer to Awodey's textbook [2]. For a more gentle introduction to the background and most (but not all) of the results of this paper, we direct the reader to thesis by Bumpus [6]. Finally we note that an extended abstract on this topic appeared at the Applied Category Theory conference ACT2021 [7].

The class $\mathcal{G}$ consists of all finite graphs that have no loops or parallel edges. By "graph" we always mean an element of $\mathcal{G}$ (note that this clashes with the common convention in category theory, which takes graphs to be reflexive). Throughout, for any natural number $n$, let $[n]$ denote the set $\{1, \ldots, n\}$. We write $K_{n}$ (resp. $\overline{K_{n}}$ ) for the complete graph (resp. discrete graph) on the set $[n]$. We denote the disjoint union of two sets $A$ and $B$ by $A \uplus B$. For graphs $G$ and $H$, we denote by $G \uplus H$ and $G \cap H$ respectively the graphs $(V(G) \uplus V(H), E(G), \uplus E(H))$ and $(V(G) \cap V(H), E(G) \cap E(H))$. We call a vertex $v$ of a graph $G$ an apex if it is adjacent to every other vertex in $G$. We denote by $G \star v$ the operation of adjoining a new apex vertex $v$ to $G$.

A circuit of length $n$ in the simple graph $G$ is a finite sequence ( $e_{1}, \ldots, e_{n}$ ) of edges of $G$ such that consecutive edges share an endpoint, as do $e_{1}$ and $e_{n}$. A simple graph that contains no circuits is called a tree.

A graph homomorphism from a graph $G$ to a graph $H$ is a function $h: V(G) \rightarrow V(H)$ such that $h(x) h(y) \in E(H)$ whenever $x y \in E(G)$. Note that, if $G$ is a subgraph of $H$, then there is an injective graph homomorphism $\phi: G \rightarrow H$ which witnesses this fact.

### 2.1 Tree-width

Intuitively, the tree-width function, tw : $\mathcal{G} \rightarrow \mathbb{N}$ measures how far a given graph is from being a tree. For example, edge-less graphs have tree-width 0 , forests with at least one edge have tree-width 1 and, for $n>1, n$-vertex cliques have tree-width $n-1$. Treewidth was introduced independently by many authors [3, 16, 28] and thus has many equivalent definitions; the most common definition makes use of the related concept of a tree-decomposition. Here we give its definition for hypergraphs [1].

Definition 2.1. [1] The pair $\left(T,\left(\boldsymbol{B}_{t}\right)_{t \in V(T)}\right)$ is a tree decomposition of a hypergraph $H$ if $\left(\boldsymbol{B}_{t}\right)_{t \in V(T)}$ ) is a sequence of subsets (called bags) of $V(H)$ indexed by the nodes of the tree $T$ such that:
( T1) for every hyper-edge $F$ of $H$, there is a node $t \in V(T)$ such that $F \subseteq B_{t}$,
(T2) for every $x \in V(H)$, the set $V_{(T, x)}:=\left\{t \in V(T): x \in B_{t}\right\}$ induces a connected subgraph in $T$ (in particular $V_{(T, x)}$ is not empty).

The width of a tree decomposition $\left(T,\left(V_{t}\right)_{t \in T}\right)$ of the hypergraph $H$ is defined as one less than the maximum of the cardinalities of its bags. The tree-width $\mathbf{t w}(H)$ of $H$ is the minimum possible width of any tree decomposition of $H$. (The definition of tree decomposition and tree-width follow for simple graphs by viewing them as 2 -uniform hypergraphs.)

Halin [16] provides an alternative characterization of tree-width as a maximal element in a class of functions called $S$-functions. These are mappings from finite graphs to $\mathbb{N}$ satisfying a set of common properties fulfilled by the chromatic number, vertexconnectivity number and the Hadwiger number. In order to define S-functions, we first recall the concept of an $H$-sum of two graphs.

Definition 2.2. Given two graphs $G_{1}$ and $G_{2}$ and a subgraph $H$ of both of them, the $H$-sum of $G_{1}$ and $G_{2}$ is the graph $G_{1} \#_{H} G_{2}$ obtained by identifying the vertices of $H$ in $G_{1}$ to the vertices of $H$ in $G_{2}$ and removing any parallel edges. Formally, given injective homorphisms $h_{i}: H \rightarrow G_{i}$ witnessing that $H$ is a subgraph in $G_{1}$ and $G_{2}$, the graph $G_{1} \#_{H} G_{2}$ is defined as

$$
G_{1} \#_{H} G_{2}:=\left(V\left(G_{1}\right) \uplus V\left(G_{2}\right) /{ }_{h_{1}=h_{2}}, E\left(G_{1}\right) \uplus E\left(G_{2}\right) / \sim\right)
$$

where edges $w x$ and $y z$ are related under $\sim$ if $\left\{h_{1}(w), h_{1}(x)\right\}=\left\{h_{2}(y), h_{2}(z)\right\}$.
Given the definition of $H$-sum, we can now recall Halin's definition of S-function.
Definition 2.3 ([16]). A function $f: \mathcal{G} \rightarrow \mathbb{N}$ is called an $S$-function if it satisfies the following four properties:
(H1) $f\left(K_{0}\right)=0\left(K_{0}\right.$ is the empty graph)
(H2) if $H$ is a minor of $G$, then $f(H) \leq f(G)$ (minor isotonicity)
(H3) $f(G \star v)=1+f(G)$ (distributivity over adding an apex)
(H4) for each $n \in \mathbb{N}, G=G_{1}{ }^{\#} K_{n} G_{2}$ implies that $f(G)=\max _{i \in\{1,2\}} f\left(G_{i}\right)$ (distributivity over clique-sum).

Theorem 2.4 ([16]). The set of all $S$-functions forms a complete distributive lattice when equipped with the pointwise ordering. Furthermore, the function $G \mapsto \mathbf{t w}(G)+1$ is maximal in this lattice.

### 2.2 Category-theoretic preliminaries

Our generalization of Halin's characterization of tree-width relies on some standard category-theoretic tools. To keep the presentation self-contained, we recall the definitions of all relevant concepts here.

Throughout we let $\mathbb{N}_{\leq}$denote the ordered set of natural numbers (under the usual ordering $\leq$ ), regarded as a category the obvious way. Similarly, $\mathbb{N}_{=}$denotes the discrete category whose objects are natural numbers. We write $\mathbf{G r}_{\text {homo }}$ for the category having finite simple graphs as objects and graph homomorphisms as arrows.

We call a morphism (or arrow) $f: A \rightarrow B$ in a category $\mathcal{C}$ a monomorphism in $\mathcal{C}$ (or a monic arrow in $\mathcal{C}$ ) if, given any two arrows $x, y: Z \rightarrow A$, we have $f \circ x=f \circ y$ implies $x=y$. Throughout this text the notation $f: A \hookrightarrow B$ always denotes a monomorphism from $A$ to $B$. Given a category $C$, we let $\operatorname{Mono}(C)$ denote the subcategory of $C$ given by all the monic arrows of $\mathcal{C}$ (note that this differs from the standard usage, where Mono( $\mathcal{C}$ ) denotes a specific subcategory of the arrow category $\operatorname{Arr}(C)$ of $\mathcal{C}$ instead).

Definition 2.5. A functor $F$ between the categories $\mathcal{C}$ to $\mathcal{D}$ is a mapping that associates

- to every object $W$ in $\mathcal{C}$ an object $F[W]$ in $\mathcal{D}$
- to every arrow $f: X \rightarrow Y$ in $\mathcal{C}$ an arrow $F[f]: F[X] \rightarrow F[Y]$ in $\mathcal{D}$
while preserving identity and compositions, i.e.
- $F\left(\mathbf{i d}_{X}\right)=\mathbf{i d}_{F[X]}$ for every object $X$ in $\mathcal{C}$, and
- $F[g \circ f]=F[g] \circ F[f]$ for all arrows $f: X \rightarrow Y, g: Y \rightarrow Z$ in $C$.

A diagram of shape $J$ in a category $\mathcal{C}$ is a functor from $J$ to $\mathcal{C}$.
We call a diagram of shape $G \longleftrightarrow g \quad A \longrightarrow h \quad$ in the category $\mathcal{C}$ a span in $\mathcal{C}$; similarly, we call $G \xrightarrow{g} A \longleftrightarrow^{h} H$ a cospan. A monic (co)span is a (co)span consisting of monic arrows.

Definition 2.6. Consider a span $G_{1} \overleftarrow{g_{1}} H \underset{g_{2}}{\longrightarrow} G_{2}$ in a category $C$. The cospan $G_{1} \xrightarrow{g_{1}^{+}} G_{1}+{ }_{H} G_{2} \stackrel{g_{2}^{+}}{\longleftrightarrow} G_{2}$ is a pushout of $g_{1}$ and $g_{2}$ in $\mathcal{C}$ if

1. $g_{1}^{+} \circ g_{1}=g_{2}^{+} \circ g_{2}$, and
2. for any cospan $G_{1} \xrightarrow{z_{1}} Z \stackrel{z_{2}}{\longleftrightarrow} G_{2}$ such that $z_{1} \circ g_{1}=z_{2} \circ g_{2}$ (a cocone of the span) we can find a unique morphism $m: G_{1}{ }^{+}{ }_{H} G_{2} \rightarrow Z$ such that $m \circ g_{1}^{+}=z_{1}$ and $m \circ g_{2}^{+}=z_{2}$.

We call $G_{1}+_{H} G_{2}$ the pushout object of $g_{1}$ and $g_{2}$.
Pushouts in $\mathbf{G r}_{\text {homo }}$ allow us to recover the definition of an $H$-sum of graphs (recall Definition 2.2).

Proposition 2.7. Every monic span in $\mathbf{G r}_{\text {homo }}$ has a pushout. In particular, the pushout of a monic span $G_{1} \underset{g_{1}}{\longleftrightarrow} H \underset{g_{2}}{\hookrightarrow} G_{2}$ is the graph $G_{1} \#_{H} G_{2}$ given by the $H$-sum of $G_{1}$ and $G_{2}$ along $H$.

Proof. Take the obvious inclusion maps as $\iota_{1}: G_{1} \hookrightarrow G_{1} \#_{H} G_{2}$ and $\iota_{2}: G_{2} \hookrightarrow G_{1} \#_{H} G_{2}$. We clearly have $l_{1} \circ g_{1}=l_{2} \circ g_{2}$. Now consider any other cospan $G_{1} \xrightarrow{z_{1}} Z \stackrel{z_{2}}{\longleftrightarrow} G_{2}$ satisfying the equality $z_{1} \circ g_{1}=z_{2} \circ g_{2}$. Define the map $m: G_{1} \#_{H} G_{2} \rightarrow Z$ on the vertices of $G_{1}{ }^{\#}{ }_{H} G_{2}$ via the equation

$$
m(v)= \begin{cases}z_{1}(v) & \text { if } v \in G_{1} \\ z_{2}(v) & \text { otherwise }\end{cases}
$$

Notice that $m$ is well-defined since if $v \in V\left(G_{1}\right) \cap V\left(G_{2}\right)$, then $z_{1}(v)=z_{1}\left(g_{1}(v)\right)= z_{2}\left(g_{2}(v)\right)=z_{2}(v)$.

We check that $m \circ \iota_{1}=z_{1}$. By extensionality, it suffices to prove $m\left(l_{1}(x)\right)=z_{1}(x)$ for an arbitrary vertex $x$ of $G$. Since $l_{1}(x)=x$ and $x \in G$, the first clause of the definition applies, and we have $m\left(l_{1}(x)\right)=m(x)=z_{1}(x)$. A similar proof allows us to conclude $m \circ l_{2}=z_{2}$. The uniqueness of $m$ follows immediately.

We cannot generalize Proposition 2.7 much further, since the pushout of an arbitrary pair ( $i: D \rightarrow G, j: D \rightarrow H$ ) need not exist in $\mathbf{G r}_{\text {homo }}$. Indeed, taking the obvious injection $i: \overline{K_{2}} \rightarrow K_{2}$ and the unique map $j: \bar{K}_{2} \rightarrow K_{1}$, we see that no object $Z$ and map $z_{1}: K_{2} \rightarrow Z$ can ever satisfy $z_{1} \circ i=z_{2} \circ j$, since the image of the right-hand side always consists of a single vertex, while the image of the left-hand side necessarily contains an edge.

## 3 Spined Categories and S-functors

Here we introduce spined categories, categories with sufficient extra structure to admit a categorial generalization of the graph-theoretic notion of tree-width (the triangulation functor, constructed in Section 4 ).

Spined categories come equipped with a notion of proxy pushout, whose role is largely analogous to that of the clique-sum operation in Halin's definition of S-functions (Definition 2.3). Proxy pushouts are similar to, but significantly less restrictive than ordinary pushouts: in fact, pushouts always give rise to proxy pushouts (Proposition (3.2), but the converse does not hold. The role of cliques themselves is played by the members of a distinguished sequence of objects, called the spine.

Among the structure-preserving functors between spined categories, we find abstract, functorial counterparts to Halin's S-functions: these are the $S$-functors of Definition 3.6 We shall see that S-functors are in fact more general than Halin's notion, even in the case of simple graphs. While every S-function yields an S-functor over the category $\mathbf{G r}_{\text {mono }}$ (Proposition 3.7), the converse is not true.

Definition 3.1. A spined category consists of a category $\mathcal{C}$ equipped with the following additional structure:

- a functor $\Omega: \mathbb{N}_{=} \rightarrow \mathcal{C}$ called the spine of $\mathcal{C}$,
- an operation $\mathfrak{P}$ (called the proxy pushout) that assigns to each span of the form

$$
G \stackrel{g}{\longleftrightarrow} \Omega_{n} \xrightarrow{h} H \text { in } \mathcal{C} \text { a distinguished cocone } G \xrightarrow{\mathfrak{P}(g, h)_{g}} \mathfrak{P}(g, h) \stackrel{\mathfrak{P}(g, h)_{h}}{\leftarrow} H
$$

subject to the following conditions:
SC1 For every object $X$ of $\mathcal{C}$ we can find a morphism $x: X \rightarrow \Omega_{n}$ for some $n \in \mathbb{N}$.
SC2 For any cocone $G \stackrel{g}{\longleftrightarrow} \Omega_{n} \xrightarrow{h} H$ and any pair of morphisms $g^{\prime}: G \rightarrow G^{\prime}$ and $h^{\prime}: H \rightarrow H^{\prime}$ we can find a unique morphism $\left(g^{\prime}, h^{\prime}\right): \mathfrak{P}(g, h) \rightarrow \mathfrak{P}\left(g^{\prime} \circ g, h^{\prime} \circ h\right)$ making the following diagram commute:
![](https://cdn.mathpix.com/cropped/a6ceea72-3d46-4a11-8691-56c7ecd0af06-08.jpg?height=330&width=695&top_left_y=979&top_left_x=756)

One could define proxy pullbacks dually to proxy pushouts. As the name suggests, categories with enough pushouts (pullbacks) always have proxy pushouts (proxy pullbacks). This observation gives rise to many examples of spined categories.

Proposition 3.2. Take a category $\mathcal{C}$ equipped with functor $\Omega: \mathbb{N}_{=} \rightarrow \mathcal{C}$ such that the following hold:

1. for any object $X$ of $\mathcal{C}$ there is some $n \in \mathbb{N}$ and morphism $x: X \rightarrow \Omega_{n}$, and
2. every span of the form $G \stackrel{g}{\longleftrightarrow} \Omega_{n} \xrightarrow{h} H$ has a pushout in $C$.

The map $\mathfrak{P}$ that assigns to every span $G \stackrel{g}{\longleftrightarrow} \Omega_{n} \xrightarrow{h} H$ its pushout square turns $\mathcal{C}$ into a spined category.

Proof. We only have to verify Property SC2. Consider the diagram
![](https://cdn.mathpix.com/cropped/a6ceea72-3d46-4a11-8691-56c7ecd0af06-08.jpg?height=343&width=566&top_left_y=1980&top_left_x=773)

We have to exhibit the unique dotted morphism $G+_{\Omega_{n}} H \rightarrow G^{\prime}+_{\Omega_{n}} H^{\prime}$ making this diagram commute. Notice that the arrows $\imath_{G}^{\prime} \circ g^{\prime}$ and $\imath_{H}^{\prime} \circ h^{\prime}$ form a cocone of the span of $g, h$. Since the pushout of $g$ and $h$ is universal among such cocones, the existence and uniqueness of the required morphism $G+_{\Omega_{n}} H \rightarrow G^{\prime}+_{\Omega_{n}} H^{\prime}$ follows. $\square$

Since pushouts in poset categories are given by least upper bounds, Proposition 3.2 allows us to construct a simple (but important) first example of a spined category.

Example 3.3. Let $\leq$ denote the usual ordering on the natural numbers. The poset $\mathbb{N}_{\leq}$, when equipped with the spine $\Omega_{n}=n$ (and maxima as proxy pushouts) constitutes a spined category denoted Nat.

Combining Propositions 2.7 and 3.2 gives us a first example of a "combinatorial" spined category, the category $\mathbf{G r}_{\text {mono }}$ which has graphs as objects and injective graph homomorphisms as arrows. First consider a span of the form $A \longleftrightarrow X \longleftrightarrow B$ in $\mathbf{G r}_{\text {homo }}$. Notice that all arrows are monic in the corresponding pushout square. However, given a cocone $A \xrightarrow[a]{ } Z \longleftarrow b$ the pushout morphism $A+_{X} B \rightarrow Z$ can fail to be a monomorphism (for instance in the case where the images of $a$ and $b$ have non-empty intersection). It follows that the clique sum does not give rise to pushouts in the category $\mathbf{G r}_{\text {mono }}$. Nonetheless, the category satisfies Property SC2, so the lack of pushouts does not stop us from constructing a spined category.

Proposition 3.4. The category $\mathbf{G r}_{\text {mono }}$, equipped with the spine $n \mapsto K_{n}$ and clique sums as proxy pushouts forms a spined category.

Proof. Property SC1 is evident, but we need to verify Property SC2 Consider the diagram
![](https://cdn.mathpix.com/cropped/a6ceea72-3d46-4a11-8691-56c7ecd0af06-09.jpg?height=338&width=532&top_left_y=1542&top_left_x=790)
in $\mathbf{G r}_{\text {homo }}$. Notice that the arrows $\boldsymbol{l}_{G}, \boldsymbol{l}_{G}^{\prime}, \boldsymbol{l}_{H}, \boldsymbol{l}_{H}^{\prime}$ are all monic. We have to establish that the morphism $p: G \#_{\Omega_{n}} H \rightarrow G^{\prime} \#_{\Omega_{n}} H^{\prime}$ (which is unique since it is a pushout arrow in $\mathbf{G r}_{\text {homo }}$ ) is monic as well. Note that $p$ maps any vertex $x$ in $G \#_{\Omega_{n}} H$ to $\left(l_{G}^{\prime} \circ g^{\prime}\right)(x)$ if $x$ is in $G$ and to $\left(l_{H}^{\prime} \circ h^{\prime}\right)(x)$ otherwise. Thus, since $V\left(G^{\prime}\right) \cap V\left(H^{\prime}\right)=V(G) \cap V(H)$, we have that, for any $x$ and $y$ in $V\left(G \#_{\Omega_{n}} H\right)$, if $p(x)=p(y)$ then $x=y$. Thus $p$ is injective (i.e. it is monic and hence it is in $\mathbf{G r}_{\text {mono }}$ ). $\square$

We will encounter further examples of spined categories below, including:

1. the poset of natural numbers under the divisibility relation (Proposition 3.11),
2. the category of posets (Proposition 3.9),
3. the category of hypergraphs (Theorem 5.2),
4. the category of vertex-labelings of graphs (Examples 6.2 and 6.3).

Now we introduce the notion of a spinal functor as the obvious notion of morphism between two spined categories.

Definition 3.5. Consider spined categories ( $\mathcal{C}, \Omega^{\mathcal{C}}, \mathfrak{P}^{\mathcal{C}}$ ) and ( $\mathcal{D}, \Omega^{\mathcal{D}}, \mathfrak{P}^{\mathcal{D}}$ ). We call a functor $F: \mathcal{C} \rightarrow \mathcal{D}$ a spinal functor if it

SF1 preserves the spine, i.e. $F \circ \Omega^{\mathcal{C}}=\Omega^{\mathcal{D}}$, and
SF2 preserves proxy pushouts, i.e. given a proxy pushout square
![](https://cdn.mathpix.com/cropped/a6ceea72-3d46-4a11-8691-56c7ecd0af06-10.jpg?height=209&width=341&top_left_y=1014&top_left_x=934)
in the category $\mathcal{C}$, the image
![](https://cdn.mathpix.com/cropped/a6ceea72-3d46-4a11-8691-56c7ecd0af06-10.jpg?height=210&width=425&top_left_y=1340&top_left_x=895)
forms a proxy pushout square in $\mathcal{D}$. Equivalently, $F\left[\mathfrak{P}^{C}(g, h)\right]=\mathfrak{P}^{D}(F g, F h)$, $F \mathfrak{P}^{C}(g, h)_{g}=\mathfrak{P}^{D}(F g, F h)_{F g}$ and $F \mathfrak{P}^{C}(g, h)_{h}=\mathfrak{P}^{D}(F g, F h)_{F h}$ all hold.

Recall the spined category Nat of Example3.3. Using spinal functors to Nat, we obtain the following categorial counterparts to Halin's S-functions.

Definition 3.6. An $S$-functor over the spined category $\mathcal{C}$ is a spinal functor $F: \mathcal{C} \rightarrow \mathbf{N a t}$.
Proxy pushouts in $\mathbf{G r}_{\text {mono }}$ are given by clique sums over complete graphs, while pushouts in Nat are given by maxima. Consequently, given an S-functor $F: \mathbf{G r}_{\text {mono }} \rightarrow$ Nat, PropertySF2 reduces to the equality $\left.F_{1} G_{K_{n}} H\right]=\max \{F[G], F[H]\}$ (cf. Property (H4) of Halin's S-functions).

Proposition 3.7. Every $S$-function $f: \mathcal{G} \rightarrow \mathbb{N}$ gives rise to an $S$-functor $F$ satisfying $F[X]=f(X)$ for all objects $X$ of $\mathbf{G r}_{\text {mono }}$.

Proof. Take an S-function $f: \mathcal{G} \rightarrow \mathbb{N}$. Take a morphism $f: X \rightarrow Y$ in $\mathcal{C}$. Since $f$ is a graph monomorphism, $X$ is isomorphic to a subgraph of $Y$, and is therefore a (trivial) minor of $Y$. Thus, $f(X) \leq f(Y)$ holds by Property (H2). It follows that the map $F$ defined by the equations $F[X]=f(X)$ and $F f=(F[X] \leq F[Y])$ for each pair
of objects $X, Y$ and each morphism $f: X \rightarrow Y$ constitutes a functor from $\mathbf{G r}_{\text {mono }}$ to the poset category $\mathbb{N}_{\leq}$.

We show that $F$ preserves the spine inductively, by proving $F\left[K_{n}\right]=f\left(K_{n}\right)=n$ for all $n \in \mathbb{N}$ :

- Base case: We have $F\left[K_{0}\right]=0$ by Property (H1).
- Inductive case: Assume that $F\left[K_{n}\right]=f\left(K_{n}\right)=n$. Since $K_{n} \star v=K_{n+1}$, we have $F\left[K_{n+1}\right]=f\left(K_{n+1}\right)=f\left(K_{n} \star v\right)=1+f\left(K_{n}\right)=1+n$ by Property (H3).

The preservation of proxy pushouts follows immediately by Property (H4) Hence $F$ is a spinal functor as we claimed.

We note, however that the converse of Proposition 3.7 does not hold (not even in $\mathbf{G r}_{\text {mono }}$ ). To see this, note that while the clique number is an $S$-functor in $\mathbf{G r}_{\text {mono }}$, it may increase when taking minors. Thus the clique number does not satisfy Property (H2) and hence it is not an $S$-function.

Using the natural indexing on the spine given by the functor $\Omega: \mathbb{N}_{=} \rightarrow \mathcal{C}$, we can associate the following numerical invariants to each object of the spined category $C$.

Definition 3.8. Take a spined category ( $\mathcal{C}, \Omega, \mathfrak{P}$ ) and an object $X \in \mathcal{C}$. We define the order $|X|$ of the object $X$ as the least $n \in \mathbb{N}$ such that $\mathcal{C}$ has a morphism $X \rightarrow \Omega_{n}$. Similarly, we define the generalized clique number $\omega(X)$ as the largest $n \in \mathbb{N}$ for which $\mathcal{C}$ contains a morphism $\Omega_{n} \rightarrow X$ (whenever such $n$ exists).

It's clear that a spined category ( $\mathcal{C}, \Omega_{n}, \mathfrak{P}$ ) where $\left|\Omega_{n}\right|<n$ (resp. $\omega\left(\Omega_{n}\right)>n$ ) does not admit any S -functors since it then would be impossible for any candidate $S$-functor to preserve the spine. In particular there are no S -functors defined on the category $\mathbf{G r}_{\text {homo }}$. However, S-functors may fail to exist even if $\left|\Omega_{n}\right|=n\left(\omega\left(\Omega_{n}\right)=n\right)$. We construct such an example below.

Proposition 3.9. There exist spined categories ( $\mathcal{C}, \Omega, \mathfrak{P}$ ) satisfying $\left|\Omega_{n}\right|=n=\omega\left(\Omega_{n}\right)$ that do not admit any $S$-functors.

Proof. Consider the category Poset $_{\text {mono }}$ which has finite posets as objects and orderpreserving injections as morphisms. Let $\Omega_{n}$ denote set $\{m \in \mathbb{N} \mid m \leq n\}$ under its usual linear ordering, and let $\mathfrak{P}$ assign to each span of the form $G \stackrel{g}{\longleftrightarrow} \Omega_{n} \xrightarrow{h} H$ the pushout $G+_{\Omega_{n}} H$ of the span in Poset $_{\text {homo }}$ (the category of posets is cocomplete [2], so in particular it has all pushouts). We will show that the structure ( $\boldsymbol{P o s e t}_{\text {mono }}, \Omega, \mathfrak{P}$ ) forms a spined category that does not admit any S-functors.

Take any poset $P$ on $n$ elements and note that there is a monomorphism from $P$ to $L_{n}$. This verifies PropertySC1. For PropertySC2 consider the following diagram.
![](https://cdn.mathpix.com/cropped/a6ceea72-3d46-4a11-8691-56c7ecd0af06-12.jpg?height=358&width=586&top_left_y=425&top_left_x=762)

Notice that the arrows $l_{G}, l_{G}^{\prime}, l_{H}, l_{H}^{\prime}$ are all monic. We have to establish that the morphism $p: G+_{\Omega_{n}} H \rightarrow G^{\prime}+_{\Omega_{n}} H^{\prime}$ (which is unique since it is a pushout arrow in Poset $_{\text {homo }}$ ) is monic as well. Notice that $p$ can be defined piece-wise as the map taking any point $x$ in $G+_{\Omega_{n}} H$ to $\left(l_{G}^{\prime} \circ g^{\prime}\right)(x)$ if $x$ is in $G$ and to $\left(l_{H}^{\prime} \circ h^{\prime}\right)(x)$ otherwise. Since $G^{\prime}+_{\Omega_{n}} H^{\prime}$ is obtained by identifying the points in the image of $\Omega_{n}$ under $g^{\prime} \circ g$ with the points in the image of $\Omega_{n}$ under $h^{\prime} \circ h$, we have that, by its definition, $p$ must be injective and hence monic.

Now we show that $\left(\boldsymbol{\operatorname { P o s e t }}_{\text {mono }}, \Omega, \mathfrak{P}\right)$ does not admit any S-functors. Assume for a contradiction that there exists an S-functor $F$ over $\left(\mathbf{P o s e t}_{\text {mono }}, \Omega, \mathfrak{P}\right)$. Consider the linearly ordered posets $\Omega_{3}=\{a \leq b \leq c\}, \Omega_{2}=\{d \leq e\}$, and $\Omega_{1}=\{x\}$. Since any spinal functor preserves the spine, we must have $F\left[\Omega_{3}\right]=3$ and $F\left[\Omega_{2}\right]=2$. Now consider the monomorphisms $f: \Omega_{1} \rightarrow \Omega_{3}$ and $g: \Omega_{1} \rightarrow \Omega_{2}$ given by $f(x)=c$ and $g(x)=d$. The pushout $P$ of $f, g$ is isomorphic to $\Omega_{4}$. Preservation of proxy pushouts immediately yields $4=F\left[\Omega_{4}\right]=F[P]=\max \{2,3\}=3$, a contradiction.

Instead of exhaustively enumerating all possible obstructions to the existence of Sfunctors, we restrict our attention to those spined categories that come equipped with at least one S-functor. We shall see that the existence of a single S-functor already suffices to construct a functorial analogue of tree-width on any such category.

Definition 3.10. We call a spined category measurable if it admits at least one Sfunctor.

Of course Nat is a measurable spined category. The measurability of $\mathbf{G r}_{\text {mono }}$ follows from Proposition 3.7, by noticing that that the clique number is an S-functor. However, this is a very special property enjoyed by $\mathbf{G r}_{\text {homo }}$.

Proposition 3.11. The generalized clique number $\omega$ need not give rise to an $S$-functor over an arbitrary measurable spined category.

Proof. Equip the natural numbers with the divisibility relation, and regard the resulting poset as a category $\mathbb{N}_{d i v}$. Equip $\mathbb{N}_{d i v}$ with the spine

$$
\Omega_{n}=\prod_{p \leq n} p^{n}
$$

where $p$ ranges over the primes. The poset category $\mathbb{N}_{\text {div }}$ has all pushouts, the pushout of objects $n, m$ given by least common multiple of $n$ and $m$. Let $\mathfrak{P}(x \leq n, x \leq m)$ denote the least common multiple $\operatorname{lcm}(n, m)$. We verify each of the spined category properties in turn:

SC1. Take any $n \in \mathbb{N}$. Let $p$ and $k$ denote respectively the largest prime and exponent which appears in the prime factorization of $n$. Then $n$ divides $\Omega_{p^{k}}$.

SC2. Immediate from Proposition 3.2
Consider the map that sends each object $n \in \mathbb{N}_{d i v}$ to the highest exponent that occurs in the prime factorization of $n$ (OEIS A051903 [18]). This is clearly an S-functor on the category ( $\mathbb{N}_{d i v}, \Omega$, lcm ), which is therefore measurable. However, we claim that $\omega$ itself is not an S -functor on this spined category.

To see this, consider the objects 16 and 81 in $\mathbb{N}_{\text {div }}$. Since $\Omega_{2}=2^{2}=4$ and $\Omega_{3}= 2^{3} \cdot 3^{3}=216$, the largest $n$ for which $\Omega_{n}$ divides 16 is $\omega[16]=2$. Similarly, $\omega[81]=1$. However, we have $\omega[16 \cdot 81]=\omega[1296]=\omega\left[\Omega_{4}\right]=4 \neq 2$.

The reader may verify that, unlike the generalized clique number, the order map does give rise to an S-functor over the category $\mathbb{N}_{d i v}$. However this is not true in general.

Proposition 3.12. The order map $X \mapsto|X|$ need not give rise to an $S$-functor over an arbitrary measurable spined category.

Proof. The order map does not constitute an S-functor over the measurable spined category $\mathbf{G r}_{\text {mono }}$. Consider two copies of the graph with two vertices and one edge, glued together along a common vertex. If order was an S-functor, the resulting graph would have only two vertices.

## 4 Tree-width in a measurable spined category

In this section we give an abstract analogue of tree-width in our categorial setting, by proving a theorem in the style of Halin's Theorem 2.4. To do so, we must find a maximum S-functor (under the point-wise order). An obvious candidate is the map taking every object to its order (Definition 3.8). However, as we just saw (Proposition 3.12), the order need not constitute an S-functor for measurable spined categories. Thus, rather than trying to define an S-functor via morphisms from objects to elements of the spine, we will consider morphisms to elements of a distinguished class of objects which we call pseudo-chordal. These objects will be used to define our abstract analogue of treewidth as an $S$-functor on any measurable spined category. We will conclude the section by showing how our abstract characterization of tree-width allows us to recover the familiar notions of graph and hypergraph tree-width.

Definition 4.1. We call an object $X$ of a spined category ( $\mathcal{C}, \Omega, \mathfrak{P}$ ) pseudo-chordal if for every two S-functors $F, G: \mathcal{C} \rightarrow$ Nat we have $F[X]=G[X]$ (if the spined category is not measurable, then every object is pseudo-chordal).

Proposition 4.2. The set $Q$ of all pseudo-chordal objects of a spined category ( $\mathcal{C}, \Omega, \mathfrak{P}$ ) contains all objects of the form $\Omega_{n}$, and is closed under proxy pushouts in the following sense: given two objects $A, B \in Q$ and two arrows $f: \Omega_{n} \rightarrow A$ and $g: \Omega_{n} \rightarrow B$, we always have $\mathfrak{P}(f, g) \in Q$.

Proof. Given two S-functors $F, G$ on $\mathcal{C}$, we always have $F\left[\Omega_{n}\right]=n=G\left[\Omega_{n}\right]$ by Property\$F1. Moreover, by Property\$F2, given $A, B \in Q$ and arrows $f: \Omega_{n} \rightarrow A$ and $g: \Omega_{n} \rightarrow B$, we have $F[\mathfrak{P}(f, g)]=\max \{F[A] . F[B]\}=\max \{G[A] . G[B]\}=G[\mathfrak{P}(f, g)]$.

In light of Proposition 4.2, it is natural to distinguish the smallest set of pseudochordal objects that contains the spine and which is closed under proxy pushouts. We call this set the set of chordal objects. The name is given in analogy to chordal graphs: a resemblance that is best seen in the following recursive definition of chordal objects.

Definition 4.3. We define the set of chordal objects of the category spined category $\mathcal{C}$ inductively, as the smallest set $S$ of objects satisfying the following:

- $\Omega_{n} \in S$ for all $n \in \mathbb{N}$, and
- $\mathfrak{P}(a, b) \in S$ for all objects $A, B \in S$ and arrows $a: \Omega_{n} \rightarrow A$ and $b: \Omega_{n} \rightarrow B$.

Note that the notions of chordality and pseudo-chordality are well-defined even in non-measurable categories (since every object is pseudo-chordal if the category in question is not measurable).

As an immediate consequence of Proposition 4.2 we have the following result.
Corollary 4.4. All chordal objects are pseudo-chordal.
However, note that the converse of Corollary 4.4 does not hold; as we shall see, it fails even in $\mathbf{G r}_{\text {mono }}$.

Proposition 4.5. Pseudo-chordality does not imply chordality.
Proof. We will show that, in the spined category $\mathbf{G r}_{\text {mono }}$, there exists a non-chordal object for which every pair of S-functors agree. To this end, consider, for some $n \in \mathbb{N}$, the element $K_{n}{ }^{\#} K_{1} C_{n}$ obtained by identifying a vertex of an $n$-clique to a vertex of an $n$-cycle. Since $C_{n}$ is a subgraph of $K_{n}$, we have a sequence of injective graph homomorphisms

$$
K_{n} \hookrightarrow K_{n}{ }^{\#} K_{1} C_{n} \hookrightarrow K_{n}{ }^{\#} K_{1} K_{n} .
$$

Thus, for any S-functor $F$, we have

$$
n=F\left[K_{n}\right] \leq F\left[K_{n} \#_{K_{1}} C_{n}\right] \leq F\left[K_{n} \# K_{1} K_{n}\right]=\max \left\{F\left[K_{n}\right], F\left[K_{n}\right]\right\}=n
$$

We will use pseudo-chordal objects to define notion of a pseudo-chordal completion of an object of a spined category. We point out that the name was given in analogy to the operation of a chordal completion of graphs (i.e. the addition of a set $F$ of edges to some graph $G$ such that the resulting graph ( $V(G), E(G) \cup F$ ) is chordal).

Definition 4.6. A pseudo-chordal completion of an object $X$ of a spined category $(\mathcal{C}, \Omega, \mathfrak{P})$ is an arrow $\delta: X \hookrightarrow H$ for some pseudo-chordal object $H$. If the pseudochordal object $H$ is also chordal, then we call $\delta$ a chordal completion.

Note that, for graphs, one can give an alternative definition of the tree-width a graph $G$ as: $\mathbf{t w}(G)=\min \{\omega(H)-1: H$ chordal completion of $G\}$ (where $\omega$ is the clique number) [13]. With this in mind, observe that the following definition of the width of a pseudo-chordal completion furthers the analogy between our construction and the tree-width of graphs.

Definition 4.7. Let $X$ and $F$ be respectively an object and an S -functor in some measurable spined category. The width of a pseudo-chordal completion $\delta: X \hookrightarrow H$ of $X$ is the value $F[H]$.

We point out that, in contrast to the case of graphs, we do not define the width of a pseudo-chordal completion by using the generalized clique number $\omega$. This is because $\omega$ need not be an S-functor in general (by Proposition 3.11). For clarity we note that the choice of S-functor in Definition 4.7 is inconsequential since every two S-functors agree on pseudo-chordal objects (by the definition of pseudo-chordality).

Proposition 4.8. Let ( $\mathcal{C}, \Omega, \mathfrak{P}$ ) be a measurable spined category and denote by $\Delta[X]$ and $\Delta^{c h}[X]$ the minimum possible width of respectively any pseudo-chordal completion of the object $X$ and any chordal completion of $X$. Then $\Delta$ and $\Delta^{c h}$ are functors from $\mathcal{C}$ to $\mathbb{N}_{\leq}$.

Proof. We only prove the claim for $\Delta$ since the argument for $\Delta^{c h}$ is the same. Let $F$ be any S -functor over $(\mathcal{C}, \Omega, \mathfrak{P})$. We need to verify that, for every arrow $f: X \rightarrow Y$ in $\mathcal{C}$, we have $\Delta[X] \leq \Delta[Y]$. To this end take any such arrow $f: X \rightarrow Y$ and two minimum-width pseudo-chordal completions $\delta_{X}: X \rightarrow H_{X}$ and $\delta_{Y}: Y \rightarrow H_{Y}$ of $X$ and $Y$ respectively. Since $\delta_{Y} \circ f$ is also a pseudo-chordal completion of $X$ and by the minimality of the width of $\delta$, we have $\Delta[X]=F\left[H_{X}\right] \leq F\left[H_{Y}\right]=\Delta[Y]$.

Definition 4.9. Let $\Delta$ and $\Delta^{c h}$ be the functors defined in Proposition 4.8 We call $\Delta$ the triangulation functor and $\Delta^{c h}$ the chordal triangulation functor.

Our goal now is to show that the triangulation functor of a measurable spined category is in fact an S-functor. Specifically we prove our main theorem which states that both $\Delta$ and $\Delta^{c h}$ are S-functors in any measurable spined category.

Theorem 4.10. Both the triangulation and chordal-triangulationfunctors are $S$-functors in any measurable spined category.

Proof. Let ( $\mathcal{C}, \Omega, \mathfrak{P}$ ) be any measurable spined category equipped with some S -functor $F$. We will prove the statement only for $\Delta$ since the method of proof for the $\Delta^{c h}$ case is the same.

Consider a pseudo-chordal completion $c: X \rightarrow H$ of a pseudo-chordal object $X$. Then $F[X] \leq F[H]$, and so the identity pseudo-chordal completion of $X$ has smaller width than any other pseudo-chordal completion of $X$. This proves that $\Delta\left[\Omega_{n}\right]=n$ and hence that $\Delta$ satisfies property SC1

For SC2 consider any span $A \stackrel{a}{\square} \Omega_{n} \xrightarrow{b} B$ in $C$. We have to prove that $\Delta[\mathfrak{P}(a, b)]=\max \{\Delta[A], \Delta[B]\}$. Choose a pseudo-chordal completion $\alpha: A \rightarrow H_{A}$ (resp. $\beta: B \rightarrow H_{B}$ ) for which $F\left[H_{A}\right]$ (resp. $F\left[H_{B}\right]$ ) is minimal. Using property SC2,
there is a unique arrow $(\alpha, \beta): \mathfrak{P}(a, b) \rightarrow \mathfrak{P}(\alpha a, \beta b)$ such that the following diagram commutes.
![](https://cdn.mathpix.com/cropped/a6ceea72-3d46-4a11-8691-56c7ecd0af06-16.jpg?height=294&width=523&top_left_y=534&top_left_x=799)

Now take a pseudo-chordal completion $\delta: \mathfrak{P}(a, b) \rightarrow H$ of $\mathfrak{P}(a, b)$ for which the quantity $F[H]$ is minimal. Consider the following diagram.
![](https://cdn.mathpix.com/cropped/a6ceea72-3d46-4a11-8691-56c7ecd0af06-16.jpg?height=416&width=1271&top_left_y=992&top_left_x=472)
![](https://cdn.mathpix.com/cropped/a6ceea72-3d46-4a11-8691-56c7ecd0af06-16.jpg?height=192&width=1378&top_left_y=1465&top_left_x=483)

To show that $\Delta[\mathfrak{P}(a, b)]=\max \{\Delta[A], \Delta[B]\}$, it suffices to deduce the existence of the dotted arrows $\mu_{1}$ and $\mu_{2}$ in the diagram above.

Note that, since $F$ is an S-functor, the bottom square (which is a diagram in Nat) commutes and $\mathfrak{P}(\alpha a, \beta b)=\max \left\{F\left[H_{A}\right], F\left[H_{B}\right]\right\}$. Since $\delta \circ \mathfrak{P}(a, b)_{a}$ constitutes a pseudochordal completion of $A$ and since we chose $H$ so that $F[H]$ is minimal, we have $F\left[H_{A}\right] \leq F[H]$. Similarly we can deduce $F\left[H_{B}\right] \leq F[H]$. Thus we have

$$
F[\mathfrak{P}(\alpha a, \beta b)]=\max \left\{F\left[H_{A}\right], F\left[H_{B}\right]\right\} \leq F[H],
$$

which proves the existence of $\mu_{1}$.
By Proposition 4.2, we know that the set of pseudo-chordal objects is closed under proxy pushouts. Since $H_{A}$ and $H_{B}$ are pseudo-chordal, so is their proxy pushout $\mathfrak{P}(\alpha a, \beta b)$. Hence $(\alpha, \beta): \mathfrak{P}(a, b) \rightarrow \mathfrak{P}(\alpha a, \beta b)$ is a pseudo-chordal completion of $\mathfrak{P}(a, b)$. However, so is $H$. In fact we chose $H$ so that $F[H]$ is minimal (since $F[H]=\Delta[\mathfrak{P}(a, b)]$ ). Thus we have $F[\mathfrak{P}(\alpha a, \beta b)] \geq F[H]$, which proves the existence of $\mu_{2}$. $\square$

Surprisingly, the S-functors $\Delta$ and $\Delta^{c h}$ defined above coincide.

Corollary 4.11. In any measurable spined category we have $\Delta=\Delta^{c h}$.
Proof. Consider any measurable spined category ( $\mathcal{C}, \Omega, \mathfrak{P}$ ) equipped with an S-functor $F$ and let $X$ be an object in $C$. Since every chordal object is also pseudo-chordal (Corollary 4.4) we know that $\Delta[X] \leq \Delta^{c h}[X]$. We now show that given any minimum-width pseudo-chordal completion $\delta: X \rightarrow H$ of $X$, we can find a chordal completion of $X$ of the same width as $\delta$.

Let $\gamma: H \rightarrow \boldsymbol{H}^{c h}$ be a minimum-width chordal completion of $H$. Since $H$ is pseudo-chordal, all S-functors take the same value on $H$. In particular this means that $\Delta[H]=\Delta^{c h}[H]$ since both $\Delta$ and $\Delta^{c h}$ are S-functors by Theorem 4.10 Thus we have $F[H]=\Delta[H]=\Delta^{c h}[H]=F\left[H^{c h}\right]$. But then $\gamma \circ \delta$ is a chordal completion of $X$ with width $F\left[H^{c h}\right]=F[H]$, as desired.

The S-functor $\Delta$ constructed above satisfies a maximality property broadly analogous to Theorem 2.4.

Theorem 4.12. Let ( $\mathcal{C}, \Omega, \mathfrak{P}$ ) be any measurable spined category. The set of all $S$ functors over ( $\mathcal{C}, \Omega, \mathfrak{P}$ ) is a join semi-lattice under the pointwise ordering with $\Delta$ as its maximum element.

Proof. Let $\mathcal{Z}$ be any non-empty (possibly infinite) subset of the set of S -functors over $(\mathcal{C}, \Omega, \mathfrak{P})$. In what follows we shall first construct the supremum of $\mathcal{Z}$ and then we will prove that it constitutes an S -functor.

Define the map $F_{\mathcal{Z}}: \mathcal{C} \rightarrow \mathbb{N}$ for any $W$ in $\mathcal{C}$ as $F_{\mathcal{Z}}[W]:=\max _{F^{\prime} \in \mathcal{Z}} F^{\prime}[W]$. (Note that this maximum always exists since every object $X$ is mapped by any S-functor to at most the value of $|X|$ and hence $\left\{F^{\prime}[X]: F^{\prime} \in \mathcal{Z}\right\}$ is a bounded set of integers.)

We claim that, for any arrow $m: X \rightarrow Y$ in $\mathcal{C}$, we have $F_{\mathcal{Z}}[X] \leq F_{\mathcal{Z}}[Y]$. To see this, let $Q$ be an element of $\mathcal{Z}$ such that $Q[X]=F_{\mathcal{Z}}[X]$ (by the definition of $F_{\mathcal{Z}}$ and since $\mathcal{Z}$ is non-empty, such a $Q$ always exists). The functoriality of $Q$ implies that, if there is an arrow $X \rightarrow Y$ in $\mathcal{C}$, then $Q[X] \leq Q[Y]$; in particular we can deduce that

$$
F_{\mathcal{Z}}[X]=Q[X] \leq Q[Y] \leq \max _{F^{\prime} \in \mathcal{Z}} F^{\prime}[Y]=F_{\mathcal{Z}}[Y]
$$

Hence there is an arrow $g: F_{\mathcal{Z}}[X] \rightarrow F_{\mathcal{Z}}[Y]$ in Nat, which means that we can (slightly abusing notation) render $F_{\mathcal{Z}}$ a functor by extending the definition of $F_{\mathcal{Z}}$ to map any arrow $m: X \rightarrow Y$ to the arrow $g: F_{\mathcal{Z}}[X] \rightarrow F_{\mathcal{Z}}[Y]$ in Nat.

From what we showed above, we know that $F_{\mathcal{Z}}$ is a functor. Now we will show that it is spinal functor. Note that $F_{\mathcal{Z}}$ clearly preserves the spine; furthermore, for any span $A \stackrel{a}{\longleftarrow} \Omega_{n} \xrightarrow{b} B$, we have

$$
\begin{array}{rlr}
F_{\mathcal{Z}}[\mathfrak{P}(a, b)] & =\max _{F^{\prime} \in \mathcal{Z}} F^{\prime}[\mathfrak{P}(a, b)] & \text { (by the definition of } \left.F_{\mathcal{Z}}\right) \\
& =\max _{F^{\prime} \in \mathcal{Z}} \max \left\{F^{\prime}[A], F^{\prime}[B]\right\} & \text { (since } F^{\prime} \text { is an S-functor) } \\
& =\max \left\{F_{\mathcal{Z}}[A], F_{\mathcal{Z}}[B]\right\} . &
\end{array}
$$

Thus $F_{\mathcal{Z}}$ is an S-functor since it satisfies Properties SF1 and SF2 In particular we have proved that the set of all S -functors over ( $\mathcal{C}, \Omega, \mathfrak{P}$ ) is a join semi-lattice under the point-wise ordering.

To see that $\Delta$ is the largest element of this semi-lattice, take any pseudo-chordal completion $\delta: X \rightarrow H$ of some object $X$. For any $S$-functor $F$, the following diagram commutes (by functoriality).
![](https://cdn.mathpix.com/cropped/a6ceea72-3d46-4a11-8691-56c7ecd0af06-18.jpg?height=190&width=291&top_left_y=580&top_left_x=915)

But since $\Delta[X]:=F[H]$, we have $F[X] \leq \Delta[X]$ and hence $\Delta$ is the maximum element of the join semi-lattice of S-functors.

## 5 Abstract analogues of tree-width.

In this section we will find instantiations of spined categories such that their triangulation numbers recover tree-width, hypergraph tree-width and complemented tree-width (i.e. the invariant $G \mapsto \mathbf{t w}(\bar{G})+1$ ) .

### 5.1 Tree-width of graphs and hypergraphs

Earlier we showed (Proposition 3.7) that every S-function yields an S-functor over $\mathbf{G r}_{\text {mono }}$. The next result goes further than this and shows that the triangulation functor on $\mathbf{G r}_{\text {mono }}$ takes every graph $G$ to $\mathbf{t w}(G)+1$.

Corollary 5.1. Let $\Delta$ be the triangulation functor of $\mathbf{G r}_{\text {mono }}$. Then, for any graph $G$, we have $\Delta[G]=\mathbf{t w}(G)+1$.

Proof. In $\mathbf{G r}_{\text {mono }}$ the generalized clique-number agrees with the clique number. Hence we compute

$$
\begin{aligned}
\mathbf{t w}(G)+1 & =\min \{\omega(H): H \text { is a chordal completion of } G\}(\text { see [13] }) \\
& =\Delta^{c h}[G]\left(\text { since } \omega \text { is an S-functor in } \mathbf{G r}_{\text {mono }}\right) \\
& =\Delta[G](\text { by Corollary } 4.11)
\end{aligned}
$$

Next we consider the category $\mathbf{H G r}_{\text {mon }}$ of hypergraphs and their injective homomoprhisms which we describe now. Let $H_{1}$ and $H_{2}$ be hypergraphs; a vertex map $h: V\left(H_{1}\right) \rightarrow V\left(H_{2}\right)$ is a hypergraph homomorphism if it preserves hyper-edges; that is to say that, for every edge $F \in E\left(H_{1}\right)$, the set $h(F):=\{h(x): x \in F\}$ is a hyper-edge in $H_{2}$. Hypergraph homomorphisms clearly compose associatively, thus we can define the category $\mathbf{H G r}_{\text {mono }}$ which has finite hypergraphs as objects and injective hypergraph homomorphisms as arrows.

Theorem 5.2. Let $\Omega: \mathbb{N}_{=} \rightarrow \mathbf{H G r}$ be the functor taking every integer $n$ to the hypergraph $\left([n], 2^{[n]}\right)$ and let $\mathfrak{P}$ assign to each span of the form $H_{1} \stackrel{h_{1}}{\longleftrightarrow} \Omega_{n} \xrightarrow{h_{2}} H_{2}$ in $\mathbf{H G r}$ the cocone $H_{1} \underset{\mathfrak{P}\left(h_{1}, h_{2}\right)_{h_{1}}}{\longrightarrow} \mathfrak{P}\left(h_{1}, h_{2}\right) \stackrel{\mathfrak{P}\left(h_{1}, h_{2}\right)_{h_{2}}}{\longleftrightarrow} H_{2}$ where

$$
\mathfrak{P}\left(h_{1}, h_{2}\right):=\left(\left(V\left(H_{1}\right) \uplus V\left(H_{2}\right)\right) / h_{1}=h_{2},\left(E\left(H_{1}\right) \uplus E\left(H_{2}\right)\right) / h_{1}=h_{2}\right)
$$

and $\mathfrak{P}\left(h_{1}, h_{2}\right)_{h_{i}}$ is the map taking every vertex $v$ in $H_{i}$ to $v_{i}$ in $\mathfrak{P}\left(h_{1}, h_{2}\right)$. Then the triple $(\mathbf{H G r}, \Omega, \mathfrak{P})$ is a spined category.

Proof. Clearly Property SC1 is satisfied, so, to show Property SC2, consider the following diagram in $\mathbf{H G r}$ (we will argue for the existence and uniqueness of $\left(j_{1}, j_{2}\right)$.
![](https://cdn.mathpix.com/cropped/a6ceea72-3d46-4a11-8691-56c7ecd0af06-19.jpg?height=308&width=689&top_left_y=1001&top_left_x=717)

We define $\left(j_{1}, j_{2}\right): \mathfrak{P}\left(h_{1}, h_{2}\right) \rightarrow \mathfrak{P}\left(j_{1}, j_{2}\right)$ as

$$
\left(j_{1}, j_{2}\right)(x):=\left\{\begin{array}{l}
j_{1}(x) \text { if } x \in V\left(H_{1}\right) \cap \mathfrak{P}\left(h_{1}, h_{2}\right) \\
j_{2}(x) \text { otherwise } .
\end{array}\right.
$$

Clearly ( $j_{1}, j_{2}$ ) is the unique injective vertex-map making the diagram commute (this can be easily seen by considering the forgetful functor taking every hypergraph to its vertex-set). Furthermore, by recalling the definition of the proxy pushout, one can easily see that it is in fact an injective hypergraph homomorphism, as desired. $\square$

Note that we can also construct a spined functor from the spined category HGr of hypergraphs to the spined category $\mathbf{G r}_{\text {mono }}$ of graphs. We do this by observing that the mapping $\mathfrak{G}: \mathbf{H G r} \rightarrow \mathbf{G r}_{\text {mon }}$ which associates every hypergraph to its Gaifman graph (sometimes also referred to as 'primal graph') is clearly functorial.

Proposition 5.3. The Gaifman graph functor $\mathfrak{G}: \mathbf{H G r} \rightarrow \mathbf{G r}_{\text {mono }}$ is a spined functor.
Proof. Note that $\mathfrak{G}\left[\left([n], 2^{[n]}\right)\right]=K_{n}$ (i.e. $\mathfrak{G}$ satisfies Property SF1). Now take the proxy pushout $\mathfrak{P}\left(h_{1}, h_{2}\right)$ of some span $\boldsymbol{H}_{1} \stackrel{h_{1}}{\longleftrightarrow} \Omega_{n} \xrightarrow{h_{2}} \boldsymbol{H}_{2}$ in HGr. Recall that $\mathfrak{P}\left(h_{1}, h_{2}\right)$ is constructed by identifying $H_{1}$ and $H_{2}$ along $\Omega_{n}:=\left([n], 2^{[n]}\right)$. Thus, since $\mathscr{G}$ preserves the spine (as we just showed) we know that the Gaifman graph $\mathfrak{G}\left[\mathfrak{P}\left(h_{1}, h_{2}\right)\right]$ of $\mathfrak{P}\left(h_{1}, h_{2}\right)$ is given by the clique-sum along a $K_{n}$ of the Gaifman graphs of $H_{1}$ and $H_{2}$. In other words we have $\mathfrak{G}\left[\mathfrak{P}\left(h_{1}, h_{2}\right)\right]=\mathfrak{G}\left[H_{1}\right] \#_{\mathfrak{G}\left[\Omega_{n}\right]} \mathfrak{G}\left[H_{1}\right]$ which proves that $\mathfrak{G}$ satisfies Property SF2 Thus $\mathfrak{G}$ is a spined functor. $\square$

Corollary 5.4. The spined category HGr is measurable; in particular there are uncountably many $S$-functors over $\mathbf{H G r}$.

Proof. Immediate from Propositions 3.7 and 5.3.
Now consider any proxy pushout $\mathfrak{P}\left(h_{1}, h_{2}\right)$ of a span $H_{1} \stackrel{h_{1}}{\longleftrightarrow} \Omega_{n} \xrightarrow{h_{2}} H_{2}$ in HGr. It follows (in much the same way as it does for graphs) that the tree-width of $\mathfrak{P}\left(h_{1}, h_{2}\right)$ is the maximum of $\mathbf{t w}\left(H_{1}\right)$ and $\mathbf{t w}\left(H_{2}\right)$. Since, by the definition of treewidth, we have $\mathbf{t w}\left(\left([n], 2^{[n]}\right)\right)=n-1$, it follows that, in $(\mathbf{H G r}, \Phi), \Delta(K)=\mathbf{t w}(K)+1$ for any chordal object $K$ in ( HGr, $\Phi$ ). Thus we shave shown the following result.

Corollary 5.5. If $\Delta$ is the triangulation number of $(\mathbf{H G r}, \Omega, \mathfrak{P})$, then, for any hypergraph $H, \Delta(H)=\mathbf{t w}(H)+1$.

### 5.2 Complemented tree-width

Another example of a spined category is given by taking the discrete graphs $\left(\overline{K_{n}}\right)_{n \in \mathbb{N}}$ as the spine for the category $\mathbf{G r}_{\mathrm{R} \text {-mono }}$ of graphs and reflexive monomorphisms (which we define in what follows).

Definition 5.6. A vertex map $f: V(G) \rightarrow V(H)$ is a reflexive homomorphism from the graph $G$ to the graph $H$ if the following implication holds for all pairs of vertices $x$ and $y$ in $G$ : $f(x) f(y) \in E(H) \Rightarrow x y \in E(G)$.

In what follows we denote by $\mathbf{G r}_{\mathrm{R} \text {-homo }}$ the category having graphs as objects and reflexive homomorphisms as arrows, while we denote by $\mathbf{G r}_{\mathrm{R} \text {-mono }}$ the category of graphs and injective reflexive homomorphisms.

Proposition 5.7. If $f: \bar{K}_{n} \rightarrow H$ is an arrow in $\mathbf{G r}_{\mathrm{R}-\operatorname{mono}}$, then the image of $f$ in $H$ is an independent set.

Proof. B.w.o.c. if $f(x) f(y) \in E(H)$, then $x y \in E\left(\overline{K_{n}}\right)$ even though $E\left(\overline{K_{n}}\right)=\emptyset$.
Since $\overline{K_{n}}$ has no edges, every graph on at-most $n$ vertices has an injective reflexive homomorphism to $\overline{K_{n}}$. Thus $\left(\overline{K_{n}}\right)_{n \in \mathbb{N}}$ satisfies Property SC1 in $\mathbf{G r}_{\mathrm{R}-\text { mono }}$ and hence forms a suitable spine.

Now, we will show that there is an appropriate choice of a proxy-pushout operation - which we will denote as $\mathfrak{J}$ - which turns $\left(\mathbf{G r}_{\mathrm{R}-\text { mono }},\left(\overline{K_{n}}\right)_{n \in \mathbb{N}}, \mathfrak{J}\right)$ into a measurable spined category.

A first, but naive candidate for $\mathfrak{J}$ is the operation taking any span of the form $L \stackrel{\ell}{\longleftrightarrow} \overline{K_{n}} \xrightarrow{r} R$ in $\mathbf{G r}_{\mathrm{R}-\text { mono }}$ to the graph obtaned by 'gluing' $L$ to $R$ along their shared independent set (c.f. Proposition5.7) of size $n$ (i.e. identify the image of $\overline{K_{n}}$ in $L$ to the image of $\overline{K_{n}}$ in $R$ ). Notice, though, that if we took $L \cong \bar{K}_{\ell}$ and $R \cong \bar{K}_{r}$, then this construction would produce as their proxy-pushout the graph $\bar{K}_{\ell+r-n}$. However, this would then preclude the existence of any S-functor $F$ over this spined category since such an $F$ would have to simlutaneously satisfy $F\left[\bar{K}_{\ell+r-n}\right]=\ell+r-n$ (because
$\bar{K}_{\ell+r-n}$ is in the spine) and also $F\left[\bar{K}_{\ell+r-n}\right]=\max \{\ell, r\}$ (because max is the proxy pushout of Nat). Thus, with these considerations in mind, we come to the following definition of $\mathfrak{J}$.

Definition 5.8. Let $\mathfrak{J}$ be the operation taking every span in $\mathbf{G r}_{\mathrm{R}-\text { mono }}$ of the form $L \stackrel{\ell}{\longleftrightarrow} \bar{K}_{n} \xrightarrow{r} R$ to the cospan $L \xrightarrow{\mathfrak{I}(\ell, r)} \mathfrak{S}(\ell, r) \stackrel{\mathfrak{S}(\ell, r)_{r}}{\stackrel{ }{ }} R$ which we define as follows. The graph $\mathfrak{I}(\ell, r)$ is given by identifying $L$ and $R$ along their shared $n$ vertex independent set and then adding edges to this resulting graph so as to make $L \backslash \ell\left(\overline{K_{n}}\right)$ complete to $R \backslash \ell\left(\overline{K_{n}}\right)$; in other words $\mathfrak{I}(\ell, r)$ is the graph with vertex-set $(V(L) \uplus V(R)) /_{\ell=r}$ and edge-set

$$
E(L) \uplus E(R) \uplus\left(\left(V(L) \backslash \ell\left(\overline{K_{n}}\right)\right) \times\left(V(R) \backslash r\left(\overline{K_{n}}\right)\right)\right) .
$$

Finally, the arrows $\mathfrak{I}(\ell, r)_{\ell}$ and $\mathfrak{I}(\ell, r)_{r}$ are just the obvious injections taking $L$ and $R$ respectively into $\mathfrak{I}(\ell, r)$ (these are easily seen to be reflexive homomorphisms).

Proposition 5.9. The triple $\left(\mathbf{G r}_{\mathrm{R}-\text { mono }},\left(\overline{K_{n}}\right)_{n \in \mathbb{N}}, \mathfrak{J}\right)$ is a spined category.
Proof. As we already observed, Property SC1 is satisfied. For Property SC2, we are given any diagram $L^{\prime} \stackrel{\ell^{\prime}}{\longleftrightarrow} L \stackrel{\ell}{\longleftrightarrow} \overline{K_{n}} \xrightarrow{r} R \xrightarrow{r^{\prime}} R^{\prime}$ in $\mathbf{G r}_{\mathrm{R}-\text { mono }}$, and we need to demonstrate the existence of a unique arrow $m: \mathfrak{I}(\ell, r) \rightarrow \mathfrak{I}\left(\ell^{\prime} \ell, r^{\prime} r\right)$ which makes the following diagram commute.
![](https://cdn.mathpix.com/cropped/a6ceea72-3d46-4a11-8691-56c7ecd0af06-21.jpg?height=297&width=618&top_left_y=1409&top_left_x=751)

We use $\ell^{\prime}$ and $r^{\prime}$ to define $m$ piece-wise as follows:

$$
m: x \mapsto\left\{\begin{array}{l}
\left(\Im\left(\ell^{\prime} \ell, r^{\prime} r\right)_{r^{\prime} r} \circ r^{\prime}\right)(x) \text { if } x \in V(R) \cap V(\Im(\ell, r)) \\
\left(\Im\left(\ell^{\prime} \ell, r^{\prime} r\right)_{\ell^{\prime} \ell^{\circ}} \circ \ell^{\prime}\right)(x) \text { otherwise. }
\end{array}\right.
$$

Clearly $m$ is the unique injective vertex-map that makes the above diagram commute; thus all that remains to be shown is that $m$ is indeed a reflexive homomorphism. However, this follows immediately from the definition of $\Im$ and from the fact that $r^{\prime}$ and $\ell^{\prime}$ are $R$-homomorphisms. $\square$

Proposition 5.10. The complementation map $\overline{(-)}: \mathbf{G r}_{\mathrm{R}-\text { mono }} \rightarrow \mathbf{G r}_{\text {mono }}$ is a functor and indeed it is an isomorphism of categories.

Proof. First notice that $\overline{(-)}$ preserves identity arrows and it is a bijection on objects; so now consider an arrow $a: A \rightarrow B$ in $\mathbf{G r}_{\mathrm{R} \text {-mono }}$ we claim that the vertex map specified
by $a$ constitutes an arrow from $\bar{A}$ to $\bar{B}$ in $\mathbf{G r}_{m o n o}$. To see this, take any edge $x y \in E(\bar{A})$; since $x$ and $y$ are not adjacent in $A$, then $a(x) a(y) \notin E(B)$ (since $a$ is a reflexive homomorphism) and thus $a(x) a(y) \in E(\overline{\boldsymbol{B}})$.

Conversely, if $a: \bar{A} \rightarrow \bar{B}$ is an arrow in $\mathbf{G r}_{\text {mono }}$, for each pair $a(x) a(y) \in E(B)$ we must have $x y \notin E(\bar{A})$ (since $a$ is a graph monomorphism and thus $A$ is a subgraph of $\boldsymbol{B}$ ) which is equivalent to saying that $a(x) a(y) \in E(\boldsymbol{B})$ implies $x y \in E(A)$, as desired. Thus we have that $\overline{(-)}$ is a functor which is bijective on objects, bijective on arrows, full and faithful. Furthermore, it is easily seen that complementation is self-inverse, so it is the desired isomorphism of categories. $\square$

Corollary 5.11. The isomorphism $\overline{(-)}: \mathbf{G r}_{\mathrm{R}-\text { mono }} \rightarrow \mathbf{G r}_{\text {mono }}$ is a spined functor

$$
\overline{(-)}:\left(\mathbf{G r}_{\mathrm{R}-\text { mono }},\left(\overline{K_{n}}\right)_{n \in \mathbb{N}}, \mathfrak{I}\right) \rightarrow\left(\mathbf{G r}_{\text {mono }},\left(K_{n}\right)_{n \in \mathbb{N}}, \#\right) .
$$

Proof. By Proposition $5.10, \overline{(-)}$ is a functor and indeed it is an isomorphism of categories. It clearly preserves the spine and it also takes any proxy-pushout square
![](https://cdn.mathpix.com/cropped/a6ceea72-3d46-4a11-8691-56c7ecd0af06-22.jpg?height=199&width=1002&top_left_y=1153&top_left_x=556)

Thus $\overline{(-)}$ is a spined functor. $\square$

Since spined functors compose and since $\left(\mathbf{G r}_{\text {mono }},\left(K_{n}\right)_{n \in \mathbb{N}}, \#\right)$ is measurable, we also immediately have the following result.

Corollary 5.12. The spined category $\left(\mathbf{G r}_{\mathrm{R}-\mathrm{mono}},\left(\overline{K_{n}}\right)_{n \in \mathbb{N}}, \mathfrak{I}\right)$ is measurable.
An example of an S-functor over $\left(\mathbf{G r}_{\mathrm{R}-\text { mono }},\left(\overline{K_{n}}\right)_{n \in \mathbb{N}}, \mathfrak{J}\right)$ is its generalized clique number $\dot{\omega}_{R}$ (i.e. the function associating to each graph its independence number). This can be easily seen either by factoring it through the complementation map as $\dot{\omega}_{R}=\omega \circ \overline{(-)}$ or by simply checking from first principles that $\dot{\omega}_{R}$ satisfies Properties SF1 and SF2.

Corollary 5.13. Letting $\Delta$ be the triangulation functor of $\left(\mathbf{G r}_{\mathrm{R}-\operatorname{mono}},\left(\overline{K_{n}}\right)_{n \in \mathbb{N}}, \mathfrak{J}\right.$ ), we have $\Delta[G]=\mathbf{t w}(\bar{G})+1$ for all graphs $G$.

## 6 New Spined Categories from Old

The spined categories encountered so far came equipped with their "standard" notion of (mono)morphism: posets with monotone maps, graphs with graph homomorphsims, hypergraphs with hypergraph homomorphisms or graphs with reflexive homomorphisms. In particular, for a class $S$ of combinatorial objects decorated with extraneous structure
(such as colored or labeled graphs), the appropriate choice of morphism may be less obvious. In these cases, a "forgetful" function $f: S \rightarrow \mathcal{C}$ from $S$ to some spined category $\mathcal{C}$ allows us to study properties of $S$ by studying properties of its image in $\mathcal{C}$.

It is straightforward to check that we can define a category $S_{\downarrow f}$, which we call the $S$-category induced by $f$ by taking $S$ itself as the collection of objects of $S_{\downarrow f}$ and, for any two objects $A$ and $B$ in $S$, setting $\boldsymbol{\operatorname { H o m }}_{S_{\downarrow f}}(A, B):=\boldsymbol{\operatorname { H o m }}_{C}(f(A), f(B))$.

It will be convenient to notice that - up to categorial isomorphism $-f^{-1}(X)$ (for any object $X$ in the range of $f$ ) consists of only one object in $S_{\downarrow f}$. To see this, suppose $f$ is not injective (otherwise there is nothing to show) and let $A, B \in S$ be elements of the set $f^{-1}(X)$. By the definition of $S_{\downarrow f}$, we know that $\mathbf{i d}_{X} \in \mathbf{H o m}_{S_{\downarrow f}}(A, B)$ since $\boldsymbol{\operatorname { H o m }}_{S_{\downarrow f}}(A, B)=\boldsymbol{\operatorname { H o m }}_{C}(A, B)$. Thus $A$ and $B$ are isomorphic in $S_{\downarrow f}$ since identity arrows are always isomorphisms.

Note that by the construction of $S_{\downarrow f}$, the function $f$ actually constitutes a faithful and injective (on objects and arrows) functor from $S_{\downarrow f}$ to $\mathcal{C}$. The next result shows that if $\mathcal{C}$ is spined and if the range of $f$ is sufficiently large, then we can chose a spine $\Omega^{S}$ and a proxy pushout $\mathfrak{P}^{S}$ on $S_{\downarrow f}$ which turn $\left(S_{\downarrow f}, \Omega^{S}, \mathfrak{P}^{S}\right)$ into a spined category and $f:\left(S_{\downarrow f}, \Omega^{S}, \mathfrak{P}^{S}\right) \rightarrow(\mathcal{C}, \Omega, \mathfrak{P})$ into a spined functor.

Theorem 6.1. Let ( $\mathcal{C}, \Omega, \mathfrak{P}$ ) be a spined category, $S$ be a set and $f: S \rightarrow \mathcal{C}$ be a function. If $f$ is both

1. surjective on the spine of $\mathcal{C}$ (i.e. $\forall n \in \mathbb{N}, \exists X \in S$ s.t. $f(X)=\Omega_{n}$ ) and such that
2. for every span $f(X) \stackrel{x}{\bigsqcup} \Omega_{n} \xrightarrow{y} f(Y)$ in $\mathcal{C}$, there exists a distinguished element $Z_{x, y} \in S$ such that $f\left(Z_{x, y}\right)=\mathfrak{P}(x, y)$,
then we can choose a functor $\Omega^{S}$ and operation $\mathfrak{P}^{S}$ such that

- $\left(S_{\downarrow f}, \Omega^{S}, \mathfrak{P}^{S}\right)$ is a spined category and
- $f$ is a spinal functor from ( $S_{\downarrow f}, \Omega^{S}, \mathfrak{P}^{S}$ ) to ( $\mathcal{C}, \Omega, \mathfrak{P}$ )
- if ( $\mathcal{C}, \Omega, \mathfrak{P}$ ) is a measurable spined category, then so is ( $S_{\downarrow f}, \Omega^{S}, \mathfrak{P}^{S}$ ).

Proof. Define $\Omega^{S}$ and $\mathfrak{P}^{S}$ as follows:

- $\Omega^{S}: \mathbb{N}_{=} \rightarrow S_{\downarrow f}$ is the functor taking each $n$ to an element of $f^{-1}\left(\Omega_{n}\right)$ (we can think of this as picking a representative of the equivalence class $f^{-1}\left(\Omega_{n}\right)$ for each $n$ since, as we observed earlier, all elements of $f^{-1}\left(\Omega_{n}\right)$ are isomorphic),
- $\mathfrak{P}^{S}$ is the operation assigning to each span $X \stackrel{x}{\longleftrightarrow} \Omega_{n} \xrightarrow{y} Y$ in $S_{\downarrow f}$ the cocone $X \xrightarrow{\mathfrak{P}(x, y)_{x}} \mathfrak{P}^{S}(x, y):=Z_{x, y} \stackrel{\mathfrak{P}(g, h)_{h}}{\stackrel{ }{\longleftrightarrow}} Y$, where $Z_{x, y}$ is the distinguished element whose existence is guaranteed by the second property of $f$.

Now we will show that ( $S_{\downarrow f}, \Omega^{S}, \mathfrak{P}^{S}$ ) is a spined category. Property SC1 holds in $\left(S_{\downarrow f}, \Omega^{S}, \mathfrak{P}^{S}\right)$ since it holds in $(\mathcal{C}, \Omega, \mathfrak{P})$ and since, for all $A, B \in S$, we have $\mathbf{H o m}_{S_{\downarrow f}}(A, B):=$
$\mathbf{H o m}_{C}(\boldsymbol{A}, \boldsymbol{B})$. To show Property SC2, we must argue that that, for every diagram of the form
![](https://cdn.mathpix.com/cropped/a6ceea72-3d46-4a11-8691-56c7ecd0af06-24.jpg?height=323&width=794&top_left_y=541&top_left_x=558)
in $S_{\downarrow f}$ there is an arrow $p$ (which is dotted in Diagram (1)) which makes the diagram commute.

By the second condition on $f$, we know that $f\left(\mathfrak{P}^{S}\left(j_{1} h_{1}, j_{2} h_{2}\right)\right)=\mathfrak{P}\left(f j_{1} h_{1}, f j_{2} h_{2}\right)$ and $f\left(\mathfrak{P}^{S}\left(j_{1} h_{1}, j_{2} h_{2}\right)\right)=\mathfrak{P}\left(f j_{1} h_{1}, f j_{2} h_{2}\right)$. Thus we have that $f$ maps Diagram (1) in $S_{\downarrow f}$ to the following diagram in $\mathcal{C}$.
![](https://cdn.mathpix.com/cropped/a6ceea72-3d46-4a11-8691-56c7ecd0af06-24.jpg?height=321&width=1286&top_left_y=1211&top_left_x=472)

Since ( $\mathcal{C}, \boldsymbol{\Omega}, \mathfrak{P}$ ) satisfies Property SC2, the dashed arrow ( $j_{1}, j_{2}$ ) in Diagram (2) exists, is unique and makes the diagram commute. But since we have $\mathbf{H o m}_{S_{\downarrow f}}(A, B):= \boldsymbol{\operatorname { H o m }}_{C}(A, B)$ for all $A, B \in S$, we know that $p=\left(j_{1}, j_{2}\right)$, as desired.

Now we will argue that $f$ is a spinal functor. By the first property of $f$, we know that $f$ preserves the spine. By the second property of $f$ and by what we just argued about Diagrams (1) and (2), we know that $f$ satisfies Property SF2 as well. Thus $f$ is a spinal functor from ( $S_{\downarrow f}, \Omega^{S}, \mathfrak{P}^{S}$ ) to ( $\mathcal{C}, \Omega, \mathfrak{P}$ ).

Finally note that, since $f$ is a spinal functor from ( $S_{\downarrow f}, \Omega^{S}, \mathfrak{P}^{S}$ ) to ( $\mathcal{C}, \Omega, \mathfrak{P}$ ), it must be that, if there exists an $S$-functor $G$ over $(\mathcal{C}, \Omega, \mathfrak{P})$, then the composition $G \circ f$ is an $S$-functor over $\left(S_{\downarrow f}, \Omega^{S}, \mathfrak{P}^{S}\right)$. Thus $\left(S_{\downarrow f}, \Omega^{S}, \mathfrak{P}^{S}\right)$ is measurable whenever $(\mathcal{C}, \Omega, \mathfrak{P})$ is. $\square$

Theorem 6.1 allows us to easily define new spined categories from ones we already know. For example, denoting, for every graph $G$, the set of all functions of the form $f: V(G) \rightarrow[|V(G)|]$ as $\ell(G)$, consider the set $\mathcal{L}:=\{\ell(G): G \in \mathcal{G}\}$ of all vertexlabelings of all finite simple graphs. Let $Q: \mathcal{L} \rightarrow \mathbf{G r}_{\text {mono }}$ be the surjection

$$
Q:(f: G \rightarrow[|V(G)|]) \longmapsto G / f
$$

which takes every labeling $f: G \rightarrow[|V(G)|]$ in $\mathcal{L}$ to the quotient graph

$$
G /_{f}:=\left(V(G) /_{f}, E(G) /_{f} \backslash\{x x: x \in V(G)\}\right) .
$$

Since $\mathbf{G r}_{\text {mono }}$ is a measurable spined category, by Theorem 6.1 we know that $\mathcal{L}_{\downarrow Q}$ is also a measurable spined category. In particular, the triangulation number $\Delta_{\ell}$ of $\mathcal{L}_{\downarrow Q}$ takes any object $f: G \rightarrow[|V(G)|]$ in $\mathcal{L}_{\downarrow Q}$ to the tree-width of $G /_{f}$.

This construction might seem peculiar, since it maps labeling functions (as opposed to graphs themselves) to tree-widths of quotiented graphs. Thus we define the $\ell$-treewidth of any graph $G$, denoted $\mathbf{t w}_{\ell}(G)$, as $\mathbf{t w}_{\ell}(G)=\min _{f \in \ell(G)} \Delta_{\ell}[f]$. This becomes trivialy if we allow all possible vertex-labelings. However, by imposing restrictions on the permissible labelings, we can obtain more meaningful width-measures on graphs. We briefly consider two examples to demonstrate this principle.

Example 6.2 (Modular tree-width). Recall that a vertex-subset $X$ of a graph $G$ is a called a module in $G$ if, for all vertices $z \in V(G) \backslash X$, either $z$ is adjacent to every vertex in $X$ or $N(z) \cap X=\emptyset$. We call a labeling function $f: V(G) \rightarrow[|V(G)|]$ modular if, for all $i \in[|V(G)|]$, the preimage $f^{-1}(i)$ of $i$ is a module in $G$. Thus, denoting by $\mathcal{M}$ the set $\mathcal{M}:=\{\{\lambda: \lambda$ is modular labeling of $G\}: G \in \mathcal{G}\}$ of all modular labelings, we obtain, as we did above, a spined category $\mathcal{M}_{\downarrow Q}$, where $Q$ is the function taking each modular labeling to its corresponding modular quotient.

Note that the triangualation number of $\mathcal{M}_{\downarrow Q}$ maps every modular labeling to the tree-width of the corresponding modular quotient. Thus we can define modular treewidth which takes any graph $G$ to the minimum tree-width possible over the set of all modular quotients of $G$.

Example 6.3 (Chromatic tree-width). Denote the set of all proper colorings as col := $\{\{\lambda: \lambda$ is proper coloring of $G\}: G \in \mathcal{G}\}$. Then, as we just did in Example 6.2, we can study the spined category $\mathbf{c o l}_{\downarrow Q}$ and its triangulation number. Proceeding as before, this immediately yields the notion of chromatic tree-width.

## 7 Further Questions

As we have seen, spined categories provide a convenient categorial settings for the study of tree-like decompositions.

Proxy pushouts occupy a middle ground between the amalgamation property familiar from model theory (see e.g. Brody's dissertation [5] for a thorough graph-theoretic treatment) and the amount of exactness available in e.g. adhesive categories [23]. The latter do not allow us to define width measures functorially since they would rule out Nat as a codomain for our functors (in particular poset categories are not adhesive). In contrast, Nat has proxy pushouts and is a spined category.

Among spined categories, the measurable ones come equipped with a distinguished S-functor, the triangulation functor of Definition 4.9, which can be seen as a general counterpart to the graph-theoretic notion of tree-width, and which gives rise to an associated notion of completion/decomposition. Moreover, Theorem 4.10 shows that the
only possible obstructions to measurability are the generic ones: if there is no obstruction so strong that it precludes the existence of every S-functor, there can be no further obstruction preventing the existence of the triangulation functor.

Since most settings have only one obvious choice of structure-preserving morphism (which fixes the pushout construction as well), functoriality leaves the choice of an appropriate spine as the only "degree of freedom'3. This makes spined categories an interesting alternative to other techniques for defining graph width measures, such as layout\$ (used for defining branch-width [29], rank-width [26], $\mathbb{F}_{4}$-width [21], bi-cut-rankwidth [21] and min-width [31]), which rely on less easily generalized, graph-theoryspecific notions of connectivity. Finding algebraic examples of spined categories and associated width measures remains a promising avenue for further work. In particular, as we move from combinatorial structures towards algebraic and order-theoretic ones, choosing a spine becomes an abundant source of technical questions.

Question. Consider the category Poset $_{o e}$ which has finite posets as objects and order embeddings as morphisms, equipped with the usual pushout construction. Is there a sequence of objects $n \mapsto \Omega_{n}$ which makes Poset $_{o e}$ into a measurable spined category?

Another promising topic for future work (which we describe in what follows) would be to 'allow more complex spines'. Currently the spine of any spined category $\mathcal{C}$ consists of an $\mathbb{N}$-indexed sequence of objects $\Omega_{1}, \Omega_{2}, \ldots$ which satisfies the requirement that for each object $X$ of $C$, there exists at least one natural $n$ such that the homset $\boldsymbol{\operatorname { H o m }}_{C}\left(X, \Omega_{n}\right)$ is non-empty. Such sequences exist in many interesting categories involving combinatorial objects; however, in these settings there might not be an optimal (not to mention unique) such choice. For example, in the category having graphs as objects and topological minors as arrows, should we choose $\left(K_{n}\right)_{n \in \mathbb{N}}$ to be the spine or should we choose the sequence $\left(\mathbb{K}_{n}\right)_{n \in \mathbb{N}}$ whose $n$-th element is the graph obtained by subdividing a each edge of an $n$-clique $n$-times? A similar example (already observed by Wollan [32, Observation 1]) can be made for graph immmersions: for every graph $G$, there exist naturals $n$ and $\ell$ such that $G$ has an immersion to a star on $n$-leaves with $\ell$ parallel edges joining the center to each leaf. These considerations motivate our desire for an even further generalization of spined categories to a similar construct where the spine need not be an $\mathbb{N}$-indexed sequence; indeed this is a promising direction for future work.

## References

[1] I. Adler, G. Gottlob, and M. Grohe. Hypertree width and related hypergraph invariants. European Journal of Combinatorics, 28(8):2167-2181, 2007.
[2] S. Awodey. Category theory. Oxford university press, 2010.
[3] U. Bertelè and F. Brioschi. Nonserial dynamic programming. Academic Press, Inc., 1972.

[^2][4] D. Berwanger, A. Dawar, P. Hunter, S. Kreutzer, and J. Obdržálek. The DAGwidth of directed graphs. Journal of Combinatorial Theory, Series B, 102(4):900923, 2012.
[5] J. Brody. On the model theory of random graphs. University of Maryland examined thesis, Ph. D., 2009.
[6] B. M. Bumpus. Generalizing graph decompositions. PhD thesis, University of Glasgow, 2021.
[7] B. M. Bumpus and Z. A. Kocsis. Treewidth via spined categories (extended abstract), 2021.
[8] M. Chein, M. Habib, and M. C. Maurer. Partitive hypergraphs. Discrete Mathematics, 37(1):35-50, 1981.
[9] B. Courcelle. The monadic second-order logic of graphs $x$ : Linear orderings. Theoretical Computer Science, 160(1):87-143, 1996.
[10] B. Courcelle, J. Engelfriet, and G. Rozenberg. Handle-rewriting hypergraph grammars. Journal of computer and system sciences, 46(2):218-270, 1993.
[11] W. H. Cunningham and J. E. A combinatorial decomposition theory. Canadian Journal of Mathematics, 32(3):734-765, 1980.
[12] M. Cygan, F. V. Fomin, Ł. Kowalik, D. Lokshtanov, D. Marx, M. Pilipczuk, M. Pilipczuk, and S. Saurabh. Parameterized algorithms. Springer, 2015.
[13] R. Diestel. Graph theory. Springer, 2010.
[14] J. Flum and M. Grohe. Parameterized complexity theory. 2006. Texts Theoret. Comput. Sci. EATCS Ser, 2006.
[15] M. Habib and C. Paul. A survey of the algorithmic aspects of modular decomposition. Computer Science Review, 4(1):41-59, 2010.
[16] R. Halin. S-functions for graphs. Journal of Geometry, 8(1-2):171-186, 1976.
[17] P. Hunter and S. Kreutzer. Digraph measures: Kelly decompositions, games, and orderings. Theoretical Computer Science (TCS), 399, 2008.
[18] O. F. Inc. The on-line encyclopedia of integer sequences. http://oeis.org/A051903, 2020. Accessed: 2020-11-08.
[19] D. S. Johnson. The np-completeness column: an ongoing guide. Journal of Algorithms, 6(3):434-451, 1985.
[20] T. Johnson, N. Robertson, P. D. Seymour, and R. Thomas. Directed tree-width. Journal of combinatorial theory. Series B, 82(1):138-154, 2001.
[21] M. M. Kanté and M. Rao. F-rank-width of (edge-colored) graphs. In International Conference on Algebraic Informatics, pages 158-173. Springer, 2011.
[22] S. Kreutzer and O.-j. Kwon. Digraphs of bounded width. In Classes of Directed Graphs, pages 405-466. Springer, 2018.
[23] S. Lack and P. Sobocinski. Adhesive categories. In I. Walukiewicz, editor, Foundations of Software Science and Computation Structures, pages 273-288, Berlin, Heidelberg, 2004. Springer Berlin Heidelberg.
[24] T. Leinster. Codensity and the ultrafilter monad. Theory and Applications of Categories, (28):332-370, 32013.
[25] T. Leinster. The categorical origins of Lebesgue integration. arXiv e-prints, page arXiv:2011.00412, Oct. 2020.
[26] S.-i. Oum and P. D. Seymour. Approximating clique-width and branch-width. Journal of Combinatorial Theory, Series B, 96(4):514-528, 2006.
[27] N. Robertson and P. Seymour. Graph minors. xx. wagner's conjecture. Journal of Combinatorial Theory, Series B, 92(2):325-357, 2004.
[28] N. Robertson and P. D. Seymour. Graph minors. II. Algorithmic aspects of treewidth. Journal of Algorithms, 7(3):309-322, 91986.
[29] N. Robertson and P. D. Seymour. Graph minors x. obstructions to treedecomposition. Journal of Combinatorial Theory, Series B, 52(2):153-190, 1991.
[30] M. A. Safari. D-width: A more natural measure for directed tree width. In International Symposium on Mathematical Foundations of Computer Science, pages 745-756. Springer, 2005.
[31] M. Vatshelle. New width parameters of graphs. 2012.
[32] P. Wollan. The structure of graphs not admitting a fixed immersion. Journal of Combinatorial Theory, Series B, 110:47-66, 2015.


[^0]:    *Mathematics and Computer Science, TU Eindhoven, GroeneLoper MetaForum Building PO Box 513, Eindhoven, 5600 MB , North Brabant, Netherlands. Supported both by an EPSRC studentship, and by the European Research Council (ERC) under the European Union's Horizon 2020 research and innovation programme (grant agreement No 803421, ReduceSearch)
    ${ }^{\dagger}$ CSIRO Data61, University of New South Wales, Kensington NSW 2052, Australia.

[^1]:    ${ }^{1}$ The maximum of the chromatic numbers over all minors [16]
    ${ }^{2}$ One plus the maximum of the connectivity number over all minors [16]

[^2]:    ${ }^{3}$ How can we tell that we chose a good spine? Measurability provides a natural criterion!
    ${ }^{4}$ Sometimes referred to as 'branch decompositions' of symmetric submodular functions.

