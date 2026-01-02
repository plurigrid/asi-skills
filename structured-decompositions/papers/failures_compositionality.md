# Algorithmic and Extremal Obstructions Through the Language of Cohomology 

Anny Beatriz Azevedo<br>University of São Paulo

Benjamin Merlin Bumpus<br>University of São Paulo

Matteo Capucci<br>University of Strathclyde

James Fairbanks<br>University of Florida

Daniel Rosiak<br>NIST


#### Abstract

We model problems as presheaves that assign sets of certificates to input instances and we show how to use presheaf Crech cohomology to capture the precise ways in which local solutions fail to patch into global ones. Applied to problems like VertexCover, CycleCover, and OddCycleTransversal, our framework exposes emergent phenomena, such as hidden cycles or the inflation of small, local solutions. This approach not only rephrases classical results like König's Theorem in cohomological terms, but also reveals how to systematically account for failures of compositionality. Although our main focus is on presheaves of sets, the methods generalize naturally to Abelian presheaves, suggesting a rich interplay between graph theory, cohomology, and complexity. This work represents a first step toward a systematic, sheaf-theoretic theory of algorithmic structure and related obstructions.


## 1 Introduction

1.1. Obstructions, objects whose existence precludes the possibility of a given mathematical construction, abound in mathematics and, accordingly, many deep results throughout the field are concerned with finding, classifying and accounting for them. Indeed, there is no lack of preeminent conjectures - such as the Hodge Conjecture (a Millennium Prize problem), the Tate Conjecture and the Weil Conjectures, to name a few famous ones - that deal more or less directly with studying obstructions.
1.2. In modern, or parameterized complexity theory, the importance of understanding combinatorial obstructions is elucidated by the simple, but profound observation that FPT ${ }^{1}$ is equivalent to polynomialtime pre-processing, or kernelization [10]. Hence there is a sense in which efficient algorithms are deeply related to either efficiently computing obstructions or efficiently reducing an input instance to a small graph. Thus not only are obstructions mathematically relevant, practical and computationally useful, but, as Estivill-Castro, Fellows, Langston and Rosamond point out [12], they stand out as a promising ingredient towards the development of a 'mathematical monster machine' [18] - where theoretical advances are obtained through small, principled, nearly automated steps - for the development of algorithmics.
1.3. Thus it would be useful to have an abstract perspective on obstructions in combinatorics and algorithmics. But how, then, in these settings should we go about detecting, accounting and manipulating obstructions in an organized and systematic way? Historically, both in the context of the aforementioned famous conjectures and in many other application areas, cohomology stands out as a convenient tool to get the job done [17]. Other than areas of discrete mathematics, that are entirely built around cohomological methods (e.g. topological data analysis and discrete Morse Theory), classical combinatorics also touts

[^0]examples of important results which rely indispensably on elegant (co)-homological methods [8, 22, 30]. Two specific and celebrated examples include Lovász's resolution of Kneeser's conjecture [20] and Alon's result on splitting necklaces [1].
1.4. In this paper, we initiate a systematic account of obstructions arising in algorithmics and we do so by cohomological means. In particular, we find these tools well suited for speaking about both obstructions to the existence of a solution and obstructions to compositionality. We give a construction that allows us to cohomologically rephrase (but not prove) König's Theorem and other results in the flavor of the Erdös-Pósa. Furthermore, we show that one can use presheaf Čech cohomology to encode precisely the kinds of failures that occur when one tries to patch together local solutions into global ones.
1.5. Our perspective is to view computational problems as structured data assignments attaching sets of certificates to input instances. Said in light category-theoretic language, we view computational problems as presheaves and we study their presheaf Čech cohomology. Applied to VertexCover, CycleCover and OddCycleTransversal, for instance, the zeroth presheaf Čech cohomology group accounts for all emergent obstructions such as local small solutions becoming too large when joined together or the emergence of (odd) cycles that are not visible in the small constituent subgraphs comprising a (odd) cycle cover. Furthermore, we develop some cohomological results of independent interest that allow for the application of these methods to other computational problems without needing a deep understanding of cohomology.
1.6. Viewing computational problem as presheaves is not new to this contribution; indeed, in a short note [23], Mazza proposes a sheaf-theoretic outlook on complexity theory. Moreover, this perspective is not even foreign to discrete mathematics; for example in Dinur's talk ${ }^{2}$ on her celebrated proof of the PCP Theorem [9], she points out that the sheaf-theoretic structure of proper colorings of graphs plays a central role. More recently, there has been a growing use of sheaf-theoretic methods in the study of (promise) constraint satisfaction problems [2,26,24,14,19] and distributed computation [21,13].
1.7. Identifying the role of compositionality in certain problems is also not new: in applied category theory, there has been a thorough study of compositional structures and their applications [3, 16, 4, 5, 6]. And along with that also comes a growing need for accounting for non-compositionality and the study of such obstructions [27].
1.8. Although, as we have mentioned above, there has been a growing community which studies graph properties encoded as (pre)-sheaves, this nascent field is still young and there has not been a formal, systematic investigation of the expressiveness of cohomological methods in this setting. For this reason, here we focus on the simplest possible encoding of computational problems as presheaves; namely we consider presheaves of sets which assign a sets of certificates to each input graph. This choice has a few drawbacks and a few strengths.

- Drawbacks: since we are considering presheaves of sets (rather than, say, presheaves of vector spaces or modules), all of our cohomological computations rely on free Abelianizations. This has the effect that the higher cohomology groups are not of clear significance and thus the full power of homological algebra does not come to bear.
- Strengths: even in this comparatively simple setting, we obtain compelling insights into both compositional and structural obstructions to computational problems by studying the zeroth

[^1]cohomology group. By standard abstract nonsense, these results are all easily seen to generalize immediately to presheaves valued in any Abelian category (i.e. presheaves of Abelian groups or vector spaces over a field or modules over a ring).
1.9. We believe that considering Abelian presheaves - mappings that attach vector spaces, say, to input instances - is an exciting and fruitful direction of future study and we suspect that the methods presented here will open new doors for the interplay of graph theory, algebra and topology. Accordingly, we endeavor to make the present article as accessible and self-contained as possible so as to accommodate readers with varied backgrounds.

## 2 Motivation: Naive Dynamic Programming

2.1. Divide and conquer, or dynamic programming, is a common approach in algorithmics. The idea is as follows: to find solutions to computational problem on an input $G$, one works locally on small constituent parts thereof and then finds clever ways of patching these local solutions together into global solutions on $G$. A key step in designing these kinds of algorithms is that of identifying how local solutions may fail to patch together and how to go about keeping track of this information. This is what we mean by obstructions to compositionality and, as mentioned in Section 1, this article is focused on finding general mathematical language for speaking about such obstructions and mathematical tools for identifying them. It is our contention that cohomology is a useful tool for accounting for exactly this kind of information. To that end, in this section we proceed by means of examples to set the scene for the rest of the paper. In particular, we will consider two computational problems (Coloring and VertexCover) and explain at an intuitive level the kinds of obstructions to dynamic programming that we will later on identify algebraically.
2.2. Consider the following graph (left) broken up into three pieces (right) as follows.
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-03.jpg?height=299&width=486&top_left_y=1508&top_left_x=365)
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-03.jpg?height=342&width=850&top_left_y=1508&top_left_x=910)

The goal is to decide if there exists a 3-coloring of the above graph by solving the problem on the pieces and combining this information into a solution on the whole. To have any hope of negotiating agreements between local data, we first need to be able to relate local solutions to each other. We do so by taking into account the intersection between the pieces, which are represented below, together with their obvious inclusions (which we denote by hooked arrows).
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-04.jpg?height=555&width=889&top_left_y=281&top_left_x=618)
2.3. Now the key intuition is that, if we know that each of the pieces above is small (bounded by some constant $k$, say), then we can enumerate the entire solution space locally and only incur a bounded timecost of $f(k)$ for each piece (where $f$ may well be exponential). For instance, in the case of 3-coloring, one has $f(k)=3^{k}$ and this can be visualized on our example graph as follows (where for the sake of space we only draw some of the many solutions for the leftmost piece).
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-04.jpg?height=641&width=966&top_left_y=1160&top_left_x=577)

Solutions in each piece relate to each other through their restriction to the pairwise intersections of the pieces. This is represented above by the arrows pointing down. Notice that, in the case of 3-Coloring, every global solution (below, right) gives rise to a set of local solutions (below, left) that have the same pairwise restrictions. But there is more: every such set of pairwise agreeing solutions gives rise to a global solution.
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-05.jpg?height=556&width=1462&top_left_y=317&top_left_x=330)

In particular, this means that, if we find a local solution that never contributes to a family of the kind shown above (i.e of pairwise agreeing local solutions), then we can safely remove it for it will never contribute to a global solution. With this in mind, we can find solutions on the whole recursively as follows. We start by asking if there exist pairs of solutions $\left(c_{1}, c_{2}\right)$ of the first and second pieces respectively such that $c_{1}$ and $c_{2}$ have the same restriction: if no such pair exists, then we reject; otherwise, we remove from the sets of local solutions all those elements that cannot be paired up this way. We then proceed recursively with the pieces of the decomposed instance. By what we already observed, this suffices for 3-Coloring since, if by the end of this process no local set of solutions has become empty, then we can can conclude that the whole admits a proper 3-coloring.
2.4. This is slightly non-standard way of writing down the well-known algorithm for coloring by dynamic programming on tree decompositions [11, 15]. As it turns out, using the language of category theory one can generalize this algorithm for categories equipped with a notion of cover of objects (in this case subgraphs whose union results in the bigger graph) as long as we can attach local solutions into a global one ${ }^{3}$, as is the case for coloring [2] (concretely, this amounts to a general categorical algorithm for constraint satisfaction problems).
2.5. In contrast, in the case of VertexCover2, we will see that local solutions are not as well-behaved. We employ the same instance along as the same decomposition into local pieces as before, but now we wish to decide if there exists a vertex cover of the graph of size at most 2 . Once again, assuming each part has at most $k$ vertices in it, we can enumerate the $2^{k}$ vertex covers of each piece as shown below (where the vertices chosen to be part of local vertex covers are marked in red).

[^2]![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-06.jpg?height=643&width=957&top_left_y=281&top_left_x=584)

However, if we apply the same method as we did in 2.3, patching together the local solutions, we do not necessarily have a solution for the bigger graph. For example, consider the following set of local solutions that agree on the intersections.
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-06.jpg?height=644&width=961&top_left_y=1125&top_left_x=580)

These do not patch together into a global solution because, although they hit all the edges, the vertex cover they form has size strictly greater than 2 .
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-06.jpg?height=240&width=459&top_left_y=1920&top_left_x=833)
2.6. The naive algorithm we used for GraphColoring no longer applies for VertexCover and this is a well-known fact in algorithmics [7]. In this second problem, we found an obstruction: the size restriction of the vertex cover is local information that does not get carried over from the local parts to the global instance. Knowing these obstructions becomes important to be able to construct dynamic
programming algorithms that $d o$ work since, to do so, one needs to be able to account for and track such local obstructions. In the following section, we will show how to use category-theoretic tools to reason about all such obstructions. To ground our abstraction firmly in a practical example, we will consider VertexCover as a case study. However, we wish to emphasize from the beginning that all the methods we will employ generalize to any suitable computational problem.

## 3 Presheaves and Čech Cohomology: VertexCover as a Case Study

3.1. In this section, we will view VertexCover through a category-theoretic lens. To aid readers not familiar with category theory and as a warm-up for what follows in this paper, the constructions in this section are purposefully presented in more familiar set-theoretic terms. In Section 4, we will employ slicker categorical devices to exhibit more examples and, in doing so, we will also restate some of the constructions in this section in more abstract terms.

## Warmup: VertexCover as a Presheaf

3.2. Definition. Given a graph $G$, we say that a vertex subset $A \subseteq V(G)$ is a vertex cover of $G$ if $G-A$ is edgeless (equivalently, if for every edge $\alpha=\{u, v\} \in E(G), u \in A$ or $v \in A$ ). We say that $A$ is a minimum vertex cover of $G$ if, for every vertex cover $B \subseteq V(G),|A| \leq|B|$.
3.3. As far as vertex covers are concerned, the computational task at hand is that of finding a minimum vertex cover in a given input graph $G$. As is standard, this is stated as a decision problem as follows.

VertexCover
Input: A graph $G$ and an integer $k$.
Task: Decide if $G$ admits a vertex cover of cardinality at most $k$.
3.4. The vertex cover number (i.e. the minimum size of a vertex cover in a given graph), is monotone under the subgraph relation, that is, the vertex cover number of a subgraph cannot be larger than that of its ambient graph. This suggests that certificates of VertexCover may be well-behaved with respect to monomorphisms ${ }^{4}$. Indeed, a vertex cover of a graph $G$ induces a vertex cover of any of its subgraphs. Here we point out that this is enough information to define a presheaf: i.e. a functorial assignment of sets of certificates to each graph equipped with maps that relate the certificates of one graph to the those of another. To do so, we will first recall some basic notions from category theory.
3.5. Definition. A category $C$ consists of a collection $C_{0}$ of objects and a collection $C_{1}$ of morphisms (arrows) with the following operations:

- For each morphism $f$ of $\mathrm{C}_{1}$, we assign an object $a=\operatorname{dom}(f)$ of $\mathrm{C}_{0}$ to be the domain of $f$ and an object $b=\operatorname{cod}(f)$ of $\mathrm{C}_{0}$ to be the codomain of $f$; we use the notation $f: a \rightarrow b$.
- For each pair $(f, g)$ of morphisms of $\mathrm{C}_{1}$ such that $\operatorname{dom}(g)=\operatorname{cod}(f)$, we assign a morphism $g \circ f$ called composition of $f$ and $g$, where $\operatorname{dom}(g \circ f)=\operatorname{dom}(f)$ and $\operatorname{cod}(g \circ f)=\operatorname{cod}(g)$, that satisfy the

[^3]Associative law: given morphisms of $\mathrm{C}_{1}$

$$
a \xrightarrow{f} b \xrightarrow{g} c \xrightarrow{h} d
$$

we have $(h \circ g) \circ f=h \circ(g \circ f)$.

- For each object $a$ of $\mathrm{C}_{0}$, we assign a morphism $i d_{a}: a \rightarrow a$ of $\mathrm{C}_{1}$ that satisfy the Identity law: given morphisms of $\mathrm{C}_{1}$

$$
a \xrightarrow{f} b \xrightarrow{g} c
$$

we have

$$
1_{b} \circ f=f, \quad g \circ 1_{b}=g .
$$

3.6. Definition. A presheaf of sets over a small category C is a contravariant functor

$$
F: \mathrm{C}^{\mathrm{op}} \rightarrow \text { Set. }
$$

Spelling this out, a presheaf of sets $F$ is an assignment of a set $F(x)$ to each object $x \in \mathrm{C}$ and a function $F(f): F(y) \rightarrow F(x)$ to each morphism $f: x \rightarrow y$ in C such that the following two conditions hold:

1. F preserves composition (i.e. if $x \xrightarrow{f} y$ and $y \xrightarrow{g} z$ are two morphisms in C , then $F(g \circ f)= F(f) \circ F(g)$ ) and
2. $F$ preserves identities (i.e. $F\left(\mathrm{id}_{x}\right)=\mathrm{id}_{F(x)}$ for all objects $x$ ).

