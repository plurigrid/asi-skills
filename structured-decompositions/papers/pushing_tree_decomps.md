# Lassos: Pushing Tree Decompositions Forward Along Homomorphisms 

Benjamin Merlin Bumpus* James Fairbanks ${ }^{\dagger} \quad$ Will J. Turner ${ }^{\ddagger}$

Friday $13{ }^{\text {th }}$ June, 2025


#### Abstract

It is folklore that tree-width is monotone under taking subgraphs (i.e. injective graph homomorphisms) and contractions (certain kinds of surjective graph homomorphisms). However, although tree-width is obviously not monotone under any surjective graph homomorphism, it is not clear whether contractions are canonically the only class of surjections with respect to which it is monotone. Under the requirement that the decomposition shape must be preserved, we prove that this is indeed the case.

Our results provide a framework for answering questions of this sort for many other kinds of combinatorial data structures (such as directed multigraphs, hypergraphs, Petri nets, circular port graphs, half-edge graphs, databases, simplicial sets etc.) for which natural analogues of tree decompositions can be defined. Furthermore and of independent interest, we prove these results by introducing the notion of a lasso, a generalization of contractions of graphs to arbitrary categories with pushouts of monomorphisms.


## 1 Introduction

1.1. Given any graph invariant $\mu$, it is always fruitful to enquire how $\mu$ behaves with respect to graph containment relations. This is often formalized as the question of determining whether the invariant $\mu$ gives rise to an order-preserving (or order-reversing) function $\mu:(\mathbb{G}, \triangleleft) \rightarrow(\mathbb{N}, \leq)$ from the poset of all graphs $(\mathbb{G}, \triangleleft)$ (viewed under some given order $\triangleleft$ ) to the natural numbers.

[^0]1.2. Graph invariants are often defined in terms of certain families of certifying objects which attest to the fact that a given graph attains some desired property. For instance, for any graph $G$, one has that: (1) $G$ has chromatic number at most $k$ if and only if it admits a proper coloring with at most $k$ colors; or (2) $G$ has tree-width at most $k$ if and only if it admits a tree decomposition of width at most $k$.
1.3. Often the relationship between graph invariants and containment relations can be furthermore carried over to a notion of monotonicity for the certificates for the invariant whereby one has a function mapping the certificates of one graph to the certificates on another. For instance, if $H$ is a subgraph of a graph $G$, then: (1) every proper coloring of $G$ induces a proper coloring of $H$ and (2) every tree decomposition of width at most $k$ of $G$ induces on $H$ a decomposition of the same kind.
1.4. Thus the relationship between the sets of certificates of an invariant $\mu$ and some given containment relation ◁ is best studied not through morphisms of posets of the form $\mu:(\mathbb{G}, \triangleleft) \rightarrow(\mathbb{N}, \leq)$, but instead through the notion of a functor $M$ : Grph → Set from the category ${ }^{1}$ of graphs and graph homomorphisms Grph to the category of sets.
1.5. In the case of tree decompositions, it has been recently shown [2] that there is a functor MDgm: Grph ${ }^{\text {op }}$ → Set taking each graph to the set of all of its decompositions (we recall this in Lemma B.2). This functor is contravariant, meaning that it reverses the direction of arrows: given any graph homomorphism
$$
G \xrightarrow{f} H
$$
there is a function
$$
\operatorname{MDgm}(G) \stackrel{\operatorname{MDgm}(f)}{\leftrightarrows} \operatorname{MDgm}(H)
$$
sending each decomposition of $H$ (i.e. an element of $\operatorname{MDgm}(H)$ ) to a decomposition of $G$ (i.e. an element of $\operatorname{MDgm}(G)$ ).
1.6. As is well-known in graph theory [4], it is easy to obtain such a mapping when the morphism $f$ is injective (i.e. $G$ is a subgraph of $H$ ). To see this, for any decomposition $d$ of $H$, observe that one obtains a decomposition of $G$ by intersecting each bag of $d$ with the image of $G$ under $f$.
1.7. In contrast, to the best of our knowledge, it was not formalized until recently that one can obtain a decomposition of $G$ from a decomposition of $H$ given any morphism $f: G \rightarrow H$, regardless of whether $f$ is injective or not. This is done by passing from "intersections" to the more general, categorical notion of a pullback: given any tree decomposition $d$ of $H$, one can pull $d$ back along any morphism $f: G \rightarrow H$ to obtain a tree decomposition of $G$ of

[^1]![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-03.jpg?height=347&width=401&top_left_y=378&top_left_x=863)
Figure 1: A trivial example of pulling a tree decomposition back along a graph homomorphism which is not injective. We are given two graphs $G$ and $H$, a graph homomorphism $f: G \rightarrow H$ and a tree decomposition of $H$ highlighted by the two colors of the edges of $H$ (the tree decomposition in question consists of two bags $\{x, y\}$ and $\{y, z\}$ with adhesion $\{y\}$ ). By pointwise pullback, one obtains a tree decomposition of $G$ consisting of the two bags $\left\{x_{1}^{\prime}, x_{2}^{\prime}, y^{\prime}\right\}$ and $\left\{y^{\prime}, z^{\prime}\right\}$.

the same shape (this result, stated not just for graphs, but in much greater generality, is due to Bumpus, Kocsis, Master and Minichiello [2] and is also recalled in the present paper as Lemma B.2) (see also Figure 1).
1.8. Thus, since one can pull any decomposition of a graph $H$ back along any morphism $f: G \rightarrow H$ to obtain a decomposition of $G$, it is natural to ask whether one can dually push decompositions forward. In other words we ask: "for which morphisms $f: G \rightarrow H$ can we produce a decomposition for $H$ starting with any decomposition of $G$ ?"
1.9. Any graph theorist comfortable with tree decompositions would immediately guess that, if $f$ in the preceding paragraph is a contraction map ${ }^{2}$ then we can always obtain a decomposition of $H$ from any decomposition $d$ of $G$ and moreover this decomposition will be of the same shape as $d$. This is well-known [4] and the intuitive idea is that one simply identifies any two vertices in any bag of $d$ if those vertices are identified by $f$.
1.10. It is thus natural to ask whether there are any other classes of surjective graph homomorphisms along which one can push a decomposition while leaving the shape of it unaltered. Here we answer this question negatively and show that contraction maps are the canonical class of maps with respect to which one can push decompositions forwards while not altering the decomposition shape. Furthermore, we generalize this result far beyond graphs and show that it holds for many other kinds of combinatorial objects (specifically the objects of any topos, quasitopos or any sufficiently well-behaved locally cartesian-closed category). Some examples of these, among others, include: sets, symmetric graphs, directed graphs, directed multigraphs, hypergraphs, Petri nets, databases, simplicial sets, circular port graphs and half-edge graphs.

[^2]1.11. To work at such a level of abstraction, we employ structured decompositions [2], recent category-theoretic generalization of graph decompositions which can be defined in any category. With lots of hand waving, structured decompositions are straightforward. One starts with a graph $J$ - the shape of the decomposition - and a category C of things one might want to decompose. Then a structured decomposition is an assignment $d$ of objects of C to each vertex (a 'bag' of the decomposition) and edge (an 'adhesion' of the decomposition) of $J$ together with homomorphisms specifying how the adhesions nestle into their corresponding bags. Waving our hands a little slower, a structured decomposition $d$ is a special kind of diagram in C where one thinks of $d$ as decomposing an object $c \in \mathrm{C}$ whenever colim $d=c$. All of this will be treated formally in Definition 2.8; for now however, a picture suffices (q.v. Figure 2).

![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-04.jpg?height=573&width=1119&top_left_y=936&top_left_x=504)
Figure 2: A structured decomposition of graphs whose shape is a triangle (i.e. a complete graph $K_{3}$ on three vertices). The bags (circled in blue) and the adhesions (circled in gold) are related by spans of injective graph homomorphisms: these are drawn componentwise where each vertex of an adhesion is sent to a vertex in a relevant bag.

1.12. To obtain our results, we embrace a light category theoretic perspective. Peering through this lens, one finds that every contraction map of graphs $f: G \rightarrow H$ arises as a pushout along a subobject of $G$ as in the following diagram.
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-04.jpg?height=183&width=269&top_left_y=2002&top_left_x=932)

This is to be read as follows: one first selects a subgraph $K$ of $G$, then one computes its connected components $\mathrm{cc}(K)$ (viewed as a reflexive ${ }^{3}$ discrete graph) and then the pushout

[^3]constructs $H$ by identifying each connected component of $K$ in $G$. Notice that, generalizing injective maps to monomorphisms and surjective maps to epimorphisms, the diagram above makes sense in any category having enough pushouts.
1.13. This category-theoretic take on the definition of a contraction map suggests a systematic way for defining classes of epimorphisms ${ }^{4}$ : one first defines a functor $\mathscr{L}:$ Grph → Grph taking each graph $K$ to a graph $\mathscr{L} K$ which is to be thought of as playing the role of connected components in the previous paragraph and then one finds a natural transformation $\eta: \mathrm{id}_{\text {Grph }} \rightarrow \mathscr{L}$ whose components are epimorphisms of the form $\eta_{x}: X \rightarrow \mathscr{L} X$. This defines a class of epimorphisms in Grph because, since pushouts preserve epimorphisms, one obtains an epimorphism $G \rightarrow G+{ }_{K} \mathscr{L} K$ by pushout as we did in Diagram 1. These observations lead us to the following definition in any category $C$ which will be our main subject of study.
1.14. Definition. A lasso on C is a pair $\left(\mathscr{L}: \mathrm{C} \rightarrow \mathrm{C}, \eta: \mathrm{id}_{\mathrm{C}} \Rightarrow \mathscr{L}\right)$ where:
(L1) $\mathscr{L}$ is a functor that preserves pushouts of monomorphic spans ${ }^{5}$; and
(L2) $\eta$ is a natural transformation, all of whose components are epimorphisms.
1.15. One can verify that connected components are an example of a lasso on the category of graphs (see Section 3). The following is a trivial example of a lasso on any category.
1.16. Example. Let C be a category. The trivial lasso on C is the lasso ( $\mathrm{id}_{\mathrm{C}}, \mathrm{id}_{\mathrm{id}_{\mathrm{C}}}$ ) composed of the identity functor and the identity natural transformation.
1.17. As we have been foreshadowing, one can abstract the category theoretic definition of a contraction of graphs to obtain the notion of a contraction with respect to a choice of lasso.
1.18. Definition. A category $C$ admits contractions with respect to a lasso $(\mathscr{L}, \eta)$ if the following pushout exists for all monomorphisms $f: X \hookrightarrow Y$ in C.
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-05.jpg?height=192&width=263&top_left_y=1787&top_left_x=928)

We call the pushout of $f$ and $\eta_{X}$ the contraction of $Y$ along $f$ and denote it by $Y_{/ f}$.
1.19. Definition 1.18 illuminates why Condition ( $\mathbf{L} \mathbf{2}$ ) is necessary in our definition of lassos (if not absolutely natural). However, we have not yet clarified the reason for the first

[^4]condition - namely the preservation of monic pushouts. Spelling this out, Condition (L1) prescribes that, if we are given any monic span $A \leftarrow a \rightharpoonup C\lrcorner b \rightarrow B$ with pushout $X$ in C , then the pushout of its image $\mathscr{L} A \leftarrow \mathscr{L} a-\mathscr{L} C-\mathscr{L} b \rightarrow \mathscr{L} B$ under $\mathscr{L}$ is $\mathscr{L} X$. Since a structured decomposition is nothing other than a diagram that is drawn by piecing spans of monomorphisms together, it follows by induction that Condition (L1) implies the preservation of all finite tree-shaped structured decompositions. Now, for any object $C$ in $C$, we can contract $C$ along a map $C \hookrightarrow C$ (itself) to obtain $\mathscr{L} C$ as a contraction; hence, without the preservation of monic pushouts, we have fallen at the first hurdle, let alone for more complicated contractions.
1.20. In Section 4 (q.v. Paragraph 4.25) we obtain the following result which shows that decompositions always interact nicely with lasso-contractions whenever one is working in what we call a mono-strong category (c.f. Definition 2.20). Examples of such categories include categories of: sets, symmetric graphs, directed graphs, directed multigraphs, hypergraphs, Petri nets, circular port graphs half-edge graphs, databases, simplicial sets etc..
1.21. Theorem. Suppose $C$ is a mono-strong category admitting pullback-stable colimits of shape $\int T \rightarrow \mathrm{C}$ for all trees $T$. If $d: \int T \rightarrow \mathrm{C}$ be a tree-shaped structured decomposition with colimit $Y$, then, for any lasso $(\mathscr{L}, \eta)$ on C and any monomorphism $f: X \hookrightarrow Y$, we have that:

1. we can push the diagram $d$ forwards along the $(\mathscr{L}, \eta)$-contraction $Y \rightarrow Y_{/ f}$ to obtain a diagram $d_{/ f}: \int T \rightarrow \mathrm{C}$ of the same shape;
2. the width ${ }^{6}$ of $d / f$ is at most that of $d$; and
3. $\operatorname{colim}\left(d_{/ f}\right)=(\operatorname{colim} d)_{/ f}=Y_{/ f}$.
1.22. Remark. Theorem 1.21 can be adapted to structured decompositions of arbitrary shape by imposing additional requirements on the definition of a lasso: in addition to preserving monic pushouts, one furthermore demands the preservation of colimits (qv. the notion of strong lassos given in Definition 4.3 and Proposition 4.18).
1.23. Our categorical treatment allows us to employ elementary arguments to conclude the following canonicity result. We will detail the arguments in Section 3 (q.v. Paragraph 3.18 in particular). In turn, this implies canonicity of the notion of contraction maps (Corollary 1.25).
1.24. Theorem. The connected component lasso is the only nontrivial lasso on the category Grph of directed multigraphs.

[^5]1.25. Corollary. In Grph the class of all epimorphisms with respect to which tree-width is monotone is precisely the class of contractions.

## 2 Preliminaries

2.1. In this section we will recall some basic categorical notions which we will need in the rest of the article. These include image factorizations in arbitrary categories, the epiand mono-triangle lemmas and a brief review of the category of graphs viewed as a functor category. Finally we will recall some examples of categories that admit pullback-stable colimits and show how many familiar kinds of combinatorial data structures (e.g. categories of: sets, symmetric graphs, directed graphs, directed multigraphs, hypergraphs, Petri nets, circular port graphs half-edge graphs, databases, simplicial sets etc.) assemble into such categories.
2.2. As is common in category theory, we view graphs as functors $G$ : SGr → Set where SGr is a category with only two objects called $E$ and $V$ and two non-identity morphisms $s, t: E \rightarrow V$ (the 'source' and 'target' maps). The functor category Set ${ }^{\mathrm{SGr}}$ - which we denote as Grph for convenience - has directed graphs (allowing loops and parallel edges) as objects and graph homomorphisms as arrows. To spell this out, notice that a functor $G$ : SGr → Set consists of:

- a set of vertices $G(V)$ and a set of edges $G(E)$
- a source function $G(s): G(E) \rightarrow G(V)$ and a target function $G(s): G(E) \rightarrow G(V)$ which map each edge of $G$ to its source and target vertices.

Being a functor category, the arrows in $\mathrm{Set}^{\mathrm{SGr}}$ are natural transformations. It is easy to verify that a natural transformation $\eta: G \Rightarrow H$ defines a graph homomorphism from $G$ to $H$.
2.3. As pointed out by Spivak [7], a functor category Set ${ }^{\mathrm{C}}$ (where C is finite) can be seen as a category of combinatorial data: the category C is playing the role of a schema that defines the kind of data structure one might be interested in (just as the category SGr was used to define Grph in the previous paragraph). For example, the following is the schema category used to define a category of Petri nets.
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-07.jpg?height=244&width=631&top_left_y=1965&top_left_x=747)

Such functor categories (also known as 'C-sets' [7,5]) all share certain properties in common with the category of graphs and in fact they all form presheaf toposes. Thus, rather than proving our results for each of these categories in turn, we will argue at the level of what we
will call mono-strong categories (c.f. Definition 2.20). Roughly, one should think of such a category as one where pushouts and pullbacks behave nicely with each other.
2.4. Example. Recall that a pushout in a category C is a colimit of a diagram of shape $\bullet \leftarrow \bullet \rightarrow \bullet$. Roughly this is to be thought of as the operation of 'gluing' two objects (the feet of the span) together along a third mediating object (the apex of the span). In the case of graphs, the pushout of a span $G_{1} \stackrel{f_{1}}{\stackrel{1}{\leftrightarrows}} G_{12} \xrightarrow{f_{2}} G_{2}$ is the cospan $G_{1} \rightarrow G_{1}+G_{12} G_{2} \leftarrow G_{2}$ where the graph $G_{1}+G_{12} G_{2}$ is defined as the quotient of the disjoint union $G_{1}+G_{2}$ of $G_{1}$ and $G_{2}$ under the equivalence relation which identifies two vertices (resp. edges) $x$ and $y$ of $G_{1}+G_{2}$ whenever there is a vertex (resp. edge) $w$ of $G_{12}$ such that $f_{1}(w)=x$ and $f_{2}(w)=y$.
2.5. Pushouts are special cases of more general constructions called colimits. The interaction of pushouts (or colimits more generally) with pullbacks is not always easy to determine. However, in many familiar cases such as toposes (e.g. categories of (co)presheaves c.f Paragraphs 2.2 and 2.3), quasitoposes and even more generally any locally cartesian-closed category, one has a strong property of pullback-stable colimits given below.
2.6. Definition. Let $\mathscr{J}$ be a class of diagrams in a category C with pullbacks and colimits of all diagrams in $\mathscr{J}$. One says that a C has pullback-stable colimits of type $\mathscr{J}$ if for any diagram $d$ in the class and any morphism $f: x \rightarrow \operatorname{colim}(d)$, the diagram $d^{\prime}$ obtained by taking pointwise pullbacks of the colimit cocone of $d$ and $f$ satisfies $\operatorname{colim}\left(d^{\prime}\right) \cong x$.
2.7. Structured decompositions, the category theoretic generalization of graph decompositions which we will use throughout this article, are most well-behaved in categories that have enough pullback-stable colimits.
2.8. Definition ([2]). For any graph $J$ one can define a category $\int J$ as follows:

1. each vertex $x$ of $J$ gives rise to an object of $\int J$;
2. each edge $e$ of $J$ gives rise to an object of $\int J$;
3. each edge $e=(x, y)$ in $J$ gives rise to precisely two arrows in $\int J$ : one from $e$ to $x$ and one from $e$ to $y$ (arrows of this kind are the only non-identity arrows in $\int J$ ).

Fixing a base category C , a C -valued structured decomposition of shape $J$ is a diagram of the form $d: \int J \rightarrow \mathrm{C}$ which assigns to each edge $e=(x, y)$ in $J$ a span $d(x) \hookleftarrow d(e) \hookrightarrow d(y)$ of monomorphisms (cf. Figure 2 where $J$ is taken to be the graph $K_{3}$ ). C -valued structured decompositions (of all shapes) assemble into a category $\mathfrak{D}(\mathrm{C})$ where a morphism from a structured decomposition $d_{1}: \int J_{1} \rightarrow \mathrm{C}$ to a structured decomposition $d_{2}: \int J_{2} \rightarrow \mathrm{C}$ is a pair
$(f, \gamma)$ of a functor $f$ and an natural transformation $\gamma: d_{1} \Rightarrow d_{2} f$ as in the following triangle.
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-09.jpg?height=286&width=401&top_left_y=466&top_left_x=861)
2.9. To aid intuition, we make an analogy to graph decompositions. Fix any decomposition $d: \int J \rightarrow \mathrm{C}$. For any vertex $x$ in $J$, think of the object $d(x)$ in C as a bag of the decomposition. Given any edge $e=(x, y)$ of $G$, think of $d(e)$ as an adhesion of the decomposition. The span $d(x) \hookleftarrow d(e) \hookrightarrow d(y)$ specifies how the adhesion fits into its corresponding bags. One says that $d$ decomposes an object $x$ if $\operatorname{colim} d=x$.
2.10. Other than categories with pullback-stable colimits and structured decompositions, we will also frequently use image factorizations. These are the categorical generalization to arbitrary categories of the notion of factorizing a function of sets (or a group homomorphism, etc.) through its image.
2.11. Definition. By a factorization of a morphism $X \xrightarrow{f} Y$, we mean any pair of composable morphisms $X \xrightarrow{g} Z \xrightarrow{h} Y$ such that $h g=f$. We will say that the factorization is mono if $h$ is a monomorphism. The image factorization of a morphism $f: X \rightarrow Y$, if it exists, is the mono-factorization denoted $X \xrightarrow{\mathrm{mi} f} \operatorname{Im} f \xrightarrow{\mathrm{im} f} Y$ which is initial in the category of mono-factorizations.
2.12. Definition 2.11 can be unpacked as follows: a mono-factorization $X \xrightarrow{\mathrm{mi} f} \operatorname{lm} f \xrightarrow{\mathrm{im} f} Y$ of a morphism $f$ is its image factorization if, for any other mono-factorization $X \rightarrow Z \hookrightarrow Y$ of $f$ there is a unique morphism $\operatorname{Im} f \rightarrow Z$ making the following diagram commute.
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-09.jpg?height=317&width=381&top_left_y=1774&top_left_x=870)
2.13. It is a folkloric fact (q.v. Riehl [6]) that, if a category has all equalizers, then image factorizations consist of an epimorphism and a monomorphism respectively (i.e. they are epi-mono-factorizations). This is the case in the category of sets, the category of graphs, any functor category Set ${ }^{\mathrm{J}}$ and indeed any topos. Another feature common to many of these examples is that of being balanced.
2.14. Definition. A category is balanced if, for any morphism, being both monomorphic and epimorphic implies being an isomorphim.
2.15. It will often be very useful in the proofs of the next section to be able to deduce, given a commutative triangle, if one of the three arrows is an epimorphism (or a monomorphism) when it is known that the other two also are. Thus we recall the following folkloric lemma.
2.16. Lemma (epi-triangle lemma). In any category, suppose that $y x$ is a factorisation of some epimorphism $f$. Then $y$ is an epic.
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-10.jpg?height=145&width=313&top_left_y=829&top_left_x=906)

Proof. For all $p, q: Y \rightarrow A$, if $p y=q y$ then $p f=p y x=q y x=q f$. Since $y$ is epic, $p=q$. Qed.
2.17. For ease of reference we note that by categorical duality Lemma 2.16 also implies the following: if a monomorphism $f$ factors as $x y$, then $y$ is monic.
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-10.jpg?height=141&width=313&top_left_y=1284&top_left_x=906)
2.18. Lemma. Let $A \xrightarrow{g} B \xrightarrow{f} C$ be two arrows in a balanced category $C$ admitting image factorisations. If $g$ is epic, then $\operatorname{lm} f \circ g$ and $\operatorname{lm} f$ are isomorphic.

Proof. By the universal property of images, we get a unique map $q: \operatorname{lm} f \rightarrow \operatorname{lm} f \circ g$ making the following commute.
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-10.jpg?height=317&width=577&top_left_y=1748&top_left_x=773)

Applying Results 2.16, 2.17, yields that $q$ is an isomorphism.
Qed.
2.19. Throughout the rest of the article we will be always working with categories which we call $\mathscr{J}$-strong. These include all toposes and hence all of the combinatorial examples we mentioned earlier.
2.20. Definition. Let $\mathscr{J}$ be a class of diagrams in a category C , we say that C is $\mathscr{J}$-strong if the following conditions are satisfied:

1. C is balanced,
2. C has pullbacks and equalizers and
3. C has pullback-stable colimits of type $\mathscr{J}$.

We say that C is mono-strong if $\mathscr{J}$ is the class of all monic diagrams (i.e. diagrams whose image consists only of monomorphisms).
2.21. Notice that, by having all equalizers, $\mathscr{J}$-strong categories always admit epi-monofactorizations.

## 3 The category of lassos

3.1. To study the space of possible lassos on a given category, we introduce the following notion.
3.2. Definition (The category of lassos). Let C be a category. The category of lassos on C - denoted Lasso( C ) - has as objects the lassos on C and its morphisms $f:(\mathscr{L}, \eta) \rightarrow\left(\mathscr{L}^{\prime}, \eta^{\prime}\right)$ are given by collections of epimorphisms ${ }^{7}\left(f_{A}: \mathscr{L} A \rightarrow \mathscr{L}^{\prime} A\right)_{A \in \mathrm{C}}$ indexed by the objects of C making the following triangle commute.
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-11.jpg?height=190&width=429&top_left_y=1491&top_left_x=846)

The composition of morphisms is given by the composition of the underlying maps.
3.3. Let $(\mathscr{L}, \eta)$ and $\left(\mathscr{L}^{\prime}, \eta^{\prime}\right)$ be lassos on some category C . Let $\eta^{\prime} \circ \eta: \mathrm{id}_{\mathrm{C}} \Rightarrow \mathscr{L}^{\prime} \circ \mathscr{L}$ be the vertical composition of $\eta^{\prime}$ after $\eta$. That is, elementwise we have $\left(\eta^{\prime} \circ \eta\right)_{X}= \left(\eta^{\prime}\right)_{\mathscr{L} X} \circ(\eta)_{X}$. It is easy to check that the pair $\left(\mathscr{L}^{\prime} \circ \mathscr{L}, \eta^{\prime} \circ \eta\right)$ is a lasso on C . In this context, we write $\left(\mathscr{L}^{\prime}, \eta^{\prime}\right) \circ(\mathscr{L}, \eta):=\left(\mathscr{L}^{\prime} \circ \mathscr{L}, \eta^{\prime} \circ \eta\right)$ and call it the composition of $(\mathscr{L}, \eta)$ and $\left(\mathscr{L}^{\prime}, \eta^{\prime}\right)$.
3.4. Observe that the collection $\eta_{\mathscr{L} X}$ is a morphism in the category of lassos from $(\mathscr{L}, \eta)$ to $\left(\mathscr{L}^{\prime}, \eta^{\prime}\right) \circ(\mathscr{L}, \eta)$. Further observe that the trivial lasso is the identity with respect to the composition of lassos. In Appendix C, we prove that the category of lassos can be viewed as a single object double category.

