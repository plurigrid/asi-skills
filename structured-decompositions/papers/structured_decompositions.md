# Structured Decompositions: Structural and Algorithmic Compositionality. 

Benjamin Merlin Bumpus, Zoltan A. Kocsis, ${ }^{\dagger}$<br>Jade Edenstar Master ${ }^{\ddagger}$ \& Emilio Minichiello ${ }^{§}$

Last compilation: May 21, 2025


#### Abstract

We introduce structured decompositions, category-theoretic structures which simultaneously generalize notions from graph theory (including treewidth, layered treewidth, cotreewidth, graph decomposition width, tree independence number, hypergraph treewidth and $H$-treewidth), geometric group theory (specifically Bass-Serre theory), and dynamical systems (e.g. hybrid dynamical systems). We define sd-functors, which provide a compositional way to analyze and relate different structural complexity measures, and establish a general duality between decompositions and completions of objects.


## Contents

1 Introduction ..... 2
1.1 Related Work ..... 4
1.2 Notation ..... 5
1.3 Acknowledgements ..... 5
2 Structured Decomposition Categories ..... 5
2.1 The Category of Graphs ..... 5
2.2 Barycentric Subdivision ..... 6
2.3 Structured Decompositions ..... 7
2.4 Grothendieck Construction ..... 7
2.5 Width Categories ..... 8
2.6 Chordal Completions ..... 11
2.7 sd-Functors ..... 14
2.8 Tree Decompositions ..... 16
2.9 Nice Tree Decompositions ..... 18

[^0]3 Examples ..... 21
3.1 Treewidth ..... 21
3.2 Pathwidth ..... 21
3.3 Complemented Treewidth ..... 22
3.4 Tree Independence Number ..... 23
3.5 Hypergraph Treewidth ..... 25
3.6 Carmesin's Graph Decompositions ..... 27
3.7 Layered Treewidth ..... 28
3.8 H-Treewidth ..... 29
3.9 Bass-Serre Theory ..... 30
3.10 Hybrid Dynamical Systems ..... 33
4 Future Work ..... 33
A Categories of Graphs ..... 35
A. 1 Overview ..... 35
A. 2 Simple Graphs ..... 37
A. 3 Multigraphs ..... 42
A. 4 Hypergraphs ..... 44
References ..... 48

## 1 Introduction

Compositionality can be understood as the perspective that the semantics, structure or function of the whole should be given by that of its constituent parts [Sza22]. This principle has long shaped thinking in mathematics and computer science and indeed basic tools like recursion and divide-and-conquer algorithms themselves rely on compositional reasoning.

More recently, a strong research effort has concentrated around the systematic mathematical study of compositional systems and their occurrences in wider scientific domains [Fon16; Pol17; Cic19; Cou20; Mas21]. Thanks to these efforts, we can now make sense of how one might build graphs, Petri nets [BM20], chemical reaction networks [BP17], stock and flow diagrams [Bae+23] or epidemiological models [Lib+22] from smaller constituent parts. Ideally, we want versatile algorithms which consider the categorial and compositional structure of their inputs, and work generically across all these instances. Compositional algorithms at this level of generality don't yet exist. This article presents a starting point for their development, based upon a rich, well-established theory for computing on graphs.

The field of parameterized complexity supplies a number of established techniques for building compositional algorithms well-suited for particular combinatorial objects that exhibit certain compositional structure. The classes of relevant objects are often identified via so-called "width measures": numerical quantities originating from structural and algorithmic graph theory which roughly can be thought as measuring compositional complexity. Treewidth, the most well-known among these, measures roughly how much the global connectivity of a graph differs from that of a tree. The focus of the present paper is to develop a general theory of those width measures which arise from colimits.

Our article continues the work of [Bum21] and [BK23], of studying category-theoretic generalizations of treewidth. We do this by introducing structured decomposition categories (which we also refer to as sd-categories for convenience, c.f. Definition 2.5.1). These are categories $C$ equipped with a given family of diagrams all of whose colimits exist in $C$. The diagrams in
question, which we call structured decompositions ${ }^{1}$, are always of a specific type and roughly they can be understood as functorial ways of attaching data to combinatorial objects. This paper thus investigates which combinatorial invariants can be expressed as colimits: in a structured decomposition category one sees an object as being decomposed if it arises as a colimit of a structured decomposition. We equip sd-categories with additional structure that interacts nicely with structured decomposition diagrams, resulting in width categories (c.f. Definition 2.5.15).

Slightly more concretely, structured decompositions are special kinds of diagrams in some fixed category. The following is a generic example of what these diagrams look like.
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-03.jpg?height=213&width=611&top_left_y=717&top_left_x=726)

Intuitively, a structured decomposition is a way of assigning objects of a category to the vertices and edges of a graph. One starts with a graph $G$ and constructs a category $\int G$ as follows: $\int G$ has an object for each vertex of $G$ (blue dots in the diagram above), an object for each edge of $G$ (gold dots) and a span joining each edge to its source and target vertices ${ }^{2}$. Then structured decompositions are functors of the form $\int G \rightarrow C$ for some category $C$.

As we already mentioned, we view structured decompositions as generalizations of graph decompositions. In graph theory, decompositions often come equipped with a notion of width - a numerical quantity measuring the structural complexity of the pieces involved in the decomposition - which itself then induces an invariant on the graphs being decomposed. For instance, consider treewidth, a very important invariant in both graph structure theory (e.g. Robertson and Seymour's celebrated graph minor theorem [RS04]) and in parameterized complexity (e.g. Courcelle's famous algorithmic meta-theorem for bounded tree-width graphs [Cou90]): one says that a graph has treewidth at most $k$ if it admits a tree decomposition of width at most $k$. In the same spirit, if $\Gamma$ is a width category (c.f. Definition 2.5.15), we associate a corresponding notion of width, which we call $\Gamma$-width $\mathbf{w}_{\Gamma}(X)$, to each object $X \in \Gamma$.

Let us now summarize the results of this paper. In Section 2, we introduce the main categorical machinery we will use, namely sd-categories, width categories and sd-functors. In Proposition 2.5.18, we prove that $\Gamma$-width is monotone with respect to monomorphisms. In Proposition 2.7.5, we prove that if $F: \Gamma \rightarrow \Delta$ is a functor satisfying certain easy-to-check conditions (Definition 2.7.1), then $F$ cannot increase width (i.e. for every $X \in \Gamma, \mathbf{w}_{\Delta}(F(X)) \leq \mathbf{w}_{\Gamma}(X)$ ). Inspired by chordal completions of graphs, we also introduce a second width measure one can associate to a width category (chordal width), and in Theorem 2.6.7, we prove that chordal width and $\Gamma$-width agree for so-called complete width categories.

In Section 3, we prove that a large number of examples from the literature appear as particular instances of our framework. These include: 1. treewidth [BB72; Hal76; RS86] (Proposition 3.1.1), 2. complemented treewidth [DOS21] (Proposition 3.3.4), 3. tree independence number [DMŠ24] (Proposition 3.4.5), 4. hypergraph treewidth [Hei13] (Proposition 3.5.7), 5. layered treewidth [Sha15; DMW17] (Proposition 3.7.4) and 6. $\mathcal{H}$-treewidth [JKW22] (Proposition 3.8.4). We explore relationships between these width categories and obtain bounds between their $\Gamma$ widths (Corollaries 3.4.8, 3.4.14, 3.5.11).

Moreover, instances of our notion also turn up outside of combinatorial settings, When instantiated in the category of groups, structured decompositions coincide with 'graphs of groups', a concept developed in the 1970s and central to Bass-Serre theory [Ser70; Ser02; Bas93;

[^1]Hig76]. When dealing with manifolds and hybrid dynamical systems, structured decompositions appear independently under the name of "hybrid objects" in Ames' PhD thesis [Ame06]. We treat these notions in Section 3. The fact that the same formalism shows up in combinatorics, geometric group theory, and hybrid systems supports the need for a general theory of structured decompositions and width measures built from colimits: that is precisely the present contribution.

One should not expect all combinatorial decomposition methods to arise as colimits. Colimits have a strong topological flavor, and there are combinatorial decomposition methods such as clique-width decomposition trees [CER93; Cou96], and rank decompositions [OS06] which do not display this topological kind of compositionality. For instance clique-width decomposition trees are defined via a grammar which allows joining two graphs together by adding edges between them: it is unclear how such an operation could be naturally described as a colimit. Section 4 discusses the research problem of capturing these methods, along with other open questions. The appendix (Section A) treats the properties of several different categories of graphs and hypergraphs in detail.

### 1.1 Related Work

Recent efforts in graph theory have sought to generalize tree decompositions in two different ways. The first considers more general decomposition "shapes", such as cycle and planar decompositions; this is best exemplified by Carmesin's work on graph decompositions [Car22a; Die+22]. The second approach is to work with tree-shaped decompositions, but to allow for more complex "bags"; examples include $\mathscr{H}$-treewidth [JKW21] and layered treewidth [Sha15; DMW17]. Our notion of structured decompositions bridges and unifies both approaches, promising exciting new avenues of research at the intersection of categorial and combinatorial ideas.

There have been a few categorifications of treewidth in the literature so far; one of which is the starting point for the present paper. This is the notion of spined categories [Bum21; BK23], categories $C$ equipped with a so called proxy-pushout operation and a sequence $\Omega: \mathbb{N}_{=} \rightarrow C$ of objects called the spine. This paper originated as a generalization of spined categories to the case where the spine is filtration on the objects of $C$, rather than being a sequence. This change allows us to recover many more examples of combinatorial invariants.

Treewidth has also received categorical treatment through the notion of monoidal width. This was introduced by Di Lavore and Sobociński [DS23a; DS23b] and it measures the width of a morphism in a monoidal category ( $C, \otimes$ ). Instead of a spine $s: n \rightarrow C$, monoidal width is determined by a width function $w: \mathcal{A} \subset \operatorname{Mor} \mathcal{C} \rightarrow \mathbb{N}$ sending a subclass of atomic morphisms to natural numbers. There are two main differences between our approach and that of Di Lavore and Sobociński. Firstly, for monoidal width, the morphisms are being decomposed whereas in the the present structured decomposition approach we decompose the objects. Setting that aside, the only other difference is that the spine and width function are going in opposite directions. Indeed, a spine $s$ may be obtained from a width function $w$ by choosing $s(n) \in w^{-1}(n)$.

The idea that the treewidth - specifically - can be encoded by taking pushouts has already been noted by Blume et. al. [Blu+11]. Those authors define a cospan decomposition of a graph $H$ to be a sequence of connected cospans whose colimit is $H$. This notion is perhaps conceptually simpler than structured decompositions (indeed it is an instantiation, or a special case of our notion) but it is deployed only in the specific case of graphs and treewidth. In contrast, as we've already mentioned, our focus is one of developing a general theory that encapsulates many notions at once. Furthermore, a benefit of viewing combinatorial decompositions as diagrams, as we do, is that one can speak of morphisms between decompositions and functorial relationships between various notions of width.

More broadly, on the topic of diagrammatic reasoning, note that although mathematicians
have considered categories of diagrams (in the sense of Definition 2.4.1) since the beginnings of category theory [EM45], apart from a handful of examples [Koc67; Gui73; Gui74; GV77], interest in their study has waned over time, but has picked up recently [PT20; PT22; Pat+23]. Structured decompositions, being particular kinds of diagrams, assemble into a subcategory of the category of diagrams. This further justifies, independently of combinatorial consideration, a systematic study of the kinds of objects that can be built via colimits.

Finally we should point out that structured decompositions bear significant similarity to undirected wiring diagrams [Spi13]. These provide an operadic view on a construction which is very similar to what we would call FinSet-valued structured decompositions. Although it is beyond the scope of the article, investigating the connections between these two notions is a promising direction for further study.

### 1.2 Notation

We use the notation $\mathcal{C}, \mathscr{D}$ for generic categories and the bold font Set for named categories. We assume all categories are locally small, and we shall refer to those that have class-sized homsets as huge categories. We let Cat denote the category of small categories and CAT denote the huge category of categories. We let Set denote the category of sets and FinSet the full subcategory of finite sets. We fix a small skeleton for FinSet, and abuse notation by also calling that category FinSet. By a finite set, we then mean an object in this skeleton. This allows us to say that the class of all finite sets is a set. If $S$ is a set, then we let $P(S)$ denote the power set of $S$, i.e. the set of subsets of $S$, and we let $P_{\neq \varnothing}(S)$ denote the set of nonempty subsets of $S$.

### 1.3 Acknowledgements

We thank Karl Heuer, Reinhard Diestel, Bart Jansen, James Fairbanks, Elena Di Lavore, and Pawel Sobociński for their helpful conversations which aided in the development of this work. We are grateful to Will Turner for spotting a slight inaccuracy in a previous version of this article and for pointing out the connection to Bass-Serre theory. Furthermore we would like to thank Evan Patterson for suggesting to use the Grothendieck construction in the definition of structured decompositions; this has considerably simplified many of the technical arguments as well as the presentation of the paper. Finally we thank the anonymous reviewers for their constructive and detailed feedback.

## 2 Structured Decomposition Categories

In this section we first define structured decompositions, the main categorical tool we will use in this paper to study various notions of width in the literature. After this we define the central notions of this paper, sd-categories, $\Gamma$-width and sd-functors. We then review the classical notion of treewidth from graph theory.

### 2.1 The Category of Graphs

Graphs notions vary throughout the literature, depending on the context and application. In what follows, we consider what the $n L a b$ [nLa24] refers to as simple graphs, which have no loops and no multiple edges between the same pair of vertices. See Section A for a discussion of different categories of graphs.

Definition 2.1.1. A graph $G$ consists of the following data:

- a finite set $V(G)$ of vertices,
- a symmetric, irreflexive binary edge relation $E(G) \subseteq V(G)^{2}$.

A graph homomorphism $f: G \rightarrow H$ between the graphs $G$ and $H$ is a function $f: V(G) \rightarrow V(H)$ that preserves the edge relation: if $(x, y) \in E(G)$, then $(f(x), f(y)) \in E(H)$. Let $\mathbf{G r}$ denote the category whose objects are graphs, and whose morphisms are graph homomorphisms.

We will frequently abuse notation and write $x \in G$ to mean that $x \in V(G)$, and say that there is an edge $x y$ when $(x, y) \in E(G)$. Since the edge relation is symmetric, we will often identify an edge $x y$ with its symmetry class $\{x y, y x\}$.

The following classes of graphs will be used throughout.
Definition 2.1.2. The complete graph on $n$ vertices, also known as the $n$-clique, denoted $K^{n}$ is the graph with $V\left(K^{n}\right)=\{1,2, \ldots, n\}$ and where every pair of vertices are connected by an edge. By convention we take $K^{0}=\varnothing$.

![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-06.jpg?height=149&width=1040&top_left_y=868&top_left_x=516)
Figure 1: The first four nonempty complete graphs.

The $n$-cycle $C^{n}$ is a graph with $n$-many vertices $\{1, \ldots, n\}$ where there is an edge between $i$ and $j$ if and only if $j=i+1$ for $1 \leq i \leq n-1$ or $i=n$ and $j=1$. A circuit of length $n$ in a graph $G$ is a morphism $f: C^{n} \rightarrow G$, which we commonly denote by the image of the vertices $\{f(1), f(2), \ldots, f(n)\}$. An $n$-cycle in a graph $G$ is a graph homomorphism $f: C^{n} \rightarrow G$, injective on vertices and edges, for some $n \geq 3$.

Let $P^{n}$ denote the graph with $V\left(P^{n}\right)=\{1, \ldots, n\}$ and such that $i$ and $j$ are adjacent if and only if $|j-i|=1$. We call $P^{n}$ an $n$-path. Let Paths denote the set of all $n$-paths for $n \geq 0$. Given $x, y \in V(G)$, a path connecting $x$ to $y$ in $G$ is a graph homomorphism $f: P^{n} \rightarrow G$, injective on vertices and edges, such that $f(1)=x$ and $f(n)=y$ for some $n \geq 1$. We say that a graph is connected if any two of its vertices have a path connecting them. We say a graph is a tree if it is connected and has no cycles. We let Trees denote the set of all trees.

### 2.2 Barycentric Subdivision

Definition 2.2.1. Consider a graph $G$. The barycentric subdivision $\int G$ of $G$ is the category which has as

- objects: all the vertices of $G$ (vertex objects) and all symmetry classes of edges of $G$ (edge objects)
- morphisms: identity morphisms for each object, and two morphisms $e_{x}: e \rightarrow x$ and $e_{y}: e \rightarrow x$ for each edge object $e=x y$.

Note that composition in $\int G$ is trivial, since one of the morphisms in each composable pair is an identity morphism.

Example 2.2.2. The barycentric subdivision of the graph $G$ on the left yields the category $\int G$ on the right.
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-06.jpg?height=184&width=186&top_left_y=2437&top_left_x=667)
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-06.jpg?height=188&width=369&top_left_y=2437&top_left_x=1032)

### 2.3 Structured Decompositions

Definition 2.3.1. Given a category $C$ and a graph $G$, a $G$-structured decomposition is a functor $d: \int G \rightarrow C$ such that the image of each morphism in $\int G$ is a monomorphism in $C$. We call

- images $d(v)$ of vertex objects $v \in \int G$ the bags,
- images $d(e)$ of edge objects $e \in \int G$ the adhesions,
- spans of the form $d\left(v_{1}\right) \hookleftarrow d(e) \hookrightarrow d\left(v_{2}\right)$ the adhesion-spans indexed by the edge object $e$.

Example 2.3.2. For $C=$ FinSet and $G$ a graph as below left, we have a structured decomposition below right.
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-07.jpg?height=321&width=467&top_left_y=815&top_left_x=255)
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-07.jpg?height=327&width=1034&top_left_y=813&top_left_x=833)

Definition 2.3.3. Take a category $C$, a graph $G$, an object $X \in C$, and a structured decomposition $d: \int G \rightarrow C$. If $X \cong \operatorname{colim} d$, we say that $d$ is a structured decomposition of the object $X$.

As a shorthand, we sometimes refer to structured decompositions of an object $X$ simply as decompositions of $X$.

Example 2.3.4. The structured decomposition of Example 2.3.2 is a structured decomposition of the finite set $\{1,2,3,4,3 / 2, \pi, \sqrt{2}, 10,11\}$.

### 2.4 Grothendieck Construction

Definition 2.4.1. Given a category $C$, let $\mathbf{D i a g}(C)$ denote the category whose objects are (small) diagrams $d: I \rightarrow C$ and for two diagrams $d: I \rightarrow C$ and $d^{\prime}: I^{\prime} \rightarrow C$, a morphism $A: d \rightarrow d^{\prime}$ in Diag( $e$ ) consists of a functor $a: I \rightarrow I^{\prime}$ and a natural transformation $\alpha: d \Rightarrow A d^{\prime}$
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-07.jpg?height=170&width=332&top_left_y=1829&top_left_x=868)

We call this the diagram category ${ }^{3}$ of $C$. Given a functor $F: C \rightarrow D$, we obtain a functor $\boldsymbol{\operatorname { D i a g }}(F): \boldsymbol{\operatorname { D i a g }}(\mathcal{C}) \rightarrow \boldsymbol{\operatorname { D i a g }}(\mathscr{D})$ by postcomposing diagrams with $F$ and by sending a natural transformation as below left to the whiskered natural transformation as below right.
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-07.jpg?height=168&width=333&top_left_y=2229&top_left_x=641)
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-07.jpg?height=173&width=339&top_left_y=2224&top_left_x=1085)

Thus we obtain a functor Diag : CAT → CAT. We let $\mathfrak{D}(\mathcal{C})$ denote the full subcategory of $\boldsymbol{\operatorname { D i a g }}(\mathcal{C})$ whose objects are structured decompositions in $\mathcal{C}$. If $\mathscr{C}_{j}$ is a set of graphs, then we let $\mathfrak{D}_{\mathscr{G}}(e)$ denote the full subcategory of the $\mathscr{G}_{\text {-structured decompositions. If } X \in C \text {, then we let }} \mathfrak{D}_{\mathscr{L}}(C, X)$ denote the full subcategory on $\mathscr{G}_{\mathscr{L}}$-structured decompositions of $X$.

[^2]Remark 2.4.2. In later sections, we will allow for more general notions of graphs, in which case our notion of graph above will be a special case. If $G$ is a multigraph (Definition A.1.7), then let $\int G$ denote the category defined just as above, but now with a span $x \leftarrow e \rightarrow y$ for each of the multiple possible edges between $x$ and $y$. This construction is functorial, and we use the notation $\int: \mathbf{G r}_{\text {mlt }} \rightarrow$ Cat for the resulting functor. We note that for a loop, we define its image in the barycentric subdivision to be a span $x \leftarrow e \rightarrow x$. By the full subcategory inclusions $\mathbf{G r}, \mathbf{G r}_{\ell}, \mathbf{G r}_{r} \hookrightarrow \mathbf{G r}_{\text {mlt }}$, we can also index structured decompositions using any of the kinds of undirected graphs considered in Section A.1.

We can also index structured decompositions using digraphs (Definition A.1.1). If $G$ is a digraph, equivalently a functor $G: \mathbf{d G r S c h} \rightarrow$ Set, then $\int G$ is precisely the category of elements or Grothendieck construction ${ }^{4}$ of $G$. We note that if $G$ is a digraph, and $U(G)$ denotes its underlying undirected multigraph, then there is an isomorphism of categories $\int G \cong \int U(G)$. Furthermore and generalizing the case of digraphs, one can clearly also index structured decompositions by objects of any category of presheaves or C-sets (e.g. Petri nets, simplicial sets, etc.). We will not be considering structured decompositions whose shapes are not graphs in the present paper; but we simply point out this possibility for completeness.

Let cst : $C \rightarrow \mathfrak{D}(C)$ denote the constant diagram functor, which sends an object $X \in C$ to the structured decomposition of $X$ given by the functor $X:\left(\mathbf{1} \cong \int \bullet\right) \rightarrow C$ that sends the single object of the terminal category $\mathbf{1}$ to $X$.

To conclude this section, let us characterize the category of structured decompositions in Set. Consider the (strict) functor $J: \mathbf{G r}^{\mathrm{op}} \rightarrow$ Cat defined as:

$$
\begin{aligned}
J: \mathbf{G r}^{\mathrm{op}} & \rightarrow \text { Cat } \\
G & \mapsto \text { Set }^{\int G} \\
(G \xrightarrow{f} H) & \mapsto\left(\text { Set }^{\int H} \xrightarrow{\text { Set }^{f f}} \text { Set }^{\int G}\right) .
\end{aligned}
$$

Taking the Grothendieck construction [JY21, Chapter 10] of this functor, we obtain a Grothendieck fibration $\pi: \int J \rightarrow \mathbf{G r}^{\mathrm{op}}$, where $\int J$ is the category whose objects are pairs ( $G, d: \int G \rightarrow$ Set) and whose morphisms are pairs $\left(f: G \rightarrow H, \eta: d \Rightarrow\left(d^{\prime} \circ \int f\right)\right.$ ), i.e. diagrams of the form
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-08.jpg?height=204&width=433&top_left_y=1722&top_left_x=817)

We recognize this as precisely the category of structured decompositions in Set.
Lemma 2.4.3. There is an isomorphism of categories

$$
\mathfrak{D}(\mathbf{S e t}) \cong \int J .
$$

### 2.5 Width Categories

In prior work, the first two of the authors introduced the formalism of spined categories [BK23] to give a uniform account of several width notions in the graph theory literature, including treewidth, co-treewidth, and hypergraph treewidth. One can regard the definitions below as advancing this formalism by generalizing the spine category and requiring actual colimits rather than proxy pushouts. This allows us to capture a larger variety of examples from the literature.

[^3]Definition 2.5.1. A structured decomposition category or sd-category $\Gamma=(\mathcal{C}, \mathcal{G})$ consists of a small category $\mathcal{C}$ equipped with a set $\mathscr{G}_{\text {g }}$ of graphs ${ }^{5}$ containing the graph • called the index set such that
(W1) for every structured decomposition $d: \int G \rightarrow C$, with $G \in \mathcal{L}_{\mathcal{L}}$, the colimit of $d$ exists in e.

We now need some additional structure on an sd-category with which we can use to obtain some notion of "size" of an object in the category.

Definition 2.5.2. A spined sd-category $\Gamma=(\mathcal{C}, \mathcal{C}, \Omega)$ consists of an sd-category ( $\mathcal{C}, \mathcal{C}_{\mathcal{L}}$ ), equipped with a filtered essentially full subcategory ${ }^{6}$ called the spine. By filtered we mean $\Omega$ is equipped with a filtration $\Omega_{0} \subseteq \Omega_{1} \subseteq \ldots \subseteq \Omega$ of essentially full subcategories of the spine with

$$
\Omega=\bigcup_{n \geq 0} \Omega_{n}
$$

such that
(W2a) for every object $X \in C$ there is a monomorphism $X \hookrightarrow W$ for some $W \in \Omega$, and
(W2b) for every $n \geq 1$ and $W \in\left(\Omega_{n} \backslash \Omega_{n-1}\right)$, there exists no monomorphism $W \hookrightarrow W^{\prime}$ into any $W^{\prime} \in \Omega_{n-1}$.

We write (W2) to mean the logical conjunction $(\mathbf{W 2})=(\mathbf{W 2 a}) \wedge(\mathbf{W 2 b})$. We say an object $W \in C$ is complete if $W \in \Omega$. If each $\Omega_{n} \backslash \Omega_{n-1}$ is a singleton $\left\{W_{n}\right\}$, then we will often write $\Omega$ as $\left\{W_{n}\right\}_{n \geq 0}$. We may also write $\Omega=\left\{W_{i}\right\}_{i \in I}$ if $I$ is a convenient indexing set.

Remark 2.5.3. The main difference between spined sd-categories and the spined categories of [BK23] is that the latter's notion of spine only allows for $\left(\Omega_{n} \backslash \Omega_{n-1}\right)$ to be a singleton, and our notion requires certain kinds of colimits rather than proxy pushouts.

Definition 2.5.4. Given a spined sd-category $\Gamma=(\mathcal{C}, \mathcal{C}, \Omega)$, let $s: \operatorname{Obj}(\mathcal{C}) \rightarrow \mathbb{N}$ be the function, which we call the size function of $\Gamma$, defined as follows. Given $X \in C$, we say that the size $s(X)$ of $X$ is $n$ if $\Omega_{n}$ is the smallest full subcategory of $\Omega$ such that there exists a monomorphism $X \hookrightarrow W$ with $W \in \Omega_{n}$.

