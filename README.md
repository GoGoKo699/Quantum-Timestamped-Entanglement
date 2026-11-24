# Quantum Timestamped Entanglement

Can three timestamped heralds deliver a useful Bell pair while the optical phase drifts? A receiver measures the local excitation count at each node and uses the surviving coherence to produce a logical Bell pair. It uses three raw-link memories per node and a classical success flag.

In an ideal example with 80% genuine heralds, the receiver succeeds on **44.8%** of triples, with **Bell fidelity of at least 95.24%**. At the same fidelity, any receiver acting only on a timestamp-selected pair from those triples succeeds on at most **33.64%**. The comparison uses one false-herald product state and the same offered timestamps.

| Question | Result and scope |
| --- | --- |
| What do three heralds buy? | [Finite receiver and matched two-input bound](science/receiver.md) |
| How much does noise erode the gain? | [Storage, latency and both false-herald products](science/robustness.md) |
| What is the best rate in a sparse stream? | [Optimal Poisson-stream rate](science/stream.md) |
| Can three heralds reveal the long-stream loss? | [Matched phase clocks and the four-herald test](science/matched-phase-diagnostics.md) |
| How do I reproduce the examples? | [Verification commands and expected outputs](verification/README.md) |

Each isolated herald is separable after averaging over the unknown optical phase. The usable entanglement comes from the phase correlation between arrivals. For an ideal stream with **one false-herald product state**, Poisson herald rate $`\lambda`$, wrapped Brownian phase diffusion rate $`D`$, and fixed genuine probability $`q`$, the optimal sparse distillable rate is

```math
R=C q^2\frac{\lambda^2}{D}+o\!\left(\frac{\lambda^2}{D}\right),
\qquad C=\frac{\ln 2-\pi^2/24}{2\ln 2}\approx0.20336 .
```

The long observation limit precedes the sparse limit. Pair processing reaches the leading term. On clean streams, three-herald processing also reaches the next coefficient. The streaming protocol uses block hashing after the bounded-memory front end. The finite receiver delivers its heralded Bell pair directly.

## What three heralds cannot identify

At any three supplied timestamps, two phase clocks can give exactly the same source state. A fourth herald exposes their second-harmonic difference using local measurements. Yet at fixed Poisson herald rate $`\lambda`$, with ideal memories and all heralds genuine, the long-stream deficits from $`\lambda`$ ebits per unit time are $`\Theta(\sqrt{\lambda\kappa})`$ for Brownian drift and $`(\kappa/4)\log_2(\lambda/\kappa)+O_\lambda(\kappa)`$ for rare $`\pi`$ phase jumps with residual diffusion. Here the long observation limit precedes $`\kappa\downarrow0`$.

The [matched-clock result](science/matched-phase-diagnostics.md) uses the same harmonic construction as [Quantum Phase Drift Capacity](https://github.com/GoGoKo699/Quantum-Phase-Drift-Capacity), which studies unassisted transmission at fixed cadence.

## Read the science

Start with the [source and timing model](science/model.md), or follow the [scientific account](science/README.md). The [related work](references/RELATED_WORK.md) covers prior two-copy and three-to-one distillation, flexible pairing and the stochastic rate question. [Download the BibTeX bibliography](references/references.bib).

## Study the result

The [30 milestones](learning/MILESTONES.md) follow one worked triple from relative phase to finite receiver performance, stream distillation and the four-herald diagnostic. The [Preskill bridge](learning/ANCHOR_BRIDGE.md) connects the argument to *Quantum Shannon Theory*, updated June 2025.

## Purpose

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
