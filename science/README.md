# Scientific account

1. [Source, timing and tasks](model.md) defines the stochastic link, the two-input benchmark, and the operational ebit rate.
2. [Three-herald receiver](receiver.md) constructs the local excitation-count circuit, derives the accepted Bell state, and bounds any decoder acting only on a selected pair.
3. [Poisson-stream optimum](stream.md) derives the leading distillable rate over all timestamp-aware local operations and classical communication, and develops the clean three-herald correction.
4. [Robustness and resource accounting](robustness.md) puts finite storage, decoding latency, control error and two false-click types into the receiver comparison.
5. [Matched phase clocks](matched-phase-diagnostics.md) proves complete agreement through three heralds, an optimal local four-herald test, and different long-record distillation deficits at fixed Poisson intensity. [Quantum Phase Drift Capacity](https://github.com/GoGoKo699/Quantum-Phase-Drift-Capacity) gives the fixed-cadence carrier-channel counterpart.

See [prior work](../references/RELATED_WORK.md) for the inherited constructions and [verification](../verification/README.md) for reproducible finite checks.
