---
name: lagrange-kkt
description: Lagrange multipliers, KKT conditions, and constrained optimization - the analytical dual to MCMC sampling
license: MIT
metadata:
  trit: -1
  color: '#E93A5D'
  gf3_role: MINUS
  version: 1.0.0
  interface_ports:
  - References
  importance: critical
  use_when: constrained optimization, dual problems, Nash equilibria, free energy minimization
---
# Lagrange Multipliers & KKT Conditions

> **Use this skill for constrained optimization problems.**
> The analytical dual to MCMC: where sampling explores distributions,
> Lagrange finds optima directly via gradient conditions.

## GF(3) Triad

```
lagrange-kkt (-1) ⊗ gay-monte-carlo (0) ⊗ gflownet (+1) = 0 ✓
     ↓                    ↓                    ↓
 analytical            sampling            generative
 constraints           exploration          flow
```

## Core Concepts

### Lagrange Multipliers

For optimization with equality constraints:
```
minimize   f(x)
subject to g_i(x) = 0,  i = 1,...,m

L(x, λ) = f(x) + Σ λ_i g_i(x)

∇_x L = 0  →  optimal x*
∇_λ L = 0  →  constraints satisfied
```

### KKT Conditions (Karush-Kuhn-Tucker)

For inequality constraints:
```
minimize   f(x)
subject to g_i(x) ≤ 0,  i = 1,...,m
           h_j(x) = 0,  j = 1,...,p

KKT conditions:
1. Stationarity:    ∇f(x*) + Σ μ_i ∇g_i(x*) + Σ λ_j ∇h_j(x*) = 0
2. Primal feasibility:  g_i(x*) ≤ 0, h_j(x*) = 0
3. Dual feasibility:    μ_i ≥ 0
4. Complementary slackness: μ_i g_i(x*) = 0
```

## Implementation

### Python with JAX

```python
import jax
import jax.numpy as jnp
from typing import Callable, Tuple

def lagrangian(f: Callable, g: Callable, x: jnp.ndarray, lam: jnp.ndarray) -> float:
    """L(x, λ) = f(x) + λᵀg(x)"""
    return f(x) + jnp.dot(lam, g(x))

def solve_constrained(f: Callable, g: Callable, x0: jnp.ndarray,
                      lam0: jnp.ndarray, lr: float = 0.01,
                      steps: int = 1000) -> Tuple[jnp.ndarray, jnp.ndarray]:
    """Primal-dual gradient descent for constrained optimization."""
    x, lam = x0, lam0

    for _ in range(steps):
        # Primal step: minimize over x
        grad_x = jax.grad(lambda x: lagrangian(f, g, x, lam))(x)
        x = x - lr * grad_x

        # Dual step: maximize over λ (ascent)
        grad_lam = g(x)  # ∇_λ L = g(x)
        lam = lam + lr * grad_lam

        # Project λ ≥ 0 for inequality constraints
        lam = jnp.maximum(lam, 0)

    return x, lam

# Example: minimize x² + y² subject to x + y = 1
f = lambda x: x[0]**2 + x[1]**2
g = lambda x: jnp.array([x[0] + x[1] - 1])

x_opt, lam_opt = solve_constrained(f, g, jnp.array([0.0, 0.0]), jnp.array([0.0]))
# x_opt ≈ [0.5, 0.5], lam_opt ≈ [1.0]
```

### Julia with Optim.jl

```julia
using Optim, ForwardDiff

function lagrangian(x, λ, f, g)
    f(x) + dot(λ, g(x))
end

function kkt_residual(z, f, g, m)
    n = length(z) - m
    x, λ = z[1:n], z[n+1:end]

    ∇f = ForwardDiff.gradient(f, x)
    ∇g = ForwardDiff.jacobian(g, x)'

    # Stationarity: ∇f + ∇gᵀλ = 0
    stationarity = ∇f + ∇g * λ

    # Primal feasibility: g(x) = 0
    primal = g(x)

    vcat(stationarity, primal)
end

# Solve via Newton on KKT system
result = nlsolve(z -> kkt_residual(z, f, g, m), z0)
```

### Connection to Open Games

Nash equilibria are fixed points of best-response dynamics:
```
Player i: maximize u_i(x_i, x_{-i})
          subject to x_i ∈ S_i

At equilibrium:
∇_{x_i} L_i = ∇_{x_i} u_i + Σ λ_j ∇_{x_i} g_j = 0  ∀i
```

