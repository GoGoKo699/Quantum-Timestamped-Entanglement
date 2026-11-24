# Identical three-herald states, different stream rates

Can complete knowledge of every three-herald state determine the leading entanglement loss of a clean stream? Two phase laws from [Quantum Phase Drift Capacity](https://github.com/GoGoKo699/Quantum-Phase-Drift-Capacity/blob/0b6f844275b7fb98e6a0bc380369c20b787798a8/science/growing-diagnostics.md) agree at every such set of timestamps. On the same Poisson clock they have different optimal weak-noise rate losses.

## Model and result

The herald clock is Poisson with fixed intensity $`\lambda\gt0`$, independent of phase. Every herald supplies a genuine pair. The endpoints have the timestamps, ideal storage and arbitrary local quantum operations with classical communication. The rate counts ebits per elapsed time, with a fixed output size and vanishing unconditional error. We use the [clean-stream convention](stream.md#clean-stream-as-an-entropy-rate) and take the long-time limit before the weak-noise limit. The formulas for the two phase laws use a fixed time unit.

Both laws start at a uniform phase and have stationary independent increments. In model A the unwrapped Brownian variance rate is $`\kappa+\kappa^4`$. In model B there is Brownian variance rate $`\kappa^4`$ and an independent Poisson process of $`\pi`$ jumps with intensity $`\kappa/4`$. The physical phase is taken modulo $`2\pi`$.

The complete conditional states agree for every set of at most three distinct timestamps. For every four distinct timestamps there is a local test with strictly better than random success for equal priors. If $`R_A`$ and $`R_B`$ are the optimal long-stream rates, then, at fixed $`\lambda`$,

$`\lambda-R_A=\Theta(\sqrt{\lambda\kappa})`$ and $`\lambda-R_B=(\kappa/4)\log_2(\lambda/\kappa)+O_\lambda(\kappa)`$ as $`\kappa\downarrow0`$.

Both rates approach $`\lambda`$. The ratio of their gaps to this ceiling diverges. The finite diagnostic concerns the total number of distinct links supplied to a test. A long run of tests that accesses more links has a different sample budget.

## Equality through three heralds

After Bob flips each qubit, the raw state is $`V\sigma V^\dagger`$, with $`V|x\rangle=|x,x\rangle`$ and

```math
\sigma=2^{-n}\sum_{x,y}\mathbb E\exp\!\left[i\sum_j(x_j-y_j)\phi(t_j)\right]|x\rangle\langle y|.
```

Uniform initial phase makes the matrix element vanish unless $`x`$ and $`y`$ have equal weight. In that case the expectation is a product of increment harmonics, one per gap, at the suffix charge of $`x-y`$. The absolute suffix charge is at most $`\lfloor n/2\rfloor`$. For a gap $`u`$, the two harmonics at integer charge $`k`$ are

```math
\begin{aligned}
\chi_A(k,u)&=\exp[-u(\kappa+\kappa^4)k^2/2],\\
\chi_B(k,u)&=\exp[-u\kappa^4k^2/2+u(\kappa/4)((-1)^k-1)].
\end{aligned}
```

They coincide at $`k=0,\pm1`$. At four timestamps, the only differing entries are the two conjugate coherences for $`x=0011`$ and $`y=1100`$. Write $`d_i=t_{i+1}-t_i`$. The two multipliers obey $`c_A=e^{-2\kappa d_2}c_B`$, with $`c_B=e^{-(\kappa+\kappa^4)(d_1+d_3)/2-2\kappa^4d_2}`$.

Each endpoint projects onto the span of these two strings. The successful branch has probability $`1/8`$ and is a logical Bell pair with visibility $`c_A`$ or $`c_B`$. The parties measure logical $`X`$ locally and compare outcomes. Random guesses elsewhere give success $`1/2+(c_B-c_A)/32`$. This equals the global Helstrom bound because the state difference has only the two conjugate entries of magnitude $`(c_B-c_A)/16`$. For two pairs with $`\kappa(d_1+d_3)\to0`$ separated by a gap with $`\kappa d_2\to\infty`$ and $`\kappa^4d_2\to0`$, the block scores tend to $`1`$ and $`9/8`$ ebits. The stream proof below accounts for the actual arrival times and all clicks.

## Optimal rate is an entropy rate

For an observation of duration $`T`$, let $`N_T`$ be the number of arrivals and $`\sigma_T`$ the auxiliary state conditioned on the full timestamp record. The clean-stream proof uses the uniform local marginals and gives

```math
\lambda-R=\lim_{T\to\infty}\frac{\mathbb E S(\sigma_T)}{T}.
```

For the converse, the uniform dephased state on the strings $`|x,x\rangle`$ is separable and has relative entropy $`N_T-S(\sigma_T)`$ from the raw state. A binary test of an $`m`$-ebit target after any timestamp-conditioned LOCC compares fidelity $`F`$ with a separable overlap of at most $`2^{-m}`$. It gives the bound $`Fm-1\le N_T-S(\sigma_T)`$. Averaging includes every record. For attainment, independent total-charge twirls on fixed-duration blocks kill interblock charge differences. Each neutral block depends only on its internal increments, so the twirled conditional state factorizes. Independent Poisson timestamp records, finite bins of timestamp vectors after a count cutoff, and one-way hashing give the mean block score per elapsed time. Finite-dimensional continuity and the integrable click-count tail allow removal of the binning and cutoff. Mean entropy subadditivity and stationarity give the long-time limit by tiling. These steps apply to both increment semigroups.

## Brownian entropy bounds on the Poisson clock

Let $`v`$ be a Brownian variance rate. To lower-bound entropy, tile the observation into windows of length $`L=(\lambda v)^{-1/2}`$. Condition on the unwrapped Brownian endpoints, the initial phase, and the bridge residual after removing the midpoint height in each window. Entropy concavity bounds the original entropy from below by the mean conditional entropy. Conditional states factor across windows up to fixed diagonal rotations. In one window the remaining random phase at time $`t`$ is $`X f(t/L)`$, where $`X`$ is Gaussian with variance $`vL/4`$ and $`f(s)=2\min(s,1-s)`$. The height and the residual are independent by Gaussian regression, and different windows have independent heights.

Conditional purity at times $`t_i`$ is $`\mathbb E_Z\prod_i\cos^2(f(t_i/L)Z/2)`$ for a Gaussian $`Z`$ of variance $`vL/2`$. The Poisson generating functional makes its timestamp average

```math
\mathbb E_Z\exp\!\left[-\lambda\int_0^L\sin^2(f(t/L)Z/2)\,dt\right].
```

With a fixed positive probability, $`|Z|`$ is between one and two of its standard deviations. For small $`v`$ it is then at most one, and on the middle half-window $`f\ge1/2`$. On this event, the exponent has magnitude bounded below by a positive constant because $`\lambda v L^2=1`$. Thus the average purity is bounded away from one. Using $`S\ge-\log_2\operatorname{Tr}\sigma^2`$ and Jensen gives a constant positive mean entropy per full window, or at least $`c\sqrt{\lambda v}`$ per unit time. The conditioning is used only in this entropy inequality.

For the upper bound, set the initial angle to zero and put back its uniform twirl at entropy cost at most $`\log_2(N_T+1)`$. The state with the initial angle fixed has the same nonzero spectrum as the uniform mixture of coherent states with real amplitudes

```math
\alpha_x(s)=\sqrt v\sum_i (x_i-\tfrac12)\mathbf 1_{[0,t_i]}(s),
\qquad 0\le s\le T.
```

This follows by comparing coherent-state overlaps with the Brownian characteristic function in the entries of $`\sigma`$. Define $`M=\sum_i|\mathbf1_{[0,t_i]}\rangle\langle\mathbf1_{[0,t_i]}|`$. Its nonzero eigenvalues are the eigenvalues of the click covariance matrix $`(\min(t_i,t_j))_{ij}`$. The mean photon number in the corresponding environment mode is $`v\,\mathrm{eig}(M)/4`$. Subadditivity and the single-mode maximum entropy at fixed photon number bound the entropy by $`\operatorname{Tr}g(vM/4)`$, where $`g(z)=(z+1)\log_2(z+1)-z\log_2 z`$.

In the eigenbasis of $`\mathbb E M`$, scalar Jensen applied first to spectral weights and then to timestamps gives $`\mathbb E\operatorname{Tr}g(vM/4)\le\operatorname{Tr}g(v\mathbb E M/4)`$. The mean kernel is $`\lambda(T-\max(s,u))`$, with eigenvalues $`\lambda T^2/[\pi^2(j-1/2)^2]`$, $`j=1,2,\ldots`$. The sum divided by $`T`$ converges to its integral, with integrable logarithmic behavior at zero and $`O(u^{-2}\log u)`$ at infinity. In particular, $`\int_0^\infty g(u^{-2})\,du=2\pi/\ln 2`$ by integration by parts. The common twirl costs $`o(T)`$ in expectation. This proves that the entropy rate is at most $`\sqrt{\lambda v}/\ln 2`$. In model A the lower and upper bounds have the same order.

## The jump arm is governed by sampled parity

Absorb the parity at the first click into the uniform starting phase. Condition on the weak Brownian path and this common phase for an entropy lower bound. At each click, the two local phase states with and without a $`\pi`$ flip are orthogonal. The resulting parity strings have entropy $`\sum_i h_2(p(d_i))`$ with

```math
p(d)=\frac{1-e^{-\kappa d/2}}{2}.
```

Conversely, mixing the weak Brownian state over sampled parity strings adds at most this string entropy. The remaining weak Brownian entropy rate is at most $`\sqrt{\lambda}\kappa^2/\ln 2`$ by the upper bound just proved. The jump-arm gap is therefore between $`J`$ and $`J+\sqrt{\lambda}\kappa^2/\ln 2`$, where $`J=\lambda\mathbb E_{\Delta\sim\operatorname{Exp}(\lambda)}h_2(p(\Delta))`$. The renewal average follows by integrating the adjacent-pair intensity $`\lambda^2(T-d)e^{-\lambda d}`$ on $`0\lt d\lt T`$ and dividing by $`T`$.

Set $`a=\kappa/(4\lambda)`$ and $`U=\lambda\Delta`$. Then $`p=(1-e^{-2aU})/2`$, $`\mathbb E p=a/(1+2a)`$, and $`p/a\le U`$. In $`h_2(p)=p\log_2(1/p)+O(p)`$ the correction from replacing $`\log_2(1/p)`$ by $`\log_2(1/a)`$ has expected magnitude $`O(a)`$, since $`x|\log_2 x|`$ is bounded on $`[0,1]`$ and $`\mathbb E[U\log_2(1+U)]`$ is finite. This yields the stated leading coefficient.

## Relation to earlier results

[Phase Drift Capacity](https://github.com/GoGoKo699/Quantum-Phase-Drift-Capacity/blob/0b6f844275b7fb98e6a0bc380369c20b787798a8/science/growing-diagnostics.md) supplies the harmonic match and its use in unit-cadence channel capacity. Here, the source is a timestamp-conditioned maximally correlated state, and the objective is distillation per unit time. [Devetak and Winter](https://arxiv.org/abs/quant-ph/0306078) supply the hashing step. [D’Arrigo, Benenti and Falci](https://arxiv.org/abs/quant-ph/0703014) give a memory-channel precedent for the entropy of correlated phase errors. [Rozpędek et al.](https://doi.org/10.1103/PhysRevA.97.062333) treat distillation from correlated pairs. [Wiseman](https://doi.org/10.1364/OL.599036) obtains square-root Rényi-2 entropy flow for a coherent laser beam. The joint result concerns complete agreement of the supplied few-herald states together with separated optimal von Neumann entropy losses on a Poisson stream of qubit pairs.

The rate theorem uses genuine heralds and ideal operations and storage. Its weak-noise regime has fixed intensity. See [verification](../verification/README.md) for finite tests of the state and parity formulas.