An element $A \in F(x)$ is said to be a section of $F$ at $x$ and, accordingly, $F(x)$ is referred to as the set of sections at $x$. The functions $F(f)$ are called restriction maps.
3.7. Staying as concrete as possible and in an attempt to bridge graph-theoretic and category-theoretic language, throughout most of this article we will be restricting our attention to the posetal category ${ }^{5} \operatorname{Sub}(G)$ where $G$ is some given graph. This category, defined formally below, has subgraphs of $G$ as objects and injective graph homomorphisms as arrows.
3.8. Definition. Given a graph $G$, the category $\operatorname{Sub}(G)$ has subgraphs of $G$ as its objects. We will say that there is an arrow $f: H \rightarrow K$ between two subgraphs of $G$ if $f$ is a homomorphism of graphs and the following diagram is commutative.
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-08.jpg?height=151&width=265&top_left_y=1884&top_left_x=930)
3.9. It is not difficult to see that if $f$ makes the above diagram commute, then $f$ is injective. So, to give an arrow between $H, K$ subgraphs of $G$ is equivalent to say $H \subseteq K-$ in particular, there is at most one such map.

[^4]![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-09.jpg?height=624&width=1439&top_left_y=240&top_left_x=345)
Figure 1: The presheaf with domain $\operatorname{Sub}\left(K_{2}\right)$ associated to the problem of deciding if a graph admits a vertex cover of cardinality at most 1 .

3.10. A sweeping conceptual point we wish to make here is that, given any computational problem $F$, it is fruitful to consider morphisms with respect to which the following assignment is functorial:

$$
\text { instance } X \mapsto \text { all certificates of } F \text { on } X \text {. }
$$

This is the case for VertexCover: there is a presheaf $\mathcal{V}: \operatorname{Sub}(G)^{\text {op }} \rightarrow$ Set which sends each subgraph of $G$ to the set of all of its vertex covers. This yields the assignment

$$
\begin{aligned}
\mathcal{V}: \operatorname{Sub}(G)^{\mathrm{op}} & \longrightarrow \text { Set } \\
H & \longmapsto\{A \subseteq V(H): A \text { is a vertex cover of } H\}
\end{aligned}
$$

equipped with the following restriction maps: given $f: H \hookrightarrow K$, we put

$$
\begin{aligned}
\mathcal{V}(f): \mathcal{V}(K) & \longrightarrow \mathcal{V}(H) \\
A & \longmapsto A \upharpoonright_{H}:=\{v \in A: v \in V(H)\}
\end{aligned}
$$

This construction is well defined and indeed yields a presheaf (Lemma 3.11 below). Notice that, for now, we put no restrictions on the size of the vertex covers; this will be done later (see Figure 1) when we consider the presheaf $\boldsymbol{V}_{\leq k}$ (e.g. in Proposition 3.21).
3.11. Lemma. $\mathcal{V}$ is a presheaf.

Proof. We need to prove that given $f: H \hookrightarrow K$ and $g: K \hookrightarrow J$, one has $\mathcal{V}(g \circ f)=\mathcal{V}(f) \circ \mathcal{V}(g)$ and that $\mathcal{V}\left(i d_{H}\right)=i d_{\mathcal{V}(H)}$.
For the first one, given $A$ a vertex cover of $J$, we have $\mathcal{V}(g \circ f)(A)=A \upharpoonright_{H}$ and $[\mathcal{V}(f) \circ \mathcal{V}(g)](A)= \left(A \upharpoonright_{K}\right) \upharpoonright_{H}$. Note that

$$
\left(A \upharpoonright_{K}\right) \upharpoonright_{H}=\left\{v \in V(H): v \in A \upharpoonright_{K}\right\}=\{v \in V(H): v \in K \wedge v \in A\} .
$$

Since $H \subseteq K$, then

$$
\{v \in V(H): v \in V(K) \wedge v \in A\}=\{v \in V(H): v \in A\}=A \upharpoonright_{H} .
$$

Hence, we have that $\mathcal{V}(g \circ f)=\mathcal{V}(f) \circ \mathcal{V}(g)$.
Finally, we also have that $\mathcal{V}\left(i d_{H}\right)=i d_{\mathcal{V}(H)}$ simply because given $A$ a vertex cover of $H, A \subseteq V(H)$, and therefore

$$
A \upharpoonright_{H}=\{v \in V(H): v \in A\}=A
$$

## Qed.

3.12. The restriction maps of a presheaf allow us to systematically track how global certificates can be converted into local ones. Notice, however, that, since we have not placed any restriction on the size of the vertex cover in the presheaf above, one can actually go the other way: given any collection of vertex covers of the subgraphs, if these vertex covers agree on intersections, then they can be patched together uniquely to form a global vertex cover. Presheaves that satisfy this condition are known as sheaves (defined below). We will show (Lemma 3.16) that $\mathcal{V}$ is an example of such a construction; another example is the $n$-coloring functor (as we alluded to earlier in 2.3, without proof).
3.13. Definition. Fix a presheaf $F: \operatorname{Sub}(G)^{\mathrm{op}} \rightarrow$ Set and a collection of subgraphs $\mathcal{U}:=\left(H_{i}\right)_{i \in I}$ which cover a subgraph $H$ of $G$ (i.e. such that $\bigcup_{i} H_{i}=H$ ). A matching family of $F$ on $\mathcal{U}$ is family $\left\{A_{i} \in F\left(H_{i}\right)\right\}_{i \in I}$ of local sections that agree on the intersections, that is, for all $i, j \in I$ we have

$$
A_{i} \upharpoonright H_{i} \cap H_{j}=A_{j} \upharpoonright H_{i} \cap H_{j}
$$

3.14. Notice how every global section $A \in F(H)$ induces a matching family on any cover $\left(H_{i}\right)_{i \in I}$ of $H$, simply by defining $A_{i}:=A \upharpoonright_{H_{i}}$. A presheaf is a sheaf when all matching families arise uniquely in such a way:
3.15. Definition. We say that a presheaf $F: \operatorname{Sub}(G)^{\mathrm{op}} \rightarrow$ Set is a sheaf if it satisfies the following sheaf condition:

For any matching family $\left\{A_{i} \in F\left(H_{i}\right)\right\}_{i \in I}$ of $F$ on a cover $\left(H_{i}\right)_{i \in I}$ of any given $H \in \operatorname{Sub}(G)$, there exists a unique global section $A \in F(H)$ that agrees with the local ones, i.e., $A \upharpoonright_{H_{i}}=A_{i}$ for all $i \in I$.

We call $A$ the amalgamation of the matching family $\left\{A_{i}\right\}_{i \in I}$.
3.16. Proposition. $\mathcal{V}$ is a sheaf.

Proof. Suppose that we have $H \in \operatorname{Sub}(G)$ and a cover of graphs $\left\{H_{i}\right\}_{i \in I}$ for $H$. Moreover, suppose that we have a family $\left\{A_{i}\right\}_{i \in I}$ of vertex covers $A_{i} \in \mathcal{V}\left(H_{i}\right)$ that agree on the intersections, that is, for all $i, j \in I$ we have

$$
A_{i} \upharpoonright H_{i} \cap H_{j}=A_{j} \upharpoonright H_{i} \cap H_{j} .
$$

Let's see that $\bigcup_{i \in I} A_{i}$ is the unique vertex cover of $H$ that agrees with the other vertex covers.
First, we note that $A=\bigcup_{i \in I} A_{i}$ is a vertex cover of $H$. Suppose not, then there exists $\alpha$ an edge in $H-A$. Since $H=\bigcup_{i \in I} H_{i}$, there exists a $i \in I$ such that $\alpha \in E\left(H_{i}\right)$. Now, because the vertices of $\alpha$ are not in $A$ and $A$ is the union $\bigcup_{i \in I} A_{i}$, we have that these vertices are also not in $A_{i}$. Hence $\alpha \in E\left(H_{i}-A_{i}\right)$, contradicting the fact that $A_{i}$ is a vertex cover of $H_{i}$.

The union $A=\bigcup_{i \in I} A_{i}$ satisfies $A \upharpoonright_{H_{i}}=A_{i}$ for all $i \in I$, so let's show that it is the unique vertex cover with this property. Suppose $B$ is a vertex cover of $H$ satisfying the property. Since $A_{i}=B \upharpoonright_{H_{i}}$ and $B \upharpoonright_{H_{i}} \subseteq B$, for all $i$, we have $A=\bigcup_{i \in I} A_{i} \subseteq B$. Now, if $v \in B \subseteq V(H)$, since $H=\bigcup_{i \in I} H_{i}$, there exists a $i \in I$ such that $v \in V\left(H_{i}\right)$. We then have $v \in A_{i}$, because $B \upharpoonright_{H_{i}}=A_{i}$. Therefore, $B \subseteq \cup_{i \in I} A_{i}$, and we proved that $B=\cup_{i \in I} A_{i}=A$.
Qed.
3.17. To view presheaves (or sheaves for that matter) as computational problems, one defines the following general computational task.

## $F$-Decision

Input: An object $x \in \mathrm{C}$ where C is the domain of the fixed presheaf $F: \mathrm{C}^{\mathrm{op}} \rightarrow$ Set.
Question: Decide if $x$ has a non-empty set of certificates; in other words, output "yes" if $F(x)$ is non-empty and "no" otherwise.
3.18. At this point the reader is going to protest that the sheaf $\mathcal{V}$ we just described does not encode an interesting decision problem, since all instances of $\mathcal{V}$-Decision are yes-instances (the fact that we have placed no restriction on the sizes of the vertex covers implies that the entire vertex set is always a certificate). This is indeed the case and the reason we have taken the time to study $\mathcal{V}$ is that it will appear naturally in connection with the following presheaf that does indeed encode VertexCover.
3.19. Given a $k \in \mathbb{N}$, we consider

$$
\begin{aligned}
\mathcal{V}_{\leq k}: \operatorname{Sub}(G)^{\text {op }} & \longrightarrow \\
H & \longmapsto\{A \subseteq V(H): A \text { is a vertex cover of } H \text { and }|A| \leq k\}
\end{aligned}
$$

and we define the action on the arrows as before, because when we restrict a vertex cover with size at most $k$, we have a vertex cover with size at most $k$ (see Figure 1).
3.20. Now the same calculations as before show that $\mathcal{V}_{\leq k}$ is a functor. But, in this case, it is not necessarily a sheaf. This is because when we consider the union of the vertex covers of the smaller graphs (and we just saw in Proposition 3.16 that this is the only possible vertex cover for the bigger graph), it can end up having size greater than $k$, as we will see next. In some sense, being reminiscent of the presheaf of bounded functions on a topological space (which famously fails to be a sheaf [29]) the following is a prototypical failure of the sheaf condition.
3.21. Proposition. $\mathcal{V}_{\leq k}$ is not a sheaf.

Proof. Let's consider the following example, where we are looking for vertex covers of size one in a two-vertex complete graph, i.e., we set $k=1$ and $G=K_{2}$ (the idea can be adapted to any $k>1$ ).
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-12.jpg?height=617&width=633&top_left_y=279&top_left_x=747)

Consider the cover $\left\{\emptyset, H_{1}, H_{2}\right\}$ of $H_{3}$ and consider the matching family

$$
\emptyset \in \mathcal{V}_{\leq 1}(\emptyset),\left\{v_{1}\right\} \in \mathcal{V}_{\leq 1}\left(H_{1}\right),\left\{v_{2}\right\} \in \mathcal{V}_{\leq 1}\left(H_{2}\right) .
$$

This family does not have an amalgamation in $\mathcal{V}_{\leq 1}\left(H_{3}\right)=\left\{\emptyset,\left\{v_{1}\right\},\left\{v_{2}\right\}\right\}$. In fact, as we saw in the proof of Proposition 3.16, the only possible amalgamation is the union of the local solutions, but in this case the union is $\left\{v_{1}, v_{2}\right\}$, which is not in $\mathcal{V}_{\leq 1}\left(H_{3}\right)$.
Qed.
3.22. Although $\mathcal{V}_{\leq k}$ is not a sheaf, it is somehow halfway there. In the definition of the sheaf condition, the amalgamation has to satisfy two things: existence and uniqueness. In the case of $\mathcal{V}_{\leq k}$, we have the latter: when the amalgamation of matching family exists, it is unique, so this presheaf fails to be a sheaf only with respect to the "existence" of amalgamations. Since a presheaf can fail to be a sheaf in these two ways, we present the following terminology that encodes what happens when a presheaf satisfies either uniqueness or existence.
3.23. Definition. We say that a presheaf $F: \operatorname{Sub}(G)^{\mathrm{op}} \rightarrow$ Set is
(a) separated if given $H \in \operatorname{Sub}(G)$ and a cover $\left\{H_{i}\right\}_{i \in I}$ for $H$, if $A, B \in F(H)$ are such that $A \upharpoonright_{H_{i}}=B \upharpoonright_{H_{i}}$ for all $i \in I$, then $A=B$.
(b) lavish ${ }^{6}$ if given $H \in \operatorname{Sub}(G)$, a cover $\left\{H_{i}\right\}_{i \in I}$ for $H$ and a matching family $\left\{A_{i} \in F\left(H_{i}\right)\right\}_{i \in I}$, there exists $A \in F(H)$ such that $A \upharpoonright_{H_{i}}=A_{i}$ for all $i \in I$.
3.24. Proposition. $\mathcal{V}_{\leq k}$ is a separated presheaf.

Proof. Given $H \in \operatorname{Sub}(G)$ and a cover $\left\{H_{i}\right\}_{i \in I}$ for $H$, suppose $A, B \in \mathcal{V}_{\leq k}(H)$ are such that $A \upharpoonright_{H_{i}}=B \upharpoonright_{H_{i}}$ for all $i \in I$. If $v \in A \subseteq V(H)$, since $H=\bigcup_{i \in I} H_{i}$, there exists a $i \in I$ such that $v \in V\left(H_{i}\right)$. Therefore, $v \in A \upharpoonright_{H_{i}}$, and since $A \upharpoonright_{H_{i}}=B \upharpoonright_{H_{i}}$ this implies that $v \in B \upharpoonright_{H_{i}}$, ie, $v \in B$. The inclusion $B \subseteq A$ is similar.
Qed.

[^5]3.25. There is a well-known construction called sheafification [29] that allows one to construct a sheaf from any given presheaf. As was shown recently [2], if a decision problem can be encoded as a sheaf, then it admits a fast (i.e. FPT-time) dynamic programming algorithm. As we will see, although it is of great use in geometry, the sheafification construction is not immediately useful for algorithmic considerations since, for example, when it is applied to $\mathcal{V}_{\leq k}$, it yields the sheaf $\mathcal{V}$ (which, we have already seen, does not encode an interesting computational problem). However, as we will see in Section 4, sheafification can be conceptually useful when trying to understand obstructions to algorithmic compositionality, in other words, obstructions to begin a sheaf. To that end, in the following subsection we will first revisit the definition of a sheaf in a more category-theoretic way and recall the definition of the zeroth cohomology group.