[^6]3.5. It is easy to verify that, for a given lasso $(\mathscr{L}, \eta)$, the collection $\eta_{X}$ is the unique morphism from the trivial lasso to $(\mathscr{L}, \eta)$ in the category of lassos. Hence the trivial lasso is the initial object in the category of lassos.

## The special case of Graphs: canonicity of contractions.

3.6. In this section, we will see that there is exactly one nontrivial lasso on Grph. Firstly, we prove a few results that let us map out the category of lassos.
3.7. Proposition. There is a cocontinuous functor cc: Grph → Grph which maps any graph $G$ to the graph $\operatorname{cc}(G)$ obtained by quotienting the vertex set of $G$ by the connectivity relation.
3.8. In the proof of the above proposition, we require the coequaliser of graphs. A coequaliser is the colimit of a diagram of the form
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-12.jpg?height=102&width=197&top_left_y=1044&top_left_x=966)

For graphs $H$ and $G$, along with a pair of graph homomorphisms $a, b: H \rightarrow G$, the coequaliser is a graph $C$ obtained from $G$ by the following identifications: vertices $u$ and $v$ are identified if they are the images $a(w)$ and $b(w)$ of a single vertex $w$ in $H$. Edges $e$ and $f$ are identified if they are the images $a(g)$ and $b(g)$ of a single edge $g$ in $H$.

Proof of Proposition 3.7. Let cc denote the map that sends each graph to the graph obtained by quotienting its vertex set by the connectivity relation. Since graph homomorphisms preserve the connectivity relation, we can extend cc to a functor by sending each graph homomorphism $f: G \rightarrow H$ to the map from $\mathrm{cc}(G)$ to $\mathrm{cc}(H)$ that sends each vertex to the the representative of its equivalence class in the image of $f$. This map $\operatorname{cc}(f)$ acts on the edge set of $\mathrm{cc}(G)$, which is the same as the edge set of $G$, identically to $f$. Given a graph $G$, let $\pi_{G}: G \rightarrow \mathrm{cc}(G)$ be the map corresponding to the 'action of cc'. That is, the map sending each vertex to its representative in the quotient and acting as the identity on edges. Observe that the maps $\pi_{G}$ assemble into a natural transformation $\pi$ : $\mathrm{id}_{\mathrm{Grph}} \Rightarrow \mathrm{cc}$.
We are required to show that cc preserves all coproducts and coequalisers. For coproducts, this follows immediately because they cannot change the connectivity relation. For coequalisers, let $a, b: H \rightarrow G$ be an arbitrary pair of graph homomorphisms. Consider the diagram $\mathrm{cc}(a), \mathrm{cc}(b): \mathrm{cc}(H) \rightarrow \mathrm{cc}(G)$. Observe that if a pair of vertices $u$ and $v$ in $G$ are the images $a(w)$ and $b(w)$ of a single vertex in $H$, then $\pi_{G}(u)$ and $\pi_{G}(v)$ in $\mathrm{cc}(G)$ are the images of $\pi_{G}(a(w))$ and $\pi_{G}(b(w))$, which, by the naturality of $\pi$, are in turn equal to $\operatorname{cc}(a)\left(\pi_{H}(w)\right)$ and $\operatorname{cc}(b)\left(\pi_{H}(w)\right)$, respectively. Hence the identification of $u$ and $v$ in the coequaliser of $a, b: H \rightarrow G$ implies the identification of $\pi_{G}(u)$ and $\pi_{G}(v)$ in the image of the coequaliser under cc. For the converse, suppose that $\pi_{G}(x)$ and $\pi_{G}(y)$ are the images of a single vertex $\pi_{G}(z)$ (for some choice of representative $z$ from $H$ ). Then there are vertices $x^{\prime}, y^{\prime}$ and $z^{\prime}$ in the connected components containing $x, y$ and $z$, respectively, so that $z^{\prime}=a\left(x^{\prime}\right)=b\left(y^{\prime}\right)$. Since graph homomorphisms preserve the connectivity relation, we get that there is one component

![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-13.jpg?height=300&width=682&top_left_y=382&top_left_x=717)
Figure 3: An illustration of the action of the connected components lasso on a particular graph $G$

of the coequaliser of $a, b: H \rightarrow G$ containing the vertices $a(x)$ and $b(y)$. Hence these have the same image in the image of the coequaliser under cc. This completes our claim that cc preserves coequalisers.

## Qed.

3.9. We call the lasso defined by the above the connected components lasso on Grph and we denote its associated natural transformation by $\pi$ : $\mathrm{id}_{\mathrm{Grph}} \Rightarrow \mathrm{cc}$.
3.10. Lemma. Let $\mathscr{F}$ be a functor from Grph to Grph along with a natural transformation $\alpha: \mathrm{id}_{\mathrm{Grph}} \Rightarrow \mathscr{F}$ whose components are epic. Let $\S$ be the graph with one vertex and two loops. If for some graph $G$, we have that $\alpha_{G}$ identifies a pair of edges in $G$, then $\alpha_{\rho}$ maps $\delta$ to the terminal graph ${ }^{8}$.

Proof. Suppose there is a graph $G$ containing a pair of edges $e$ and $e^{\prime}$ such that $e$ and $e^{\prime}$ are identified by $\alpha_{G}: G \rightarrow \mathscr{F}(G)$. Then let $f: G \rightarrow \infty$ denote a homomorphism which identifies all vertices in $G$ and maps $e$ and $e^{\prime}$ to different loops in $\S$. By the functoriality of $\mathscr{F}$ and the fact that the components of $\alpha$ are epic, we have that $\mathscr{F}(\varnothing)$ is the terminal graph. This situation is depicted in Figure 4.
Qed.
3.11. Lemma. Let $\mathscr{F}$ be a functor from Grph to Grph and suppose there is a natural transformation $\alpha: \operatorname{id}_{\mathrm{Grph}} \Rightarrow \mathscr{F}$ whose components are epic. Let $\delta$ be the graph with one vertex and two loops. If $F$ maps $\circ$ to the terminal graph, then $F$ does not preserve monic pushouts.

Proof. Let $d$ be the diagram consisting of the monic span of two single vertices with loops over a vertex with no loop, as in Figure 5. Observe that $\delta$ is the colimit of $d$. That is, a monic pushout. Further observe that, since the components of $\alpha$ are epic, the diagram $d$ is unchanged under $F$. Hence the colimit of $F(d)$ is $\S$, which is not $F(\S)$.
Qed.
3.12. We say that a graph homomorphism is vertex-trivial if its vertex map is a bijection.

[^7]![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-14.jpg?height=656&width=662&top_left_y=371&top_left_x=741)
Figure 4: A depiction of the proof of Lemma 3.10

![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-14.jpg?height=445&width=955&top_left_y=1160&top_left_x=584)
Figure 5: A depiction of the counterexample from Lemma 3.11

We say that a lasso is vertex-trivial if all of the components of its natural transformation are vertex-trivial. We define edge-triviality analogously.
3.13. Lemma. All lassos on Grph are edge-trivial.

Proof. Let $(\mathscr{L}, \eta)$ be a lasso on Grph and suppose for a contradiction that for some graph $G$, the map $\eta_{G}$ identifies a pair of edges in $G$. By combining Lemma 3.10 and Lemma 3.11, we get that $\mathscr{L}$ does not preserve monic pushouts, a contradiction.
Qed.
3.14. Corollary. The trivial lasso is the unique vertex-trivial lasso on Grph.

Qed.
3.15. Lemma. The connected components lasso ( $\mathrm{cc}, \pi$ ) is the terminal object in the category
of lassos on Grph.
Proof. Let $(\mathscr{L}, \eta)$ be a lasso on Grph. We are required to show that there is a unique map from $(\mathscr{L}, \eta)$ to $(\mathrm{cc}, \pi)$ in the category of lassos on Grph. Suppose first that for every graph $G$ and every pair of vertices $u$ and $v$ in $G$ that lie in distinct connected components, we have that $\eta_{G}(u)$ and $\eta_{G}(v)$ are distinct. Then for each vertex $w$ in $\mathscr{L} G$, there is a unique vertex $f_{G}(w)$ in cc $G$ so that for all $u \in \eta_{G}^{-1}(w)$ we have $\pi_{G}(u)=f_{G}(w)$. The function $f_{G}$ extends uniquely to a homomorphism $\mathscr{L} G \rightarrow \mathrm{cc} G$ by sending every edge $x y$ to the single loop at the vertex $f_{G}(x)=f_{G}(y)$.
Now suppose for a contradiction that there is some graph $G$ and a pair of vertices $x$ and $y$ in different connected components of $G$ so that $\eta_{G}$ identifies $x$ and $y$. Let $o^{\circ}$ be the graph with two vertices and a loop at each vertex. Let $h: G \rightarrow 0^{\circ}$ be a homomorphism sending each of $x$ and $y$ to separate vertices. By the naturality of $\eta$ and the fact that $\eta_{\circ} \circ$ is epic, we have that $\mathscr{L}_{\circ}$ ⊙ must be a graph consisting of a single vertex. However, $\odot^{\circ}$ is the coproduct of two copies of a single vertex with a loop. Since coproducts are monic pushouts over an empty graph, we get a contradiction to the fact that $\mathscr{L}$ preserves monic pushouts.
Qed.
3.16. Lemma. Suppose that $(\mathscr{L}, \eta)$ is a lasso on Grph which is not vertex-trivial. Let $G$ be an arbitrary graph. Then $\mathscr{L} G$ has one vertex for every connected component of $G$ and $\eta_{G}: G \rightarrow \mathscr{L} G$ maps each vertex to the representative of its component. Furthermore, $\mathscr{L} G$ has no edges between distinct vertices.

Proof. Let $G$ be a graph so that $\eta_{G}$ identifies some pair $x$ and $y$ of its vertices. Let be the graph consisting of two vertices, each having a loop, along with an edge in each direction between the two. Then there is a morphism $f: G \rightarrow$ sending each of $x$ and $y$ to a distinct vertex of $\mathrm{L}^{2}$. By naturality of $\eta$, we conclude that $\mathscr{L}$ is a graph consisting of a single vertex (but its number of loops is yet undetermined).
Let $\mathscr{T}$ be the graph consisting of a single edge. Observe that colimit of the following structured decomposition.
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-15.jpg?height=179&width=957&top_left_y=1774&top_left_x=586)

Since $\mathscr{L}$ preserves monic pushouts, and hence preserves structured decompositions, the image of the above diagram under $\mathscr{F}$ should have $\mathscr{L}$ as a colimit. By Lemma 3.15, the functor $\mathscr{L}$ cannot map the graphs having two disconnected vertices to a graph with only one vertex. Hence, in order to produce the right colimit, $\mathscr{L} \neq 0$ must be the terminal graph.
Now let $G$ be an arbitrary graph and observe that for every edge $e$ of $G$ there is a morphism $f: \mathscr{l} \rightarrow G$ which maps $\mathscr{l}$ onto $e$. By naturality, we must have that the endvertices of $e$ are identified by $\eta_{G}$. Since $e$ was chosen arbitrarily, all pairs of endvertices of edges are identified. By Lemma 3.15, no vertices between connected components are identified by $\eta_{G}$
and we conclude that $\eta_{G}$ maps each vertex to a representative of its connected component. Finally, we note that there are no edges between vertices of $\mathscr{L} G$ since $\eta_{G}$ is epic and this would imply edges between connected components of $G$.
Qed.
3.17. Now we prove Theorem 1.24, which states that the connected components lasso is the only nontrivial lasso on the category of graphs.
3.18. Proof of Theorem 1.24. Let $(\mathscr{L}, \eta)$ be a nontrivial lasso on Grph. By Lemma 3.13, the lasso $(\mathscr{L}, \eta)$ is edge-trivial but not vertex-trivial. By Lemma 3.16, we conclude that $(\mathscr{L}, \eta)$ is the connected components lasso.
Qed.
3.19. By the above analysis, the category of lassos on Grph is simply the following category of two objects.

$$
(\mathrm{id}, \mathrm{id}) \longrightarrow(\mathrm{cc}, \pi)
$$

3.20. Remark. The category Grph is the category of directed multigraphs. If we restrict our attention to the category of undirected multigraphs, it is easy to see that all of the above results specialize and hence the category of lassos is essentially identical to the above.

## Examples of lassos beyond Grph

## Reflexive graphs

