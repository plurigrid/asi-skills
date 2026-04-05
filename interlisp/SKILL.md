---
name: interlisp
description: Interlisp-D/Medley environment as ACSet-backed interactive programming
  with DWIM, structure editing, and the Programmer's Assistant
license: MIT
metadata:
  source: Xerox PARC + Medley Interlisp revival
  trit: 0
  gf3_conserved: true
  dynamic_sufficiency: verified
  version: 1.0.0
---

# interlisp

> *"The system should do what I mean, not what I say."* -- Warren Teitelman

**Version**: 1.0.0
**Trit**: 0 (Ergodic - coordinates between programmer intent and execution)
**Dynamic Sufficiency**: VERIFIED

## Overview

Interlisp was the premier interactive programming environment, developed at BBN
and Xerox PARC (1966-1992), now revived as [Medley Interlisp](https://interlisp.org).
This skill bridges Interlisp's pioneering concepts with ACSets and category-theoretic
composition, modeling the *environment itself* as a structured mathematical object.

Key Interlisp innovations captured here:
1. **DWIM** (Do What I Mean) - intent-aware error correction as adjunction
2. **SEdit** - structure editor operating on S-expression trees
3. **Programmer's Assistant** - undo/redo history as a category of edits
4. **Masterscope** - cross-reference analysis as functorial dependency graph
5. **CLISP** - conversational syntax extensions via algebraic rewriting

## Core Concept: Environment as ACSet

The Interlisp environment is not just a REPL -- it is a *persistent, interconnected
knowledge structure*. We model this as an ACSet schema:

```julia
@present SchInterlisp(FreeSchema) begin
    # Objects
    (Fn, Var, File, History, Breakpoint)::Ob

    # Function graph
    calls::Hom(Fn, Fn)          # Masterscope call graph
    defines::Hom(Fn, File)      # File residence
    binds::Hom(Var, Fn)         # Variable scope

    # Edit history (Programmer's Assistant)
    prev::Hom(History, History)  # Undo chain
    target::Hom(History, Fn)     # What was edited
    
    # Debugging
    at_fn::Hom(Breakpoint, Fn)   # BREAK location

    # Attributes
    (Name, SexpStr, Timestamp)::AttrType
    fn_name::Attr(Fn, Name)
    fn_body::Attr(Fn, SexpStr)
    var_name::Attr(Var, Name)
    file_name::Attr(File, Name)
    edit_time::Attr(History, Timestamp)
end
```

## DWIM as Galois Connection

Teitelman's DWIM (Do What I Mean) is formalized as a Galois connection between
the lattice of *intended programs* and *typed programs*:

```
                 dwim
    Intended ─────────→ WellTyped
       ↑                    │
       │     f(p) ≤ q       │
       │       ⟺           │
       │     p ≤ g(q)       │
       │                    ↓
    WellTyped ←─────── Intended
                 undo
```

- **dwim(p)**: Given a malformed expression p, find the closest well-typed program
- **undo(q)**: The Programmer's Assistant can always reverse a DWIM correction
- **Adjunction**: `dwim(p) ≤ q ⟺ p ≤ undo(q)` -- correction is left adjoint to reversal

### DWIM Strategies

```julia
struct DWIMStrategy
    edit_distance::Int       # Levenshtein threshold
    scope_search::Bool       # Search enclosing scopes
    spelling_correct::Bool   # Phonetic/spelling correction
    paren_balance::Bool      # Auto-balance parentheses
end

function dwim(expr, env::InterlispEnv, strategy::DWIMStrategy)
    candidates = Candidate[]
    
    # 1. Spelling correction (original Interlisp approach)
    if strategy.spelling_correct
        for sym in all_symbols(env)
            d = edit_distance(string(expr), string(sym))
            d <= strategy.edit_distance && push!(candidates, Candidate(sym, d))
        end
    end
    
    # 2. Parenthesis balancing
    if strategy.paren_balance
        balanced = balance_parens(expr)
        balanced !== nothing && push!(candidates, Candidate(balanced, 0))
    end
    
    # 3. Scope search (DWIM across packages)
    if strategy.scope_search
        for scope in enclosing_scopes(env)
            found = lookup(scope, expr)
            found !== nothing && push!(candidates, Candidate(found, 1))
        end
    end
    
    # Return best candidate or ask user
    isempty(candidates) ? ask_user(expr) : best(candidates)
end
```

## Structure Editor (SEdit) via Specter Navigation

SEdit operates on the *tree structure* of S-expressions, not on text. We implement
it using Specter-style navigators from `lispsyntax-acset`:

```julia
# SEdit commands as Specter paths
const SEDIT_COMMANDS = Dict(
    :next     => [SEXP_TAIL, FIRST],        # Move to next sibling
    :prev     => [SEXP_TAIL, LAST],          # Move to previous sibling  
    :down     => [SEXP_CHILDREN, FIRST],     # Enter subexpression
    :up       => [],                          # Exit to parent (pop path)
    :delete   => [SEXP_CHILDREN],            # Remove current node
    :replace  => [ATOM_VALUE],               # Replace current atom
    :wrap     => [SEXP_HEAD],                # Wrap in new list
)

function sedit(sexp, command::Symbol, arg=nothing)
    path = SEDIT_COMMANDS[command]
    if command == :replace && arg !== nothing
        transform(path, _ -> arg, sexp)
    else
        select(path, sexp)
    end
end
```

## Programmer's Assistant: Edit History Category

The Programmer's Assistant maintains a complete undo history, modeled as a
category where:
- **Objects** are environment states
- **Morphisms** are edit operations  
- **Composition** chains edits
- **Inverses** exist for every edit (groupoid structure)

```julia
struct EditOp
    kind::Symbol           # :define, :edit, :delete, :rename, :advise
    target::Symbol         # Function/variable name
    before::Any            # Previous state (for undo)
    after::Any             # New state
    timestamp::Float64
end

struct ProgrammersAssistant
    history::Vector{EditOp}
    cursor::Int            # Current position in undo chain
    
    function undo!(pa::ProgrammersAssistant)
        op = pa.history[pa.cursor]
        apply_state!(op.target, op.before)
        pa.cursor -= 1
        op
    end
    
    function redo!(pa::ProgrammersAssistant)
        pa.cursor += 1
        op = pa.history[pa.cursor]
        apply_state!(op.target, op.after)
        op
    end
end
```

## Masterscope as Functorial Analysis

Masterscope performs cross-reference analysis. Categorically, it is a functor
from the category of **Programs** to the category of **DependencyGraphs**:

```
Masterscope : Prog → DepGraph

Where:
  Prog     = category of Interlisp functions and calls
  DepGraph = category of directed graphs with labeled edges
```

```julia
function masterscope(env::InterlispEnv)
    dep = @acset Graph begin
        V = length(env.functions)
        E = 0  # Will be populated
    end
    
    for (i, fn) in enumerate(env.functions)
        called = extract_calls(fn.body)
        for callee in called
            j = findfirst(f -> f.name == callee, env.functions)
            j !== nothing && add_edge!(dep, i, j)
        end
    end
    
    dep
end

# Queries via ACSet navigation
who_calls(env, fn)  = select([acset_where(:E, :tgt, ==(fn_id(env, fn))), 
                               acset_field(:E, :src)], masterscope(env))
calls_who(env, fn)  = select([acset_where(:E, :src, ==(fn_id(env, fn))),
                               acset_field(:E, :tgt)], masterscope(env))
```

## CLISP: Conversational Syntax as Algebraic Rewriting

CLISP extends standard Lisp syntax with infix notation and iteration constructs,
implemented as term rewriting rules:

```julia
# CLISP rewrite rules (iterative statements)
const CLISP_RULES = [
    # Infix arithmetic
    :(a + b)   => :(PLUS a b),
    :(a - b)   => :(DIFFERENCE a b),
    :(a * b)   => :(TIMES a b),
    :(a / b)   => :(QUOTIENT a b),
    
    # Iteration (Interlisp's FOR loop)
    :(for x in lst do body) => :(MAPC (FUNCTION (LAMBDA (x) body)) lst),
    
    # Conditional assignment
    :(x _ test)  => :(SETQ x (COND (test x) (T NIL))),
]
```

## Advising: Aspect-Oriented Interlisp

Interlisp's ADVISE mechanism wraps functions with before/after/around advice --
a precursor to aspect-oriented programming:

```julia
struct Advice
    kind::Symbol        # :before, :after, :around
    target::Symbol      # Function to advise
    body::Expr          # Advice code
end

function advise!(env::InterlispEnv, target::Symbol, kind::Symbol, body)
    original = env.functions[target]
    advised = wrap_with_advice(original, kind, body)
    
    # Record in Programmer's Assistant for undo
    push!(env.assistant.history, EditOp(
        :advise, target, original, advised, time()
    ))
    
    env.functions[target] = advised
end

# Example: trace all calls to FACTORIAL
advise!(env, :FACTORIAL, :before, 
    :(PRINT (LIST "entering FACTORIAL with" N)))
```

## Medley Interlisp Revival

The [Medley Interlisp Project](https://interlisp.org) has revived the full
Xerox Lisp environment as open source. Key components:

| Component | Description | ACSet Mapping |
|-----------|-------------|---------------|
| Maiko VM | C-based bytecode interpreter | Execution substrate |
| LOOPS | Lisp Object-Oriented Programming | Schema morphisms |
| Rooms | Window management system | Spatial ACSet |
| TEdit | Rich text editor | Document ACSet |
| Notecards | Hypertext system | Knowledge graph |

### Running Medley

```bash
# Clone and run
git clone https://github.com/Interlisp/medley.git
cd medley
./run-medley
```

## GF(3) Triads

| Triad | Role |
|-------|------|
| lispsyntax-acset (-1) ⊗ interlisp (0) ⊗ free-monad-gen (+1) | Interactive DSL |
| interaction-nets (-1) ⊗ interlisp (0) ⊗ specter-acset (+1) | Evaluation Bridge |
| structured-decompositions (-1) ⊗ interlisp (0) ⊗ algebraic-rewriting (+1) | DWIM Correction |

## References

- Teitelman, W. "Interlisp Reference Manual" (1974), Xerox PARC
- Teitelman, W. "Do What I Mean: The Programmer's Assistant" (1972)
- Teitelman, W. & Masinter, L. "The Interlisp Programming Environment" (1981), IEEE Computer
- Xerox PARC. "Interlisp-D Reference Manual" (1983)
- [Medley Interlisp Project](https://interlisp.org) - Modern open-source revival
- [Interlisp/medley](https://github.com/Interlisp/medley) - GitHub repository
- Bobrow, D. & Stefik, M. "The LOOPS Manual" (1983) - Object system

## Scientific Skill Interleaving

This skill connects to the K-Dense-AI/claude-scientific-skills ecosystem:

### Programming Environments
- **lispsyntax-acset** [0] via S-expression parsing infrastructure
- **specter-acset** [0] via bidirectional structure navigation
- **interaction-nets** [-1] via evaluation model (optimal reduction)
- **free-monad-gen** [+1] via DSL generation from environment signatures

## Cat# Integration

This skill maps to **Cat# = Comod(P)** as a bicomodule in the equipment structure:

```
Trit: 0 (ERGODIC)
Home: Prof
Poly Op: ⊗
Kan Role: Adj
Color: #26D826
```

### GF(3) Naturality

The skill participates in triads satisfying:
```
(-1) + (0) + (+1) ≡ 0 (mod 3)
```

This ensures compositional coherence in the Cat# equipment structure.

---

## Galois Hole Type (Seven Sketches S1.4.1)

> **HOLE TYPE**: This skill is accessible via Galois connection to `structured-decompositions`.
> DWIM itself is a Galois connection: correction ⊣ undo.
>
> **Adjunction**: f(p) <= q <=> p <= g(q) unlocks world navigation.
