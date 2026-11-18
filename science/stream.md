# Distillable entanglement of a timestamped stream

The source reports a Poisson stream of raw links of rate $`\lambda`$. Each reported link is a genuine single-excitation pair with probability $`q`$, independently of the other links and of the optical phase. Given the phase $`\phi(t)`$ at its timestamp $`t`$, a genuine link is $`(|01\rangle+e^{i\phi(t)}|10\rangle)/\sqrt{2}`$. Each false link is the same product $`|00\rangle`$. The phase is stationary Brownian motion on the circle with first harmonic $`\mathbb E[e^{i(\phi(t+u)-\phi(t))}]=e^{-Du}`$ and $`D>0`$.

The endpoints know the timestamps and source parameters. They can store their local shares, send classical messages, and perform ideal local quantum operations. The rate $`R_q(\lambda,D)`$ is the supremum of ebits per unit time obtained with a fixed output size per observing interval and unconditional error tending to zero. All heralds count, including misses of the eventual receiver filter. The limit in observing time is taken before the sparse limit $`\varepsilon=\lambda/D\to0`$. The rate benchmark allows unrestricted memory for outer distillation.

## Rate law

For each fixed $`0<q\le1`$,

```math
R_q(\lambda,D)
=Cq^2\frac{\lambda^2}{D}+o\!\left(\frac{\lambda^2}{D}\right),
\qquad
C=\frac{\ln 2-\pi^2/24}{2\ln 2}\simeq0.2033577224.
```

The leading coefficient is optimal over all timestamp-aware local operations and classical communication (LOCC). A finite buffer that retains consecutive short-gap dyads, followed by outer hashing, attains it. For a clean stream the next coefficient is also explicit,

```math
R_1(\lambda,D)
=\lambda\big[C\varepsilon+C_2\varepsilon^2+O(\varepsilon^3)\big].
```

The coefficient $`C_2`$ contains a three-herald term from conditioning on the middle link. A receiver that holds up to three raw shares per endpoint, preserves the three-level sectors of short triplets, and then hashes attains the expansion through order $`\lambda\varepsilon^2`$.

## Clean stream as an entropy rate

Given timestamps $`t_1<\dots<t_n`$, define a state on $`n`$ auxiliary qubits by

```math
\sigma(t_1,\ldots,t_n)=
\mathbb E_\phi\!\left[\bigotimes_{i=1}^n |+_{\phi(t_i)}\rangle\!\langle +_{\phi(t_i)}|\right],
\qquad
|+_\phi\rangle=\frac{|0\rangle+e^{i\phi}|1\rangle}{\sqrt 2}.
```

A bit flip on each of Bob's physical qubits maps the source to the maximally correlated state $`\rho=V\sigma V^\dagger`$ with $`V|x\rangle=|x\rangle_A|x\rangle_B`$. Its entropy is $`S(\sigma)`$, and the diagonal and each endpoint marginal are uniform. All entropies below are in bits. The entropy score is

```math
Y(t_1,\ldots,t_n)=n-S\big(\sigma(t_1,\ldots,t_n)\big).
```

It takes values in $`[0,n]`$. For an empty or singleton block it is zero. The separable comparator $`2^{-n}\sum_x|x,x\rangle\!\langle x,x|`$ has relative entropy distance $`Y`$ from $`\rho`$. Run an arbitrary timestamp-conditioned LOCC protocol on both states and test the output for $`m`$ ebits. The comparator passes with probability at most $`2^{-m}`$. If the actual output passes with probability $`F`$, monotonicity of relative entropy under the resulting binary measurement gives $`Y\ge Fm-h_2(F)\ge Fm-1`$. Averaging over timestamps bounds the rate of any such protocol by the entropy score per observing time.

