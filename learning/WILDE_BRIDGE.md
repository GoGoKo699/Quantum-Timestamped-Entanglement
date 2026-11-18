# From Wilde to timestamped entanglement

The educational anchor is Mark M. Wilde, *Quantum Information Theory*, second edition (Cambridge University Press, 2017). Use the sections below when a concept enters the project. The [30-milestone map](MILESTONES.md) leads from the physical source to the receiver and then to the rate of a random stream. [Publisher's book page](https://doi.org/10.1017/9781316809976)

## Reading route

| In the milestone map | Read in Wilde | Use it here |
| --- | --- | --- |
| M01–M12, preliminaries | §§3.2, 3.5–3.6 and §§4.1–4.4 | Represent a genuine raw link as a bipartite state, average over hidden phase and false-click labels, and reduce a block state to an individual click. |
| M13–M21, finite receiver | §§5.3–5.4, §§9.1–9.3 and §19.2 | Keep a measurement outcome in a classical register, derive the corresponding state update, and compare flagged Bell-pair success at a fixed fidelity under local operations and classical communication (LOCC). |
| M22–M29, stream | §§11.1–11.2, §§11.4–11.5, §§11.7–11.10 and §§19.2–19.3 | Turn a known timestamp block into an entropy score. Use conditional mutual information for the three-click correction, continuity to control separated blocks, and relative entropy for the rate converse. |
| M30, synthesis | §24.9 | Connect the coherent information of a mixed state to one-way distillation after local filtering. Identify the extra storage required for hashing and the charge for elapsed time. |

Wilde writes $`H(A)_\rho`$ for the von Neumann entropy of subsystem $`A`$ in state $`\rho`$. The project writes $`S(\rho_A)`$. Coherent information is $`I(A\rangle B)_\rho=H(B)_\rho-H(AB)_\rho`$ in Wilde's notation. The project measures entropy in bits, fidelity to a pure target by the expectation of its projector, and time gaps in units of $`D^{-1}`$, where $`D`$ is the phase diffusion rate.

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

The new step in the stream analysis is to express each clean timestamp block of $`n`$ links as a maximally correlated state with the entropy of an auxiliary state $`\sigma`$. Its uniform endpoint marginal has entropy $`n`$, yielding the coherent information $`n-S(\sigma)`$. After binning timestamps and removing cross-block phase, one-way hashing approaches that score. For the converse, compare the block with its separable diagonal state, evolve both through the same LOCC protocol, and test for the ideal Bell output. Relative-entropy monotonicity makes the same score an upper bound on the asymptotic rate.

The three-click connected score subtracts the two adjacent two-click scores. It equals $`I(Q_1:Q_3\mid Q_2)_\sigma`$ and is nonnegative by strong subadditivity. In the clean example above it is about $`0.13656`$ ebits. Continuity controls the contributions of intervals separated by a wide gap. This is where Wilde's conditional entropy and relative entropy tools meet the project's Brownian phase model.

Poisson timing then sets the frequency of those blocks. A herald arrives at rate $`\lambda`$ and has another herald within a diffusion time with probability of order $`\lambda/D`$. Averaging $`Y_2`$ over the rescaled gap gives the leading sparse rate coefficient $`0.2033577`$. Independent genuine probabilities multiply the leading term by $`q^2`$ in the one-sided false-click model. The clean next-order term also accounts for the connected three-click score and the change in the two-click gap density. The long observation limit comes first. [Stream proof](../science/stream.md)
