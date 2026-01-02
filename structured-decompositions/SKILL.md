---
name: structured-decompositions
description: "AlgebraicJulia/StructuredDecompositions.jl with complete Bumpus corpus, mathpix-gem paper processing, and Narya structured diffs for every interaction"
license: MIT
metadata:
  source: AlgebraicJulia/StructuredDecompositions.jl
  deepwiki: https://deepwiki.com/AlgebraicJulia/StructuredDecompositions.jl
  trit: -1
  color: "#9400D3"
  gf3_conserved: true
  version: 3.0.0
  julia_compat: "≥1.10"
---

# Structured Decompositions Skill

> **Trit**: -1 (MINUS - Validator)  
> **Color**: #9400D3 (Violet)  
> **Principle**: Category-theoretic tree decompositions for FPT algorithms  
> **Foundation**: AlgebraicJulia + Bumpus Corpus + Mathpix OCR

## Denotation

> **Structured decompositions map compositional data to compositional algorithms, yielding FPT decidability via sheaf conditions on adhesive categories.**

The skill reaches a **fixed point** when:
1. All bags satisfy local sheaf conditions
2. Adhesions verify pullback compatibility
3. GF(3) conservation holds across decomposition width

## Mathematical Foundations

> **DeepWiki Reference**: [Mathematical Foundations](https://deepwiki.com/AlgebraicJulia/StructuredDecompositions.jl/2.3-mathematical-foundations)

### Three Interconnected Theories

| Theory | Module | Purpose |
|--------|--------|---------|
| **Structured Decomposition** | `Decompositions` | Generalizes tree decompositions to arbitrary objects |
| **Functorial Lifting** | `FunctorUtils` | Lifts computational problems to decomposed structures |
| **Sheaf-Theoretic Decision** | `DecidingSheaves` | Encodes problems as sheaves, solves via cohomology |

### Classical → General Progression

```
Classical Tree Decomposition (graphs only)
    ↓ category-theoretic generalization
Structured Decomposition (arbitrary objects)
    ↓ functorial lifting
Problem Encoding as Sheaf
    ↓ cohomological decision
FPT Algorithm (O(f(width)·poly(n)))
```

### Sheaf Structure Over Decomposition

- **Base Space**: The decomposition tree structure
- **Stalks**: Solution spaces for individual bags
- **Restriction Maps**: Consistency constraints between overlapping bags
- **Global Sections**: Valid solutions to the entire problem

A decision problem has a solution iff there exists a **global section** (consistent choice of local solutions).

## Formal Contract

```
Effect: StrDecomp × Sheaf → Decision × Witness
Invariant: ∀ adhesion: pullback(bag_i, bag_j) = adhesion
Complexity: O(f(width) × n) where width = max |adhesion|
Denotation: ⟦SD⟧ = colim_{∫G} (bags ⊔_adhesions)
```

### FPT Algorithm Pipeline

| Step | Module | Complexity |
|------|--------|------------|
| 1. Compute decomposition of width k | Decompositions | poly(n) |
| 2. Encode problem as sheaf | DecidingSheaves | O(1) |
| 3. Solve locally at each bag | DecidingSheaves | exp(k) |
| 4. Check global consistency via gluing | DecidingSheaves | poly(n) |
| **Total** | | **O(f(k)·poly(n))** |

---

## Complete Bumpus Corpus (20 Papers)

### Primary Implementation Papers

| # | Paper | arXiv | Year | Citations |
|---|-------|-------|------|-----------|
| 1 | **Structured Decompositions: Structural and Algorithmic Compositionality** | [2207.06091](https://arxiv.org/abs/2207.06091) | 2022 | 11 |
| 2 | **Compositional Algorithms on Compositional Data: Deciding Sheaves on Presheaves** | [2302.05575](https://arxiv.org/abs/2302.05575) | 2023 | 7 |
| 3 | **Spined Categories: Generalizing Tree-Width Beyond Graphs** | [2104.01841](https://arxiv.org/abs/2104.01841) | 2021 | 6 |

### Temporal and Time-Varying Data

| # | Paper | arXiv | Year | Citations |
|---|-------|-------|------|-----------|
| 4 | **Towards a Unified Theory of Time-Varying Data** | [2402.00206](https://arxiv.org/abs/2402.00206) | 2024 | 2 |
| 5 | **Pushing Tree Decompositions Forward Along Graph Homomorphisms** | [2408.15184](https://arxiv.org/abs/2408.15184) | 2024 | 2 |
| 6 | **Failures of Compositionality: Cohomology, Sheafification and Lavish Presheaves** | [2407.03488](https://arxiv.org/abs/2407.03488) | 2024 | 1 |

### Graph Theory and Algorithms

| # | Paper | arXiv | Year | Citations |
|---|-------|-------|------|-----------|
| 7 | **Edge Exploration of Temporal Graphs** | Algorithmica 85(3) | 2023 | 57 |
| 8 | **Directed Branch-Width: A Directed Analogue of Tree-Width** | [2009.08903](https://arxiv.org/abs/2009.08903) | 2020 | 12 |
| 9 | **Search-Space Reduction via Essential Vertices** | SIAM J. Discrete Math 38(3) | 2024 | 6 |
| 10 | **Generalizing Graph Decompositions** | PhD Thesis, Glasgow | 2021 | 7 |

### Category Theory and Logic

| # | Paper | arXiv | Year | Citations |
|---|-------|-------|------|-----------|
| 11 | **Degree of Satisfiability in Heyting Algebras** | J. Symbolic Logic 90(2) | 2025 | 3 |
| 12 | **How Nice is this Functor? Two Squares and Some Homology** | ACT 2024 | 2024 | 1 |
| 13 | **Treewidth via Spined Categories** | [2105.05372](https://arxiv.org/abs/2105.05372) | 2021 | 1 |

### Applied Category Theory

| # | Paper | arXiv | Year | Citations |
|---|-------|-------|------|-----------|
| 14 | **Additive Invariants of Open Petri Nets** | Compositionality 7 | 2025 | 1 |
| 15 | **FPT Certified Algorithms for Covering/Dominating in Planar Graphs** | SWAT 2024 | 2024 | 1 |
| 16 | **A Constraint Model for Tree Decomposition** | [1908.02530](https://arxiv.org/abs/1908.02530) | 2019 | - |
| 17 | **Interval-Membership-Width: DP on Temporal Graphs** | TGSA Book Ch. 3.2 | - | - |

### Collaborator Network

```
Benjamin Merlin Bumpus (USP)
├── Kitty Meeks (Glasgow) - temporal graphs
├── Zoltan A. Kocsis (CSIRO) - spined categories
├── Bart M. P. Jansen (TU/e) - parameterized complexity
├── William Pettersson (Glasgow) - branch-width
├── Jade Master (Strathclyde) - structured decomps
├── James Fairbanks (UF) - AlgebraicJulia
├── Daniel Rosiak - sheaves on presheaves
└── Sophie Libkind - Petri nets
```

---

## Mathpix-Gem Paper Processing

### Configuration

Requires Mathpix API credentials (user must configure):

```ruby
# ~/.mathpix/config or environment variables
# MATHPIX_APP_ID=your_app_id
# MATHPIX_APP_KEY=your_app_key

require 'mathpix'

Mathpix.configure do |config|
  config.app_id = ENV['MATHPIX_APP_ID']
  config.app_key = ENV['MATHPIX_APP_KEY']
  config.timeout = 60
end
```

### Extract LaTeX from Bumpus Papers

```ruby
#!/usr/bin/env ruby
# extract_bumpus_corpus.rb

require 'mathpix'

BUMPUS_PAPERS = [
  { arxiv: "2207.06091", name: "structured_decompositions" },
  { arxiv: "2302.05575", name: "compositional_algorithms" },
  { arxiv: "2104.01841", name: "spined_categories" },
  { arxiv: "2402.00206", name: "time_varying_data" },
  { arxiv: "2408.15184", name: "pushing_tree_decomps" },
  { arxiv: "2407.03488", name: "failures_compositionality" },
]

def process_paper(arxiv_id, name)
  pdf_url = "https://arxiv.org/pdf/#{arxiv_id}.pdf"
  
  conversion = Mathpix
    .document(pdf_url)
    .with_formats(:markdown, :latex)
    .with_tables(include_table_html: true)
    .with_diagrams
    .convert
  
  puts "Processing #{name}..."
  conversion.wait_until_complete(max_wait: 900, poll_interval: 5.0)
  
  result = conversion.result
  
  # Save outputs
  File.write("papers/#{name}.md", result.markdown)
  File.write("papers/#{name}.tex", result.latex)
  
  # Extract equations
  equations = result.equations.map { |eq| eq['latex'] }
  File.write("papers/#{name}_equations.txt", equations.join("\n\n"))
  
  { name: name, page_count: result.page_count, equations: equations.count }
end

# Process all papers
BUMPUS_PAPERS.each do |paper|
  stats = process_paper(paper[:arxiv], paper[:name])
  puts "✓ #{stats[:name]}: #{stats[:page_count]} pages, #{stats[:equations]} equations"
end
```

### Batch Equation Extraction

```ruby
# Extract all diagrams from Bumpus papers
diagrams = Dir['papers/*.pdf'].flat_map do |pdf|
  conversion = Mathpix.document(pdf).with_diagrams.convert
  conversion.wait_until_complete
  conversion.result.diagrams
end

# Color-code by paper using Gay.jl seed
require 'digest'
diagrams.each_with_index do |diag, idx|
  seed = 1069 ^ Digest::SHA256.hexdigest(diag['source']).to_i(16)
  diag[:trit] = seed % 3 - 1  # -1, 0, or +1
  diag[:color] = gay_color(seed)
end
```

---

## Narya Structured Diff Templates

### Every Interaction Has a Diff

```python
@dataclass
class NaryaDiff:
    """Structured diff for every StructuredDecompositions operation."""
    
    # Core fields
    before: Any           # State before operation
    after: Any            # State after operation
    delta: Dict[str, Any] # Change description
    
    # Metadata
    birth: str            # Initial condition
    impact: int           # 1 if equivalence class changed, else 0
    trit: int             # -1, 0, or +1
    
    # Verification
    sheaf_condition: bool # Did adhesions satisfy pullback?
    width_bounded: bool   # Is width within FPT threshold?
    gf3_conserved: bool   # Sum of trits ≡ 0 (mod 3)?
```

### Diff Template: Decomposition Creation

```python
def diff_create_decomposition(graph: Graph) -> NaryaDiff:
    """Narya diff for creating a structured decomposition."""
    
    before = {
        "graph": graph,
        "decomposition": None,
        "bags": [],
        "adhesions": []
    }
    
    decomp = StrDecomp(graph)
    
    after = {
        "graph": graph,
        "decomposition": decomp,
        "bags": bags(decomp),
        "adhesions": adhesions(decomp)
    }
    
    return NaryaDiff(
        before=before,
        after=after,
        delta={
            "operation": "create_decomposition",
            "bag_count": len(bags(decomp)),
            "adhesion_count": len(adhesions(decomp)),
            "width": max(len(a) for a in adhesions(decomp)),
            "shape": "tree" if is_tree(decomp.shape) else "dag"
        },
        birth="empty_decomposition",
        impact=1,  # Always impacts: new structure created
        trit=-1,   # Creation is MINUS (consumption of graph)
        sheaf_condition=True,  # By construction
        width_bounded=max_width(decomp) <= WIDTH_THRESHOLD,
        gf3_conserved=True  # Single operation
    )
```

### Diff Template: Sheaf Decision

```python
def diff_decide_sheaf(sheaf: Functor, decomp: StrDecomp) -> NaryaDiff:
    """Narya diff for deciding sheaf satisfiability."""
    
    before = {
        "sheaf": sheaf,
        "decomposition": decomp,
        "local_solutions": None,
        "decision": None
    }
    
    # Run FPT algorithm
    answer, witness = decide_sheaf_tree_shape(sheaf, decomp)
    local_solutions = [sheaf(bag) for bag in bags(decomp)]
    
    after = {
        "sheaf": sheaf,
        "decomposition": decomp,
        "local_solutions": local_solutions,
        "decision": answer,
        "witness": witness
    }
    
    return NaryaDiff(
        before=before,
        after=after,
        delta={
            "operation": "decide_sheaf",
            "satisfiable": answer,
            "witness_size": len(witness) if witness else 0,
            "bags_checked": len(local_solutions),
            "adhesions_filtered": count_filtered_adhesions(decomp)
        },
        birth="undecided",
        impact=1 if answer else 0,
        trit=0,   # Decision is ERGODIC (coordination)
        sheaf_condition=verify_sheaf_condition(decomp, local_solutions),
        width_bounded=True,  # FPT guarantees
        gf3_conserved=True
    )
```

### Diff Template: Adhesion Filter

```python
def diff_adhesion_filter(decomp: StrDecomp, edge_idx: int) -> NaryaDiff:
    """Narya diff for adhesion filtering step."""
    
    old_adhesion = adhesionSpans(decomp)[edge_idx]
    
    before = {
        "adhesion": old_adhesion,
        "left_bag": old_adhesion.left,
        "right_bag": old_adhesion.right,
        "apex": old_adhesion.apex
    }
    
    # Apply adhesion filter (pullback + image)
    filtered = adhesion_filter(edge_idx, decomp)
    
    after = {
        "adhesion": filtered,
        "left_bag": filtered.left,
        "right_bag": filtered.right,
        "apex": filtered.apex
    }
    
    return NaryaDiff(
        before=before,
        after=after,
        delta={
            "operation": "adhesion_filter",
            "edge_index": edge_idx,
            "apex_reduction": len(before["apex"]) - len(after["apex"]),
            "is_empty": len(after["apex"]) == 0,
            "pullback_computed": True
        },
        birth="unfiltered_adhesion",
        impact=1 if len(before["apex"]) != len(after["apex"]) else 0,
        trit=+1,  # Filtering is PLUS (execution/transformation)
        sheaf_condition=is_pullback(filtered),
        width_bounded=len(after["apex"]) <= WIDTH_THRESHOLD,
        gf3_conserved=True
    )
```

### Diff Template: 𝐃 Functor Application

```python
def diff_lift_functor(F: Functor, decomp: StrDecomp) -> NaryaDiff:
    """Narya diff for lifting a functor via 𝐃."""
    
    before = {
        "functor": F,
        "decomposition": decomp,
        "lifted": None
    }
    
    lifted = 𝐃(F, decomp, CoDecomposition)
    
    after = {
        "functor": F,
        "decomposition": decomp,
        "lifted": lifted
    }
    
    return NaryaDiff(
        before=before,
        after=after,
        delta={
            "operation": "lift_functor",
            "source_category": str(dom(F)),
            "target_category": str(codom(F)),
            "lifted_bags": [F(bag) for bag in bags(decomp)],
            "decomp_type": "CoDecomposition"
        },
        birth="unlifted_problem",
        impact=1,
        trit=-1,  # Lifting is MINUS (validation/preparation)
        sheaf_condition=True,  # By functoriality
        width_bounded=True,
        gf3_conserved=True
    )
```

---

## Core Julia API

> **DeepWiki Reference**: [Module System and Code Organization](https://deepwiki.com/AlgebraicJulia/StructuredDecompositions.jl/2.2-module-system-and-code-organization)

### Package Architecture (Three-Module Pattern)

The package implements a **module aggregator pattern** with three independent sub-modules:

```
StructuredDecompositions.jl (17 lines - pure re-export facade)
├── Decompositions/          # Core decomposition algorithms
│   └── CliqueTrees, AbstractTrees
├── FunctorUtils/            # Category-theoretic transformations  
│   └── Catlab
└── DecidingSheaves/         # Sheaf-based decision algorithms
    └── Catlab, PartialFunctions
```

### Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `Catlab` | ≥0.16 | Categorical programming framework |
| `CliqueTrees` | ≥0.5.1 | Clique tree decomposition algorithms |
| `AbstractTrees` | ≥0.4 | Generic tree data structures |
| `MLStyle` | ≥0.4 | Pattern matching for algebraic types |
| `PartialFunctions` | ≥1.1 | Functional programming utilities |
| `Reexport` | ≥1.2.2 | Module re-export mechanism |

### StrDecomp Type

```julia
using StructuredDecompositions

# Structured decomposition = diagram d: ∫G → Span(C)
abstract type StructuredDecomposition{G, C, D} <: Diagram{id, C, D} end

struct StrDecomp{G, C, D} <: StructuredDecomposition{G, C, D}  
  decomp_shape ::G          # Shape graph (tree, dag, etc.)
  diagram      ::D          # Functor to category C
  decomp_type  ::DecompType # Decomposition or CoDecomposition
  domain       ::C          # Source category
end
```

### Key Operations

```julia
# Create from graph (via clique tree)
decomp = StrDecomp(graph)

# Access structure
bags(decomp)           # Vector of bag ACSets
adhesions(decomp)      # Vector of adhesion ACSets
adhesionSpans(decomp)  # Vector of span morphisms

# Lift functor to decomposition
lifted = 𝐃(functor, decomp, CoDecomposition)

# Decide sheaf satisfiability
(answer, witness) = decide_sheaf_tree_shape(sheaf, decomp)
```

### Adhesion Filter Algorithm

```julia
function adhesion_filter(i::Integer, d::StructuredDecomposition)
    # Get adhesion cospan
    d_csp = adhesionSpans(d, true)[i][2]
    
    # Compute pullback
    p_cone = pullback(d_csp)
    
    # Compute images via pullback legs
    imgs = map(f -> legs(image(f))[1], legs(p_cone))
    
    # Compose with original cospan
    new_d_csp = map(t -> compose(t...), zip(imgs, d_csp))
    
    # Return filtered decomposition
    # ...
end
```

---

## GF(3) Triadic Integration

### Canonical Triads

```
structured-decompositions (-1) ⊗ tripartite-decompositions (0) ⊗ gay-mcp (+1) = 0 ✓
sheaf-cohomology (-1) ⊗ bumpus-narratives (0) ⊗ triad-interleave (+1) = 0 ✓
structured-decompositions (-1) ⊗ acsets (0) ⊗ colimit-reconstruct (+1) = 0 ✓
```

### Skill Dependencies

| Skill | Trit | Integration |
|-------|------|-------------|
| [tripartite-decompositions](file:///Users/barton/.claude/skills/tripartite-decompositions/SKILL.md) | 0 | GF(3)-balanced K₃ decompositions |
| [sheaf-cohomology](file:///Users/barton/.claude/skills/sheaf-cohomology/SKILL.md) | -1 | Čech cohomology verification |
| [bumpus-narratives](file:///Users/barton/.claude/skills/bumpus-narratives/SKILL.md) | 0 | Time-varying sheaves |
| [acsets-algebraic-databases](file:///Users/barton/.claude/skills/acsets-algebraic-databases/SKILL.md) | 0 | Schema foundation |
| [gay-mcp](file:///Users/barton/.claude/skills/gay-mcp/SKILL.md) | +1 | Deterministic coloring |
| [compositional-acset-comparison](file:///Users/barton/.claude/skills/compositional-acset-comparison/SKILL.md) | 0 | Geometric morphisms |
| [l-space](file:///Users/barton/.claude/skills/l-space/SKILL.md) | 0 | Narrative decompositions |
| [bisimulation-game](file:///Users/barton/.claude/skills/bisimulation-game/SKILL.md) | -1 | Equivalence verification |

---

## Narya Compatibility

| Field | Definition | Example |
|-------|------------|---------|
| `before` | State before decomposition operation | `{"graph": G, "decomp": None}` |
| `after` | State after with bags/adhesions | `{"decomp": d, "width": 3}` |
| `delta` | Change metrics | `{bag_count: 5, width: 3}` |
| `birth` | Initial undecomposed state | `"raw_graph"` |
| `impact` | 1 if new structure, 0 otherwise | Used for ANIMA detection |

## Invariant Set

| Invariant | Definition | Verification |
|-----------|------------|--------------|
| `SheafCondition` | Local solutions glue on adhesions | `verify_sheaf_condition()` |
| `WidthBounded` | Adhesion size ≤ k for FPT | `max_width(decomp) <= k` |
| `TreeShape` | Decomposition shape is acyclic | `is_tree(decomp.shape)` |
| `GF3Conservation` | Trit sum ≡ 0 (mod 3) | `sum(trits) % 3 == 0` |

## Condensation Policy

**Trigger**: When all bags have empty solution sets (unsatisfiable) or all adhesions filtered to identity (saturated).

```python
def should_condense(decomp: StrDecomp, solutions: Dict) -> bool:
    # Unsatisfiable: some bag has no local solutions
    if any(len(s) == 0 for s in solutions.values()):
        return True  # Condense to "NO"
    
    # Saturated: all adhesions are identity (no filtering needed)
    if all(is_identity(adh) for adh in adhesions(decomp)):
        return True  # Condense to "YES"
    
    return False
```

---

## Commands

```bash
# Process Bumpus papers with mathpix-gem
just bumpus-extract

# Run structured decomposition on graph
just strdecomp-decide graph.json sheaf.jl

# Verify sheaf condition
just strdecomp-verify decomp.json

# Generate Narya diff report
just strdecomp-narya-report graph.json

# Extract equations from paper
just mathpix-equations paper.pdf
```

---

## References

1. Bumpus, Kocsis, Master, Minichiello. "Structured Decompositions" arXiv:2207.06091
2. Althaus, Bumpus, Fairbanks, Rosiak. "Compositional Algorithms" arXiv:2302.05575
3. Bumpus, Kocsis. "Spined Categories" arXiv:2104.01841
4. Bumpus et al. "Unified Theory of Time-Varying Data" arXiv:2402.00206
5. AlgebraicJulia ecosystem: https://algebraicjulia.github.io
6. TeglonLabs/mathpix-gem: https://github.com/TeglonLabs/mathpix-gem
7. **DeepWiki**: https://deepwiki.com/AlgebraicJulia/StructuredDecompositions.jl

## DeepWiki Navigation

| Page | URL |
|------|-----|
| Overview | [/AlgebraicJulia/StructuredDecompositions.jl](https://deepwiki.com/AlgebraicJulia/StructuredDecompositions.jl) |
| Package Architecture | [/2-package-architecture](https://deepwiki.com/AlgebraicJulia/StructuredDecompositions.jl/2-package-architecture) |
| Module System | [/2.2-module-system-and-code-organization](https://deepwiki.com/AlgebraicJulia/StructuredDecompositions.jl/2.2-module-system-and-code-organization) |
| Mathematical Foundations | [/2.3-mathematical-foundations](https://deepwiki.com/AlgebraicJulia/StructuredDecompositions.jl/2.3-mathematical-foundations) |
| Development Guide | [/3-development-guide](https://deepwiki.com/AlgebraicJulia/StructuredDecompositions.jl/3-development-guide) |
| CI/CD and Automation | [/5-cicd-and-automation](https://deepwiki.com/AlgebraicJulia/StructuredDecompositions.jl/5-cicd-and-automation) |

---

## Scientific Skill Interleaving

This skill connects to the K-Dense-AI/claude-scientific-skills ecosystem:

### Tree Decomposition
- **etetoolkit** [○] via bicomodule
- **networkx** [○] via graph algorithms

### Bibliography References

- `algorithms`: 19 citations in bib.duckdb
- `category-theory`: 139 citations in bib.duckdb

## Cat# Integration

This skill maps to **Cat# = Comod(P)** as a bicomodule in the equipment structure:

```
Trit: -1 (MINUS)
Home: Prof
Poly Op: ⊗
Kan Role: Adj
Color: #9400D3
```

### GF(3) Naturality

The skill participates in triads satisfying:
```
(-1) + (0) + (+1) ≡ 0 (mod 3)
```

This ensures compositional coherence in the Cat# equipment structure.

---

## Extracted Papers (via Mathpix)

| Paper | Pages | File |
|-------|-------|------|
| Structured Decompositions | 54 | [structured_decompositions.md](papers/structured_decompositions.md) |
| Compositional Algorithms | 38 | [compositional_algorithms.md](papers/compositional_algorithms.md) |
| Spined Categories | 28 | [spined_categories.md](papers/spined_categories.md) |
| Time-Varying Data | 25 | [time_varying_data.md](papers/time_varying_data.md) |
| Pushing Tree Decomps | 40 | [pushing_tree_decomps.md](papers/pushing_tree_decomps.md) |
| Failures of Compositionality | 37 | [failures_compositionality.md](papers/failures_compositionality.md) |

**Total**: 222 pages extracted via Mathpix API.

---

**Skill Name**: structured-decompositions  
**Type**: FPT Algorithms / Category Theory  
**Trit**: -1 (MINUS - Validator)  
**GF(3)**: Conserved via triadic composition  
**Mathpix**: Paper OCR integration  
**Narya**: Structured diff for every operation  
**DeepWiki**: https://deepwiki.com/AlgebraicJulia/StructuredDecompositions.jl

---

# APPENDIX: Bumpus Corpus (Verbatim Extractions via Mathpix API)

> **Note**: The following papers were extracted from arXiv PDFs using the Mathpix API on 2026-01-01. These are academic works by Benjamin Merlin Bumpus and collaborators. All rights remain with the original authors.

---

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



---


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



---


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



---


# Towards a Unified Theory of Time-Varying Data 

Benjamin Merlin Bumpus * James Fairbanks* Martti Karvonen ${ }^{\dagger} \quad$ Wilmer Leal*<br>Frédéric Simard ${ }^{\#}$<br>Last compilation: Wednesday $26{ }^{\text {th }}$ March, 2025


#### Abstract

What is a time-varying graph, a time-varying topological space, or, more generally, a mathematical structure that evolves over time? In this work, we lay the foundations for a general theory of temporal data by introducing categories of narratives. These are sheaves on posets of time intervals that encode snapshots of a temporal object along with the relationships between them. This theory satisfies five desiderata distilled from the burgeoning field of time-varying graphs: (D1) it defines both time-varying objects and their morphisms; (D2) it distinguishes between cumulative and persistent interpretations and provides principled methods for transitioning between them; (D3) it systematically lifts static notions to their temporal analogues; (D4) it is object agnostic; (D5) it integrates with theories of dynamical systems. To achieve this, we build upon existing categorical and sheaf-theoretic approaches to temporal graph theory, generalizing them to any category with limits and colimits. We also formalize tacit intuitions that, while present, often remain implicit in temporal graph theory. Beyond synthesizing and reformulating existing ideas in categorical language, we introduce sheaf-theoretic constructions and prove results that, to our knowledge, have not appeared in the temporal data literature-such as the adjunction between persistent and cumulative narratives. More importantly, we integrate these existing and novel elements into a consistent and coherent framework, setting the stage for a unified theory of time-varying data.


## 1 Introduction

We can never fully observe the underlying dynamics that govern nature. Instead we are left with two approaches; we call these: the 'method of axioms' and 'method of data'. The first focuses on establishing mechanisms (specified via, for example, differential equations or automata) that align with our experience of the hidden dynamics we seek to study. On the other hand, the 'method of data' emphasizes empirical observations, discerning appropriate mathematical structures that underlie the observed time-varying data and extracting meaningful insights into the time-varying system. Both of these approaches are obviously interlinked, yet the lack of a formal, unifying framework for time-varying data structures prevents us from making this connection explicit. While significant progress has been made in fields such as graph theory and topological data analysis, a more encompassing theoretical framework is needed-one that unifies these perspectives and extends to other temporal data structures.

In studying the data we can collect over time, we limit ourselves to the 'visible' aspects of the underlying dynamics. Thus, in much the same way as one can glean some (but perhaps not much) of the narrative of Romeo and Juliet by only reading a page of the whole, we view time-varying data as an observable narrative that tells a small portion of larger stories governed by more complex dynamics. This simple epistemological stance appears implicitly in many areas of mathematics concerned with temporal or time-varying data. For instance, consider the explosive birth of temporal graph theory. Here, one is interested in graphs whose vertices

[^0]and edges may come and go over time. To motivate these models, one tacitly appeals to the connection between time-varying data and a hidden dynamical system that generates it. A common example in the field of temporal graphs is that of opportunistic mobility [9]: physical objects in motion, such as buses, taxis, trains, or satellites, transmit information between each other at limited distances, and snapshots of the communication networks are recorded at various evenly-spaced instants in time. Further examples that assume the presence of underlying dynamics include human and animal proximity networks, human communication networks, collaboration networks, citation networks, economic networks, neuro-scientific networks, biological, chemical, ecological, and epidemiological networks [17, 32, 21, 28, 20, 9].

Although it is clear that what makes data temporal is its link to an underlying dynamical system, this connection is in no way mathematically explicit and concrete. Indeed one would expect there to be further mathematical properties of temporal data which allow us to distinguish a mere $\mathbb{N}$-indexed sequence of sets or graphs or groups, say, from their temporal analogues. As of yet, though, this distinction has rarely been formally and systematically investigated. For example think of temporal graphs once again. Modulo embellishing attributes such as latencies or wait times, typical definitions ${ }^{1}$ simply require temporal graphs to be sequences of graphs (e.g. [17, 32, 21, 20, $9,23,14,15,38,13,4,29,24,22$ ]). There no further semantics on the relationships between time steps is imposed. And these definitions never explicitly state what kind of global information should be tracked by the temporal data: is it the total accumulation of data over time or is it the persistent structure that emerges in the data throughout the evolution of the underlying dynamical system?

In this paper we ask: how does one build a robust and general theory of temporal data? To address this question, we first turn to the theory of time-varying graphs, a field that has received considerable attention in recent years $[17,32,21,20,9,23,14,15,38,13,4,29,24,22]$. This body of work has served both as a source of inspiration and as a foundation for our approach, offering concrete ideas, methodologies and perspectives that have shaped our understanding of time-varying structures. By analyzing the questions and techniques developed in this field, we seek to construct an abstract framework that captures the essential structures and hypotheses necessary for generalizing temporal data analysis across a broad spectrum of mathematical structures beyond graphs.

One key hypothesis that emerges from the study of time-varying graphs is that temporal data should not only record what occurred at various instants in time, but it should also keep track of the relationships between successive time-points. In other words, what makes data temporal is whether it is 'in the memory' [27] in the sense of st Augustine's Confessions [34, 2]. Hidden in this seemingly simple statement, is the structure of a sheaf: a temporal set (or graph or group, etc.) should consist of an assignment of a data set at each time point together with consistent assignments of sets over each interval of time in such a way that the sets assigned on intervals are determined by the sets assigned on subintervals. The sheaf-theoretic perspective we adopt here builds upon Schultz, Spivak and Vasilakopoulou's [39] notion of an interval sheaf and it allows for a very general definition of temporal objects.

Our contribution is twofold; first we distill the lessons learned from temporal graph theory into the following set of desiderata for any mature theory of temporal data:
(D1) (Categories of Temporal Data) Any theory of temporal data should define not only time-varying data, but also appropriate morphisms thereof.
(D2) (Cumulative and Persistent Perspectives) In contrast to being a mere sequence, temporal data should explicitly record whether it is to be viewed cumulatively or persistently. Furthermore there should be methods of conversion between these two viewpoints.
(D3) (Systematic 'Temporalization') Any theory of temporal data should come equipped with systematic ways of obtaining temporal analogues of notions relating to static data.

[^1](D4) (Object Agnosticism) Theories of temporal data should be object agnostic and applicable to any kinds of data originating from given underlying dynamics.
(D5) (Sampling) Since temporal data naturally arises from some underlying dynamical system, any theory of temporal data should be seamlessly interoperable with theories of dynamical systems.

Our second main contribution is to introduce categories of narratives, an object-agnostic theory of time-varying objects which satisfies the desiderata mentioned above. As a benchmark, we then observe how standard ideas of temporal graph theory crop up naturally when our general framework of temporal objects is instantiated on graphs.

We choose to see this task of theory-building through a category theoretic lens for three reasons. First of all this approach directly addresses our first desideratum (D1), namely that of having an explicit definition of isomorphisms (or more generally morphisms) of temporal data. Second of all, we adopt a category-theoretic approach because its emphasis, being not on objects, but on the relationships between them [36, 3], makes it particularly well-suited for general, object-agnostic definitions. Thirdly, sheaves, which are our main technical tool in the definition of time-varying data, are most naturally studied in category theoretic terms [37, 30].

### 1.1 Previous and Related Work: Accumulating Desiderata for a General Theory of Temporal Data

There are as many different definitions of temporal graphs as there are application domains from which the notion can arise. This has lead to a proliferation of many subtly different concepts such as: temporal graphs, temporal networks, dynamic graphs, evolving graphs and time-varying graphs [17, 32, 21, 20, 9, 23]. Each model of temporal graphs makes different assumptions on what may vary over time. For example, are the vertices fixed, or may they change? Does it take time to cross an edge? And does this change as an edge appears and disappears? If an edge reappears after having vanished at some point in time, in what sense has it returned, is it the same edge?

The novelty of these fields and the many fascinating directions for further inquiry they harbor make the mathematical treatment of temporal data exciting. However, precisely because of the field's youth, we believe that it is crucial to pause and distill the lessons we have learned from temporal graphs into desiderata for the field of temporal data more broadly. In what follows we shall briefly contextualize each desideratum mentioned above in turn while also signposting previous work and how our framework addresses each point. We begin with (D1)

1. Morphisms of temporal graphs are rarely treated as a central concept, let alone formally defined and systematically exploited to gain insights or prove new results. In [25], for example, the authors note in [Table 3][25] that cosheaves in the poset of subobjects of a fixed complete graph can be interpreted as cumulative temporal graphs. This is a beautiful idea that we will systematically investigate, extend, and connect with other aspects of temporal data (see Section 2.2). However, morphisms are only implicitly recognized in [25] (since cosheaves inherently come with a notion of morphism), and their potential for yielding technical results and deeper insights into temporal structures remains largely unexplored in both this work and the broader literature. This is a serious impediment to the generalization of the ideas of temporal graphs to other time-varying structures since any such general theory should be invariant under isomorphisms. Thus we distill our first desideratum (D1) theories of temporal data should not only concern themselves with what time-varying data is, but also with what an appropriate notion of morphism of temporal data should be. These morphisms will enable analysis of temporal objects.

Narratives, our definition of time-varying data (Definition 2.8), are stated in terms of certain kinds of sheaves. This immediately addresses desideratum (D1) since it automatically equips us with a suitable and well-studied [37, 30] notion of a morphism of temporal data, namely morphisms of sheaves. Then, by instantiating narratives on graphs in Section 2.4, we define categories of temporal graphs as a special case of the broader theory. This notion of morphisms is central to accomplishing each of the desiderata. This is especially true for Theorem 2.10, where we define an adjunction between the persistent and
cumulative perspectives (D2), and also in Section 2.5, where classes of temporal objects are defined in terms of which morphisms of temporal objects they admit (D3).
2. Our second desideratum is born from observing that most current definitions of temporal graphs are equivalent to mere sequences of graphs [9, 23] (snapshots) without explicit mention of how each snapshot is related to the next (see below for a notable exception in TDA). To understand the importance of this observation, we must first note that in any theory of temporal graphs, one always finds great use in relating time-varying structure to its older and more thoroughly studied static counterpart. For instance, any temporal graph is more or less explicitly assumed to come equipped with an underlying static graph [9, 23]. This is a graph consisting of all those vertices and edges that were ever seen to appear over the course of time and it should be thought of as the result of accumulating data into a static representation. Rather than being presented as part and parcel of the temporal structure, the underlying static graphs are presented as the result of carrying out a computation-that of taking unions of snap-shots-involving input temporal graphs. The implicitness of this representation has two drawbacks. The first is that it does not allow for vertices or edges to merge or divide over time; these are very natural operations that one should expect of time-varying graphs in the 'wild' (think for example of cell division or acquisitions or merges of companies). The second drawback of the implicitness of the computation of the underlying static graph is that it conceals another very natural static structure that always accompanies any given temporal graph, we call it the persistence graph. This is the static graph consisting of all those vertices and edges which persisted throughout the entire life-span of the temporal graph. We distill this general pattern into desideratum (D2) temporal data should come explicitly equipped with either a cumulative or a persistent perspective which records which information we should be keeping track of over intervals of time.

Outside of the temporal graph community, in topological data analysis the authors of [25] use cosheaves over intervals to define a time-varying graph whose snapshots are all subgraphs of a fixed, globallydefined complete graph. In our language, this is an instance of a cumulative narrative valued in the subobject poset of $K_{n}$ for some $n$. Kim and Memoli [25] are interested in applications of this cosheaf perspective for uses in TDA and do not consider persistent time-varying graphs (sheaves over intervals) and the relationship between these two kinds of temporal graphs. Our work differs from [25] in three fundamental ways: (1) we define cumulative narratives not just for subobject posets of the complete graphs, but for any category with colimits ${ }^{2}$, (2) we introduce persistent time-varying graphs and, more generally, persistent narratives valued in any category with limits; and (3) we establish a formal connection between these two perspectives using categorical duality. Specifically, we prove that there is an adjunction between the categories of persistent and cumulative narratives, providing a principled way to satisfy desideratum (D2). sheaves encode the persistence perspective, while cosheaves-the dual of a sheaf-encode the accumulation perspective. As we will show, while these two perspectives give rise to equivalences on certain subcategories of temporal graphs, in general, when one passes to arbitrary categories of temporal objects-such as temporal groups, for example-this equivalence weakens to an adjunction (this is Theorem 2.10, roughly one can think of this as a Galois connection [16]). In particular our results imply that in general there is the potential for a loss of information when one passes from one perspective (the persistent one, say) to another (the cumulative one) and back again. This observation, which has so far been ignored, is of great practical relevance since it means that one must take a great deal of care when collecting temporal data since the choices of mathematical representations may not be interchangeable. We will prove the existence of the adjunction between cumulative and persistent temporal data (for any category with pullbacks and pushouts, such as the category of graphs) in Theorem 2.10 and discuss all of these subtleties in Section 2.3 Furthermore, this adjunction opens interesting directions for future work investigating the relationship between the persistent and cumulative perspectives present in topological data analysis; for instance, the program of 'generalized persistence' initiated by Patel and developed in the work of Kim and Memoli [25].

[^2]3. Another common theme arising in temporal graph theory is the relationship between properties of static graphs and their temporal analogues. At first glance, one might naïvely think that static properties can be canonically lifted to the temporal setting by simply defining them in terms of underlying static graphs. However, this approach completely forgets the temporal structure and is thus of no use in generalizing notions such as for example connectivity or distance where temporal information is crucial to the intended application [32, 9, 14, 8]. Moreover, the lack of a systematic procedure for 'temporalizing' notions from static graph theory is more than an aesthetic obstacle. It fuels the proliferation of myriads of subtly different temporal analogues of static properties. For instance should a temporal coloring be a coloring of the underlying static graph? What about the underlying persistence graph? Or should it instead be a sequence of colorings? And should the colorings in this sequence be somehow related? Rather than accepting this proliferation as a mere consequence of the greater expressiveness of temporal data, we sublime these issues into desideratum (D3) any theory of temporal data should come equipped with a systematic way of 'temporalizing' notions from traditional, static mathematics.
In Section 2.5, we show how our theories of narratives satisfies desideratum (D3) We do so systematically by leveraging two simple, but effective functors: the change of temporal resolution functor (Proposition 2.19) and the change of base functor (Propositions 2.15 and 2.16). The first allows us to modify narratives by rescaling time, while the second allows us to change the kind of data involved in the narrative (e.g. passing from temporal simplicial complexes to temporal graphs). Using these tools, we provide a general way for temporalizing static notions which roughly allows one to start with a class of objects which satisfy a given property (e.g. the class of paths, if one is thinking about temporal graphs) and obtain from it a class of objects which temporally satisfy that property (e.g. the notion of temporal paths). As an example (other than temporal paths which we consider in Proposition 2.17) we apply our abstract machinery to recover in a canonical way (Proposition 2.22) the notion of a temporal clique (as defined by Viard, Latapy and Magnien [42]). Crucially, the only information one needs to be given is the definition of a clique (in the static sense). Summarizing this last point with a slogan, one could say that 'our formalism can derive the definition of temporal cliques given solely the definition of a clique as input'. Although it is beyond the scope of the present paper, we believe that this kind of reasoning will prove to be crucial in the future for a systematic study of how theories of temporal data (e.g. temporal graph theory) relate to their static counterparts (e.g. graph theory).
4. Temporal graphs are definitely ubiquitous forms of temporal data $[17,32,21,20,9,23$, but they are by far not the only kind of temporal data one could attach, or sample from an underlying dynamical system. Thus Desideratum (D4) is evident: to further our understanding of data which changes with time, we cannot develop case by case theories of temporal graphs, temporal simplicial complexes, temporal groups etc., but instead we require a general theory of temporal data that encompasses all of these examples as specific instances and which allows us to relate different kinds of temporal data to each other.
Our theory of narratives addresses part of Desideratum(D4)almost out of the box: our category theoretic formalism is object agnostic and can be thus applied to mathematical objects coming from any such category thereof. We observe through elementary constructions that there are change of base functors which allow one to convert temporal data of one kind into temporal data of another. Furthermore, we observe that, when combined with the adjunction of Theorem 2.10, these simple data conversions can rapidly lead to complex relationships between various kinds of temporal data.
5. As we mentioned earlier, our philosophical contention is that on its own data is not temporal; it is through originating from an underlying dynamical system that its temporal nature is distilled. This link can and should be made explicit. But until now the development of such a general theory is impeded by a great mathematical and linguistic divide between the communities which study dynamics axiomatically (e.g. the study of differential equations, automata etc.) and those who study data (e.g. the study of time series, temporal graphs etc.). Thus we distill our last Desideratum (D5) any theory of temporal data should be seamlessly interoperable with theories of dynamical systems from which the data can arise.
This desideratum is ambitious enough to fuel a research program and is thus beyond the scope of a single paper. However, for any such theory to be developed, one first needs to place both the theory of
dynamical systems and the theory of temporal data on the same mathematical and linguistic footing. This is precisely how our theory of narratives addresses Desideratum (D5) since both narratives (our model of temporal data) and Schultz, Spivak and Vasilakopoulou's interval sheaves [39] (a general formalism for studying dynamical systems) are defined in terms of sheaves on categories of intervals, we have bridged a significant linguistic divide between the study of data and dynamics. We expect this to be a very fruitful line of further research in the years to come.

Having identified the desiderata for a theory of time-varying data, we conclude this section by further contextualizing our work with other uses of sheaf theory to study time-varying phenomena. As we already mentioned, Schultz, Spivak and Vasilakopoulou [39] study dynamical systems through a sheaf-theoretic lens; moreover, there have been other investigations of time-varying structures which use similar tools. An example within the applied topology and topological data analysis communities is the examination of connected components over time using Reeb graphs. For instance, in [12], the authors leverage the established fact that the category of Reeb graphs is equivalent to a certain class of cosheaves. This equivalence is exploited to define a distance between Reeb graphs, which proves to be resilient to perturbations in the input data. Furthermore, it serves the purpose of smoothing the provided Reeb graphs in a manner that facilitates a geometric interpretation. Similarly, the study of the persistence of topological features in point-cloud datasets has given rise to the formulation of the theory of persistence for 'Zigzag diagrams'. This theory extends beyond persistent homology and also has a cosheaf interpretation [11, 10]. Although it is beyond the scope of the current paper, we believe that exploring the connections between our work these notions from applied topology is an exciting direction for further study.

## 2 Categories of Temporal Data

Our thesis is that temporal data should be represented mathematically via sheaves (or cosheaves, their categorical dual). Sheaf theory, already established in the 1950s as a crucial tool in algebraic topology, complex analysis, and algebraic geometry, is canonically the study of local-to-global data management. For our purposes here, we will only make shallow use of this theory; nevertheless, we anticipate that more profound sheaf-theoretic tools, such as cohomology, will play a larger role in the future study of temporal data. To accommodate readers from disparate backgrounds, we will slowly build up the intuition for why one should represent temporal data as a sheaf by first peeking at examples of temporal sets in Section 2.1. We will then formally introduce interval sheaves (Section 2.2) and immediately apply them by collecting various examples of categories of temporal graphs (Section 2.4) before ascending to more abstract theory.

### 2.1 Garnering Intuition: Categories of Temporal Sets.

Take a city, like Venice, Italy, and envision documenting the set of ice cream companies that exist in that city each year. For instance, in the first year, there might be four companies $\left\{a_{1}, a_{2}, b, c\right\}$. One could imagine that from the first year to the next, company $b$ goes out of business, company $c$ continues into the next year, a new ice cream company $b^{\prime}$ is opened, and the remaining two companies $a_{1}$ and $a_{2}$ merge into a larger company $a_{\star}$. This is an example of a discrete temporal set viewed from the perspective of persistence: not only do we record the sets of companies each year (which, in the $i$-th year, we denote as $F_{i}^{i}$ ), but instead we also keep track of which companies persist from one year to the next and how they do so (which we denote as $F_{i}^{j}$ ). Diagramatically we could represent the first three years of this story as follows.
![](https://cdn.mathpix.com/cropped/ca25655d-fbfb-48e6-bc70-6703e81dac02-06.jpg?height=173&width=1431&top_left_y=2191&top_left_x=320)

This is a diagram of sets and the arrows are functions between sets. In this example we have that $f_{1,2}^{1}$ is the
canonical injection of $F_{1}^{2}$ into $F_{1}^{1}$ while $f_{1,2}^{2}$ maps $c$ to itself and it takes both $a_{1}$ and $a_{2}$ to $a_{\star}$ (representing the unification of the companies $a_{1}$ and $a_{2}$ ).

Diagram 1 is more than just a time-series or a sequence of sets: it tells a story by relating (via functions in this case) the elements of successive snapshots. It is obvious, however, that from the relationships shown in Diagram 1 we should be able to recover longer-term relationships between instances in time. For instance we should be able to know what happened to the four companies $\left\{a_{1}, a_{2}, b, c\right\}$ over the course of three years: by the third year we know that companies $a_{1}$ and $a_{2}$ unified and turned into company $a_{\star}$, companies $b$ and $c$ dissolved and ceased to exist and two new companies $b^{\prime}$ and $c^{\prime}$ were born.

The inferences we just made amounted to determining the relationship between the sets $F_{1}^{1}$ and $F_{3}^{3}$ completely from the data specified by Diagram 1 Mathematically this is an instance of computing $F_{1}^{3}$ as a fibered product (or pullback) of the sets $F_{1}^{2}$ and $F_{2}^{3}$ along functions $f_{1,2}^{2}$ and $f_{2,3}^{2}$ :

$$
F_{1}^{3}:=\left\{(x, y) \in F_{1}^{2} \times F_{2}^{3} \mid f_{1,2}^{2}(x)=f_{2,3}^{2}(y)\right\} .
$$

Diagrammatically this is drawn as follows.
![](https://cdn.mathpix.com/cropped/ca25655d-fbfb-48e6-bc70-6703e81dac02-07.jpg?height=265&width=1423&top_left_y=928&top_left_x=326)

The selection of the aforementioned data structures, namely sets and functions, allowed us to encode a portion of the history behind the ice cream companies in Venice. If we were to delve deeper and investigate, for instance, why company $c$ disappeared, we could explore a cause within the dynamics of the relationships between ice cream companies and their suppliers. These relationships can be captured using directed graphs, as illustrated in Diagram 3, where there is an edge from $x$ to $y$ if the former is a supplier to the latter. This diagram reveals that company $a_{2}$ not only sold ice cream but also supplied companies $a_{1}$ and $c$. Notably, with the dissolution of company $b$ in the second year, it becomes conceivable that the closure of company $c$ occurred due to the cessation of its supply source.
![](https://cdn.mathpix.com/cropped/ca25655d-fbfb-48e6-bc70-6703e81dac02-07.jpg?height=334&width=1441&top_left_y=1602&top_left_x=326)

More generally, within a system, numerous observations can be made. Each observation is intended to capture a different facet of the problem. This diversity translates into the necessity of employing various data structures, such as sets, graphs, groups, among others, to represent relevant mathematical spaces underlying the data. Our goal in this work is to use a language that enables us to formally handle data whose snapshots are modeled via commonly used data structures in data analysis. As we will explain in Section 2.2, the language we are looking for is that of sheaves, and the structure hidden in Diagrams 2 and 3 is that of a sheaf on a category of intervals. Sheaves are most naturally described in category-theoretic terms and, as is always the case in category theory, they admit a categorically dual notion, namely cosheaves. As it turns out, while sheaves capture the notion of persistent objects, cosheaves on interval categories instead capture the idea of an underlying static object that is accumulated over time. Thus we see (this will be explained formally in Section 2.3) that the two perspectives-persistent vs. cumulative-of our second desideratum are not only convenient and intuitively natural, they are also dual to each other in a formal sense.

### 2.2 Narratives

From this section onward we will assume basic familiarity with categories, functors and natural transformations. For a very short, self-contained introduction to the necessary background suitable for graph theorists, we refer the reader to the thesis by Bumpus [7, Sec. 3.2]. For a thorough introduction to the necessary categorytheoretic background, we refer the reader to any monograph on category theory (such as Riehl's textbook [36] or Awodey's [3]). We will give concrete definitions of the specific kinds of sheaves and co-sheaves that feature in this paper; however, we shall not recall standard notions in sheaf theory. For an approachable introduction to any notion from sheaf theory not explicitly defined here, we refer the reader to Rosiak's excellent textbook [37].

For most, the first sheaves one encounters are sheaves on a topological space. These are assignments of data to each open of a given topological space in such a way that these data can be restricted along inclusions of opens and such that the data assigned to any open $U$ of the space is completely determined from the data assigned to the opens of any cover of $U$. In gradually more concrete terms, a Set-valued sheaf $\mathcal{F}$ on a topological space $\mathcal{X}$ is a contravariant functor (a presheaf) $\mathcal{F}: O(\mathcal{X})^{o p} \rightarrow$ Set from the poset of opens in $\mathcal{X}$ to sets which satisfies certain lifting properties relating the values of $\mathcal{F}$ on any open $U$ to the values of $\left(\mathcal{F}\left(U_{i}\right)\right)_{i \in I}$ for any open cover $\left(U_{i}\right)_{i \in I}$ of $U$. Here we are interested in sheaves that are: (1) defined on posets (categories) of closed intervals of the non-negative reals (or integers) and (2) not necessarily Set-valued. The first requirement has to do with representing time. Each point in time $t$ is represented by a singleton interval $[t, t]$ and each proper interval $\left[t_{1}, t_{2}\right]$ accounts for the time spanned between its endpoints. The second requirement has to do with the fact that we are not merely interested in temporal sets, but instead we wish to build a more general theory capable or representing with a single formalism many kinds of temporal data such as temporal graphs, temporal topological spaces, temporal databases, temporal groups etc..

Thus one can see that, in order to specify a sheaf, one requires: (1) a presheaf $\mathcal{F}: \mathrm{C}^{o p} \rightarrow \mathrm{D}$ from a category C to a category D, (2) a notion of what should count of as a 'cover' of any object of C and (3) a formalization of how $\mathcal{F}$ should relate objects to their covers. To address the first point we will first give a reminder of the more general notation and terminology surrounding presheaves.

Definition 2.1. For any small category $C$ (such as $I$ or $I_{\mathbb{N}}$ ) we denote by $D^{C}$ the category of $D$-valued co-presheaves on C ; this has functors $P: \mathrm{C} \rightarrow \mathrm{D}$ as objects and natural transformations as morphisms. When we wish to emphasize contravariance, we call $\mathrm{D}^{\mathrm{C}^{o p}}$ the category of D -valued presheaves on C .

The second point - on choosing good notions of 'covers' - is smoothly handled via the notion of a Grothendieck topology (see Rosiak's textbook [37] for a formal definition). Categories equipped with a choice of a Grothendieck topology are known as sites and the following definition (due to Schultz, Spivak and Vasilakopoulou [39]) amounts to a way of turning categories of intervals into sites by specifying what counts as a valid cover of any interval.

Definition 2.2 (Interval categories [40]). The category of intervals, denoted Int is the category having closed intervals $\left[\ell, \ell^{\prime}\right]$ in $\mathbb{R}+$ (the non-negative reals) as objects and orientation-preserving isometries as morphisms. Analogously, one can define the category $\operatorname{Int}_{\mathbb{N}}$ of discrete intervals by restricting only to $\mathbb{N}$-valued intervals. These categories can be turned into sites by equipping them with the Johnstone coverage [40] which stipulates that any cover of any interval $\left[\ell, \ell^{\prime}\right]$ is generated by a partition into two closed intervals $\left([\ell, p],\left[p, \ell^{\prime}\right]\right)^{a}$

[^3]Schultz, Spivak and Vasilakopoulou defined interval sites to speak of dynamical systems as sheaves [40]. Here we are instead interested in temporal data. As most would expect, data should in general be less temporally interwoven compared to its dynamical system of provenance (after all the temporal data should carry less information than a dynamical system). This intuition ${ }^{3}$ motivates why we will not work directly with Schultz,

[^4]Spivak and Vasilakopoulou's definition, but instead we will make use of the following stricter notion of categories of strict intervals ${ }^{4}$

Definition 2.3 (Closed Intervals and Inclusions). We denote by I (resp. $\mathrm{I}_{\mathbb{N}}$ ) the full subcategory (specifically a join-semilattice) of the subobject poset of $\mathbb{R}$ (resp. $\mathbb{N}$ ) whose objects are closed intervals and whose morphisms are inclusions of intervals.

Clearly, the categories defined above are subcategories of Int (resp. $\operatorname{lnt}_{\mathbb{N}}$ ) since their morphisms are orientation-preserving isometries. Notice that the categories I (resp. $\mathbb{I}_{\mathbb{N}}$ ) are posetal (in contrast, Int is not posetal). Hence, the poset of subobjects of any interval $[a, b]$ forms a subcategory of I (resp $\mathrm{I}_{\mathbb{N}}$ ), which we denote by $\mathrm{I} /[a, b]$ (resp. $\mathrm{I}_{\mathbb{N}} /[a, b]$ ). In what follows, since we will want to speak of discrete, continuous, finite and infinite time, it will be convenient to have terminology to account for which categories we will allow as models of time. We will call such categories time categories.

Notation 2.4. A time category is any sub-join-semilattice T of either I or $\mathrm{I}_{\mathbb{N}}$. The left hand side of Figure 1 visualizes the time category $\mathrm{I}_{\mathbb{N}} /[1,3]$.

The following lemma states that time categories can be given Grothendieck topologies in much the same way as the interval categories of Definition 2.2 Since the proof is completely routine, but far too technical for newcomers to sheaf theory, we will omit it assuming that the readers well-versed in sheaf theory can reproduce it on their own.

Lemma 2.5. Any time category forms a site when equipped with the Johnstone coverage.
Equipped with suitable sites, we are now ready to give the definition of the categories $\mathrm{Cu}(\mathrm{T}, \mathrm{D})$ and $\operatorname{Pe}(T, D)$ where $T$ is any time category. We will refer to either one of these as categories of D-narratives in T-time: intuitively these are categories whose objects are time-varying objects of D. For instance, taking D to be Set or Grph one can speak of time varying sets or time-varying graphs. The difference between $\operatorname{Pe}(T, D)$ and $\mathrm{Cu}(\mathrm{T}, \mathrm{D})$ will be that the first encodes D -narratives according to the persistent perspective (these will be D -valued sheaves on T ), while the second employs a cumulative one (these will be D -valued co-sheaves on T ).

Definition 2.6. We will say that the narratives are discrete if the time category involved is either $I_{\mathbb{N}}$ or any sub-join-semilattices thereof. Similarly we will say that a category of narratives has finite lifetime if its time category has finitely many objects or if it is a subobject poset generated by some element of 1 or $\mathbb{I}_{\mathbb{N}}$.

Now we are ready to give the definition of a sheaf with respect to any of the sites described in Lemma 2.5 The reader not interested in sheaf theory should take the following proposition (whose proof is a mere instantiation of the standard definition of a sheaf on a site) as a definition of a sheaf on a time category.

Proposition 2.7 (T-sheaves and T-cosheaves). Let T be any time category equipped with the Johnstone coverage. Suppose D is a category with pullbacks, then a D -valued sheaf on T is a presheaf $F: \mathrm{T}^{o p} \rightarrow \mathrm{D}$ satisfying the following additional condition: for any interval $[a, b]$ and any cover $([a, p],[p, b])$ of this interval, $F([a, b])$ is the pullback $F([a, p]) \times_{F([p, p])} F([p, b])$. (See Figure 1])

Similarly, supposing D to be a category with pushouts, then a D -valued cosheaf on T is a copresheaf $\hat{F}: \mathrm{T} \rightarrow \mathrm{D}$ satisfying the following additional condition: for any interval $[a, b]$ and any cover $([a, p],[p, b])$ of this interval, $\hat{F}([a, b])$ is the pushout $\hat{F}([a, p])+\hat{F}([p, p]) \hat{F}([p, b])$.

Proof. By definition, a sheaf (resp. cosheaf) on the Johnstone coverage is simply a presheaf which takes each cover (a partion of an interval) to a limit (resp. colimit).

[^5]![](https://cdn.mathpix.com/cropped/ca25655d-fbfb-48e6-bc70-6703e81dac02-10.jpg?height=280&width=1507&top_left_y=382&top_left_x=309)
Figure 1: A schematic visualization of a sheaf on a discrete time category (a persistent narrative) with three snapshots. The domain is the time category $\mathrm{I}_{\mathbb{N}} /[1,3]$, a join-semi-lattice whose objects are closed subintervals of $[1,3]$ and whose morphisms are interval inclusions. The codomain of the sheaf is a category $D$ with pullbacks. We use the shorthand $F_{i}^{j}$ (for $i \leq j$ ) to denote the data assigned the interval $[i, j]$ by $F$ (i.e. $F_{i}^{j}:=F([i, j])$ ).

Definition 2.8. We denote by $\mathrm{Pe}(\mathrm{T}, \mathrm{D})$ (resp. $\mathrm{Cu}(\mathrm{T}, \mathrm{D})$ ) the category of D -valued sheaves (resp. cosheaves) on T and we call it the category of persistent D-narratives (resp. cumulative D-narratives) with T-time.

By this point, the reader has already encountered an example of a persistent discrete Set-narrative: Diagram 2, which illustrates the evolution of the temporal set over only three time steps. In contrast, Diagram 4 is not a persistent Set-narrative since $F_{1}^{3} \neq F_{1}^{2} \times F_{2}^{2} F_{2}^{3}$. To see this, observe that $F_{1}^{2} \times F_{2}^{2} F_{2}^{3}$ is the pullback of two subsets (indicated by the hooked arrows denoting injective maps), each of size two. Thus, $F_{1}^{2} \times F_{2}^{2} F_{2}^{3}$ has at most four elements, whereas $F_{1}^{3}$ has five.
![](https://cdn.mathpix.com/cropped/ca25655d-fbfb-48e6-bc70-6703e81dac02-10.jpg?height=304&width=1421&top_left_y=1383&top_left_x=326)

When writing examples, it is useful to observe that all discrete D-narratives (see Definition 2.6) are completely determined by the objects and morphisms associated to intervals of length zero and one. This also implies, for example, that, in order to store a discrete graph narrative with $t$-time steps, it suffices to store $2 t-1$ graphs (one for each interval of length zero and one for each interval of length one) and $2(t-1)$ graph homomorphisms.

Proposition 2.9. Suppose we are given a objects $F([t, t])$ and $F([t, t+1])$ of D for each time point $[t, t]$ and for each length-one interval $[t, t+1]$ and that we are furthermore given a span $F([t, t]) \leftarrow F([t, t+1]) \rightarrow F([t+1, t+1])$ for each pair of successive times $t$ and $t+1$. Then there is (up to isomorphism) a unique discrete D-narrative which agrees with these choices of objects and spans. Conversely, a mere sequence of objects of D (i.e. a choice of one object for each interval of length zero) does not determine a unique discrete D-narrative.

Proof. To see the first point, simply observe that applying the sheaf condition to this data leaves no choice for the remaining assignments on objects and arrows: these are completely determined by pullback and pullbacks are unique up to isomorphism.

On the other hand, suppose we are only given a list of objects of $D$, one for each interval of length zero. Then, having to satisfy the sheaf condition does not determine a unique D-narrative that agrees with the given
snapshots. To see this, observe that any length-one interval $[t, t+1]$ has exactly two covers: namely ( $[t, t],[t, t+ 1])$ and $([t, t+1],[t+1, t+1])$. Thus, applying the sheaf condition, we we have that $G([t, t+1])$ must be the pullback $G([t, t]) \times_{G([t, t])} G([t, t+1])$. However, this pullback is always isomorphic to $G([t, t+1])$ for any choice of the object $G([t, t+1])$ since pullbacks preserve isomorphisms (and since the restriction of $G([t, t])$ to itself is its identity morphism). This concludes the proof since the argument is exactly the same for the cover $([t, t+1],[t+1, t+1])$. $\square$

For an example of a cumulative narrative, consider the following diagram (recall that, since they are cosheaves, cumulative narratives are covariant functors).
![](https://cdn.mathpix.com/cropped/ca25655d-fbfb-48e6-bc70-6703e81dac02-11.jpg?height=269&width=1498&top_left_y=700&top_left_x=309)

We can think of this diagram (where we denoted injections via hooked arrows) as representing a cumulative view of the example from Section 2.1 of ice cream companies over time. Note that not all arrows are injections (the arrow $F_{1}^{1} \rightarrow F_{1}^{2}$ marked in blue is not injective since it takes every company to itself except for $a_{1}$ and $a_{2}$ which are both mapped to $a_{\star}$ ). Thus one can think of the cumulative perspective as accumulating not only the data (the companies) seen so far, but also the relationships that are 'discovered' thus far in time.

### 2.3 Relating the Cumulative and Persistent Perspectives

This section marks a significant step toward achieving our Desideratum (D2) for a theory for temporal structures. This desideratum emerges from the realization that, as we extend our focus to encompass categories beyond graphs, there exists a potential for information loss during the transition between the cumulative and persistent data structures. The present section systematically characterizes such transitions. Our Theorem 2.10 yields two key results: the functoriality of transitioning from cumulative to persistent and vice versa, and the establishment of the adjunction $\mathscr{K} \dashv \mathscr{P}$ formally linking these perspectives.

Theorem 2.10. Let D be a category with limits and colimits and T a time category. There exist functors $\mathscr{K}: \operatorname{Pe}(\mathrm{T}, \mathrm{D}) \rightarrow \mathrm{Cu}(\mathrm{T}, \mathrm{D})$ and $\mathscr{P}: \mathrm{Cu}(\mathrm{T}, \mathrm{D}) \rightarrow \mathrm{Pe}(\mathrm{T}, \mathrm{D})$. Moreover, these functors are adjoint to each other:
![](https://cdn.mathpix.com/cropped/ca25655d-fbfb-48e6-bc70-6703e81dac02-11.jpg?height=140&width=459&top_left_y=1766&top_left_x=833)

Proof. We first prove that passing from the persistent to the cumulative perspective is functorial. To this end, we define a functor $\mathscr{K}: \operatorname{Pe}(\mathrm{T}, \mathrm{D}) \rightarrow \mathrm{Cu}(\mathrm{T}, \mathrm{D})$ which takes any sheaf $F: \mathrm{T}^{\text {op }} \rightarrow \mathrm{D}$ to the copresheaf $\mathscr{K}(F): \mathrm{T} \rightarrow \mathrm{D}$ defined on objects by:

$$
[a, b] \mapsto \mathscr{K}(F)_{a}^{b}:=\operatorname{colim}\left((\mathrm{T} /[a, b] \hookrightarrow \mathrm{T})^{o p} \xrightarrow{F} \mathrm{D}\right),
$$

where $\mathscr{K}(F)_{a}^{b}$ serves as shorthand for $\mathscr{K}(F)([a, b])$. The existence of the colimit $\mathscr{K}(F)_{a}^{b}$ follows from the hypothesis, since $(\mathrm{T} /[a, b] \hookrightarrow \mathrm{T})^{\text {op }} \xrightarrow{F} \mathrm{D}$ is a diagram in D . Moreover, $\mathscr{K}(F)$ is defined on arrows as follows:

$$
\left(\left[a^{\prime}, b^{\prime}\right] \stackrel{f}{\hookrightarrow}[a, b]\right) \quad \mapsto \quad\left(\mathscr{K}(F)_{a^{\prime}}^{b^{\prime}} \mathscr{K}(F) f . \mathscr{K}(F)_{a}^{b}\right),
$$

where $\mathscr{K}(F) f$ is the unique arrow from $\mathscr{K}(F)_{a^{\prime}}^{b^{\prime}}$ to $\mathscr{K}(F)_{a}^{b}$, determined by the universal property of $\mathscr{K}(F)_{a^{\prime}}^{b^{\prime}}$. The fact that $\mathscr{K}(F) f$ maps identities to identities and respects composition also follows from universal properties of certain colimits involved. Moreover, $\mathscr{K}(F)$ satisfies the sheaf condition by construction (since its values in any interval are determined by an appropriate colimit).

Now we prove that passing from the cumulative to the persistent perspective is functorial. For this, we define $\mathscr{P}$ as the map that assigns to any cosheaf $\hat{F}: \mathrm{T} \rightarrow \mathrm{D}$ in $\mathrm{Cu}(\mathrm{T}, \mathrm{D})$ the presheaf $\mathscr{P}(\hat{F}): \mathrm{T}^{o p} \rightarrow \mathrm{D}$ defined on objects by:

$$
[a, b] \mapsto \mathscr{P}(\hat{F})_{a}^{b}:=\lim (\mathrm{T} /[a, b] \hookrightarrow \mathrm{T} \xrightarrow{\hat{F}} \mathrm{D}) .
$$

We will use the notation $\mathscr{P}(\hat{F})_{a}^{b}$ instead of $\mathscr{P}(\hat{F})([a, b])$. The existence of $\lim (\mathrm{T} /[a, b] \hookrightarrow \mathrm{T} \xrightarrow{\hat{F}} \mathrm{D})$ follows from the hypothesis, since $\mathrm{T} /[a, b] \hookrightarrow \mathrm{T} \xrightarrow{\hat{F}} \mathrm{D}$ is a diagram in D . Furthermore, $\mathscr{P}(\hat{F})$ is defined on the arrows as follows:

$$
\left(\left[a^{\prime}, b^{\prime}\right] \stackrel{f}{\hookrightarrow}[a, b]\right) \quad \mapsto \quad\left(\mathscr{P}(\hat{F})_{a}^{b} \xrightarrow{\mathscr{P}(\hat{F}) f} \mathscr{P}(\hat{F})_{a^{\prime}}^{b^{\prime}}\right),
$$

where $\mathscr{P}(\hat{F}) f$ is the unique arrow from $\mathscr{P}(\hat{F})_{a}^{b}$ to $\mathscr{P}(\hat{F})_{a^{\prime}}^{b^{\prime}}$, determined by the universal property of $\mathscr{P}(\hat{F})_{a^{\prime}}^{b^{\prime}}$. The fact that $\mathscr{P}(\hat{F})$ maps identities to identities and respects composition follows from universal properties of certain limits involved. Moreover, $\mathscr{P}(\hat{F})$ satisfies the sheaf condition by construction (since its values in any interval are determined by an appropriate limit).

We will now prove that there exist an adjunction $\mathscr{K} \dashv \mathscr{P}$, which relates the two perspectives. For this, we will build a pair of natural transformations $\mathscr{K} \mathscr{P} \xrightarrow{\varepsilon} 1_{\mathrm{Cu}(\mathrm{T}, \mathrm{D})}$ and $1_{\mathrm{Pe}(\mathrm{T}, \mathrm{D})} \xrightarrow{\eta} \mathscr{P} \mathscr{K}$ that make the triangle identities commute:
![](https://cdn.mathpix.com/cropped/ca25655d-fbfb-48e6-bc70-6703e81dac02-12.jpg?height=229&width=362&top_left_y=1381&top_left_x=603)
![](https://cdn.mathpix.com/cropped/ca25655d-fbfb-48e6-bc70-6703e81dac02-12.jpg?height=229&width=373&top_left_y=1381&top_left_x=1151)

We need to define the components $\mathscr{K} \mathscr{P}(\hat{F}) \xrightarrow{\varepsilon_{\hat{F}}} 1_{\mathrm{Cu}(\mathrm{T}, \mathrm{D})}(\hat{F})$ for every cosheaf in $\mathrm{Cu}(\mathrm{T}, \mathrm{D})$. This involves choosing natural transformations $\varepsilon_{\hat{F}_{a}^{b}}: \mathscr{K} \mathscr{P}(\hat{F})_{a}^{b} \rightarrow \hat{F}_{a}^{b}$ for each interval $[a, b]$ in T. As $\mathscr{K} \mathscr{P}(\hat{F})_{a}^{b}$ is a colimit, there exists only one such arrow. We define $\varepsilon_{\hat{F}_{a}^{b}}$ to be this unique arrow, as illustrated in the cummutative diagram on the left:
![](https://cdn.mathpix.com/cropped/ca25655d-fbfb-48e6-bc70-6703e81dac02-12.jpg?height=501&width=671&top_left_y=1897&top_left_x=337)
![](https://cdn.mathpix.com/cropped/ca25655d-fbfb-48e6-bc70-6703e81dac02-12.jpg?height=499&width=680&top_left_y=1899&top_left_x=1110)

Applying a dual argument, we can construct $1_{\operatorname{Pe}(\mathrm{T}, \mathrm{D})} \xrightarrow{\eta} \mathscr{P} \mathscr{K}$ using the natural transformations $\eta_{F_{a}^{b}}$, as illustrated in the diagram on the right. The existence of these natural transformations $\varepsilon$ and $\eta$ is sufficient to ensure that the triangle identities commute. This is attributed to the universal map properties of $\mathscr{K} \mathscr{P}(\hat{F})_{a}^{b}$ and $\mathscr{P} \mathscr{K}(F)_{a}^{b}$, respectively. $\square$

From a practical perspective, Theorem 2.10 implies that in general there is the potential for a loss of information when one passes from one perspective (the persistent one, say) to another (the cumulative one) and back again. Furthermore the precise way in which this information may be lost is explicitly codified by the unit $\eta$ and co-unit $\varepsilon$ of the adjunction. These observations, which were hidden in other encodings of temporal data [32, 23, 9], are of great practical relevance since it means that one must take a great deal of care when collecting temporal data: the choices of mathematical representations may not be interchangeable.

### 2.4 Collecting Examples: Narratives are Everywhere

Temporal graphs. Think of satellites orbiting around the earth where, at each given time, the distance between any two given satellites determines their ability to communicate. To understand whether a signal can be sent from one satellite to another one needs a temporal graph: it does not suffice to solely know the static structure of the time-indexed communication networks between these satellites, but instead one needs to also keep track of the relationships between these snapshots. We can achieve this with narratives of graphs, namely cosheaves (or sheaves, if one is interested in the persistent model) of the form $\mathcal{G}: T \rightarrow$ Grph from a time category T into Grph, $a$ category of graphs ${ }^{5}$ There are many ways in which one could define categories of graphs; for the purposes of recovering definitions from the literature we will now briefly review the category of graphs we choose to work with.

We view graphs as objects in Set ${ }^{\mathrm{SGr}}$, the functor category from the graph schema to set. It has as objects functors $G$ : SGr → Set where SGr is thought of as a schema category with only two objects called $E$ and $V$ and two non-identity morphisms $s, t: E \rightarrow V$ which should be thought as mnemonics for 'source' and 'target'. We claim that Set ${ }^{\mathrm{SGr}}$ is the category of directed multigraphs and graph homomorphisms. To see this, notice that any functor $G$ : SGr → Set consists of two sets: $G(E)$ (the edge set) and $G(V)$ (the vertex set). Moreover each edge $e \in G(E)$ gets mapped to two vertices (namely its source $G(s)(e)$ and target $G(t)(e)$ ) via the functions $G(s): G(E) \rightarrow G(V)$ and $G(t): G(E) \rightarrow G(V)$. Arrows in Set ${ }^{\mathrm{SGr}}$ are natural transformations between functors. To see that natural transformations $\eta: G \Rightarrow H$ define graph homomorphisms, note that any such $\eta$ consists of functions $\eta_{E}: G(E) \rightarrow H(E)$ and $\eta_{V}: G(V) \rightarrow H(V)$ (its components at $E$ and $V$ ) which commute with the source and target maps of $G$ and $H$.

The simplest definition of temporal graphs in the literature is that due to Kempe, Kleinberg and Kumar [23] which views temporal graphs as a sequence of edge sets over a fixed vertex set.

Definition 2.11 ([23]). A temporal graph $\mathcal{G}$ consists of a pair $\left(V,\left(E_{i}\right)_{i \in \mathbb{N}}\right)$ where $V$ is a set and $\left(E_{i}\right)_{i \in \mathbb{N}}$ is a sequence of binary relations on $V$.

The above definition can be immediately formulated in terms of our discrete cumulative (resp. persistent) graph narratives whereby a temporal graph is a cumulative narrative valued in the category Set ${ }^{\mathrm{SGr}}$ with discrete time. To see this, observe that, since Definition 2.11 assumes a fixed vertex set and since it assumes simple graphs, the cospans (resp. spans) can be inferred from the snapshots (see Figure 2 for examples). For instance, in the persistent case, there is one maximum common subgraph to use as the apex of each span associated to the inclusions of intervals of length zero into intervals of length one. This, combined with Proposition 2.9 yields a unique persistent graph narrative which encodes any given temporal graph (as given in Definition 2.11).

Notice that once an edge or vertex disappears in a persistent (or cumulative) graph narrative, it can never reappear: the only way to reconnect two vertices is to create an entirely new edge. In particular this means that cumulative graph narratives associate to most intervals of time a multigraph rather than a simple graph (see Figure 2c). This is a very natural requirement, for instance: imagining a good being delivered from $u$ to $v$ at

[^6]![](https://cdn.mathpix.com/cropped/ca25655d-fbfb-48e6-bc70-6703e81dac02-14.jpg?height=618&width=1428&top_left_y=296&top_left_x=345)
Figure 2: A temporal graph along with its persistent and cumulative narratives

times $t$ and $t^{\prime}$, it is clear that the goods need not be delivered by the same person and, in any event, the very acts of delivery are different occurrences ${ }^{6}$

As shown by Patterson, Lynch and Fairbanks [35], by passing to slice categories, one can furthermore encode various categories of labelled data. For instance, one can fix the monoid of natural numbers viewed as a single-vertex graph with a loop edge for each natural number $G_{B \mathbb{N}}:$ SGr $\rightarrow$ Set having $G_{B \mathbb{N}}(V)=1$ and $G_{B \mathbb{N}}(E)=\mathbb{N}$ ) and consider the slice category Set ${ }^{\mathrm{SGr}} / G_{B \mathbb{N}}$. This will have pairs ( $G, \lambda: G \rightarrow G_{B \mathbb{N}}$ ) as objects where $G$ is a graph and $\lambda$ is a graph homomorphism effectively assigning a natural number label to each edge of $G$. The morphisms of Set ${ }^{\mathrm{SGr}} / G_{B \mathbb{N}}$ are label-preserving graph homomorphisms. Thus narratives valued in Set ${ }^{\mathrm{SGr}} / G_{B \mathbb{N}}$ can be interpreted as time-varying graphs whose edges come equipped with latencies (which can change with time).

By similar arguments, it can be easily shown that one can encode categories of graphs which have labeled vertices and labeled edges [35]. Narratives in such categories correspond to time-varying graphs equipped with both vertex- and edge-latencies. This allows us to recover the following notion, due to Casteigts, Flocchini, Quattrociocchi and Santoro, of a time-varying graph which has recently attracted much attention in the literature.

Definition 2.12 (Section 2 in [9]). Take $\mathbb{T}$ to be either $\mathbb{N}$ or $\mathbb{R}$. A $\mathbb{T}$-temporal (directed) network is a quintuple ( $G, \rho_{e}, \eta_{e}, \rho_{v}, \eta_{v}$ ) where $G$ is a (directed) graph and $\rho_{e}, \eta_{e}, \rho_{v}$ and $\eta_{v}$ are functions of the following types:

$$
\begin{array}{lc}
\rho_{e}: E(G) \times \mathbb{T} \rightarrow\{\perp, \top\}, & \eta_{e}: E(G) \times \mathbb{T} \rightarrow \mathbb{T}, \\
\rho_{v}: V(G) \times \mathbb{T} \rightarrow\{\perp, \top\}, & \eta_{v}: V(G) \times \mathbb{T} \rightarrow \mathbb{T}
\end{array}
$$

where $\rho_{e}$ and $\rho_{v}$ are are functions indicating whether an edge or vertex is active at a given time and where $\eta_{e}$ and $\eta_{v}$ are latency functions indicating the amount of time required to traverse an edge or vertex.

We point out that this definition, stated as in [9] does not enforce any coherence conditions to ensure that edges are present at times in which their endpoints are. Our approach, in contrast, comes immediately equipped with all such necessary coherence conditions.

[^7]Other structures. There exist diverse types of graphs, such as reflexive, symmetric, and half-edge graphs, each characterized by the nature of the relation aimed to be modeled. Each graph type assemble into specific categories, and the selection of graph categories distinctly shapes the resulting graph narratives. To systematically investigate the construction of various graph narratives, we employ a category-theoretic trick. This involves encoding these diverse graphs as functors, specifically set-valued copresheaves, over a domain category known as a schema. The schema encapsulates the syntax of a particular graph type (e.g., symmetric graphs, reflexive graphs, etc.), allowing us to encode a multitude of structures. Notable examples of such schemata include SSGr, reflexive graphs SRGr, symmetric-and-reflexive graphs SSRGr and half-edge graphs SHeGr.
![](https://cdn.mathpix.com/cropped/ca25655d-fbfb-48e6-bc70-6703e81dac02-15.jpg?height=209&width=1310&top_left_y=745&top_left_x=414)

$$
\begin{array}{llll}
\text { s.t. } s \circ i=t \text { and } t \circ i=s & \text { s.t. } s \circ \ell=t \circ \ell & \text { s.t. } s \circ i=t \text { and } t \circ i=s \text { and } s \circ \ell=t \circ \ell & \text { s.t. inv ∘ inv }=\operatorname{id}_{H}
\end{array}
$$

These are all subcategories of multigraphs but other relational structures of higher order such as Petri nets and simplicial complexes can also be constructed using this approach. For instance, the following is the schema for Petri nets [35]:
![](https://cdn.mathpix.com/cropped/ca25655d-fbfb-48e6-bc70-6703e81dac02-15.jpg?height=283&width=577&top_left_y=1258&top_left_x=775)

It is known that all of these categories of CSets are presheaf toposes (and thus admit limits and colimits which are computed point-wise) and thus we can define narratives as presheaves $F: \mathrm{T}^{o p} \rightarrow$ CSet satisfying the sheaf condition stated in Proposition 2.7 for any choice of schema (e.g., SSGr, SRGr, SSRGr SHeGr, etc.).

Note 2.13 (Beyond relational structures). Proposition 2.7 indeed states that we can define narratives valued in any category that has limits and/or colimits. For instance, the category Met of metric spaces and contractions is a complete category, allowing us to study persistent Met-narratives. Diagram 5 illustrates a Met-narrative that recounts the story of how the geographical distances of ice cream companies in Venice changed over time. Each snapshot (depicted in pink) represents a metric space, and all morphisms are canonical isometries. The curious reader can use it to speculate about why company $b$ ceased its activities and what happened to the physical facilities of companies $a_{1}$ and $c$.
![](https://cdn.mathpix.com/cropped/ca25655d-fbfb-48e6-bc70-6703e81dac02-15.jpg?height=339&width=1450&top_left_y=2036&top_left_x=317)

### 2.5 Temporal Analogues of Static Properties

The theory of static data (be it graph theory, group theory, etc.) is far better understood than its temporal counterpart (temporal graphs, temporal groups, etc.). For this reason and since static properties are often easier to think of, it is natural to try to lift notions from the static setting to the temporal.

This idea has been employed very often in temporal graph theory for instance with the notion of a temporal path. In this section we will consider temporal paths and their definition in terms of graph narratives. This section is a case-study intended to motivate our more general approach in Section 2.5.

### 2.5.1 Temporal Paths

As we mentioned in Section 1.1, one easy way of defining the notion of a temporal path in a temporal graph $\mathcal{G}$ is to simply declare it to be a path in the underlying static graph of $\mathcal{G}$. However, at first glance (and we will address this later on) this notion does not seem to be particularly 'temporal' since it is forgetting entirely the various temporal relationships between edges and vertices. In contrast (using Kempe et. al.'s Definition 2.11 of a temporal graph) temporal paths are usually defined as follows (we say that these notions are '(K3)-temporal' to make it clear that they are defined in terms of Kempe, Kleinberg and Kumar's definition of a temporal graph).

Definition 2.14 ((K3)-temporal paths and walks). Given vertices $x$ and $y$ in a temporal graph ( $G, \tau$ ), a temporal $(x, y)$-walk is a sequence $W=\left(e_{1}, t_{1}\right), \ldots,\left(e_{n}, t_{n}\right)$ of edge-time pairs such that $e_{1}, \ldots, e_{n}$ is a walk in $G$ starting at $x$ and ending at $y$ and such that $e_{i}$ is active at time $t_{i}$ and $t_{1} \leq t_{2} \leq \cdots \leq t_{n}$. We say that a temporal $(x, y)$-walk is closed if $x=y$ and we say that it is strict if the times of the walk form a strictly increasing sequence.

Using this definition, one also has the following natural decision problem on temporal graphs.

```
Temp $_{K^{3}}$ Path $_{n}$
Input: a (K3)-temporal graph $G:=\left(V,\left(E_{i}\right)_{i \in \mathbb{N}}\right)$ and an $n \in \mathbb{N}$
Task: determine if there exists a (K3)-temporal path of length at least $n$ in $G$.
```

Notice that in static graph theory most computational problems can be cast as homomorphism problems in appropriate categories of graphs. For instance, the question of determining whether a fixed graph $G$ admits a path of length at least $n$ is equivalent to asking if there is at least one injective homomorphism $P_{n} \hookrightarrow G$ from the $n$-path to $G$. Similarly, if we wish to ask if $G$ contains a clique on $n$ vertices as a minor ${ }^{7}$, then this is simply a homomorphism problem in the category Grph ${ }_{\preceq}$ having graphs as objects and graph minors as morphisms: $G$ contains $K_{n}$ as a minor if and only if the hom-set $\operatorname{Grph}_{\preceq}\left(K_{n}, G\right)$ is nonempty.

Wishing to emulate this pattern from traditional graph theory, one immediately notices that, in order to define notions such as temporal paths, cliques and colorings (to name but a few), one first needs two things:

1. a notion of morphism of temporal graphs and
2. a way of lifting graph classes to classes of temporal graphs (for instance defining temporal path-graphs, temporal complete graphs, etc...).

Fortunately our narratives come equipped with a notion of morphism (these are simply natural transformations between the functors encoding the narratives). Thus, all that remains to be determined is how to convert classes of graphs into classes of temporal graphs. More generally we find ourselves interested in converting classes of objects of any category C into classes of C-narratives. We will address these questions in an even more general manner (Propositions 2.15 and 2.16 by developing a systematic way for converting C -narratives into D -narratives whenever we have certain kinds of data-conversion functors $K: \mathrm{C} \rightarrow \mathrm{D}$.

[^8]Proposition 2.15 (Covariant Change of base). Let C and D be categories with limits (resp. colimits) and let T be any time category. If $K: \mathrm{C} \rightarrow \mathrm{D}$ is a continuous functor, then composition with $K$ determines a functor $(K \circ-)$ from persistent (resp. cumulative) C -narratives to persistent (resp. cumulative) D narratives. Spelling this out explicitly for the case of persistent narratives, we have:

$$
\begin{aligned}
& (K \circ-): \operatorname{Pe}(\mathrm{T}, \mathrm{C}) \rightarrow \operatorname{Pe}(\mathrm{T}, \mathrm{D}) \\
& (K \circ-):\left(F: \mathrm{T}^{o p} \rightarrow \mathrm{C}\right) \mapsto\left(K \circ F: \mathrm{T}^{o p} \rightarrow \mathrm{D}\right) .
\end{aligned}
$$

Proof. It is standard to show that $K \circ F$ is a functor of presheaf categories, so all that remains is to show that it maps any C -narrative $F: \mathrm{T}^{o p} \rightarrow \mathrm{C}$ to an appropriate sheaf. This follows immediately since $K$ preserves limits: for any cover $([a, p],[p, b])$ of any interval $[a, b]$ we have $(K \circ F)([a, b]))=K\left(F([a, p]) \times_{F([p, p])} F([p, b])\right)= \left.(K \circ F)([a, p]) \times_{(K \circ F)([p, p])}(K \circ F)([p, b])\right)$. By duality the case of cumulative narratives follows.

Notice that one also has change of base functors for any contravariant functor $L$ : $C^{o p} \rightarrow \mathrm{D}$ taking limits in C to colimits in D. This yields the following result (which can be proven in the same way as Proposition 2.15).

Proposition 2.16 (Contravariant Change of base). Let C be a category with limits (resp. colimits) and D be a category with colimits (resp. limits) and let T be any time category. If $K: \mathrm{C}^{o p} \rightarrow \mathrm{D}$ is a functor taking limits to colimits (resp. colimits to limits), then the composition with $K$ determines a functor from persistent (resp. cumulative) C-narratives to cumulative (resp. persistent) D-narratives.

To see how these change of base functors are relevant to lifting classes of objects in any category C to corresponding classes of C -narratives, observe that any such class P of objects in C can be identified with a subcategory $P: \mathrm{P} \rightarrow \mathrm{C}$. One should think of this as a functor which picks out those objects of C that satisfy a given property $P$. Now, if this functor $P$ is continuous, then we can apply Proposition 2.15 to identify a class

$$
(P \circ-): \operatorname{Pe}(\mathrm{T}, \mathrm{P}) \rightarrow \operatorname{Pe}(\mathrm{T}, \mathrm{C})
$$

of C -narratives which satisfy the property $P$ at all times. Similar arguments let us determine how to specify temporal analogues of properties under the cumulative perspective. For example, consider the full subcategory $\mathfrak{P}$ : Paths ↪ Grph which defines the category of all paths and the morphisms between them. As the following proposition shows, the functor $\mathfrak{P}$ determines a subcategory $\mathrm{Cu}(\mathrm{T}, \mathrm{Paths}) \hookrightarrow \mathrm{Cu}(\mathrm{T}, \mathrm{Grph})$ whose objects are temporal path-graphs.

Proposition 2.17. The monic cosheaves in $\mathrm{Cu}(\mathrm{T}$, Paths $)$ determine temporal graphs (in the sense of Definition 2.11) whose underlying static graph over any interval of time is a path. Furthermore, for any graph narrative $\mathcal{G} \in \mathrm{Cu}(\mathrm{T}, \operatorname{Grph})$ all of the temporal paths in $\mathcal{G}$ assemble into a poset $\mathrm{Sub}_{(\mathfrak{P o -})}(\mathcal{G})$ defined as the subcategory of the subobject category $\operatorname{Sub}(\mathcal{G})$ whose objects are in the range of $(\mathfrak{P} \circ-)$. Finally, strict temporal paths in a graph narrative $\mathcal{G}$ consists of all those monomorphism $\mathfrak{P}(\mathcal{P}) \hookrightarrow \mathcal{G}$ where the path narrative $P$ in $\operatorname{Sub}_{(\mathfrak{P} \circ-)}(\mathcal{G})$ sends each instantaneous interval (i.e. one of the form $[t, t]$ ) to a single-edge path.

Proof. Since categories of copresheaves are adhesive [26] (thus their pushouts preserve monomorphims), one can verify that, when they exists (pushouts of paths need not be paths in general), pushouts in Paths are given by computing pushouts in Grph. Thus a monic cosheaf $P$ in $\mathrm{Cu}(\mathrm{T}$, Paths $)$ is necessarily determined by paths for each interval of time that combine (by pushout) into paths at longer intervals, as desired. Finally, by noticing that monomorphisms of (co)sheaves are simply natural transformations whose components are all monic, one can verify that any monomorphism from $\mathfrak{P}(\mathcal{P})$ to $\mathcal{G}$ in the category of graph narratives determines a temporal path of $\mathcal{G}$ and that this temporal path is strict if $\mathcal{P}([t, t])$ is a path on at most one edge for all $t \in \mathrm{~T}$. Finally, as is standard in category theory [3], observe that one can collect all such monomorphisms (varying $P$ over all objects of $\mathrm{Cu}(\mathrm{T}$, Paths)) into a subposet of the subobject poset of $\mathcal{G}$, which, by our preceding observation, determines all of the temporal paths in $\mathcal{G}$.

Comparing the Cumulative to the Persistent. Given Proposition 2.17 one might wonder what a temporal path looks like under the persistent perspective. By duality (and since pullbacks preserve monomorphisms and connected subgraphs of paths are paths) one can see that monic persistent path narratives must consist of paths at each snapshot satisfying the property that over any interval the data persisting over that interval is itself a path.

Since applying the functor $\mathscr{P}: \mathrm{Cu}(\mathrm{T}, \mathrm{Paths}) \rightarrow \mathrm{Pe}(\mathrm{T}, \mathrm{Paths})$ of Theorem 2.10 turns any cumulative path narrative into a persistent one, it seem at first glance that there is not much distinction between persistent temporal paths and those defined cumulatively in Proposition 2.17. However, the distinction becomes apparent once one realises that in general we cannot simply turn a persistent path narrative into a cumulative one: in general arbitrary pushouts of paths need not be paths (they can give rise to trees).

Realizing the distinctions between cumulative and persistent paths is a pedagogical example of a subtlety that our systematic approach to the study of temporal data can uncover but that would otherwise easily go unnoticed: in short, this amounts to the fact that studying the problem of the temporal tree (defined below) is equivalent to studying the persistent temporal path problem.

To make this idea precise, consider the adjunction
![](https://cdn.mathpix.com/cropped/ca25655d-fbfb-48e6-bc70-6703e81dac02-18.jpg?height=140&width=669&top_left_y=958&top_left_x=726)
given to us by Theorem 2.10 (notice that the result applies since Grph has all limits and colimits). This together with Proposition 2.15 applied to the full subcategory $\mathfrak{T}$ : Trees ${ }_{\text {mon }} \rightarrow \mathrm{Grph}_{\text {mono }}$ yields the following diagram.
![](https://cdn.mathpix.com/cropped/ca25655d-fbfb-48e6-bc70-6703e81dac02-18.jpg?height=248&width=682&top_left_y=1256&top_left_x=721)

The pullback (in Cat) of this diagram (i.e. of ( $\mathfrak{T} \circ-$ ) and $\mathscr{K} \circ(\mathfrak{P} \circ-)$ ) yields a category having as objects pairs $(\mathcal{T}, \mathcal{P})$ consisting of a cumulative tree narrative $\mathcal{T}$ and a persistent path narrative $\mathcal{P}$ such that, when both are viewed as cumulative $\mathrm{Grph}_{\text {mono }}$-narratives, they give rise to the same narrative. Thus we see that the question of determining whether a cumulative graph narrative $\mathcal{G}$ contains $\mathfrak{T}(\mathcal{T})$ as a sub-narrative can be reduced to the question of determining whether $P$ is a persistent path sub-narrative of $\mathscr{P}(\mathcal{G})$.

Aside 2.18. Although it is far beyond the scope of this paper, we believe that there is a wealth of understanding of temporal data (and in particular temporal graphs) to be gained from the interplay of lifting graph properties and the persistent-cumulative adjunction of Theorem 2.10. For instance the preceding discussion shows that one can equivalently study persistent paths instead of thinking about cumulative temporal trees. Since persistent paths are arguably easier to think about (because paths are fundamentally simpler objects than trees) it would stand to reason that this hidden connection between these classes of narratives could aid in making new observations that have so far been missed.

### 2.5.2 Changing the Resolution of Temporal Analogues.

As we have done so far, imagine collecting data over time from some hidden dynamical system and suppose, after some exploratory analysis of our data, that we notice the emergence of some properties in our data that are only visible at a certain temporal resolution. For example it might be that some property of interest is only visible if we accumulate all of the data we collected over time intervals whose duration is at least ten seconds.

In contrast notice that the temporal notions obtained solely by 'change of base' (i.e. via functors such as (6)) are very strict: not only do they require each instantaneous snapshot to satisfy the given property $P$, they also
require the property to be satisfied by any data that persists (or, depending on the perspective, accumulates) over time. For instance the category of temporal paths of Proposition 2.17 consists of graph narratives that are paths at all intervals. In this section we will instead give a general, more permissive definition of temporal analogues or static notions. This definition will account for the fact that one is often only interested in properties that emerge at certain temporal resolutions, but not necessarily others.

To achieve this, we will briefly explain how to functorially change the temporal resolution of our narratives (Proposition 2.19). Then, combining this with our change of base functors (Propositions 2.15 and 2.16) we will give an extremely general definition of a temporal analogue of a static property. The fact that this definition is parametric in the temporal resolution combined with the adjunction that relates cumulative and persistent narratives (Theorem 2.10) leads to a luscious landscape of temporal notions whose richness can be systematically studied via our category-theoretic perspective.

Proposition 2.19 (Change of Temporal Resolution). Let T be a time category and $\mathrm{S} \stackrel{\tau}{\hookrightarrow} \mathrm{T}$ be a sub-joinsemilattice thereof. Then, for any category C with (co)limits, there is a functor $(-\circ \tau)$ taking persistent (resp. cumulative) C narratives with time T to narratives of the same kind with time $S$.

Proof. By standard arguments the functor is defined by post composition as

$$
(-\circ \tau): \mathrm{Cu}(\mathrm{~T}, \mathrm{C}) \rightarrow \mathrm{Cu}(\mathrm{~S}, \mathrm{C}) \quad \text { where } \quad(-\circ \tau):(\mathcal{F}: \mathrm{T} \rightarrow \mathrm{C}) \mapsto(\mathcal{F} \circ \tau: \mathrm{S} \rightarrow \mathrm{C}) .
$$

The persistent case is defined in the same way. $\square$

Thus, given a sub-join-semilattice $\tau: S \hookrightarrow \mathrm{~T}$ of some time-category T , we would like to specify the collection of objects of a category of narratives that satisfy some given property $P$ only over the intervals in $S$. A slick way of defining this is via a pullback of functors as in the following definition.

Definition 2.20. Let $\tau: S \hookrightarrow T$ be a sub-join-semilattice of a time category $T$ let $C$ be a category with limits and let $P: \mathrm{P} \hookrightarrow \mathrm{C}$ be a continuous functor. Then we say that a persistent C -narrative with time T $\tau$-satisfies the property $P$ if it is in the image of the pullback (i.e. the red, dashed functor in the following diagram) of $(-\circ \tau)$ along $(P \circ-\circ \tau)$. An analogous definition also holds for cumulative narratives when C has colimits and P is continuous.
![](https://cdn.mathpix.com/cropped/ca25655d-fbfb-48e6-bc70-6703e81dac02-19.jpg?height=160&width=1023&top_left_y=1641&top_left_x=554)

As a proof of concept, we shall see how Definition 2.20 can be used to recover notions of temporal cliques as introduced by Viard, Latapy and Magnien [42].

Temporal cliques were thought of as models of groups of people that commonly interact with each other within temporal contact networks. Given the apparent usefulness of this notion in epidemiological modeling and since the task of finding temporal cliques is algorithmically challenging, this notion has received considerable attention recently [18, 5, 6, 19, 33, 41]. They are typically defined in terms of Kempe, Kleinberg and Kumar's definition of a temporal graph (Definition 2.11) (or equivalently in terms of link streams) where one declares a temporal clique to be a vertex subset $S$ of the time-invariant vertex set such that, cumulatively, over any interval of length at least some given $k, S$ induces a clique. The formal definition follows.

Definition 2.21 ([42]). Given a (K3)-temporal graph $G:=\left(V,\left(E_{i}\right)_{i \in \mathbb{N}}\right.$ ) and an $n \in \mathbb{N}$, a subset $S$ of $V$ is said to be a temporal $k$ clique if $|S| \geq k$ and if for all intervals $[a, b]$ of length $n$ in $\mathbb{N}$ (i.e. $b=a+n-1$ ) one has that: for all $x, y \in S$ there is an edge incident with both $x$ and $y$ in $\bigcup_{t \in[a, b]} E_{t}$.

Now we will see how we can obtain the above definition as an instance of our general construction of Definition 2.20. We should note that the following proposition is far more than simply recasting a known definition into more general language. Rather, it is about simultaneously achieving two goals at once.

1. It is showing that the instantiation of our general machinery (Definition 2.20) recovers the specialized definition (Definition 2.21).
2. It provides an alternative characterization of temporal cliques in terms of morphisms of temporal graphs. This generalizes the traditional definitions of cliques in static graph theory as injective homomorphisms into a graph from a complete graph.

Proposition 2.22. Let $\kappa_{\geq k}$ : Complete ${ }^{\geq k} \hookrightarrow$ Grph be the subcategory of Grph whose objects are complete graphs on at least $k$ vertices and let $\tau_{\geq n}: \mathrm{T} \rightarrow \mathrm{I}_{\mathbb{N}}$ be the sub-join-semilattice of $\mathrm{I}_{\mathbb{N}}$ whose objects are intervals of $\mathrm{T}_{\mathbb{N}}$ length at least $n$. Consider any graph narrative $\mathcal{K}$ which $\tau_{n}$-satisfies $\kappa_{\geq k}$ then all of its instantaneous snapshots $\mathcal{K}([t, t])$ have at least $k$ vertices. Furthermore consider any monomorphism $f: \mathcal{K} \hookrightarrow \mathcal{G}$ from such a $\mathcal{K}$ to any given cumulative graph narrative $\mathcal{G}$. If $\mathcal{K}$ preserves monomorphisms, then we have that: every such morphism of narratives $f$ determines a temporal clique in $\mathcal{G}$ (in the sense of Definition 2.21) and moreover all temporal cliques in $\mathcal{G}$ are determined by morphisms of this kind.

Proof. First of all observe that if a pushout $L+_{M} R$ of a span graphs $L \stackrel{\ell}{\leftarrow} M \stackrel{r}{\rightarrow} R$ is a complete graph, then we must have that at least one of the graph homomorphisms $\ell$ and $r$ must be surjective on the vertex set (if not then there would be some vertex of $L$ not adjacent to some vertex of $R$ in the pushout). With this in mind now consider any cumulative graph narrative $\mathcal{K}$ which $\tau_{\geq n}$-satisfies $\kappa_{\geq k}$. By Definition 2.20 this means that for all intervals $[a, b]$ of length at least $n$ the graph $\mathcal{K}([a, b])$ is in the range of $\kappa_{\geq k}$ : i.e. it is a complete graph on at least $k$ vertices. This combined with the fact that $\mathcal{K}$ is a cumulative narrative implies that every pushout of the form

$$
\mathcal{K}([a, p])+_{\mathcal{K}([p, p])} \mathcal{K}([p, b])
$$

yields a complete graph and hence every pair of arrows

$$
\mathcal{K}([a, p]) \stackrel{\ell}{\leftarrow} \mathcal{K}([p, p]) \xrightarrow{r} \mathcal{K}([p, b])
$$

must have at least one of $\ell$ or $r$ surjective. From this one deduces that for all times $t \geq n$ every instantaneous graph $\mathcal{K}([t, t])$ must have at least $k$ vertices: since $\mathcal{K} \tau_{\geq n}$-satisfies $\kappa_{\geq k}$, the pushout of the span

$$
\mathcal{K}([t-n+1, t])+_{\mathcal{K}([t, t])} \mathcal{K}([t, t+n-1])
$$

must be a complete graph on at least $k$ vertices and this is also true of both feet of this span, thus we are done by applying the previous observation.

Observe that, if $S$ is a vertex set in $\mathcal{G}$ which determines a temporal clique in the sense of Definition 2.21, then this immediately determines a cumulative graph narrative $\mathcal{K}$ which $\tau_{\geq n}$-satisfies $\kappa_{\geq k}$ and that has a monomorphism into $\mathcal{G}$ : for any interval $[a, b], \mathcal{K}([a, b])$ is defined as the restriction (i.e. induced subgraph) of $\mathcal{G}([a, b])$ to the vertices in $S$. The fact that $\mathcal{K}$ preserves monomorphisms follows since $\mathcal{G}$ does.

For the converse direction, notice that, if $\mathcal{K}$ preserves monomorphisms (i.e. the projection maps of its cosheaf structure are monomorphisms), then, by what we just argued, for any interval $[a, b]$ we have $|\mathcal{K}([a, b])| \geq|\mathcal{K}([a, a])| \geq k$. Thus, since all of the graphs of sections have a lower bound on their size, we have that there must exist some time $t$ such that $\mathcal{K}([t, t+n-1])$ has minimum number of vertices. We claim that the vertex-set of $\mathcal{K}([t, t+n-1])$ defines a temporal clique in $\mathcal{G}$ (in the sense of Definition 2.21). To that end, all that we need to show is that the entire vertex set of $\mathcal{K}([t, t+n-1])$ is active in every interval of length exactly $n$. To see why, note that, since all of the projection maps in the cosheaf $\mathcal{K}$ are monic, every interval of length at least $n$ will contain all of the vertex set of $\mathcal{K}([t, t+n-1])$; furthermore each pair of vertices will be connected by at least one edge in the graphs associated to such intervals since $\mathcal{K} \tau_{\geq n}$-satisfies $\kappa_{\geq k}$.

Thus, to conclude the proof, it suffices to show that for all times $s \geq n-1$ we have that every vertex of $\mathcal{K}([t, t+n-1])$ is contained in $\mathcal{K}([s, s])$ (notice that for smaller $s$ there is nothing to show since there is no interval $\left[s^{\prime}, s\right]$ of length at least $n$ which needs to witness a clique on the vertex set of $\mathcal{K}([t, t+n-1])$ ). To that end we distinguish three cases.

1. Suppose $s \notin[t, t+n-1]$, then, if $s>t+n-1$, consider the diagram of monomorphisms
![](https://cdn.mathpix.com/cropped/ca25655d-fbfb-48e6-bc70-6703e81dac02-21.jpg?height=306&width=899&top_left_y=575&top_left_x=657)
and observe by our previous arguments that $\ell$ or $r$ must be surjective on vertices. We claim that $\ell$ is always a vertex-surjection: if $r$ is surjective on vertices, then, by the minimality of the number of vertices of $\mathcal{K}([t, t+n-1])$ and the fact that the diagram is monic, we must have that $\ell$ is surjective on vertices. But then this yields the desired result since we have a diagram of monomorphisms. Otherwise, if $s<t$ either $s<n-1$ (in which case there is nothing to show), or a specular argument to the one we just presented for case of $s>t+n-1$ suffices.
2. If $s \in[t, t+n-1]$, then consider the following diagram
![](https://cdn.mathpix.com/cropped/ca25655d-fbfb-48e6-bc70-6703e81dac02-21.jpg?height=145&width=1398&top_left_y=1263&top_left_x=403)
and observe that, by the same minimality arguments as in the previous point, we have that $f$ and $g$ must be surjective on vertices. By what we argued earlier, one of $\alpha$ and $\beta$ must be surjective on vertices; this combined with the fact that there are monomorphisms

$$
\mathcal{K}([t, t]) \hookrightarrow \mathcal{K}([s-n+1, s]) \text { and } \mathcal{K}([t+n-1, t+n-1]) \hookrightarrow[s, s+n-1]
$$

(since $t \in[s-n+1, s]$ and $t+n-1 \in[s, s+n-1]$ ) implies that every vertex of $\mathcal{K}([t, t+n-1])$ is contained in $\mathcal{K}([s, s])$ as desired.

In the world of static graphs, it is well known that dual to the notion of a clique in a graph is that of a proper coloring. This duality we refer to is not merely aesthetics, it is formal: if a clique in a graph $G$ is a monomorphism from a complete graph $K_{n}$ into $G$, then a coloring of $G$ is a monomorphism $K_{n} \hookrightarrow G$ in the opposite category. Note that this highlights the fact that different categories of graphs give rise to different notions of coloring via this definition (for instance note that, although the typical notion of a graph coloring is defined in terms of irreflexive graphs, the definition given above can be stated in any category of graphs).

In any mature theory of temporal data and at the very least any theory of temporal graphs, one would expect there to be similar categorical dualities at play. And indeed there are: by dualizing Proposition 2.22, one can recover different notions of temporal coloring depending on whether one studies the cumulative or persistent perspectives. This is an illustration of a much deeper phenomenon whereby stating properties of graphs in a categorical way allows us to both lift them to corresponding temporal analogues while also retaining the ability to explore how they behave by categorical duality.

## 3 Discussion: Towards a General Theory of Temporal Data

Here we tackled the problem of building a robust and general theory of temporal data. First we distilled a list of five desiderata (see (D1), (D2), (D3), (D4), (D5) in Section 1 ) for any such theory by drawing inspiration from the study of temporal graphs, a relatively well-developed branch of the mathematics of time-varying data.

Given this list of desiderata, we introduced the notion of a narrative. This is a kind of sheaf on a poset of intervals (a join-semilattice thereof, to be precise) which assigns to each interval of time an object of a given category and which relates the objects assigned to different intervals via appropriate restriction maps. The structure of a sheaf arises immediately from considerations on how to encode the time-varying nature of data, which is not specific to the kinds of mathematical object one chooses to study (Desideratum (D4)). This object-agnosticism allows us to use of a single set of definitions to think of time varying graphs or simplicial complexes or metric spaces or topological spaces or groups or beyond. We expect the systematic study of different application areas within this formalism to be a very fruitful line of future work. Examples abound, but, in favor of concreteness, we shall briefly mention two such ideas:

- The shortest paths problem can be categorified in terms of the free category functor [31]. Since this is an adjoint, it satisfies the continuity requirements to be a change of base functor (Proposition 2.15) and thus one could define and study temporal versions of the algebraic path problem (a vast generalization of shortest paths) by relating narratives of graphs to narratives of categories.
- Metabolic networks are cumulative representations of the processes that determine the physiological and biochemical properties of a cell. These are naturally temporal objects since different reactions may occur at different times. Since reaction networks, one of the most natural data structures to represent chemical reactions, can be encoded as copresheaves [1], one can study time varying reaction networks via appropriate narratives valued in these categories.

Encoding temporal data via narratives equips us with a natural choice of morphism of temporal data, namely: morphism of sheaves. Thus we find that narratives assemble into categories (Desideratum (D1), a fact that allows us to leverage categorical duality to find that narratives come in two flavours (cumulative and persistent, Desideratum (D2) depending on how information is being tracked over time. In sufficiently nice categories, persistent and cumulative narratives are furthermore connected via an adjunction (Theorem 2.10) which allows one to convert one description into the other. As is often the case in mathematics, we expect this adjunction to play an important role for many categories of narratives.

To be able to lift notions from static settings to temporal ones, we find that it suffices to first determine canonical ways to change the temporal resolution of narratives or to change the underlying categories in which they are valued. Both of these tasks can be achieved functorially (Propositions 2.15 and 2.16 and Proposition 2.19 and, embracing minimalism, one finds that they are all that is needed to develop a framework for the systematic lifting of static properties to their temporal counterparts (D3).

Finally, addressing Desideratum (D4), we showed how to obtain change of base functors (Propositions 2.15 and 2.16) which allows for the conversion of narratives valued in one category to another. In the interest of a self-contained presentation, we focused on only one application of these functors; namely that of building a general machinery (Definition 2.20) capable of lifting the definition of a property from any category to suitable narratives valued in it. However, the change of base functors have more far reaching applications than this and should instead be thought of as tools for systematically relating different kinds of narratives arising from the same dynamical system. This line of enquiry deserves its own individual treatment and we believe it to be a fascinating new direction for future work.

In so far as the connection between data and dynamical systems is concerned (Desideratum (D5), our contribution here is to place both the theory of dynamical systems and the theory of temporal data on the same mathematical and linguistic footing. This relies on the fact that Schultz, Spivak and Vasilakopoulou's interval sheaves [39] provide an approach to dynamical systems which is very closely related (both linguistically and mathematically) to our notion of narratives: both are defined in terms of sheaves on categories of intervals. We anticipate that exploring this newfound mathematical proximity between the way one represents temporal data and the axiomatic approach for the theory of dynamical systems will be a very fruitful line of further research in the years to come.

## Acknowledgment

We would like to thank Justin Curry for helpful discussions and for observing connections of our work to topological data analysis. We also thank Kevin Carlson and anonymous reviewers for their helpful suggestions and corrections.

## References

[1] Aduddell, R., Fairbanks, J., Kumar, A., Ocal, P. S., Patterson, E., and Shapiro, B. T. A compositional account of motifs, mechanisms, and dynamics in biochemical regulatory networks. arXiv preprint arXiv:2301.01445 (2023).
[2] Augustine, S. Confessions, volume ii: Books 9-13. edited and translated by c j.-b. hammond. loeb classical library 27, isbn 0-67499693-3, 2016.
[3] Awodey, S. Category theory. Oxford University Press, 2010. ISBN:0199237182.
[4] Backstrom, L., Huttenlocher, D., Kleinberg, J., and Lan, X. Group formation in large social networks: Membership, growth, and evolution. In Proceedings of the 12th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (New York, NY, USA, 2006), KDD '06, Association for Computing Machinery, p. 44-54.
[5] Banerjee, S., and Pal, B. On the enumeration of maximal $(\delta, \gamma)$-cliques of a temporal network. In Proceedings of the ACM India Joint International Conference on Data Science and Management of Data (2019), pp. 112-120.
[6] Bentert, M., Himmel, A.-S., Molter, H., Morik, M., Niedermeier, R., and Saitenmacher, R. Listing all maximal k-plexes in temporal graphs. Journal of Experimental Algorithmics (JEA) 24 (2019), 1-27.
[7] Bumpus, B. M. Generalizing graph decompositions. PhD thesis, University of Glasgow, 2021.
[8] Bumpus, B. M., and Meeks, K. Edge exploration of temporal graphs. Algorithmica (2022), 1-29.
[9] Casteigts, A., Flocchini, P., Quattrociocchi, W., and Santoro, N. Time-varying graphs and dynamic networks. International Journal of Parallel, Emergent and Distributed Systems 27, 5 (2012), 387-408.
[10] Curry, J. Sheaves, Cosheaves and Applications. PhD thesis, University of Pennsylvania, 2014.
[11] Curry, J. M. Topological data analysis and cosheaves. Japan Journal of Industrial and Applied Mathematics 32, 2 (Jul 2015), 333-371.
[12] de Silva, V., Munch, E., and Patel, A. Categorified reeb graphs. Discrete \& Computational Geometry 55, 4 (Jun 2016), 854-906.
[13] Enright, J., and Kao, R. R. Epidemics on dynamic networks. Epidemics 24 (2018), 88-97.
[14] Enright, J., Meeks, K., Mertzios, G. B., and Zamaraev, V. Deleting edges to restrict the size of an epidemic in temporal networks. Journal of Computer and System Sciences 119 (2021), 60-77.
[15] Enright, J., Meeks, K., and Skerman, F. Assigning times to minimise reachability in temporal graphs. Journal of Computer and System Sciences 115 (2021), 169-186.
[16] Fong, B., and Spivak, D. I. An Invitation to Applied Category Theory: Seven Sketches in Compositionality. Cambridge University Press, 2019.
[17] Harary, F., and Gupta, G. Dynamic graph models. Mathematical and Computer Modelling 25, 7 (1997), 79-87.
[18] Hermelin, D., Itzhaki, Y., Molter, H., and Niedermeier, R. Temporal interval cliques and independent sets. Theoretical Computer Science (2023), 113885.
[19] Himmel, A.-S., Molter, H., Niedermeier, R., And Sorge, M. Adapting the bron-kerbosch algorithm for enumerating maximal cliques in temporal graphs. Social Network Analysis and Mining 7 (2017), 1-16.
[20] Holme, P. Modern temporal network theory: a colloquium. The European Physical Journal B 88, 9 (2015), 1-30.
[21] Holme, P., and Saramäki, J. Temporal networks. Physics Reports 519, 3 (2012), 97-125.
[22] Kempe, D., and Kleinberg, J. Protocols and impossibility results for gossip-based communication mechanisms. In The 43rd Annual IEEE Symposium on Foundations of Computer Science, 2002. Proceedings. (2002), pp. 471-480.
[23] Kempe, D., Kleinberg, J., and Kumar, A. Connectivity and inference problems for temporal networks. Journal of Computer and System Sciences 64, 4 (2002), 820-842.
[24] Kempe, D., Kleinberg, J., and Tardos, E. Maximizing the spread of influence through a social network. In Proceedings of the Ninth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (New York, NY, USA, 2003), KDD '03, Association for Computing Machinery, p. 137-146.
[25] Kım, W., and MÉmoli, F. Extracting persistent clusters in dynamic data via möbius inversion. Discrete \& Computational Geometry (Oct 2023).
[26] Lack, S., and Sobocinski, P. Adhesive categories. In Foundations of Software Science and Computation Structures (Berlin, Heidelberg, 2004), I. Walukiewicz, Ed., Springer Berlin Heidelberg, pp. 273-288.
[27] Le Poidevin, R. The Experience and Perception of Time. In The Stanford Encyclopedia of Philosophy, E. N. Zalta, Ed., Summer 2019 ed. Metaphysics Research Lab, Stanford University, 2019.
[28] Leal, W. Exploration of Chemical Space: Formal, chemical and historical aspects. PhD thesis, Dissertation, Leipzig, Universität Leipzig, 2022, 2022.
[29] Llanos, E. J., Leal, W., Luu, D. H., Jost, J., Stadler, P. F., and Restrepo, G. Exploration of the chemical space and its three historical regimes. Proceedings of the National Academy of Sciences 116, 26 (2019), 12660-12665.
[30] MacLane, S., and Moerdijk, I. Sheaves in geometry and logic: A first introduction to topos theory. Springer Science \& Business Media, 2012.
[31] Master, J. The Open Algebraic Path Problem. In LIPIcs Proceedings of CALCO 2021 (2021), Schloss Dagstuhl, pp. 20:1-20:20.
[32] Michail, O. An introduction to temporal graphs: An algorithmic perspective. Internet Mathematics 12, 4 (2016), 239-280.
[33] Molter, H., Niedermeier, R., and Renken, M. Isolation concepts applied to temporal clique enumeration. Network Science 9, S1 (2021), S83-S105.
[34] of Hippo, A. Confessions, Volume I: Books 1-8, vol. 26 of Loeb Classical Library. Harvard University Press, Cambridge, MA, 1912.
[35] Patterson, E., Lynch, O., and Fairbanks, J. Categorical Data Structures for Technical Computing. Compositionality 4 (Dec. 2022).
[36] RiehL, E. Category theory in context. Courier Dover Publications, 2017. ISBN:048680903X.
[37] Rosiak, D. Sheaf Theory through Examples. The MIT Press, 102022.
[38] Ruget, A.-S., Rossi, G., Pepler, P. T., Beaunée, G., Banks, C. J., Enright, J., and Kao, R. R. Multi-species temporal network of livestock movements for disease spread. Applied Network Science 6, 1 (2021), 1-20.
[39] Schultz, P., and Spivak, D. I. Temporal type theory: A topos-theoretic approach to systems and behavior. arXiv preprint arXiv:1710.10258 (2017).
[40] Schultz, P., Spivak, D. I., and Vasilakopoulou, C. Dynamical systems and sheaves. Applied Categorical Structures 28, 1 (2020), 1-57.
[41] Viard, J., and Latapy, M. Identifying roles in an ip network with temporal and structural density. In 2014 IEEE Conference on Computer Communications Workshops (INFOCOM WKSHPS) (2014), IEEE, pp. 801-806.
[42] Viard, T., Latapy, M., and Magnien, C. Computing maximal cliques in link streams. Theoretical Computer Science 609 (2016), 245-252.


[^0]:    *(Corresponding authors.)
    University of Florida, Computer \& Information Science \& Engineering, Florida, USA.
    ${ }^{\dagger}$ University of Ottawa, Department of Mathematics, Canada.
    ${ }^{\ddagger}$ University of Ottawa, School of Electrical Engineering and Computer Science, Canada.

[^1]:    ${ }^{1}$ As an example of a notable exception, see Kim and Mémoli 25). For a more detailed discussion on how morphisms are considered in [25], see points one and two of Section 1.1

[^2]:    ${ }^{2}$ Notice that the approach in 25) does not allow merging of vertices or edges since the corestriction maps of such cosheaves must necessarily be injections. In contrast, our definition of cumulative time-varying graphs as cosheaves valued Grph (the category of graphs and their homomorphisms) allows for merging and splitting of vertices and edges over time.

[^3]:    ${ }^{a}$ Thus note that, for any interval $[a, b]$, a valid cover can be specified by simply choosing any number of distinct points $p_{1}, \ldots, p_{n}$ such that $a \leq p_{1} \leq \cdots \leq p_{n} \leq b$; this yields the cover $\left\{\left[a, p_{1}\right],\left[p_{1}, p_{2}\right], \ldots\left[p_{n-1}, p_{n}\right],\left[p_{n}, b\right]\right\}$.

[^4]:    ${ }^{3}$ By comparing examples of interval sheaves with sheaves on categories of strict intervals, the reader can verify that there is a sense in which these intuitions can be made mathematically concrete (in order to not derail the presentation of this paper, we omit these examples).

[^5]:    ${ }^{4}$ Note that there is a sense in which a functor defined on a subcategory of some category C has greater freedom compared to a functor defined on all of C. This is because there are fewer arrows (and hence fewer equations) which need to be accounted for in the subcategory.

[^6]:    ${ }^{5}$ Note that many categories of graphs are presheaf toposes and thus have all limits and colimits.

[^7]:    ${ }^{6}$ If one insists on avoiding this "duplication" of edge- or vertex-appearances, then this can be achieved by changing the codomain of these narratives to another category of graphs (for instance to a category of simple, reflexive graphs or to a slice category of some large ambient graph).

[^8]:    ${ }^{7}$ Recall that a contraction of a graph $G$ is a surjective graph homomorphism $q: G \rightarrow G^{\prime}$ such that every preimage of $q$ is connected in $G$ (equivalently $G^{\prime}$ is obtained from $G$ by a sequence of edge contractions). A minor of a graph $G$ is a subgraph $H$ of a contraction $G^{\prime}$ of $G$.



---


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



---


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

---

## Galois Connections as Hole Types (Seven Sketches §1.4.1)

> **HOLE TYPE**: Accessibility gates between worlds via adjoint monotone maps

Structured decompositions are fundamentally about **Galois connections** — the left adjoint decomposes (analysis), the right adjoint composes (synthesis).

### Definition 1.95 (Seven Sketches)

A **Galois connection** between preorders P and Q is a pair of monotone maps f: P → Q and g: Q → P such that:

```
f(p) ≤ q   ⟺   p ≤ g(q)
```

f is the **left adjoint**, g is the **right adjoint**.

### Example 1.97: Ceiling Division

```julia
# Left adjoint:  ⌈-/3⌉ : ℝ → ℤ
# Right adjoint: (3×-) : ℤ → ℝ
# The adjunction: ⌈x/3⌉ ≤ y  ⟺  x ≤ 3y
```

### Structured Decomposition as Galois Connection

```
┌─────────────────────────────────────────────────────────────────┐
│              STRUCTURED DECOMPOSITION GALOIS PAIR              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│    Object X                    Decomposition d: ∫G → C          │
│        │                              │                         │
│        │ decompose (left adjoint)     │ colimit (right adjoint) │
│        ▼                              ▼                         │
│    d: ∫G → C  ←──────────────────  colim(d) ≅ X                │
│                                                                 │
│  decompose(X) ≤ d   ⟺   X ≤ colim(d)                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### World Accessibility via Galois Gates

The **obstruction** to accessing a world is the failure of the Galois condition. When `f(p) ≤ q ⟺ p ≤ g(q)` holds, we have a **gate** between worlds:

| Previously Obstructed | Now Accessible Via | Galois Connection |
|----------------------|--------------------|--------------------|
| High-treewidth graphs | Tree decomposition | decompose ⊣ colim |
| Non-local solutions | Sheaf sections | restrict ⊣ extend |
| Exponential search | FPT algorithm | bags ⊣ adhesions |
| Schema migration | Functorial data migration | Σ ⊣ Δ |

### 69 Skills Unlocked by Galois Hole Type

These skills reference `structured-decompositions` via Galois accessibility:

#### Tier 1: Direct Adjoint Structure (15 skills)
1. `acsets` - Σ ⊣ Δ data migration
2. `kan-extensions` - Lan ⊣ Res ⊣ Ran
3. `sheaf-cohomology` - Γ ⊣ sheafification
4. `dialectica` - proof ⊣ counterexample
5. `open-games` - play ⊣ coplay
6. `topos-generate` - ∃ ⊣ pullback ⊣ ∀
7. `propagators` - merge ⊣ split
8. `covariant-fibrations` - pushforward ⊣ pullback
9. `elements-infinity-cats` - yoneda ⊣ coyoneda
10. `oapply-colimit` - oapply ⊣ ocompose
11. `operad-compose` - substitution ⊣ operadic nerve
12. `free-monad-gen` - free ⊣ forget
13. `infinity-operads` - dendroidal ⊣ simplicial
14. `synthetic-adjunctions` - counit ⊣ unit
15. `catsharp-galois` - ⟨-|-⟩ galois operators

#### Tier 2: Decomposition Applications (18 skills)
16. `tripartite-decompositions` - GF(3) bag splitting
17. `bumpus-narratives` - temporal sheaves
18. `compositional-acset-comparison` - structural diff
19. `algebraic-rewriting` - DPO ⊣ SPO
20. `topos-adhesive-rewriting` - adhesive decomposition
21. `graph-grafting` - graft ⊣ prune
22. `specter-acset` - navigate ⊣ transform
23. `lispsyntax-acset` - parse ⊣ unparse
24. `protocol-acset` - encode ⊣ decode
25. `nix-acset-worlding` - derive ⊣ instantiate
26. `osm-topology` - simplify ⊣ subdivide
27. `crn-topology` - reaction ⊣ species
28. `interaction-nets` - cut ⊣ glue
29. `interaction-rewriting` - rewrite ⊣ antirewrite
30. `datalog-fixpoint` - immediate consequence ⊣ stratify
31. `temporal-coalgebra` - unfold ⊣ fold
32. `persistent-homology` - birth ⊣ death
33. `moebius-inversion` - μ ⊣ ζ

#### Tier 3: Algorithmic FPT Access (12 skills)
34. `three-match` - 3-SAT ⊣ gadget reduction
35. `ramanujan-expander` - spectral ⊣ combinatorial
36. `ihara-zeta` - prime cycles ⊣ determinant
37. `assembly-index` - complexity ⊣ assembly path
38. `kolmogorov-compression` - compress ⊣ decompress
39. `compression-progress` - learn ⊣ predict
40. `gflownet` - flow ⊣ reward
41. `koopman-generator` - lift ⊣ project
42. `fokker-planck-analyzer` - forward ⊣ backward
43. `langevin-dynamics` - drift ⊣ diffusion
44. `lagrange-kkt` - primal ⊣ dual
45. `enzyme-autodiff` - forward ⊣ reverse mode

#### Tier 4: World Navigation (12 skills)
46. `world-hopping` - enter ⊣ exit
47. `glass-hopping` - play ⊣ synthesize
48. `world-extractable-value` - extract ⊣ inject
49. `multiversal-finance` - bet ⊣ settle
50. `ordered-locale` - open ⊣ closed
51. `ordered-locale-fanout` - cone ⊣ cocone
52. `glass-bead-game` - thesis ⊣ antithesis
53. `world-memory-worlding` - remember ⊣ forget
54. `unworld` - create ⊣ destroy
55. `unworlding-involution` - ι ⊣ ι⁻¹
56. `world-runtime` - spawn ⊣ terminate
57. `effective-topos` - realize ⊣ abstract

#### Tier 5: GF(3) Triadic Balance (12 skills)
58. `gay-mcp` - color ⊣ decolor
59. `gay-julia` - sample ⊣ condition
60. `gf3-tripartite` - balance ⊣ tilt
61. `triad-interleave` - interleave ⊣ deinterleave
62. `triadic-skill-orchestrator` - assign ⊣ verify
63. `bisimulation-game` - attack ⊣ defend
64. `spi-parallel-verify` - split ⊣ merge
65. `chromatic-walk` - step ⊣ backtrack
66. `gay-integration` - integrate ⊣ differentiate
67. `catsharp-sonification` - encode ⊣ decode
68. `finder-color-walk` - explore ⊣ exploit
69. `gf3-pr-verify` - conserve ⊣ violate

### Julia: Galois-Aware Decomposition

```julia
using StructuredDecompositions, Catlab

# The Galois connection in action
# Left adjoint: decompose object into bags + adhesions
d = TreeDecomposition(graph)

# Right adjoint: colimit reconstructs original
@assert colimit(d) ≅ graph

# Sheaf condition = Galois preservation
# For each adhesion, the restriction maps form a Galois pair
for a in adhesions(d)
    @assert restrict(bag_left(a)) ⊣ extend(adhesion(a))
end
```

### Hole Type Learning Path

```
     ┌──────────────────────────────────────────────┐
     │           GALOIS HOLE TYPE                   │
     │                                              │
     │  1. Master f(p)≤q ⟺ p≤g(q)                  │
     │  2. Recognize adjoint pairs in skills        │
     │  3. Navigate worlds via Galois gates         │
     │  4. Unlock 69+ skills via accessibility      │
     │                                              │
     └──────────────────────────────────────────────┘
              │
              ▼
    Previously obstructed skills now accessible
```

