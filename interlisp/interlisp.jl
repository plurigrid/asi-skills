"""
    Interlisp Environment as ACSet

Bridges Interlisp-D/Medley concepts with ACSets.jl:
- DWIM (Do What I Mean) as Galois connection
- SEdit structure editing via Specter navigation
- Programmer's Assistant edit history as groupoid
- Masterscope cross-reference as functorial analysis
"""
module Interlisp

using Catlab
using Catlab.CategoricalAlgebra

# ============================================================================
# Schema: Interlisp Environment
# ============================================================================

@present SchInterlisp(FreeSchema) begin
    (Fn, Var, File, History, Breakpoint)::Ob

    # Function call graph (Masterscope)
    calls::Hom(Fn, Fn)
    defines::Hom(Fn, File)
    binds::Hom(Var, Fn)

    # Edit history (Programmer's Assistant)
    prev::Hom(History, History)
    target::Hom(History, Fn)

    # Debugging
    at_fn::Hom(Breakpoint, Fn)

    # Attributes
    (Name, SexpStr, Timestamp)::AttrType
    fn_name::Attr(Fn, Name)
    fn_body::Attr(Fn, SexpStr)
    var_name::Attr(Var, Name)
    file_name::Attr(File, Name)
    edit_time::Attr(History, Timestamp)
end

@acset_type InterlispEnv(SchInterlisp, index=[:calls, :defines, :binds, :fn_name])

# ============================================================================
# DWIM: Do What I Mean
# ============================================================================

"""
    DWIMStrategy

Configuration for DWIM correction. Controls which heuristics are applied
when an unrecognized symbol is encountered.
"""
struct DWIMStrategy
    edit_distance::Int
    scope_search::Bool
    spelling_correct::Bool
    paren_balance::Bool
end

DWIMStrategy() = DWIMStrategy(2, true, true, true)

"""
    dwim_candidates(name::String, env::InterlispEnv, strategy::DWIMStrategy)

Find candidate corrections for an unrecognized symbol using DWIM heuristics.
Returns vector of (candidate_name, distance) pairs sorted by distance.
"""
function dwim_candidates(name::String, env::InterlispEnv, strategy::DWIMStrategy)
    candidates = Tuple{String, Int}[]

    if strategy.spelling_correct
        for fn_id in parts(env, :Fn)
            fn = env[fn_id, :fn_name]
            d = levenshtein(name, fn)
            if d <= strategy.edit_distance
                push!(candidates, (fn, d))
            end
        end
    end

    sort!(candidates, by=last)
    candidates
end

"""
    levenshtein(s::AbstractString, t::AbstractString) -> Int

Compute Levenshtein edit distance between two strings.
"""
function levenshtein(s::AbstractString, t::AbstractString)
    m, n = length(s), length(t)
    d = zeros(Int, m + 1, n + 1)
    for i in 0:m; d[i+1, 1] = i; end
    for j in 0:n; d[1, j+1] = j; end
    for j in 1:n, i in 1:m
        cost = s[i] == t[j] ? 0 : 1
        d[i+1, j+1] = min(
            d[i, j+1] + 1,      # deletion
            d[i+1, j] + 1,      # insertion
            d[i, j] + cost       # substitution
        )
    end
    d[m+1, n+1]
end

# ============================================================================
# Programmer's Assistant: Edit History
# ============================================================================

"""
    EditOp

A single edit operation in the Programmer's Assistant history.
Stores before/after states for undo/redo.
"""
struct EditOp
    kind::Symbol
    target_fn::Int
    before::String
    after::String
    timestamp::Float64
end

"""
    ProgrammersAssistant

Maintains undo/redo history of all edits to the Interlisp environment.
Models edit history as a groupoid (every edit has an inverse).
"""
mutable struct ProgrammersAssistant
    history::Vector{EditOp}
    cursor::Int
end

ProgrammersAssistant() = ProgrammersAssistant(EditOp[], 0)

function record!(pa::ProgrammersAssistant, op::EditOp)
    # Truncate redo history beyond cursor
    resize!(pa.history, pa.cursor)
    push!(pa.history, op)
    pa.cursor += 1
    op
end

function undo!(pa::ProgrammersAssistant, env::InterlispEnv)
    pa.cursor < 1 && error("Nothing to undo")
    op = pa.history[pa.cursor]
    env[op.target_fn, :fn_body] = op.before
    pa.cursor -= 1
    op
end

function redo!(pa::ProgrammersAssistant, env::InterlispEnv)
    pa.cursor >= length(pa.history) && error("Nothing to redo")
    pa.cursor += 1
    op = pa.history[pa.cursor]
    env[op.target_fn, :fn_body] = op.after
    op
