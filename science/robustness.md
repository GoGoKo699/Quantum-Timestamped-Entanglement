# Storage, false heralds and imperfect controls

Consider three herald times $`t_1\lt t_2\lt t_3`$ supplied to the [three-herald receiver](receiver.md). The source has first-harmonic phase correlation $`e^{-D(t_j-t_i)}`$. Conditional on its phase, each herald independently supplies the genuine single-excitation link with probability $`q`$, the product state $`\lvert 00\rangle`$ with probability $`\alpha`$, or the product state $`\lvert 11\rangle`$ with probability $`\beta`$. These probabilities sum to one and are independent of the timestamps and the phase. Including both product states models two distinct ways a click can fail to signal a genuine link. Transduction simulations include both of these error products and compare the EPL and Chi–Kim–Lee distillation circuits. [Dirnegger et al., §2.2 and appendices C–D](https://arxiv.org/html/2503.10842v1)

## Storage until a declared time

The raw memories undergo independent pure dephasing. A qubit at endpoint $`X`$ has its computational-basis off-diagonal entries multiplied by $`e^{-\gamma_X a}`$ after storage for time $`a`$. The two endpoints may have different rates. Write $`\Gamma=\gamma_A+\gamma_B`$, and let $`T\ge t_3`$ be the time at which the local receiver begins. The phase-clock time for a raw coherence between positions $`i\lt j`$ is $`t_j-t_i`$. Both raw links carry the coherence during their respective storage periods. Its visibility at the receiver is therefore

```math
v_{ij}
= e^{-D(t_j-t_i)}
  e^{-\Gamma[(T-t_i)+(T-t_j)]}.
```

For example, the weight-one codeword with its excitation at $`i`$ differs from the weight-one codeword with its excitation at $`j`$ in exactly those two raw link positions. The same holds for the weight-two codewords labeled by their holes. The optical phase factor in that matrix entry is $`e^{i[\phi(t_i)-\phi(t_j)]}`$ or its conjugate. Local pure dephasing multiplies this entry by both raw-memory factors and preserves its diagonal and total weight.

The reference receiver acts instantaneously at $`T`$. Any subsequent idle time $`\ell`$ in independent logical phase memories multiplies all good output visibilities by $`e^{-\Gamma_L\ell}`$, where $`\Gamma_L`$ is the sum of the two logical phase damping rates. Correlated storage errors, leakage, relaxation, and imperfect operations can instead be included in the instrument error below, measured relative to the stipulated dephasing and idle-time model.

## Exact finite-block success and fidelity with both false states

Measure the local weights nondestructively and exchange their values. In the $`(1,2)`$ and $`(2,1)`$ sectors, use the logical excitation or hole labels to identify the three levels. Alice announces her two-level filter outcome. Bob projects onto those same two levels and announces success. Decode to a common $`\lvert\Phi^+\rangle=(\lvert00\rangle+\lvert11\rangle)/\sqrt 2`$ convention. The Bob projection is automatic on the all-genuine component and defines a success condition for false inputs. In the $`(1,1)`$ sector, pick a fixed dyad from the timestamps before looking at the positions. Each endpoint tests whether its excitation lies in that dyad and decodes with complementary labels on success. A convenient choice is a dyad with largest $`v_{ij}`$ under the declared storage contract.

| Successful sector | Input composition | Accepted probability |
| --- | --- | ---: |
| Weight pair $`(1,2)`$ or $`(2,1)`$ | Three genuine links | $`3q^3/4`$ |
| Weight pair $`(1,2)`$ or $`(2,1)`$ | One genuine link, one $`00`$ and one $`11`$ | $`3q\alpha\beta`$ |
| Weight pair $`(1,1)`$ | The selected dyad is genuine and the third link is $`00`$ | $`q^2\alpha/2`$ |
| Weight pair $`(1,1)`$ | The selected dyad contains the sole $`11`$ link and both other links are $`00`$ | $`2\beta\alpha^2`$ |

For the second row, the total weight is three. Measuring the two local weights resolves the single genuine link's orientation. The resulting Alice and Bob labels differ, so one of the three announced subsets contains both labels and has probability $`1/2`$ under Alice's filter. There are six orderings of the three raw link types. In the fourth row, the endpoints' excitations occupy the same raw position, so their complementary decoding produces different logical bits. Both false rows therefore contribute zero weight to the Bell projector. The first row retains three equally likely two-level outcomes, with fidelities $`(1+v_{ij})/2`$ for $`i\lt j`$. The selected genuine dyad contributes its visibility $`v_*`$ in the third row.

Let $`P`$ denote total success probability before applying instrument errors and let $`J`$ denote the unnormalized Bell overlap, so ideal conditional fidelity is $`F=J/P`$. With $`\bar v=(v_{12}+v_{13}+v_{23})/3`$,

```math
\begin{aligned}
P &= (q^2+4\alpha\beta)\left(\frac{3q}{4}+\frac{\alpha}{2}\right),\\
J &= \frac{3q^3}{4}\frac{1+\bar v}{2}
     +\frac{q^2\alpha}{2}\frac{1+v_*}{2}.
\end{aligned}
```

In the ideal operation model, each accepted sector and filter outcome has the same fraction $`q^2/(q^2+4\alpha\beta)`$ of its weight in the corresponding genuine branch. For a filter outcome indexed by $`i,j`$, the conditional fidelity is that fraction times $`(1+v_{ij})/2`$. For the selected dyad sector it is the same fraction times $`(1+v_*)/2`$. These per-outcome formulas and $`J/P`$ distinguish a fidelity floor for every accepted record from a fidelity guarantee averaged over successful records.

## Benchmark with earlier processing and ideal two-link storage

Allow the two-input receiver to choose its dyad using all three timestamps and to process its selected first input before the second arrives. Give it ideal storage, including storage of its decoded Bell output to the declared delivery time. This choice only strengthens the benchmark. The ideal raw two-link joint state can be supplied together to simulate any temporal local operations and classical communication on those two links, as long as the operations do not affect the source or use the discarded link. A timestamp-selected dyad at separation $`\Delta`$ has optical visibility $`w=e^{-D\Delta}`$.

The two-link state has a single potentially negative partial-transpose eigenvalue $`\alpha\beta-q^2w/4`$. In the joint local-weight $`(1,1)`$ sector the off-diagonal genuine term is $`q^2w/4`$. After partial transposition it couples the two false-product basis vectors, each of diagonal weight $`\alpha\beta`$. The other blocks remain positive. Thus the input negativity is $`[q^2w/4-\alpha\beta]_+`$, where $`[z]_+=\max(z,0)`$. In particular, the usual nonzero dyad negativity threshold is $`q^2w>4\alpha\beta`$.

Negativity cannot increase on average under local operations and classical communication. A two-qubit output of Bell overlap $`F_*>1/2`$ has negativity at least $`F_*-1/2`$. This follows from the partial transpose of the Bell projector, whose operator norm is $`1/2`$. [Vidal and Werner, Proposition 3](https://arxiv.org/abs/quant-ph/0102117)

Apply these facts to the accepted ensemble, including any separable outputs a receiver might add to increase acceptance. For $`w_{\max}=e^{-D\min(t_2-t_1,t_3-t_2)}`$, the probability of a dyad receiver's success obeys

```math
P_{\mathrm{two}}
\le \min\left\{1,\,
\frac{[q^2 w_{\max}/4-\alpha\beta]_+}{F_*-1/2}
\right\}.
```

This is a comparison on the same offered three timestamps with a receiver restricted to consuming one selected dyad. A receiver that measures a third raw link as a phase pilot belongs to a different class. The [stream theorem](stream.md) separately includes arbitrary collective operations in the ideal sparse-rate model.

## A certified noisy operating region

Model the complete local receiver, classical coordination, accept flag, and final corrected two-qubit output as a trace-preserving instrument with a dummy output on failure. Let its half diamond distance from the reference instrument at the declared delivery time be at most $`\delta`$. This compares the full instrument, including branch probabilities and the states those branches produce. A sequence with component bounds $`\delta_k`$ has a valid total bound $`\sum_k\delta_k`$ by telescoping and trace-norm contractivity. A measurement confusion rate alone only controls classical branch labels.

The actual success probability $`P'`$ satisfies $`P'\ge P-\delta`$. For a desired average accepted fidelity $`F_*`$, the ideal observable for the fidelity margin is the accept projector tensored with $`\Phi^+-F_*I`$, where $`\Phi^+`$ denotes the Bell projector. Its spectral range is contained in $`[-F_*,1-F_*]`$, of width one. The change in its expectation is therefore at most $`\delta`$ by the instrument bound. If $`P>\delta`$ and $`J-F_*P\ge\delta`$, the actual accepted fidelity is at least $`F_*`$. In particular,

```math
F' \ge \max\left\{0,\frac{J-\delta}{P}\right\}.
```

As an example, set $`q=0.8`$, $`\alpha=0.198`$, $`\beta=0.002`$, both dimensionless consecutive gaps equal to $`0.05`$, and $`D(T-t_3)=0.01`$. Let $`\Gamma=0.1D`$, $`\ell=0`$ and $`\delta=0.002`$. The three raw-storage-adjusted visibilities are about $`0.93520`$, $`0.89404`$, and $`0.94459`$ in the order $`12,13,23`$. The formula gives $`P=0.448467`$ and $`J/P=0.961341`$. After the full instrument disturbance, $`P'\ge0.446467`$ and $`F'\ge0.956881`$. At $`F_*=0.95`$, the ideal-memory two-input receiver has $`P_{\mathrm{two}}\le0.337335`$. All decisive inequalities are strict, so the gain holds on an open neighborhood with positive rates for both false outcomes, memory dephasing and control error. The parameters in this example specify an instrument and source contract.

The same disturbance argument applies to each declared successful record if the instrument bound includes these records in its classical output. The ideal probability of each of the six qutrit filter records is $`(q^2+4\alpha\beta)q/8`$ and that of the successful $`(1,1)`$ record is $`(q^2+4\alpha\beta)\alpha/2`$. Replace $`J`$ and $`P`$ by the corresponding record's overlap and probability. With the above rates and errors, but consecutive dimensionless gaps $`0.01`$, this gives fidelity at least $`0.9545`$ for every successful record. The total success bound is unchanged, and the ideal-memory dyad probability is at most $`0.3512`$ at fidelity $`0.95`$.

## Counting wall-clock time

One bounded-latency implementation opens fixed admission windows of length $`W`$ and reserves time $`L`$ after each window for local processing and classical messages. It supplies a single finite-receiver attempt only in windows containing exactly three arrivals. It charges every window and the full $`W+L`$ interval, including windows whose heralds are discarded. Within a window, the raw memories are held until closing. If $`T`$ is the closing time and rates are uniform, each visibility is at least

```math
v_{\mathrm{floor}}=\exp[-W\max(2\Gamma,D+\Gamma)].
```

Indeed, maximize $`D(t_j-t_i)+\Gamma(2T-t_i-t_j)`$ over ordered times in the window. The extrema place both at the opening time or one at each endpoint. Any specified logical idle attenuation multiplies this visibility floor, and remaining time-dependent imperfections enter $`\delta`$. Substituting the floor for both visibilities in $`J`$ certifies a uniform fidelity target if the margin condition still holds.

For exogenous Poisson heralds of rate $`\lambda`$ the expected number of accepted outputs per unit wall time is bounded below by

```math
\frac{e^{-\lambda W}(\lambda W)^3}{6(W+L)}(P-\delta).
```

For example, with the same source proportions, $`\Gamma=0.1D`$ and no additional stipulated logical idle attenuation, $`DW=0.075`$ gives $`v_{\mathrm{floor}}\ge0.92081`$. A total instrument bound $`\delta=0.002`$ through delivery certifies average accepted fidelity at least $`0.95357`$ for every admitted window, with the instrument duration charged in $`L`$.

This finite-clock construction uses at most three simultaneously stored raw links per endpoint. Its delivered Bell-pair count at specified fidelity is distinct from the asymptotic ebit rate after hashing. The numerical comparison on a fixed triple controls that triple's success probability, and the wall-clock formula charges one particular admission schedule.
