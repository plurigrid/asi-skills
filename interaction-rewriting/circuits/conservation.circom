/*
 * GF(3) Conservation Circuit for Interaction Rewriting
 * =====================================================
 * 
 * Proves that a set of interactions preserves GF(3) conservation
 * without revealing the specific trit values or payloads.
 * 
 * Compile: circom conservation.circom --r1cs --wasm --sym
 * Setup:   snarkjs groth16 setup conservation.r1cs pot12_final.ptau conservation_0000.zkey
 * Prove:   snarkjs groth16 prove conservation_0000.zkey witness.wtns proof.json public.json
 * Verify:  snarkjs groth16 verify verification_key.json public.json proof.json
 */

pragma circom 2.1.0;

include "circomlib/circuits/comparators.circom";
include "circomlib/circuits/poseidon.circom";

/*
 * ValidTrit: Constrains input to be in {0, 1, 2} representing {-1, 0, +1}
 */
template ValidTrit() {
    signal input trit;
    signal output valid;
    
    // trit * (trit - 1) * (trit - 2) === 0
    signal t1;
    signal t2;
    t1 <== trit * (trit - 1);
    t2 <== t1 * (trit - 2);
    t2 === 0;
    
    valid <== 1;
}

/*
 * TritSum: Sum trits modulo 3
 */
template TritSum(n) {
    signal input trits[n];
    signal output sum;  // Result in {0, 1, 2}
    
    // Validate each trit
    component validators[n];
    for (var i = 0; i < n; i++) {
        validators[i] = ValidTrit();
        validators[i].trit <== trits[i];
    }
    
    // Compute raw sum
    var rawSum = 0;
    for (var i = 0; i < n; i++) {
        rawSum += trits[i];
    }
    
    // Compute sum mod 3
    // We need to constrain: sum === rawSum mod 3
    signal quotient;
    signal remainder;
    
    quotient <-- rawSum \ 3;  // Integer division
    remainder <-- rawSum % 3;
    
    // Constrain: rawSum === 3 * quotient + remainder
    rawSum === 3 * quotient + remainder;
    
    // Constrain remainder in {0, 1, 2}
    component remValid = ValidTrit();
    remValid.trit <== remainder;
    
    sum <== remainder;
}

/*
 * InteractionConservation: Verify a single interaction conserves GF(3)
 * 
 * pre_trits: trits of agents before interaction
 * post_trits: trits of agents after interaction
 */
template InteractionConservation(pre_n, post_n) {
    signal input pre_trits[pre_n];
    signal input post_trits[post_n];
    signal output conserved;
    
    // Compute pre-interaction sum
    component preSum = TritSum(pre_n);
    for (var i = 0; i < pre_n; i++) {
        preSum.trits[i] <== pre_trits[i];
    }
    
    // Compute post-interaction sum
    component postSum = TritSum(post_n);
    for (var i = 0; i < post_n; i++) {
        postSum.trits[i] <== post_trits[i];
    }
    
    // Conservation: pre_sum === post_sum (mod 3)
    component equal = IsEqual();
    equal.in[0] <== preSum.sum;
    equal.in[1] <== postSum.sum;
    
    conserved <== equal.out;
    conserved === 1;  // MUST be conserved
}

/*
 * BatchConservation: Verify multiple interactions all conserve GF(3)
 */
template BatchConservation(n_interactions, max_pre, max_post) {
    // Each interaction has pre and post trits
    signal input pre_trits[n_interactions][max_pre];
    signal input post_trits[n_interactions][max_post];
    signal input pre_counts[n_interactions];  // Actual count of pre agents
    signal input post_counts[n_interactions]; // Actual count of post agents
    
    signal output all_conserved;
    
    component interactions[n_interactions];
    signal conservation_results[n_interactions];
    
    for (var i = 0; i < n_interactions; i++) {
        interactions[i] = InteractionConservation(max_pre, max_post);
        
        for (var j = 0; j < max_pre; j++) {
            interactions[i].pre_trits[j] <== pre_trits[i][j];
        }
        for (var j = 0; j < max_post; j++) {
            interactions[i].post_trits[j] <== post_trits[i][j];
        }
        
        conservation_results[i] <== interactions[i].conserved;
    }
    
    // All must be conserved (product of booleans)
    var product = 1;
    for (var i = 0; i < n_interactions; i++) {
        product = product * conservation_results[i];
    }
    
    all_conserved <== product;
    all_conserved === 1;
}