end

# ============================================================================
# Masterscope: Cross-Reference Analysis
# ============================================================================

"""
    masterscope(env::InterlispEnv) -> ACSet

Extract the function call graph from the environment as an ACSet.
Functorial: preserves composition of call chains.
"""
function masterscope_graph(env::InterlispEnv)
    n = nparts(env, :Fn)
    g = @acset Graphs.Graph begin
        V = n
    end

    for fn_id in parts(env, :Fn)
        body = env[fn_id, :fn_body]
        called = extract_called_names(body)
        for callee_name in called
            callee_ids = incident(env, callee_name, :fn_name)
            for cid in callee_ids
                add_part!(g, :E, src=fn_id, tgt=cid)
            end
        end
    end

    g
end

"""
    who_calls(env::InterlispEnv, fn_name::String)

Return names of all functions that call `fn_name` (Masterscope WHO-CALLS).
"""
function who_calls(env::InterlispEnv, fn_name::String)
    g = masterscope_graph(env)
    fn_ids = incident(env, fn_name, :fn_name)
    isempty(fn_ids) && return String[]

    callers = Int[]
    for fid in fn_ids
        edges = incident(g, fid, :tgt)
        append!(callers, g[edges, :src])
    end

    [env[c, :fn_name] for c in unique(callers)]
end

"""
    calls_who(env::InterlispEnv, fn_name::String)

Return names of all functions called by `fn_name` (Masterscope CALLS-WHO).
"""
function calls_who(env::InterlispEnv, fn_name::String)
    g = masterscope_graph(env)
    fn_ids = incident(env, fn_name, :fn_name)
    isempty(fn_ids) && return String[]

    callees = Int[]
    for fid in fn_ids
        edges = incident(g, fid, :src)
        append!(callees, g[edges, :tgt])
    end

    [env[c, :fn_name] for c in unique(callees)]
end

# ============================================================================
# Advising: Aspect-Oriented Function Wrapping
# ============================================================================

"""
    Advice

Wraps a function with before/after/around advice (Interlisp ADVISE).
Precursor to aspect-oriented programming.
"""
struct Advice
    kind::Symbol        # :before, :after, :around
    target::String      # Function name
    body::String        # Advice S-expression
end

function apply_advice(original_body::String, advice::Advice)
    if advice.kind == :before
        "(PROGN $(advice.body) $original_body)"
    elseif advice.kind == :after
        "(PROG1 $original_body $(advice.body))"
    elseif advice.kind == :around
        replace(advice.body, "INNER" => original_body)
    else
        error("Unknown advice kind: $(advice.kind)")
    end
end

# ============================================================================
# S-expression Utilities
# ============================================================================

"""
    extract_called_names(sexp_str::String) -> Vector{String}

Extract function names called in an S-expression body.
Simple heuristic: symbols immediately after '(' that are uppercase.
"""
function extract_called_names(sexp_str::String)
    names = String[]
    for m in eachmatch(r"\(([A-Z][A-Z0-9_-]*)", sexp_str)
        push!(names, m.captures[1])
    end
    unique(names)
end

"""
    balance_parens(s::String) -> String

Auto-balance parentheses in an S-expression string (DWIM paren balancing).
"""
function balance_parens(s::String)
    depth = 0
    for c in s
        c == '(' && (depth += 1)
        c == ')' && (depth -= 1)
    end
    if depth > 0
        s * ")" ^ depth
    elseif depth < 0
        "(" ^ (-depth) * s
    else
        s
    end
end

# ============================================================================
# Environment Construction
# ============================================================================

"""
    new_env() -> InterlispEnv

Create a fresh Interlisp environment.
"""
function new_env()
    InterlispEnv()
end

"""
    define_fn!(env::InterlispEnv, name::String, body::String, file::String="INIT")

Define a new function in the environment.
"""
function define_fn!(env::InterlispEnv, name::String, body::String, file::String="INIT")
    # Find or create file
    file_ids = incident(env, file, :file_name)
    fid = if isempty(file_ids)
        add_part!(env, :File, file_name=file)
    else
        first(file_ids)
    end

    # Add function
    add_part!(env, :Fn, fn_name=name, fn_body=body, defines=fid)
end

export InterlispEnv, DWIMStrategy, ProgrammersAssistant, EditOp, Advice
export dwim_candidates, levenshtein, balance_parens
export masterscope_graph, who_calls, calls_who
export apply_advice, define_fn!, new_env
export undo!, redo!, record!

end # module
