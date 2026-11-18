# Quantum Timestamped Entanglement

Can three time-stamped heralds deliver a useful Bell pair while the optical phase drifts? A receiver that measures the local excitation count can combine the three links without learning their phases. It uses three raw-link memories per node, preserves the coherence within each excitation sector, and outputs a logical Bell qubit with a classical success flag.

In one example with 80% genuine heralds, the receiver succeeds on **44.8%** of triples at **95.24%** Bell fidelity. At the same fidelity, any receiver acting only on a timestamp-selected pair from those triples succeeds on at most **33.64%**. The example uses ideal memories and controls and a single false-herald product state. A separate receiver bound includes storage dephasing, control error and both false-herald product states.

| Question | Result and scope |
| --- | --- |
| What do three heralds buy? | [Finite receiver and matched two-input bound](science/receiver.md) |
| How much does noise erode the gain? | [Storage, latency and false-herald analysis](science/robustness.md) |
| What is the best rate in a sparse stream? | [Optimal Poisson-stream rate](science/stream.md) |
| How can I reproduce the numerical examples? | [Verification commands and scope](verification/README.md) |

Each isolated herald is separable after averaging over the unknown optical phase. The usable entanglement comes from the phase correlation between arrivals. For Poisson herald rate $`\lambda`$, phase diffusion rate $`D`$, and independent genuine probability $`q`$, the leading ideal distillable rate is

```math
R = C q^2\frac{\lambda^2}{D} + o\!\left(\frac{\lambda^2}{D}\right),
\qquad C=\frac{\ln 2-\pi^2/24}{2\ln 2}\approx 0.20336 .
```

Here the long observation limit precedes the sparse limit, and $`q`$ is fixed. Pair processing reaches the leading coefficient. On clean streams, three-herald processing also reaches the next coefficient. The distillable-rate result uses block hashing after the bounded-memory front end. The finite receiver instead delivers a heralded output directly.

Start with the [model](science/model.md) or follow the [scientific account](science/README.md). The [related work](references/RELATED_WORK.md) covers the physical two-copy primitive, prior three-to-one protocols, flexible pairing and the phase-correlation rate question.