Lemma 2.5.5. If $\Gamma=(\mathcal{C}, \mathcal{C}, \Omega)$ is a spined sd-category and $f: X \hookrightarrow Y$ is a monomorphism in $C$, then $s(X) \leq s(Y)$.

Proof. If $Y \hookrightarrow W$ is monic with $W \in \Omega$, then the composite $X \hookrightarrow Y \hookrightarrow W$ is monic and witnesses $s(X) \leq s(Y)$.

Remark 2.5.6. By Lemma 2.5.5 say that the size $s$ of a spined sd-category $\Gamma$ is monotonic with respect to monomorphisms.

Definition 2.5.7. Given a spined sd-category $\Gamma=(\mathcal{C}, \mathcal{G}, \Omega)$, an object $X \in C$, and a $\mathcal{C}_{\mathcal{I}}$-structured decomposition $d: \int G \rightarrow C$ of $X$, we define the width $w(d)$ of the decomposition to be the maximal size of all of its bags minus 1 ,

$$
w(d)=\max _{x \in V(G)} s(d(x))-1
$$

We say that a $\mathcal{C}_{\mathcal{L}}$-structured decomposition $d$ of $X$ is minimum, if $w(d) \leq w\left(d^{\prime}\right)$ for all other $\mathcal{G}_{j}$-structured decompositions $d^{\prime}$ of $X$.

[^4]Given an object $X \in C$ we say that its $\Gamma$-width - written $\mathbf{w}_{\Gamma}(X)$ - is the width of any one of its minimum decompositions, or equivalently:

$$
\mathbf{w}_{\Gamma}(X)=\min _{d \in \mathfrak{D}_{\mathscr{L}}(\ell, X)} w(d)
$$

If the ambient sd-category $\Gamma$ is clear from context, then we will refer to the $\Gamma$-width of an object $X$ simply as its width.

Example 2.5.8. If we take $\Gamma=\left(\mathbf{G r}\right.$, Trees, $\left.\left\{K^{n}\right\}_{n \geq 0}\right)$, (see Definition 2.1.2) and if $G \in \mathbf{G r}$, then the $\Gamma$-width of $G$ is precisely its treewidth. We will prove this later: see Proposition 3.1.1.

Example 2.5.9. The poset $(\mathbb{N}, \leq)$ of the natural numbers forms a spined sd-category of the form $\Gamma=\left((\mathbb{N}, \leq)\right.$, Graphs, $\left.\{n\}_{n \geq 0}\right)$. The colimit of a finite diagram here is the maximum, hence any structured decomposition $d$ of an object $n$ must include $n$ as a bag $d(x)$, and furthermore this must be an object of maximal size in the decomposition. Hence the $\Gamma$-width of any number $n$ is $n-1$.

Lemma 2.5.10. Given a spined sd-category $\Gamma=(\mathcal{C}, \mathcal{G}, \Omega)$ and an object $X \in C$,

$$
\mathbf{w}_{\Gamma}(X) \leq s(X)-1
$$

Proof. Given any $X \in C$, the $\mathcal{G}_{\text {g }}$-structured decomposition $d: \int \bullet \rightarrow C$ that picks out $X$ has width $s(X)-1$.

Definition 2.5.11. If $\Gamma=(\mathcal{C}, \mathcal{C})$ is an sd-category, and $\mathscr{F}$ is a pullback-stable ${ }^{7}$ class of morphisms in $C$, then we say that $\Gamma$ is $\mathcal{F}$-stable if it additionally satisfies
(W3) the pullback $f^{*}(d)$ of the colimit cocone of any $\mathcal{G}_{g}$-structured decomposition $d$ of an object $Y$ along a morphism $f: X \rightarrow Y$ with $f \in \mathscr{F}$ exists and is a colimit cocone of $X$.

We say that $\Gamma$ is stable if it is $\operatorname{Mor}(\mathcal{C})$-stable, and monic-stable if it is $\operatorname{Mono}(\mathcal{C})$-stable.
Remark 2.5.12. The condition (W3) is a special case of having universal or pullback-stable colimits. More precisely, given a category $C$ with pullbacks, suppose that $\mathscr{I}$ is a class of (small) diagrams $d: I \rightarrow C$ whose colimit exists in $C$. We say that $C$ has universal $I$-colimits if pulling back a colimit cocone of a diagram $d \in \mathscr{I}$ over an object $Y$ along an arbitrary map $f: X \rightarrow Y$ is a colimit cocone over $X$.

We say that a category has universal colimits if it has universal $\mathscr{I}$-colimits for $\mathscr{I}$ the class of all small diagrams. Every locally cartesian closed category has universal colimits. The class of locally cartesian closed categories includes quasitoposes and toposes. Given a set $\mathscr{C}_{\text {g }}$ of graphs, we say that a category $\mathcal{C}$ has universal $\mathscr{G}$-colimits, if it has universal $\mathscr{I}$-colimits, where $\mathscr{I}$ is the
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-10.jpg?height=54&width=1232&top_left_y=2060&top_left_x=242)

We repackage the above remark with the following lemma.
Lemma 2.5.13. Suppose that $\mathscr{I}$ is a class of (small) diagrams and $C$ is a category with pullbacks and universal $\mathscr{I}$-colimits. By choosing representatives for every pullback, one obtains a welldefined presheaf

$$
\mathrm{Dgm}_{\mathscr{J}}: e^{\mathrm{op}} \rightarrow \text { Set }
$$

where for $X \in C, \operatorname{Dgm}_{\mathscr{J}}(X)$ is the set of diagrams $d: I \rightarrow C$ in $\mathscr{I}$ equipped with a colimit cocone $\sigma: d \Rightarrow \Delta(X)$. Given a map $f: X \rightarrow Y$ in $C, \operatorname{Dgm}_{\mathscr{J}}(f)$ is the function that takes a colimit cocone $\sigma$ over $Y$ to its pullback $f^{*}(\sigma)$ over $X$.

[^5]Example 2.5.14. Any finitely complete, cocomplete and locally cartesian closed category $C$ is a stable spined sd-category if we set $\Omega_{0}=\varnothing, \Omega_{1}=\cdots=\Omega=C$ and $\mathscr{G}=$ Graphs. In this case all objects then have width 0 .

We now single out the class of spined sd-categories that are monic-stable. These are the kinds of sd-categories that are well-behaved and appear most frequently in examples.

Definition 2.5.15. We call a spined sd-category $\Gamma=(\mathcal{C}, \mathcal{L}, \Omega)$ a width category if it is monicstable.

Example 2.5.16. The main example of a width category for us is ( $\mathbf{G r}$, Trees, $\left\{K^{n}\right\}_{n \geq 0}$ ). We prove that this is indeed a width category in Proposition 3.1.1.

However we note that the size and width of even a complete object can have arbitrarily large difference.

Example 2.5.17. The category of finite sets forms a width category (FinSet, Paths, $\{\underline{n}\}_{n \geq 0}$ ), where $\underline{n}=\{1,2, \ldots, n\}$. The size of a finite set is its cardinality, but the width of $\underline{1}$ is clearly 0 , and the width of every other finite set is 1 , because we can always obtain a Paths-structured decomposition of $\underline{n}$ of the form
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-11.jpg?height=186&width=1289&top_left_y=1133&top_left_x=388)

Proposition 2.5.18. Given a width category $\Gamma=(\mathcal{C}, \mathcal{G}, \Omega)$, if $f: X \hookrightarrow Y$ is monic, then

$$
\mathbf{w}_{\Gamma}(X) \leq \mathbf{w}_{\Gamma}(Y) .
$$

Proof. Suppose that $d: \int G \rightarrow C$ is a $\mathcal{C}_{\mathcal{I}}$-structured decomposition of $Y$ of minimal width. So $w(d)=\mathbf{w}_{\Gamma}(Y)$. Then since $\Gamma$ is monic-stable, $f^{*}(d)$ is a $\mathscr{C}_{j}$-structured decomposition of $X$ and since monomorphisms are stable under pullback, we obtain monomorphisms $f^{*}(d)(x) \hookrightarrow d(x)$ between the bags for every $x \in V(G)$. So by Lemma 2.5.5, $s\left(f^{*}(d)(x)\right) \leq s(d(x))$ for all $x \in V(G)$. Thus $w\left(f^{*}(d)\right) \leq w(d)=\mathbf{w}_{\Gamma}(Y)$, and therefore $\mathbf{w}_{\Gamma}(X) \leq \mathbf{w}_{\Gamma}(Y)$. $\square$

Remark 2.5.19. Observe that the definition of a spined sd-category (Definition 2.5.2) forces every object to have a finite size. This is actually not due to mathematical necessity, but purely a stylistic choice. The reader can verify that, by considering ordinal-indexed filtrations as the spine and by changing the definition of width (Definition 2.5.7) to simply be the maximum bag size (i.e. removing the minus one), one obtains a theory of spined sd-categories that does not impose any finiteness conditions on bags of decompositions. These considerations, although relevant to tree-width of infinite graphs, will not be further addressed in the present contribution.

### 2.6 Chordal Completions

Let us now introduce a competing notion of width for width categories, using Lemma 2.8.12 as our motivation.

Definition 2.6.1. Given a spined sd-category $\Gamma=(\mathcal{C}, \mathcal{G}, \Omega)$, if $d: \int G \rightarrow C$ is a $\mathcal{C}_{\mathcal{L}}$-structured decomposition such that each of its bags $d(x)$ belong to $\Omega$, then we say that $d$ is a $(\mathcal{L}, \Omega)$ structured decomposition. We let $\mathfrak{D}_{(\mathscr{L}, \Omega)}(e)$ and $\mathfrak{D}_{(\mathscr{L}, \Omega)}(e, X)$ denote the full subcategories of ( $\mathcal{G}, \Omega$ )-structured decompositions in $C$ and of an object $X \in C$ respectively.

A chordal object is an object $Y \in C$ which is the colimit of a $\left(\mathscr{C}_{,} \Omega\right)$-structured decomposition. The $(\mathcal{G}, \Omega)$-width $w_{(\mathcal{G}, \Omega)}(d)$ of a $(\mathcal{L}, \Omega)$-decomposition $d$ of $Y$ is $n-1$ if $\Omega_{n}$ is the smallest
full subcategory that the bags of $d$ are objects of. The $\left(\mathcal{G}_{\mathcal{J}}, \Omega\right)$-width $\mathbf{w}_{(\mathcal{G}, \Omega)}(Y)$ of a chordal object $Y$ is the minimal ( $\mathcal{G}, \Omega$ )-width of all of its ( $\mathcal{G}, \Omega$ )-decompositions.

A chordal completion of an object $X$ is a monomorphism $i: X \hookrightarrow Y$ where $Y$ is chordal. We define the chordal $\Gamma$-width of an object $X$, $\operatorname{denoted} \mathbf{c w}_{\Gamma}(X)$, to be the minimal ( $\mathcal{G}, \Omega$ )-width of every chordal completion of $X$. When $\Gamma$ is clear from context, we may refer to chordal $\Gamma$-width simply as chordal width.

Remark 2.6.2. We note that $\left(\mathscr{L}^{\circ}, \Omega\right)$-width $\mathbf{w}_{(\mathscr{G}, \Omega)}(Y)$ is only defined for chordal objects $Y$ in a spined sd-category. We will see in Section 3.9 that even though $(\mathcal{L}, \Omega)$-width is not defined for all objects, it can still be a useful width measure in categories where monomorphisms don't behave like they do in $\mathbf{G r}$.

Remark 2.6.3. Given a width category $\Gamma=(\mathcal{C}, \mathcal{C}, \Omega)$, an object $Y \in C$ is chordal if and only if it is in the essential image of the left Kan extension
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-12.jpg?height=193&width=321&top_left_y=895&top_left_x=872)

Now given a width category $\Gamma=(\mathcal{C}, \mathcal{G}, \Omega)$, and $X \in C$, suppose that $f: X \hookrightarrow Y$ is a chordal completion of an object $X$. Then by definition there is a $(\mathcal{G}, \Omega)$-structured decomposition $d: \int G \rightarrow C$ of $Y$, and we can pull back this decomposition along $f$ to get a $\mathscr{C}_{\text {- }}$-structured decomposition $f^{*}(d)$ of $X$. Furthermore we obtain a morphism of structured decompositions
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-12.jpg?height=177&width=396&top_left_y=1347&top_left_x=836)
given by mapping each component along the pullback maps.
Conversely, given a $\mathcal{C}_{\mathcal{I}}$-structured decomposition $d$ of an object $X$, by ( $\mathbf{W 2}$ ) there exists a monomorphism $d(x) \hookrightarrow W_{x}$ for each bag of the decomposition, and so we can consider the $\mathscr{G}_{-}$ structured decomposition $d^{\prime}$ obtained by replacing each bag $d(x)$ by their corresponding object $W_{x}$ and the adhesion maps $d(e) \hookrightarrow d(x)$ by the composite morphisms $d(e) \hookrightarrow W_{x}$. We call this completing the $\mathcal{G}_{\mathcal{L}}$-structured decomposition $d$. In more detail we have the following.

Definition 2.6.4. Let $\Gamma=(\mathcal{C}, \mathcal{G}, \Omega)$ be a width category with $X \in C$ and let $d: \int G \rightarrow C$ be a $\mathcal{G}_{\mathcal{I}}$ structured decomposition of $X$. Suppose that $d^{\prime}: \int G \rightarrow C$ is a diagram of the same shape. We say that a natural transformation $\alpha: d \Rightarrow d^{\prime}$ is a completion of $d$ if each bag in $d^{\prime}$ is a complete object of $C$, each component map $\alpha_{e}: d(e) \rightarrow d^{\prime}(e)$ between the adhesions is an identity map, and the component maps $\alpha_{x}: d(x) \rightarrow d^{\prime}(x)$ between the bags are monomorphisms.

If we let $Y$ denote the colimit of $d^{\prime}$, then we obtain an induced map $f: X \rightarrow Y$ on the colimits. If the maps $d(x) \hookrightarrow W_{x}$ are minimal in the sense that $d(x)$ does not have a monomorphism to a complete object of size strictly smaller than the size of $W_{x}$, then we say that the completion $d^{\prime}$ is minimal.

We wish to be able to go between $\mathcal{C}_{\mathcal{J}}$-structured decompositions and chordal completions of objects, as is the case with Lemma 2.8.12.

However, there is no reason why the map $f: X \rightarrow Y$ one obtains by completing a $\mathcal{G}_{\text {- }}$ structured decomposition will be a monomorphism. In order to get this correspondence to behave correctly, we ask for a stronger property from our width categories.

Definition 2.6.5. We say that a width category $\Gamma=(\mathcal{C}, \mathcal{C}, \Omega)$ is complete ${ }^{8}$ if

[^6](W4) for every completion $\alpha: d \Rightarrow d^{\prime}$ of a $\mathscr{G}_{\text {- }}$-structured decomposition $d$, the induced map $f: X \rightarrow Y$ between their colimits is a monomorphism.

Adhesive categories are categories where pushouts are particularly well behaved [LS04]. Many familiar categories of combinatorial data are adhesive, including all presheaf categories. The following result establishes a connection between such categories and complete width categories defined thereupon.

Proposition 2.6.6. Let $\Gamma=(C$, Trees, $\Omega)$ be a width category. If $C$ is adhesive, then $\Gamma$ is complete.
Proof. Let $\delta: \int T \rightarrow C$ denote a completion of any given tree-shaped structured decomposition $d: \int T \rightarrow C$. Our argument proceeds by induction on the edges of $T$. If $T$ has no edges, the claim is trivially true since the only completion arrow is also the colimit arrow.

For the inductive step, consider an edge $e=x y$ of $T$ which splits $T$ into two subtrees $T_{1}$ and $T_{2}$. By the induction hypothesis, there are monomorphisms

$$
g_{i}: \operatorname{colim}\left(\int T_{i} \hookrightarrow \int T \xrightarrow{d} C\right) \hookrightarrow \operatorname{colim}\left(\int T_{i} \hookrightarrow \int T \xrightarrow{\delta} C\right) \text { where } i \in\{1,2\} .
$$

Since colimits of tree-shaped decompositions can be computed recursively (one pushout at a time, for each adhesion span) it suffices to show that the dashed puhout arrow in the comutative cube shown below is monic.
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-13.jpg?height=574&width=1357&top_left_y=1247&top_left_x=354)

To that end, observe that the top and bottom faces of the above cube are pushouts (by construction) and that the back faces must necessarily be pullbacks since the adhesion spans of the completion $\delta$ are constructed by composition. Thus, since $C$ is adhesive, the previous observations amount to saying that the above cube in van Kampen [LS04, Definition 2.1] and hence the front faces are pushouts. This concludes the proof since, $C$ being adhesive, pushout squares of monomorphisms are also van Kampen (by definition) and hence preserve monormophisms [LS04, Lemma 2.3]. $\square$

It now follows immediately that if ( $\mathcal{C}, \mathcal{G}, \Omega$ ) is a complete width category, and $d: \int G \rightarrow C$ is a $\mathscr{C}_{\mathcal{L}}$-structured decomposition of an object $X$, then completing $d$ results in a $\left(\mathscr{C}_{\mathcal{L}}, \Omega\right)$-structured decomposition $d^{\prime}$ and by taking colimits, we obtain a chordal completion $i: X \hookrightarrow Y$. Conversely, if we have a chordal completion $i: X \hookrightarrow Y$, then by definition $Y$ has a $(\mathcal{G}, \Omega)$-structured decomposition $d$, and pulling back along $i$ we obtain a decomposition $i^{*}(d)$ of $X$.

However, unlike with Lemma 2.8.11, there is no canonical choice for how to complete a structured decomposition. However, every chordal completion does arise from a $\mathscr{C}_{\text {- }}$-structured decomposition. Indeed if $i: X \hookrightarrow Y$ is a chordal completion, then if we pull back any decomposition $d$ of $Y$, we get a decomposition, $i^{*}(d)$, and the colimit of the map $i^{*}(d) \Rightarrow d$ is isomorphic to the completion $i$. Furthermore, we have the following result, generalizing Lemma 2.8.12.

Theorem 2.6.7. Given a complete width category $\Gamma=(\mathcal{C}, \mathcal{G}, \Omega)$ with $X \in C$, we have

$$
\mathbf{w}_{\Gamma}(X)=\mathbf{c w}_{\Gamma}(X) .
$$

Proof. Suppose that $d_{0}: \int G \rightarrow C$ is a minimal $\mathcal{G}_{\text {f }}$-structured decomposition of $X$, in the sense that it has the smallest possible size of all $\mathscr{C}_{\mathcal{I}}$-structure decompositions of $X$. Then by the discussion above, we can obtain a minimal completion $d_{0}^{\prime}: \int G \rightarrow C$ of $d_{0}$, whose colimit we denote $Y$. This provides a chordal completion $f: X \hookrightarrow Y$. Since $d_{0}^{\prime}$ is a minimal completion of $d_{0}$, this means that $w\left(d_{0}\right)=w_{\left(\mathscr{L}_{\mathcal{L}, \Omega}\right)}\left(d_{0}^{\prime}\right)$. Since $\mathbf{w}_{\left(\mathscr{L}_{\mathcal{L}, \Omega}\right)}(Y) \leq w_{\left(\mathscr{L}_{\mathcal{L}, \Omega}\right)}\left(d_{0}^{\prime}\right)$, we have that $\mathbf{w}_{(\mathscr{L}, \Omega)}(Y) \leq w\left(d_{0}\right)$.

But since $Y$ is chordal, then there exists a $(\mathcal{L}, \Omega)$-decomposition $d_{1}^{\prime}$ that achieves its width $\mathbf{w}_{(\mathcal{G}, \Omega)}(Y)$. By pulling this decomposition back, we obtain a decomposition $d_{1}$ of $X$. By definition of the width of $d_{1}$, we have $w\left(d_{1}\right) \leq w\left(d_{1}^{\prime}\right)=\mathbf{w}_{(\mathscr{C}, \Omega)}(Y)$. But $w\left(d_{0}\right) \leq w\left(d_{1}\right)$, since we assumed that $d_{0}$ is minimal. Hence $\mathbf{w}_{\Gamma}(X)=w\left(d_{0}\right)=\mathbf{w}_{(\mathscr{C}, \Omega)}(Y)$. Therefore $\mathbf{w}_{\Gamma}(X) \geq \mathbf{c w}_{\Gamma}(X)$.

Now suppose that $f: X \rightarrow Y^{\prime}$ is a minimal chordal completion of $X$, so that $\mathbf{c w}_{\Gamma}(X)= \mathbf{w}_{(\mathcal{G}, \Omega)}\left(Y^{\prime}\right)$. Then if we pull back a minimal decomposition $d_{2}^{\prime}$ of $Y^{\prime}$, i.e. $w_{(\mathcal{G}, \Omega)}\left(d_{2}^{\prime}\right)=\mathbf{w}_{(\mathcal{G}, \Omega)}\left(Y^{\prime}\right)$, we obtain a decomposition $d_{2}$ of $X$ such that $w\left(d_{2}\right) \leq \mathbf{w}_{(\mathscr{L}, \Omega)}\left(Y^{\prime}\right)$. Then we have

$$
\mathbf{w}_{\Gamma}(X) \leq w\left(d_{2}\right) \leq \mathbf{w}_{(\mathscr{L}, \Omega)}\left(Y^{\prime}\right)=\mathbf{c w}_{\Gamma}(X) .
$$

Thus the $\Gamma$-width and chordal $\Gamma$-width of $X$ agree.
Although it is beyond the scope of the current paper, Theorem 2.6.7 is particularly relevant to algorithmic applications of structured decompositions. To see this, we will briefly recall why chordal completions are useful when dealing with graphs and their tree decompositions. In algorithmic applications [FG06; Cyg+15; CE12; Gro17] one is not only interested in knowing whether a given graph or structure has bounded treewidth, say, but instead one is interested in algorithms that, given an input graph $G$, will compute a decomposition of $G$ of small width. The most famous such algorithm is due to Bodlaender and Kloks [BK96] (see Althaus and Ziegler for a simplified exposition [AZ21]) which builds on Perković and Reed's earlier algorithm [PR00]. This algorithm is an FPT-time algorithm parameterized by treewidth which decides whether a given graph has treewidth at most $k$ (and outputs such a decomposition, if it exists). However, due to being fairly complicated to implement, in practice approximation or heuristic methods are often preferred. For these methods one usually relies on finding a chordal completion of the graph. These approaches usually build upon Bouchitté and Todinca's exact algorithm [BT01; KBJ19] by imposing various vertex ordering schemes for computing a chordal completion [TY84; RTL76; CM69; Ber+04].

## 2.7 sd-Functors

We now define functors between sd-categories. Far from routine, pinning down the right notion requires considerable care: we use the data in the sd-category to define permitted structured decompositions, but we need functors not just to preserve the data, but to send decompositions to decompositions in the appropriate sense.

Definition 2.7.1. Given spined sd-categories $\Gamma=(\mathcal{C}, \mathcal{G}, \Omega)$ and $\Gamma^{\prime}=\left(\mathcal{C}^{\prime}, \mathcal{G}^{\prime}, \Omega^{\prime}\right)$, an sd-functor $F: \Gamma \rightarrow \Gamma^{\prime}$ consists of

- a functor $F: C \rightarrow C^{\prime}$,
- a function $F_{g}: \mathscr{G}^{-} \mathscr{G}^{\prime}$,
- for each $G \in \mathscr{G}_{\text {f }}$ a functor $F_{G}: \int F_{g}(G) \rightarrow \int G$
such that
- $F$ is size-nonincreasing, in the sense that for any object $X \in C, s^{\prime}(F(X)) \leq s(X)$, and
- given a structured decomposition $d: \int G \rightarrow C$ of an object $X$ in $C$, the composite

$$
\int F_{g}(G) \xrightarrow{F_{G}} \int G \xrightarrow{d} C \xrightarrow{F} C^{\prime}
$$

which we denote $F_{*}(d): \int F_{g}(G) \rightarrow C^{\prime}$ is a structured decomposition of $F(X)$ in $C^{\prime}$.
Intuitively, the intermediate functors $F_{G}$ of Definition 2.7.1 serve to track how each structured decomposition transforms as we change the structure graph. Their presence introduces some nuance into the definition of composition for sd-functors.

Definition 2.7.2. Given sd-functors $(\mathcal{C}, \mathcal{G}, \Omega) \xrightarrow{A}\left(\mathcal{C}^{\prime}, \mathcal{G}^{\prime}, \Omega^{\prime}\right) \xrightarrow{B}\left(\mathcal{C}^{\prime \prime}, \mathcal{G}^{\prime \prime}, \Omega^{\prime \prime}\right)$ we define their composite $B \circ A:(\mathcal{C}, \mathcal{C}, \Omega) \rightarrow\left(e^{\prime \prime}, \mathcal{C}^{\prime \prime}, \Omega^{\prime \prime}\right)$ by the following data:

- the functor $B \circ A: C \rightarrow C^{\prime \prime}$,
- the function $(B \circ A)_{g}=B_{g} \circ A_{g}: \mathscr{G} \rightarrow \mathscr{L}^{\prime \prime}$,
- for each $G \in \mathscr{C}_{\text {J }}$, the functor $(B \circ A)_{G}=\left(A_{G} \circ B_{A_{g}(G)}: \int(B \circ A)_{g}(G) \rightarrow \int G\right)$.

Lemma 2.7.3. Given sd-functors $A$ and $B$ as in Definition 2.7.2, their composite $B \circ A$ is also an sd-functor.

Proof. Clearly $B \circ A$ is size-nonincreasing since both $A$ and $B$ are. Given a structured decomposition $d: \int G \rightarrow C$ of an object $X$ in $C$, we claim that $(B \circ A) \circ d \circ(B \circ A)_{G}: \int(B \circ A)_{g} G \rightarrow C^{\prime \prime}$ is a structured decomposition of $B(A(X))$ in $C^{\prime \prime}$. Using the fact that $A$ is an sd-functor, we get that $A \circ d \circ A_{G}: \int A_{g}(G) \rightarrow C^{\prime}$ is a structured decomposition of $A(X)$ in $C^{\prime}$. Then, invoking the sd-functor condition for $B$ on the decomposition $A \circ d \circ A_{G}$, we obtain that $B \circ\left(A \circ d \circ A_{G}\right) \circ B_{A_{g}(G)}: \int B_{g}\left(A_{g}(G)\right) \rightarrow C^{\prime \prime}$ is a structured decomposition of $B(A(X))$ and from there associativity of composition and the definition of $(B \circ A)_{G}$ lets us conclude that

$$
B \circ\left(A \circ d \circ A_{G}\right) \circ B_{A_{g}(G)}=(B \circ A) \circ d \circ\left(A_{G} \circ B_{A_{g}(G)}\right)=(B \circ A) \circ d \circ(B \circ A)_{G}
$$