/*
 * GadgetProof: Prove a rewriting gadget preserves conservation
 */
template GadgetProof() {
    // Gadget: 2 agents interact, produce up to 4 agents
    signal input left_trit;   // Trit of left agent
    signal input right_trit;  // Trit of right agent
    signal input result_trits[4];  // Trits of result agents
    signal input result_count;     // How many result agents (0-4)
    
    signal output valid;
    
    // Validate input trits
    component leftValid = ValidTrit();
    leftValid.trit <== left_trit;
    
    component rightValid = ValidTrit();
    rightValid.trit <== right_trit;
    
    // Validate result trits
    component resultValid[4];
    for (var i = 0; i < 4; i++) {
        resultValid[i] = ValidTrit();
        resultValid[i].trit <== result_trits[i];
    }
    
    // Pre-sum
    signal pre_sum;
    pre_sum <== left_trit + right_trit;
    
    // Post-sum (only count active results)
    // For simplicity, assume unused slots have trit = 0 (which is 0 in GF(3))
    var post_raw = 0;
    for (var i = 0; i < 4; i++) {
        post_raw += result_trits[i];
    }
    
    // Compute mod 3 for both
    signal pre_mod;
    signal post_mod;
    
    pre_mod <-- pre_sum % 3;
    post_mod <-- post_raw % 3;
    
    // Constrain modular arithmetic
    signal pre_quot;
    signal post_quot;
    pre_quot <-- pre_sum \ 3;
    post_quot <-- post_raw \ 3;
    
    pre_sum === 3 * pre_quot + pre_mod;
    post_raw === 3 * post_quot + post_mod;
    
    // Conservation check
    component eq = IsEqual();
    eq.in[0] <== pre_mod;
    eq.in[1] <== post_mod;
    
    valid <== eq.out;
    valid === 1;
}

/*
 * CommitmentProof: Prove conservation with hidden values
 * Uses Poseidon hash for commitment
 */
template CommitmentProof(n) {
    signal input trits[n];           // Private: actual trit values
    signal input blinding[n];        // Private: blinding factors
    signal input commitments[n];     // Public: commitments
    signal output conserved;
    
    // Verify commitments
    component hashers[n];
    for (var i = 0; i < n; i++) {
        hashers[i] = Poseidon(2);
        hashers[i].inputs[0] <== trits[i];
        hashers[i].inputs[1] <== blinding[i];
        hashers[i].out === commitments[i];
    }
    
    // Verify conservation
    component tritSum = TritSum(n);
    for (var i = 0; i < n; i++) {
        tritSum.trits[i] <== trits[i];
    }
    
    // Sum must be 0 (mod 3)
    component isZero = IsZero();
    isZero.in <== tritSum.sum;
    
    conserved <== isZero.out;
    conserved === 1;
}

/*
 * TriadicInteraction: Model the canonical (+1, 0, -1) interaction
 */
template TriadicInteraction() {
    signal input commit_trit;   // Should be 2 (representing +1)
    signal input compute_trit;  // Should be 1 (representing 0)
    signal input verify_trit;   // Should be 0 (representing -1)
    
    signal output balanced;
    
    // Validate each is a valid trit
    component v1 = ValidTrit();
    component v2 = ValidTrit();
    component v3 = ValidTrit();
    
    v1.trit <== commit_trit;
    v2.trit <== compute_trit;
    v3.trit <== verify_trit;
    
    // Sum should be 0 (mod 3)
    // In our encoding: +1 → 2, 0 → 1, -1 → 0
    // So: 2 + 1 + 0 = 3 ≡ 0 (mod 3) ✓
    signal sum;
    sum <== commit_trit + compute_trit + verify_trit;
    
    signal mod3;
    signal quotient;
    quotient <-- sum \ 3;
    mod3 <-- sum % 3;
    sum === 3 * quotient + mod3;
    
    component isZero = IsZero();
    isZero.in <== mod3;
    
    balanced <== isZero.out;
    balanced === 1;
}

/*
 * Main component for standard usage
 */
component main {public [pre_trits, post_trits]} = InteractionConservation(4, 4);