3.21. There are two equivalent ways to define the category of reflexive graphs. Firstly, one may take the objects to be the all graphs, but allow the morphisms to map edges to vertices. Secondly, we can modify the schema that defines Grph so that every vertex comes with a distinguished loop. We will use this second formulation. The category
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-16.jpg?height=165&width=129&top_left_y=1705&top_left_x=999)
which we will denote by SRGr , is endowed with the equations

$$
s \circ l=\mathrm{id}_{V} \text { and } t \circ l=\mathrm{id}_{V}
$$

We abbreviate the category Set $^{\mathrm{SRGr}}$ of reflexive graphs by RGrph. We will see that RGrph admits a richer category of lassos than Grph. Indeed, we obtain the category depicted in Figure 6. Since its explication requires a few pages, we leave the details to Appendix A.
3.22. Remark. It is also interesting to mention that, unlike the other lassos we've seen so far, some of the lassos in Figure 6 are not idempotent. In particular, there are some lassos for which performing the action of the lasso twice is equivalent to the action of the terminal lasso, and not the original lasso.

![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-17.jpg?height=269&width=1045&top_left_y=408&top_left_x=541)
Figure 6: The category of lassos on RGrph

## Edge-coloured graphs

3.23. Whereas Grph and RGrph are defined by the schema SGr and SRGr, respectively, we can represent $k$-edge-coloured graphs using following schema. Denote by $\mathrm{CGr}_{k}$ the following category.
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-17.jpg?height=141&width=311&top_left_y=1048&top_left_x=906)

Then the objects of $\mathbf{S e t}^{\mathrm{CGr}_{k}}$ can be interpreted as graphs whose edges recieve one of $k$ colours. The morphisms between them are exactly the graph homomorphisms which preserve the colour of edges.
3.24. For each colour $i=1, \ldots, k$, we obtain a lasso $\left(\mathscr{L}_{i}, \eta^{i}\right)$ which acts on $k$-edge-coloured graphs by identifying vertices which are connected by edges of colour $i$. Given lassos $\left(\mathscr{L}_{i}, \eta_{i}\right)$ and $\left(\mathscr{L}_{j}, \eta_{j}\right)$, we obtain a lasso $\left(\mathscr{L}_{i, j}, \eta_{i, j}\right)$ by composing the underlying maps. We remark that it doesn't matter the order in which we do this. The category of lassos on $\mathbf{S e t}^{\mathrm{CGr}_{k}}$ is generated by composing the basic lassos $\left(\mathscr{L}_{i}, \eta_{i}\right)$. That is, it is the directed $k$-cube.
3.25. Example. The category of lassos on Set ${ }^{\mathrm{CGr}_{3}}$, the category of 3-edge-coloured graphs, is the following cube.
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-17.jpg?height=390&width=843&top_left_y=1791&top_left_x=640)

## simplicial sets

3.26. The category of simplicial sets extends the category of graphs. We define it to be

Set $^{\Delta^{\mathrm{op}}}$, the category of presheaves over the simplex category $\Delta$ (c.f. [6, Ex. 1.3.7. pt. vi]).
3.27. Given $n \geq 1$ and a simplicial set $D$, let $\sim_{n}$ be the relation on vertices of $D$ given by being contained in the same $n$-dimensional face and let $\approx_{n}$ be its transitive closure. For a graph $G$, viewed as a simplicial set, the relation $\approx_{1}$ is simply the connectivity relation on vertices.
3.28. For each $n \geq 1$, the relation $\approx_{n}$ defines a lasso ( $\mathrm{cc}_{n}, \eta^{n}$ ). Indeed, its action identifies all related vertices. For each pair $i, j$, the action of $\mathrm{cc}_{i}$ commutes with the action $\mathrm{cc}_{j}$. Furthermore, lassos with a lower index are strictly stronger than those with a higher index, in the sense that the composition of a pair of such lassos is equal to the one with a lower index. This is shown below. However, we refrain from providing an exhaustive characterization of the category of lassos of simplicial sets (like we have done for Grph and RGrph). Instead this is left as future work.

$$
(\mathrm{id}, \mathrm{id}) \longrightarrow \ldots \longrightarrow\left(\mathrm{cc}_{3}, \eta^{3}\right) \longrightarrow\left(\mathrm{cc}_{2}, \eta^{2}\right) \longrightarrow\left(\mathrm{cc}_{1}, \eta^{1}\right)
$$

## 4 Lifting Contractions to Diagrams

4.1. In this section we will show how to push decompositions forward along lasso contractions. The picture to keep in mind is the following.
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-18.jpg?height=347&width=528&top_left_y=1396&top_left_x=792)

Here we are given a lasso contraction $Y \rightarrow Y_{/ f}$ along a subobject $X \hookrightarrow Y$. The goal is to be able to push any structured decomposition $d$ whose colimit is the object $Y$ forward along the contraction map $\eta_{X}^{\#}$ (by image factorizations) to obtain a structured decomposition $d_{/ f}$ whose colimit is $Y_{/ f}$.
4.2. It turns out to be slicker to prove something slightly different to our main result. Indeed, we make the following definition of 'strong lassos' and work with them for the rest of the section. The proof of our main result can easily be derived from the proofs of the following (as we will explain at the end of this section).
4.3. Definition (Strong lasso). Let $(\mathscr{L}, \eta)$ be a lasso on a category C . We say that $(\mathscr{L}, \eta)$ is strong if the functor $\mathscr{L}$ preserves the colimits of all monic diagrams (on top of preserving monic pushouts).
4.4. One might think it would be possible to build our required diagram simply by contracting each individual object in $d$ along its 'intersection' with $X$. However the following example for graphs shows that this is not the case.
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-19.jpg?height=454&width=1239&top_left_y=554&top_left_x=442)

Indeed, the diagram of three graphs in the top right builds $Y$ as a colimit, but we cannot assemble the three graphs in the bottom right into a tree decomposition which builds $Y / f$ (indeed note that one no longer has a span of monomorphism). The graphs in the bottom right are obtained by contracting the subgraphs corresponding to $X$ in each of the three top-right graphs. All of this is to say that it is not enough to simply apply the lasso contraction point-wise. Instead we will make use of image factorizations of the global lasso contraction.
4.5. We now seek to introduce the notion of a diagram of images (Definition 4.7). To define it formally, we will first need to establish Lemma 4.6 below. In the meantime, as a first pass, we remark that a diagram of images is exactly what it sounds like: it is the diagram $\operatorname{Im}(\Omega, d)$ one obtains by point-wise image factorizations of a cocone $\Omega$ sitting above a given diagram $d: \mathrm{J} \rightarrow \mathrm{C}$. This is visualized as follows.
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-19.jpg?height=248&width=413&top_left_y=1628&top_left_x=582)
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-19.jpg?height=244&width=411&top_left_y=1632&top_left_x=1117)
4.6. Lemma. Consider the following commutative diagram in a category C which admits all image factorizations.
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-19.jpg?height=241&width=588&top_left_y=2099&top_left_x=766)

If $b q=a$, then there exists a unique monomorphism $u: \operatorname{im} f a \rightarrow \operatorname{im} f b$ that makes the following diagram commute.
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-20.jpg?height=291&width=974&top_left_y=494&top_left_x=571)

Proof. Consider the path of morphisms $A \xrightarrow{q} B \xrightarrow{b} G \xrightarrow{f} H$. Taking two image factorizations and applying the universal property of $\operatorname{Im}(f b q)$, one finds a unique morphism $u: \operatorname{Im}(f b q) \rightarrow \mathrm{Im}(f b)$ making the following commute.
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-20.jpg?height=265&width=781&top_left_y=992&top_left_x=670)

This concludes the proof since $f b q=f a$ and since $u$ is monic (q.v. Paragraph 2.17).
Qed.
4.7. Definition. Given a diagram $d: \mathrm{J} \rightarrow \mathrm{C}$ and a cocone $\Omega$ over $d$, we can define a diagram $\operatorname{lm}(\Omega, d): \mathrm{J} \rightarrow \mathrm{C}$ whose objects come from taking the image factorisation of each $\Omega_{i}$ and whose maps arise as in Lemma 4.6. We call the diagram obtained in this way the diagram of images obtained from the cocone $\Omega$ (cf. Paragraph 4.5).
4.8. Using the language of Definition 4.7, we can now state Theorem 4.9 which establishes the desired diagram corresponding to a lasso contraction.
4.9. Theorem. Let $(\mathscr{L}, \eta)$ be a strong lasso on a mono-strong category C . Let Y be an object of C which arises as a colimit of a monic diagram $d: \mathrm{J} \rightarrow \mathrm{C}$. Denoting by $\Lambda$ the cocone sitting above $d$, for any monomorphism $f: X \hookrightarrow Y$, let $d_{/ f}: \mathrm{J} \rightarrow \mathrm{C}$ denote the diagram of images $\operatorname{Im}\left(\eta_{X}^{\sharp} \Lambda, d\right): \mathrm{J} \rightarrow \mathrm{C}$ obtained from the cocone $\eta_{X}^{\sharp} \Lambda$. That is, the cocone whose components are the composition of the components of $\Lambda$ with the contraction map $\eta_{X}^{\sharp}$. Then $d_{/ f}$ has colimit $Y_{/ f}$.
4.10. Rather than giving a proof of Theorem 4.9 (we defer it to later on in this section, q.v. Paragraph 4.24), we will instead construct the required diagram $d_{/ f}$ as a pushout of diagrams (Proposition 4.18 and Theorem 4.20) and then prove this construction is equivalent to that of Theorem 4.9. This indirect proof approach of ours has a two benefits: (1) it clarifies the cryptomorphic relationship between the two constructions and (2) it allows for a short and conceptual proof (see Proposition 4.18).
4.11. Building towards this more conceptual proof, consider now a lasso contraction $Y_{/ f}$ of an object $Y$ with respect to a subobject $f: X \hookrightarrow Y$. Given any J-shaped diagram $d$ with colimit $(Y, \Lambda)$, one can define a family of objects $X_{i}:=X \times_{Y} d(i)$ indexed by $i \in \mathrm{~J}$ by point-wise pullback of $f$ and $\Lambda_{i}$.
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-21.jpg?height=261&width=620&top_left_y=610&top_left_x=749)

When C is mono-strong, the family $X_{i}$ assembles into a J -shaped diagram whose colimit object is $X$. Moreover, this can be done functorially: the following result, whose proof we defer to the apendix, is a corollary of theorem of Bumpus, Kocsis, Master and Minichiello [2].
4.12. Corollary. The functor MDgm : $\mathrm{C}^{\mathrm{op}} \rightarrow$ Set in Lemma B.2, which sends objects to their sets of structured decompositions, extends to a functor

$$
\mathscr{M}: \mathrm{C}^{\mathrm{op}} \rightarrow \text { Cat. }
$$

Proof. See Appendix B.
Qed.
4.13. We have already seen in Paragraph 4.4 that we cannot naively construct our new diagram by individually contracting each $d(i)$ along the subobjects $f_{i}: X_{i} \hookrightarrow d(i)$ as defined in Paragraph 4.11. Instead, we want each object to respect the global changes that happen in the contraction along $f$ that might not be respected locally in a contraction along each $f_{i}$. To that end, we define a diagram whose objects are the images of each $X_{i}$ under the whole contraction map. The first step is to show that any diagram has the same colimit as its associated diagram of images.
4.14. Lemma. Let C be a category with image factorizations and colimits of shape J . If $d: \mathrm{J} \rightarrow \mathrm{C}$ is a diagram with colimit cocone $\Lambda$, then $\operatorname{colim} \operatorname{Im}(\Lambda, d) \cong \operatorname{colim} d$.

Proof. We will show that the category of cocones over $d$ is isomorphic to the category of cocones over $\operatorname{Im}(\Lambda, d)$. As such, the two categories will have the same terminal object: i.e. $\operatorname{colim} d \cong \operatorname{colim} \operatorname{Im}(\Lambda, d)$.
To see that, suppose that $\left(z_{i}\right)_{i \in J}$ is a family of cocone arrows over $d$ with apex $Z$. Let $f: i \rightarrow j$
be a morphism in J and consider the following diagram.
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-22.jpg?height=295&width=857&top_left_y=481&top_left_x=635)

Since $\left(\left(z_{i}\right)_{i \in J}, Z\right)$ is a cocone, we have that $z_{i}=z_{j} \circ d(f)$ and so

$$
w \circ \operatorname{im}\left(\Lambda_{i}\right) \circ \operatorname{mi}\left(\Lambda_{i}\right)=z_{i}=z_{j} \circ d(f)=w \circ \operatorname{im}\left(\Lambda_{j}\right) \circ \operatorname{lm}(\Lambda, d)(f) \circ \operatorname{mi}\left(\Lambda_{i}\right)
$$

and hence, since $\mathrm{mi}\left(\Lambda_{i}\right)$ is an epimorphism, we have that