## Some Background on Cohomology: Obstructions to being a sheaf

3.26. In general, what it means for a presheaf to be a sheaf (resp. a separated or lavish presheaf) can be stated in terms of an equalizer diagram. In the interest of being self-contained, we include the definition below.
3.27. Definition. Given two morphisms $f, g: x \rightarrow y$ in a category C , we say that an object $z \in \mathrm{C}$ together with a morphism $h: z \rightarrow x$ is an equalizer of $f$ and $g$ if

- $f \circ h=g \circ h$;
- Whenever $j: w \rightarrow x$ satisfies $f \circ j=g \circ j$, there exists a unique morphism $k: w \rightarrow z$ such that $h \circ k=j$.
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-13.jpg?height=195&width=385&top_left_y=1297&top_left_x=915)
3.28. Equalizers can be thought as categorical ways of encoding equalitites. In Set, we have that the equalizer object of two functions $f, g: A \rightarrow B$ is the subset $E=\{a \in A: f(a)=g(a)\}$ of $A$ on which $f$ and $g$ agree.
3.29. With this definition in mind, we can now recall a more categorical framing of the properties described in Definitions 3.15 and 3.23.
3.30. Definition. Let $F: \operatorname{Sub}(G)^{\text {op }} \rightarrow$ Set be a presheaf. For any object $H \in \operatorname{Sub}(G)$ and any cover

$$
\mathcal{U}=\left(H_{i} \stackrel{f_{i}}{\hookrightarrow} H\right)_{i \in I}
$$

of $H$, the matching family of $F$ on $\mathcal{U}$ are defined to be the following equalizer in Set (which we will denote as Match( $\mathcal{U}, F$ ))

$$
\mathrm{Eq}\left(q_{1,0}, q_{1,1}\right) \stackrel{\longrightarrow}{\longrightarrow} \prod_{i \in I} F\left(H_{i}\right) \underset{q_{1,1}}{\stackrel{q_{1,0}}{\longrightarrow}} \prod_{i, j \in I} F\left(H_{i} \cap H_{j}\right)
$$

where $q_{1,0}$ is given for each $i, j \in I$ by the restriction map $F\left(H_{i}\right) \rightarrow F\left(H_{i} \cap H_{j}\right)$, while $q_{1,1}$ by the restriction $F\left(H_{j}\right) \rightarrow F\left(H_{i} \cap H_{j}\right)$.

The maps $\left(F(H) \xrightarrow{F\left(f_{i}\right)} F\left(H_{i}\right)\right)_{i \in I}$ assemble into a morphism

$$
\begin{aligned}
\delta^{-1}: \quad F(H) & \longrightarrow \prod_{i \in I} F\left(H_{i}\right) \\
A & \longmapsto\left(F\left(f_{i}\right)(A)\right)_{i \in I}
\end{aligned}
$$

equalizing $q_{1,0}$ and $q_{1,1}$ (where the superscript in $\delta^{-1}$ denotes an index, not an inverse map). Thus, by the universal property of equalizers, one has a unique map $\xi$ making the following commute.
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-14.jpg?height=222&width=1251&top_left_y=640&top_left_x=436)

If, for all objects $H$ and all covers $\mathcal{U}$ thereof, the arrow $\xi$ is

- a monomorphism, then one says that $F$ is separated;
- an epimorphism, then one says that $F$ is lavish;
- an isomorphism, then one says that $F$ is sheaf.
3.31. Example. Taking $F$ in the definition above to be $\mathcal{V}_{\leq k}$ and setting $\mathcal{U}=\left\{H_{1}, H_{2}, H_{3}\right\}$ to be a cover of some graph $H \subseteq G$, we have that

$$
\begin{array}{rlr}
q_{1,0}: \quad \mathcal{V}_{\leq k}\left(H_{1}\right) \times \mathcal{V}_{\leq k}\left(H_{2}\right) \times \mathcal{V}_{\leq k}\left(H_{3}\right) & \longrightarrow & \mathcal{V}_{\leq k}\left(H_{1} \cap H_{2}\right) \times \mathcal{V}_{\leq k}\left(H_{1} \cap H_{3}\right) \times \mathcal{V}_{\leq k}\left(H_{2} \cap H_{3}\right) \\
\left(A_{1}, A_{2}, A_{3}\right) & \longmapsto & \left(A_{1} \upharpoonright \Lambda_{1} \cap H_{2}, A_{1} \upharpoonright \Lambda_{1} \cap H_{3}, A_{2} \upharpoonright H_{2} \cap H_{3}\right)
\end{array}
$$

when we restrict to the first index, and

$$
\begin{array}{ccc}
q_{1,1}: \quad \mathcal{V}_{\leq k}\left(H_{1}\right) \times \mathcal{V}_{\leq k}\left(H_{2}\right) \times \mathcal{V}_{\leq k}\left(H_{3}\right) & \longrightarrow \mathcal{V}_{\leq k}\left(H_{1} \cap H_{2}\right) \times \mathcal{V}_{\leq k}\left(H_{1} \cap H_{3}\right) \times \mathcal{V}_{\leq k}\left(H_{2} \cap H_{3}\right) \\
\left(A_{1}, A_{2}, A_{3}\right) & \longmapsto & \left(A_{2} \upharpoonright H_{1} \cap H_{2}, A_{3} \upharpoonright H_{1} \cap H_{3}, A_{3} \upharpoonright H_{2} \cap H_{3}\right)
\end{array}
$$

when we restrict to the second one. Now, the set of triples ( $A_{1}, A_{2}, A_{3}$ ) that have the same image under $q_{0}$ and $q_{1}$ are exactly the families of solutions that agree on the intersections, that is, the matching families as we defined in 3.15 . Also, $\xi$ has the same action of $\delta^{-1}$, i.e., the restriction of solutions; thus, to say that $\xi$ is mono is to say that two solutions of $H$ that agree on each restriction are the same and to say that $\xi$ is epi is to say that for each matching family of local solutions there exists at least a solution of $H$ whose restriction to each subgraph corresponds to the local solutions of the matching family.
3.32. Notice, as it is completely standard, that if we consider Ab, the category of Abelian groups instead of Set in the definition of sheaf, we can rewrite the set where the functions agree to be the kernel of the difference $q_{1,1}-q_{1,0}$. This approach will be useful to us as we wish to apply standard constructions in cohomology. In order to talk about Čech cohomology, we first recall the notion of Crech nerve.
3.33. Definition. Consider $X \in \operatorname{Sub}(G)$ and a cover $\mathcal{U}=\left(H_{i} \stackrel{f_{i}}{\hookrightarrow} X\right)_{i \in I}$. The Čech nerve of the cover $\mathcal{U}$ - denoted $N(\mathcal{U})$ - is the following simplicial object in $\operatorname{Sub}(G)$ (whose degeneracy maps are left unnamed
for clarity):
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-15.jpg?height=186&width=1513&top_left_y=322&top_left_x=305)

Here the parallel morphisms are defined the usual way (e.g., implicitly assuming an ordering on the index set $I$, one has that $d_{2,1}: H_{i} \cap H_{j} \cap H_{k} \rightarrow H_{i} \cap H_{k}$ ).
3.34. Now fix a presheaf $F: \operatorname{Sub}(G)^{\mathrm{op}} \rightarrow \mathrm{Ab}$. Taking the image of a Čech nerve under $F$ induces the following cochain complex (note that the domain of $\delta_{\mathcal{U}}^{-1}$ is $F(X)$ - i.e. the global sections - instead of 0 ; this differs from the standard treatment ${ }^{7}$ )

$$
F(X) \xrightarrow{\delta_{\mathcal{U}}^{-1}} \prod_{i} F\left(H_{i}\right) \xrightarrow{\delta_{\mathcal{U}}^{0}} \prod_{i, j} F\left(H_{i} \cap H_{j}\right) \xrightarrow{\delta_{\mathcal{U}}^{1}} \prod_{i, j, k} F\left(H_{i} \cap H_{j} \cap H_{k}\right)
$$

where the coboundary maps are given by

$$
\delta_{\mathcal{U}}^{-1}:=F\left(d_{0}\right) \quad \text { and } \quad \delta_{\mathcal{U}}^{n}:=\sum_{i=0}^{n}(-1)^{i} F\left(d_{n+1, i}\right)
$$

Since $F$ takes values in Ab , one can define the $n$-th Čech cohomology of the presheaf $F$ on the object $H$ with cover $\mathcal{U}$ as the quotient of $\operatorname{ker} \delta_{\mathcal{U}}^{n}$ by $\operatorname{im} \delta_{\mathcal{U}}^{n-1}$ as in the Definition 3.35 below.
3.35. Definition. The $n$-th Čech cohomology of a presheaf $F: \operatorname{Sub}(G)^{\mathrm{op}} \rightarrow$ Set on an object $X$ with cover $\mathcal{U}$ is defined as

$$
H^{n}(X, \mathcal{U}, F):=\operatorname{ker}\left(\delta^{n}\right) / \operatorname{im}\left(\delta^{n-1}\right) .
$$

3.36. Observation. For readers familiar with sheaf theory, we point out that all general results pertaining to cohomology that we develop in this paper apply to any site $(\mathrm{C}, J)$ where $J$ is a Grothendieck pretopology whose covers are finitely generated. ${ }^{8}$ For the reader not familiar with sheaf theory, the previous sentence roughly means that we need not restrict to (pre)sheaves of the form $\operatorname{Sub}(G)^{\text {op }} \rightarrow$ Set; instead we can consider any category C with sufficiently nice structure (i.e. admitting pullbacks) and equipped with a well-defined notion of what it means for a collection of objects to "cover" any given input object $x \in \mathrm{C}$. We also can consider any Abelian category instead of Ab, such as $\operatorname{Vect}(K)$ vector spaces over a field $K$ and $\operatorname{Mod}(R)$ modules over a ring $R$. In that case, the quotient in Definition 3.35 can be generalized by $\operatorname{coker}\left(\operatorname{im}\left(\delta^{n-1}\right) \rightarrow \operatorname{ker}\left(\delta^{n}\right)\right)$.
3.37. Example. Let's see the zeroth presheaf-Čech cohomology in a concrete example. Consider the same example of Proposition 3.21, where $G$ is a two-vertex complete graph. Let's look at the cover $\mathcal{U}=\left\{\emptyset, H_{1}, H_{2}\right\}$ of $H_{3}$. First, we compute $\operatorname{ker}\left(\delta^{0}\right)$ (which is exactly the matching families)

$$
\operatorname{ker}\left(\delta^{0}\right)=\left\{\{\emptyset, \emptyset, \emptyset\}, \quad\left\{\emptyset,\left\{v_{1}\right\}, \emptyset\right\}, \quad\left\{\emptyset, \emptyset,\left\{v_{2}\right\}\right\}, \quad\left\{\emptyset,\left\{v_{1}\right\},\left\{v_{2}\right\}\right\}\right\} .
$$

[^6]Now, we need to describe im( $\delta^{-1}$ ). We have

$$
\begin{aligned}
& \delta^{-1}: \mathcal{V}_{\leq 1}\left(H_{3}\right) \rightarrow \mathcal{V}_{\leq 1}(\emptyset) \times \mathcal{V}_{\leq 1}\left(H_{1}\right) \times \mathcal{V}_{\leq 1}\left(H_{2}\right) \\
& \delta^{-1}:\left\{\emptyset,\left\{v_{1}\right\},\left\{v_{2}\right\}\right\} \rightarrow\{\emptyset\} \times\left\{\emptyset,\left\{v_{1}\right\}\right\} \times\left\{\emptyset,\left\{v_{2}\right\}\right\}
\end{aligned}
$$

which is given by sending each solution of $\mathcal{V}_{\leq 1}\left(H_{3}\right)$ to its corresponding restriction to each $H_{i}$. That way, we have

$$
\operatorname{im}\left(\delta^{-1}\right)=\left\{\{\emptyset, \emptyset, \emptyset\}, \quad\left\{\emptyset,\left\{v_{1}\right\}, \emptyset\right\}, \quad\left\{\emptyset, \emptyset,\left\{v_{2}\right\}\right\}\right\} .
$$

Therefore, the quotient $H^{0}=\operatorname{ker}\left(\delta^{0}\right) / \operatorname{im}\left(\delta^{-1}\right)$ is generated by $\left\{\emptyset,\left\{v_{1}\right\},\left\{v_{2}\right\}\right\}$, which is exactly the matching family that fails to have an amalgamation.
3.38. We have that $\delta^{-1}$ describes how global sections restrict to local sections. If $\mathcal{V}_{\leq 1}$ were a sheaf, every matching family would be "lifted" to a unique global section, i.e., every matching family (all of $\operatorname{ker}\left(\delta^{0}\right)$ ) would be in the image of $\delta^{-1}$.
3.39. The generators of $H^{0}$ indicate the local sections that, despite agreeing on the intersections, fail to be lifted to global sections. Recall that the functor $F$ being lavish means that for each matching family of local solutions there exists at least a solution on the global graph whose restriction to each subgraph corresponds to the local solutions of the matching family. Thus, $H^{0}$ generally informs us about the existence of amalgamations: when $H^{0}(X, \mathcal{U}, F)$ is trivial for all objects $X$ and all covers of $X, F$ is lavish; when $H^{0}(X, \mathcal{U}, F)$ is non-trivial, $F$ fails to be lavish. In short, we have learned that the zeroth presheaf Čech cohomology can be thought of as a measure of the failure of being lavish.
3.40. One can distill (see for example Gallier and Quaintance [17]) from Definition 3.35 a cover-independent cohomology object $H^{n}(X, F)$ defined as

$$
H^{n}(X, F):=\operatorname{colim}_{\mathcal{U} \in \operatorname{Cov}(X)} H^{n}(X, \mathcal{U}, F)
$$

We will be interested in the functor that this defines when the first argument varies and the second is fixed, namely the presheaf:

$$
H^{n}(-, F): \mathrm{C}^{\mathrm{op}} \rightarrow \mathrm{Ab}
$$

3.41. We note that we can use the technique of Abelianization to define the functor $\mathcal{V}_{\leq k}$ in Ab . As a matter of fact, it can be used in any $F$ defined in Set. We describe this process below.
3.42. Definition. Given a set $S$, we say that a function $a: S \rightarrow \mathbb{Z}$ with $\operatorname{im}(a) \backslash\{0\}$ finite is a linear combination of (elements of) $S$. We can also represent the linear combinations of $S$ as $a=\sum_{s \in S} a_{s} \cdot s$ where $a_{s}:=a(s)$ and we denote by $s$ the function $s: S \rightarrow \mathbb{Z}$ that sends $s$ to 1 and the rest of the elements of $S$ to 0 . Now, we define the group $\mathbb{Z}[S]=\{a: a$ is a linear combination of $S\}$ with group operation given by $\left(\sum_{s \in S} a_{s} \cdot s\right)+\left(\sum_{s \in S} b_{s} \cdot s\right)=\sum_{s \in S}\left(a_{s}+b_{s}\right) \cdot s$.
3.43. In the case of VertexCover we have

$$
\mathbb{Z}\left[\mathcal{V}_{\leq k}(H)\right]=\left\{\sum_{A \in \mathcal{V}_{\leq k}(H)} a_{A} \cdot A: a \text { is a linear combination of } \mathcal{V}_{\leq k}(H)\right\}
$$

