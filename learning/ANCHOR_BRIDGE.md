# From Preskill to timestamped entanglement

The educational anchor is **John Preskill, *Quantum Information*, Chapter 10: *Quantum Shannon Theory*, updated June 2025**. Use the [official chapter PDF](https://www.preskill.caltech.edu/ph219/chap10_6A_2025.pdf). The [30 milestones](MILESTONES.md) lead from one raw link through the three-herald receiver to the rate of a random stream and the four-herald diagnostic.

## Reading route

| In the milestone map | Read in Preskill | Use it here |
| --- | --- | --- |
| M01–M12 | [§§10.2.1–10.2.4](https://www.preskill.caltech.edu/ph219/chap10_6A_2025.pdf#page=21) | Follow mixing and measurement, evaluate von Neumann entropy, and use subadditivity and monotonicity after a measurement. |
| M13–M21 | [§10.2.2](https://www.preskill.caltech.edu/ph219/chap10_6A_2025.pdf#page=22) | Use the entropy and measurement background alongside the project's explicit count instrument and negativity bound. |
| M22–M26 | [§§10.2.3–10.2.4](https://www.preskill.caltech.edu/ph219/chap10_6A_2025.pdf#page=23), [§10.7.1](https://www.preskill.caltech.edu/ph219/chap10_6A_2025.pdf#page=57) and [§10.8.2](https://www.preskill.caltech.edu/ph219/chap10_6A_2025.pdf#page=70) | Identify the block's coherent information, compare with a separable state using data processing, and use one-way hashing on independent blocks. |
| M27–M30 | [§§10.2.1–10.2.4](https://www.preskill.caltech.edu/ph219/chap10_6A_2025.pdf#page=21) and [§10.8.2](https://www.preskill.caltech.edu/ph219/chap10_6A_2025.pdf#page=70) | Connect dyad and triplet entropy scores to sparse-stream distillation, then contrast finite phase diagnosis with long-record entropy. |

Preskill writes $`H(A)`$ for von Neumann entropy of subsystem $`A`$. The project uses $`S(\rho_A)`$ and reserves $`H`$ for classical entropy. Both write coherent information as the entropy of Bob's marginal minus the entropy of the joint state, $`I_c(A\rangle B)=S(\rho_B)-S(\rho_{AB})`$. The project measures entropy in bits and fidelity to a pure target by the expectation of its projector. The sparse Brownian calculation expresses gaps in units of $`D^{-1}`$, with phase diffusion rate $`D`$.

The count circuit, negativity benchmark and Poisson averaging are developed in the [scientific account](../science/README.md). The chapter supplies the entropy inequalities, coherent information and hashing framework.

## From a state mixture to a useful measurement

A genuine click at time $`t`$ prepares a superposition with one excitation shared between the nodes. Its optical phase determines the relative amplitude of the two possible locations.

```math
|\psi(\phi_t)\rangle
=\frac{|0\rangle_A|1\rangle_B+e^{i\phi_t}|1\rangle_A|0\rangle_B}{\sqrt{2}}.
```

The nodes know the click time. Averaging over the unobserved phase, whose marginal is uniform, eliminates the off-diagonal entries of a single genuine link. The mixture of the two location states is separable. For nearby clicks, the phases are correlated. A term exchanging which click supplies Alice's excitation carries $`e^{i(\phi_j-\phi_i)}`$, whose mean is $`e^{-D(t_j-t_i)}`$. Averaging a whole block therefore preserves a coherence that averaging its individual links would erase. [Source model](../science/model.md)

Alice and Bob measure their local total excitation counts. Projecting onto a count preserves superpositions among the positions of those excitations. On two genuine clicks, both nodes have count one in half the runs. The two alternatives inside that sector produce the normalized logical state

```math
\rho(v)=\frac12
\left(
|00\rangle\langle00|+|11\rangle\langle11|
+v|00\rangle\langle11|+v|11\rangle\langle00|
\right),
\qquad
v=e^{-D(t_j-t_i)} .
```

The logical basis labels the placement of the local excitation. Bob reverses his position labels so that the two paired assignments have the same logical labels. In the Bell basis, the weights of $`|\Phi^+\rangle`$ and $`|\Phi^-\rangle`$ are $`(1+v)/2`$ and $`(1-v)/2`$. The former is the accepted state's fidelity to the target. The count measurement supplies a classical accept flag alongside a quantum output. [Receiver construction](../science/receiver.md)

## Follow one three-click block

Take consecutive gaps $`D(t_2-t_1)=D(t_3-t_2)=0.05`$. In the ideal finite example each click independently supplies the genuine state with probability $`q=0.8`$ and otherwise supplies the product $`|00\rangle`$. With three genuine clicks, the complementary count outcomes one and two occur with total probability $`3/4`$. Each side keeps three positions in superposition, indexed by the minority bit. The conditional state is supported on joint position labels $`|i,i\rangle`$. In this basis, with $`a=e^{-0.05}`$, its matrix is

```math
M_3=\frac13
\begin{pmatrix}
1 & a & a^2\\
a & 1 & a\\
a^2 & a & 1
\end{pmatrix}.
```

Alice's filter announces a pair of positions while preserving their coherence. Bob relabels those same positions. The output has the two-dimensional form $`\rho(v)`$, with $`v=a`$ for adjacent positions and $`v=a^2`$ for the two ends. The third click also enables a fallback when the preferred pair is genuine and the remaining click is false. That event has probability $`q^2(1-q)`$, and the fallback accepts half of those events. The total success and the minimum accepted fidelity are

```math
P_3=\frac34q^3+\frac12q^2(1-q)=0.448,\qquad
F_*=\frac{1+a^2}{2}\simeq0.95242.
```

To compare receivers, hold this fidelity fixed and let the rival choose any two of the offered timestamps before processing those two raw states. The best available input visibility is $`a`$. The state's negativity is $`q^2a/4`$. Since a two-qubit output of fidelity $`F_*`$ needs negativity at least $`F_*-1/2`$, average monotonicity of negativity gives

```math
P_2\left(F_*-\tfrac12\right)\le \frac{q^2a}{4},
\qquad
P_2\le \frac{q^2}{2a}\simeq0.33641 .
```

This inequality charges the full success probability, including low-fidelity outputs added to a success branch. It applies to operations on the selected two inputs, with the third input discarded. For a model that includes storage, a full flagged-instrument error budget, and both false-click polarities, follow the same success-versus-fidelity comparison in the [robustness analysis](../science/robustness.md).

## Follow the same positions into the rate proof

In the ideal clean stream, use the same three timestamps and keep the entire logical qutrit when the count sector supports it. The finite receiver converts this sector to one heralded logical Bell pair. The stream receiver retains the sector and distills with many compatible outputs. The distillation score of a two-click block is obtained from its accepted branch's coherent information. Its reduced state is maximally mixed and its joint entropy is the binary entropy of the Bell weights. Including the half of the runs with matching local counts gives, for a gap $`x`$ in units of $`D^{-1}`$,

```math
Y_2(x)=\frac12\left[1-h_2\!\left(\frac{1+e^{-x}}2\right)\right],
\qquad
h_2(p)=-p\log_2p-(1-p)\log_2(1-p).
```

For the two short gaps just used, $`Y_2(0.05)\simeq0.41730`$ ebits per offered clean dyad. The three-click analogue includes the nontrivial sector probability $`3/4`$ and uses the entropy of $`M_3`$. It is $`\tfrac34[\log_2 3-S(M_3)]\simeq0.97116`$ ebits per offered clean triplet. These figures count the offered clean blocks. Converting them to a rate also counts the time spent waiting for suitable clicks.

The key step in the stream analysis is to express each clean timestamp block of $`n`$ links as a maximally correlated state with the entropy of an auxiliary state $`\sigma`$. Its uniform endpoint marginal has entropy $`n`$, yielding the coherent information $`n-S(\sigma)`$. After binning timestamps and removing cross-block phase, one-way hashing approaches that score. For the converse, compare the block with its separable diagonal state, evolve both through the same LOCC protocol, and test for the ideal Bell output. Relative-entropy monotonicity makes the same score an upper bound on the asymptotic rate.

The three-click connected score subtracts the two adjacent two-click scores. It equals $`I(Q_1:Q_3\mid Q_2)_\sigma`$ and is nonnegative by strong subadditivity. In the clean example above it is about $`0.13656`$ ebits. Continuity controls the contributions of intervals separated by a wide gap. Preskill's entropy inequalities apply after the Brownian model specifies the state. The interval analysis supplies the continuity estimate.

Poisson timing then sets the frequency of those blocks. A herald arrives at rate $`\lambda`$ and has another herald within a diffusion time with probability of order $`\lambda/D`$. Averaging $`Y_2`$ over the rescaled gap gives the leading sparse rate coefficient $`0.2033577`$. Independent genuine probabilities multiply the leading term by $`q^2`$ in the one-sided false-click model. The clean next-order term also accounts for the connected three-click score and the change in the two-click gap density. The long observation limit comes first. [Stream proof](../science/stream.md)

## From a triplet to a phase diagnostic

The worked triplet only samples the first harmonic of the gap phase. Any surviving coherence between equal-weight strings has a suffix charge in $`\{-1,0,1\}`$ at each gap when there are at most three heralds. A wrapped Brownian clock of variance rate $`\kappa+\kappa^4`$ and a clock with variance rate $`\kappa^4`$ plus independent $`\pi`$ jumps of rate $`\kappa/4`$ have the same first harmonic at every gap. They therefore give the same whole source state for any supplied triplet.

Four heralds permit the two local strings $`x=0011`$ and $`y=1100`$. The two sequences have the same total excitation count, but the middle gap carries suffix charge two. Keep their span on each side, then measure the logical $`X`$ basis and compare the two classical outcomes. Their parity tests precisely the coherence where the two models differ. The [matched-clock proof](../science/matched-phase-diagnostics.md) gives the exact success probability and why this local measurement reaches it.

For the clean, ideal Poisson stream, hold the herald intensity $`\lambda`$ fixed, define the long-time rate first, and let $`\kappa`$ tend to zero. The Brownian clock's rate deficit from $`\lambda`$ ebits per time has order $`\sqrt{\lambda\kappa}`$. The jump clock loses $`(\kappa/4)\log_2(\lambda/\kappa)+O_\lambda(\kappa)`$. The sparse expansion above instead sends the herald intensity to zero relative to the Brownian diffusion rate. [Quantum Phase Drift Capacity](https://github.com/GoGoKo699/Quantum-Phase-Drift-Capacity) uses the same charge calculation for communication on a fixed-cadence train, with every transmitted carrier counted.