$$
w \circ \operatorname{im}\left(\Lambda_{i}\right)=w \circ \operatorname{im}\left(\Lambda_{j}\right) \circ \operatorname{lm}(\Lambda, d)(f) .
$$

In other words, we have that $\left(\left(w \circ \operatorname{im}\left(\Lambda_{i}\right)\right)_{i \in J}, Z\right)$ is a cocone over $\operatorname{Im}(\Lambda, d)$.
Conversely, suppose that $\left(z_{i}\right)_{i \in J}$ is a family of cocone arrows over $\operatorname{Im}(\Lambda, d)$ with apex $Z$ as shown in the following diagram.
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-22.jpg?height=304&width=857&top_left_y=1359&top_left_x=635)

Since $\operatorname{lm}(\Lambda, d)(f) \circ \operatorname{mi}\left(\Lambda_{i}\right)=\operatorname{mi}\left(\Lambda_{j}\right) \circ d(f)$, one has that $\left(\left(z_{i} \circ \operatorname{mi}\left(\Lambda_{i}\right)_{i \in J}, Z\right)\right.$ is a cocone over $d$, as desired.
Thus we have shown that every cocone over $d$ yields a cocone over $\operatorname{Im}(\Lambda, d)$ and viceversa. This can be easily seen to yield an isomorphism of categories Cocones $(d) \cong$ Cocones $(\operatorname{Im}(\Lambda, d))$.
Qed.
4.15. Lemma. Let $(\mathscr{L}, \eta)$ be a strong lasso on an mono-strong category C with all colimits. Given any monic diagram $d$ with colimit cocone $(\Lambda, X)$, let

$$
\mathscr{Q}_{X}: d \mapsto \operatorname{Im}\left(\eta_{X} \Lambda, d\right)
$$

be the function taking $d$ to the diagram of images obtained from $d$ under the cocone $\eta_{X} \Lambda$. Then for each such $d$, the colimit of $\mathscr{Q}_{X}(d)$ is $\mathscr{L} X$.

Proof. By Lemma 2.18 and the fact that $\eta_{X} \circ \Lambda_{i}=\mathscr{L} \Lambda_{i} \circ \eta_{X_{i}}$ we have $\mathscr{Q}_{X}(d)(i) \cong \operatorname{Im} \mathscr{L} \Lambda_{i}$. Now we may apply Lemma 4.14 to the diagrams $\mathscr{Q}_{X}(d)$ and $\mathscr{L} X_{i}$, and this gives us that that $\operatorname{colim} \mathscr{Q}_{X}(d) \cong \operatorname{colim}_{i} \mathscr{L} X_{i}$. Since $\mathscr{L}$ preserves monic pushouts, we have that $\operatorname{colim}_{i} \mathscr{L} X_{i}=\mathscr{L} X$, as desired.

## Qed.

4.16. Lemma. The functions in Lemma 4.15 assemble into a lax natural transformation
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-23.jpg?height=153&width=347&top_left_y=715&top_left_x=889)

Proof. See Appendix B.
Qed.
4.17. For any morphism $f: X \rightarrow Y$, Lemma B. 2 and Lemma 4.16 establish the following pair of composable functors: $\mathscr{M} \mathscr{L} X \stackrel{\mathscr{Q}_{X}}{\longleftarrow} \mathscr{M} X \stackrel{\mathscr{M} f}{\leftrightarrows} \mathscr{M} Y$. To recall and clarify how these functors operate, it is useful to consider their action on any fixed $d \in \mathscr{M} Y$ (i.e. for any diagram $d: \mathrm{J} \rightarrow \mathrm{C}$ with colimit $Y$ ). To that end, consider the following diagram which shows how one constructs $\mathscr{M}(f)(d)$ (resp. $\left(\mathscr{Q}_{X} \circ \mathscr{M}(f)\right)(d)$ ) by pointwise pullbacks (resp. pointwise image factorizations).
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-23.jpg?height=413&width=897&top_left_y=1332&top_left_x=612)

These constructions yield two families of morphisms. The first is the family