where $A$ denotes the function $A: \mathcal{V}_{\leq k}(H) \rightarrow \mathbb{Z}$ that sends $A$ to 1 and the rest of the elements of $\mathcal{V}_{\leq k}(H)$ to 0 . In the next section, we use this technique to explicitly describe $H^{0}$ for VertexCover.

## 4 The Zeroth Čech Cohomology of Computational Problems

4.1. In this section we will consider other computational problems such as CycleCover and OddCycleTransversal. We will show that the zeroth cohomology group finds other kinds of obstructions. For example, in the case of CycleCover (Proposition 4.47), the zeroth cohomology groups detects not just issues of size, as it did in the case of VertexCover, but also the phenomenon of emergent cycles: cycles that are only seen when one considers more than one piece of a cover at once.
4.2. To do this systematically, we will first develop some general results concerning the cohomology of separated presheaves in the following subsection. These results are of independent interest, but they are also useful since they will allow us to avoid tedious calculations later on and indeed they make it possible to apply cohomological tools to study computational problems without needing to focus too much on the commutative algebra involved. With that in mind, the reader who is not interested in (or not familiar with) category theory can safely skip the proofs in the following subsection and simply consider how the results are used later on.

## Developing Some Technical Machinery

4.3. We have mentioned that one can turn a presheaf into a sheaf through a construction called sheafification. Formally, being an adjoint functor, there is a sense in which sheafification sends any presheaf to its "nearest" sheaf [29,28]. We will see that, in cases where $F$ is a separated presheaf on $\operatorname{Sub}(G)$, the sheafification of $F$, denoted by $F^{+}$, will help us characterize the zeroth presheaf Čech cohomology: $H^{0}(X, F)$ will be something analogous to the quotient of $F^{+}(X)$ by $F(X)$. This result gives us an easier and more conceptual approach to computing $H^{0}$.
4.4. Observation. Once again, nodding to readers knowledgeable in sheaf theory, we point out that the following results all generalize to more interesting domains: rather than studying presheaves on $\operatorname{Sub}(G)$, the results of this section apply equally well to any category equipped with a Grothendieck pretopology which is finitely presented (meaning that each covering sieve is generated by finitely many morphisms).
4.5. To turn $F$ into a sheaf, the idea is to somehow replace $F(H)$ by the matching families over all possible covers of $H$. Sheafification consists of two application of a construction called the plus construction. Roughly the idea is the following: we want to keep any section of $F(H)$ that was already an amalgamation of a matching family, but we also want to formally add to our collection of global sections all those matching families that did not admit an amalgamation. Furthermore, we wish to do so without creating duplicates of amalgamations. To that end one instead works with equivalence classes of matching families (where these equivalence classes are obtained by identifying matching families that have a restriction in common).
4.6. Definition. Let $\operatorname{Sh}(\operatorname{Sub}(G)), \operatorname{SPsh}(\operatorname{Sub}(G))$ and $\operatorname{Psh}(\operatorname{Sub}(G))$ denote the categories of sheaves, separated presheaves and presheaves on $\operatorname{Sub}(G)$, respectively. The composite

$$
\operatorname{Sh}(\operatorname{Sub}(G)) \hookrightarrow \operatorname{SPsh}(\operatorname{Sub}(G)) \hookrightarrow \operatorname{Psh}(\operatorname{Sub}(G))
$$

admits a left adjoint called the sheafification functor (see Rosiak's textbook [29, Sec. 10.2.7] for a reference). This functor is given by two applications of the plus construction $(-)^{+}: \operatorname{Psh}(\operatorname{Sub}(G)) \rightarrow \operatorname{Psh}(\operatorname{Sub}(G))$ defined as

$$
F^{+}: X \mapsto \operatorname{colim}_{\mathcal{U} \in \operatorname{Cov}(\mathcal{X})} \operatorname{Match}(\mathcal{U}, F)
$$

4.7. In Set, this colimit is given by the quotient

$$
\coprod_{\mathcal{U} \in \operatorname{Cov}(X)} \operatorname{Match}(\mathcal{U}, F) / \sim
$$

where □ denotes a disjoint union and $\sim$ is the equivalence relation given as follows: for $A=\left\{A_{i}\right\}_{i \in I} \in$ Match $(\mathcal{U}, F)$ and $B=\left\{B_{j}\right\}_{j \in J} \in \operatorname{Match}\left(\mathcal{U}^{\prime}, F\right)$, with $\mathcal{U}=\left\{H_{i}\right\}_{i \in I}, \mathcal{U}^{\prime}=\left\{H_{j}\right\}_{j \in J} \in \operatorname{Cov}(X)$, we have

$$
A \sim B \text { iff } \exists \mathcal{U}^{\prime \prime}=\left\{H_{l}\right\}_{l \in L} \in \operatorname{Cov} \text {, with } \mathcal{U}^{\prime \prime} \subseteq \mathcal{U}, \mathcal{U}^{\prime \prime} \subseteq \mathcal{U}^{\prime},(H), \text { such that } \forall l \in L, A_{l}=B_{l}
$$

which justifies the idea presented in 4.5.
4.8. Observation. One can also state the definition of the plus construction as $F^{+} X \cong \operatorname{colim}_{\mathcal{U} \in \operatorname{Cov}(X)} \operatorname{ker} \delta_{\mathcal{U}}^{0}$. This follows directly from the definition since $\operatorname{Match}(\mathcal{U}, F) \cong \operatorname{ker} \delta_{\mathcal{U}}^{0}$ for any cover $\mathcal{U}$ of any $X$.
4.9. We point out that, for any presheaf $F$, the presheaf $F^{+}$is necessarily separated and $F^{++}$is a sheaf; in particular, one application of the plus construction suffices to obtain a sheaf from any separated presheaf (see [29] for a reference).
4.10. Many interesting problems are monotone under the subgraph relation, as we will see later in this section. We will see that such problems can be represented by presheaves $F$ on $\operatorname{Sub}(G)$ such that the set of solutions of a subgraph $H \subseteq G$ is actually a subset of $\operatorname{Sub}(H)$ (in the case of VertexCover, the vertex covers can be seen as subgraphs with only vertices, no edges). We will also see that, as is the case of VertexCover, such problems are always separated presheaves, where the union is the only possible solution. We prove now a result that can characterize the sheafification of such problems.
4.11. Proposition. Let $F: \operatorname{Sub}(G)^{\mathrm{op}} \rightarrow$ Set be a separated presheaf. Suppose that $\tilde{F}: \operatorname{Sub}(G)^{\mathrm{op}} \rightarrow$ Set is a presheaf such that for all edges $\alpha \in E(G), \tilde{F}(\alpha) \subseteq F(\alpha)$. Moreover, given $H \subseteq G$, suppose that $\bigcup_{i \in I} A_{i} \in \tilde{F}(H)$ whenever $\left\{A_{i} \in F\left(H_{i}\right)\right\}_{i \in I}$ is a matching family of the cover $H=\bigcup_{i \in I} H_{i}$. Then $\tilde{F}$ is the sheafification of $F$.

Proof. Since $F$ is separated we have

$$
F^{+}(H)=\operatorname{colim}_{\mathcal{U} \in \operatorname{Cov}(H)} \operatorname{Match}(\mathcal{U}, F)
$$

So we need to check that

$$
\tilde{F}(H)=\operatorname{colim}_{\mathcal{U} \in \operatorname{Cov}(H)} \operatorname{Match}(\mathcal{U}, F)
$$

Given $\mathcal{U}, \mathcal{U}^{\prime} \in \operatorname{Cov}(H)$ and an arrow $\mathcal{U} \hookrightarrow \mathcal{U}^{\prime}$, we have the following commutative triangles
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-18.jpg?height=205&width=761&top_left_y=2023&top_left_x=681)
where the arrows to $\tilde{F}(H)$ act as taking the union. We need to show that, given any $X$ and any arrows $f_{\mathcal{U}}: \operatorname{Match}(\mathcal{U}, F) \rightarrow X$ and $f_{\mathcal{U}^{\prime}}: \operatorname{Match}\left(\mathcal{U}^{\prime}, F\right) \rightarrow X$, there exists a unique $k: \tilde{F}(H) \rightarrow X$ such that the
following commutes
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-19.jpg?height=330&width=768&top_left_y=296&top_left_x=678)

We divide $H$ in subgraphs given by the edges, i.e., if $E(H)=\left\{\alpha_{1}, \ldots, \alpha_{n}\right\}$ we denote $H_{i}=H\left[\alpha_{i}\right]$ and $f_{i}: H_{i} \hookrightarrow H$. We then consider the cover $\mathcal{U}=\left\{H_{i}\right\}_{i \leq n}$.
Given $A \in \tilde{F}(H)$, for each $i \leq n$ we consider $A_{i}=\tilde{F}\left(f_{i}\right)(A)$. By hypothesis, $A_{i} \in F\left(H_{i}\right)$, for all $i \leq n$. We denote this matching family by

$$
Y_{H}=\left\{A_{i} \in F\left(H_{i}\right)\right\} \in \operatorname{Match}(\mathcal{U}, F)
$$

We then define

$$
\begin{aligned}
k: \tilde{F}(H) & \longrightarrow \quad X \\
A & \longmapsto f_{\mathcal{U}}\left(Y_{H}\right)
\end{aligned}
$$

Now, because $\mathcal{U}$ is the minimal cover of $H$ and because the arrows between the sets of matching families are the restriction, we have that $k$ makes the above diagram commute. Let us see that is the only arrow with this property.
Let $k^{\prime}: \tilde{F}(H) \rightarrow X$ be a function such that the following diagram commutes ( $\mathcal{U}$ being the cover we defined above)
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-19.jpg?height=190&width=433&top_left_y=1387&top_left_x=846)

Given $H^{\prime} \subseteq H$ we can always consider the matching family $Y_{H^{\prime}}$ defined above and we have that

$$
k^{\prime}\left(H^{\prime}\right)=k^{\prime}\left(\cup Y_{H^{\prime}}\right)=f_{\mathcal{U}}\left(Y_{H^{\prime}}\right)
$$

where the second equality comes from the last commutative diagram. Therefore $k=k^{\prime}$.

## Qed.

4.12. Applying the above result, we will now see that, for $k \geq 2$, the sheafification of the presheaf $\boldsymbol{V}_{\leq k}$ encoding VertexCover is none other than the sheaf $\mathcal{V}$ of Proposition 3.16
4.13. Proposition. $\mathcal{V}: \operatorname{Sub}(G)^{\mathrm{op}} \rightarrow$ Set is the sheafification of $\mathcal{V}_{\leq k}$, for $k \geq 2$.

Proof. We have seen in Proposition 3.16 that if we have $H \subseteq G$, a cover $\bigcup_{i \in I} H_{i}=H$ and $\left\{A_{i}\right\}_{i \in I}$ a family of vertex covers that agree on the intersections, then $\bigcup_{i \in I} A_{i}$ is a vertex cover of $H$. Furthermore, given an edge $\alpha \in E(G)$ and $A \in \mathcal{V}(\alpha)$, we have $|A| \leq 2 \leq k$, so that $A \in \mathcal{V}_{\leq k}$. By Proposition 4.11, $\mathcal{V}$ is the sheafification of $\mathcal{V}_{\leq k}$, whenever $k \geq 2$.
Qed.
4.14. One of the contributions of this work is to show that this connection between cohomology and sheafification can be made very explicit and satisfying: Theorem 4.19 will show that, for any presheaf $F$, the zeroth presheaf Čech cohomology functor arises as the quotient of $F^{+}$by $F$ (precisely, it will be the cokernel of $\eta_{F}: F \rightarrow F^{+}$, the unit of the adjunction given by sheafification).
4.15. Lemma. If $F: \operatorname{Sub}(G)^{\mathrm{op}} \rightarrow \mathrm{Ab}$ is separated, then $\operatorname{colim}{ }_{\mathcal{U} \in \operatorname{Cov}(X)} \operatorname{im} \delta_{\mathcal{U}}^{-1} \cong F(X)$.

Proof. Since $F$ is separated, the morphism $\delta_{\mathcal{U}}^{-1}: F(X) \rightarrow \prod_{i} F\left(H_{i}\right)$ is mono as shown in the following commutative diagram.
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-20.jpg?height=222&width=592&top_left_y=653&top_left_x=764)

Thus, since $F$ is valued in an Abelian category, where every morphism which is both a monomorphism and an epimorphism is already an isomorphism, one has that $F(X) \cong \operatorname{im} \delta_{\mathcal{U}}^{-1}$. Moreover, this made no assumption on the choice of $\mathcal{U}$, thus

$$
F(X) \cong \operatorname{im} \delta_{\mathcal{U}}^{-1} \quad \forall \mathcal{U} \in \operatorname{Cov}(X) .
$$

By the property of colimits, there exists a unique arrow $r: \operatorname{colim}_{\mathcal{U} \in \operatorname{Cov}(X)} \operatorname{im}_{\mathcal{U}}^{-1} \rightarrow F(X)$ such that for all $\mathcal{U} \in \operatorname{Cov}(X)$
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-20.jpg?height=212&width=538&top_left_y=1258&top_left_x=792)
commutes, that is, $r \circ s=i$, where $i: \operatorname{im} \delta_{\mathcal{U}}^{-1} \cong F(X)$. Let us see that $r$ is an isomorphism. Since $i$ is iso, there exists $j: F(X) \rightarrow \operatorname{im} \delta_{\mathcal{U}}^{-1}$ such that $i \circ j=i d_{F(X)}$ and $j \circ i=i d_{\operatorname{im} \delta_{\mathcal{U}}^{-1}}$. We have that $s \circ j$ is the inverse of $r$. Indeed, we have that

$$
r \circ s \circ j=i \circ j=i d_{F(X)} .
$$

Now, by the property of colimits, $i d_{\mathrm{im}} \delta_{\mathcal{U}}^{-1}$ is the only arrow such that
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-20.jpg?height=205&width=770&top_left_y=1826&top_left_x=676)
commutes, that is, $i d_{\text {im } \delta_{\mathcal{U}}^{-1}} \circ s=s$. But,

$$
s \circ j \circ r \circ s=s \circ j \circ i=s \circ i d_{\operatorname{im}} \delta_{\mathcal{U}}^{-1}=s
$$

so that $s \circ j \circ r=i d_{\text {im } \delta_{\mathcal{U}}^{-1}}$. Therefore, $\operatorname{colim}_{\mathcal{U} \in \operatorname{Cov}(X)} \operatorname{im} \delta_{\mathcal{U}}^{-1} \cong F(X)$, as desired.
Qed.
4.16. We will now use Observation 4.8 and Lemma 4.15 to prove that, if $F$ is separated, then the functor $H^{0}(-, F): \operatorname{Sub}(G)^{\mathrm{op}} \rightarrow \mathrm{Ab}$ can be rewritten as the quotient of $F^{+}$by $F$.
4.17. Corollary. Let $F: \operatorname{Sub}(G)^{\text {op }} \rightarrow$ Set be a separated presheaf. For every $X \subseteq G$, we fix a cover $\mathcal{U} \in \operatorname{Cov}(X)$ and consider $f_{X}: F(X) \rightarrow F^{+}(X)$ given by

