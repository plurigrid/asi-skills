#!/bin/bash
# Add Galois hole type reference to 69 skills

SKILLS_DIR="/Users/barton/.claude/skills"
GALOIS_REF='

---

## Galois Hole Type (Seven Sketches §1.4.1)

> **HOLE TYPE**: This skill is now accessible via Galois connection to `structured-decompositions`.
> See `structured-decompositions/SKILL.md` for the 69-skill accessibility network.
> 
> **Adjunction**: f(p) ≤ q ⟺ p ≤ g(q) unlocks world navigation.
'

# Tier 1: Direct Adjoint Structure
TIER1=(
  "acsets" # already updated
  "kan-extensions"
  "sheaf-cohomology"
  "dialectica"
  "open-games"
  "topos-generate"
  "propagators"
  "covariant-fibrations"
  "elements-infinity-cats"
  "oapply-colimit"
  "operad-compose"
  "free-monad-gen"
  "infinity-operads"
  "synthetic-adjunctions"
  "catsharp-galois"
)

# Tier 2: Decomposition Applications
TIER2=(
  "tripartite-decompositions"
  "bumpus-narratives"
  "compositional-acset-comparison"
  "algebraic-rewriting"
  "topos-adhesive-rewriting"
  "graph-grafting"
  "specter-acset"
  "lispsyntax-acset"
  "protocol-acset"
  "nix-acset-worlding"
  "osm-topology"
  "crn-topology"
  "interaction-nets"
  "interaction-rewriting"
  "datalog-fixpoint"
  "temporal-coalgebra"
  "persistent-homology"
  "moebius-inversion"
)

# Tier 3: Algorithmic FPT Access
TIER3=(
  "three-match"
  "ramanujan-expander"
  "ihara-zeta"
  "assembly-index"
  "kolmogorov-compression"
  "compression-progress"
  "gflownet"
  "koopman-generator"
  "fokker-planck-analyzer"
  "langevin-dynamics"
  "lagrange-kkt"
  "enzyme-autodiff"
)

# Tier 4: World Navigation
TIER4=(
  "world-hopping"
  "glass-hopping"
  "world-extractable-value"
  "multiversal-finance"
  "ordered-locale"
  "ordered-locale-fanout"
  "glass-bead-game"
  "world-memory-worlding"
  "unworld"
  "unworlding-involution"
  "world-runtime"
  "effective-topos"
)

# Tier 5: GF(3) Triadic Balance
TIER5=(
  "gay-mcp"
  "gay-julia"
  "gf3-tripartite"
  "triad-interleave"
  "triadic-skill-orchestrator"
  "bisimulation-game"
  "spi-parallel-verify"
  "chromatic-walk"
  "gay-integration"
  "catsharp-sonification"
  "finder-color-walk"
  "gf3-pr-verify"
)

ALL_SKILLS=("${TIER1[@]}" "${TIER2[@]}" "${TIER3[@]}" "${TIER4[@]}" "${TIER5[@]}")

count=0
for skill in "${ALL_SKILLS[@]}"; do
  SKILL_FILE="$SKILLS_DIR/$skill/SKILL.md"
  if [[ -f "$SKILL_FILE" ]]; then
    # Check if already has Galois reference
    if ! grep -q "Galois Hole Type" "$SKILL_FILE"; then
      echo "$GALOIS_REF" >> "$SKILL_FILE"
      echo "✓ Updated: $skill"
      ((count++))
    else
      echo "⊘ Already has Galois ref: $skill"
    fi
  else
    echo "✗ Not found: $skill"
  fi
done

echo ""
echo "Updated $count skills with Galois hole type reference"