$$
\left(\mathscr{M}(f)(d)(j) \xrightarrow{f_{i}^{\#}} d(j)\right)_{j \in \mathrm{~J}},
$$

while the second is the family

$$
\left(\mathscr{M}(f)(d)(j) \xrightarrow{\mathrm{mi}\left(\eta_{X} \Lambda_{i}^{\#}\right)}\left(\mathscr{Q}_{X} \circ \mathscr{M}(f)\right)(d)(j)\right)_{j \in \mathrm{~J}} .
$$

Viewed as morphisms in $\mathrm{C}^{\mathrm{J}}$, these assemble into the following span:

$$
\left(\mathscr{Q}_{X} \circ \mathscr{M}(f)\right)(d) \longleftarrow \mathscr{M}(f)(d) \longrightarrow d .
$$

The following result shows that the pushout of this span is precisely the diagram we have been seeking to construct.
4.18. Proposition. Let $(\mathscr{L}, \eta)$ be a strong lasso on a mono-strong category C with all colimits. Suppose $f: X \hookrightarrow Y$ is a monomorphism in C and that $d \in \mathscr{M} Y$ is a monic diagram of shape J whose colimit is $Y$. Then, working in $\mathrm{C}^{\mathrm{J}}$, where pushouts are computed pointwise, the pushout of the span of Equation (2) is a diagram with colimit $Y_{/ f}$.
Proof. Colimits commute with each other, thus we have that:

$$
\begin{aligned}
\operatorname{colim} & \left(\left(\mathscr{Q}_{X} \circ \mathscr{M}(f)\right)(d)+\mathscr{M}(f)(d) d\right)= \\
& =\operatorname{colim}\left(\left(\mathscr{Q}_{X} \circ \mathscr{M}(f)\right)(d)\right)+\operatorname{colim} \mathscr{M}(f)(d) \operatorname{colim} d \\
& =\mathscr{L} X+\operatorname{colim} \mathscr{M}(f)(d) \operatorname{colim} d \\
& =\mathscr{L} X+{ }_{X} \operatorname{colim} d \\
& =\mathscr{L} X+{ }_{X} Y \\
& =Y_{/ f}
\end{aligned}
$$

## Qed.

4.19. We can actually prove a stronger result than Proposition 4.18. Indeed, we can forgo the assumption that the category C has all colimits. For the proof of this result, we have to manually show that our construction satisfies the definition of a colimit.
4.20. Theorem (Upgrade of Proposition 4.18). Let $(\mathscr{L}, \eta)$ be a strong lasso on a monostrong category C. Suppose $f: X \hookrightarrow Y$ is a monomorphism in C and that $d \in \mathscr{M} Y$ is a monic diagram whose colimit is $Y$. Then the span Equation (2) has $Y_{/ f}$ as its colimit.
Proof. We abbreviate the diagram $\mathscr{M}(f)(d)$ by $x$ and the diagram $\left(\mathscr{Q}_{x} \circ \mathscr{M}(f)\right)(d)$ by $q$. Denote by $h: \mathrm{J} \rightarrow \mathrm{C}$ the diagram obtained via the following pointwise pushout.
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-24.jpg?height=163&width=609&top_left_y=1619&top_left_x=751)

By Lemmas B. 2 and 4.13, we have that the colimits of $d, x$ and $q$ are $Y, X$ and $\mathscr{L} X$, respectively. Observe that $Y_{/ f}$ forms the apex of a cocone over the pushout diagram defining $h$. Hence there exists a unique map $\Omega_{i}: h(i) \rightarrow Y_{/ f}$ making the following commute.
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-24.jpg?height=415&width=579&top_left_y=1972&top_left_x=773)

We are required to show that $(h, \Omega)$ form a colimit cocone with apex $Y_{/ f}$. To this end, suppose that $\Sigma$ is a cocone over $h$ with some apex $Z$. Observe that by composing $\Sigma$ with the collections of maps ( $u_{i}$ ) and ( $v_{i}$ ) in turn, we obtain cocones over $q$ and $d$, both having apex $Z$. Since $Y$ and $\mathscr{L} X$ are the colimits of $d$ and $q$, respectively, we obtain unique maps $s$ and $t$ making the following commute.
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-25.jpg?height=452&width=714&top_left_y=646&top_left_x=704)

Since $Y_{/ f}$ is a pushout of $\mathscr{L} X$ and $Y$ over $X$, we obtain a unique morphism from $Y_{/ f}$ to $Z$, commuting with the above, as required.
Qed.
4.21. Theorem 4.20 implies that one can start with any diagram $d$ with colimit $Y$ and, so long as $d$ is a diagram of monomorphisms, then one can produce a diagram whose colimit is the $(\mathscr{L}, \eta)$-contraction $Y_{/ f}$ of $Y$ along a monomorphism $f: X \hookrightarrow Y$. This is very close to being the result we have been working towards throughout this section; however, what it is missing is any guarantee that the diagram constructed in Theorem 4.20 is itself a diagram of monomorphisms. Fortunately, this can be fixed by taking pointwise image factorizations of its colimit cocone as the following corollary points out.
4.22. Corollary. Let C be a mono-strong category with colimits. Suppose $f: X \hookrightarrow Y$ is a monomorphism in C and that $d \in \mathscr{M} Y$ is a monic diagram whose colimit is $Y$. Then the diagram of images obtained from the colimit cocone sitting above $\left(\mathscr{Q}_{X} \circ \mathscr{M}(f)\right)(d)+\mathscr{M}(f)(d) d$ has $Y_{/ f}$ as its colimit.

Proof. Combine Lemma 4.14 and Theorem 4.20.
Qed.
4.23. Finally, we prove that our construction is equivalent to the simpler one given in Theorem 4.9.
4.24. Proof of Theorem 4.9. We will show that $d_{/ f}$ is identical to the diagram obtained in Corollary 4.22. Recall Diagram 3. Since pushouts preserve epimorphisms, we have that the maps $u_{i}: d(i) \rightarrow h(i)$ are epic. Hence by Lemma 2.18 the images of $\Omega_{i}$ and $\Omega_{i} u_{i}=\eta_{X}^{\sharp} \Lambda_{i}$ coincide for each $i \in \mathrm{~J}$. Since this is how both diagrams are defined, this completes our
proof.

## Qed.

4.25. Proof of Theorem 1.21. One can readily verify that the constructions in Lemma B. 2 and Lemma 4.16 yield diagrams of the same shape as the diagram $d$ one starts with. In particular, this means that all of the results above can be specialized to the case in which one only seeks to construct objects via diagrams whose shape is limited to a special class (for example, trees). Furthermore, observe that both Lemma B. 2 and Lemma 4.16 preserve diagrams of monomorphisms (i.e. they send a diagram $d$ whose arrows are all monic to a new diagram whose arrows are also all monic). These two facts imply that all of the results above can be specialized to the case in which $d$ is a structured decomposition of some given shape (for example, a tree decomposition of graphs).
All of this implies that, if instead of considering diagrams of any shape one only cares about structured decompositions, then all the results of this section can actually be stated for lassos which are not strong (namely lassos which preserve pushouts of monomorphisms, but not colimits in general, cf. Definitions 1.14 and 4.3).
Qed.
4.26. Remark. As in Section 3, we could investigate categories of strong lassos. By Lemma 3.7 and the surrounding results, we see that all the lassos on Grph are strong. However in Appendix A we show that this is not always the case. In particular, see Example A. 11 for a strictly weak lasso.
4.27. Remark. In the statement of Theorem 4.9, we assume that the morphism $f: X \hookrightarrow Y$ is monic. However we don't use this fact anywhere in the proof. This suggests that we could define contractions differently, and allow for contractions along any morphism. However, it is easy to check that in Grph a contraction defined in this way is always equivalent to a contraction defined along a monomorphism. Indeed, this is because given any map $f: X \rightarrow Y$, the connected components of $X$ are exactly the preimages of the connected components of $Y$ which have nonempty preimage. Hence the contraction along im $f$ is isomorphic to the contraction along $f$. It is perhaps an interesting question to ask whether this holds in general in mono-strong categories, or not.

## 5 Discussion \& Open Problems

5.1. Here we introduce the notion of a lasso. This machinery allows us to systematically identify classes of epimorphisms - called lasso contractions - in a category C along which one can push decompositions in a meaningful way. In more detail, lasso contractions have the property that, given any epimorphism $f: X \rightarrow Y$ and any tree-shaped structured decomposition $d_{X}$ of $X$, if $f$ arises as a lasso contraction, then one can obtain a decomposition $d_{Y}$ such that: (1) $d_{Y}$ is a decomposition with the same shape as $d_{X}$ and (2) $d_{Y}$ is a decomposition of $Y$.
5.2. Instantiating our results in the category Grph of directed multigraphs, the above results can be used to answer the following question: for which classes of surjective homomorphisms $f: H \rightarrow G$ can one always push a tree decomposition for $H$ along $f$ to obtain a tree decomposition for $G$ of the same shape? In Grph, as it turns out, contraction maps are the only class of epimorphisms along which one can push decompositions while leaving their shape unchanged. Thus, in this particular instance, our general machinery yields a canonicity result which characterizes contraction maps.
5.3. Not only is our category theoretic approach ideal for proving canonicity results, ${ }^{9}$ but it also enables out proof techniques to be adapted to wide range of mathematical objects all at once. For example our results apply in any mono-strong category such as directed multigraphs, hypergraphs, Petri nets, circular port graphs, half-edge graphs, databases, simplicial sets or indeed any (co)presheaf category.
5.4. Interestingly, although we can prove the above canonicity result for graph contractions, if one moves away from the category Grph of directed multigraphs to other more embellished categories of categorical data, a much richer story begins to appear. For instance, already in the category of reflexive graphs one finds that there are many more kinds of lassos, each one defining a different class of epimorphisms along which (tree) decompositions can be pushed forward. Moreover, as we continue to add attributes to the combinatorial object under study, we observe that the corresponding categories of lassos appear to become more and more involved. This suggests that there should be a relationship between the defining schema of the combinatorial data and the resulting category of lassos. Understanding this relationship would be particularly useful in studying lassos on much more complicated categories of copresheaves than the one studied here. Thus we state the following conjecture.
5.5. Conjecture. There is a contravariant functor Lasso: Cat → Cat which takes any functor $F: \mathrm{S} \rightarrow \mathrm{T}$ between schemata S and T to a functor $\operatorname{Lasso}\left(\mathrm{Set}^{\top}\right) \rightarrow \operatorname{Lasso}\left(\mathrm{Set}^{\mathrm{S}}\right)$ between the categories of lassos on the associated copresheaf categories.
5.6. A further open problem, possibly a more challenging one, is to determine whether pushing decompositions along morphisms is a functorial operation. Slightly more formally, one would like an analogue of Theorem B. 2 (or Corollary 4.12) for contractions; namely a covariant functor which assigns to each object of a category the set of all of its decompositions and which acts functorially on lasso contractions. Obviously there is significant impediment to such a result: we do not know whether, given a lasso $(\mathscr{L}, \eta)$ on a category C , it is even possible to construct a category $\mathrm{C}_{(\mathscr{L}, \eta)}$ whose objects are those of C but whose morphisms are only those epimorphisms in C which arise as $(\mathscr{L}, \eta)$-contractions. The technical hurdle one needs to overcome is that of proving that lasso-contractions can be

[^8]composed. Indeed, although the special case of graphs is very easy ${ }^{10}$, the general question of determining whether the composite of two $(\mathscr{L}, \eta)$-contractions is itself a $(\mathscr{L}, \eta)$-contraction has resisted our efforts thus far. We state this as the following conjecture.
5.7. Conjecture. Let $(\mathscr{L}, \eta)$ be a lasso on a category C. Consider any two monomorphisms $f_{1}: X_{1} \hookrightarrow Y$ and $f_{2}: X_{2} \rightarrow Y_{/ f}$ as in the following diagram.
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-28.jpg?height=205&width=979&top_left_y=691&top_left_x=571)

Then there is a subobject $f: X \hookrightarrow Y$ whose lasso contraction
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-28.jpg?height=192&width=596&top_left_y=1005&top_left_x=764)
satisfies $Y_{/ f}=\left(Y_{/ f_{1}}\right)_{/ f_{2}}$ and $\eta_{X}^{\#}=\eta_{X_{2}}^{\#} \eta_{X_{1}}^{\#}$.

Acknowledgments: we wish to thank Kevin Carlson for feedback and suggestions on a preliminary version of this article.

## A The category of lassos on reflexive graphs

A.1. Many of the proofs for Grph adapt to the category RGrph. Indeed, the connected components lasso ( $\mathrm{cc}, \pi$ ) restricts to a lasso on RGrph, which we will also denote by ( $\mathrm{cc}, \pi$ ). However, not all of the proofs transfer. In particular, Lemma 3.11 relies on the existence of graphs without loops and so it fails, along with its consequences, namely Lemma 3.13 and Corollary 3.14. We prove the following alternatives.
A.2. Lemma. Let $(\mathscr{F}, \alpha)$ be a lasso. Suppose that the components of $\alpha$ are vertex-trivial. If for some graph $G$, we have that $\alpha_{G}$ identifies some pair of parallel non-loop edges in $G$, then $\alpha$ identifies all pairs of parallel edges in all graphs (including pairs of parallel loops).

Proof. Suppose there is a graph $G$ containing a pair of parallel non-loop edges $e$ and $e^{\prime}$ such that $e$ and $e^{\prime}$ are identified under $\alpha_{G}: G \rightarrow \mathscr{F}(G)$. Denote by $\mathscr{O}^{\mathscr{P}}$ the graph with two vertices, a loop at each vertex and a pair of parallel edges spanning the vertices and denote by the graph obtained from by adding a new edge in the opposite direction to the parallel edges. Observe that there exists a homomorphism $f: G \rightarrow$ so that $f(e)$ and $f\left(e^{\prime}\right)$ are exactly the pair of parallel edges of Then by the naturality of $\alpha$, the fact that $\alpha$ is the identity on

[^9]vertex sets and the fact that $\alpha$ is epic, we have that: $1 . \mathscr{F}$ is the identity on discrete reflexive graphs; 2. $\mathscr{F}$ preserves the single edge graph (i.e. $\mathscr{F}\left(\sigma^{\infty}\right)=\sigma^{\infty}$ ); and 3. $\mathscr{F}\left(\sigma^{\mathscr{P}}\right)$ is the graph having two vertices, with loops, and one edge in each direction between them. Consider the fact that is the monic pushout of and $\mathscr{P}$. Since $\mathscr{F}$ preserves monic pushouts we get that $\mathscr{F}(\mathrm{O})$ is isomorphic to of.
Let $H$ be an arbitrary graph and suppose that there is a pair $e, e^{\prime}$ of parallel edges (possibly loops) in $H$. Consider the homomorphism $h$ : → $H$ that sends one parallel edge to $e$ and the other to $e^{\prime}$. Now by the naturality of $\alpha$ and our analysis above, we get that $\alpha_{H}$ identifies the edges $e$ and $e^{\prime}$. Since $H$ and the choice of parallel edges were arbitrary, this completes our proof.

## Qed.

A.3. Proposition. Let smooth be the map RGrph → RGrph that sends each graph $G= (V, E)$ to a graph smooth $(G)$ with vertex set $V$ and edge set obtained from $E$ by identifying parallel edges (including parallel loops). Then the map smooth extends uniquely to a functor smooth: RGrph → RGrph such that there is a natural transformation id ${ }_{\text {RGrph }} \Rightarrow$ smooth.

Proof. Let $f: G \rightarrow H$ be a graph homomorphism. We first claim that there is a unique homomorphism $\operatorname{smooth}(f)$ from $\operatorname{smooth}(G)$ to $\operatorname{smooth}(H)$ that acts identically to $f$ on vertices. Indeed, consider the reflexive closure of the relation of edges being parallel. This relation is preserved by graph homomorphism and so such a homomorphism as smooth $(f)$ exists. It is unique since smooth $(G)$ and $\operatorname{smooth}(H)$ have no pairs of parallel edges. Hence it remains to show that any functor extending the map smooth is the identity on the vertex-map of homomorphisms.
Let $\eta$ be a natural transformation from id $_{\text {RGrph }}$ to smooth. Clearly $\eta$ must be vertex-trivial. Hence by naturality we have our required property.
Qed.
A.4. We call the functor defined by the above proposition the smoothing functor.
A.5. Lemma. The smoothing functor does not preserve monic pushouts in RGrph.

Proof. One finds a counterexample by considering the following monic pushout
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-29.jpg?height=166&width=817&top_left_y=1899&top_left_x=655)
which is not preserved under the action of the smoothing functor.
Qed.
A.6. Lemma. Let $\mathscr{F}$ be a functor RGrph to RGrph along with a natural transformation $\alpha: \mathrm{id}_{\mathrm{RGrph}} \Rightarrow \mathscr{F}$ whose components are epimorphisms. If some component of $\alpha$ is not
edge-trivial, then for each reflexive graph $G$, the map $\alpha_{G}$ identifies every class of parallel loops in $G$.

Proof. Analogously to Lemma 3.10, one finds that $\mathscr{L}$ must map the graph \&, with one vertex and two loops, to the terminal graph. Now consider an arbitrary reflexive graph $G$. Suppose that $G$ contains a vertex $x$ with two loops $e$ and $e^{\prime}$. Then there is a morphism $f: \delta \rightarrow G$ mapping the unique vertex of $\delta$ to $x$ and sending the two loops of $\delta$ to each of $e$ and $e^{\prime}$. By naturality, we must have that $e$ and $e^{\prime}$ are identified by $\eta_{G}$. This completes the proof.
Qed.
A.7. Proposition. Let deloop be the map RGrph → RGrph that sends each graph $G= (V, E)$ to a graph deloop $(G)$ with vertex set $V$ and edge set obtained from $E$ by identifying loops which have the same endvertex. Then the map deloop extends uniquely to a functor deloop: RGrph → RGrph such that there is a natural transformation id ${ }_{\text {RGrph }} \Rightarrow$ deloop.

Proof. By similar arguments to the proof of Proposition A.3, we obtain our functor. This functor sends each graph homomorphism $f: G \rightarrow H$ to a homomorphism from deloop $(G)$ to deloop $(H)$ that acts identically to $f$ on vertex sets, and on edges in the obvious way.
Qed.
A.8. We call the functor defined in the above proposition the delooping functor.
A.9. Lemma. The delooping functor preserves monic pushouts in RGrph.

Proof. Consider an arbitrary monic span $A \hookleftarrow C \hookrightarrow B$ in RGrph and denote by $G$ its pushout. Since $\delta$ is vertex-trivial, it is sufficient to prove that, if none of the graphs $A, B$ or $C$ possess parallel loops, then their pushout $G$ does not. So let $u$ be a vertex in $G$. Suppose first that $u$ is not in the image of $C$. Then $u$ has exactly one loop, since its preimage (which is a singleton since the morphisms are monic) in either $A$ or $B$ also has exactly one loop. Instead suppose that $u$ is in the image of $C$. Then there is a loop at each preimage of $u$ in both $A$ and $B$. However, both of these loops are the image of a single loop in $C$. In this case, $u$ also has exactly one loop. This completes our proof.
Qed.
A.10. By the above analysis, the delooping functor gives us a lasso on RGrph which we denote by (deloop, $\boldsymbol{\delta}$ ).
A.11. Example. Although the delooping functor preserves monic pushouts, it does not preserve all monic colimits. In particular, it doesn't preserve all coequalisers. Indeed, consider the diagram $a, b: \diamond$ ↪ where ∘ is the terminal graph, o is the reflexive graph on two vertices with a single edge between them and $a$ and $b$ are the two possible homomorphisms ஒ ↪ . Now observe that the colimit of this diagram is the graph with one vertex and three distinct loops.
A.12. Lemma. Let $(\mathscr{L}, \eta)$ be a nontrivial lasso on RGrph and suppose that it is vertextrivial. Then $(\mathscr{L}, \eta)$ is the delooping lasso (deloop, $\delta$ ).

Proof. Since $(\mathscr{L}, \eta)$ is nontrivial, but vertex-trivial, there is a graph $G$ so that $\eta_{G}$ identifies some pair of parallel edges in $G$. If such a pair of edges are not loops, then by Lemma A. 2 the functor $\mathscr{L}$ has to be the smoothing functor. However, by Lemma A.5, this can't be the case. Hence, no pair of non-loop parallel edges may be identified. So the identified edges must be a pair of parallel loops and by Lemma A.6, we conclude that $\mathscr{L}$ is the delooping functor.
Qed.
A.13. One may prove an analogue of Lemma 3.16 for RGrph (q.v. (A.15)), which states that any non-vertex-trivial lasso on RGrph must act like the connected components lasso on vertices. We formalise this in the following definition. It then remains to deduce the possibilities for how such a lasso can act on edges.
A.14. Definition. We say that a lasso $(\mathscr{L}, \eta)$ on RGrph is component-collapsing if, for all graphs $G$ in RGrph, the graph $\mathscr{L}(G)$ has the same vertex set as the graph $\mathrm{cc}(G)$ and the vertex map of the homomorphism $\eta_{G}: G \rightarrow \mathscr{L}(G)$ is identical to the vertex map of the homomorphism $\pi_{G}: G \rightarrow \mathrm{cc}(G)$. That is, the lasso acts like the connected components lasso ( $\mathrm{cc}, \pi$ ) on the vertex sets of graphs. Observe that ( $\mathrm{cc}, \pi$ ) is initial in the subcategory of component-collapsing lassos.
A.15. Corollary. Let $(\mathscr{L}, \eta)$ be a lasso on RGrph. If $(\mathscr{L}, \eta)$ is not vertex-trivial, then it is component-collapsing.

Proof. The proof is analogous to the proof of Lemma 3.16.
Qed.
A.16. Proposition. There is a component-collapsing lasso (source, $\sigma$ ) so that for each graph $G$, the map $\sigma_{G}$ identifies exactly the edges having $u$ as a source, for each vertex $u$ in $G$.

Proof. For each reflexive graph $G$, let source $(G)$ be the graph obtained from $\operatorname{cc}(G)$ by identifying edges sharing a source in $G$. It is easy to see that this assembles into a functor and that the maps $\sigma_{G}$ form a natural transformation $\sigma: \mathrm{id}_{\mathrm{RGrph}} \Rightarrow$ source. Now consider an arbitrary monic span $A \hookleftarrow C \hookrightarrow B$ in RGrph and denote by $G$ its pushout. We are required to show that quotienting edges by the relation of sharing a source commutes with monic pushouts, which in turn consist of a disjoint union and then a quotient by the relation on edges given by the span. Let $a$ and $b$ be edges in the disjoint union of $A$ and $B$. Our required outcome is clear when $a$ and $b$ both lie in one of the graphs so we assume, without loss of generality, that $a$ is an edge of $A$ and $b$ is an edge of $B$. Now observe that if there is some $c$ in $C$ so that $a$ and $b$ are the images of $c$ in $A$ and $B$, respectively, then the naturality of $\gamma$ implies that the edges $\gamma_{A}(a)$ and $\gamma_{B}(b)$ are related in the span source $(A) \hookleftarrow \operatorname{source}(C) \hookrightarrow \operatorname{source}(B)$ by $\gamma_{C}(c)$. Now assume that $a$ and $b$ are not related by the span. Then they do not share a
source in $G$ and do not share a source in $\operatorname{source}(A)+\operatorname{source}(B)$. This completes our proof.
Qed.
A.17. We call the lasso (source, $\sigma$ ) defined in the above the source lasso.
A.18. Proposition. There is a component-collapsing lasso (target, $\tau$ ) so that for each graph $G$, the map $\tau_{G}$ identifies exactly the edges having $u$ as a target, for each vertex $u$ in $G$.

Proof. The proof is exactly analogous to the proof of Proposition A.16.
Qed.
A.19. We call the lasso (target, $\tau$ ) defined in the above the target lasso.
A.20. Proposition. There is a component-collapsing lasso (gather, $\gamma$ ) so that for each graph $G$, the map $\gamma_{G}$ identifies exactly the edges of $G$ which are loops in $c$, for each connected component $c$ of $G$.

Proof. For each reflexive graph $G$, let gather $(G)$ be the graph obtained from $\operatorname{cc}(G)$ by identifying the loops of $G$ in $c$, for each connected component $c$ of $G$. It is easy to see that we can extend gather to a functor gather: RGrph → RGrph and that the maps $\gamma_{G}$ form a natural transformation $\gamma$ : id $_{\text {RGrph }} \rightarrow$ gather.
Now consider an arbitrary monic span $A \hookleftarrow C \hookrightarrow B$ in RGrph and denote by $G$ its pushout. We are required to show that quotienting edges by the relation of being loops in the same connected component commutes with monic pushouts. This is clear, since $\gamma_{G}$ preserves connected components for each $G$ and also preserves the property of being a loop.
Qed.
A.21. We call the lasso (gather, $\gamma$ ) defined in the above the gathering lasso. Along with the source and target lassos, we shall see that we have finally exhausted the space of lassos on RGrph.
A.22. Lemma. Let $(\mathscr{L}, \eta)$ be a component-collapsing lasso. Suppose that some component of $\eta$ identifies a pair of parallel non-loop edges. Then some component of $\eta$ must identify a pair of non-parallel edges.

Proof. Let $G$ be a graph so that $\eta_{G}$ identifies a pair $e, e^{\prime}$ of parallel edges in $G$. Then analogously to in the proof of Lemma A.2, we get that all parallel classes of edges in all graphs are identified to single edges by $\eta$. Suppose for a contradiction that no component of $\eta$ identifies edges which are not in parallel. Consider the reflexive graph consisting of a pair of vertices, spanning which is a pair of parallel edges and a single other non-loop edge in the opposing direction. Then we may express as a monic pushout over graphs having no parallel edges as in the following illustration.
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-33.jpg?height=194&width=1089&top_left_y=380&top_left_x=519)

However we observe that the colimit of the image of this diagram under $\mathscr{L}$ does not have the original parallel edges identified. Hence $\mathscr{L}$ does not preserve monic pushouts, a contradiction.
Qed.
A.23. Lemma. Let $G$ be a reflexive graph and $e$ and $e^{\prime}$ distinct edges in $G$ which are not parallel but lie in the same connected component. Let denote the reflexive graph having two vertices and an edge in each direction between them. Let of denote the reflexive graph having two vertices and just one edge between them. Then there is an epimorphism $f$ from $G$ to either of of so that one of the following holds:
(1) the edges $f(e)$ and $f\left(e^{\prime}\right)$ are distinct loops; or
(2) the edges $f(e)$ and $f\left(e^{\prime}\right)$ are a loop and a non-loop, respectively, or vice versa.

Proof. First suppose that $e$ and $e^{\prime}$ are both loops and denote by $u$ and $u^{\prime}$ the vertices which they are attached to. Let $T$ be a spanning tree in $G$ and let $d$ be an edge that separates $u$ and $u^{\prime}$ in $T$. Now identify all of the vertices in each of the two components of $T-d$. The resulting graph has two vertices and from this we can easily obtain our function $f$ satisfying (1). In the case where one of $e$ is a loop and the other is a non-loop, we perform the same operation where $d$ is the non-loop edge and $T$ is an arbitrary spanning tree containing $d$. This gives us outcome (2). Finally, in the case where $e$ and $e^{\prime}$ are both non-loops, we choose one of these edges arbitrarily to be $d$ and the spanning tree $T$ so that it contains this chosen edge. In this case, we also have outcome (2).
Qed.
A.24. Lemma. Let $(\mathscr{L}, \eta)$ be a component-collapsing lasso. If $(\mathscr{L}, \eta)$ is not edge-trivial, then either it is:

1. the lasso $(\mathrm{cc}, \pi) \circ($ deloop, $\boldsymbol{\delta})$;
2. one of the lassos (source, $\sigma$ ), (target, $\tau$ ), (gather, $\gamma$ ); or
3. the lasso (deloop, $\boldsymbol{\delta}$ ) $\circ(\mathrm{cc}, \boldsymbol{\pi})$, which is the terminal lasso on RGrph.

Proof. We first observe that, by Lemma A.6, the components of $\eta$ identify all classes of parallel loops. If this is the only edge-identification which is performed, then $(\mathscr{L}, \eta)$ is the lasso $(\mathrm{cc}, \pi) \circ($ deloop, $\boldsymbol{\delta})$.
Now suppose that, in addition to this identification, there is some graph $G$ so that $\eta_{G}$ identifies a pair of edges $e, e^{\prime}$ which are not a pair of parallel loops. By Lemma A.22, we may assume that $e$ and $e^{\prime}$ are not parallel.

Let $f$ be the graph homomorphism given by Lemma A. 23 and split into cases based on the outcomes (1) and (2).
Case 1. First suppose that the codomain of $f$ is the graph . That is, $f$ is a homomorphism from $G$ to $\sigma^{\infty}$ so that $e$ and $e^{\prime}$ are mapped to distinct loops. Then since $\eta_{G}$ identifies $e$ and $e^{\prime}$ and by the naturality of $\eta$, we must have that $\eta_{\infty}$ identifies the two loops of . Now given any reflexive graph $H$, one may inject o into $H$ to show that any two loops either end of an edge are identified under $\eta_{H}$. By extension, any two loops in the same connected component in $H$ are identified by $\eta_{H}$. We claim that the same outcome holds in the case that the codomain of $f$ is the graph and andeed, since and be expressed as the monic pushout of two copies of over the discrete reflexive graph $\odot^{\circ}$ on two vertices, the preservation of monic pushouts implies that $\eta_{\text {of }}$ identifies the loops of . We conclude this case by noting the following: if the identification of loops in the same connected component is the only additional identification of edges on top of identifying parallel loops, then we get that $(\mathscr{L}, \eta)$ is the gathering lasso (gather, $\gamma$ ).
Case 2. First suppose that the codomain of $f$ is the graph of. So $f$ is a homomorphism from $G$ to so that $e$ and $e^{\prime}$ are mapped to one loop and one non-loop. Then since $\eta_{G}$ identifies $e$ and $e^{\prime}$ and by the naturality of $\eta$, we must have that $\eta_{\circlearrowleft}$ o identifies a loop with a non-loop from . There are two subcases. Either the non-loop is identified with the loop at its source or identified with the loop at its target. Now given any reflexive graph $H$, one may inject o into $H$ to show that any edges sharing a source (resp. a target) are identified under $\eta_{H}$. In the case where the codomain of $f$ is , we proceed analogously to in Case 1 and obtain the same conclusion. That is, the components of $\eta$ identify all edges sharing a source or identify all edges sharing a target. If these are the only identifications on top of identifying parallel loops, then $(\mathscr{L}, \eta)$ is either (source, $\sigma$ ) or (target, $\tau$ ).
The conclusion of the proof comes from the following observation: out of the three relations we obtain as outcomes of Cases 1 and 2, if $\gamma$ identifies via more than one of them, then $(\mathscr{L}, \eta)$ is the terminal lasso. That is, the lasso which identifies all edges belonging to the same connected component.
Qed.
A.25. The above lemma completes our analysis of the category of lassos on the category RGrph of reflexive graphs, giving us Figure 6 from Section 3.

## B Proof of Lemma 4.16

B.1. We begin by first recalling background results due to [2].
B.2. Lemma (Lemma 2.5.13 in [2]). Suppose that $\mathscr{I}$ is a class of all (small) monic diagrams and $C$ is a category with pullbacks and pullback-stable colimits of type $\mathscr{I}$. By choosing representatives for every pullback, one obtains a well-defined presheaf

MDgm : $\mathrm{C}^{\mathrm{OP}} \rightarrow$ Set,
where for $X \in \mathrm{C}, \operatorname{MDgm}(X)$ is the set of diagrams $d: I \rightarrow \mathrm{C}$ in $\mathscr{I}$ equipped with a colimit cocone $\sigma: d \Rightarrow \Delta(X)$. Given a map $f: X \rightarrow Y$ in $\mathrm{C}, \operatorname{MDgm}(f)$ is the function that takes a colimit cocone $\sigma$ over $Y$ to its pullback $f^{*}(\sigma)$ over $X$.
B.3. It turns out we can promote the functor MDgm of the above lemma to a functor into Cat (the category of small categories) as shown in the following corollary. The proof of Corollary 4.12 is straightforward and mechanical, but, since it is more categorically involved than the rest of the document, we defer it to Appendix B in order to not distract from the main points.
B.4. Corollary (Corollary 4.12 restated). The functor MDgm : C ${ }^{\text {op }} \rightarrow$ Set in Lemma B. 2 extends to a functor $\mathscr{M}: \mathrm{C}^{\mathrm{op}} \rightarrow \mathbf{C a t}$.

Proof of Corollary 4.12. For each $X \in \mathrm{C}$, define $\mathscr{M}(X)$ be the category of structured decompositions which yield $X$ as a colimit. For each $f: X \rightarrow Y$ in C , we are required to define a functor $\mathscr{M}(f): \mathscr{M}(X) \rightarrow \mathscr{M}(Y)$. On objects, the action of this functor is analogous to $\operatorname{MDgm}(f)$. That is,

$$
\mathscr{M}(f):\left(d_{Y} \in \mathscr{M}(Y)\right) \mapsto\left(d_{X} \in \mathscr{M}(X)\right) .
$$

where $d_{X}$ is obtained from $d_{Y}$ by pointwise pullbacks along $f$. Finally, given a map $(F, \eta): d_{Y} \rightarrow d_{Y}^{\prime}$ between structured decompositions which have colimit $Y$, we define the action of $\mathscr{M}(f)$ on $(F, \eta)$ to be given by the collection of unique pullback arrows $\varphi_{i}$ making the following commute.
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-35.jpg?height=329&width=953&top_left_y=1435&top_left_x=584)

