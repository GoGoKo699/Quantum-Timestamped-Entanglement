# Three-herald receiver

A single herald leaves no usable entanglement once its uniformly distributed optical phase is averaged out. A short group of heralds retains relative phases. The receiver uses local excitation counts to isolate sectors where the absolute phase cancels, then converts the remaining coherence into a Bell pair.

## Input and output

At three known times $`t_1<t_2<t_3`$, the two nodes receive one raw qubit each per herald. Independently at each herald, with probability $`q`$ the joint state is

```math
|\psi(\phi_j)\rangle
=\frac{|01\rangle+e^{i\phi_j}|10\rangle}{\sqrt{2}}.
```

With probability $`1-q`$ it is $`|00\rangle`$. These source labels are hidden. Heralds carrying a known detection sign can first be corrected by a local phase flip. The optical phase is stationary and uniform on the circle, with Brownian increments satisfying $`\mathbb E[e^{i(\phi_j-\phi_i)}]=e^{-D(t_j-t_i)}`$ for $`j>i`$. Write

```math
a=e^{-D(t_2-t_1)},\qquad
b=e^{-D(t_3-t_2)},\qquad
v_{12}=a,\quad v_{23}=b,\quad v_{13}=ab .
```

The nodes have ideal local operations, classical messages, and three raw-link memory cells each. The receiver announces failure or delivers one logical qubit at each node. Its fidelity is the overlap with the fixed output target $`|\Phi^+\rangle=(|00\rangle+|11\rangle)/\sqrt2`$ in the declared logical encoding. The receiver uses timestamps, count outcomes, and the known detection signs.

## Protocol

Each node computes and measures its local excitation count. This must preserve superpositions of different positions at the same count. For example, on binary occupancies $`z_1,z_2,z_3`$, the two bits of the count are $`z_1\oplus z_2\oplus z_3`$ and $`z_1z_2\oplus z_1z_3\oplus z_2z_3`$. Three CNOTs and three Toffoli gates compute these into a two-qubit ancillary register. Measuring this register implements the count projection without a position measurement. The nodes exchange their counts.

| Joint counts | Local processing |
| --- | --- |
| $`(1,2)`$ or $`(2,1)`$ | Relabel each node's three-dimensional sector by the position of its minority bit. The position of the single excitation at one node equals the position of the single vacancy at the other. Apply the two-position filter described below. |
| $`(1,1)`$ | Select the two closest timestamps, with a fixed tie rule. Each node projects onto the subspace in which its single excitation belongs to one of those two slots. Accept if both projections pass. |
| All other outcomes | Announce failure. |

In a three-dimensional sector, Alice uses the three-outcome instrument with Kraus operators

```math
K_{\{i,j\}}=\frac{|i\rangle\langle i|+|j\rangle\langle j|}{\sqrt{2}},
\qquad 1\le i<j\le3.
```

Each level occurs in exactly two operators, so $`\sum_{\{i,j\}}K_{\{i,j\}}^\dagger K_{\{i,j\}}=I`$. One implementation attaches a flag register to level $`k`$ in the equal superposition of the two labels $`\{i,j\}`$ that contain $`k`$, then measures the flag. Alice sends the accepted label. Both nodes map positions $`i`$ and $`j`$ to logical zero and one in the same order. In the $`(1,1)`$ case Bob reverses his position labels so his logical index also agrees with Alice's.

## Exact success and fidelity

All three heralds must be genuine if the count sum is three. Conditional on three genuine heralds, the two accepted count patterns have probabilities $`3/8`$ each. This follows from the uniform occupancies in the computational basis of the three-link pure state. Within either accepted sector, dephasing by the Brownian phase leaves a maximally correlated qutrit state. In the common minority-position index its matrix on $`\{|11\rangle,|22\rangle,|33\rangle\}`$ is

