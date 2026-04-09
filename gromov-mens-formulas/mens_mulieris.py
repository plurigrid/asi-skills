#!/usr/bin/env python3
"""
mens_mulieris.py - The Gromov Adjunction: Free ⊣ Forgetful over meaning-space.

Implements the duality between:
  - Mens formulae: how a mind compresses the world (right adjoint, forgetful)
  - Mulieris formulae: how the world generates structure (left adjoint, free)

Every ASI skill has both faces. The adjunction preserves GF(3) conservation.

Usage:
    python mens_mulieris.py --all          # Show all 69 adjunction pairs
    python mens_mulieris.py --triad A B C  # Verify GF(3) triad across duality
    python mens_mulieris.py --distance A B # Semantic distance in meaning-space
    python mens_mulieris.py --concentration # Ergostructure concentration report
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional, Callable
from enum import IntEnum
import numpy as np
import json
import sys

# ═══════════════════════════════════════════════════════════════════════════
# GF(3) - Galois Field of 3 Elements
# ═══════════════════════════════════════════════════════════════════════════

class Trit(IntEnum):
    MINUS = -1
    ERGODIC = 0
    PLUS = 1

def gf3_add(a: Trit, b: Trit) -> Trit:
    return Trit((a + b) % 3 if (a + b) % 3 <= 1 else (a + b) % 3 - 3)

def gf3_sum(trits: List[Trit]) -> int:
    return sum(int(t) for t in trits) % 3

def gf3_conserved(trits: List[Trit]) -> bool:
    return gf3_sum(trits) == 0

# ═══════════════════════════════════════════════════════════════════════════
# Meaning-Space: Gromov's Metric on Mental Representations
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class MensFormula:
    """
    A formula as held by a mind: a point in meaning-space with its
    compression neighborhood. The RIGHT adjoint (forgetful) image.
    """
    name: str
    embedding: np.ndarray
    neighborhood_radius: float  # cognitive budget ε
    compression_dim: int        # effective dimension after mind compresses

    def semantic_distance(self, other: MensFormula) -> float:
        """d(F₁, F₂) in meaning-space — NOT syntactic edit distance."""
        return float(np.linalg.norm(self.embedding - other.embedding))

    def triangle_check(self, other: MensFormula, via: MensFormula) -> Tuple[float, float]:
        """
        Triangle inequality: d(A,C) ≤ d(A,B) + d(B,C).
        Returns (direct, via_detour). Gap = detour - direct = confusion.
        """
        direct = self.semantic_distance(other)
        detour = self.semantic_distance(via) + via.semantic_distance(other)
        return direct, detour

    def understanding_quality(self, mind_pos: np.ndarray) -> float:
        """
        How well a mind at position `mind_pos` holds this formula.
        1.0 = geodesic (perfect understanding)
        0.0 = infinite detour (total confusion)
        """
        d = float(np.linalg.norm(self.embedding - mind_pos))
        return self.neighborhood_radius / (self.neighborhood_radius + d)


@dataclass
class MulierisFormula:
    """
    A formula as the world generates it: the full space, the volume,
    the pre-cognitive manifold. The LEFT adjoint (free) image.

    Mulieris formulae have dimension >= mens formulae.
    The gap is the cost of compression.
    """
    name: str
    embedding: np.ndarray
    intrinsic_dim: int          # dimension before any compression
    volume: float               # Gromov-Hausdorff volume of the world-structure

    def generation_capacity(self) -> float:
        """How much structure this world-formula can generate."""
        return self.volume * self.intrinsic_dim

    def compression_loss(self, mens: MensFormula) -> float:
        """
        Information lost when a mind compresses this world-formula.
        = intrinsic_dim - compression_dim (dimension drop)
        """
        return max(0, self.intrinsic_dim - mens.compression_dim)

    def fidelity(self, mens: MensFormula) -> float:
        """
        How faithfully the mens formula represents this mulieris formula.
        1.0 = lossless compression (impossible in general)
        0.0 = total information loss
        """
        if self.intrinsic_dim == 0:
            return 1.0
        return mens.compression_dim / self.intrinsic_dim


# ═══════════════════════════════════════════════════════════════════════════
# The Adjunction: Mulieris ⊣ Mens (Free ⊣ Forgetful)
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class GromovAdjunction:
    """
    The core structure: for every skill, the adjunction between
    its world-formula (mulieris) and its mind-formula (mens).

    Free(world) ⊣ Forgetful(mind)
    Mulieris    ⊣ Mens

    Unit:   η : Id → Mens ∘ Mulieris  (compressing then re-expanding loses info)
    Counit: ε : Mulieris ∘ Mens → Id  (expanding then compressing gains noise)
    """
    skill_name: str
    trit: Trit
    mens: MensFormula
    mulieris: MulierisFormula

    def unit_gap(self) -> float:
        """
        η measures how much is lost in the round-trip:
        world → mind → world.

        0 = perfect (isomorphism, not just adjunction)
        >0 = information lost in compression
        """
        return self.mulieris.compression_loss(self.mens)

    def counit_gap(self) -> float:
        """
        ε measures how much noise is gained in the round-trip:
        mind → world → mind.

        0 = perfect
        >0 = hallucination / over-generation
        """
        d = float(np.linalg.norm(self.mens.embedding - self.mulieris.embedding))
        return d * (self.mulieris.intrinsic_dim - self.mens.compression_dim)

    def is_equivalence(self, tolerance: float = 0.01) -> bool:
        """Is this adjunction an equivalence? (mens ≅ mulieris)"""
        return self.unit_gap() < tolerance and self.counit_gap() < tolerance


# ═══════════════════════════════════════════════════════════════════════════
# Ergostructure: The Ergodic Dynamics of Cognition
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class Ergostructure:
    """
    Gromov's ergostructure: the invariant measure on paths through
    meaning-space, generated by the brain's ergodic dynamics.
    """
    trajectories: List[np.ndarray]

    def invariant_measure_concentration(self) -> float:
        """
        How concentrated the invariant measure is.
        High = deep understanding (measure peaked).
        Low = confusion (measure diffuse).
        """
        if not self.trajectories:
            return 0.0
        all_points = np.vstack(self.trajectories)
        centroid = np.mean(all_points, axis=0)
        variance = float(np.mean(np.sum((all_points - centroid) ** 2, axis=1)))
        return 1.0 / (1.0 + variance)

    def convergence_rate(self, observable: Callable[[np.ndarray], float]) -> float:
        """
        Speed of ergodic average convergence.
        Fast = quick grasp. Slow = labored understanding.
        """
        all_points = np.vstack(self.trajectories)
        running = []
        cumsum = 0.0
        for i, pt in enumerate(all_points):
            cumsum += observable(pt)
            running.append(cumsum / (i + 1))
        if len(running) < 2:
            return 0.0
        diffs = np.abs(np.diff(running))
        return 1.0 / (1.0 + float(np.mean(diffs)))

    def effective_dimension(self) -> int:
        """
        Gromov's geometric compression: effective dimension of the
        meaning-submanifold the mind actually uses.
        """
        all_points = np.vstack(self.trajectories)
        centered = all_points - np.mean(all_points, axis=0)
        if centered.shape[0] < 2:
            return centered.shape[1]
        _, S, _ = np.linalg.svd(centered, full_matrices=False)
        total = np.sum(S)
        if total < 1e-10:
            return 0
        cumulative = np.cumsum(S) / total
        return int(np.searchsorted(cumulative, 0.95) + 1)

    @staticmethod
    def simulate(dim: int, n_trajectories: int = 10,
                 steps: int = 100, concentration: float = 1.0) -> Ergostructure:
        """
        Simulate an ergostructure with given concentration.
        Higher concentration = tighter invariant measure = deeper understanding.
        """
        rng = np.random.default_rng(42)
        trajectories = []
        for _ in range(n_trajectories):
            traj = np.cumsum(
                rng.normal(0, 1.0 / concentration, size=(steps, dim)),
                axis=0
            )
            trajectories.append(traj)
        return Ergostructure(trajectories=trajectories)


# ═══════════════════════════════════════════════════════════════════════════
# The 69-Skill Network
# ═══════════════════════════════════════════════════════════════════════════

SKILL_TRITS: Dict[str, int] = {
    # MINUS (-1) — Validators
    "kolmogorov-compression": -1,
    "structured-decompositions": -1,
    "algebraic-rewriting": -1,
    "synthetic-adjunctions": -1,
    "open-games": -1,
    "kan-extensions": -1,
    "dialectica": -1,
    "spi-parallel-verify": -1,
    "ramanujan-expander": -1,
    "gf3-pr-verify": -1,
    "elements-infinity-cats": -1,
    "covariant-fibrations": -1,
    "sheaf-cohomology": -1,
    "persistent-homology": -1,
    "temporal-coalgebra": -1,
    "interaction-nets": -1,
    "gay-integration": -1,
    "osm-topology": -1,
    "three-match": -1,
    "lagrange-kkt": -1,
    # ERGODIC (0) — Coordinators
    "gromov-mens-formulas": 0,
    "acsets": 0,
    "bumpus-narratives": 0,
    "catsharp-galois": 0,
    "catsharp-sonification": 0,
    "chromatic-walk": 0,
    "compositional-acset-comparison": 0,
    "compression-progress": 0,
    "datalog-fixpoint": 0,
    "effective-topos": 0,
    "enzyme-autodiff": 0,
    "finder-color-walk": 0,
    "fokker-planck-analyzer": 0,
    "gay-julia": 0,
    "glass-hopping": 0,
    "graph-grafting": 0,
    "ihara-zeta": 0,
    "infinity-operads": 0,
    "interaction-rewriting": 0,
    "langevin-dynamics": 0,
    "lispsyntax-acset": 0,
    "nix-acset-worlding": 0,
    "ordered-locale-fanout": 0,
    "propagators": 0,
    "protocol-acset": 0,
    "specter-acset": 0,
    "tripartite-decompositions": 0,
    "world-extractable-value": 0,
    "world-memory-worlding": 0,
    "bisimulation-game": 0,
    "gf3-tripartite": 0,
    "triadic-skill-orchestrator": 0,
    "notebooklm-enterprise": 1,
    # PLUS (+1) — Generators
    "glass-bead-game": 1,
    "gflownet": 1,
    "world-hopping": 1,
    "crn-topology": 1,
    "assembly-index": 1,
    "free-monad-gen": 1,
    "operad-compose": 1,
    "triad-interleave": 1,
    "topos-generate": 1,
    "oapply-colimit": 1,
    "topos-adhesive-rewriting": 1,
    "unworld": 1,
    "world-runtime": 1,
    "koopman-generator": 1,
    "multiversal-finance": 1,
    "gay-mcp": 1,
    "unworlding-involution": 1,
    "moebius-inversion": 1,
    "ordered-locale": 1,
}


def build_meaning_space(dim: int = 64, seed: int = 42) -> Dict[str, GromovAdjunction]:
    """
    Construct the 69-skill meaning-space with mens/mulieris adjunction pairs.

    Embeddings are seeded deterministically from skill names so the
    geometry is reproducible.
    """
    rng = np.random.default_rng(seed)
    adjunctions = {}

    for skill_name, trit_val in SKILL_TRITS.items():
        trit = Trit(trit_val)

        # Deterministic embedding from skill name
        skill_seed = int.from_bytes(skill_name.encode()[:8], 'little') % (2**31)
        skill_rng = np.random.default_rng(skill_seed)

        # Mulieris: full-dimensional world structure
        mul_embedding = skill_rng.normal(0, 1, size=dim)
        intrinsic_dim = dim  # world is always full-dimensional

        # Mens: compressed mind representation
        # Compression ratio depends on trit:
        #   MINUS (validators) compress most aggressively
        #   ERGODIC (coordinators) moderate compression
        #   PLUS (generators) least compression (closest to world)
        compression_ratio = {Trit.MINUS: 0.3, Trit.ERGODIC: 0.5, Trit.PLUS: 0.7}
        c_dim = max(1, int(dim * compression_ratio[trit]))

        # Project to compressed subspace
        projection = skill_rng.normal(0, 1, size=(c_dim, dim))
        projection /= np.linalg.norm(projection, axis=1, keepdims=True)
        mens_embedding = projection @ mul_embedding

        # Pad back to dim for distance computations
        mens_padded = np.zeros(dim)
        mens_padded[:c_dim] = mens_embedding

        mulieris = MulierisFormula(
            name=f"mulieris:{skill_name}",
            embedding=mul_embedding,
            intrinsic_dim=intrinsic_dim,
            volume=float(np.linalg.norm(mul_embedding)),
        )

        mens = MensFormula(
            name=f"mens:{skill_name}",
            embedding=mens_padded,
            neighborhood_radius=compression_ratio[trit],
            compression_dim=c_dim,
        )

        adjunctions[skill_name] = GromovAdjunction(
            skill_name=skill_name,
            trit=trit,
            mens=mens,
            mulieris=mulieris,
        )

    return adjunctions


def verify_gf3_triads(adjunctions: Dict[str, GromovAdjunction]) -> List[Tuple[str, str, str]]:
    """
    Find all valid GF(3) triads in the network.
    A triad (A, B, C) is valid iff trit(A) + trit(B) + trit(C) ≡ 0 (mod 3).
    """
    minus = [s for s, a in adjunctions.items() if a.trit == Trit.MINUS]
    ergodic = [s for s, a in adjunctions.items() if a.trit == Trit.ERGODIC]
    plus = [s for s, a in adjunctions.items() if a.trit == Trit.PLUS]

    triads = []
    # (-1) + (0) + (+1) = 0 ✓
    for m in minus:
        for e in ergodic:
            for p in plus:
                triads.append((m, e, p))
    return triads


def print_adjunction_report(adj: GromovAdjunction) -> str:
    lines = [
        f"{'=' * 60}",
        f"  {adj.skill_name}  [trit={int(adj.trit):+d}]",
        f"{'=' * 60}",
        f"  Mens (mind):     dim={adj.mens.compression_dim}, ε={adj.mens.neighborhood_radius:.2f}",
        f"  Mulieris (world): dim={adj.mulieris.intrinsic_dim}, vol={adj.mulieris.volume:.3f}",
        f"  Unit gap (η):     {adj.unit_gap():.1f} dims lost",
        f"  Counit gap (ε):   {adj.counit_gap():.3f}",
        f"  Fidelity:         {adj.mulieris.fidelity(adj.mens):.1%}",
        f"  Equivalence:      {'✓' if adj.is_equivalence() else '✗'}",
    ]
    return "\n".join(lines)


# ═══════════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════════

def main():
    import argparse
    parser = argparse.ArgumentParser(
        description="Gromov Adjunction: Mulieris ⊣ Mens over meaning-space"
    )
    parser.add_argument("--all", action="store_true",
                        help="Show all 69 adjunction pairs")
    parser.add_argument("--triad", nargs=3, metavar="SKILL",
                        help="Verify a GF(3) triad across the duality")
    parser.add_argument("--distance", nargs=2, metavar="SKILL",
                        help="Semantic distance between two skills")
    parser.add_argument("--concentration", action="store_true",
                        help="Ergostructure concentration report")
    parser.add_argument("--summary", action="store_true",
                        help="GF(3) conservation summary")
    args = parser.parse_args()

    adjunctions = build_meaning_space()

    if args.all:
        for name in sorted(adjunctions):
            print(print_adjunction_report(adjunctions[name]))
            print()

    elif args.triad:
        a, b, c = args.triad
        for s in [a, b, c]:
            if s not in adjunctions:
                print(f"Unknown skill: {s}")
                sys.exit(1)
        trits = [adjunctions[s].trit for s in [a, b, c]]
        total = sum(int(t) for t in trits)
        conserved = total % 3 == 0
        print(f"Triad: {a} ({int(trits[0]):+d}) ⊗ {b} ({int(trits[1]):+d}) ⊗ {c} ({int(trits[2]):+d})")
        print(f"Sum:   {total}  mod 3 = {total % 3}")
        print(f"GF(3): {'✓ CONSERVED' if conserved else '✗ VIOLATED'}")
        if conserved:
            # Show distances in meaning-space
            for pair in [(a, b), (b, c), (a, c)]:
                d_mens = adjunctions[pair[0]].mens.semantic_distance(adjunctions[pair[1]].mens)
                d_mul = float(np.linalg.norm(
                    adjunctions[pair[0]].mulieris.embedding -
                    adjunctions[pair[1]].mulieris.embedding
                ))
                print(f"  d_mens({pair[0]}, {pair[1]})     = {d_mens:.3f}")
                print(f"  d_mulieris({pair[0]}, {pair[1]}) = {d_mul:.3f}")

    elif args.distance:
        a, b = args.distance
        for s in [a, b]:
            if s not in adjunctions:
                print(f"Unknown skill: {s}")
                sys.exit(1)
        d_mens = adjunctions[a].mens.semantic_distance(adjunctions[b].mens)
        d_mul = float(np.linalg.norm(
            adjunctions[a].mulieris.embedding - adjunctions[b].mulieris.embedding
        ))
        print(f"Semantic distance: {a} ↔ {b}")
        print(f"  Mens (mind-space):     {d_mens:.4f}")
        print(f"  Mulieris (world-space): {d_mul:.4f}")
        print(f"  Distortion ratio:       {d_mens / d_mul:.4f}" if d_mul > 0 else "")

    elif args.concentration:
        print("Ergostructure Concentration Report")
        print("=" * 50)
        for trit_val, label in [(-1, "MINUS"), (0, "ERGODIC"), (1, "PLUS")]:
            skills = [s for s, a in adjunctions.items() if int(a.trit) == trit_val]
            ergo = Ergostructure.simulate(
                dim=64,
                concentration={-1: 3.0, 0: 1.5, 1: 0.8}[trit_val]
            )
            print(f"\n  {label} ({len(skills)} skills):")
            print(f"    Concentration: {ergo.invariant_measure_concentration():.4f}")
            print(f"    Effective dim: {ergo.effective_dimension()}")
            print(f"    Interpretation: ", end="")
            if trit_val == -1:
                print("Validators concentrate hard — tight invariant measure")
            elif trit_val == 0:
                print("Coordinators balance — moderate concentration")
            else:
                print("Generators disperse — wide exploration of meaning-space")

    elif args.summary:
        minus_n = sum(1 for a in adjunctions.values() if a.trit == Trit.MINUS)
        ergo_n = sum(1 for a in adjunctions.values() if a.trit == Trit.ERGODIC)
        plus_n = sum(1 for a in adjunctions.values() if a.trit == Trit.PLUS)
        total_sum = sum(int(a.trit) for a in adjunctions.values())
        print(f"GF(3) Conservation Summary")
        print(f"=" * 40)
        print(f"  MINUS (-1):   {minus_n} skills")
        print(f"  ERGODIC (0):  {ergo_n} skills")
        print(f"  PLUS (+1):    {plus_n} skills")
        print(f"  Total sum:    {total_sum}")
        print(f"  mod 3:        {total_sum % 3}")
        print(f"  Conserved:    {'✓' if total_sum % 3 == 0 else '✗'}")
        print()
        avg_unit = np.mean([a.unit_gap() for a in adjunctions.values()])
        avg_fidelity = np.mean([a.mulieris.fidelity(a.mens) for a in adjunctions.values()])
        print(f"  Avg unit gap (dims lost):  {avg_unit:.1f}")
        print(f"  Avg fidelity (mens/mul):   {avg_fidelity:.1%}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