from which the claim immediately follows.
Remark 2.7.4. The identity sd-functor $F:(\mathcal{C}, \mathcal{C}, \Omega) \rightarrow(\mathcal{C}, \mathcal{G}, \Omega)$ for the composition defined above has the components

- $F=\operatorname{id}_{C}: C \rightarrow C$,
- $F_{g}=\mathrm{id}_{\mathscr{G}}: \mathscr{G}^{\circ} \rightarrow G$,
- for each $G \in \mathcal{G}_{\mathcal{L}}$ the functor $F_{G}=\operatorname{id}_{\int G}: \int G \rightarrow \int G$.

Using this along with Lemma 2.7.3, we can define the category SdCat whose objects are sdcategories and whose morphisms are sd-functors.

Proposition 2.7.5. Given spined sd-categories $\Gamma=(\mathcal{C}, \mathcal{G}, \Omega), \Gamma^{\prime}=\left(\mathcal{C}^{\prime}, \mathcal{G}^{\prime}, \Omega^{\prime}\right)$ and an sd-functor $F: \Gamma \rightarrow \Gamma^{\prime}$, then for any $X \in C$, we have

$$
\mathbf{w}_{\Gamma^{\prime}}(F(X)) \leq \mathbf{w}_{\Gamma}(X) .
$$

Proof. Suppose that $d: \int G \rightarrow C$ is a minimal $\mathcal{C}_{\mathcal{L}}$-structured decomposition of $X$, which implies that $w(d)=\mathbf{w}_{\Gamma}(X)$. Since $F$ is an sd-functor, $F_{*}(d): \int F_{g}(G) \rightarrow C^{\prime}$ is a $\mathscr{G}^{\prime}$-structured decomposition of $F(X)$. But since $F$ is size-nonincreasing, for every $x \in V(G)$ we have $s^{\prime}(F(d(x))) \leq s(d(x))$. Hence $w\left(F_{*}(d)\right) \leq w(d)=\mathbf{w}_{\Gamma}(X)$. Thus $\mathbf{w}_{\Gamma^{\prime}}(F(X)) \leq \mathbf{w}_{\Gamma}(X)$.

The most common use case for sd-functors arises from the desire to relax structural constraints on decompositions (i.e. expand the set of allowed structure graphs) or to refine width measures by adding more permitted bounds.

![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-17.jpg?height=663&width=915&top_left_y=228&top_left_x=575)
Figure 2: An example of a tree decomposition of a graph $G$.

Now it is easy to give a definition for the treewidth of a graph $G$.
Definition 2.8.3. If ( $X, T$ ) is an RS-tree decomposition of a graph $G$, let

$$
w(X, T)=\max _{t \in T}|X(t)|-1
$$

denote the width of the tree decomposition, where $|X(t)|$ is the number of vertices in the bag $X(t)$. Then we define the treewidth $\mathbf{t w}(G)$ of $G$ to be the minimum width $w(X, T)$ over all RS-tree decompositions ( $X, T$ ) of $G$.

Remark 2.8.4. Note that there is always an RS-tree decomposition ( $X, T$ ) of a graph $G$ where $T=\bullet$ and $X(\bullet)=V(G)$. Hence $\mathrm{tw}(G) \leq|V(G)|-1$.

Example 2.8.5. Every tree $T$ has $\mathbf{t w}(T)=1$. To see this, note that one can obtain an RS-tree decomposition where there is one bag per edge of $T$, containing both endpoints of the edge. This decomposition has the smallest possible maximum bag size, and so achieves the treewidth.

Remark 2.8.6. In order to connect our theory to the classical graph theory literature, we must show that the RS-tree decompositions given above can be understood using structured decompositions.

In Appendix A.4.1 we show that to every RS-tree decomposition ( $X, T$ ) of a graph ${ }^{10} G$ one can associate a structured decomposition $d: \int T \rightarrow \mathbf{G r}$ of $G$, and vice versa. These maps will not define a bijection, as the corresponding adhesions of $d$ can change. However, this ultimately makes little difference. In Corollary A.4.12 we prove that the corresponding width-measure $\mathbf{w}_{\Gamma}(G)$ defined in terms of tree-shaped structured decompositions of $G$ (Definition 2.5.7) is equal to $\mathbf{t w}(G)$.

Therefore, in what follows, we will be cavalier and refer to tree-shaped structured decompositions $d: \int T \rightarrow \mathbf{G r}$ of a graph $G$ simply as tree decompositions of $G$.

While Definition 2.8.3 is rather elegant and simple, it turns out that another equivalent definition ${ }^{11}$ for treewidth is very useful for algorithmic purposes.

Definition 2.8.7. A chord of an $n$-cycle $\left\{x_{1}, \ldots, x_{n}\right\}$ is an edge connecting two vertices $x_{i}$ and $x_{j}$ such that $|i-j|>1$. A graph $G$ is chordal if every $n$-cycle in $G$ has a chord for $n>3$. By a chordal completion of a graph $G$, we mean a monomorphism $f: G \hookrightarrow H$ where $H$ is a chordal graph.

[^7]The chordal graphs can also be characterized using the following theorem of Dirac.
Theorem 2.8.8 ([Dir61]). A graph $H$ is chordal if and only if

- $H$ is a complete graph, i.e. $H \cong K^{n}$ for some $n \geq 0$, or
- there is a monic span $H_{0} \hookleftarrow K^{n} \hookrightarrow H_{1}$ where $H_{0}$ and $H_{1}$ are chordal, and $H \cong H_{0}+K^{n} H_{1}$.

The connection between tree decompositions and chordal graphs is given by the following result.

Lemma 2.8.9 ([Die10, Proposition 12.3.11]). A graph $G$ is chordal if and only if it has a tree decomposition $d: \int T \rightarrow \mathbf{G r}$ where each bag $d(t)$ is a complete graph $K^{n}$.

Definition 2.8.10. Given a graph $G$, let $\operatorname{Tree}(G)$ denote the subcategory of $\mathfrak{D}_{\text {Trees }}(\mathbf{G r}, G)$ (Definition 2.4.1) whose morphisms are monomorphisms. Let $\operatorname{Chord}(G)$ denote the category whose objects are pairs $(f, g)$ where $f: G \hookrightarrow H$ is a monomorphism to some chordal graph $H$ (a chordal completion of $G$ ) and $d$ is a (Trees, $\left\{K^{n}\right\}$ )-structured decomposition of $H$. Define the morphisms to be monomorphisms $h: H \rightarrow H^{\prime}$ making the following diagram commute
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-18.jpg?height=168&width=367&top_left_y=1059&top_left_x=849)

Suppose that $(f: G \hookrightarrow H, d)$ is an object of $\operatorname{Chord}(G)$. By Corollary A.2.13 the pullback of $d$ along $f$ exists, and is a tree decomposition $f^{*}(d)$ of $G$. By choosing representatives for each pullback, this extends to a functor $(-)^{*}: \operatorname{Chord}(G) \rightarrow \operatorname{Tree}(G)$.

Conversely, if $d: \int T \rightarrow \mathbf{G r}$ is a tree decomposition of $G$, then we can embed each bag $d(t)$, into $K^{|V(d(t))|}$ to form a new tree decomposition $d^{\prime}$. We call this completing the tree decomposition. The colimit $H$ of $d^{\prime}$ will then be a chordal graph, and we have canonical chordal completion $f: G \hookrightarrow H$. This also extends to a functor Comp : Tree $(G) \rightarrow \operatorname{Chord}(G)$.

Lemma 2.8.11. The functor $(-)^{*}$ is left adjoint to Comp. Furthermore $(-)^{*} \circ \operatorname{Comp} \cong 1_{\operatorname{Tree}(G)}$ and the functor Comp is surjective on objects.

It is now obvious how treewidth can be characterized using chordal completions. If $G$ is a graph, let $\omega(G)$ denote its clique number, i.e. the largest integer $n$ such that $K^{n}$ is a subgraph of $G$.

Lemma 2.8.12 ([Die10, Corollary 12.3.12]). Given a graph $G$, we have

$$
\mathbf{t w}(G)=\min \{\omega(H)-1 \mid G \hookrightarrow H, \text { and } H \text { is chordal }\} .
$$

### 2.9 Nice Tree Decompositions

The main algorithmic applications of pathwidth, treewidth and related graph parameters proceed by dynamic programming on the associated decompositions. Although the classic characterization of treewidth uses arbitrary tree decompositions, algorithms are more easily described by restricting attention to narrower decomposition structures. For instance, dynamic programming on trees benefits from restricting algorithms to binary trees: trees consisting of vertices with degree at most 3 . Our formalism allows us to prove a general result showing that ordinary and binary tree decompositions yield the same width notion.

Definition 2.9.1. Let BTrees denote the class of binary trees, i.e. trees whose vertices have degree at most 3.

Suppose that $\Gamma=(\mathcal{C}$, Trees, $\Omega)$ is a spined sd-category. Then clearly $\Gamma^{\prime}=(\mathcal{C}, \mathrm{B}$ Trees, $\Omega)$ is as well, and by Lemma 2.7.6 we have an sd-functor $t:(\mathcal{C}$, BTrees, $\Omega) \rightarrow(\mathcal{C}$, Trees, $\Omega)$ which is the identity on the underlying category. We now show the existence of a width-preserving sd-functor $B:(\mathcal{C}$, Trees, $\Omega) \rightarrow(\mathcal{C}$, BTrees, $\Omega)$.

Proposition 2.9.2. Given a spined sd-category $\Gamma=(\mathcal{C}$, Trees, $\Omega)$ and a Trees-structured decomposition $d: \int T \rightarrow C$ of an object $X \in C$, there exists a binary tree $U$ and a functor $U_{*}: \int U \rightarrow \int T$ such that the composite $\left(d \circ U_{*}\right): \int U \rightarrow C$ is a BTrees-structured decomposition of $X$, and furthermore has the same width as $d$.

Proof. We prove this by simultaneous induction on the maximal degree $m$ of any vertex in $T$, and the number $n$ of vertices which actually have degree $m$. Assume that every tree with $m \leq M$ and $n<N$ satisfies the result. We show that a tree $T$ with maximal degree $M$ and $N$ vertices of maximal degree also satisfies the result. We can further assume that $M>3$ : otherwise $T$ is already a binary tree, so we can take $U=T$ and $U_{*}=1_{\int T}$.

Choose a degree $M$ vertex $v$ of $T$, and partition the adjacent vertices into two sets $L, R$ of respective sizes $\left\lceil\frac{M}{2}\right\rceil$ and $\left\lfloor\frac{M}{2}\right\rfloor$. Let $T^{L}$ (resp. $T^{R}$ ) denote the induced subgraph consisting of those nodes that are connected to $v$ via a path in $L(R)$. Since $T$ is a tree, $T^{L}$ and $T^{R}$ are disjoint subgraphs of $T$.

Consider the tree $T^{\prime}$ formed by $T^{L}, T^{R}$ and 3 new vertices $\ell, v^{\prime}, r$, with edges $e_{\ell, x}$ connecting $\ell$ to each vertex $x$ in $L$, edges $e_{r, x}$ connecting $r$ to all vertices $x$ in $R$, and edges $e_{\ell, v^{\prime}}$ and $e_{r, v^{\prime}}$ connecting $v^{\prime}$ to $\ell$ and $r$ respectively. In $T^{\prime}, \ell$ has degree $|L|+1, r$ has degree $|R|+1$ and $v^{\prime}$ has degree 2 . Given that $M>3$, we have $M>|L|+1 \geq|R|+1$, so either the maximal degree of any vertex in $T^{\prime}$ is less than $M$, or else the number of elements of degree $M$ in $T^{\prime}$ is at most $N-1$, since $T^{L}$ and $T^{R}$ do not contain $v$, and $\ell, v^{\prime}, r$ each have degree strictly less than $M$.

Either way, the inductive hypothesis applies, and we obtain a binary tree $U^{\prime}$ along with a functor $U_{*}^{\prime}: \int U^{\prime} \rightarrow \int T^{\prime}$ so that for any Trees-structured decomposition $d^{\prime}: \int T^{\prime} \rightarrow C$ of an object $X$ in $C$, the composite $\left(d^{\prime} \circ U_{*}^{\prime}\right): \int U^{\prime} \rightarrow C$ is a BTrees-structured decomposition of $X$ in $\Gamma^{\prime}$ of the same width as $d^{\prime}$.

Now let us construct a functor $T_{*}^{\prime}: \int T^{\prime} \rightarrow \int T$ as follows. Define $T_{*}^{\prime}$ to

1. act as the identity on the vertex and edge objects of $\int T^{L}$ and $\int T^{R}$,
2. send the vertex objects of $\ell, v^{\prime}, r$ and the edge objects $e_{\ell, v^{\prime}}, e_{r, v^{\prime}}$ in $\int T^{\prime}$ to the vertex object of $v$ in $\int T$,
3. send the edge morphisms in $\int T^{\prime}$ connecting $e_{\ell, v^{\prime}}$ and $e_{r, v^{\prime}}$ to the vertex object of $v^{\prime}$, to the identity morphism on the vertex object of $v$,
4. the edge morphisms connecting the edge objects $e_{\ell, x}$ between $\ell$ and each vertex $x$ of $L$ in $T^{\prime}$ to the respective edge morphisms between $v$ and $L$ in $T$, and
5. similarly for the edge morphisms between $r$ and the vertices of $R$ in $T^{\prime}$.

Now the diagram $d \circ T_{*}^{\prime}: \int T^{\prime} \rightarrow C$ differs from $d$ only by the insertion of a trivial span, so any cocone for $d$ extends uniquely to a cocone for ( $d \circ T_{*}^{\prime}$ ), and it clearly has the same width as $d$.

Now setting $U=U^{\prime}$ and $U_{*}=T_{*}^{\prime} \circ U_{*}^{\prime}: \int U^{\prime} \rightarrow \int T$ gives for any Trees-structured decomposition $d: \int T \rightarrow C$ of an object $X$ in $C$, the composite $d \circ U_{*}: \int U \rightarrow C$ is a BTrees-structured decomposition of $X$ with the same width as $d$.

Thus by setting $B: C \rightarrow C$ to be the identity, $B_{g}$ : Trees → BTrees to be the map that assigns to a tree $T$ the binary tree $U^{\prime}$ as constructed above, and for $T \in$ Trees we let $B_{T}: \int B_{g}(T) \rightarrow \int T$ be $U_{*}$, we obtain a width-preserving sd-functor $B:(\mathcal{C}$, Trees, $\Omega) \rightarrow(\mathcal{C}$, BTrees, $\Omega)$.

Now consider a graph class $\mathscr{G}_{\text {which }}$ whitisfies closure under barycentric subdivision, so that whenever the class $\mathscr{C}_{\mathcal{L}}$ contains some graph $G$, we have that its barycentric subdivision $\int G$, regarded as a graph, also belongs to $\mathscr{G}$. For example $\mathscr{G}^{\circ}=$ Trees satisfies this property.

Let $\int \mathfrak{C}_{\mathcal{L}}$ denote the class of graphs in $\mathfrak{C}_{\mathcal{L}}$ that are in the image of the barycentric subdivision. For the remainder of this section, let $t:(\mathcal{C}, \mathcal{G}, \Omega) \rightarrow(\mathcal{C}, \mathcal{G}, \Omega)$ denote the identity on $\mathcal{C}$, which is an sd-functor by Lemma 2.7.6. By constructing an appropriate sd-functor from ( $\mathcal{C}, \mathcal{C}, \Omega$ ) to $(\mathcal{C}, \mathcal{G}, \Omega)$, we show that restricting to $(\mathcal{C}, \mathcal{G}, \Omega)$ does not change the associated $\Gamma$-width.

Definition 2.9.3. Define the barycentric restriction functor $S$ between ( $\mathcal{C}, \mathcal{G}, \Omega$ ) and ( $\mathcal{C}, \mathcal{G}, \Omega$ ) by setting the underlying functor $S: C \rightarrow C$ to be the identity, $S_{g}: \mathscr{L} \rightarrow \int G$ as barycentric subdivision so that $S_{g}(G)=\int G$ regarded as a graph, and for $G \in \mathcal{C}_{\text {define }} S_{G}: \int S_{g} G \rightarrow \int G$ in the following manner.

In $\int S_{g} G$, objects come in two types: those corresponding to vertices of $S_{g} G$ (originating from vertex or edge objects of $\int G$ ) and those arising as the vertex resulting from the subdivision of an edge in $S_{g} G$. The functor $S_{G}$ sends each vertex object of the former kind to the corresponding vertex object in $\int G$, and both the edge object and the subdivision vertex object corresponding to each edge $e$ in $S_{g} G$ to the edge object $e$ in $\int G$, while sending the legs of every span connecting preimages of edge objects to the identity morphism. These functors $S_{G}$ are clearly final, so the sd-functor condition pertaining to preservation of colimits is satisfied.

Example 2.9.4. Consider the graph $G$ consisting of a single edge $e$ and its end vertices $x, y$. The upper diagram depicts the category $\int G$, the diagram lower depicts the category $\int S_{g} G$, where now $e$ has become a vertex object, and there are two new edge objects $e x$ and $e y$. The dashed arrows depict the action of the functor $S_{G}: \int S_{g} G \rightarrow \int G$ on the objects of $\int S_{g} G$; the morphisms of $\int S_{g} G$ are labeled with their $S_{G}$-images.
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-20.jpg?height=239&width=639&top_left_y=1299&top_left_x=712)

Proposition 2.9.5. The barycentric subdivision functor defines a width-preserving sd-functor $S:(\mathcal{C}, \mathcal{G}, \Omega) \rightarrow(\mathcal{C}, \mathcal{G}, \Omega)$.

Proof. Clearly $S$ is size non-increasing and the barycentric restriction functor associates to each $G$-structured decomposition of $X$ to an $\int G$-structured decomposition of $X$. $\square$

Combining Proposition 2.9.2 with Proposition 2.9.5 gives the existence of so-called nice tree decompositions in any sd-category of tree-structured decompositions. Nice tree decompositions of graphs are commonly used when defining dynamic programming algorithms on tree decompositions, see [Nie06, Chapter 10] for more information.

Corollary 2.9.6. Given an sd-category of the form $\Gamma=(\mathcal{C}$, Trees, $\Omega)$ and $X \in C$, we can find a binary tree $G$ and a $G$-structured decomposition $d: \int G \rightarrow C$ of $X$ such that each span $d\left(v_{1}\right) \hookleftarrow d(e) \hookrightarrow d\left(v_{1}\right)$ has one of the following forms:

1. $d\left(v_{1}\right) \cong d(e) \cong d\left(v_{2}\right)$ and both monos of the span are isomorphisms (join nodes),
2. $d\left(v_{1}\right) \cong d(e)$, the left mono is an isomorphism but the right mono is not, or
3. $d(e) \cong d\left(v_{2}\right)$, the right mono is an isomorphism and the left mono is not (introduce/forget nodes).

A similar, but simpler argument yields the existence of nice path decompositions as well.

## 3 Examples

In this section we detail several examples of our formalism that already exist in the literature. We are able to capture treewidth, pathwidth, complemented treewidth, tree independence number and hypergraph treewidth directly as examples of $\Gamma$-width, and we draw connections between sd-categories and $\Gamma$-width with Carmesin's graph decompositions, layered treewidth and $\mathscr{H}$-treewidth.

### 3.1 Treewidth

We obtain the main combinatorial invariant of a graph of interest in this paper, namely treewidth, as an example of $\Gamma$-width as follows.

Proposition 3.1.1. The triple $\Gamma=\left(\mathrm{Gr}\right.$, Trees, $\left.\left\{K^{n}\right\}_{n \geq 0}\right)$ is a complete width category and the $\Gamma$ width of a graph $G \in \mathbf{G r}$ is precisely its treewidth $\mathbf{t w}(G)=\mathbf{w}_{\Gamma}(G)$.

Proof. Condition (W1) holds by Corollary A.2.12, (W2) holds since there exist no monomorphisms $f: G \rightarrow H$ of graphs where $|V(G)|>|V(H)|$, and (W3) holds by Corollary A.2.13. Furthermore (W4) holds because completing a tree decomposition $d$ of a graph $G$ to a (Trees, $\left\{K^{n}\right\}_{n \geq 0}$ )-decomposition $d^{\prime}$ can never reduce the number of vertices of the corresponding colimit colim $d^{\prime}=H$. This is because the bags of $d^{\prime}$ can only be greater than or equal to the size of the bags of $d$, and the adhesions are the same. In effect we are quotienting larger graphs by the "same relation." Hence the induced map $G \rightarrow H$ must be a monomorphism. The fact that $\mathbf{w}_{\Gamma}(G)=\mathbf{t w}(G)$ is Corollary A.4.12. $\square$

In fact, we need not restrict ourselves to $\mathbf{G r}$ to capture treewidth. Let $K_{r}^{n}$ denote the reflexive $n$-clique, i.e. the $n$-clique additionally having a single loop on each vertex. Let $K_{\mathrm{mlt}}^{n}$ denote the multi $n$-clique. This is the multigraph with $n$ vertices and between every pair of (not necessarily distinct) vertices there are $n$ edges.

Lemma 3.1.2. The triples $\Gamma=\left(\mathbf{G r}_{\ell}\right.$, Trees, $\left.\left\{K_{r}^{n}\right\}_{n \geq 0}\right)$ and $\Gamma^{\prime}=\left(\mathbf{G r}_{\mathrm{mlt}}\right.$, Trees, $\left.\left\{K_{\mathrm{mlt}}^{n}\right\}_{n \geq 0}\right)$ both form width categories, and the inclusion functors $\mathbf{G r} \hookrightarrow \mathbf{G r}_{\ell} \hookrightarrow \mathbf{G r}_{\text {mlt }}$ are sd-functors. Furthermore if $G$ is a simple graph, then

$$
\mathbf{w}_{\Gamma}(G)=\mathbf{w}_{\Gamma^{\prime}}(G)=\mathbf{t w}(G) .
$$

Proof. This follows from noticing that the inclusion functors above all preserve finite limits and pushouts of spans of monomorphisms. The size of a loop graph $G$ in ( $\mathbf{G r}_{\ell}$, Trees, $\left.\left\{K^{n}\right\} \cup\left\{K_{r}^{n}\right\}_{n \geq 0}\right)$ is its number of vertices, while the size of a multigraph $H$ in ( $\mathbf{G r}_{\text {mlt }}$, Trees, $\left\{K^{n}\right\} \cup\left\{K_{\text {mlt }}^{n}\right\}_{n \geq 0}$ ) is the maximum of its vertices and edges. For a simple graph $G$, its number of vertices is always greater than or equal to its number of edges. Hence the size of any simple graph embedded in $\mathbf{G r}_{\text {mlt }}$ is still its number of vertices. Thus the inclusion functors clearly are size preserving. Now for a simple graph $G$ embedded in $\mathbf{G r}_{\ell}$ or $\mathbf{G r}_{\text {mlt }}$, none of the multigraphs appearing in any of the bags or adhesions of any decomposition of $G$ can have loops or multiple edges. Hence every decomposition must factor through Gr, and therefore the inclusion functors must take minimal decompositions of graphs to minimal decompositions, thus by Lemma 2.7.9, the inclusion functors are width-preserving. $\square$

### 3.2 Pathwidth

Pathwidth is another common width-measure used for graphs [Die10, Page 279], [RS83].
Definition 3.2.1. A path-decomposition of a graph $G$ is a Paths-structured decomposition (Definition 2.1.2) $d: \int P \rightarrow \mathbf{G r}$. The corresponding notion of pathwidth $\mathbf{p w}(G)$ of a graph $G$ is defined in the obvious way.

Clearly every path is a tree, i.e. Paths $\subseteq$ Trees.
Lemma 3.2.2. The triple $\Gamma=\left(\mathbf{G r}\right.$, Paths, $\left.\left\{K^{n}\right\}_{n \geq 0}\right)$ forms a complete width category. Furthermore the $\Gamma$-width of a graph $G$ is precisely its pathwidth $\mathbf{p w}(G)$.
Proof. This follows from Proposition 3.1.1 and Lemma 2.7.6.
The following result is obvious and well-known, but we include it anyway, as it follows immediately from our formalism.

Corollary 3.2.3. Given a graph $G$, we have $\mathbf{t w}(G) \leq \mathbf{p w}(G)$.
Proof. The identity functor (Gr, Paths, $\left.\left\{K^{n}\right\}_{n \geq 0}\right) \rightarrow\left(\mathbf{G r}\right.$, Trees, $\left.\left\{K^{n}\right\}_{n \geq 0}\right)$ is a sd-functor, so the result holds by Proposition 2.7.5.

### 3.3 Complemented Treewidth

Another graph width measure of interest is the notion of complemented treewidth. Given a graph $G$, this is defined as

$$
\overline{\mathbf{t w}}(G):=\mathbf{t w}(\bar{G}),
$$

where $\bar{G}$ denotes the complement ${ }^{12}$ of $G$. Complemented treewidth has useful applications in algorithmics [DOS21] since it allows for recursive algorithms on graph classes that are both dense and incomparable to bounded treewidth classes. Using the theory of spined categories [BK23, Section 5.2], one can already provide a category-theoretic characterization of complemented treewidth. Here we recast this characterization in the language of width categories.
Definition 3.3.1. Let $\overline{\mathbf{G r}}$ denote the category whose objects are graphs, and whose morphisms $f: G \rightarrow H$ are vertex maps $f: V(G) \rightarrow V(H)$ with the property that if $f(x) f(y)$ is an edge in $H$, then $x y$ is an edge in $X$. We call this a reflexive graph homomorphism.

Let $\overline{(-)}: \mathbf{G r} \rightarrow \overline{\mathbf{G r}}$ denote the complementation functor that sends a graph $G$ to its complement $\bar{G}$ and a graph homomorphism $f: G \rightarrow H$ to the corresponding reflexive graph homomorphism $\bar{f}: \bar{G} \rightarrow \bar{H}$.
Lemma 3.3.2. A reflexive graph homomorphism $f: G \rightarrow H$ is a mono/epimorphism in $\overline{\mathbf{G r}}$ if and only $V(f)$ is an in/surjective function.
Proof. The vertex set functor $V: \overline{\mathbf{G r}} \rightarrow$ Set is faithful, and furthermore has a left adjoint CoDisc and a right adjoint Disc, so the result follows from the same reasoning as in the beginning of Section A.4. $\square$

Lemma 3.3.3 ([BK23, Proposition 5.10]). The complementation functor $\overline{(-)}: \mathbf{G r} \rightarrow \overline{\mathbf{G r}}$ is an isomorphism of categories.