$$
F(X) \xrightarrow{\xi_{\mathcal{U}}} \operatorname{Match}(\mathcal{U}, F) \hookrightarrow \coprod_{\mathcal{U} \in \operatorname{Cov}(X)} \operatorname{Match}(\mathcal{U}, F) \xrightarrow{\pi} F^{+}(X)
$$

where $\pi: \coprod_{\mathcal{U} \in \operatorname{Cov}(X)} \operatorname{Match}(\mathcal{U}, F) \rightarrow F^{+}(X)=\coprod_{\mathcal{U} \in \operatorname{Cov}(X)} \operatorname{Match}(\mathcal{U}, F) / \sim$ is the projection map of the equivalence relation defined in 4.7. Then, we have that the zeroth Čech cohomology is the quotient

$$
H^{0}(X, F)=\mathbb{Z}\left(F^{+}(X)\right) / \mathbb{Z}\left(\operatorname{im} f_{X}\right)
$$

4.18. The proof of Corollary 4.17 is rather algebraic and thus mostly relevant to readers comfortable with sheaf theory. For this reason and since the proof techniques actually yield a much more general result, we will only give a proof of this stronger theorem (Theorem 4.19 below) from which one can easily deduce Corollary 4.17 as a special case.
4.19. Theorem. Suppose $F$ is an Abelian presheaf on a site ( $\mathrm{C}, J$ ) where $J$ is a finitely generated Grothendieck topology. If $F$ is separated, then, letting $\eta: F \Rightarrow F^{+}$be the unit of the adjunction given by sheafification, one has that $H^{0}(-, F)=\operatorname{coker}\left(F \xrightarrow{\eta_{F}} F^{+}\right)$.

Proof. We have

$$
\begin{aligned}
H^{0}(X, F) & :=\underset{\mathcal{U} \in \operatorname{Cov}(X)}{\operatorname{colim}} H^{0}(X, \mathcal{U}, F) \\
& =\underset{\mathcal{U} \in \operatorname{Cov}(X)}{\operatorname{colim}} \operatorname{coker}\left(\operatorname{im} \delta^{-1} \xrightarrow{\xi_{\mathcal{U}}^{0}} \operatorname{ker} \delta_{\mathcal{U}}^{0}\right) \\
& =\operatorname{coker} \underset{\mathcal{U} \in \operatorname{Cov}(X)}{\operatorname{colim}}\left(\operatorname{im} \delta^{-1} \xrightarrow{\xi_{\mathcal{U}}^{0}} \operatorname{ker} \delta_{\mathcal{U}}^{0}\right) \\
& =\operatorname{coker}\left(\underset{\mathcal{U} \in \operatorname{Cov}(X)}{\operatorname{colim}} \operatorname{im} \delta^{-1} \xrightarrow{\operatorname{colim}}{ }_{\mathcal{U} \in \operatorname{Cov}(X)} \xi_{\mathcal{U}}^{0} \underset{\mathcal{U} \in \operatorname{Cov}(X)}{\operatorname{colim}} \operatorname{ker} \delta_{\mathcal{U}}^{0}\right) \\
& =\operatorname{coker}\left(F X \xrightarrow{\operatorname{colim}}{ }_{\mathcal{U} \in \operatorname{Cov}(X)} \xi_{\mathcal{U}}^{0} \underset{\mathcal{U} \in \operatorname{Cov}(X)}{\operatorname{colim}} \operatorname{ker} \delta_{\mathcal{U}}^{0}\right) \\
& =\operatorname{coker}\left(F X \xrightarrow{\operatorname{colim}_{\mathcal{U} \in \operatorname{Cov}(X)} \xi_{\mathcal{U}}^{0}} F^{+} X\right)
\end{aligned}
$$

The morphisms $\operatorname{colim}_{\mathcal{U} \in \operatorname{Cov}(X)} \xi_{\mathcal{U}}^{0}$ are the components of a natural transformation $\eta: F \Rightarrow F^{+}$. Moreover, this is precisely the definition of the unit of the sheafification functor. Thus, our previous derivation allows us to restate the functor $H^{0}(-, F)$ as a cokernel of $\eta$, as desired.
Qed.
4.20. In the example of Proposition 3.21, $\boldsymbol{V}_{\leq k}$ failed to be a sheaf when the union of local solutions was "too big". We will see now that this case is the only obstruction we have for this particular presheaf.

First, we prove a result that will help even more with our calculation of the zeroth cohomology. Since all the problems we work with in this paper are separated presheaves, they are sub-presheaves of their sheafification (i.e. the unit of the adjunction is monic). In other words, one has that the set of solutions $F(H)$ is canonically a subset of $F^{+}(H)$. With this in mind, the next result shows that, when dealing with presheaves of sets, which are Abelianized freely, the quotient of $F^{+}(H) / F(H)$ is equivalent to the Abelianization of the difference $F^{+}(H)-F(H)$.
4.21. Lemma. Let $Y$ be a set and $B \subseteq Y$ a subset. If $f: B \hookrightarrow Y$ is the inclusion, then the quotient $\mathbb{Z}[Y] / \mathbb{Z}[\operatorname{im} f]$ is isomorphic to $\mathbb{Z}[Y-B]$.

Proof. To make the writing simpler, we denote $W:=\mathbb{Z}[\operatorname{im} f]$. We define

$$
\begin{array}{rll}
h: & \mathbb{Z}[Y] / W & \longrightarrow \\
\mathbb{Z}[Y-B] \\
\sum_{y \in Y} a_{y} \cdot y+W & \longmapsto \sum_{y \in Y-B} a_{y} \cdot y
\end{array}
$$

First, let's see that $h$ is well defined. Let $\sum_{y \in Y} a_{y} \cdot y+W=\sum_{y \in Y} b_{y} \cdot y+W$. We have that $0 \in W$, so there exists $\sum_{y \in B} c_{y} \cdot y \in W$ such that

$$
\sum_{y \in Y} a_{y} \cdot y+0=\sum_{y \in Y} b_{y} \cdot y+\sum_{y \in B} c_{y} \cdot y
$$

We can rewrite that as

$$
\sum_{y \in B} a_{y} \cdot y+\sum_{y \in Y-B} a_{y} \cdot y=\sum_{y \in B}\left(b_{y}+c_{y}\right) \cdot y+\sum_{y \in Y-B} b_{y} \cdot y
$$

so that $\sum_{y \in Y-B} a_{y} \cdot y=\sum_{y \in Y-B} b_{y} \cdot y$, which means that $\sum_{y \in Y} a_{y} \cdot y+W$ and $\sum_{y \in Y} b_{y} \cdot y+W$ are sent by $h$ to the same element.
Let's check that $h$ is injective. Suppose that $\sum_{y \in Y-B} a_{y} \cdot y=\sum_{y \in Y-B} b_{y} \cdot y$, let's see that $\sum_{y \in Y} a_{y} \cdot y+W= \sum_{y \in Y} b_{y} \cdot y+W$. Let $\sum_{y \in Y} a_{y} \cdot y+\sum_{y \in B} c_{y} \cdot y$ be an arbitrary element of $\sum_{y \in Y} a_{y} \cdot y+W$, we consider $\sum_{y \in B}\left(a_{y}+c_{y}-b_{y}\right) \cdot y \in W$, so that

$$
\sum_{y \in Y} b_{y} \cdot y+\sum_{y \in B}\left(a_{y}+c_{y}-b_{y}\right) \cdot y=\sum_{y \in B}\left(a_{y}+c_{y}\right) \cdot y+\sum_{y \in Y-B} b_{y} \cdot y
$$

and using the hypothesis we have

$$
\sum_{y \in B}\left(a_{y}+c_{y}\right) \cdot y+\sum_{y \in Y-B} b_{y} \cdot y=\sum_{y \in B}\left(a_{y}+c_{y}\right) \cdot y+\sum_{y \in Y-B} a_{y} \cdot y=\sum_{y \in Y} a_{y} \cdot y+\sum_{y \in B} c_{y} \cdot y
$$

and thus we proved that $\sum_{y \in Y} a_{y} \cdot y+W=\sum_{y \in Y} b_{y} \cdot y+W$.
Finally, let's check that $h$ is surjective. Given $\sum_{y \in Y-B} a_{y} \cdot y$, we define $\sum_{y \in Y} b_{y} \cdot y \in \mathbb{Z}[Y]$ as

$$
b_{y}= \begin{cases}a_{y}, & \text { if } y \in Y-B \\ 0, & \text { if } y \in Y\end{cases}
$$

and we have that $h\left(\sum_{y \in Y} b_{y} \cdot y\right)=\sum_{y \in Y-B} a_{y} \cdot y$.
Qed.
4.22. Observation. Notice that the fact that $F^{+}(H) / F(H)$ is equivalent to the Abelianization of $F^{+}(H)- F(H)$ is possible precisely because in this paper we are considering free Abelianizations of presheaves of sets. We leave it as exciting future work to consider Abelian presheaves where the algebraic structure is not free.
4.23. We now have all tools to finally characterize the zeroth Čech cohomology for VertexCover.
4.24. Proposition. If $k \geq 2$, then $H^{0}\left(X, \mathcal{V}_{\leq k}\right)=\mathbb{Z}[\{A \in \mathcal{V}(X):|A|>k\}]$.

Proof. We fix a cover $\mathcal{U}=\left\{X_{i}\right\}_{i \leq m} \in \operatorname{Cov}(X)$ and we consider $f_{X}: \mathcal{V}_{\leq k}(X) \rightarrow \mathcal{V}(X)$ given by

$$
\mathcal{V}_{\leq k}(X) \xrightarrow{\xi_{\mathcal{U}}} \operatorname{Match}\left(\mathcal{U}, \mathcal{V}_{\leq k}\right) \hookrightarrow \coprod_{\mathcal{U} \in \operatorname{Cov}(X)} \operatorname{Match}\left(\mathcal{U}, \mathcal{V}_{\leq k}\right) \xrightarrow{\pi} \mathcal{V}_{\leq k}^{+}(X) \cong \mathcal{V}(X)
$$

On an object $X \in \operatorname{Sub}(G)$, this function identifies sections that agree locally on some cover of $X$. The action of $f_{X}$ is given by

$$
A \in \mathcal{V}_{\leq k}(X) \stackrel{\xi \mathcal{u}}{\longmapsto}\left(A \upharpoonright_{X_{1}}, \ldots, A \upharpoonright_{X_{m}}\right) \hookrightarrow\left(A \upharpoonright_{X_{1}}, \ldots, A \upharpoonright_{X_{m}}\right) \stackrel{\pi}{\mapsto}\left[\left(A \upharpoonright_{X_{1}}, \ldots, A \upharpoonright_{X_{m}}\right)\right] \stackrel{\cong}{\mapsto} \bigcup_{i \leq m} A \upharpoonright_{X_{i}}=A
$$

Thus, $f_{X}$ can be seen as the inclusion $f_{X}: \mathcal{V}_{\leq k}(X) \hookrightarrow \mathcal{V}(X)$.
Defining $Y=\mathcal{V}(X)$ and $B=\mathcal{V}_{\leq k}(X)$, we have that

$$
\mathbb{Z}[Y-B]=\mathbb{Z}[\{A \in \mathcal{V}(X):|A|>k\}]
$$

We then use Theorem 4.19 and Lemma 4.21 to obtain the desired result.
Qed.
4.25. Summarizing briefly, as we mentioned earlier, $H^{0}$ intuitively collects all the obstructions to lavishness. Based on the example of Proposition 3.21, we argued informally that these obstructions should only have to do with cardinality: namely, in the case of VertexCover the only obstructions to algorithmic compositionality are the sizes of the associated sets. We showed this formally by proving that $H^{0}\left(-, \mathcal{V}_{\leq k}\right)$ is exactly $\mathbb{Z}[\{A \in \mathcal{V}:|A|>k\}]$. However, these are not the only kinds of obstructions that $H^{0}$ can detect: in the following subsection we will see that, along with detecting "size issues", $H^{0}$ also detects other kinds of emergent phenomena. For example, in the case of CycleCover we can divide a graph in pieces in such way that $H^{0}$ will detect cycles that are not visible locally by pieces that are small.

## More computational problems as examples

4.26. In this section, we spell out another two concrete examples and consider their cohomology. Furthermore, since we use constructions similar to those employed for VertexCover, we will employ some general category-theoretic tools that, as biproduct, can be easily seen to yield a great many more examples of computational problems as presheaves on $\operatorname{Sub}(G)$. Since these examples would all have a similar flavor, we limit ourselves to giving concrete descriptions of VertexCover, CycleCover and BipartiteCover.

## Categorical Generalities to Construct Presheaves from Monotone Graph Properties

4.27. Definition. Given a category C and a fixed object $X$ of C , we say that an object $Y$ of C is a subobject of $X$ if there exists in C a monic arrow $f: Y \hookrightarrow X$.
4.28. Definition. A functor $p: \mathbb{P} \hookrightarrow \mathrm{C}$ is pullback-absorbing if, given any pullback square of the following form,
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-24.jpg?height=181&width=329&top_left_y=554&top_left_x=898)
there exists an object $X^{\prime} \in \mathbb{P}$ such that $p\left(X^{\prime}\right) \cong p(X) \times_{Y} Z$.
4.29. We intend to use this language in the following way: we wish to use the functor $p: \mathbb{P} \hookrightarrow C$ to talk about a property that some objects of C satisfy. Given a property $P$, we see $\mathbb{P}$ as the category of objects of C that satisfy $P$, and $p(X)$ will denote that $X$ satisfies the property $P$.
4.30. Intuitively a property $p$ is pullback-absorbing if for all $Y \in \mathrm{C}$, the pullback of two subobjects of $Y$ satisfies the property as long as one of the subobjects of $Y$ satisfies the property. In the case $\mathrm{C}=\operatorname{Sub}(G)$, this translates to monotonicity under subobjects: if an object $Y$ satisfies the property $p$, all the subobjects of $Y$ also satisfy $p$.
4.31. Lemma. If $\mathrm{C}=\operatorname{Sub}(G)$, then $p$ is pullback-absorbing if and only if $\mathbb{P}$ is monotone under the subgraph relation.

Proof. $(\Rightarrow)$ Let $Y=p(Y) \in \mathbb{P}$ and $f: Z \hookrightarrow Y$ be a subobject of $y$. Consider the following pullback
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-24.jpg?height=197&width=439&top_left_y=1456&top_left_x=844)
we have that $i d: Z \rightarrow Z$ and $f: Z \hookrightarrow Z$ make the following commute
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-24.jpg?height=197&width=355&top_left_y=1761&top_left_x=885)
so that there exists a unique $k: Z \rightarrow p(Y) \times_{Y} Z$ such that the whole diagram commutes
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-24.jpg?height=349&width=587&top_left_y=2071&top_left_x=769)