For attainment, divide time into fixed blocks of duration $`T`$. Independently twirl Alice's total excitation phase in each block. A block state then depends only on its internal phase increments, and the blocks are independent after conditioning on their timestamps. For each fixed $`T`$, discard blocks with more than $`n_{\max}`$ arrivals and group the others into finitely many bins of timestamp vectors. Averaged states within a bin have the same uniform local marginal, and their joint entropy converges to the timestamp-conditioned entropy as bin precision increases. This follows from finite-dimensional entropy continuity and continuity of $`\sigma`$ in the timestamps on the fixed block. One-way hashing in each populated bin attains its coherent information. Bin frequencies converge to their probabilities, so allowing fine bins and then taking $`n_{\max}`$ large recovers $`\mathbb E Y/T`$. [Devetak and Winter, *Distillation of secret key and entanglement from quantum states*](https://arxiv.org/abs/quant-ph/0306078)

The mean score over adjacent time blocks is superadditive by entropy subadditivity on $`\sigma`$ and stationarity. It is bounded above by $`\lambda T`$. Tiling a long interval with fixed blocks shows that its asymptotic rate equals the supremum over block lengths. In combination with the converse,

```math
R_1(\lambda,D)
=\lim_{T\to\infty}\frac{\mathbb E\big[N_T-S(\sigma_T)\big]}{T}
=\sup_{T>0}\frac{\mathbb E\big[N_T-S(\sigma_T)\big]}{T}.
```

Here $`N_T`$ and $`\sigma_T`$ refer to the record in the observing interval $`[0,T]`$. This identity permits collective distillation with arbitrarily many clicks.

## Contiguous intervals resolve the sparse expansion

For the auxiliary-qubit interval $`[i,j]`$ write $`Y_{i:j}=(j-i+1)-S(\sigma_{i:j})`$. The marginal $`\sigma_{i:j}`$ is the phase-state matrix for the corresponding timestamps. For two or more consecutive clicks let

```math
G_{i:j}=Y_{i:j}-Y_{i+1:j}-Y_{i:j-1}+Y_{i+1:j-1}
=I(Q_i:Q_j\mid Q_{i+1},\ldots,Q_{j-1})_\sigma\ge0.
```

Strong subadditivity gives the sign. Summing over $`i<j`$ telescopes to $`Y_{1:n}`$ because the singleton and empty scores vanish. If the interval contains $`m`$ clicks, write its score as $`G_m(X_1,\ldots,X_{m-1})`$, where $`X_i`$ is the succeeding gap in units of $`D^{-1}`$.

After a Poisson arrival the future gaps $`X_i`$ are independent exponentials of rate $`\varepsilon`$. For an interval of duration $`T`$, the expected number per unit time of starting clicks that leave enough room for a gap tuple gets a factor $`(1-(X_1+\cdots+X_{m-1})/(DT))_+`$. Summing over lengths and taking $`T\to\infty`$ by monotone convergence gives the exact series

```math
R_1(\lambda,D)=
\lambda\sum_{m\ge2}\mathbb{E}_{\varepsilon}
\big[G_m(X_1,\ldots,X_{m-1})\big].
```

To bound the tail, choose the largest internal gap $`z=\max X_i`$. The wrapped Brownian transition has density

```math
k_z(\theta)=\frac{1}{2\pi}
\left(1+2\sum_{\ell\ge1}e^{-\ell^2z}\cos(\ell\theta)\right).
```

Replacing this transition by an independent uniform phase changes the law of the entire phase trajectory by total variation at most $`\sum_{\ell\ge1}e^{-\ell^2z}`$. It splits the phase-state matrix into independent left and right factors, for which the interval conditional mutual information vanishes. Contractivity under the classical-to-quantum preparation bounds the trace distance by the same total variation. Apply conditional entropy continuity to $`S(Q_i\mid Q_{i+1:j-1})`$ and $`S(Q_i\mid Q_{i+1:j})`$. Both bounds use only the dimension of $`Q_i`$, which is two. Consequently there is an absolute $`K`$ such that

```math
0\le G_m(X_1,\ldots,X_{m-1})\le K(1+z)e^{-z}
```