```math
\frac{1}{3}
\begin{pmatrix}
1 & a & ab\\
a & 1 & b\\
ab & b & 1
\end{pmatrix}.
```

For a weight-one output at Alice, its $`(i,j)`$ element is proportional to $`\mathbb E[e^{i(\phi_i-\phi_j)}]`$. For a weight-two output it is the conjugate, which is equal here because the Brownian phase moment is real. Each filter label occurs with probability $`1/3`$ in either sector. For label $`\{i,j\}`$ the normalized two-qubit output is

```math
\sigma(v_{ij})
=\frac{1}{2}\left(
|00\rangle\langle00|+|11\rangle\langle11|
+v_{ij}|00\rangle\langle11|+v_{ij}|11\rangle\langle00|
\right).
```

In a $`(1,1)`$ sector exactly two heralds were genuine. The two local support projections pass precisely when those two genuine heralds occupy the selected slots. That source label pattern has probability $`q^2(1-q)`$ and gives $`(1,1)`$ with probability $`1/2`$. The output on this branch is $`\sigma(\max(a,b))`$.

Every accepted branch therefore has fidelity at least $`F_\star=(1+ab)/2`$. The success probability per generated three-herald block is

```math
P_3=\frac{3q^3}{4}+\frac{q^2(1-q)}{2}
=\frac{q^2}{2}+\frac{q^3}{4}.
```

If the application consumes a qutrit instead of a qubit, it can keep the full accepted count-three sector. Its use for block distillation is a different output contract from the finite Bell-pair guarantee.

## Best two retained inputs at matched fidelity

Allow the comparator to choose any two of the three heralds from their timestamps, possibly at random. It has arbitrary LOCC on those two links. This includes finer success scores and padding an acceptance branch with low-fidelity outcomes, provided the resulting conditional state meets the target. The comparator discards the unselected raw link.

For two links at a gap with visibility $`v`$, all joint-count sectors except $`(1,1)`$ are separable. The exceptional block appears with probability $`q^2/2`$ and has the form $`\sigma(v)`$. The input is block diagonal under the local count flags. Its negativity is therefore exactly $`q^2 v/4`$, since $`\sigma(v)`$ has negativity $`v/2`$. This is the same two-input charge sector analyzed in the earlier remote-entanglement protocol. [Rozpędek et al., Sec. IV.D](https://doi.org/10.1103/PhysRevA.97.062333)

For any conditional two-qubit output $`\tau`$ of fidelity $`F`$, the partial transpose $`(\Phi^+)^\Gamma`$ has operator norm $`1/2`$. Thus

```math
F=\operatorname{Tr}[\tau^\Gamma(\Phi^+)^\Gamma]
\leq \frac{\|\tau^\Gamma\|_1}{2}
=\frac{1}{2}+{\cal N}(\tau).
```

Negativity cannot increase on average under LOCC. Applying this to a local instrument with a success flag gives $`P(F-1/2)\le q^2 v/4`$. The bound still holds if the successful state averages several labeled outputs with their respective local corrections. [Vidal and Werner](https://doi.org/10.1103/PhysRevA.65.032314)

Since $`\max(a,b)`$ is the maximum available $`v`$, at the three-input target the two-input success probability obeys

```math
P_2\le
\frac{q^2\max(a,b)}{2ab}
=\frac{q^2}{2\min(a,b)} .
```

Consequently $`P_3>P_2`$ on the open parameter range $`\min(a,b)>2/(2+q)`$. This bound covers arbitrary two-input postprocessing under the stated selection rule.

For $`q=0.8`$ and $`D(t_2-t_1)=D(t_3-t_2)=0.05`$, the target fidelity is $`F_\star=0.952418709`$. The three-input success probability is $`0.448000`$, while the two-input upper bound is $`0.336407`$. The guarantee is conditional on the three chosen timestamps. A throughput comparison must also count the waiting time for those timestamps and the use of memory during the wait. See [storage and implementation errors](robustness.md).