Therefore, $p(Y) \times_{Y} Z=Z$, and because $p$ is pullback-absorbing, we have that $p(Y) \times_{Y} Z=p(Z)$. $(\Leftarrow)$ When we consider the pullback
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-25.jpg?height=181&width=331&top_left_y=382&top_left_x=898)
we have that $p(X) \times_{Y} Z$ is a subobject of $p(X)$, so, by hypothesis, it also satisfies $p$.
Qed.
4.32. Lemma. If $p_{1}: \mathbb{P}_{1} \hookrightarrow \operatorname{Sub}(G)$ and $p_{2}: \mathbb{P}_{2} \hookrightarrow \operatorname{Sub}(G)$ are pullback-absorbing functors, then the following is a presheaf

$$
\begin{array}{rlr}
\operatorname{Sub}_{\mathbb{P}_{1,2}}(-): \operatorname{Sub}(G)^{o p} & \longrightarrow & \text { Set } \\
H & \longmapsto\left\{H^{\prime} \subseteq H: H^{\prime} \in \mathbb{P}_{1} \text { and } H-H^{\prime} \in \mathbb{P}_{2}\right\}
\end{array}
$$

and given $f: H \hookrightarrow K$, we put

$$
\begin{aligned}
\operatorname{Sub}_{\mathbb{P}_{1,2}}(f): \quad \operatorname{Sub}_{\mathbb{P}_{1,2}}(K) & \longrightarrow \operatorname{Sub}_{\mathbb{P}_{1,2}}(H) \\
K^{\prime} & \longmapsto \quad K^{\prime} \cap H
\end{aligned}
$$

where $K^{\prime} \cap H$ is the pullback of $K^{\prime} \hookrightarrow K$ and $H \hookrightarrow K$ in the category $\operatorname{Sub}(G)$.
Proof. We have that $\operatorname{Sub}_{\mathbb{P}_{1,2}}(-)$ is well defined on the arrows because $\left(K-K^{\prime}\right) \cap H=H-\left(K^{\prime} \cap H\right)$ and because $p_{1}$ and $p_{2}$ are pullback-absorbing, so that $K^{\prime} \cap H \in \mathbb{P}_{1}$ and $H-\left(K^{\prime} \cap H\right) \in \mathbb{P}_{2}$. Also, it is a functor, because if $H \hookrightarrow J \hookrightarrow K$ and
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-25.jpg?height=177&width=360&top_left_y=1514&top_left_x=644)
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-25.jpg?height=175&width=278&top_left_y=1516&top_left_x=1203)
are pullbacks, then the bigger square
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-25.jpg?height=308&width=364&top_left_y=1800&top_left_x=883)
is a pullback, which is the same as saying that $K^{\prime} \cap H=K^{\prime} \times_{K} H=\left(K^{\prime} \times_{K} J\right) \times_{J} H=\left(K^{\prime} \cap J\right) \cap H$ and means that the following commutes
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-25.jpg?height=145&width=764&top_left_y=2264&top_left_x=678)

And since $H^{\prime} \cap H=H^{\prime}$, for $H^{\prime} \subseteq H$, we also have that $\operatorname{Sub}_{\mathbb{P}_{1,2}}\left(i d_{H}\right)=i d_{\operatorname{Sub}_{\mathbb{P}_{1,2}}}(H)$.
Qed.
4.33. Lemma. $\operatorname{Sub}_{\mathbb{P}_{1,2}}(-)$ is a separated presheaf.

Proof. Let $H$ be a subgraph of $G,\left\{H_{i}\right\}_{i \in I}$ a cover of $H$ and $H_{1}, H_{2} \in \operatorname{Sub}_{\mathbb{P}_{1,2}}(H)$, ie, $H_{1}, H_{2} \subseteq H$ such that $H_{1}, H_{2} \in \mathbb{P}_{1}$, and suppose that $H_{1} \upharpoonright_{H_{i}}=H_{2} \upharpoonright_{H_{i}}$ for all $i \in I$. Let us see that $H_{1}=H_{2}$. If $v \in V\left(H_{1}\right) \subseteq V(H)$, then there exists $i$ such that $v \in V\left(H_{i}\right)$, so that $v \in V\left(H_{1}\right) \upharpoonright_{H_{i}}=V\left(H_{2}\right) \upharpoonright_{H_{i}}$, therefore $v \in V\left(H_{1}\right)$. We can prove that all edges of $H_{1}$ are in $H_{2}$ using the same argument and the inclusion $H_{2} \subseteq H_{1}$ is analogous.
Qed.
4.34. Remark. For the purpose of this work, having in mind the examples we will be working on, we defined the previous functor with a property for the complement of graphs, but we note that if we define $H \mapsto\left\{H^{\prime} \subseteq H: H^{\prime} \in \mathbb{P}\right\}$, with only one property about the subgraphs, this also results in a separated presheaf, as long as $p: \mathbb{P} \hookrightarrow \operatorname{Sub}(G)$ is pullback-absorbing, since we can put $\mathbb{P}_{2}=\operatorname{Sub}(G)$.
4.35. For VertexCover, we define $\mathbb{V} \subseteq \operatorname{Sub}(G)$ as $H \in \mathbb{V}$ iff $H$ is edgeless; and given a $k \in \mathbb{N}$, we define $\mathbb{V}_{k} \subseteq \operatorname{Sub}(G)$ as $H \in \mathbb{V}_{k}$ iff $H$ is edgeless and $|H| \leq k$. We have that $\mathbb{V}$ and $\mathbb{V}_{k}$ are monotone under subobjects.
4.36. Notice that $\mathcal{V}_{\leq k}$ can be alternatively defined as

$$
\begin{array}{rlr}
\mathcal{V}_{\leq k}: \operatorname{Sub}(G)^{\text {op }} & \longrightarrow & \text { Set } \\
H & \longmapsto\left\{H^{\prime} \subseteq H: H^{\prime} \in \mathbb{V}_{k} \text { and } H-H^{\prime} \in \mathbb{V}\right\}
\end{array}
$$

and the relationship between the set of solutions of subgraphs is described as follows: given $f: H \hookrightarrow K$, we put

$$
\begin{aligned}
\mathcal{V}_{\leq k}(f): \quad \mathcal{V}_{\leq k}(K) & \longrightarrow \mathcal{V}_{\leq k}(H) \\
K^{\prime} & \longmapsto K^{\prime} \cap H
\end{aligned}
$$

4.37. Lemma. $\mathcal{V}_{\leq k}$ is a separated functor.

Proof. Since $\mathbb{V}$ and $\mathbb{V}_{k}$ are monotone under subobjects, the result follows from Lemma 4.32 and Lemma 4.33.
Qed.

## More Examples: CycleCover and OddCycleTransversal

4.38. Definition. Given a graph $G=(V(G), E(G))$, we say that $S \subseteq V(G)$ is a cycle cover of $G$ if $G-S$ is a forest, i.e., it does not have cycles. We say that $S$ is a minimum cycle cover if, for every cycle cover $R$, $|S| \leq|R|$.
4.39. We can state the cycle cover problem as

CycleCover
Input: A graph $G$ and an integer $k$.
Task: Decide if $G$ admits a cycle cover of cardinality at most $k$.
4.40. We will use the same property of $4.35, \mathbb{V}_{k}$, that relates to being a set of vertices of a given cardinality. But for talking about cycle covers, we need another property: we define $\mathbb{C} \subseteq \operatorname{Sub}(G)$ as $H \in \mathbb{C}$ iff $H$ doesn't have a cycle. We have that $\mathbb{C}$ is monotone under subobjects.
4.41. We define

$$
\begin{array}{rlr}
\mathscr{C}_{\leq k}: \quad \operatorname{Sub}(G)^{\text {op }} & \longrightarrow & \text { Set } \\
H & \longmapsto \quad\left\{H^{\prime} \subseteq H: H^{\prime} \in \mathbb{V}_{k} \text { and } H-H^{\prime} \in \mathbb{C}\right\}
\end{array}
$$

and given $f: H \hookrightarrow K$, we put

$$
\begin{aligned}
\mathscr{C}_{\leq k}(f): \quad \mathscr{C}_{\leq k}(K) & \longrightarrow \mathscr{C}_{\leq k}(H) \\
K^{\prime} & \longmapsto K^{\prime} \cap H
\end{aligned}
$$

4.42. Lemma. $\mathscr{C}_{\leq k}$ is a separated functor.

Proof. Since $\mathbb{V}_{k}$ and $\mathbb{C}$ are monotone under subobjects, the result follows from Lemma 4.32 and Lemma 4.33.
Qed.
4.43. Lemma. $\mathscr{C}_{\leq k}$ is not a sheaf.

Proof. Just like in the case of vertex covers, the only possible gluing for a matching family is the union. What might happen is that the union doesn't need to be a cycle cover as we see in this example: let's consider $H=K_{3}$ and the following cover $\left\{H_{1}, H_{2}\right\}$ :
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-27.jpg?height=319&width=369&top_left_y=1411&top_left_x=588)
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-27.jpg?height=383&width=347&top_left_y=1448&top_left_x=1194)

Now, we have that the empty set is a solution for the subgraphs $H_{1}$ and $H_{2}$, but the union is empty, which is not a solution for $H$.
Qed.
4.44. Let's think about the zeroth presheaf-Cech cohomology in the example given in the last proof. Calculating the matching families (i.e. $\operatorname{ker} \delta^{0}$ ) and the restrictions of $\mathscr{C}(H)$ (i.e. $\operatorname{im} \delta^{1}$ ), we have that $\{\emptyset, \ldots, \emptyset\}$ is the only matching family that doesn't lift to a global solution. This corresponds to the fact that $H^{0}$ is detecting the presence of an emergent cycle: the two graphs $H_{1}$ and $H_{2}$ do not contain cycles; and yet, their union does.
4.45. Since $\mathscr{C}_{\leq k}$ is separated, we can characterize its zeroth presheaf-Čech cohomology as we did for VertexCover. First, we need to talk about the sheafification of $\mathscr{C}_{\leq k}$.
4.46. Proposition. For $k \geq 2$, the sheafification of $\mathscr{C}_{\leq k}$ is given by

$$
\begin{aligned}
\operatorname{Sub}(-): \quad \operatorname{Sub}(G)^{\text {op }} & \longrightarrow \\
H & \longmapsto\left\{H^{\prime}: H^{\prime} \subseteq H\right\}
\end{aligned}
$$

and given $f: H \hookrightarrow K$, we put

$$
\begin{aligned}
\operatorname{Sub}(f): \quad \operatorname{Sub}(K) & \longrightarrow \operatorname{Sub}(H) \\
K^{\prime} & \longmapsto K^{\prime} \cap H
\end{aligned}
$$

Proof. Given $H \subseteq G$, a cover $\bigcup_{i \in I} H_{i}=H$ and $\left\{H_{i}^{\prime} \in \mathscr{C}_{\leq k}\left(H_{i}\right)\right\}_{i \in I}$ a matching family of cycle covers, we have $\bigcup_{i \in I} H_{i}^{\prime} \in \operatorname{Sub}(H)$. Moreover, given $\alpha=K \in E(H)$ an edge, if we consider $f: K \hookrightarrow H$, then

$$
\operatorname{Sub}(f)\left(H^{\prime}\right)=H^{\prime} \cap K, \forall H^{\prime} \in \operatorname{Sub}(H) .
$$

Since $K$ is an edge, we have that $H^{\prime} \cap K$ is a cycle cover of $K$ and $\left|H^{\prime} \cap K\right| \leq 2 \leq k$, so that $\operatorname{Sub}(f)\left(H^{\prime}\right) \in \mathscr{C}_{\leq k}(H)$. By Proposition 4.11, we have that $\operatorname{Sub}(-)$ is the sheafification of $\mathscr{C}_{\leq k}$.
Qed.
4.47. Proposition. $H^{0}\left(X, \mathscr{C}_{\leq k}\right)=\mathbb{Z}\left[\left\{X^{\prime} \subseteq X: X^{\prime} \notin \mathbb{V}_{k}\right.\right.$ or $\left.\left.X-X^{\prime} \notin \mathbb{C}\right\}\right]$.

Proof. We fix a cover $\mathcal{U}=\left\{X_{i}\right\}_{i \leq m} \in \operatorname{Cov}(X)$ and we consider $f_{X}: \mathcal{V}_{\leq k}(X) \rightarrow \mathcal{V}(X)$ given by

$$
\mathscr{C}_{\leq k}(X) \xrightarrow{\xi_{\mathcal{U}}} \operatorname{Match}\left(\mathcal{U}, \mathscr{C}_{\leq k}\right) \hookrightarrow \coprod_{\mathcal{U} \in \operatorname{Cov}(X)} \operatorname{Match}\left(\mathcal{U}, \mathscr{C}_{\leq k}\right) \xrightarrow{\pi} \mathscr{C}_{\leq k}^{+}(X) \cong \operatorname{Sub}(X)
$$

As was the case for VertexCover in Proposition 4.24, we have that $f_{X}$ can be seen as the inclusion $f_{X}: \mathscr{C}_{\leq k}(X) \hookrightarrow \operatorname{Sub}(X)$.
Defining $Y=\operatorname{Sub}(X)$ and $B=\mathscr{C}_{\leq k}(X)$, we have that

$$
\mathbb{Z}[Y-B]=\mathbb{Z}\left[\left\{X^{\prime} \subseteq X: X^{\prime} \notin \mathbb{V}_{k} \text { or } X-X^{\prime} \notin \mathbb{C}\right\}\right]
$$

We then use Theorem 4.19 and Lemma 4.21 to obtain the desired result.
Qed.
4.48. With this result we see that, in the case of CycleCover, $H^{0}$ can detect not only the problem with size but also emergent cycles.
4.49. Definition. Given a graph $G$, we say that $S \subseteq V(G)$ is a bipartite cover of $G$ if $G-S$ is a bipartite graph. We say that $S$ is a minimum bipartite cover if, for every bipartite cover $R,|S| \leq|R|$.
4.50. We can state the bipartite cover problem (also known as OddCycleTransversal) as follows.

## BipartiteCover

Input: A graph $G$ and an integer $k$.
Task: Decide if $G$ admits a bipartite cover of cardinality at most $k$.
4.51. Again, we will use the property $\mathbb{V}_{\leq k}$ presented in 4.35 . We also define other property $\mathbb{B}$ as follows: $H \in \mathbb{B}$ iff $H$ is bipartite. We have that $\mathbb{B}$ is monotone under subobjects.
4.52. We define

$$
\begin{array}{rlr}
\mathscr{B}_{\leq k}: \quad \operatorname{Sub}(G)^{\text {op }} & \longrightarrow & \text { Set } \\
H & \longmapsto\left\{H^{\prime} \subseteq H: H^{\prime} \in \mathbb{V}_{k} \text { and } H-H^{\prime} \in \mathbb{B}\right\}
\end{array}
$$

and given $f: H \hookrightarrow K$, we put

$$
\begin{aligned}
\mathscr{B}_{\leq k}(f): \quad \mathscr{B}_{\leq k}(K) & \longrightarrow \mathscr{B}_{\leq k}(H) \\
K^{\prime} & \longmapsto K^{\prime} \cap H
\end{aligned}
$$

4.53. And the next results follow as in the case of CycleCover, including its sheafification and the example that $\mathscr{C}_{\leq k}$ is not a sheaf.
4.54. Lemma. $\mathscr{B}_{\leq k}$ is a separated functor but not a sheaf.
4.55. Lemma. $H^{0}\left(X, \mathscr{B}_{\leq k}\right)=\mathbb{Z}\left[\left\{X^{\prime} \subseteq X: X^{\prime} \notin \mathbb{V}_{k}\right.\right.$ or $\left.\left.X-X^{\prime} \notin \mathbb{B}\right\}\right]$.