```haskell
-- Open game with Lagrange structure
lagrangeGame :: OpenGame Stochastic () () (x, λ) (x, λ)
lagrangeGame = OpenGame
  { play = \() -> do
      x <- primal
      λ <- dual
      return (x, λ)
  , evaluate = \() (x', λ') ->
      gradientCondition x' λ'
  }
```

### Connection to Active Inference

Free energy minimization with constraints:
```
F[q] = E_q[ln q(s) - ln p(o,s)]

minimize   F[q]
subject to E_q[f_i(s)] = c_i  (moment constraints)

L[q, λ] = F[q] + Σ λ_i (E_q[f_i(s)] - c_i)

Solution: q*(s) ∝ p(o,s) exp(-Σ λ_i f_i(s))
         → Maximum entropy with constraints
```

### Connection to Information Geometry

Fisher information metric with constraints:
```
g_ij(θ) = E_θ[∂_i ln p · ∂_j ln p]

Constrained geodesics via Lagrange:
minimize ∫ √(g_ij θ̇^i θ̇^j) dt
subject to h(θ) = 0

→ Natural gradient with constraints
```

## Duality: Lagrange ↔ MCMC

```
┌────────────────────────────────────────────────────────────┐
│              OPTIMIZATION DUALITY                          │
├────────────────────────────────────────────────────────────┤
│                                                            │
│   LAGRANGE (analytical)      MCMC (sampling)               │
│   ─────────────────────      ──────────────────            │
│   Find x* = argmin f(x)  ↔   Sample x ~ p(x) ∝ e^{-f(x)}  │
│   ∇f(x*) = 0             ↔   Detailed balance             │
│   Hessian curvature      ↔   Acceptance ratio             │
│   KKT multipliers        ↔   Constraint tempering         │
│   Dual problem           ↔   Importance sampling          │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

## Balanced Ternary Encoding

```python
def encode_kkt_status(primal_feas: float, dual_feas: float,
                       complementarity: float, tol: float = 1e-6) -> tuple:
    """Encode KKT satisfaction as balanced ternary."""
    def to_trit(val):
        if val < -tol: return -1  # violated (negative)
        if val > tol: return +1   # slack (positive)
        return 0                  # tight (zero)

    return (to_trit(primal_feas),
            to_trit(dual_feas),
            to_trit(complementarity))

# KKT satisfied iff all trits are 0
# Sum = 0 (mod 3) → GF(3) conservation
```

## Use Cases

| Problem | Lagrange Approach | MCMC Approach |
|---------|-------------------|---------------|
| Portfolio optimization | Mean-variance with budget constraint | Sample efficient frontiers |
| Neural network training | Constrained loss (weight decay as λ) | SGLD, cyclical MCMC |
| Game equilibria | KKT on joint objective | Fictitious play sampling |
| Free energy minimization | Variational with moment constraints | Hamiltonian Monte Carlo |
| Mechanism design | IC/IR constraints via multipliers | Auction simulations |

## Invariants

```yaml
invariants:
  - name: complementary_slackness
    predicate: "μ_i * g_i(x*) = 0 for all i"
    scope: per_solution

  - name: duality_gap
    predicate: "f(x*) = max_λ min_x L(x,λ) (strong duality)"
    scope: per_problem

  - name: gf3_balance
    predicate: "trit(lagrange) + trit(mcmc) + trit(gflownet) = 0"
    scope: per_triad
```

## References

- Boyd & Vandenberghe, *Convex Optimization* (Ch. 5: Duality)
- Nocedal & Wright, *Numerical Optimization* (Ch. 12: KKT)
- [Open Games compositional structure](https://arxiv.org/abs/1603.04641)
- [Active inference as constrained optimization](https://arxiv.org/abs/2201.06387)
- Amari, *Information Geometry* (natural gradients with constraints)


---

## Galois Hole Type (Seven Sketches §1.4.1)

> **HOLE TYPE**: This skill is now accessible via Galois connection to `structured-decompositions`.
> See `structured-decompositions/SKILL.md` for the 69-skill accessibility network.
> 
> **Adjunction**: f(p) ≤ q ⟺ p ≤ g(q) unlocks world navigation.