We abuse notation and let $\overline{(-)}: \overline{\mathbf{G r}} \rightarrow \mathbf{G r}$ denote the inverse of the isomorphism of Lemma 3.3.3. If we let $\operatorname{Disc}(n)$ denote the discrete graph on $n$ vertices, then it is obvious that $\overline{K^{n}}= \operatorname{Disc}(n)$. Furthermore, since $\overline{(-)}$ is an isomorphism, we know that we can transfer the width category structure of $\mathbf{G r}$ over to $\overline{\mathbf{G r}}$.

Proposition 3.3.4. Graphs with reflexive graph homomorphism form a width category $\Gamma= \left(\overline{\mathbf{G r}}\right.$, Trees, $\left.\{\operatorname{Disc}(n)\}_{n \geq 0}\right)$. Furthermore the $\Gamma$-width of a graph $G$ is precisely its complemented treewidth $\overline{\mathbf{t w}}(G)$.

Proof. Clearly $\Gamma$ satisfies (W1) and (W3) since it is isomorphic to the width category of Proposition 3.1.1. Since the size in $\Gamma$ is the number of vertices, by Lemma 3.3.2, condition (W2) is satisfied. Now a functor $d: \int T \rightarrow \overline{\mathbf{G r}}$ is a decomposition of a graph $G$ if and only if $\bar{d}=\overline{(-)} \circ d$ : $\int T \rightarrow \mathbf{G r}$ is a tree decomposition of $\bar{G}$, and $w(d)=w(\bar{d})$. Therefore $\mathbf{w}_{\Gamma}(G)=\mathbf{t w}(\bar{G})=\overline{\mathbf{t w}}(G)$. $\square$

[^8]
### 3.4 Tree Independence Number

We can also capture another interesting graph invariant, called the tree independence number $\mathbf{t w}_{\alpha}(G)$ of a graph $G$. This invariant, introduced in [DMŠ24], is defined similarly to treewidth, but using a different measure of size for the bags. It is important in algorithmics as the Maximum Weight Independent Packing problem can be solved in polynomial time on a graph $G$ equipped with a tree decomposition of bounded independence number [DMŠ24, Theorem 7.2].

Definition 3.4.1. Given a graph $G$, an independent set $I$ of $G$ is a subset $I \subseteq V(G)$ such that each pair $x, y \in I$ are not adjacent, i.e. $x y \notin E(G)$. The independence number $\alpha(G)$ of a graph $G$ is the cardinality of the largest independent set of $G$. The tree independence number $\mathbf{t w}_{\alpha}(d)$ of a tree decomposition $d: \int T \rightarrow \mathbf{G r}$ of a graph $G$ is $\max _{t \in V(T)} \alpha(d(t))-1$. The tree independence number $\mathbf{t w}_{\alpha}(G)$ of a graph $G$ is the minimal tree independence number of all of its tree decompositions.

We wish to capture tree independence number using a width category. If we try to do this using $\mathbf{G r}$ as the underlying category, we immediately run up against the fact that independence number is not monotone with respect to monomorphisms.

Example 3.4.2. Take $G=\operatorname{Disc}(n)$ to be the discrete graph on $n>1$ vertices and $H=K^{n}$ the complete graph on $n$ vertices. Then there is a canonical monomorphism $G \hookrightarrow H$ in $\mathbf{G r}$, but $\alpha(G)=n$ and $\alpha(H)=1$.

By Lemma 2.5.5, this implies that there does not exist a spine on $\mathbf{G r}$ with which we can obtain tree independence number as $\Gamma$-width. However, the following result provides us with the correct category with which to capture tree independence number. Recall the notion of a reflexive graph homomorphism from Definition 3.3.1.

Lemma 3.4.3. Let $f: G \rightarrow H$ be a reflexive graph homomorphism. If $I \subseteq V(G)$ is an independent set of $G$, then $f(I)$ is an independent set of $H$.

Proof. Suppose that $x, y \in I$ and $f(x) f(y) \in E(H)$. Then since $f$ is reflexive, this implies $x y \in E(G)$, which is a contradiction as $I$ is an independent set. Thus $f(I)$ is an independent set of $H$.

Lemma 3.4.4. If $f: G \hookrightarrow H$ is a monomorphism in $\overline{\mathbf{G r}}$, then $\alpha(G) \leq \alpha(H)$.
Proof. This follows from Lemma 3.3.2 and Lemma 3.4.3.
Let $\Omega_{k}^{\alpha}$ denote the set of graphs $G$ with $\alpha(G) \leq k$. Let $\Omega^{\alpha}$ denote the corresponding filtered full subcategory of $\overline{\mathbf{G r}}$.

Proposition 3.4.5. Graphs with reflexive graph homomorphisms form a width category $\Gamma=$ ( $\overline{\mathbf{G r}}$, Trees, $\Omega^{\alpha}$ ). The $\Gamma$-width of a graph $G$ is precisely its tree independence number $\mathbf{t w}_{\alpha}(G)$.

Proof. The conditions (W1) and (W3) follow from the same reasoning as in Proposition 3.3.4. Condition (W2) holds by Lemma 3.4.4. The fact that $\mathbf{w}_{\Gamma}(G)=\mathbf{t w}_{\alpha}(G)$ is practically by definition.

Corollary 3.4.6. Given a reflexive graph homomorphism $f: G \rightarrow H$ which is furthermore injective on vertices we have

$$
\mathbf{t w}_{\alpha}(G) \leq \mathbf{t w}_{\alpha}(H)
$$

Proof. This follows from Proposition 3.4.5 and Proposition 2.5.18.
Let $\overline{\mathbf{G r}}_{\alpha}$ denote the width category from Proposition 3.4.5, and let $\overline{\mathbf{G r}}_{\mathbf{t w}}$ denote the width category from Proposition 3.3.4.

Lemma 3.4.7. The identity functor on $\overline{\mathbf{G r}}$ is a sd-functor $1_{\overline{\mathbf{G r}}}: \overline{\mathbf{G r}}_{\mathbf{t w}} \rightarrow \overline{\mathbf{G r}}_{\alpha}$.
Proof. If $G$ is a graph, then clearly $\alpha(G) \leq|V(G)|$. Thus the result follows by Proposition 2.7.5.

Corollary 3.4.8. Given a graph $G$,

$$
\mathbf{t w}_{\alpha}(G) \leq \overline{\mathbf{t w}}(G)
$$

There is a well-known duality between independent sets and cliques.
Lemma 3.4.9. Given a graph $G$, a subgraph $K \subseteq G$ is complete if and only if the corresponding subgraph of its complement $\bar{K} \subseteq \bar{G}$ is an independent set.

Recall the notion of the clique number $\omega(G)$ of a graph $G$ from Lemma 2.8.12. Let $\Omega_{k}^{\omega}$ denote the set of graphs with clique number less than or equal to $k \geq 0$, and let $\Omega^{\omega}$ denote the corresponding full subcategory of Gr.

Lemma 3.4.10. If $f: G \hookrightarrow H$ is a monomorphism in $\mathbf{G r}$, then $\omega(G) \leq \omega(H)$.
Proof. If $K \subseteq G$ is a complete subgraph of $G$, then $f(K)$ is a complete subgraph of $H$ with the same number of vertices.

Proposition 3.4.1. Graphs with clique number form a width category $\Gamma=\left(\mathbf{G r}, \operatorname{Trees}, \Omega^{\omega}\right)$.
Proof. Conditions (W1) and (W3) follow from the same reasoning as in Proposition 3.1.1. Condition (W2) follows from Lemma 3.4.10.

We now define the following auxiliary graph parameter, which is intimately related with tree-independence number by Lemma 3.4.13.

Definition 3.4.12. Given a graph $G$, we call the $\Gamma$-width of $G$ with respect to the width category $\Gamma$ of Proposition 3.4.11 the tree clique number of $G$ and denote it

$$
\operatorname{tcn}(G)=\mathbf{w}_{\Gamma}(G)
$$

Let $\mathbf{G r}_{\omega}$ denote the width category $\mathbf{G r}_{\omega}=\left(\mathbf{G r}\right.$, Trees, $\left.\Omega^{\omega}\right)$ and let $\overline{\mathbf{G r}}_{\alpha}$ denote the width category $\overline{\mathbf{G r}}_{\alpha}=\left(\overline{\mathbf{G r}}\right.$, Trees, $\left.\Omega^{\alpha}\right)$.

Lemma 3.4.13. The complementation functors $\overline{(-)}: \mathbf{G r}_{\omega} \rightarrow \overline{\mathbf{G r}}_{\alpha}$ and $\overline{(-)}: \overline{\mathbf{G r}}_{\alpha} \rightarrow \mathbf{G r}_{\omega}$ are sizepreserving sd-functors.

Proof. Since $\overline{(-)}$ is an isomorphism of the underlying categories by Lemma 3.3.3, we need only to show that $\overline{(-)}$ is size nonincreasing. Let $G$ be a graph. Its size in $\mathbf{G r}_{\omega}$ is equal to its clique number $\omega(G)$. Suppose that $K^{n} \subseteq G$ is a maximal clique, so that $\omega(G)=n$. Then $\overline{K^{n}} \subseteq \bar{G}$ is an $n$-independent set. If $I \subseteq V(\bar{G})=V(G)$ is a $k$-independent set of $\bar{G}$ with $n \leq k$, then $\bar{I}$ is a $k$-clique in $G$ by Lemma 3.4.9. Hence $n=k$, and so $I$ is maximal. Thus $\omega(G)=\alpha(\bar{G})$, which immediately implies that $\omega(\bar{G})=\alpha(G)$.

Corollary 3.4.14. Given a graph $G$ we have

$$
\operatorname{tcn}(G)=\operatorname{tw}_{\alpha}(\bar{G})
$$

Proof. By Lemma 3.4.13 and Proposition 2.7.5, we have

$$
\mathbf{t w}_{\alpha}(\bar{G}) \leq \mathbf{t c n}(G)
$$

and

$$
\mathbf{t c n}(\bar{G}) \leq \mathbf{t w}_{\alpha}(G)
$$

Hence $\mathbf{t c n}(G) \leq \mathbf{t w}_{\alpha}(\bar{G}) \leq \mathbf{t c n}(G)$.

### 3.5 Hypergraph Treewidth

In this section, we construct sd-categories which capture the notions of hypergraph treewidth and generalized hypertreewidth.

Definition 3.5.1. A hypergraph $H$ consists of a finite set $V(H)$ of vertices and a subset $E(H) \subseteq P_{\neq \varnothing}(V(H))$ of nonempty subsets of $V(H)$ called hyperedges. If $e \in E(H)$ is a hyperedge with cardinality $n$, we call $e$ an $n$-edge, and let $P_{n}(V(H))$ denote the set of $n$-subsets of $V(H)$ and $E_{n}(H)$ the set of $n$-edges of $H$. A map $f: H \rightarrow H^{\prime}$ of hypergraphs consists of a function $V(f): V(H) \rightarrow V\left(H^{\prime}\right)$ such that if $e \in E_{n}(H)$, then $f(e) \in E_{n}\left(H^{\prime}\right)$. We call $f$ a hypergraph homomorphism. Let Hyp denote the category of hypergraphs and hypergraph homomorphisms.

Definition 3.5.1 is equivalent to the definition of hypergraphs given in [AGG07, Section 2], except that they do not allow for empty hypergraphs or hypergraphs with isolated vertices, namely those vertices that do not belong to any hyperedge.

We can consider a graph $G$ as a special kind of hypergraph. Namely it is a hypergraph where each hyperedge $e \in E(G)$ has cardinality 2 . Then a function $V(f): V(G) \rightarrow V\left(G^{\prime}\right)$ is a map of graphs if and only if it is a map of hypergraphs. In other words, we obtain a fully faithful inclusion functor $\iota$ : Gr ↪ Hyp.

Remark 3.5.2. We mention another popular category of hypergraphs from the literature. Let $\mathbf{H y p}_{\text {mlt }}$ denote the category considered in [DW80, Section 2]. An object $H$ of this category consists of finite sets $V(H), E(H)$, and a function $\partial: E(H) \rightarrow P_{\neq \varnothing}(V(H))$. This means that multiple edges can contain the same vertices, and hence we call these multihypergraphs. If we require $\partial$ to be injective, then we get precisely our notion of hypergraph, which is sometimes called a simple hypergraph. We note that the corresponding notion of morphism in [DW80] is quite loose. It allows for example the unique morphism $f: H \rightarrow H^{\prime}$ where $H$ has three vertices $x, y, z$ and one hyperedge $e=\{x, y, z\}$ and $H^{\prime}$ has one vertex $w$ and one hyperedge $\ell=\{w\}$. We will return to this observation in Remark 3.5.4.

Definition 3.5.3. Given a hypergraph $H$, we let Gaif $(H)$ denote the Gaifman graph ${ }^{13}$ of $H$. This is the graph with $V(\operatorname{Gaif}(H))=V(H)$ and where there is an edge $x y \in E(\operatorname{Gaif}(H))$ if and only if $x \neq y$ and there exists a hyperedge $e \in E(H)$ with $x, y \in e$.

The Gaifman graph construction extends to a functor Gaif : Hyp → Gr. Indeed if $f: H \rightarrow H^{\prime}$ is a map of hypergraphs, then $V(\operatorname{Gaif}(f)): V(\operatorname{Gaif}(H)) \rightarrow V\left(\operatorname{Gaif}\left(H^{\prime}\right)\right)$ is equal to $V(f): V(H) \rightarrow V\left(H^{\prime}\right)$, so we need only to show that $\operatorname{Gaif}(f)$ is a graph homomorphism. Suppose that $x y \in E(\operatorname{Gaif}(H))$, so $x \neq y$. Then there exists a $n$-edge $e \in E_{n}(H)$ of cardinality $n>1$ with $x, y \in e$. Since $f$ is a map of hypergraphs, this means that $f(e)$ is an $n$-edge, and $f(x) \neq f(y)$. Thus $f(x) f(y) \in \operatorname{Gaif}\left(H^{\prime}\right)$. Thus Gaif $(f)$ is a graph homomorphism.

Remark 3.5.4. Had we chosen to work instead with $\mathbf{H y p}_{\mathrm{mlt}}$, then we would not obtain a functor to $\mathbf{G r}$, but instead to $\mathbf{G r}_{\ell}$, as we would have to be able to collapse edges to loops, such as in Remark 3.5.2.

As with graphs in Section 2.8, there is an obvious extension of the notion of RobertsonSeymour tree decompositions for hypergraphs.

Definition 3.5.5 ([Hei13, Page 11]). An RS-tree decomposition ( $X, T$ ) of a hypergraph $H$ consists of a tree $T$ along with a function $X: V(T) \rightarrow P(V(H))$ such that

1. $\bigcup_{t \in V(T)} X(t)=V(G)$,
2. for every $e \in E(H)$, there exists a bag $X(t)$ such that $e \subseteq X(t)$,

[^9]3. given three vertices $t_{1}, t_{2}, t_{3} \in V(T)$, if $t_{2}$ lies on the unique path between $t_{1}$ and $t_{3}$, then $X\left(t_{1}\right) \cap X\left(t_{3}\right) \subseteq X\left(t_{2}\right)$.

The width $w(X, T)$ of a tree decomposition ( $X, T$ ) of $H$ is the maximal number of vertices of its bags minus 1 . The hypergraph treewidth $\mathbf{t w}_{\mathbf{H y p}}(H)$ of $H$ is defined to be the minimal width of all of its tree decompositions.

Remark 3.5.6. We note that if $H$ is a graph, then Definition 3.5.5 is precisely the same as Definition 2.8.1.

In order to connect hypergraph treewidth with the $\Gamma$-width of Proposition A.4.11, we need to connect tree-shaped structured decompositions of hypergraphs with RS-tree decompositions. This takes a bit of work, so the construction and proofs are relegated to Section A.4.1. We therefore abuse notation and call both RS-tree decompositions and tree-shaped structured decomposition $d: \int T \rightarrow$ Hyp of a hypergraph $H$ tree decompositions.

Let $K_{\text {Hyp }}^{n}$ denote the hypergraph with $V\left(K_{\text {Hyp }}^{n}\right)=\{1, \ldots, n\}$ and where every nonempty subset of $\{1, \ldots, n\}$ is a hyperedge. We call $K_{\text {Hyp }}^{n}$ the complete hypergraph on $n$ vertices. A hypergraph $H$ has a monomorphism $H \hookrightarrow K_{\text {Hyp }}^{n}$ if and only if $|V(H)| \leq n$.

Proposition 3.5.7. Hypergraphs form a width category $\Gamma=\left(\mathbf{H y p}\right.$, Trees, $\left.\left\{K_{\mathbf{H y p}}^{n}\right\}_{n \geq 0}\right)$. Furthermore, given a hypergraph $H$, its hypergraph treewidth and $\Gamma$-width are equal

$$
\mathbf{t w}_{\mathbf{H y p}}(H)=\mathbf{w}_{\Gamma}(H) .
$$

Proof. It is clear that (W1) holds, (W2) holds by Lemma A.4.2 and (W3) holds by Lemma A.4.3 and a similar argument for (W4) as in the proof of Proposition 3.1.1. The fact that $\mathbf{t w}_{\mathbf{H y}}(H)= \mathbf{w}_{\Gamma}(H)$ is Proposition A.4.11.

It is well-known that the hypergraph treewidth of a hypergraph $H$ is equal to the treewidth of its Gaifman graph Gaif $(H)[\operatorname{Got}+05$, Page 2]. We will now prove this using the sd-category framework.

For the next result, let $\mathbf{G r}$ denote the sd-category from Proposition 3.1.1, with $\mathbf{w}_{\mathbf{G r}}(G)$ its corresponding $\Gamma$-width, and let Hyp denote the sd-category of hypergraphs given above, with $\mathbf{w}_{\mathbf{H y p}}(H)$ its corresponding $\Gamma$-width.

Lemma 3.5.8. The inclusion functor $\iota: \mathbf{G r} \rightarrow \mathbf{H y p}$ and the Gaifman graph functor Gaif : $\mathbf{H y p} \rightarrow$ Gr are both sd-functors.

Proof. The inclusion functor preserves pushouts of spans of monomorphisms by construction, and is size-preserving. The Gaifman graph functor preserves pushouts of spans of monomorphisms by Lemma A.4.6 and is also size-preserving.

Corollary 3.5.9. Given a hypergraph $H$ and a graph $G$,

$$
\mathbf{w}_{\mathbf{H y p}}(l(G)) \leq \mathbf{t w}(G),
$$

and

$$
\mathbf{t w}(\operatorname{Gaif}(H)) \leq \mathbf{w}_{\mathbf{H y p}}(H) .
$$

Thus we see that if $G$ is a graph, then $\mathbf{w}_{\mathbf{H y p}}(\iota(G))=\mathbf{t w}(G)$. Let us now prove the reverse of the second inequality.

Lemma 3.5.10. If $H$ is a hypergraph, then

$$
\mathbf{w}_{\mathbf{H y p}}(H) \leq \mathbf{t w}(\operatorname{Gaif}(H)) .
$$

Proof. Suppose that $d: \int T \rightarrow \mathbf{G r}$ is a tree decomposition of $\operatorname{Gaif}(H)$. Then by Proposition A.4.11, we can construct an RS-tree decomposition ( $X, T$ ) with the same bags as $d$, and then by [Die10, Lemma 12.3.4], we know that every complete subgraph of $\operatorname{Gaif}(H)$ will belong to a single bag of $(X, T)$ and hence to $d$. Thus $d$ can be extended uniquely to a structured decomposition $d^{\prime}: \int T \rightarrow$ Hyp of $H$ with the same width as $d$. Hence the inequality follows. $\square$

Corollary 3.5.11. Given a hypergraph $H$,

$$
\mathbf{w}_{\mathbf{H y p}}(H)=\mathbf{t w}(\operatorname{Gaif}(H))=\mathbf{t w}_{\mathbf{H y p}}(H) .
$$

### 3.6 Carmesin's Graph Decompositions

In [Car22b, Definition 9.3], Carmesin introduced the notion of graph-decomposition, which we give in the language of structured decompositions. Let mltGraphs denote the set of multigraphs.
Definition 3.6.1. Given a multigraph $H$, a graph decomposition of $H$ is a mltGraphsstructured decomposition $d: \int G \rightarrow \mathbf{G r}_{\mathrm{mlt}}$ of $H$.

Now one might wonder why the definition was not given as a structured decomposition in Gr. This is because Gr does not have colimits of all Graphs-structured decompositions. For example, consider the following structured decomposition $d: \int K^{3} \rightarrow \mathbf{G r}$
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-27.jpg?height=309&width=403&top_left_y=1199&top_left_x=833)
where the images of $f, g$ are disjoint and we colored the adhesions red for readability. The diagram $d$ does not have a colimit in Gr. Such a colimit would have to coequalize the morphisms $f$ and $g$. But constructing a map $h: K^{2} \rightarrow G$ so that $h f=h g$ requires sending both vertices of $K^{2}$ to the same vertex in $G$, and hence collapsing the edge of $K^{2}$. This cannot be done in Gr.

Carmesin works around this issue by taking the colimit in the category $\mathbf{G r}_{\text {mlt }}$ of multigraphs, which is finitely cocomplete (see Definition A.1.7). This also has the effect that the indexing graph itself must be allowed to be a multigraph, see [Car22b, Example 9.6, 9.7].

Let mltGraphs ${ }_{\leq n}$ denote the set of multigraphs with at most $n$ vertices.
Proposition 3.6.2. The triple ( $\mathbf{G r}_{\text {mlt }}$, mltGraphs, $\left\{\text { mltGraphs }_{\leq n}\right\}_{n \geq 0}$ ) is a width category. Furthermore, the width of a mltGraphs-structured decomposition of a graph $G$ is precisely the same as the width of its corresponding graph-decomposition in the sense of Carmesin.
Proof. It is easy to see that (W2) holds, and (W1) holds because $\mathbf{G r}_{\mathrm{mlt}}$ has all finite colimits. Now (W3) holds by Corollary A.3.8. Carmesin defines the width of a graph-decomposition $d$ of a graph $G$ as the maximum number of vertices of its bags, which in this case is precisely the size of the structured decomposition. $\square$

Note that Carmesin does not actually ever define the graphwidth of a graph $G$. In other words, he considers width only as a propert of graph decompositionss, not as a property of graphs. This is explained by the following result.
Lemma 3.6.3. Given $\Gamma=\left(\mathbf{G r}_{\text {mlt }}\right.$, mltGraphs, $\left.\left\{\text { mltGraphs }_{\leq n}\right\}_{n \geq 0}\right)$, every multigraph $G$ with more than one vertex has $\Gamma$-width 1 .

Proof. Every multigraph can be glued together all at once using colimits from three kinds of bags, the graph • the multigraph with one vertex and one loop, and the multigraphs with two vertices and $n$-many edge between them, all of which have size less than or equal to 2 . $\square$

### 3.7 Layered Treewidth

Layered treewidth is a graph invariant introduced independently in [Sha15] and [DMW17]. Unlike treewidth, layered treewidth is bounded on the class of planar graphs [DMW17, Theorem 12].

Definition 3.7.1 ([Bos+22, Section 2]). A layering $L$ for a graph $G$ consists of a partition $\left(L_{0}, L_{1}, \ldots, L_{n}, \ldots\right)$ of $V(G)$ such that if $x y \in E(G)$, and $x \in L_{i}, y \in L_{j}$, then $|i-j| \leq 1$.

There is a convenient way to think about layerings using graph homomorphisms. Let $\mathbf{G r}^{\infty}, \mathbf{G r}_{\ell}^{\infty}, \mathbf{G r}_{r}^{\infty}$ and $\mathbf{G r}_{\text {mlt }}^{\infty}$ denote the categories of graphs corresponding to those in Section A. 1 but whose sets of vertices (and sets of edges in the case of multigraphs) can now be infinite. We can consider the faithful inclusion $i: \mathbf{G r} \hookrightarrow \mathbf{G r}_{r}^{\infty}$. Then a layering of a graph $G$ is equivalent to a morphism $G \rightarrow P_{r}^{\infty}$ in $\mathbf{G r}_{r}^{\infty}$, where $P_{r}^{\infty}$ is the infinite reflexive graph with $V\left(P_{r}^{\infty}\right)=\mathbb{N}$ and where for $x, y \in V\left(P_{r}^{\infty}\right)$, there is an edge $x y$ if and only if $|x-y| \leq 1$. Let $\mathbf{G r}_{\text {Lyr }}$ denote the comma category ( $i \downarrow P_{r}^{\infty}$ ). We call the objects of $\mathbf{G r}_{\text {Lyr }}$ layered graphs and the morphisms layered graph homomorphisms. Note that every graph $G$ has at least one layering, by say putting all of the vertices of $G$ in $L_{0}$. Let $\pi: \mathbf{G r}_{\text {Lyr }} \rightarrow \mathbf{G r}$ denote the projection functor.

Note that the inclusion $i$ : $\mathbf{G r} \hookrightarrow \mathbf{G r}_{r}^{\infty}$ preserves pushouts along monomorphisms and finite limits. Hence by Lemma A.3.4, $\mathbf{G r}_{\mathrm{Lyr}}$ has pushouts along monomorphisms and finite limits, and they are computed as in Gr.

Let $\mathbf{i}=\left(i_{0}, \ldots, i_{n}, \ldots\right)$ denote an infinite sequence of non-negative integers where only finitely many of the $i_{k}$ are non-zero. We say $\mathbf{i}$ is a sequence of finite support and let $\mathbf{I}$ denote the set of all sequences of finite support. Given a sequence $\mathbf{i} \in \mathbf{I}$, let $K^{\mathbf{i}}$ denote the following layered graph. Its $n$th layer $L_{n}$ is the complete graph $K^{i_{n}}$ (where recall that $K^{0}=\varnothing$ ), and for every $x \in V\left(L_{n-1}\right)=V\left(K^{i_{n-1}}\right)$ and $y \in V\left(L_{n}\right)=V\left(K^{i_{n}}\right)$, there is an edge $x y \in K^{\mathbf{i}}$ for $n \geq 1$.

Example 3.7.2. If $\mathbf{i}=(1,2,2,0, \ldots, 0, \ldots)$, then $K^{\mathbf{i}}$ is the graph
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-28.jpg?height=333&width=661&top_left_y=1516&top_left_x=703)

Given a sequence of finite support $\mathbf{i}$, we call $K^{\mathbf{i}}$ a layered complete graph, and we let max(i) denote the maximal $i_{k} \in \mathbf{i}$. We let $\Omega_{n}$ denote the set of layered complete graphs $K^{\mathbf{i}}$ where $\max (\mathbf{i}) \leq n$. Thus there exists a monomorphism $G \hookrightarrow K^{\mathbf{i}}$ if and only if the maximal number of vertices of each layer of $G$ is less than or equal to maxi.