## The Compositionality of $H^{0}$

4.56. We saw that the zeroth presheaf Čech cohomology provides the information of the obstructions to naive algorithmic compositionality: i.e., the obstructions to the success of naive dynamic programming algorithms. Given a computational problem $F$, it is natural to ask if these failures, namely $H^{0}(-, F)$ itself, admit some form of well-behaved compositionality. In other words, we ask: "how close to being a sheaf can $H^{0}$ itself be?"
4.57. We will see that although $H^{0}(-, F)$ is not a sheaf in general, if $F$ has a suitably nice structure, then $H^{0}(-, F)$ is a lavish presheaf which, recalling from earlier (c.f. Definition 3.23), is to say that it satisfies the existence condition for global section.
4.58. Fixing some Abelian category A (e.g. Ab or $\operatorname{Vect}_{\mathbb{R}}$ ), we will now employ Theorem 4.19 to show that $H^{0}(-, F)$ is lavish for an Abelian presheaf $F: \operatorname{Sub}(G)^{\mathrm{op}} \rightarrow \mathrm{A}$ whenever $F$ is flasque, meaning that its restriction maps are epimorphisms. To this end, we will first need the following technical lemma which shows that one can distribute cokernels over pullbacks in an Abelian category. We prove this result for A any Abelian category; the reader not familiar with the relevant categorical notions can simply think of the whole proof as concerning Abelian groups.
4.59. Lemma. In an Abelian category, for any morphism $f$ into a pullback as shown in the following diagram,
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-29.jpg?height=294&width=508&top_left_y=2023&top_left_x=809)
there is an epimorphism $u$ : coker $f \rightarrow \operatorname{coker}\left(\ell_{1} f\right) \times_{\operatorname{coker}\left(\ell_{2} \ell_{1} f\right)} \operatorname{coker}\left(r_{1} f\right)$.

Proof. We liberally assume to be working in a concrete Abelian category of modules, by Freyd-Mitchell embedding [25].
From the situation described, one always gets a commutative square of cokernels which, by universality of pullbacks, yields a unique arrow as dashed below:
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-30.jpg?height=343&width=1466&top_left_y=470&top_left_x=320)

Here $(-)^{*}$ denotes the maps induced between cokernels.
Any element of $\operatorname{coker}\left(\ell_{1} f\right) \times_{\operatorname{coker}\left(\ell_{2} \ell_{1} f\right)} \operatorname{coker}\left(r_{1} f\right)$ is a coset of the form

$$
\left(S_{L}, S_{R}\right):=\left(\lambda+\operatorname{im}\left(\ell_{1} f\right), \rho+\operatorname{im}\left(r_{1} f\right)\right)
$$

for some $\lambda \in L$ and $\rho \in R$ such that $\ell_{2}^{*}\left(S_{L}\right)=r_{2}^{*}\left(S_{R}\right)$. Thus the coset $(\lambda, \rho)+\operatorname{im} f \in \operatorname{coker} f$ maps to ( $S_{L}, S_{R}$ ), which proves $u$ is an epimorphism.
Qed.
4.60. Theorem. Suppose $F$ is an Abelian presheaf on a site ( $\mathrm{C}, J$ ) where $J$ is a finitely generated Grothendieck topology. If $F$ is flasque and separated, then $H^{0}(-, F): \mathrm{C}^{\mathrm{op}} \rightarrow \mathrm{A}$ is lavish with respect to $J$.

Proof. Since $F$ is separated, a single application of the plus construction amounts to sheafification. With this in mind, for any cover $\left(U_{i} \rightarrow X\right)_{i \in I}$ of $X$ in $J$ one has

$$
\begin{aligned}
& H^{0}(X, F)=\operatorname{coker}\left(F X \xrightarrow{\eta_{F_{X}}} F^{+} X\right) \\
& \cong \operatorname{coker}\left(F X \xrightarrow{\eta_{F_{X}}} \operatorname{ker}\left(\prod_{i} F^{+} U_{i} \xrightarrow{p-q} \prod_{i, j} F^{+} U_{i, j}\right)\right) \\
& \left.\rightarrow \operatorname{ker}\left(\operatorname{coker}\left(F X \rightarrow \prod_{i} F^{+} U_{i}\right) \rightarrow \operatorname{coker}\left(F X \rightarrow \prod_{i, j} F^{+} U_{i, j}\right)\right)\right) \\
& \left.=\operatorname{ker}\left(\operatorname{coker}\left(\prod_{i}\left(F X \rightarrow F^{+} U_{i}\right)\right) \rightarrow \operatorname{coker}\left(\prod_{i, j}\left(F X \rightarrow F^{+} U_{i, j}\right)\right)\right)\right)
\end{aligned}
$$

( $F^{+}$is a sheaf)
which, since colimits commute with each other, since finite products and finite coproducts agree in Abelian categories and since the covers in $J$ are finitely generated (see Paragraph 3.36), yields

$$
\begin{aligned}
& \left.=\operatorname{ker}\left(\prod_{i} \operatorname{coker}\left(F X \rightarrow F^{+} U_{i}\right) \rightarrow \prod_{i, j} \operatorname{coker}\left(F X \rightarrow F^{+} U_{i, j}\right)\right)\right) \\
& \left.=\operatorname{ker}\left(\prod_{i} \operatorname{coker}\left(F X \rightarrow F U_{i} \rightarrow F^{+} U_{i}\right) \rightarrow \prod_{i, j} \operatorname{coker}\left(F X \rightarrow F U_{i, j} \rightarrow F^{+} U_{i, j}\right)\right)\right) \quad(\eta \text { is natural }) \\
& \left.\cong \operatorname{ker}\left(\prod_{i} \operatorname{coker}\left(F U_{i} \rightarrow F^{+} U_{i}\right) \rightarrow \prod_{i, j} \operatorname{coker}\left(F U_{i, j} \rightarrow F^{+} U_{i, j}\right)\right)\right) \quad(F \text { is flasque }) \\
& =\operatorname{ker}\left(\prod_{i} H^{0}\left(U_{i}, F\right) \rightarrow \prod_{i, j} H^{0}\left(U_{i, j}, F\right)\right) \quad \text { (Theorem 4.19). }
\end{aligned}
$$

## Qed.

4.61. Although none of the problems that we saw so far are flasque, we will show in the next section that there is a functorial construction that sends any presheaf to a flasque and separated presheaf that records relevant combinatorial information and this construction can be directly applied to the old VertexCover, CycleCover and BipartiteCover problems - as well as any problems that can be represented by presheaves on $\operatorname{Sub}(G)$.

## 5 Model collecting

5.1. In this section, instead of considering the obstructions to "algorithmic compositionality" (i.e. obstructions to being a sheaf), we will focus on identifying suitable abstract language to speak about obstructions to having any solution at all. Given a presheaf $F$ that describes a computational problem, we will define another presheaf $\mathfrak{M} F$ which will send any object $H$ to the set

$$
\left\{H^{\prime} \subseteq H \mid F\left(H^{\prime}\right) \neq \emptyset\right\}
$$

of all subgraphs of $H$ such that which are yes-instances for $F$-Decision. In a way, $\mathfrak{M} F(H)$ can be thought of as collecting all the subgraphs of $H$ that are models ${ }^{9}$ for $F$. The rest of this section is devoted to the proof of the following fact.
5.2. Theorem. There exists a covariant functor $\mathfrak{M}$, called the model collecting functor, that maps any presheaf $F: \mathrm{C}^{\mathrm{op}} \rightarrow$ Set, where C is a category with pullbacks, to a flasque presheaf $\mathfrak{M} F$. Moreover, if $\mathrm{C}=\operatorname{Sub}(G)$ and the complete graph with two vertices has a solution for $F$, then

- $H^{0}(X, \mathfrak{M} F)=\mathbb{Z}\left[\left\{X^{\prime} \subseteq X: F\left(X^{\prime}\right)=\emptyset\right\}\right]$;
- $F X \neq \emptyset$ iff $H^{0}(X, \mathfrak{M} F)=0$.
5.3. The above result tells us we can use cohomology to decide if a graph $X$ has a solution for a certain problem $F$. For example consider König's Theorem which states that a bipartite graph $X$ admits a matching of size greater than $k$ if and only if $X$ has no vertex cover with size at most $k$. This theorem can be restated in terms of the zeroth presheaf cohomology of the model collecting functor, as follows.
5.4. Theorem (König's Theorem, Cohomologically). If $X$ is a bipartite graph, then

$$
H^{0}\left(X, \mathfrak{M} \mathcal{V}_{\leq k}\right)=\{\text { matchings of } X \text { of size greater than } k\}
$$

5.5. Although we don't provide an algebraic proof of König's Theorem, the above result points to the fact that cohomological methods provide a possible avenue towards stating and proving results in extremal graph theory. However, this is beyond the scope of the present paper and we leave it as future work.

[^7]
## Proof of Theorem 5.2

5.6. Given a presheaf $F: \mathrm{C}^{\mathrm{op}} \rightarrow$ Set, we define

$$
\begin{array}{rlcc}
\mathfrak{M} F: & \mathrm{C}^{\text {op }} & \longrightarrow & \text { Set } \\
C & \longmapsto & \left\{C^{\prime} \hookrightarrow C: F\left(C^{\prime}\right) \neq \emptyset\right\}
\end{array}
$$

and given $f: C \hookrightarrow D$, we put

$$
\begin{aligned}
\mathfrak{M} F(f): \mathfrak{M} F(D) & \longrightarrow \mathfrak{M} F(C) \\
D^{\prime} & \longmapsto D^{\prime} \times_{D} C
\end{aligned}
$$

where $D^{\prime} \times_{D} C$ is the pullback of $D^{\prime} \hookrightarrow D$ and $C \hookrightarrow D$ in the category C .
5.7. Lemma. $\mathfrak{M}: \operatorname{Psh}(\mathrm{C}) \rightarrow \operatorname{Psh}(\mathrm{C})$ ) is a covariant functor.

Proof. Given $\alpha: F \Rightarrow L$ a natural transformation between two functors $F, L: \mathrm{C}^{\mathrm{op}} \rightarrow$ Set, we can define a natural transformation $\mathfrak{M}(\alpha): \mathfrak{M} F \rightarrow \mathfrak{M} L$ that acts as an identity, since, given $C^{\prime} \in \mathfrak{M} F(C)$, we have an arrow $\alpha_{C^{\prime}}: F\left(C^{\prime}\right) \rightarrow L\left(C^{\prime}\right)$ with $F\left(C^{\prime}\right) \neq \emptyset$, so that $C^{\prime} \in \mathfrak{M} L(C)$ and $\mathfrak{M}(\alpha)$ is then well defined. With this definition, the property of naturality of $\mathfrak{M}(\alpha)$ and the property of $\mathfrak{M}$ being a functor follow easily. Qed.
5.8. Lemma. For every presheaf $F: C^{\circ p} \rightarrow$ Set, $\mathfrak{M} F$ is also a presheaf.

Proof. We define the above construction with a property $\mathbb{P}$ defined as follows: $C$ is an object of $\mathbb{P}$ iff $F(C) \neq \emptyset$. We then consider the functor

$$
\begin{aligned}
\mathrm{C}_{\mathbb{P}}: \mathrm{C}^{\mathrm{op}} & \longrightarrow \quad \text { Set } \\
C & \longmapsto\left\{C^{\prime} \hookrightarrow C: C^{\prime} \in \mathbb{P}\right\}
\end{aligned}
$$

and given $f: C \hookrightarrow D$, we put

$$
\begin{aligned}
\mathrm{C}_{\mathbb{P}}(f): \quad \mathrm{C}_{\mathbb{P}}(D) & \longrightarrow \mathrm{C}_{\mathbb{P}}(C) \\
D^{\prime} & \longmapsto D^{\prime} \times_{D} C
\end{aligned}
$$

Now, $p: \mathbb{P} \hookrightarrow C$ pullback-absorbing because if
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-32.jpg?height=186&width=334&top_left_y=1959&top_left_x=898)
is a pullback in C , then
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-32.jpg?height=185&width=446&top_left_y=2230&top_left_x=837)
is a diagram in Set. Since $F(X) \neq \emptyset$ and we have an arrow $F(X) \rightarrow F\left(X \times_{Y} Z\right)$, we have that $F\left(X \times_{Y} Z\right) \neq \emptyset$, so that $X \times_{Y} Z$ is an object of $\mathbb{P}$.
We have that $\mathrm{C}_{\mathbb{P}}$ is well defined on the arrows because $p$ is pullback-absorbing. Also, it is a functor, because if $C \hookrightarrow D \hookrightarrow E$ and
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-33.jpg?height=177&width=369&top_left_y=472&top_left_x=635)
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-33.jpg?height=177&width=286&top_left_y=472&top_left_x=1203)
are pullbacks, then the bigger square
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-33.jpg?height=316&width=375&top_left_y=769&top_left_x=876)
is a pullback, which means that the following commutes
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-33.jpg?height=119&width=566&top_left_y=1203&top_left_x=777)

And since $C^{\prime} \times_{C} C \cong C^{\prime}$, for $C^{\prime} \hookrightarrow C$, we also have that $\mathrm{C}_{\mathbb{P}}\left(i d_{C}\right)=i d_{\mathrm{C}_{\mathbb{P}}(C)}$.
Qed.
5.9. Lemma. If we denote by $\operatorname{FPSh}(\mathrm{C})$ the category of flasque presheaves, then $\mathfrak{M}$ factors through FPSh(C), i.e., the following diagram commutes.
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-33.jpg?height=201&width=639&top_left_y=1624&top_left_x=743)