Since $d_{X}$ has the same shape as $d_{Y}$, and $d_{X}^{\prime}$ the same shape as $d_{Y}^{\prime}$, this properly defines a morphism of decompositions of the form $(F, \varphi)$ where the $i$-th component to $\varphi$ is $\varphi_{i}$ as in the diagram above. Thus this defines the action of $\mathscr{M}$ on morphisms since one then has $\mathscr{M}(f)(F, \eta):=(F, \varphi)$. This assignment is functorial since identities are preserved and, by the universal property of the morphisms $\varphi_{i}$, composition is respected.
Qed.
B.5. Lemma (Lemma 4.16 restated). The functions in Lemma 4.15 assemble into a lax natural transformation
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-35.jpg?height=154&width=347&top_left_y=2208&top_left_x=889)

Proof of Lemma 4.16. Recall that the function

$$
\mathscr{Q}_{X}: \mathscr{M} X \rightarrow \mathscr{M} \mathscr{L} X,
$$

acts by sending a diagram $d: \mathrm{J} \rightarrow \mathrm{C}$ with colimit colone ( $\Lambda, X$ ) to the diagram of images under $\eta_{X} \Lambda$. By Lemma 4.15, the action of $\mathscr{Q}_{X}: \mathscr{M} X \rightarrow \mathscr{M} \mathscr{L} X$ on any object $d \in \mathscr{M} X$ is indeed a diagram whose colimit is $\mathscr{L} X$.
Having given the action of $\mathscr{Q}_{X}$ on objects, we will turn it into a functor by defining its action on morphisms. This will follow immediately by the universal property of images. To that end, consider the following morphism of diagrams $d \rightarrow d^{\prime}$ in $\mathscr{M} X$ :