Definition 3.7.3 ([Bos+22, Section 2]). A layered tree decomposition ( $L, d$ ) of a graph $G$ consists of a layering $L$ of $G$ along with a tree decomposition $d$ of the underlying graph $G$. The width of a layered tree decomposition ( $L, d$ ) of a graph $G$ is the maximal number of vertices in the intersection of the bags of $d$ and the layers of $L$, i.e. the width of ( $L, d$ ) is $\max \left|L_{i} \cap d(x)\right|$.

Let $L: G \rightarrow P_{r}^{\infty}$ be a layered graph. Note that if $d: \int T \rightarrow \mathbf{G r}_{\text {Lyr }}$ is a structureddecomposition of $G$ in $\mathbf{G r}_{\text {Lyr }}$, where $T$ is a tree, then we obtain a tree decomposition of $G$ in Gr. Furthermore, using Lemma A.3.4, it is easy to see that to every tree decomposition $d: \int T \rightarrow \mathbf{G r}$ of $G$ taken in $\mathbf{G r}$, there is a unique diagram $d^{\prime}: \int T \rightarrow \mathbf{G r}_{\text {Lyr }}$ with $\pi d^{\prime}=d$, where each bag and adhesion $d^{\prime}(x)$ of $d^{\prime}$ are given the layering $d^{\prime}(x)=d(x) \rightarrow P_{r}^{\infty}$ given by composing with the colimit cocone maps $d(x) \rightarrow G \rightarrow P_{r}^{\infty}$.

In other words, structured decompositions of the form $d: \int T \rightarrow \mathbf{G r}_{\text {Lyr }}$ where $T$ is a tree are equivalent to layered tree decompositions.

Proposition 3.7.4. Layered graphs form a width category $\Gamma=\left(\mathbf{G r}_{\text {Lyr }}\right.$, Trees, $\left.\left\{K^{\mathbf{i}}\right\}_{\mathbf{i} \in \mathbf{I}}\right)$. Furthermore, if $d: \int T \rightarrow \mathbf{G r}_{\text {Lyr }}$ is a structured decomposition, then the width of $d$ is precisely the width of the layered tree decomposition ( $L, d$ ) as in Definition 3.7.3.

Proof. It is easy to check that the conditions for $\Gamma$ to be a monic-stable sd-category hold thanks to Lemma A.3.4. The size of a layered graph $L: G \rightarrow P_{r}^{\infty}$ is clearly the largest number of vertices of its layers. Hence by definition, the width of a decomposition $d: \int T \rightarrow \mathbf{G r}_{\text {Lyr }}$ is the largest bag size $s(d(x))$ minus 1 , which is precisely the maximal number of vertices in the largest layer of each bag minus 1 .

Definition 3.7.5 ([Bos+22, Section 2]). The layered treewidth of a graph $G$ is the minimal width of every layered tree decomposition $(L, d)$ of $G$.

Hence the layered treewidth of a graph $G$ is the minimal $\Gamma$-width of each layered graph in the fiber $\pi^{-1}(G)$ where $\pi: \mathbf{G r}_{\text {Lyr }} \rightarrow \mathbf{G r}$ is the projection functor.

### 3.8 H-Treewidth

Given a class of graphs $\mathscr{H}, \mathscr{H}$-treewidth is a graph invariant introduced in $[\mathrm{Eib}+21]$ for the purpose of obtaining "hybrid" width parameters.

Definition 3.8.1 ([JKW22, Definition 3.4]). Given a class of graphs $\mathscr{H}$, an $\mathscr{H}$-tree decomposition ( $X, T, L$ ) of a graph $G$ consists of a tree decomposition ( $X, T$ ) of $G$ along with a subset $L \subseteq V(G)$ such that

1. for each $v \in L$, there exists a unique leaf $t \in T$ with $v \in X(t)$, and
2. for each $t \in T$, the induced subgraph $G[X(t) \cap L]$ belongs to $\mathscr{H}$.

The width of an $\mathscr{H}$-tree decomposition $(X, T, L)$ is

$$
w(X, T, L)=\max \left(0, \max _{t \in T}|X(t) \backslash L|-1\right)
$$

The $\mathscr{H}$-treewidth $\mathbf{t w}_{\mathscr{H}}(G)$ of a graph $G$ is defined to be the minimal width of all of its $\mathscr{H}$-tree decompositions.

Remark 3.8.2. If $v \in L$, then by (1), it must belong to a unique bag $X(t)$ where $t \in T$ is a leaf vertex. This implies that $X(t) \cap L$ is either a nonempty subset of $X(t)$ and $t$ is a leaf node or $X(t) \cap L=\varnothing$. In other words, $L$ must be a subset of a union of bags indexed by leaf vertices of $T$, and each induced subgraph must belong to $\mathscr{H}$.

Lemma 3.8.3. If ( $X, T, L$ ) is a $\mathscr{H}$-tree decomposition of a graph $G$, let ( $X^{\prime}, T^{\prime}, L^{\prime}$ ) denote the $\mathscr{H}$ tree decomposition of $G$ where to every leaf vertex $t$ we set $X(t)=X(t) \backslash L$, add a new vertex $t^{\prime}$ and a new bag $X\left(t^{\prime}\right)=X(t) \cap L$.

We can easily obtain a width measure on graphs which is comparable to $\mathscr{H}$-treewidth as follows. Let $\Omega^{\mathscr{H}}$ be the spine of $\mathbf{G r}$ where $\Omega_{n}^{\mathscr{H}}=\left\{K^{n}\right\}_{n \geq 0} \cup \mathscr{H}$ for $n \geq 0$.

Proposition 3.8.4. The triple $\Gamma=\left(\mathbf{G r}\right.$, Trees, $\left.\Omega^{\mathscr{H}}\right)$ forms a width category.
Proof. Conditions (W1) and (W3) follow from Proposition 3.1.1. Condition (W2) holds because every graph has a monomorphism to some complete graph, and because there are no monos $K^{n} \hookrightarrow K^{m}$ if $m<n$, and each graph in $\mathscr{H}$ belongs to each $\Omega_{n}^{\mathscr{H}}$, so ( $\mathbf{W} 2 \mathbf{b}$ ) holds there vacuously.

Remark 3.8.5. Note that the size of each $H \in \mathscr{H}$ with respect to $\Gamma$ is 0 .

Proposition 3.8.6. Given a graph $G$, we have

$$
\mathbf{w}_{\Gamma}(G) \leq \mathbf{t} \mathbf{w}_{\mathscr{H}}(G) .
$$

Proof. Given a $\mathscr{H}$-tree decomposition ( $X, T, L$ ), let us construct a new $\mathscr{H}$-tree decomposition ( $X^{\prime}, T^{\prime}, L^{\prime}$ ) with the same width as ( $X, T, L$ ). For each leaf vertex $t \in T$, we set $X^{\prime}(t)=X(t) \backslash L$. We add a new vertex $t^{\prime}$ and a single edge $t t^{\prime}$ to $T$ to form $T^{\prime}$, and set $X^{\prime}\left(t^{\prime}\right)=X(t) \cap L$. Immediately it is clear that $w(X, T, L)=w\left(X^{\prime}, T^{\prime}, L\right)$, and it is also clear that $\left(X^{\prime}, T^{\prime}\right)$ is still a tree decomposition of $G$.

Now let $d: \int T \rightarrow \mathbf{G r}$ denote the structured decomposition of $G$ corresponding to $\left(X^{\prime}, T^{\prime}\right)$. Then by construction $w(d) \leq w\left(X^{\prime}, T^{\prime}, L^{\prime}\right)$, as $d$ may contain bags which belong to $\mathscr{H}$ that are not leaf bags. So if $(X, T, L)$ is a minimal $\mathscr{H}$-tree decomposition of $G$, then

$$
\mathbf{w}_{\Gamma}(G) \leq w(d) \leq w\left(X^{\prime}, T^{\prime}, L\right)=w(X, T, L)=\mathbf{t w}_{\mathcal{H}}(G) .
$$ $\square$

It is easy to see that the reverse inequality does not hold in general. For example, let $G$ be the following graph
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-30.jpg?height=145&width=606&top_left_y=1096&top_left_x=731)
and let $\mathscr{H}=\left\{K^{3}\right\}$. Then there is an obvious tree decomposition where each bag is a $K^{3}$. So $\mathbf{w}_{\Gamma}(G)=0$, but there exists no $\mathscr{U}$-tree decomposition of $G$ with width less than 2 .

### 3.9 Bass-Serre Theory

A well-studied precursor of our structured decompositions originates outside of combinatorics, in the field of geometric group theory. Specifically, graphs of groups, the central objects of BassSerre theory, correspond exactly to structured decomposition of the form $d: \int G \rightarrow \mathbf{G r p}$ in the category of groups and homomorphisms.

By general algebraic considerations, any diagram $A \stackrel{a}{\longleftrightarrow} C \stackrel{b}{\longleftrightarrow} B$ in the category Grp has a colimit. One can construct the colimit as the quotient of the free product $A * B$ by the normal closure of the set $\left\{a(x) b(x)^{-1} \mid x \in C\right\}$. As customary in the group theory literature, we call the colimit a free product with amalgamation of $A, B$ over $C$ and (suppressing the monomorphisms) denote it $A{ }^{*}{ }_{C} B$.

Fix a group $H$ and a graph $D$. Bass-Serre theory (introduced in Arbres, amalgames, $S L_{2}$ [Ser77], later translated into English under the title Trees [Ser80]) exhibits a correspondence between:

- actions of $H$ on barycentric subdivisions of a tree ${ }^{14} T$ with quotient graph $D$, and
- graphs of groups on $D$ with fundamental group $H$, where a graph of groups is precisely a (not necessarily tree-shaped) structured decomposition $d: \int G \rightarrow \mathbf{G r p}$.

As long as the quotient graph itself is a tree, the colimit of the graph of groups $d: \int D \rightarrow \operatorname{Grp}$ coincides with the fundamental group. Thus, by Bass-Serre theory, tree-structured decompositions of a group $G$ correspond to well-behaved actions of $G$ on trees.

Using this correspondence, one can equip the category of groups with the structure of a spined sd-category, and characterize the resulting width notion. However it turns out that $\Gamma$-width is less interesting than the $(\mathcal{L}, \Omega)$-width of Definition 2.6.1.

[^10]This also serves as an example of a spined sd-category which is not stable, but is nonetheless well-behaved enough to admit a notion of monotonicity (Corollary 3.9.12) for $(\mathcal{G}, \Omega)$-width. We will give a simple example of an action with tree quotient in Example 3.9.5.

Definition 3.9.1. For $n \in \mathbb{N}$, let $\Omega_{n}$ denote the class of all groups with order at most $n$. The sd-category of groups is the sd-category $\Gamma_{\text {BS }}=(\operatorname{Grp}$, Trees, $\Omega)$ where $\Omega=\left\{\Omega_{n} \mid n \geq 0\right\}$.

Clearly, $\Gamma_{\mathrm{BS}}$ is a spined sd-category. Let $w_{\mathrm{BS}}$ denote the $(\mathcal{L}, \Omega)$-width of Definition 2.6.1 for $\Gamma_{\text {BS }}$. We say that an object $X$ in an sd-category ( $\mathcal{C}, \mathcal{G}, \Omega$ ) has infinite ( $\mathcal{L}, \Omega$ )-width if there exists no ( $\mathcal{C}_{\mathcal{L}}, \Omega$ )-structured decomposition of $X$, i.e. $X$ is not chordal.

Now since Grp contains both finite and infinite groups, let us begin by characterizing the behavior of $w_{\mathrm{BS}}$ on finite groups. To aid with this, we introduce the notion of inseparable object.

Definition 3.9.2. Consider a category $C$ and an object $K$ of $C$. We call $K$ inseparable if for any pushout $A+_{C} B$ and monomorphism $\iota: K \hookrightarrow A+_{B} C$ in $C$, one can find a monomorphism $\iota_{A}: K \hookrightarrow A$ or a monomorphism $\iota_{B}: K \hookrightarrow B$.

Keep in mind that Definition 3.9.2 does not imply that the monomorphism $\iota: K \rightarrow A+{ }_{B} C$ factors through either $\iota_{A}$ or $\iota_{B}$.

Lemma 3.9.3. In the category Grp of groups, every finite group is inseparable.
Proof. Immediate from [Ser80], Theorem 8. $\square$

Corollary 3.9.4. For a finite group $G$, we have $w_{\mathrm{BS}}(G)=|G|$.
Proof. Since the one-vertex graph is a permitted structure graph, we have $w_{\mathrm{BS}}(G) \leq|G|$. Now assume that $G$ admits a (Trees, $\Omega$ )-structured decomposition $d: \int T \rightarrow \mathbf{G r p}$ of width $n<|G|$. Then we have some vertex $v \in V(T)$ so that $|d(v)|<n$. But $G$ is a subobject of itself (i.e. the colimit of $d$ ), so Lemma 3.9.3 guarantees that $G$ is a subobject of $d(v)$. But then $|G| \leq n<|G|$, a contradiction. Thus, $w_{\mathrm{BS}}(G)=|G|$. $\square$

Before characterizing the width of infinite groups, we present the simplest nontrivial example of a group acting on the barycentric subdivision of a tree with a tree quotient.

Example 3.9.5. Consider the infinite path $P_{\mathbb{Z}}$ with vertex set the integers ( $V\left(P_{\mathbb{Z}}\right)=\mathbb{Z}$ ), and edges connecting $x, y \in \mathbb{Z}$ precisely when $|x-y|=1$. We depict the resulting tree (all black vertices) and its barycentric subdivision (black and white vertices) below:
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-31.jpg?height=145&width=1185&top_left_y=1973&top_left_x=495)

The infinite dihedral group $D_{\infty}$, presented as $\left\langle a, b \mid a^{2}=b^{2}=1\right\rangle$ acts on the integers by

$$
\begin{aligned}
& a(x)=0-x \\
& b(x)=1-x
\end{aligned}
$$

We can extend this to an action of $D_{\infty}$ on the barycentric subdivision of the tree $P_{\mathbb{Z}}$. The generator $a$ then acts by turning the tree 180 degrees around the zero vertex, whereas the generator $b$ acts by turning the tree 180 degrees around the midpoint $\frac{1}{2}$ between 0 and $1(b)$. Computing the quotient yields the graph $K^{2}$,

-     - o
and $K^{2}$ is a tree. By Bass-Serre theory, we can thus write $D_{\infty}$ as the colimit of some $K^{2}$ structured decomposition. The theory even lets us determine the appropriate bags and adhesions by considering vertex and edge stabilizers, but here we can read off such a decomposition purely from the presentation of $D_{\infty}$ given above: $D_{\infty}$ arises as the colimit of the span
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-32.jpg?height=54&width=503&top_left_y=479&top_left_x=781)
i.e. the diagram $d: \int K^{2} \rightarrow \mathbf{G r p}$ with bags $d(\bullet)=d(\circ)=\mathbb{Z} / 2 \mathbb{Z}$ and adhesion $d(-)=\{1\}$.
Remark 3.9.6. Example 3.9 .5 shows that $w_{\mathrm{BS}}\left(D_{\infty}\right) \leq 2$. Hence the width notion $w_{\mathrm{BS}}$ is nontrivial. It also shows that infinite groups are generally not inseparable in Grp. For example, the morphism that maps 1 to the product of the two generators $a b$ is a monomorphism from $\mathbb{Z}$ to $D_{\infty}$, even though no monomorphism of signature $\mathbb{Z} \hookrightarrow \mathbb{Z} / 2 \mathbb{Z}$ exists. This also shows the failure of monic-stability in the sd-category $\Gamma_{B S}$.

We now characterize the width of infinite groups. Specifically, we will show that for every bounded width group $G$, the order of the largest finite subgroup $W<G$ coincides with $w_{\mathrm{BS}}(G)$.

Proposition 3.9.7. Consider a group $G$ such that $w_{\mathrm{BS}}(G)$ is finite and let $W<G$ be a finite subgroup. Then every decomposition of $G$ has width bounded below by $|W|$.

Proof. Consider a tree decomposition $d: \int T \rightarrow \mathbf{G r p}$ of width $n$. By repeated applications of Lemma 3.9.3, $W$ is a subobject of some bag $d(v)$. But then $|W| \leq d(v) \leq n$.

We now show that the order of a maximal finite subgroup also upper bounds the width of the group. Recall that a group is virtually free if it has a free subgroup of finite index. Since the free group on no generators (the trivial group $\{1\}$ ) has finite index in any finite group, in what follows we regard finite groups as virtually free.

Lemma 3.9.8. Subgroups of virtually free groups are virtually free.
Proof. Immediate from the Nielsen-Schreier theorem (subgroups of free groups are free).
Lemma 3.9.9. Groups of finite width are virtually free.
Proof. See [Ser80], Proposition 11.
Remark 3.9.10. Lemma 3.9.9 gives an easy example of a group with unbounded width: $w_{\mathrm{BS}}\left(\mathbb{Z}^{2}\right)=\infty$.

Proposition 3.9.11. Consider a finite-width group $G$ and let the nontrivial finite subgroup $W<G$ have maximal order. Then $G$ has a decomposition of width at most $|W|$.

Proof. Since $G$ has finite width, all finite subgroups of $G$ have order at most $v$. A result of Linnel [Lin83] shows that one can write all such groups as free products with amalgamation where the edge groups are all finite, and the vertex groups are subgroups of $G$ with Cayley graphs that have at most one end. By Lemma 3.9.9 the vertex groups are themselves virtually free. The Cayley graph of a virtually free group has either zero, two or infinitely many ends. Thus, in this case the vertex groups have no ends, and are finite as required. This yields a decomposition of $G$ whose bags are finite subgroups of $F$. Since $W$ has maximal order among the finite subgroups, this decomposition has width at most $|W|$ as required.

From Propositions 3.9.7 and 3.9.11 it follows that, as long as a group $\Gamma$ has a nontrivial finite subgroup of maximal order, its width is this maximal order.

Corollary 3.9.12. Consider a group $G$. Then either $w_{\mathrm{BS}}(G)=\infty$, or else $w_{\mathrm{BS}}(G)$ is the order of a maximal-order finite subgroup of $G$. Consequently, when $H<G$ and both $w_{\mathrm{BS}}(G)<\infty$ and $w_{\mathrm{BS}}(H)<\infty$ hold, then $w_{\mathrm{BS}}(H) \leq w_{\mathrm{BS}}(G)$ holds as well.

The failure of pullback-stability and monic-stability in $\Gamma_{B S}$ sheds light on a general phenomenon: in Gr, subobjects of well-behaved objects usually remain similarly well-behaved. This is very far from the case in algebra: for example, a subgroup of a finitely presented group will in general fail to have a finite presentation. Moreover, via the Bass-Serre correspondence, the general theory developed in Section 2 lets us conclude facts purely about group actions as corollaries. We present one example of this below.

Corollary 3.9.13. If a group $G$ acts on the barycentric subdivision of a tree with a tree-shaped quotient $T$, then $G$ acts on some other tree with a binary tree quotient $T^{\prime}$.

Proof. Use Bass-Serre theory to obtain a (Gr, Trees, $\Omega$ )-decomposition of $G$. Apply Proposition 2.9.2 to obtain a (Gr, BTrees, $\Omega$ )-decomposition of $G$. Using the Bass-Serre correspondence in reverse yields the desired action.

### 3.10 Hybrid Dynamical Systems

The thesis [Ame06] sets up a framework with which to discuss hybrid systems categorically, where here a hybrid system is a dynamical system that has both discrete and continuous components.

Definition 3.10.1 ([Ame06, Definition 1.6]). A D-category is a small category $C$ such that

1. for every object $X \in C, X$ is either the domain or codomain of a non-identity morphism, but not both, and
2. if $X \in C$ is the domain for a non-identity morphism $f: X \rightarrow Y$, then there exists exactly one other morphism $g: X \rightarrow Z$ in $C$ with domain $X$.

Clearly if $G$ is a (possibly infinite) digraph, then $\int G$ is a $D$-category. Ames defines a corresponding notion of functor of $D$-categories, resulting in a category DCat of $D$-categories, and the Grothendieck construction extends to a functor $\int: \mathbf{d G r}^{\infty} \rightarrow$ DCat.

Theorem 3.10.2 ([Ame06, Theorem 1.1]). The functor

$$
\int: \mathbf{d G r}^{\infty} \rightarrow \text { DCat, }
$$

is an isomorphism of categories.
Definition 3.10.3 ([Ame06, Definition 1.9]). A hybrid object in a category $C$ is a functor $d$ : $I \rightarrow C$ where $I$ is a $D$-category.

So hybrid objects for Ames are precisely our structured decompositions. The main object of study for this thesis is the notion of a hybrid system, which turns out [Ame06, Proposition 2.1] to be equivalent to certain hybrid objects in a category of smooth manifolds.

## 4 Future Work

In this brief section we consider possible avenues for future research.

## Other Shapes

Recall that a $G$-shaped structured decomposition valued in some category $C$ is just a diagram $d: \int G \rightarrow C$ whose shape is given by the Grothendieck construction applied to a graph $G$. In principle there is nothing stopping us from letting $G$ be another kind of presheaf and indeed, one could for instance study structured decompositions whose shapes are given not by graphs, but simplicial complexes or other combinatorial objects.

## Obstructions to Low Width

In graph-theory, one natural direction for further work is to characterize what obstacles prevent general objects from admitting structured decompositions of low width. When it comes to graphs and tree-shaped structured decompositions, there is a well-established theory of obstacles to having low tree-width, including notions such as brambles [ST93], $k$-blocks [Car+14], tangles [RS91] and abstract separation systems [DHL19]. It is a fascinating, but highly nontrivial research direction to lift these ideas to the more general, category-theoretic setting of structured decompositions.

## Co-Decompositions

Zooming out, the focus of this paper has been to investigate which combinatorial invariants can be expressed as colimits. In particular, in a structured decomposition category we think of objects as being decomposed if they arise as colimits of a structured decompositions. An obvious question for future work is to dualize these ideas: rather than building objects as colimits, we might want to build objects as limits. Thus one has the notion of a strctured co-decomposition, namely diagrams of the form $d:\left(\int G\right)^{\mathrm{op}} \rightarrow C$ which are thought to decompose an object $X \in C$ if $\lim d \cong X$. It is not at all clear what graph classes can be captured via structured co-decompositions and indeed even the case of path-shaped structured co-decompositions of graphs seems to yield interesting graph classes. Preliminary investigation suggests that graphs of bounded tree-co-width should admit a highly symmetric structure, but much further research is still needed to understand the structure of such graphs. We believe that this is a fascinating direction for future work harboring many applications in graph theory and algorithmics.

## Submodular Width Measures

The astute reader will notice that nearly all of our examples come from tree shaped decompositions. Other important width measures for graphs exist that are not asymptotically equivalent to tree width, such as clique-width, mim-width and sim-width [Bre+23]. Each of these width measures can be obtained using a submodular function and branch decompositions. Studying the relationship between these submodular width measures and width categories is future work.

## Generalized Hypertreewidth

In Section 3.5, we showed how to capture hypergraph treewidth using width categories. Hypergraph treewidth is already a useful invariant of hypergraphs in algorithmics. For example the Conjunctive Query Containment Problem is polynomial time solvable on hypergraphs of bounded Gaifman treewidth [KV98]. However, as discussed in [Hli+08, Section 5.2], there exists a notion of hypergraph acyclicity, called $\alpha$-acyclicity [Fag83], which is not well behaved with respect to hypergraph treewidth. Namely there exist classes of $\alpha$-acyclic hypergraphs that have unbounded hypergraph treewidth. The asymptotically equivalent width measures of hypertreewidth and generalized hypertreewidth, introduced in [GLS99], do not suffer from this
defect. We note that generalized hypertreewidth $\mathbf{g h w}(H)$ of a hypergraph $H$ can be defined using tree decompositions where the measure of size for the bags of the decomposition is given by the edge cover number. This is problematic for our formalism, as edge cover number is not monotonic with respect to monomorphisms of hypergraphs, and hence there exists no spine on Hyp which we can use to capture generalized hypertreewidth. So far we have been unable to find another category of hypergraphs where edge cover number is monotonic with respect to the monomorphisms. This suggests expanding the definition of spine and possibly also considering pushing forward structured decompositions (as in [BFT24]) rather than pulling them back. This avenue of research is future work.

## A Categories of Graphs

In this appendix, we detail some facts about categories of graphs. First we give an overview of several categories of graphs we are considering, and then examine the categories $\mathbf{G r}$ and $\mathbf{G r}_{\text {mlt }}$ more deeply.

## A. 1 Overview

There are many different notions of graphs, with different corresponding categories. These various categories, their properties and relationships are at this point well understood [BL+86; Bro+08; Ple11; Sch19; Cam21]. Thus we will only quickly review the relevant categories for our purposes.

Definition A.1.1. Let dGrSch ${ }^{15}$ denote the category with two objects and two non-identity morphisms

$$
E \underset{t}{\stackrel{s}{\rightrightarrows}} V
$$

Then let $\mathbf{d G r}=$ Fun(dGrSch, FinSet). We call the objects of this category directed multigraphs. By this we mean that the edges of the graph are directed, there can be multiple edges and loops at vertices. Morphisms are directed graph homomorphisms.

Definition A.1.2. Let sGrSch denote the category given by
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-35.jpg?height=88&width=259&top_left_y=1731&top_left_x=900)
and where $t=s i, s=t i$ and $i i=1_{E}$. Let $\mathbf{s G r}=$ Fun(sGrSch, FinSet). We call the objects of this category symmetric multigraphs.

The objects of this category can be thought of as symmetric directed graphs, where the involution $i$ sends a directed edge to the same edge with the opposite direction. This does introduce a mild pathology however, as loops on vertices can be their own involution, and such loops cannot be mapped to arbitrary loops in other graphs ${ }^{16}$.

We similarly have a reflexive version of sGr.
Definition A.1.3. Let $\mathbf{s G r} \mathbf{r}_{r} \mathbf{S c h}$ denote the category given by

$$
i C E \underset{t}{\stackrel{s}{\leftarrow u}} V
$$

and where $t=s i, s=t i, s u=t u=1_{V}, i u=u$ and $i i=1_{E}$. Let $\mathbf{s G r} \mathbf{r}_{r}=$ Fun( $\mathbf{s G} \mathbf{r}_{r} \mathbf{S c h}$, FinSet). We call the objects of this category reflexive symmetric multigraphs.

[^11]Although dGr, $\mathbf{s G r}$ and $\mathbf{s G r}_{r}$ are categorically nice, being toposes, we are primarily interested in undirected graphs. Let us introduce the categories of graphs under consideration.