Proof. We need to check that, for every $f: C \rightarrow D, \mathfrak{M} F(f)$ is surjective. Given $C^{\prime} \in \mathfrak{M} F(C)$, ie, $C^{\prime} \xrightarrow{g} C$ such that $F\left(C^{\prime}\right) \neq \emptyset$, we have
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-33.jpg?height=181&width=231&top_left_y=1970&top_left_x=953)
so that we have an arrow $C^{\prime} \rightarrow D$ with $F\left(C^{\prime}\right) \neq \emptyset$. Hence, $C^{\prime} \in \mathfrak{M} F(D)$ and $\mathfrak{M} F(f)\left(C^{\prime}\right)=C^{\prime}$
Qed.
5.10. Lemma. If we denote by $\operatorname{SPsh}(\mathrm{C})$ the category of separated presheaves, then, when $\mathrm{C}=\operatorname{Sub}(G)$, we have that $\mathfrak{M}$ factors through SPsh(C), i.e., the following diagram commutes.
![](https://cdn.mathpix.com/cropped/473f3197-aa41-426e-9835-037974053621-34.jpg?height=194&width=912&top_left_y=380&top_left_x=605)

Proof. We note that to prove Lemma 4.33 we didn't use the properties $\mathbb{P}_{1}$ and $\mathbb{P}_{2}$, only the topology defined in $\operatorname{Sub}(G)$ and the fact that elements of $\operatorname{Sub}_{\mathbb{P}_{1,2}}(H)$ are subgraphs of $H$, so we can use the same argument to prove that $\mathrm{C}_{\mathbb{P}}$ is a separated presheaf when $\mathrm{C}=\operatorname{Sub}(G)$.
Qed.
5.11. Now, we wish to look at the zeroth presheaf Čech cohomology for $\mathfrak{M} F$ in the case where $\mathrm{C}=\operatorname{Sub}(G)$. Again, since $\mathfrak{M} F$ is a separated presheaf, we can use Theorem 4.19 to characterize $H^{0}(X, \mathfrak{M} F)$ as the quotient $\mathfrak{M} F^{+} / \mathfrak{M} F$. So the next step will be to describe the sheafification of $\mathfrak{M} F$.
5.12. Proposition. Suppose $F: \operatorname{Sub}(G)^{\text {op }} \rightarrow$ Set is a presheaf such that $F\left(K_{2}\right) \neq \emptyset$, i.e., the complete graph with two vertices has a solution for $F$, then $(\mathfrak{M} F)^{+}=\operatorname{Sub}(-)$.

Proof. Given $H \subseteq G$, a cover $\bigcup_{i \in I} H_{i}=H$ and $\left\{H_{i}^{\prime} \in \mathfrak{M} F\left(H_{i}\right)\right\}_{i \in I}$ a matching family, we have $\bigcup_{i \in I} H_{i}^{\prime} \in \operatorname{Sub}(H)$. Furthermore, given an edge $\alpha=K \in E(H)$, if we consider $f: K \hookrightarrow H$, we have

$$
\operatorname{Sub}(f)\left(H^{\prime}\right)=H^{\prime} \cap K, \forall H^{\prime} \in \operatorname{Sub}(H) .
$$

Now, because $K \cong K_{2}$, by hypothesis we have $F(K) \neq \emptyset$. Since $H^{\prime} \cap K \hookrightarrow K$ and the function $F(K) \rightarrow F\left(H^{\prime} \cap K\right)$ is in Set, we have $F\left(H^{\prime} \cap K\right) \neq \emptyset$, so that $\operatorname{Sub}(f)\left(H^{\prime}\right) \in \mathfrak{M} F(H)$. By Proposition 4.11, we have that $\operatorname{Sub}(-)$ is the sheafification of $\mathfrak{M} F$, whenever $F\left(K_{2}\right) \neq \emptyset$.
Qed.
5.13. Note that the hypothesis $F\left(K_{2}\right) \neq 0$ is verified by all the problems we have been working on so far. Thus, the next two characterizations of $H^{0}(-, \mathfrak{M} F)$ can be applied when $F$ describes the problems of VertexCover, CycleCover and BipartiteCover.
5.14. Proposition. If $F\left(K_{2}\right) \neq \emptyset$, then $H^{0}(X, \mathfrak{M} F)=\mathbb{Z}\left[\left\{X^{\prime} \subseteq X: F\left(X^{\prime}\right)=\emptyset\right\}\right]$.

Proof. We fix a cover $\mathcal{U}=\left\{X_{i}\right\}_{i \leq m} \in \operatorname{Cov}(X)$ and we consider $f_{X}: \mathcal{V}_{\leq k}(X) \rightarrow \mathcal{V}(X)$ given by

$$
\mathfrak{M} F(X) \xrightarrow{\xi_{\mathcal{U}}} \operatorname{Match}(\mathcal{U}, \mathfrak{M} F) \hookrightarrow \coprod_{\mathcal{U} \in \operatorname{Cov}(X)} \operatorname{Match}(\mathcal{U}, \mathfrak{M} F) \xrightarrow{\pi} \mathfrak{M} F^{+}(X) \cong \operatorname{Sub}(X)
$$

As it was the case for VertexCover and CycleCover in Proposition 4.24 and Proposition 4.47, we have that $f_{X}$ can be seen as the inclusion $f_{X}: \mathfrak{M} F(X) \hookrightarrow \operatorname{Sub}(X)$.
Defining $Y=\operatorname{Sub}(X)$ and $B=\mathfrak{M} F(X)$, we have that

$$
\mathbb{Z}[Y-B]=\mathbb{Z}\left[\left\{X^{\prime} \subseteq X: F\left(X^{\prime}\right)=\emptyset\right\}\right]
$$

We then use Theorem 4.19 and Lemma 4.21 to obtain the desired result.
Qed.
5.15. We now have a characterization the helps us proving the main result of this section.
5.16. Theorem. $F X \neq \emptyset$ iff $H^{0}(X, \mathfrak{M} F)=0$, whenever $F\left(K_{2}\right) \neq \emptyset$.

Proof. Using Proposition 5.14 we only need to prove that

$$
F X \neq \emptyset \Longleftrightarrow \forall X^{\prime} \subseteq X, F X^{\prime} \neq \emptyset
$$

The ( $\Leftarrow$ ) direction is trivial, since $X \subseteq X$. To check ( $\Rightarrow$ ), we note that if $X^{\prime} \subseteq X$ then we have the restriction function $F X \rightarrow F X^{\prime}$ in Set with $F X \neq \emptyset$, which implies that $F X^{\prime} \neq \emptyset$.
Qed.

## 6 Discussion \& Future Work

6.1. This work takes a first step toward applying cohomological tools to the study of obstructions in algorithmics and combinatorics. Building on prior work [2] that interprets dynamic programming as a sheaf condition - that is, the ability to assemble global solutions from compatible local ones - we model computational problems as functors, or presheaves, assigning sets of certificates to input instances. Within this categorical framework, we show that two key types of algorithmic obstructions - failures of solution existence and failures of compositionality - can be naturally detected and expressed via Čech cohomology. In particular, the zeroth cohomology group captures the emergence of global inconsistencies not visible at the local level.
6.2. By adapting Čech cohomology to preshaves, our work illustrates how existing cohomological methods can be meaningfully applied to classical algorithmic problems. We explore this perspective in detail through three concrete cases - VertexCover, CycleCover, and OddCycleTransversal - and show how their structural obstructions manifest cohomologically. Although our examples are specific, the approach generalizes to a broader class of problems involving monotone graph properties, suggesting wider applicability. These observations invite further exploration at the intersection of topology, category theory, and algorithm design.
6.3. Looking ahead, a natural next step is to investigate the role of higher Čech cohomology groups in detecting more subtle obstructions within computational problems. Higher cohomology is defined in the usual way, as $H^{n}(X, \mathcal{U}, F)=\operatorname{coker}\left(\operatorname{im}\left(\delta^{n-1}\right) \rightarrow \operatorname{ker}\left(\delta^{n}\right)\right)$. To explore the potential of higher cohomology in this setting, one can construct a short exact sequence of presheaves

$$
0 \rightarrow \mathcal{V}_{\leq k} \hookrightarrow \mathscr{C}_{\leq k} \rightarrow \mathscr{C}_{\leq k} / \mathcal{V}_{\leq k} \rightarrow 0
$$

relating the problems studied in this paper. This induces a long exact sequence of cohomology functors as usual. However, when cohomology is computed by freely Abelianizing these set-valued presheaves, the connecting map

$$
H^{0}\left(-, \mathscr{C}_{\leq k} / \mathcal{V}_{\leq k}\right) \rightarrow H^{1}\left(-, \mathcal{V}_{\leq k}\right)
$$

is trivial - again suggesting that deeper insights may require defining computational problems directly as presheaves valued in an Abelian category.

## References

[1] Alon, N. Splitting necklaces. Advances in Mathematics 63, 3 (1987), 247-253.
[2] Althaus, E., Bumpus, B. M., Fairbanks, J., and Rosiak, D. Compositional algorithms on compositional data: Deciding sheaves on presheaves. arXiv preprint arXiv:2302.05575(2023).
[3] Baez, J. C., and Courser, K. Structured cospans. Theory and Applications of Categories 35, 48 (2020), 1771-1822.
[4] Baez, J. C., and Master, J. Open petri nets. Mathematical Structures in Computer Science 30, 3 (2020), 314-341.
[5] Bumpus, B. M., Kocsis, Z. A., and Master, J. E. Structured Decompositions: Structural and Algorithmic Compositionality. arXiv preprint arXiv:2207.06091 (2022).
[6] Chaudhuri, A., Köhl, R., and Wolkenhauer, O. A mathematical framework to study organising principles in graphical representations of biochemical processes. arXiv preprint arXiv:2410.18024 (2024).
[7] Cygan, M., Fomin, F. V., Kowalik, Ł., Lokshtanov, D., Marx, D., Pilipczuk, M., Pilipczuk, M., and Saurabh, S. Parameterized algorithms. Springer, 2015. ISBN:978-3-319-21275-3.
[8] De Longueville, M. A course in topological combinatorics. Springer Science \& Business Media, 2013.
[9] Dinur, I. The PCP theorem by gap amplification. In Proc. 38th ACM Symp. on Theory of Computing (2006), pp. 241-250.
[10] Downey, R. G., and Fellows, M. R. Parameterized complexity. Springer Science \& Business Media, 2012.
[11] Downey, R. G., Fellows, M. R., et al. Fundamentals of parameterized complexity, vol. 4. Springer, 2013. ISBN:978-1-4471-5558-4.
[12] Estivill-Castro, V., Fellows, M., Langston, M., and Rosamond, F. FPT is P-time extremal structure I. Proc. 1st ACiD (2005).
[13] Felber, S., Flores, B. H., and Galeana, H. R. A sheaf-theoretic characterization of tasks in distributed systems. arXiv preprint arXiv:2503.02556 (2025).
[14] Filakovský, M., Nakajima, T.-V., Opršal, J., Tasinato, G., and Wagner, U. Hardness of Linearly Ordered 4-Colouring of 3-Colourable 3-Uniform Hypergraphs. In 41st International Symposium on Theoretical Aspects of Computer Science (STACS 2024) (Dagstuhl, Germany, 2024), O. Beyersdorff, M. M. Kanté, O. Kupferman, and D. Lokshtanov, Eds., vol. 289 of Leibniz International Proceedings in Informatics (LIPIcs), Schloss Dagstuhl - Leibniz-Zentrum für Informatik, pp. 34:1-34:19.
[15] Flum, J., and Grohe, M. Parameterized Complexity Theory. Texts Theoret. Comput. Sci. EATCS Ser, 2006. ISBN:978-3-540-29952-3.
[16] Fong, B. Decorated cospans. Theory and Applications of Categories 30 (2015), 1096-1120.
[17] Gallier, J., and Quaintance, J. Homology, Cohomology, and Sheaf Cohomology for Algebraic Topology, Algebraic Geometry, and Differential Geometry. WORLD SCIENTIFIC, 2022.
[18] Jackson, A. As if summoned from the void: the life of alexandre grothendieck (parts i,ii). Notices of the American Mathematical Society $51(9,10)(2004)$.
[19] Krokhin, A., Opršal, J., Wrochna, M., and Živný, S. Topology and adjunction in promise constraint satisfaction. SIAM Journal on Computing 52, 1 (2023), 38-79.
[20] Lovász, L. Kneser's conjecture, chromatic number, and homotopy. Journal of Combinatorial Theory, Series A 25, 3 (1978), 319-324.
[21] Malcolm, G. Sheaves, objects, and distributed systems. Electronic Notes in Theoretical Computer Science 225 (2009), 3-19.
[22] Matoušek, J., Buörner, A., and Ziegler, G. M. Using the Borsuk-Ulam theorem: lectures on topological methods in combinatorics and geometry. Springer, 2003.
[23] Mazza, D. Towards a sheaf-theoretic definition of decision problems. 2019.
[24] Meyer, S., and Opršal, J. A topological proof of the Hell-Nešetřil dichotomy. Society for Industrial and Applied Mathematics, Jan. 2025, p. 4507-4519.
[25] Mitchell, B. The full imbedding theorem. American Journal of Mathematics 86, 3 (1964), 619-637.
[26] Ó Conghaile, A. Cohomology in Constraint Satisfaction and Structure Isomorphism. In 47th International Symposium on Mathematical Foundations of Computer Science (MFCS 2022) (Dagstuhl, Germany, 2022), S. Szeider, R. Ganian, and A. Silva, Eds., vol. 241 of Leibniz International Proceedings in Informatics (LIPIcs), Schloss Dagstuhl - Leibniz-Zentrum für Informatik, pp. 75:1-75:16.
[27] Puca, C., Hadzihasanovic, A., Genovese, F., and Coecke, B. Obstructions to compositionality. arXiv preprint arXiv:2307.14461 (2023).
[28] Riehl, E. Category theory in context. Courier Dover Publications, 2017. ISBN:048680903X.
[29] Rosiak, D. Sheaf Theory through Examples. The MIT Press, 102022.
[30] Scoville, N. A. Discrete Morse Theory, vol. 90. American Mathematical Soc., 2019.


[^0]:    ${ }^{1}$ The class of Fixed-Parameter Tractable problems which are solvable by algorithms that are exponential only in the size of a fixed parameter while polynomial in the size of the input.

[^1]:    ${ }^{2}$ The talk was held at the Institute for Advanced Study in Princeton and sheaves are mentioned roughly at minute 4:10.

[^2]:    ${ }^{3}$ For the reader knowledgeable in sheaf theory, one can generalize this algorithm for sufficiently well-behaved categories equipped with a subcanonical topology, as long as the data assignment is compositional, i.e., a sheaf.

[^3]:    ${ }^{4} \mathrm{~A}$ monomorphism of graphs is a homomorphism of graphs witnessing the inclusion of subgraph, i.e. injective on vertices and edges.

[^4]:    ${ }^{5}$ The reader knowledgeable in sheaf theory should be able to imagine how the story goes when one replaces $\operatorname{Sub}(G)$ with another suitable site.

[^5]:    ${ }^{6}$ What we call lavish presheaves are often referred to as epi-presheaves. We find this terminology confusing since flasque presheaves (i.e. presheaves whose restriction maps are epic) could also be deserving of the name "epi-presheaf". To mitigate any source of confusion, we stray from any use of this term by sticking to "lavish" and "flasque". Furthermore, and this is part of the moral of the present paper, lavish presheaves deserve their own name since they are in many respects just as important as their separated counterpart.

[^6]:    ${ }^{7}$ The reader familiar with standard treatments of Čech cohomology might expect $H^{0}(X, F)$ to be the global sections of $F$ whenever $F$ is a sheaf. However, under the constrution we are considering here, since the domain of $\delta_{\mathcal{U}}^{-1}$ is $F(H), H^{0}(X, F)$ measures the difference between matching families ( $\operatorname{ker} \delta^{0}$ ) and the global sections: thus it is trivial if $F$ is a sheaf. Note that there are no differences between our approach and the standard one for higher cohomology objects.
    ${ }^{8}$ Recall that a sieve on an object $X$ is finitely generated if it can be generated by pre-composition starting with a family of morphisms $\left(U_{i} \rightarrow X\right)_{i \in I}$ indexed by a finite family $I$.

[^7]:    ${ }^{9}$ Our motivation for this terminology is the idea that when we have a formula $p$ describing a property in the logic of graphs, we can consider the set $\left\{G^{\prime} \hookrightarrow G: G^{\prime} \vDash p\right\}$ which will be the models for $p$.