$$
(F, \alpha):(\mathrm{J} \xrightarrow{d} \mathrm{C}) \rightarrow\left(\mathrm{J}^{\prime} \xrightarrow{d^{\prime}} \mathrm{C}\right) .
$$

For any $i \in \mathrm{~J}$, this yields the following diagram where one deduces the existence of the monomorphism $q_{i}$ by the universal property of images (and that it is a monomorphism by Paragraph 2.17).
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-36.jpg?height=594&width=953&top_left_y=1121&top_left_x=584)

The morphisms $q_{i}$ assemble into a natural transformation $\beta$ which we will use to define the morphism

$$
\mathscr{Q}_{X}(F, \alpha): \mathscr{Q}_{X}(d) \rightarrow \mathscr{Q}_{x}\left(d^{\prime}\right)
$$

as $\mathscr{Q}_{X}(F, \alpha):=(F, \beta)$. Having defined the action of $\mathscr{Q}_{X}$ on objects and morphisms, it is easy to check functoriality: preservation of identities is immediate and preservation of composition follows by Lemma 4.6.
All that remains is to show that $\mathscr{Q}$ is a lax natural transformation. This amounts to exhibiting a natural transformation $\mathscr{Q}(f)$ as in the following diagram for every morphism $f: X \rightarrow Y$ in C.
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-36.jpg?height=203&width=485&top_left_y=2189&top_left_x=820)

Each component of $\mathscr{Q}(f)$ will be a morphism of diagrams in $\mathscr{M} \mathscr{L} X$. Since neither $\mathscr{M}$ nor $\mathscr{Q}$ change the shapes of any diagram they are applied to, $\mathscr{Q}(f)$ will be a morphism of the following form (where $v$ will be defined below)

$$
(\mathrm{id}, v)_{d}:\left(\mathscr{Q}_{X} \circ \mathscr{M}(f)\right)(d)(i) \rightarrow\left((\mathscr{M} \mathscr{L})(f) \circ \mathscr{Q}_{Y}\right)(d)(i)
$$

Towards establishing the definition of $v$, consider - for $i$ any object of dom $(d)$ - the following diagram.
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-37.jpg?height=455&width=1002&top_left_y=777&top_left_x=556)

The blue morphism $u_{i}$ in the above diagram is deduced by the universal property of images. Using $u_{i}$ and the universal property of pullbacks, one obtains the unique arrow $v_{i}$ shown in red in Diagram 6. Finally, observing that

$$
\begin{aligned}
\left(\mathscr{Q}_{X} \circ \mathscr{M}(f)\right)(d)(i) & =\operatorname{lm}\left(\eta_{X} \ell_{i}\right) \\
\left((\mathscr{M} \mathscr{L})(f) \circ \mathscr{Q}_{Y}\right)(d)(i) & =(\mathscr{L} X) \times_{\mathscr{L} Y} \operatorname{lm} \eta_{Y} \Lambda_{i},
\end{aligned}
$$

one finds that the natural transformation $v$ will have as its $i$-component the unique pullback arrow $v_{i}$ of Diagram 6. Thus, as desired, we have now defined, for any morphism $f: X \rightarrow Y$, the natural transformation $\mathscr{Q}(f)$ whose component at any object $d \in \mathscr{M} Y$ is given by

$$
\mathscr{Q}(f)_{d}:=(\mathrm{id}, v)_{d} \quad(\text { as in Equation } 5) .
$$

All that remains to be shown is that $\mathscr{Q}(f)$ is natural. To that end, take any morphism of diagrams

$$
(F, \mu):\left(\mathrm{J}_{1} \xrightarrow{d_{1}} \mathrm{C}\right) \rightarrow\left(\mathrm{J}_{2} \xrightarrow{d_{2}} \mathrm{C}\right)
$$

in $\mathscr{M} Y$. By two applications of the exactly the same reasoning as in Diagram 6, on obtains the red and blue portions of the following diagram (the red portion corresponds to $d_{2}$ and the
blue portion corresponds to $d_{1}$ ).
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-38.jpg?height=730&width=1369&top_left_y=448&top_left_x=377)

The existence of the pink arrows $q_{1}, q_{2}$ and $q_{3}$ shown in Diagram 7 are deduced as follows: $q_{1}$ and $q_{2}$ follow by the universal property of images while $q_{3}$ follows by the universal property of pullbacks. The proof of naturality of $\mathscr{Q}(f)$ is now complete by observing that:

$$
\begin{aligned}
\left(\mathscr{Q}_{X} \circ \mathscr{M}(f)\right)\left(d_{1}\right)(i) & =\operatorname{lm}\left(\eta_{x} \ell_{1, i}\right) & & \text { and } \\
\left(\mathscr{Q}_{X} \circ \mathscr{M}(f)\right)\left(d_{2}\right)(i) & =\operatorname{lm}\left(\eta_{x} \ell_{2, F i}\right) & & \text { and } \\
\left(\mathscr{Q}_{X} \circ \mathscr{M}(f)\right)(F, \mu) & =q_{1} & & \text { and } \\
\left((\mathscr{M} \mathscr{L})(f) \circ \mathscr{Q}_{Y}\right)\left(d_{1}\right)(i) & =(\mathscr{L} X) \times_{\mathscr{L} Y} \operatorname{lm} \eta_{Y} \Lambda_{1, i} & & \text { and } \\
\left((\mathscr{M} \mathscr{L})(f) \circ \mathscr{Q}_{Y}\right)\left(d_{2}\right)(i) & =(\mathscr{L} X) \times_{\mathscr{L} Y} \operatorname{lm} \eta_{Y} \Lambda_{2, F i} & & \text { and } \\
\left((\mathscr{M} \mathscr{L})(f) \circ \mathscr{Q}_{Y}\right)(F, \mu) & =q_{3} & & \text { and } \\
v_{2, F i} \circ q_{1} & =q_{3} \circ v_{1, i} & &
\end{aligned}
$$

## Qed.

B.6. Consider a strong lasso $(\mathscr{L}, \eta)$ and the functor $\mathscr{M}$ of Corollary 4.12 as shown below.
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-38.jpg?height=149&width=620&top_left_y=2019&top_left_x=751)

From the above, one defines the natural transformation
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-38.jpg?height=151&width=437&top_left_y=2247&top_left_x=846)
via "whiskering". That is, where the component of $\mathscr{M} \circ \boldsymbol{\eta}$ at any object $x$ is simply the action

$$
\mathscr{M}\left(X \xrightarrow{\eta_{x}} \mathscr{L} X\right): \mathscr{M}(\mathscr{L} X) \rightarrow \mathscr{M}(X)
$$

taking diagrams whose colimits are $\mathscr{L} X$ to diagrams whose colimits are $X$. As we saw above, the construction of Paragraph 4.13 yields a lax natural transformation in the opposite direction as shown in Lemmas 4.15 and 4.16. The fact that the natural transformation in question is lax hints at deeper categorical structure which, despite being interesting, we leave as future work.

## C Double Category of Lassos

C.1. Recall the definition of the category of lassos on C from Section 3. We can view maps between lassos as 2-cells as in
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-39.jpg?height=272&width=311&top_left_y=1041&top_left_x=906)
C.2. Furthermore, give four lassos $(\mathscr{L}, \eta),\left(\mathscr{L}^{\prime}, \eta^{\prime}\right),(\mathscr{M}, \mu)$ and $\left(\mathscr{M}^{\prime}, \mu^{\prime}\right)$, along with two maps $(\mathscr{L}, \eta) \xrightarrow{f}\left(\mathscr{L}^{\prime} \eta^{\prime}\right)$ and $(\mathscr{M}, \mu) \xrightarrow{g}\left(\mathscr{M}^{\prime}, \mu^{\prime}\right)$ in the category of lassos, we can define a kind of 'horizontal composition' in the following way. Let $g * f$ be the collection of maps given by the diagonals of the following commutative square.
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-39.jpg?height=246&width=497&top_left_y=1572&top_left_x=812)

In the above context, we make the following proposition.
C.3. Proposition. Given a category C , the category of lassos on C is a double category with a single object.

Proof. Given the following lassos and maps between them (2-cells) in the category of lassos
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-39.jpg?height=265&width=501&top_left_y=2122&top_left_x=812)
we are required to show that vertical and horizontal composition of the 2-cells is associative. Consider the following commutative diagram.
![](https://cdn.mathpix.com/cropped/6d3bae2a-43bd-46ab-9652-5feaf811b1d5-40.jpg?height=533&width=966&top_left_y=509&top_left_x=573)

Composing the two long horizontal and vertical arrows yields $\left(\left(g^{\prime} \circ g\right) *\left(f^{\prime} \circ f\right)\right)_{X}$ and hence $\left(g^{\prime} \circ g\right) *\left(f^{\prime} \circ f\right)=(g * f) \circ\left(g^{\prime} * f^{\prime}\right)$ as required.
Qed.

## References

[1] Jiří Adámek, Horst Herrlich, and George Strecker. Abstract and concrete categories. Wiley-Interscience, 1990. ISBN:9780486469348.
[2] B. M. Bumpus, Z. A. Kocsis, and J. E. Master. Structured Decompositions: Structural and Algorithmic Compositionality. arXiv preprint arXiv:2207.06091, 2022.
[3] Benjamin Merlin Bumpus. Generalizing graph decompositions. PhD thesis, University of Glasgow, 2021.
[4] R. Diestel. Graph theory. Springer, 2010. ISBN:9783642142789.
[5] E Patterson, O Lynch, and J Fairbanks. Categorical Data Structures for Technical Computing. Compositionality, 4, December 2022.
[6] E. Riehl. Category theory in context. Courier Dover Publications, 2017. ISBN:048680903X.
[7] David I. Spivak. Functorial data migration. Information and Computation, 217:31-51, 2012.


[^0]:    *Instituto de Matemática e Estatística, Universidade de São Paulo. Rua do Matão, 1010-05508-090, São Paulo, SP, Brasil.
    ${ }^{\dagger}$ University of Florida, Computer \& Information Science \& Engineering, Florida, USA.
    ${ }^{\ddagger}$ TU Freiberg, Mathematics and Computer Science, Freistaat Sachsen, Deutschland.

    - Authors Bumpus and Fairbanks acknowledge funding from the DARPA ASKEM and Young Faculty Award programs through grants HR00112220038 and W911NF2110323.

[^1]:    ${ }^{1}$ We assume the reader is familiar with the notion of categories, functors and natural transformations. Riehl's textbook [6] is an excellent reference; Bumpus' thesis [3, Section 3.2] provides a very basic introduction which only requires minimal background in graph theory.

[^2]:    ${ }^{2}$ Recall that a surjective graph homomorphism $f: G \rightarrow H$ is a contraction map if the preimage of any vertex in $H$ is a connected subgraph in $G$.

[^3]:    ${ }^{3}$ A graph is reflexive if every vertex has a loop-edge.

[^4]:    ${ }^{4}$ Notice that in the special case of sets (or graphs, for that matter) every surjective function can be written as a quotient over the relation given by an injective function. Translated to "abstract nonsense", this is just saying that every epimorphism is regular in Set [1, Example 7.72].
    ${ }^{5}$ A span is a diagram of the form $A \leftarrow C \rightarrow B$.

[^5]:    ${ }^{6}$ The width of a tree decomposition of graphs is the maximum size of any of the pieces (often called bags or parts) of the decomposition. This notion admits an appropriate categorial generalization as shown in [2].

[^6]:    ${ }^{7}$ Here we specify that the maps $f_{A}$ have to be epimorphisms but observe that, by Lemma 2.16, this is already guaranteed.

[^7]:    ${ }^{8}$ The terminal graph is the terminal object in Grph, consisting of one vertex with a single loop.

[^8]:    ${ }^{9}$ This is a very well-known strength of category theory: since all definitions are stated up to isomorphism and since constructions are done via universal properties, there is a sense in which all the results one obtains are canonical.

[^9]:    ${ }^{10}$ It is well known that, if $f: G \rightarrow H$ and $g: H \rightarrow J$ are graph contractions, then $g f: G \rightarrow J$ also is.