We have already seen the category $\mathbf{G r}$ of graphs (Definition 2.1.1). We will explore it more deeply in the next section. Another practical choice for a category of graphs is the category of loop graphs.

Definition A.1.4. By a loop graph, we mean a finite set equipped with a binary, symmetric relation. A morphism $f: G \rightarrow H$ of loop graphs consists of a function $V(f): V(G) \rightarrow V(H)$ which preserves the relation. We let $\mathbf{G r}_{\ell}$ denote the category of loop graphs. We can visualize these objects as simple graphs with loops allowed.

We call a loop graph irreflexive if it has no loops and reflexive if every vertex has a loop. Thus we can obtain $\mathbf{G r}$ as the full subcategory of $\mathbf{G r}_{\ell}$ on the irreflexive loop graphs, and we let $\mathbf{G} \mathbf{r}_{r}$ denote the full subcategory of reflexive loop graphs. The category $\mathbf{G r}_{r}$ can also be thought of as the category whose objects are simple graphs, but where morphisms are allowed to collapse edges.

We can characterize the categories $\mathbf{G r}_{\ell}$ and $\mathbf{G r}_{r}$ as reflective subcategories of $\mathbf{s G} \mathbf{r}$ and $\mathbf{s G} \mathbf{r}_{r}$ respectively.

Definition A.1.5. We say that a small category $C$ is terminally concrete if it has a terminal object *, and such that the functor

$$
C(*,-): C \rightarrow \text { Set }
$$

is faithful. If $C$ is terminally concrete, then a presheaf $X: e^{\mathrm{op}} \rightarrow$ Set is concrete if for every $U \in C$, the canonical map

$$
X(U) \rightarrow \operatorname{Set}(C(*, U), X(*))
$$

is injective.
Proposition A.1.6 ([BH11, Lemma 47]). Given a terminally concrete category $C$, the category of concrete presheaves on $C$ is a reflective subcategory of presheaves on $C$

$$
\operatorname{Con} \operatorname{Pre}(C) \underset{i}{\stackrel{\text { Con }}{\stackrel{\text { t }}{r}} \operatorname{Pre}(C)}
$$

Furthermore this still holds if we consider categories of presheaves of finite sets.
The category $\mathbf{G r}_{\ell}$ is precisely the category of concrete presheaves of finite sets on $\mathbf{s G r S c h}{ }^{\mathrm{op}}$, and $\mathbf{G r}_{r}$ is precisely the category of concrete finite presheaves of finite sets on $\mathbf{s G} \mathbf{r}_{r} \mathbf{S c h}{ }^{\mathrm{op}}$. Hence both $\mathbf{G r}_{\ell}$ and $\mathbf{G r}_{r}$ are quasitoposes. These are very nice categories, which are finitely (co)complete, locally cartesian closed, and have a weak subobject classifier [BH11, Definition 8].
Definition A.1.7. If $S$ is a finite set, let $S^{(2)}$ denote ${ }^{17}$ the set $S^{2}$ quotiented by the relation $(x, y) \sim(y, x)$. A multigraph $G$ consists of two finite sets $V(G), E(G)$ and a function $\partial: E(G) \rightarrow V(G)^{(2)}$. We can visualize these as unordered graphs that can have multiple loops and parallel edges. Morphisms $f: G \rightarrow H$ of multigraphs are then functions $V(f): V(G) \rightarrow V(H)$ and $E(f): E(G) \rightarrow E(H)$ making the following diagram commute
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-36.jpg?height=209&width=378&top_left_y=2339&top_left_x=845)

[^12]We note that the category of multigraphs has all finite limits and colimits but is not cartesian closed [Ple11, Proposition 2.3.1].

Remark A.1.8. We see that there is a chain of fully faithful functors $\mathbf{G r} \hookrightarrow \mathbf{G r}_{\ell} \hookrightarrow \mathbf{G r}_{\mathrm{mlt}}$, and furthermore note that each functor preserves finite limits and pushouts of spans of monomorphisms. There is a left adjoint $L_{\mathrm{mlt}}: \mathbf{G r}_{\mathrm{mlt}} \rightarrow \mathbf{G r}_{\ell}$ to the inclusion, given by collapsing multiple edges.

We can also embed $\mathbf{G r}_{r} \hookrightarrow \mathbf{G r}_{\ell}$ by just thinking of reflexive graphs as graphs where every vertex has a loop. This has a left adjoint $L_{\ell}: \mathbf{G r}_{\ell} \rightarrow \mathbf{G r}_{r}$ that just adds a loop to every vertex of a loop graph if it doesn't already have one.

Lemma A.1.9 ([Ple11, Proposition 2.3.13, 2.3.14]). A map $f: G \rightarrow H$ of (reflexive/loop) graphs is a mono/epimorphism in $\left(\mathbf{G r}_{r} / \mathbf{G r}_{\ell}\right) \mathbf{G r}$ if and only if $V(f)$ is an in/surjective function. A map $f: G \rightarrow H$ of multigraphs is a mono/epimorphism in $\mathbf{G r}_{\text {mlt }}$ if and only if both $E(f)$ and $V(f)$ are in/surjective functions.

Remark A.1.10. We took the term loop graph from [nLa24] and the term multigraph from [Die10, Section 1.10]. In [nLa24] what we call multigraphs are called pseudographs.

We summarize the relationships between our notation and that of [Ple11], along with the properties of the categories.

| Graph name | Category | Plessas | Categorical properties |
| :--- | :--- | :--- | :--- |
| simple graphs | Gr | SiLlStGraphs | products, pullbacks, pushouts of monos |
| loop graphs | $\mathbf{G r}_{\ell}$ | SiStGraphs | quasitopos |
| reflexive loop graphs | $\mathbf{G r}_{r}$ | SiGraphs | quasitopos |
| multigraphs | $\mathbf{G r}_{\text {mlt }}$ | StGraphs | finite (co)limits, regular |

Table 1: Different notation for categories of graphs.

## A. 2 Simple Graphs

The category that is perhaps closest to what combinatorialists and computer scientists think of for simple graphs we call $\mathbf{G r}$ (Definition 2.1.1). This is the category whose objects are finite sets equipped with a binary, symmetric, irreflexive relation, and whose morphisms are functions that preserve the relation. We summarize some of the properties of this category below. For relations to other categories of graphs see Section A. 1

Let us work out some of the structure of $\mathbf{G r}$. First we note that there is a functor $V: \mathbf{G r} \rightarrow$ FinSet that gives the set of vertices of a graph. This functor has a left adjoint Disc : Set $\rightarrow \mathbf{G r}$ that sends a finite set $S$ to the discrete graph $\operatorname{Disc}(S)$. Therefore, $V$ must preserve whatever limits $\mathbf{G r}$ has. So we can conclude that $\mathbf{G r}$ does not have a terminal object. If it did, call it *, then $V(*) \cong \mathbf{1}$, where $\mathbf{1}$ denotes a singleton set. There is only one graph with a single vertex, which we denote by • . But any graph with an edge does not have a map to • Therefore $\mathbf{G r}$ does not have a terminal object. However it does have binary products. Given $G, H \in \mathbf{G r}, G \times H$ is the graph with $V(G \times H)=V(G) \times V(H)$ and where $(g, h)\left(g^{\prime}, h^{\prime}\right) \in E(G \times H)$ if and only if $g g^{\prime} \in E(G)$ and $h h^{\prime} \in E(H)$. The category $\mathbf{G r}$ also has pullbacks. If $f: G \rightarrow K$ and $g: H \rightarrow K$ are maps of graphs, then $G \times_{K} H$ is the graph with $V\left(G \times_{K} H\right)=V(G) \times_{V(K)} V(H)$ and where $(g, h)\left(g^{\prime}, h^{\prime}\right) \in E\left(G \times_{K} H\right)$ if and only if $g g^{\prime} \in E(G)$ and $h h^{\prime} \in E(H)$. Therefore it also has equalizers. Note that $\mathbf{G r}$ is not cartesian closed [Ple11, Proposition 2.3.6].

The category $\mathbf{G r}$ clearly has an initial object given by the empty graph $\varnothing$, and it has finite coproducts, where $G+H$ is the graph with $V(G+H)=V(G)+V(H)$ and $E(G+H)=E(G)+E(H)$. The category Gr does not have all pushouts in general, see [BK23, Page 7]. However it does have pushouts along spans of monomorphisms.

Definition A.2.1. Let $i: G \rightarrow H$ and $j: G \rightarrow K$ be monomorphisms in Gr. Let $H+_{G} K$ be the graph defined as follows. Let $V\left(H+_{G} K\right)$ be the pushout $V(H)+_{V(G)} V(K)$, i.e. the set $V(H)+V(K) / \sim$, where $\sim$ is the smallest equivalence relation such that for $h \in V(H)$ and $k \in V(K), h \sim k$ if there exists a $g \in V(G)$ such that $i(g)=j(g)$. Since $i$ and $j$ are monomorphisms, $V(i)$ and $V(j)$ are injective. Given $h \in V(H), k \in V(K),[h]=[k]$ in $V\left(H+_{G} K\right)$ if and only if there exists a finite zig-zag of elements
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-38.jpg?height=179&width=1307&top_left_y=568&top_left_x=379)
i.e. $i\left(g_{0}\right)=h, j\left(g_{0}\right)=k_{0}, j\left(g_{1}\right)=k_{0}, \ldots, j\left(g_{n}\right)=k$. But since $V(i)$ and $V(j)$ are injective, this means that $g_{0}=g_{1}=\cdots=g_{n}$. Thus if $[h]=[k]$, then there exists a two-arrow zig-zag of elements
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-38.jpg?height=168&width=323&top_left_y=922&top_left_x=872)
in other words, there exists a unique $g \in V(G)$ such that $i(g)=h$ and $j(g)=k$. Thus every element $x \in V\left(H+_{G} K\right)$ can either be represented uniquely by an $h \in V(H)$ such that $i^{-1}(h)=\varnothing$, a $k \in V(K)$ such that $j^{-1}(k)=\varnothing$, or there exists a unique $g \in V(G)$ such that $x=[i(g)]=[j(g)]$. This also implies that for $h, h^{\prime} \in V(H)$, if $[h]=\left[h^{\prime}\right]$, then $h=h^{\prime}$, and similarly for $V(K)$.

Now let us define $E\left(H+_{G} K\right)$. For $x, y \in V\left(H+_{G} K\right)$ there is an edge $x y \in E\left(H+_{G} K\right)$ if and only if $x \neq y$ and there exists an edge $h h^{\prime} \in E(H)$ such that $x=[h], y=\left[h^{\prime}\right]$ or $k k^{\prime} \in E(K)$ such that $x=[k], y=\left[k^{\prime}\right]$. Thus $H+_{G} K$ is a well-defined graph.

Let $r: H \rightarrow H+{ }_{G} K$ and $s: K \rightarrow H+{ }_{G} K$ be defined simply as the quotient map on vertices. They are easily seen to be graph morphisms.

Lemma A.2.2. Given a span of monomorphisms in Gr
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-38.jpg?height=195&width=291&top_left_y=1695&top_left_x=886)
their pushout exists, and furthermore the maps $r$ and $s$ are monomorphisms as well.
Proof. Suppose that $p, q: G \rightarrow Q$ are graph homomorphisms such that $p a=q b$. By the universal property of pushouts in Set, there exists a unique $\ell: V\left(H+_{G} K\right) \rightarrow V(Q)$ such that $\ell r=p$ and $\ell s=q$, given by $\ell(x)=p(h)$ if $x=[h]$ or $\ell(x)=q(k)$ if $x=[k]$. If $x y \in E\left(H+_{G} K\right)$, then we want to show that $\ell(x) \ell(y) \in E(Q)$. But if $x y \in E\left(H+_{G} K\right)$, then there must be either an edge $h h^{\prime} \in E(H)$ or $k k^{\prime} \in E(K)$ that quotient to $x y$. Thus $p(h) p\left(h^{\prime}\right) \in E(Q)$ or $q(k) q\left(k^{\prime}\right) \in E(Q)$, but then $\ell(x) \ell(y)=\ell[h] \ell\left[h^{\prime}\right]=p(h) p\left(h^{\prime}\right)$ or $\ell(x) \ell(y)=\ell[k] \ell\left[k^{\prime}\right]=q(k) q\left(k^{\prime}\right)$. Thus $\ell$ is a graph homomorphism such that $\ell r=p$ and $\ell s=q$. Hence $H+_{G} K$ is a pushout in Gr.

Now suppose that $r(h)=r\left(h^{\prime}\right)$ for $h, h^{\prime} \in V(H)$. Then $[h]=\left[h^{\prime}\right]$ in $V(H)+_{V(G)} V(K)$. But by the discussion above, this implies that $h=h^{\prime}$. Similarly, $s$ is a monomorphism. $\square$

Given a graph $G$, a subgraph of $G$ is a graph $H$ with $V(H) \subseteq V(G)$. We say that $H$ is an induced subgraph if for all $x, y \in V(H)$, there is an edge $x y \in E(H)$ if and only $x y \in E(G)$. We write $H \subseteq G$ to mean that $H$ is a subgraph of $G$. We will sometimes also call a monomorphism $i: H \hookrightarrow G$ a subgraph, though we really mean the isomorphism equivalence class of $i$. If $G$ is a graph, then subgraphs of $G$ are in bijection with subobjects of $G$ in $\mathbf{G r}$.

Given a graph $G$ and subgraphs $H, K \subseteq G$, let $H \cap K$ denote the subgraph of $G$ with $V$ ( $H \cap K)=V(H) \cap V(K)$ and $E(H \cap K)=E(H) \cap E(K)$. We call $H \cap K$ the intersection of $H \subseteq G$ and $K \subseteq G$. There are monomorphisms $i_{H}: H \cap K \hookrightarrow H$ and $i_{K}: H \cap K \hookrightarrow K$.

Similarly we let $H \cup K$ denote the subgraph of $G$ with $V(H \cup K)=V(H) \cup V(K)$ and where there is an edge $x y \in E(H \cup K)$ if and only if $x, y \in V(H)$ and $x y \in E(H)$ or $x, y \in V(K)$ and $x y \in E(K)$. We note that there are monomorphisms $j_{H}: H \hookrightarrow H \cup K$ and $j_{K}: K \hookrightarrow H \cup K$.

Lemma A.2.3. Given a graph $G$ and subgraphs $H, K \subseteq G$, then the following square commutes and is a pullback
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-39.jpg?height=186&width=268&top_left_y=657&top_left_x=900)
furthermore, the following square commutes and is a pushout
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-39.jpg?height=207&width=339&top_left_y=952&top_left_x=863)

Lemma A.2.4. Suppose that the following commutative square
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-39.jpg?height=191&width=218&top_left_y=1274&top_left_x=922)
is a pushout of monomorphisms in $\mathbf{G r}$. Then the pullback diagram
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-39.jpg?height=195&width=272&top_left_y=1585&top_left_x=900)
is also a pushout, $V(G)=V(H \cap K)$, and $G \subseteq H \cap K$.
Proof. Suppose we have a commutative diagram of the form
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-39.jpg?height=298&width=725&top_left_y=1978&top_left_x=671)
we want to construct the dashed map $h$. First we note that the unique map $\ell: G \rightarrow H \cap K$ obtained from the universal property of the pullback must be a monomorphism since, for instance, $i_{K} \ell=g$ is a monomorphism. Hence, as subgraphs, $G \subseteq H \cap K$. Now since $a i_{H}=b i_{K}$, we have $a f=b g$. Thus there exists a unique map $h: P \rightarrow Q$ such that $h r=a$ and $h s=b$. But this implies that $P$ is a pushout of $i_{K}$ and $i_{H}$, which is what we wanted to show. Now clearly $V(G) \subseteq V(H \cap K)$. But by construction $V(P)=V(H)+_{V(G)} V(K)$. So the only way that a point $x \in V(P)$ can be considered as a vertex of the subgraph $G$ is if there exists a $z \in V(G)$ such that $x=[f(z)]=[g(z)]$. So if $x \in V(H) \cap V(K)$, then $x \in V(G)$. $\square$

We furthermore note that pushouts along monomorphisms are pullback-stable. This observation is important for the proof of Proposition 3.1.1.

Lemma A.2.5. Suppose that we have a diagram in $\mathbf{G r}$ of the form
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-40.jpg?height=465&width=570&top_left_y=461&top_left_x=742)
where $h_{0}, h_{2}$ are monomorphisms and the four vertical faces are all pullbacks. If $H$ is a pushout, then so is $G$.

Proof. We first note that the functor $V: \mathbf{G r} \rightarrow$ Set preserves finite limits and pushouts along spans of monomorphisms. Hence applying $V$ to the diagram, we know that $V(G) \cong V\left(G_{0}\right)+_{V\left(G_{1}\right)} V\left(G_{2}\right)$ since Set has universal colimits. Now suppose we have a commutative diagram
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-40.jpg?height=323&width=398&top_left_y=1279&top_left_x=829)
we wish to define a unique dashed map $h$. Applying $V$, we obtain a unique map $V(h): V(G) \rightarrow V(Q)$ by the universal property of the pushout in Set. We want to show that this is a graph homomorphism. Suppose that $x y \in E(G)$. Then $f(x y) \in E(H)$, and hence since $H$ is a pushout, there exists some $v v^{\prime} \in E\left(H_{0}\right)$ or $w w^{\prime} \in E\left(H_{2}\right)$ such that $f(x y)=[v]\left[v^{\prime}\right]$ or $f(x y)=[w]\left[w^{\prime}\right]$. But $G_{0}$ and $G_{2}$ are pushouts, hence there exists $x_{0} y_{0} \in E\left(G_{0}\right)$ or $x_{1} y_{1} \in E\left(G_{1}\right)$ such that $f_{0}\left(x_{0} y_{0}\right)=v v^{\prime}$ or $f_{1}\left(x_{1} y_{1}\right)=w w^{\prime}$. Since $p$ and $q$ are graph homomorphisms, this implies that $h(x y)=p\left(x_{0} y_{0}\right) \in E(Q)$ or $h(x y)=q\left(x_{1} y_{1}\right) \in E(Q)$. Hence $h$ is a graph homomorphism, and thus $G$ is a pushout. $\square$

Remark A.2.6. Lemma A.2.5 is equivalent to saying that $\mathbf{G r}$ has universal pushouts alongs spans of monomorphisms. This is closely related to, but is more general than, the concept of adhesivity, see $[\mathrm{LS} 04]^{18}$.

Now let us show that colimits of tree decompositions (Definition 2.8.1) always exist in Gr.
Definition A.2.7. We say a category $C$ is connected if it is non-empty, and for every pair of objects $c, c^{\prime} \in C$ there exists of a finite zig-zag of the form

$$
c \longrightarrow c_{0} \longleftarrow c_{1} \longrightarrow \ldots \longleftarrow c_{n} \longrightarrow c^{\prime}
$$

or of the form where the direction of any of the arrows is reversed, in $C$.

[^13]We now wish to define what it means for a category to be simply connected. To do this, we need to discuss the Gabriel-Zisman localization of a small category at the set of all of its morphisms. This construction first appeared in [GZ67], but is now well-known. For an indepth discussion see [Sim05]. We will merely sketch its construction here.

Definition A.2.8. Given a small category $C$, let $\widetilde{C}$ denote the category with the same objcts as $C$ and whose morphisms consist of equivalence classes of finite zig-zags consisting of morphisms in $C$ and $C^{\mathrm{op}}$ under the smallest equivalence relation such that

- adjacent arrows pointing in the same direction may be composed,
- adjacent pairs of the forms

$$
c \stackrel{f}{\leftarrow} d \xrightarrow{f^{\mathrm{op}}} c, \quad d \xrightarrow{f^{\mathrm{op}}} c \stackrel{f}{\leftarrow} d
$$

are equivalent to identities, and

- identity arrows pointing either forwards or backwards may be removed.

Note that $\widetilde{C}$ is a groupoid. We say that a small, connected category $C$ is simply connected if $\widetilde{C}$ has precisely one morphism between any two objects.

In other words, a category is simply connected if it is connected and there are no "nontrivial" zig-zags from each object to itself.

Example A.2.9 ([Par90, Page 733]). If a category $C$ is finitely cofiltered, i.e. every finite diagram in $\mathcal{C}$ has a cone, then it is simply connected.

By a beautiful result of Paré [Par90, Theorem 1], limits of simply connected diagrams can be computed purely by pullbacks. However his proof is quite involved and much more powerful than what we need for our purposes, so we record our own simplified version of this result. We have taken the following proof from [nLa21].

Proposition A.2.10. Let $C$ be a category with pushouts. If $d: I \rightarrow C$ is a diagram where $I$ is a finite, simply connected category, then the colimit of $d$ exists and is given by an iterated pushout.

Proof. Since $I$ is non-empty, let us fix an object $x_{0} \in I$. For any $y \in I$ we define $\ell(y)$ to be the number of morphisms of any minimal zig-zag between $x_{0}$ and $y$. Since $I$ is finite and simply connected, this is well-defined. Now choose a linear order of the objects of $I$ as $x_{0}, x_{1}, \ldots, x_{n}$ such that $\ell\left(x_{i}\right) \leq \ell\left(x_{i+1}\right)$ for $0 \leq i \leq n-1$.

Now let us inductively define objects $P_{i}$ in $C$ equipped with maps $p_{i j}: d\left(x_{j}\right) \rightarrow P_{i}$ for all $0 \leq j \leq i \leq n$ as follows.

For the base case, let $P_{0}=d\left(x_{0}\right)$ and let $p_{00}: d\left(x_{0}\right) \rightarrow d\left(x_{0}\right)$ be the identity map.
Now for the inductive step, suppose that we have objects $P_{i}$ for $0 \leq i \leq k$ and maps $p_{i j}$ : $d\left(x_{j}\right) \rightarrow P_{i}$ for all $0 \leq j \leq i \leq k$. Now choose a zig-zag of minimal length between $x_{0}$ and $x_{k+1}$. It will look like

$$
x_{0} \leftrightarrow y_{1} \leftrightarrow y_{2} \leftrightarrow \cdots \leftrightarrow y_{\ell\left(x_{k+1}\right)-1} \leftrightarrow x_{k+1} .
$$

But since we have ordered all of the objects of $I$, we know that each $y_{r}=x_{j}$ for some $j \leq k$ and so we have a morphism $p_{i j}: y_{r} \rightarrow P_{i}$ for every $j \leq i$ and $r \leq \ell\left(x_{k+1}\right)-1$. Let us write $y_{\ell}=y_{\ell\left(x_{k+1}\right)-1}=x_{j}$ for the final object. Suppose that the final map in the zig-zag is a map directed as $f: y_{\ell} \leftarrow x_{k+1}$. Then let $P_{k+1}=P_{k}$ and let $p_{(k+1)(k+1)}: d\left(x_{k+1}\right) \rightarrow P_{k+1}$ be the composite map

$$
d\left(x_{k+1}\right) \xrightarrow{d(f)} d\left(y_{\ell}\right) \xrightarrow{p_{k j}} P_{k+1}=P_{k}
$$

and set each other $p_{(k+1) r}: d\left(x_{r}\right) \rightarrow P_{k+1}$ equal to $p_{k r}$, which we assumed has already been defined for all $r \leq k$.

If the final map in the zig-zag is instead a map directed as $f: y_{\ell} \rightarrow x_{k+1}$, then let $P_{k+1}$ be the pushout
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-42.jpg?height=218&width=323&top_left_y=342&top_left_x=868)
and this defines the map $p_{(k+1)(k+1)}$. The other maps $p_{(k+1) i}$ are defined with composition of $d(f)$ with $p_{k i}$.

Thus we have defined an object $P_{n}$ in $C$ along with a cocone $p$ over $d$ given by the maps $p_{n i}: d\left(x_{i}\right) \rightarrow P_{n}$ for $0 \leq i \leq n$, and let $p_{k}=p_{k k}$. Let us show that $p$ is a colimit cocone over $d$. Suppose there was an object $Q$ and a cocone $q: d \Rightarrow \Delta_{Q}$ with components $q_{i}: d\left(x_{i}\right) \rightarrow Q$. Let us prove that it must factor uniquely through the $p$ by induction. In the base case, $q_{0}$ clearly factors uniquely through $p_{0}: P_{0} \rightarrow d\left(x_{0}\right)$ since it is the identity map. Now suppose that each $q$ factors uniquely through $p$ restricted to $x_{0}, \ldots, x_{k}$. Then in the inductive step, either $P_{k+1}$ is the same as $P_{k}$ and therefore $q_{k+1}$ factors uniquely through $p_{k+1}$ because $q_{k}$ factors uniquely through $p_{k}$ by assumption, or $P_{k+1}$ is a pushout, and therefore $q_{k+1}$ factors uniquely through $p_{k+1}$ by the universal property of the pullback. Therefore $p: d \Rightarrow \Delta_{P_{n}}$ is a colimit cocone. $\square$

Example A.2.11. Computing the colimit of a diagram $d: \int T \rightarrow \mathbf{G r}$ where $T$ is a tree with three vertices $x, y, z$ and edges $e=x y, f=y z$
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-42.jpg?height=328&width=985&top_left_y=1265&top_left_x=539)

Corollary A.2.12. If $d: \int T \rightarrow \mathbf{G r}$ is a tree-shaped structured decomposition, then the colimit of $d$ exists. Furthermore, the colimit cocone maps are monomorphisms.

Proof. This follows from Lemma A.2.2 and Proposition A.2.10. $\square$

Corollary A.2.13. Let $d: \int T \rightarrow \mathbf{G r}$ be a tree-shaped structured decomposition of a graph $H$, and suppose there is a map $f: G \rightarrow H$ of graphs. Let $f^{*}(d): \int T \rightarrow \mathbf{G r}$ denote the diagram obtained by pulling back the colimit cocone maps along $f$. Then $f^{*}(d)$ is a structured decomposition of $G$.

Proof. This follows from Lemma A.2.5 and Proposition A.2.10. $\square$

In the language of Remark 2.5.12, Corollary A.2.13 proves that $\mathbf{G r}$ has universal Treescolimits.

## A. 3 Multigraphs

This section is used primarily in Section 3.6. We first collect a few facts about $\mathbf{G r}_{\text {mlt }}$, the category of multigraphs, and then show that $\mathbf{G r}_{\text {mlt }}$ has pullback-stable or universal finite colimits.

Lemma A.3.1 ([Ple11, Theorem 3.6.1, 3.6.2]). Given a morphism $f: G \rightarrow H$ in $\mathbf{G r}_{\mathrm{mlt}}$, the following are equivalent:

- $f$ is a mono/epimorphism,
- $f$ is a regular mono/epimorphism,
- $f$ is an effective mono/epimorphism,
- $f$ is an extremal mono/epimorphism.

Since $\mathbf{G r}_{\text {mlt }}$ is finitely complete, thanks to Lemma A.3.1, we need only to show that epimorphisms of multigraphs are stable under pullback in order to show that $\mathbf{G r}_{\text {mlt }}$ is regular.

Lemma A.3.2. Epimorphisms in $\mathbf{G r}_{\text {mlt }}$ are stable under pullback.
Proof. Given maps $f: K \rightarrow H$ and $g: G \rightarrow H$, the pullback $K \times_{H} G$ is the multigraph with $V\left(K \times_{H} G\right)=V(K) \times_{V(H)} V(G)$ and where there is an edge $e$ between ( $k, g$ ) and ( $k^{\prime}, g^{\prime}$ ) for every pair of edges $e^{\prime}$ between $k$ and $k^{\prime}$ and $e^{\prime \prime}$ between $g$ and $g^{\prime}$ such that $f\left(e^{\prime}\right)=g\left(e^{\prime \prime}\right)$. Therefore, if $g$ is an epimorphism of multigraphs, then by Lemma A.1.9, $E(g)$ and $V(g)$ are surjective. So if we let $f^{*}(g): K \times_{H} G \rightarrow K$ denote the induced map from the pullback, then $E\left(f^{*}(g)\right)$ and $V\left(f^{*}(g)\right)$ will be surjective as well, so again by Lemma A.1.9, $f^{*}(g)$ is an epimorphism of multigraphs. $\square$

Corollary A.3.3. The category $\mathbf{G r}_{\mathrm{mlt}}$ is regular.
We recall (Definition A.1.7) that a multigraph $G$ consists of finite sets $V(G), E(G)$ and a function

$$
\partial: E(G) \rightarrow V(G)^{(2)} .
$$

We note that $(-)^{(2)}$ itself forms a functor $(-)^{(2)}$ : FinSet → FinSet, and so we can write $\mathbf{G r}_{\text {mlt }}$ as the comma category ( $1_{\text {FinSet }},(-)^{(2)}$ ). It is useful to know the following result on computing (co)limits in comma categories.

Lemma A.3.4 ([RB88, Theorem 5.2.3]). Let $F: C \rightarrow \mathcal{E}$ and $G: \mathscr{D} \rightarrow \mathcal{E}$ be functors, and let $(F \downarrow G)$ denote the corresponding comma category, with projection functors $\pi:(F \downarrow G) \rightarrow C$, $\pi^{\prime}:(F \downarrow G) \rightarrow D$. If $d: I \rightarrow(F \downarrow G)$ is a diagram such that the colimits $U=\operatorname{colim} \pi d$ and $V=\operatorname{colim} \pi^{\prime} d$ exist in $C$ and $D$ respectively, and $F$ preserves this colimit, then the colimit of $d$ exists in $(F \downarrow G)$ and is given by the unique map

$$
\operatorname{colim} F \pi d \cong F(U) \rightarrow G(V)
$$

in $\mathcal{E}$ that commutes with the colimit cocone maps. Conversely if $G$ preserves the limit of $\pi^{\prime} d$ then the limit of $d$ exists in ( $F \downarrow G$ ) and is given by the corresponding unique map

$$
F(U) \rightarrow G(V) \cong \lim G \pi^{\prime} d .
$$

Thanks to Lemma A.3.4, we know how to compute colimits in $\mathbf{G r}_{\text {mlt }}$.
Lemma A.3.5. Let $d: I \rightarrow \mathbf{G r}_{\mathrm{mlt}}$ be a finite diagram. Then the colimit colim $d$ exists and is given by the multigraph

$$
\partial: \operatorname{colim} E(d(i)) \rightarrow(\operatorname{colim} V(d(i)))^{(2)},
$$

where $\partial$ is the unique induced map from the colimit cocone maps.
The category $\mathbf{G r}_{\text {mlt }}$ has both an initial object $\varnothing$ given by the empty graph, and a terminal object * given by the multigraph with one vertex and one loop. Given multigraphs $G$ and $H$, their product $G \times H$ is the multigraph with $V(G \times H)=V(G) \times V(H), E(G \times H)=E(G) \times E(H)$, and if $e \in E(G)$ with $\partial_{G}(e)=\left\{x, x^{\prime}\right\}$ and $e^{\prime} \in E(H)$ with $\partial_{H}\left(e^{\prime}\right)=\left\{y, y^{\prime}\right\}$, then $\partial_{G \times H}\left(e, e^{\prime}\right)=\left\{(x, y),\left(x^{\prime}, y^{\prime}\right)\right\}$. Pullbacks are similarly easy to describe. If $f: G \rightarrow H$ and $g: K \rightarrow H$ are maps of multigraphs, then $G \times_{H} K$ is the multigraph with $V\left(G \times_{H} K\right)=V(G) \times_{V(H)} V(K), E\left(G \times_{H} K\right)=E(G) \times_{E(H)} E(K)$ and where if $e \in E(G)$ with $\partial_{G}(e)=\left\{x, x^{\prime}\right\}$ and $e^{\prime} \in E(K)$ with $\partial_{K}\left(e^{\prime}\right)=\left\{y, y^{\prime}\right\}$, then $\partial_{G \times_{H} K}\left(e, e^{\prime}\right)= \left\{(x, y),\left(x^{\prime}, y^{\prime}\right)\right\}$. If $f: G \rightarrow H$ is a map of multigraphs, and $H^{\prime} \hookrightarrow H$ is a monomorphism, i.e. a subgraph inclusion, then the pullback $f^{-1}\left(H^{\prime}\right)$ is given by the multigraph with vertex set $V(f)^{-1}\left(V\left(H^{\prime}\right)\right)$ and edge set $E(f)^{-1}\left(E\left(H^{\prime}\right)\right)$.

Lemma A.3.6. Coproducts in $\mathbf{G r}_{\mathrm{mlt}}$ are stable under pullbacks.
Proof. If $f: G \rightarrow H$ is a map of multigraphs, where $H \cong H_{0}+H_{1}$, then we have $G \cong f^{-1}\left(H_{0}\right)+ f^{-1}\left(H_{1}\right)$.

Lemma A.3.7. Coequalizers in $\mathbf{G r}_{\mathrm{mlt}}$ are stable under pullbacks.
Proof. This follows from coequalizers being stable under pullback in Set. Indeed, suppose that $f, g: G \rightarrow H$ are maps of multigraphs, with colimit $X=\operatorname{coeq}(f, g)$. If $h: Y \rightarrow X$ is a map of multigraphs, then we obtain a pair of pullback diagrams
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-44.jpg?height=305&width=337&top_left_y=717&top_left_x=863)

So we have $V\left(q_{Y}\right): V\left(Y \times_{X} H\right) \rightarrow V(Y)$ is the coequalizer of $V\left(h^{*}(f)\right)$ and $V\left(h^{*}(g)\right)$, and the same holds for the edges. Its then easy to see this causes $Y$ to be coequalizer of $h^{*}(f)$ and $h^{*}(g)$.

Corollary A.3.8. Finite colimits in $\mathbf{G r}_{\mathrm{mlt}}$ are stable under pullbacks.

## A. 4 Hypergraphs

This section is used primarily in Section 3.5. We prove several facts about the category Hyp of hypergraphs (Definition 3.5.1).

The vertex functor $V=V_{\mathbf{H y p}}: \mathbf{H y p} \rightarrow$ FinSet has both a left adjoint Disc : FinSet $\rightarrow \mathbf{H y p}$ given by the discrete hypergraph on a set, and right adjoint CoDisc : FinSet → Hyp given by taking every nonempty subset of a set $S$ to be a hyperedge edge. Furthermore $V$ is a faithful functor, making Hyp into a concrete category. Hence if $V(f)$ is inj/surjective, then $f: H \rightarrow H^{\prime}$ is a mono/epimorphism. Since $V$ has a left and right adjoint, a map $f: H \rightarrow H^{\prime}$ in Hyp is a mono/epimorphism if and only if $V(f)$ is inj/surjective.

Given a hypergraph $H$, a subhypergraph $H^{\prime} \subseteq H$ consists of subsets $V\left(H^{\prime}\right) \subseteq V(H)$ and $E\left(H^{\prime}\right) \subseteq E(H)$ such that if $e \in E\left(H^{\prime}\right)$ and $v \in e$, then $v \in V\left(H^{\prime}\right)$. Subhypergraphs of a hypergraph $H$ are in bijection with subobjects of $H$ in Hyp. Given a subset of vertices $S \subseteq V(H)$ of a hypergraph $H$, the induced subhypergraph $H[S]$ is the subhypergraph of $H$ containing all of the vertices of $S$ and all the hyperedges $e$ in $H$ such that $e \subseteq S$.

The intersection $H \cap K$ of subhypergraphs of $H \subseteq H^{\prime}$ and $K \subseteq H^{\prime}$ of a hypergraph $H^{\prime}$ is the subhypergraph $H \cap K \subseteq H^{\prime}$ with $V(H \cap K)=V(H) \cap V(K)$, and $E(H \cap K)=E(H) \cap E(K)$. There are monomorphisms $i_{H}: H \cap K \hookrightarrow H$ and $i_{K}: H \cap K \hookrightarrow K$.

The empty hypergraph $\varnothing$ is clearly an initial object in $\mathbf{H y p}$, but there is no terminal object.
Definition A.4.1. Suppose that we have a span of monomorphisms $i: G \rightarrow H$ and $j: G \rightarrow K$ of hypergraphs. Let $H+{ }_{G} K$ denote the hypergraph defined as follows. Let $V\left(H+{ }_{G} K\right)=V(H)+{ }_{V(G)} V(K)$, and if $e=\left\{x_{1}, \ldots, x_{n}\right\}$ is a nonempty subset of $V\left(H+_{G} K\right)$, then it is a hyperedge of $H+_{G} K$ if and only if there exists a hyperedge $e^{\prime}=\left\{v_{1}, \ldots, v_{n}\right\}$ in $H$ or $K$ such that $x_{i}=\left[v_{i}\right]$ for all $1 \leq i \leq n$. By the same reasoning as in Definition A.2.1, since $i$ and $j$ are monomorphisms, a vertex $x \in H+_{G} K$ belongs either to $H$ or $K$ or if it belongs to both of them, then there is a unique vertex $x^{\prime} \in G$ such that $i\left(x^{\prime}\right)=j\left(x^{\prime}\right)=x$. It is not hard to see that $H+{ }_{G} K$ is a well-defined hypergraph.

Let $r: H \rightarrow H+_{G} K$ and $s: K \rightarrow H+{ }_{G} K$ be defined simply as the quotient map on vertices. They are easily seen to be hypergraph homomorphisms.

The proofs of the following four results are practically identical to the proofs of Lemma A.2.2, Lemma A.2.5, Corollary A.2.12 and Corollary A.2.13.

Lemma A.4.2. Given a span of monomorphisms in Hyp
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-45.jpg?height=195&width=362&top_left_y=557&top_left_x=849)
their pushout exists, is given by $P$, and furthermore the maps $r$ and $s$ are monomorphisms.
Lemma A.4.3. Suppose that we have a diagram in Hyp of the form
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-45.jpg?height=465&width=568&top_left_y=954&top_left_x=744)
where $h_{0}, h_{2}$ are monomorphisms and the four vertical faces are all pullbacks. If $H$ is a pushout, then so is $G$.

Corollary A.4.4. If $d: \int T \rightarrow \mathbf{H y p}$ is a tree-shaped structured decomposition, then the colimit of $d$ exists. Furthermore, the colimit cocone maps are monomorphisms.

Corollary A.4.5. Let $d: \int T \rightarrow \mathbf{H y p}$ be a tree-shaped structured decomposition of a hypergraph $H^{\prime}$, and suppose there is a map $f: H \rightarrow H^{\prime}$ of hypergraphs. Let $f^{*}(d): \int T \rightarrow$ Hyp denote the diagram obtained by pulling back the colimit cocone maps along $f$. Then $f^{*}(d)$ is a structured decomposition of $H$.

By construction the inclusion $\iota$ : Gr $\hookrightarrow$ Hyp preserves finite limits, coproducts and pushouts of spans of monomorphisms.

Lemma A.4.6. The Gaifman graph functor Gaif : $\mathbf{H y p} \rightarrow \mathbf{G r}$ preserves pushouts of spans of monomorphisms.

Proof. Suppose we have a pushout of a span of monomorphisms in Hyp
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-45.jpg?height=200&width=206&top_left_y=2261&top_left_x=932)
and suppose that $p: \operatorname{Gaif}(H) \rightarrow Q$ and $q: \operatorname{Gaif}(K) \rightarrow Q$ are graph morphisms such that $p \operatorname{Gaif}(i)=q \operatorname{Gaif}(j)$. We want to obtain a unique graph morphism $h$ such that $h \operatorname{Gaif}(r)=p$
and $h \operatorname{Gaif}(s)=q$.
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-46.jpg?height=340&width=586&top_left_y=296&top_left_x=735)

Applying $V_{\mathbf{H y p}}$ to the above commutative diagram, we obtain a pushout diagram in Set, since $V_{\mathbf{H y p}} \circ$ Gaif $=V_{\mathbf{G r}}$. So we get a unique map $V(h): V(\operatorname{Gaif}(P))=V(P) \rightarrow V(Q)$. We need only to show that it is a graph map. Suppose that $x y \in E(\operatorname{Gaif}(P))$. Then there exists an $n$-edge $e \in E(P)$ such that $x, y \in e$. Thus there is either an $n$-edge $e^{\prime} \in E(H)$ or $e^{\prime \prime} \in E(K)$ such that $e=\left[e^{\prime}\right]$ or $e=\left[e^{\prime \prime}\right]$. Thus there is either a $v w \in E(\operatorname{Gaif}(H))$ or $a b \in E(\operatorname{Gaif}(K))$ such that $v, w \in e^{\prime}$ or $a, b \in e^{\prime \prime}$ and $x=[v], y=[w]$ or $x=[a], y=[b]$. Hence $h(x y)=p(v) p(w)$ or $q(a) q(b)$, which in both cases are edges. Hence $h$ is a graph map.

## A.4.1 RS and sd-Tree Decompositions

Our goal for this section is to prove Proposition A.4.11, which says that if $\Gamma=$ (Hyp, Trees, $\left\{K_{\mathbf{H y p}}^{n}\right\}_{n \geq 0}$ ) is the width category from Proposition 3.5.7 and $H \in \mathbf{H y p}$, then $\mathbf{t w}(H)= \mathbf{w}_{\Gamma}(H)$. To do this, we need to get a better handle on the connection between structured decompositions and tree decompositions.

Recall Definition 3.5.5 for the notion of a (Robertson-Seymour) or RS-tree decomposition $(X, T)$ of a hypergraph $H$. We want to compare this kind of decomposition with the notion of a structured decomposition $d: \int T \rightarrow \mathbf{H y p}$ of $H$ where $T$ is a tree. Let us call the first notion an RS-tree decomposition and the latter an sd-tree decomposition of $H$.

We shall define functions
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-46.jpg?height=191&width=1237&top_left_y=1571&top_left_x=415)
as follows.
First let us define $\Phi$. Suppose that ( $X, T$ ) is an RS-tree decomposition of a hypergraph $H$. Then consider the diagram $\Phi(X, T)=d_{(X, T)}: \int T \rightarrow$ Hyp given by mapping each vertex $t \in T$ to the induced subhypergraph $H[X(t)]$, and to each edge $t t^{\prime}$ of $T$ the adhesion $H\left[X(t) \cap X\left(t^{\prime}\right)\right]$, and the corresponding maps being the inclusions.

Lemma A.4.7. If ( $X, T$ ) is an RS-tree decomposition of a hypergraph $H$, then $\Phi(X, T)=d_{(X, T)}$ is an sd-tree decomposition of $H$.

Proof. The inclusions $\iota_{t}: H[X(t)] \hookrightarrow H$ define a cocone $\iota: d_{(X, T)} \Rightarrow \Delta(H)$. Let us show that this is a colimit cocone. If $\sigma: d_{(X, T)} \Rightarrow \Delta\left(H^{\prime}\right)$ is another cocone, we want to construct a unique map $h: H \rightarrow H^{\prime}$ such that $\Delta(h) \iota=\sigma$. On vertices, let us define $V(h): V(H) \rightarrow V\left(H^{\prime}\right)$ by setting $V(h)(x)=\sigma_{t}(x)$, for $x \in H$. Let us show that this is well-defined. First, since $(X, T)$ is an RS-tree decomposition, every vertex $x \in H$ belongs to some $H[X(t)]$, by condition (1). If $x$ belongs to $H[X(t)]$ and $H\left[X\left(t^{\prime}\right)\right]$, then by condition (3), it belongs to every bag $X\left(t_{0}\right)$ with $t_{0}$ lying on the unique path between $t$ and $t^{\prime}$. Since $\sigma$ is a cocone, this means that for every such $t_{0}, \sigma_{t}(x)= \sigma_{t_{0}}(x)=\sigma_{t^{\prime}}(x)$. Thus $V(h)$ is well defined.

Now if $e \in E_{n}(H)$, then there exists some bag $X(t)$ such that $e \in E_{n}(H[X(t)])$ by condition (2). Thus $h(e) \in E_{n}\left(H^{\prime}\right)$, since each $\sigma_{t}$ is a hypergraph homomorphism. Thus $h: H \rightarrow H^{\prime}$ is
a well-defined hypergraph homomorphism. Thus we need now only show that it the unique such map such that $\Delta(h) \iota=\sigma$.

If $h^{\prime}: H \rightarrow H^{\prime}$ is a hypergraph homomorphism such that $\Delta\left(h^{\prime}\right) \iota=\sigma$, then for every $x \in H$, by condition (1), there exists a $t \in T$ such that $x$ is in the image of $\iota_{t}: H[X(t)] \rightarrow H$. Thus $h^{\prime}(x)=\sigma_{t}(x)$, and therefore $h$ is unique, so $\iota$ is a colimit cocone. $\square$

Remark A.4.8. When $H$ is a graph, then an sd-tree decomposition $d: \int T \rightarrow \mathbf{H y p}$ of $H$ factors uniquely through Gr
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-47.jpg?height=188&width=435&top_left_y=607&top_left_x=815)
simply because if $H^{\prime}$ is a hypergraph that is not a graph, i.e. it contains an edge of cardinality not equal to 2 , then there exists no hypergraph homomorphism $H^{\prime} \rightarrow H$. So the map $\Phi$, when restricted to $H$ a graph, lands in the set of sd-tree decompositions of $H$ in Gr.

Now let us define the map $\Psi$. Suppose that $d: \int T \rightarrow \mathbf{H y p}$ is an sd-tree decomposition of a hypergraph $H$. Let $\Psi(d)=\left(X_{d}, T\right)$ be defined as follows. Define $X_{d}: V(T) \rightarrow P(V(H))$ as $X_{d}(t)=V(d(t))$ for each $t \in T$.

Lemma A.4.9. If $d: \int T \rightarrow \mathbf{H y p}$ is an sd-tree decomposition of a hypergraph $H$, then $\Psi(d)=$ ( $X_{d}, T$ ) is an RS-tree decomposition of $H$.
Proof. By Lemma A.4.2 and Lemma A.2.10, the colimit cocone maps $\lambda_{t}: d(t) \rightarrow H$ are all monomorphisms. Hence we can think of the bags and adhesions of $d$ as subhypergraphs of $H$. It is clear that conditions (1) and (2) of Definition 2.8.1 hold for $\Phi(d)=\left(X_{d}, T\right)$, as every vertex and hyperedge of $H$ must belong to some bag in order for them to exist in the colimit. Now we need only to show that condition ( 3 ) holds.

Let $x, y, z \in T$, we want to show that if the unique path between $x$ and $z$ contains $y$ then $X_{d}(x) \cap X_{d}(z) \subseteq X_{d}(y)$. Let $T_{0}$ denote the subgraph of $T$ consisting of the unique path from $x$ to $z$, and let $d_{0}$ denote the restriction of $d$ to $T_{0}$. The colimit of $d_{0}$ will still be given by an iterated pushout, with $x$ and $z$ the endpoints of a zig-zag diagram in $\mathbf{H y p}$ by Proposition A.2.10.

Suppose that $v \in d(x) \cap d(z)$. If $v$ belongs to both $d(x)$ and $d(z)$, we want to show that it belongs to each intermediate bag of the zig-zag $d_{0}$. Let us prove this by induction on the length of the path $T_{0}$. For the base case, suppose that $T_{0}$ consists of the three vertices $x, y, z$ and two edges $e=x y$ and $f=y z$. Then the diagram in Example A.2.11 is precisely the colimit of $d_{0}$, interpreted in Hyp. We see that if $v \in d(x)$, then $v \in P_{2}$. But in order for $v$ to belong to both $P_{2}$ and $d(z)$, by the set-theoretic construction of the pushout (Definition A.4.1), it must be the case that $v \in d(f)$. But $d(f) \subseteq d(y)$, hence $v \in d(y)$.

