# Source, timing and tasks

Two nodes receive a stream of heralds from a single link. The timestamp and herald sign are public. Absorb the known sign by a local Pauli correction so that the remaining phase is an optical path phase. Conditional on the phase $`\phi_j`$ at time $`t_j`$, the ideal genuine raw state is

```math
|\psi(\phi_j)\rangle
=\frac{|0\rangle_A|1\rangle_B+e^{i\phi_j}|1\rangle_A|0\rangle_B}{\sqrt 2}.
```

The stationary phase is initially uniform on the circle. It follows wrapped Brownian motion with independent increments and first harmonic

```math
\mathbb E\,e^{i k (\phi(t+u)-\phi(t))}=e^{-k^2 D u},
\qquad k\in\mathbb Z,\quad u\geq 0.
```

The visibility between times $`t_i`$ and $`t_j`$ is $`e^{-D|t_i-t_j|}`$. The Brownian realization and genuine/false labels are inaccessible. The parties have local controls, local buffer qubits and classical communication. These resources do not supply the optical phase.

## False heralds

A raw herald is genuine with probability $`q`$, independent of the other heralds and of the phase. The simplest calibrated source model has one false-click component, with conditional state

```math
q|\psi(\phi_j)\rangle\langle\psi(\phi_j)|+(1-q)|00\rangle\langle00|.
```

Simultaneously exchanging the local basis labels covers a fixed false state $`|11\rangle`$. The robustness model permits both product states, with $`\alpha,\beta\geq 0`$ and $`q+\alpha+\beta=1`$. These are classical mixture weights. Conditional on the phase path and these labels, raw links are independent. The model holds the source parameters fixed. The setup does not provide phase tracking or additional pilot specimens.

One phase-averaged genuine link is the equal mixture of $`|01\rangle`$ and $`|10\rangle`$. The correlations nevertheless survive across two or more arrivals. For a cluster of raw links, an excitation-count measurement retains coherence between different assignments of those excitations to the same node. Those coherences depend only on phase differences within the cluster.

## Finite receiver comparison

Condition on the same three supplied timestamps and known source parameters. The receiver can retain all three raw links. The two-input comparator chooses any two timestamps and acts on their raw states by arbitrary local operations and classical communication. The selection can be randomized using the timestamps. The third specimen is unused by this comparator. The metric is success probability per supplied triple at a lower bound on conditional fidelity with a standard logical Bell pair. Every accepted branch, including a branch produced by padding the success flag, counts in the conditional fidelity. Success does not hide the probability of an abort.

In the basic finite comparison all operations and memories are ideal. The storage and gate extension declares when states are read out and bounds a comparator given ideal storage and earlier decoding. A third specimen measured as a phase pilot or used coherently is a different finite resource. The separate stream converse allows unrestricted collective processing of the stream.

## Distillable stream rate

The timestamps form an exogenous Poisson process of observed herald rate $`\lambda`$, independent of phase realizations and false-click labels. The horizon is elapsed time and includes every waiting interval. The Poisson model is a source assumption. It does not model hardware dead time, the optical pump budget or attempts that fail to herald beyond their inclusion in the elapsed time.

The ideal rate is the asymptotically achievable number of Bell pairs per time, using fixed output sizes below rate and unconditional trace-distance error tending to zero. It allows arbitrary timestamp-aware local operations, classical communication and ideal memories. Any conditioning and discards must be reflected in that time rate. The sparse expansion sends $`\lambda/D\to 0`$ after the long-time rate is defined. The finite receiver and the ideal stream benchmark therefore have distinct output-memory requirements.