for every interval length. The bound for small $`z`$ follows from $`G_m\le2`$. [Winter, *Tight uniform continuity bounds for quantum entropies*, Lemma 2](https://arxiv.org/abs/1507.07775)

The largest of $`k`$ exponential gaps has density $`k\varepsilon e^{-\varepsilon z}(1-e^{-\varepsilon z})^{k-1}`$. Its sum over $`k\ge3`$ is bounded by $`3\varepsilon^3 z^2 e^{\varepsilon z}`$, from the geometric-series derivative and $`1-e^{-\varepsilon z}\le\varepsilon z`$. Multiplying by the uniform bound on $`G_m`$ and integrating yields

```math
\sum_{m\ge4}\mathbb E_\varepsilon G_m=O(\varepsilon^3)
\quad (0<\varepsilon\le1/2).
```

### Two and three clicks

Write $`h_2`$ for binary entropy. For two clicks at dimensionless gap $`x`$, the two one-dimensional excitation sectors are separable. The weight-one sector has probability $`1/2`$ and is a dephased Bell pair of visibility $`e^{-x}`$. Its contribution is

```math
G_2(x)=Y_2(x)=\tfrac12\left[1-h_2\left(\frac{1+e^{-x}}2\right)\right].
```

For three clicks with successive gaps $`x,y`$, the weight-one and weight-two sectors have combined probability $`3/4`$. They have the same entropy, with normalized phase-state matrix

```math
M_3(x,y)=\frac13\begin{pmatrix}
1 & e^{-x} & e^{-(x+y)}\\
e^{-x} & 1 & e^{-y}\\
e^{-(x+y)} & e^{-y} & 1
\end{pmatrix}.
```

For weight two, use the position of the missing excitation as the logical label. The extremal sectors are separable. Thus

```math
Y_3(x,y)=\frac34\big[\log_2 3-S(M_3(x,y))\big],
\qquad
G_3(x,y)=Y_3(x,y)-Y_2(x)-Y_2(y).
```

The score $`G_3`$ is nonnegative. For a triplet with both gaps finite, $`Y_3`$ strictly exceeds the yield of the better single dyad because both dyad scores are positive. This comparison concerns the ideal local weight receiver preserving its qutrit output for outer hashing. The separate finite-output protocol in [the receiver analysis](receiver.md) maps the qutrit to one heralded Bell qubit and uses a different fidelity-success criterion.

Taylor expanding the exponential gap densities, using the integrable bound and its finite moments, gives

```math
C=\int_0^\infty Y_2(x)\,dx,\qquad
C_2=\int_0^\infty\!\int_0^\infty G_3(x,y)\,dx\,dy
-\int_0^\infty xY_2(x)\,dx.
```

For the first integral, the binary entropy deficit has the positive series

```math
1-h_2\!\left(\frac{1+r}{2}\right)
=\frac{1}{\ln 2}\sum_{k\ge1}\frac{r^{2k}}{(2k)(2k-1)}.
```

At $`r=e^{-x}`$, integrate term by term. The summand after integration is proportional to $`1/(2k-1)-1/(2k)-1/(4k^2)`$, giving the stated $`C`$. Numerical quadrature gives $`C_2\approx-0.06025`$.

## Three raw memories attain both clean coefficients

Choose a gap cutoff $`L/D`$, where $`L=3\ln(1/\varepsilon)`$ in the sparse regime. A cluster consists of consecutive clicks connected by gaps at most $`L/D`$. At the timeout, process only clusters of size two or three. Discard singleton clusters. When a fourth click arrives before timeout, discard the cluster and ignore its subsequent clicks until a gap exceeds the cutoff. This uses three raw memories per endpoint because the timestamp of a fourth click suffices to tell the receiver to discard. A retained raw share waits at most $`3L/D`$ before local processing, with ideal local operations. Outer hashing requires additional block storage.

Measure local excitation weights without resolving positions. Preserve the weight-one qubit sector of a dyad and the weight-one and weight-two qutrit sectors of a triplet. The local weights erase dependence on the absolute optical phase. Retained clusters can be hashed independently in bins of gap tuples and sector labels. The within-cluster increments are independent across disjoint clusters, conditional on timestamps.

In stationarity a retained cluster has a gap larger than $`L`$ on each end. The mean score per time of this receiver is

```math
\lambda e^{-2\varepsilon L}
\left[
\varepsilon\int_0^L e^{-\varepsilon x}Y_2(x)\,dx+
\varepsilon^2\int_0^L\!\int_0^L
e^{-\varepsilon(x+y)}Y_3(x,y)\,dx\,dy
\right].
```

Insert $`Y_3(x,y)=Y_2(x)+Y_2(y)+G_3(x,y)`$. The truncated dyad integral then comes with factor $`e^{-2\varepsilon L}(3-2e^{-\varepsilon L})=1+O((\varepsilon L)^2)`$, since the triplet terms supply the two possible short dyads. The truncated $`G_3`$ term comes with factor $`e^{-2\varepsilon L}=1+O(\varepsilon L)`$. The uniform exponential bound on the complement of $`[0,L]^2`$, and the corresponding bound on $`Y_2`$, imply that the receiver attains the optimal clean rate up to $`o(\lambda\varepsilon^2)`$. This receiver implements the first correction without a buffer that grows in the number of raw shares per endpoint.

### Best additive dyad score

A comparison with flexible pairing is to maximize the sum of the standalone yields $`Y_2`$ over disjoint pairs selected using all the timestamps. This gives a benchmark for receivers evaluated by their individual dyad yields. The collective LOCC benchmark above also covers protocols that exploit correlations between processed outputs.

A dyad longer than $`L/D`$ can be removed at an expected cost per time at most $`\lambda\varepsilon\int_L^\infty Y_2(x)\,dx`$, summing over all unordered long pairs of arrivals. Surviving pairs stay inside the short-gap clusters. The expected number of clicks per time in clusters of size at least four is $`O(\lambda(\varepsilon L)^3)`$, because their internal gaps have probability $`1-e^{-\varepsilon L}`$. The remaining optimization has one possible dyad in each two-click cluster and selects the shorter adjacent gap in each three-click cluster. This rule is feasible and achieves its additive score by hashing the selected dyads in timestamp bins.

In the cluster rate formula, replacing $`Y_3(x,y)`$ by $`\max\{Y_2(x),Y_2(y)\}`$ therefore gives the optimal additive score up to $`o(\lambda\varepsilon^2)`$. Its rate deficit relative to the three-share receiver at this order is $`\lambda\varepsilon^2\Delta`$, with

```math
\Delta=\int_0^\infty\!\int_0^\infty
\big[Y_3(x,y)-\max\{Y_2(x),Y_2(y)\}\big]\,dx\,dy
=\int_0^\infty\!\int_0^\infty G_3(x,y)\,dx\,dy
+2\int_0^\infty xY_2(x)\,dx>0.
```

The equality uses $`\min\{Y_2(x),Y_2(y)\}=Y_2(\max\{x,y\})`$. The positive deficit is approximately $`0.22466\lambda^3/D^2`$ in the sparse limit.

## One-sided false heralds

For an upper bound, reveal every genuine-versus-false label to the endpoints. Discard the phase-independent product links and retain a thinned Poisson stream of rate $`q\lambda`$. Independently thinned-out heralds contribute classical randomness and local product ancillas, resources already allowed by LOCC. The clean-stream converse gives $`R_q(\lambda,D)\le R_1(q\lambda,D)`$.

To attain the leading order without those labels, retain two-click clusters and apply the local odd-weight checks. Only two genuine links can pass, and they pass together with probability $`q^2/2`$. Thus the achievable score is the two-click contribution above multiplied by $`q^2`$. With $`L\to\infty`$ and $`\varepsilon L\to0`$, its leading coefficient matches the upper bound. The proof of the second coefficient uses the clean source.

The dyad distillation step and its dephased-state yield are inherited from earlier work on remote entanglement. The stream result evaluates the timestamped source with a collective LOCC converse and identifies the first rate contribution of coherent three-click processing. [Rozpędek et al., *Optimizing practical entanglement distillation*, Sec. IV.D and Appendix H](https://doi.org/10.1103/PhysRevA.97.062333) · [Kalb et al., *Entanglement Distillation between Solid-State Quantum Network Nodes*](https://arxiv.org/abs/1703.03244) · [Lu et al., *Entanglement Model for Mode-Pairing Quantum Key Distribution*](https://arxiv.org/abs/2304.09621)