For the inductive step, suppose now that $T_{0}$ is a path of length $n$ between $x$ and $z$ passing through $y$, and suppose further that for every path of length less than $n$ the intersection of the bags of the endpoints must belong to every intermediate bag. Then let $d(w)$ denote the bag immediately to the left of $d(z)$, and let $g=w z$ denote the rightmost edge in $T_{0}$. Let $T_{1}$ denote the unique path between $x$ and $w$, and let $d_{1}$ denote the restriction of $d$ to $T_{1}$. Suppose that $P$ is constructed as an iterated pushout of the zig-zag $d_{1}$ as in Example A.2.11. By assumption we know that $d(x) \cap d(w) \subseteq d(y)$, and we have the pushout
![](https://cdn.mathpix.com/cropped/a45b5065-f34d-47cf-ab4d-9b35ec45b866-47.jpg?height=181&width=633&top_left_y=2348&top_left_x=715)

But if $v \in d(x) \cap d(z)$, then $v \in P$. But then as in the base step, we know that since $v \in P \cap d(z)$, then $v \in d(g)$. But $d(g) \subseteq d(w)$, so $v \in d(w)$. Thus $v \in d(x) \cap d(w)$, and so $v \in d(y)$. Therefore $\Phi(d)=\left(X_{d}, T\right)$ satisfies condition (3), and is therefore an RS-tree decomposition of $H$. $\square$

Remark A.4.10. If $H$ is a graph and $d: \int T \rightarrow \mathbf{H y p}$ an sd-tree decomposition, then as in Remark A.4.8, $d$ must factor uniquely through $\mathbf{G r}$. Hence the map $\Psi$ restricted to sd-tree deceompositions in $\mathbf{G r}$ lands in the set of RS-tree decompositions of $H$ as in Definition 2.8.1.

Thus we have constructed the functions of (4). It is clear that if ( $X, T$ ) is an RS-tree decomposition, then $(\Psi \circ \Phi)(X, T)=(X, T)$. Thus $\Psi$ is surjective.

We also note that since $\Phi$ and $\Psi$ do not change the bags of the decompositions, if ( $X, T$ ) is an RS-tree decomposition of a hypergraph $H$, then $w(X, T)=w(\Phi(X, T))$, where the former width is from Definition 3.5.5 and the latter is from Definition 2.5.7. Conversely if $d$ is an sd-tree decomposition of $H$, then $w(d)=w(\Psi(d))$.

Proposition A.4.11. If $\Gamma=\left(\mathbf{H y p}\right.$, Trees, $\left.\left\{K_{\mathbf{H y p}}^{n}\right\}_{n \geq 0}\right)$ is the sd-category from Proposition 3.5.7, and $H$ is a hypergraph, then

$$
\mathbf{w}_{\Gamma}(H)=\mathbf{t w}_{\mathbf{H y p}}(H) .
$$

Proof. Suppose that $d: \int T \rightarrow \mathbf{H y p}$ is a minimal sd-tree decomposition of $H$. Then $\Psi(d)$ is a minimal RS-tree decomposition of $H$. Indeed, if ( $X, T$ ) were any other RS-tree decomposition, then

$$
w(\Psi(d))=w(d) \leq w(\Phi(X, T))=w(X, T) .
$$

But $w(d)=w(\Psi(d))$, and since both decompositions are minimal $\mathbf{w}_{\Gamma}(H)=\mathbf{t w}_{\mathbf{H y p}}(H)$.
Corollary A.4.12. If $\Gamma=\left(\mathbf{G r}\right.$, Trees, $\left.\left\{K^{n}\right\}_{n \geq 0}\right)$ is the sd-category from Proposition 3.1.1, and $G$ is a graph, then

$$
\mathbf{w}_{\Gamma}(G)=\mathbf{t w}(G) .
$$

Proof. This follows from Remarks A.4.8 and A.4.10 along with Proposition A.4.11.

## References

[AGG07] Isolde Adler, Georg Gottlob, and Martin Grohe. "Hypertree width and related hypergraph invariants". In: European Journal of Combinatorics 28.8 (2007), pp. 21672181. DOI: https://doi.org/10.1016/j.ejc.2007.04.013 (p. 25).
[Ame06] Aaron David Ames. "A categorical theory of hybrid systems". PhD thesis. University of California, Berkeley, 2006. url: https://www2.eecs.berkeley.edu/Pubs/ TechRpts/2006/EECS-2006-165.pdf (pp. 4, 33).
[AZ21] Ernst Althaus and Sarah Ziegler. "Optimal tree decompositions revisited: a simpler linear-time FPT algorithm". In: Graphs and Combinatorial Optimization: from Theory to Applications: CTW2020 Proceedings (2021), pp. 67-78 (p. 14).
[Bae+23] J. C. Baez et al. "Compositional Modeling with Stock and Flow Diagrams". In: Proceedings Fifth International Conference on Applied Category Theory, Glasgow, United Kingdom, 18-22 July 2022. Ed. by J. E. Master and M. Lewis. Vol. 380. Electronic Proceedings in Theoretical Computer Science. Open Publishing Association, 2023, pp. 77-96. dor: 10.4204/EPTCS.380.5 (p. 2).
[Bas93] H. Bass. "Covering theory for graphs of groups". In: Journal of Pure and Applied Algebra 89.1 (1993), pp. 3-47. issn: 0022-4049. dor: https://doi.org/10.1016/0022-4049(93)90085-8 (p. 3).
[BB72] U. Bertelè and F. Brioschi. Nonserial dynamic programming. Academic Press, Inc., 1972. DOI: https://doi.org/10.1016/s0076-5392(08)x6010-2 (pp. 3, 17).
[Ber+04] Anne Berry et al. "Maximum cardinality search for computing minimal triangulations of graphs". In: Algorithmica 39 (2004), pp. 287-298. dor: 10.1007/s00453-004-1084-3 (p. 14).
[BFT24] Benjamin Merlin Bumpus, James Fairbanks, and Will J. Turner. Pushing Tree Decompositions Forward Along Graph Homomorphisms. 2024. arXiv: 2408.15184 [math.C0] (p. 35).
[BH11] John Baez and Alexander Hoffnung. "Convenient categories of smooth spaces". In: Transactions of the American Mathematical Society 363.11 (2011), pp. 5789-5825 (p. 36).
[BK23] B. M. Bumpus and Z. A. Kocsis. "Spined categories: Generalizing tree-width beyond graphs". In: European Journal of Combinatorics 114 (2023). dor: https://doi. org/10.1016/j.ejc.2023.103794 (pp. 2, 4, 8-9, 22, 37).
[BK96] Hans L. Bodlaender and Ton Kloks. "Efficient and Constructive Algorithms for the Pathwidth and Treewidth of Graphs". In: Journal of Algorithms 21.2 (1996), pp. 358-402. ISSN: 0196-6774. DOI: https://doi.org/10.1006/jagm.1996.0049. URL: https://www.sciencedirect.com/science/article/pii/S0196677496900498 (p. 14).
[BL+86] Richard T Bumby, Dana May Latch, et al. "Categorical constructions in graph theory". In: International Journal of Mathematics and Mathematical Sciences 9.1 (1986), pp. 1-16 (p. 35).
[Blu+11] Christoph Blume et al. "Treewidth, pathwidth and cospan decompositions". In: Electronic Communications of the EASST 41 (2011) (p. 4).
[BM20] J. C. Baez and J. Master. "Open Petri nets". In: Mathematical Structures in Computer Science 30.3 (2020), pp. 314-341. url: https://doi.org/10.1017/S0960129520000043 (p. 2).
[Bos+22] Prosenjit Bose et al. "Separating layered treewidth and row treewidth". In: Discrete Mathematics and Theoretical Computer Science 24 (2022). issn: 1365-8050. dor: https: //doi.org/10.46298/dmtcs. 7458 (pp. 28-29).
[BP17] J. C. Baez and B. S. Pollard. "A compositional framework for reaction networks". In: Reviews in Mathematical Physics 29.09 (2017), p. 1750028. url: https://doi.org/ 10.1142/S0129055X17500283 (p. 2).
[Bre+23] Nick Brettell et al. Comparing Width Parameters on Graph Classes. 2023. arXiv: 2308. 05817 [math.C0] (p. 34).
[Bro+08] Ronald Brown et al. "Graphs of morphisms of graphs". In: the electronic journal of combinatorics 15 (2008) (p. 35).
[BT01] Vincent Bouchitté and Ioan Todinca. "Treewidth and Minimum Fill-in: Grouping the Minimal Separators". In: SIAM Journal on Computing 31.1 (2001), pp. 212232. dor: 10. 1137 / S0097539799359683. eprint: https : / / doi . org / 10 . 1137 / S0097539799359683. url: https://doi.org/10.1137/S0097539799359683 (p. 14).
[Bum21] B. M. Bumpus. "Generalizing graph decompositions". PhD thesis. University of Glasgow, 2021. urt: https://theses.gla.ac.uk/82496/ (pp. 2, 4).
[Cam21] Tim Campion. Is Graph cartesian-closed? 2021. url: https://mathoverflow.net/q / 321902 (p. 35).
[Car+14] J. Carmesin et al. "k-Blocks: A Connectivity Invariant for Graphs". In: SIAM Journal on Discrete Mathematics 28.4 (2014), pp. 1876-1891. url: https://doi.org/10. 1137/130923646 (p. 34).
[Car22a] J. Carmesin. "Local 2-separators". In: Journal of Combinatorial Theory, Series B 156 (2022), pp. 101-144. ISSN: 0095-8956. dor: https://doi.org/10.1016/j.jctb.2022.04.005. url: https://www.sciencedirect.com/science/article/pii/S0095895622000430 (p. 4).
[Car22b] J. Carmesin. "Local 2-separators". In: Journal of Combinatorial Theory, Series B 156 (2022), pp. 101-144. dor: https://doi.org/10.1016/j.jctb.2022.04.005 (p. 27).
[CE12] B. Courcelle and J. Engelfriet. Graph structure and monadic second-order logic: a language-theoretic approach. Vol. 138. Cambridge University Press, 2012. dor: https: //doi.org/10.1017/CBO9780511977619 (pp. 14, 17).
[CER93] B. Courcelle, J. Engelfriet, and G. Rozenberg. "Handle-rewriting hypergraph grammars". In: Journal of computer and system sciences 46.2 (1993), pp. 218-270. DOI: https://doi.org/10.1016/0022-0000(93)90004-G (p. 4).
[Cic19] D. Cicala. Rewriting structured cospans: A syntax for open systems. University of California, Riverside, 2019. url: https://www.proquest.com/docview/2308216336?pqorigsite=gscholar\&fromopenview=true (p. 2).
[CM69] E. Cuthill and J. McKee. "Reducing the bandwidth of sparse symmetric matrices". In: Proceedings of the 1969 24th National Conference. ACM '69. New York, NY, USA: Association for Computing Machinery, 1969, pp. 157-172. isbn: 9781450374934. dor: 10.1145/800195.805928. url: https://doi.org/10.1145/800195.805928 (p. 14).
[Cou20] K. A. Courser. Open systems: A double categorical perspective. University of California, Riverside, 2020. url: https://www.proquest.com/docview/2404393265?pqorigsite=gscholar\&fromopenview=true (p. 2).
[Cou90] B. Courcelle. "The monadic second-order logic of graphs I. Recognizable sets of finite graphs". In: Information and computation 85.1 (1990), pp. 12-75. dor: https: //doi.org/10.1016/0890-5401(90)90043-H (p. 3).
[Cou96] B. Courcelle. "The monadic second-order logic of graphs X: Linear orderings". In: Theoretical Computer Science 160.1 (1996), pp. 87-143. dor: https://doi.org/10.1016/ 0304-3975(95)00083-6 (p. 4).
[Cyg+15] M. Cygan et al. Parameterized algorithms. ISBN:978-3-319-21275-3. Springer, 2015. DOI: https://doi.org/10.1007/978-3-319-21275-3 (p. 14).
[DHL19] R. Diestel, F. Hundertmark, and S. Lemanczyk. "Profiles of separations: in graphs, matroids, and beyond". In: Combinatorica 39.1 (2019), pp. 37-75. url: https://doi. org/10.1007/s00493-017-3595-y (p. 34).
[Die+22] R. Diestel et al. Canonical graph decompositions via coverings. 2022. url: https://doi. org/10.48550/arXiv.2207.04855 (p.4).
[Die10] R. Diestel. Graph Theory. Springer, 2010. dor: https://doi.org/10.1007/978-3-662-53622-3 (pp. 18, 21, 27, 37).
[Dir61] Gabriel Andrew Dirac. "On rigid circuit graphs". In: Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg 25.1 (1961), pp. 71-76. dor: https:// doi.org/10.1007/BF02992776 (p. 18).
[DMŠ24] Clément Dallard, Martin Milanič, and Kenny Štorgel. "Treewidth versus clique number. II. Tree-independence number". In: Journal of Combinatorial Theory, Series B 164 (2024), pp. 404-442. DOI: https://doi.org/10.1016/j.jctb.2023.10.006 (pp.3, 23).
[DMW17] Vida Dujmović, Pat Morin, and David R Wood. "Layered separators in minorclosed graph classes with applications". In: Journal of Combinatorial Theory, Series B 127 (2017), pp. 111-147. DOI: https://doi.org/10.1016/j.jctb.2017.05.006 (pp. 3-4, 28).
[DOS21] G. L. Duarte, M. de Oliveira Oliveira, and U. S. Souza. "Co-Degeneracy and CoTreewidth: Using the Complement to Solve Dense Instances". In: 46th International Symposium on Mathematical Foundations of Computer Science, MFCS 2021, August 23-27, 2021, Tallinn, Estonia. Ed. by Filippo Bonchi and Simon J. Puglisi. Vol. 202. LIPIcs. Schloss Dagstuhl - Leibniz-Zentrum für Informatik, 2021. dor: https://doi. org/10.4230/LIPIcs.MFCS.2021.42 (pp. 3, 22).
[DS23a] E. Di Lavore and P. Sobociński. "Monoidal Width". en. In: Logical Methods in Computer Science 19, Issue 3 (Sept. 2023) (p. 4).
[DS23b] E. Di Lavore and P. Sobociński. "Monoidal Width: Capturing Rank Width". In: Proceedings Fifth International Conference on Applied Category Theory, Glasgow, United Kingdom, 18-22 July 2022. Ed. by J. E. Master and M. Lewis. Vol. 380. Electronic Proceedings in Theoretical Computer Science. Open Publishing Association, 2023, pp. 268-283. doi: 10.4204/EPTCS.380.16 (p. 4).
[DW80] Willibald Dörfler and D. A. Waller. "A category-theoretical approach to hypergraphs". In: Archiv der Mathematik 34 (1980), pp. 185-192. dor: https://doi.org/10. 1007/BF01224952 (p. 25).
[EH20] Christopher Eur and June Huh. "Logarithmic concavity for morphisms of matroids". In: Advances in Mathematics 367 (2020). Dor: https://doi.org/10.1016/j. aim. 2020.107094 (p. 36).
[Eib+21] Eduard Eiben et al. "Measuring what matters: A hybrid approach to dynamic programming with treewidth". In: Journal of Computer and System Sciences 121 (2021), pp. 57-75. dor: https://doi.org/10.1016/j.jcss.2021.04.005 (p. 29).
[EM45] S. Eilenberg and S. MacLane. "General theory of natural equivalences". In: Transactions of the American Mathematical Society 58 (1945), pp. 231-294 (p. 5).
[Fag83] Ronald Fagin. "Degrees of acyclicity for hypergraphs and relational database schemes". In: Journal of the ACM (JACM) 30.3 (1983), pp. 514-550. dor: https:// doi.org/10.1145/2402.322390 (p. 34).
[FG06] J. Flum and M. Grohe. "Parameterized Complexity Theory. 2006". In: Texts Theoret. Comput. Sci. EATCS Ser (2006). ISBN:978-3-540-29952-3. dor: https://doi.org/10. 1007/3-540-29953-X (p. 14).
[Fon16] B. Fong. "The algebra of open and interconnected systems". In: arXiv preprint arXiv:1609.05382 (2016). url: https://doi.org/10.48550/arXiv. 1609.05382 (p. 2).
[GLS99] Georg Gottlob, Nicola Leone, and Francesco Scarcello. "Hypertree decompositions and tractable queries". In: Proceedings of the eighteenth ACM SIGMOD-SIGACTSIGART symposium on Principles of database systems. 1999, pp. 21-32. doi: https: //doi.org/10.1145/303976.303979 (p. 34).
[Got+05] Georg Gottlob et al. "Hypertree decompositions: Structure, algorithms, and applications". In: International Workshop on Graph-Theoretic Concepts in Computer Science. Springer. 2005, pp. 1-15. dor: https://doi.org/10.1007/11604686_1 (p. 26).
[Gro17] M. Grohe. "Descriptive Complexity, Canonisation, and Definable Graph Structure Theory, Cambridge University Press, Cambridge, 2017, $\mathrm{x}+544$ pp". English. In: The Bulletin of Symbolic Logic 23.4 (2017). ISBN:1079-8986, pp. 493-494 (p. 14).
[Gui73] R. Guitart. "Sur le foncteur diagramme". In: Cahiers de topologie et géométrie différentielle catégoriques 14 (1973), pp. 181-182 (p. 5).
[Gui74] R. Guitart. "Remarques sur les machines et les structures". In: Cahiers de topologie et géométrie différentielle 15.2 (1974), pp. 113-144 (p. 5).
[GV77] R. Guitart and L. Van den Bril. "Décompositions et lax-complétions". In: Cahiers de topologie et géométrie différentielle 18.4 (1977), pp. 333-407 (p. 5).
[GZ67] Peter Gabriel and Michel Zisman. Calculus of Fractions and Homotopy Theory. Springer, 1967 (p. 41).
[Hal76] R. Halin. "S-functions for graphs". In: Journal of Geometry 8.1-2 (1976), pp. 171186. DOI: https://doi.org/10.1007/BF01917434 (pp. 3, 17).
[Hei13] Miriam Heinz. "Tree decomposition: graph minor theory and algorithmic implications". PhD thesis. Vienna University of Technology, 2013. url: https://dmg.tuwien. ac.at/drmota/DAHeinz.pdf (pp. 3, 25).
[Hig76] P. J. Higgins. "The Fundamental Groupoid of a Graph of Groups". In: Journal of the London Mathematical Society s2-13.1 (1976), pp. 145-149. dor: https://doi.org/10. 1112/jlms/s2-13.1.145. eprint: https://londmathsoc.onlinelibrary.wiley.com/doi/pdf/ 10.1112/jlms/s2-13.1.145. URL: https://londmathsoc.onlinelibrary.wiley.com/doi/abs/ 10.1112/jlms/s2-13.1.145 (p. 4).
[Hli+08] Petr Hliněnỳ et al. "Width parameters beyond tree-width and their applications". In: The computer journal 51.3 (2008), pp. 326-362. dor: https://doi.org/10.1093/ comjnl/bxm052 (p. 34).
[JKW21] B. M. P. Jansen, J. J. H. de Kroon, and M. Włodarczyk. "Vertex Deletion Parameterized by Elimination Distance and Even Less". In: Proceedings of the 53rd Annual ACM SIGACT Symposium on Theory of Computing. STOC 2021. Virtual, Italy: Association for Computing Machinery, 2021, pp. 1757-1769. isbn: 9781450380539. doi: 10.1145/3406325.3451068. url: https://doi.org/10.1145/3406325.3451068 (p. 4).
[JKW22] Bart M. P. Jansen, Jari J. H. de Kroon, and Michał Włodarczyk. Vertex Deletion Parameterized by Elimination Distance and Even Less. 2022. arXiv: 2103.09715 [cs .DS] (pp. 3, 29).
[JY21] Niles Johnson and Donald Yau. 2-dimensional categories. Oxford University Press, USA, 2021. DOI: https://doi.org/10.1093/oso/9780198871378.001.0001 (p. 8).
[KBJ19] Tuukka Korhonen, Jeremias Berg, and Matti Järvisalo. "Solving Graph Problems via Potential Maximal Cliques: An Experimental Evaluation of the BouchittéTodinca Algorithm". In: ACM J. Exp. Algorithmics 24 (Feb. 2019). issn: 1084-6654. DOI: 10.1145/3301297. URL: https://doi.org/10.1145/3301297 (p. 14).
[Koc67] A. Kock. "Limit monads in categories". PhD thesis. The University of Chicago, 1967 (p. 5).
[KV98] Phokion G Kolaitis and Moshe Y Vardi. "Conjunctive-query containment and constraint satisfaction". In: Proceedings of the seventeenth ACM SIGACT-SIGMODSIGART symposium on Principles of database systems. 1998, pp. 205-213. dor: https: //doi.org/10.1006/jcss.2000.1713 (p. 34).
[Lib+22] S. Libkind et al. "An algebraic framework for structured epidemic modelling". In: Philosophical Transactions of the Royal Society A, Mathematical, Physical and Engineering Sciences 380.2233 (Oct. 2022), p. 20210309 (p. 2).
[Lin83] P.A. Linnell. "On accessibility of groups". In: Journal of Pure and Applied Algebra 30.1 (1983), pp. 39-46. ISSN: 0022-4049. dor: https://doi.org/10.1016/0022-4049(83) 90037-3 (p. 32).
[LS04] Stephen Lack and Paweł Sobociński. "Adhesive categories". In: International Conference on Foundations of Software Science and Computation Structures. Springer. 2004, pp. 273-288. DOI: https://doi.org/10.1007/978-3-540-24727-2_20 (pp. 13, 40).
[Mas21] J. Master. Composing Behaviors of Networks. University of California, Riverside, 2021. URL: https://www.proquest.com/docview/2565195807?pq-origsite=gscholar\& fromopenview=true (p. 2).
[Nie06] Rolf Niedermeier. Invitation to fixed-parameter algorithms. Vol. 31. OUP Oxford, 2006 (p. 20).
[nLa21] nLab authors. Connected Limits. Revision 14. 2021. url: https://ncatlab.org/nlab/ show/connected+limit\#construction_from_pullbacks_and_equalizers (p. 41).
[nLa24] nLab authors. Graph. Revision 109. 2024. url: https://ncatlab.org/nlab/show/graph (pp. 5, 37).
[OS06] S.-i. Oum and P. D. Seymour. "Approximating clique-width and branch-width". In: Journal of Combinatorial Theory, Series B 96.4 (2006), pp. 514-528. dor: https: //doi.org/10.1016/j.jctb.2005.10.006 (p. 4).
[Par90] Robert Paré. "Simply connected limits". In: Canadian Journal of Mathematics 42.4 (1990), pp. 731-746. DOI: https://doi.org/10.4153/CJM-1990-038-6 (p. 41).
[Pat+23] E. Patterson et al. "A diagrammatic view of differential equations in physics". In: Mathematics in Engineering 5.2 (2023), pp. 1-59. issn: 2640-3501. dor: 10.3934/ mine.2023036. URL: https://www.aimspress.com/article/doi/10.3934/mine.2023036 (p. 5).
[Pat21] Evan Patterson. Categories of diagrams in data migration and computational physics. 2021. URL: https://www.algebraicjulia.org/assets/slides/topos-colloquium-2021.pdf (p. 7).
[Ple11] Demitri Joel Plessas. "The categories of graphs". PhD thesis. University of Montana, 2011. URL: https:// scholarworks.umt.edu/cgi/viewcontent.cgi? referer = \&httpsredir=1\&article=1986\&context=etd (pp. 35, 37, 42).
[Pol17] B. S. S. Pollard. Open Markov processes and reaction networks. University of California, Riverside, 2017. url: https://www.proquest.com/docview/1972046592?pqorigsite=gscholar\&fromopenview=true (p. 2).
[PR00] Ljubomir Perkovic and Bruce Reed. "An Improved Algorithm for Finding Tree Decompositions of Small Width". In: International Journal of Foundations of Computer Science 11.03 (2000), pp. 365-371. dor: 10.1142/S0129054100000247 (p. 14).
[PT20] G. Peschke and W. Tholen. "Diagrams, fibrations, and the decomposition of colimits". In: arXiv preprint arXiv:2006.10890 (2020) (p. 5).
[PT21] George Peschke and Walter Tholen. Diagrams, Fibrations, and the Decomposition of Colimits. 2021. arXiv: 2006.10890 [math.CT] (p. 7).
[PT22] P. Perrone and W. Tholen. "Kan extensions are partial colimits". In: Applied Categorical Structures 30.4 (2022), pp. 685-753. url: https://doi.org/10.1007/s10485-021-09671-9 (p. 5).
[RB88] David E Rydeheard and Rod M Burstall. Computational category theory. Vol. 152. Prentice Hall Englewood Cliffs, 1988 (p. 43).
[Rie17] Emily Riehl. Category theory in context. Courier Dover Publications, 2017 (p. 8).
[RS04] N. Robertson and P.D. Seymour. "Graph Minors. XX. Wagner's conjecture". In: Journal of Combinatorial Theory, Series B 92.2 (2004), pp. 325-357. dor: https://doi. org/10.1016/j.jctb.2004.08.001 (p. 3).
[RS83] Neil Robertson and Paul D Seymour. "Graph minors. I. Excluding a forest". In: Journal of Combinatorial Theory, Series B 35.1 (1983), pp. 39-61. dor: https://doi. org/10.1016/0095-8956(83)90079-5 (p. 21).
[RS86] N. Robertson and P. D. Seymour. "Graph minors. II. Algorithmic aspects of treewidth". In: Journal of Algorithms 7.3 (Sept. 1986), pp. 309-322. dor: https://doi.org/ 10.1016/0196-6774(86)90023-4 (pp. 3, 16-17).
[RS91] N. Robertson and P. D. Seymour. "Graph minors X. Obstructions to treedecomposition". In: Journal of Combinatorial Theory, Series B 52.2 (1991), pp. 153190. DOI: https://doi.org/10.1016/0095-8956(91)90061-N (p. 34).
[RTL76] Donald J. Rose, R. Endre Tarjan, and George S. Lueker. "Algorithmic Aspects of Vertex Elimination on Graphs". In: SIAM Journal on Computing 5.2 (1976), pp. 266283. DOI: 10.1137/0205021. eprint: https://doi.org/10.1137/0205021. url: https: //doi.org/10.1137/0205021 (p. 14).
[Sch19] Martin Schmidt. Functorial Approach to Graph and Hypergraph Theory. 2019. doi: https://doi.org/10.1145/3605776. arXiv: 1907.02574 [math.C0] (p. 35).
[Ser02] J-P. Serre. Trees. Springer Science \& Business Media, 2002 (p. 3).
[Ser70] J-P. Serre. "Groupes discrets: arbres, amalgames et SL2". In: duplicated notes, College de France (1970). url: http://numdam.org/item/AST_1983_46_1_0/ (p. 3).
[Ser77] Jean-Pierre Serre. Arbres, amalgames, $S L_{2}$. fr. Astérisque 46. Société mathématique de France, 1977. url: http://www.numdam.org/item/AST_1983__46__1_0/ (p. 30).
[Ser80] Jean-Pierre Serre. Trees. Springer, 1980. dor: https://doi.org/10.1007/978-3-642-61856-7 (pp. 30-32).
[Sha15] Farhad Shahrokhi. New representation results for planar graphs. 2015. arXiv: 1502. 06175 [math.C0] (pp. 3-4, 28).
[Sim05] Carlos T. Simpson. Explaining Gabriel-Zisman localization to the computer. 2005. arXiv: math/0506471 [math.CT] (p. 41).
[Spi13] D. I. Spivak. "The operad of wiring diagrams: formalizing a graphical language for databases, recursion, and plug-and-play circuits". In: arXiv preprint arXiv:1305.0297 (2013). url: https://doi.org/10.48550/arXiv. 1305.0297 (p. 5).
[ST93] P.D. Seymour and R. Thomas. "Graph Searching and a Min-Max Theorem for TreeWidth". In: Journal of Combinatorial Theory, Series B 58.1 (1993), pp. 22-33. issn: 0095-8956. url: https://doi.org/10.1006/jctb. 1993.1027 (p. 34).
[Sza22] Z. G. Szabó. "Compositionality". In: The Stanford Encyclopedia of Philosophy. Ed. by E. N. Zalta. Fall 2022. Metaphysics Research Lab, Stanford University, 2022. url: https://plato.stanford.edu/entries/compositionality/ (p. 2).
[TY84] Robert E. Tarjan and Mihalis Yannakakis. "Simple Linear-Time Algorithms to Test Chordality of Graphs, Test Acyclicity of Hypergraphs, and Selectively Reduce Acyclic Hypergraphs". In: SIAM Journal on Computing 13.3 (1984), pp. 566-579. dor: 10.1137/0213035. eprint: https://doi.org/10.1137/0213035. url: https://doi.org/ 10.1137/0213035 (p. 14).


[^0]:    *Instituto de Matemática e Estatística, Universidade de São Paulo. Rua do Matão, 1010 - 05508-090, São Paulo, SP, Brasil. This author acknowledges ERC funding under the European Union's Horizon 2020 research and innovation program (grant \# 803421, "ReduceSearch") which was received while at the Department of Mathematics and Computer Science of Eindhoven University of Technology. benjamin.merlin.bumpus(at)gmail.com
    ${ }^{\dagger}$ School of Computer Science and Engineering, University of New South Wales, z.kocsis(at)unsw.edu.au
    ${ }^{\ddagger}$ Independent researcher, jadeedenstarmaster(at)gmail.com
    ${ }^{§}$ CUNY CityTech, eminichiello(at)gmail.com

[^1]:    ${ }^{1}$ We invite the computationally-minded reader to furthermore experiment with structured decompositions via their implementation StructuredDecompositions.jl in Algebraic Julia.
    ${ }^{2}$ This is an instance of the more general notion of a Grothendieck construction.

[^2]:    ${ }^{3}$ The diagram category construction is well understood, see [PT21], and for further applications see [Pat21].

[^3]:    ${ }^{4}$ See [Rie17, Section 2.4].

[^4]:    ${ }^{5}$ We also allow for the indexing graphs to be multigraphs or digraphs to accommodate for examples like those in Section 3.6. We consider graphs, loop graphs, and reflexive loop graphs as special kinds of multigraphs, see Section A.1. For most examples of interest however $\mathscr{G}=$ Trees.
    ${ }^{6}$ In other words, if $X \in \Omega$ and $X \cong Y$, then $Y \in \Omega$.

[^5]:    ${ }^{7}$ We say that $\mathcal{F}$ is pullback-stable if for any $f: X \rightarrow Y$ in $\mathcal{F}$ and any map $g: Z \rightarrow Y$, the pullback $g^{*}(f): Z \times Y \rightarrow Z$ exists and belongs to $\mathscr{F}$.

[^6]:    ${ }^{8}$ Not to be confused with having all small limits.

[^7]:    ${ }^{10}$ We will actually do this for hypergraphs, which will immediately imply the same result for graphs.
    ${ }^{11}$ In fact, there are numerous cryptomorphic definitions for treewidth [BB72; Hal76; RS86; CE12].

[^8]:    ${ }^{12}$ Recall the complement of a graph $G$ is the graph $\bar{G}$ where $x y$ is an edge in $\bar{G}$ if and only $x$ and $y$ are not incident in $G$.

[^9]:    ${ }^{13}$ Also called the primal graph or clique graph of $H$.

[^10]:    ${ }^{14}$ Here and only here, we allow infinite trees!

[^11]:    ${ }^{15}$ which stands for directed graph schema.
    ${ }^{16}$ In [Bro+08], edges on a single vertex whose involution does not map to themselves are called bands, and those that do are called loops. In fact, it is known that in any conventional category of graphs that has exponential objects, this phenomenon must appear [Sch19, Introduction].

[^12]:    ${ }^{17}$ We took this notation from [EH20, Remark 2.2]. We note that $S^{(2)}$ is isomorphic to the set of cardinality two multi-subsets of $S$, i.e. subsets of cardinality two that allow for repeated elements. Our category of multigraphs is precisely the category of graphs that Eur and Huh consider in their paper.

[^13]:    ${ }^{18}$ But notice there that adhesive categories in particular have universal pushouts along monomorphisms. The category Gr does not even have all pushouts along monomorphisms. Both morphisms in the span must be monos in order for the pushout to exist.

