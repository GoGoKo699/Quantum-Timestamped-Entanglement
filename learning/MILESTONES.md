# Quantum Timestamped Entanglement in 30 milestones

Follow one link from the first detector click to the optimal rate of an entire stream. M01–M12 assemble the physical and information-theoretic tools. M13–M30 use those tools to decode a three-herald block, compare it with any selected two-input receiver, and explain which parts of that gain persist in a sparse stream.

Chapter and section numbers refer to Wilde's *Quantum Information Theory*, second edition (2017). The [Wilde bridge](WILDE_BRIDGE.md) connects the textbook notation to the research model. The [scientific account](../science/README.md) collects the full derivations.

## Background and preliminaries

### M01 Read a herald

*What does a detector click tell the receiving nodes?*

Distinguish an observed herald from the hidden label that says whether it is genuine. Identify which inputs come with a time and a known detector sign, and count rejected attempts when measuring success per offered triple. This fixes the resources for every later comparison. [Source and timing](../science/model.md)

### M02 Write the raw link state

*How can a single excitation be shared by two nodes?*

Starting from M01, write the two terms $`\lvert01\rangle`$ and $`\lvert10\rangle`$ of one genuine link and identify the relative phase between them. Separate the known sign correction from the unobserved path phase, and recognize a Bell fidelity as an overlap with a declared target state. Wilde §§3.2, 3.5–3.6 and 9.2. [Receiver inputs and output](../science/receiver.md#input-and-output)

### M03 Average over the unknown phase

*What survives when the optical phase of one link is uniformly unknown?*

Use the state in M02 to form its density matrix and average the two off-diagonal terms over one full circle. Read the resulting mixture as equal probabilities for two product states. This explains why a single herald averaged over its phase has no distillable entanglement. Wilde §§4.1 and 4.3. [Phase and false heralds](../science/model.md#false-heralds)

### M04 Measure time in phase-coherence units

*What remains predictable about two phases when each phase is individually uniform?*

Build on M03 by separating the absolute phase from the increment across a known time gap. Interpret $`e^{-D\lvert t_j-t_i\rvert}`$ as the coherence left in a first-harmonic relative-phase term. Use the independent increments to multiply visibilities across consecutive gaps. [Wrapped Brownian model](../science/model.md)

### M05 Measure a count without locating the excitation

*Which superpositions are preserved by a local excitation-count measurement?*

From M02 and M04, group local bit strings by excitation count. Explain why the count projection keeps the coherence between $`\lvert100\rangle`$ and $`\lvert010\rangle`$ and what extra information a position readout would expose. This is the operation that lets the receiver use relative phase. Wilde §§3.4, 4.2 and 5.4. [Count circuit](../science/receiver.md#protocol)

### M06 Keep the measurement record with its quantum output

*How does a measurement branch describe both acceptance and the delivered state?*

Starting from M05, read $`K\rho K^\dagger`$ as an unnormalized branch, its trace as branch probability, and the normalized operator as the conditional state. Connect the sum of the effects $`K^\dagger K`$ to a complete instrument, so that a fidelity target and a probability of meeting it can be tracked separately. Wilde §§4.2, 4.4 and 5.3. [Finite receiver protocol](../science/receiver.md#protocol)

### M07 Declare what the receiver may use

*Which actions count as local operations and classical communication?*

Using M01 and M06, assign the stored qubits to the two endpoints and identify which records they can exchange. Explain why a comparison against any such two-input receiver must give it the same timestamps and permit classical adaptation within its selected pair. Wilde §19.1. [Finite receiver comparison](../science/model.md#finite-receiver-comparison)

### M08 Bound entanglement with partial transpose

*How can the input state limit the success of an arbitrary local receiver?*

Build on M07 by taking the transpose on one node's indices and identifying the sum of the absolute values of the negative eigenvalues as negativity. Relate that quantity to Bell fidelity and account for every instrument outcome when applying its average monotonicity. Wilde §19.1 supplies the local-operation context. [Negativity benchmark](../science/receiver.md#best-two-retained-inputs-at-matched-fidelity)

### M09 Read an entropy from a state

*What do a joint spectrum and a local marginal each contribute to an entanglement rate?*

Use the mixed state of M03 and the count sectors of M05 to distinguish global entropy from the entropy of either endpoint alone. When the local marginal is maximally mixed, relate coherent information to the difference between the log of its dimension and the joint entropy. Wilde §§11.1–11.2 and 11.4–11.5. [Clean stream as an entropy rate](../science/stream.md#clean-stream-as-an-entropy-rate)

### M10 Use an output test to bound what came before

*Why can a simple Bell test constrain every decoder in a rate proof?*

Combine M07–M09 by comparing the actual source and a separable source under the same receiver and the same pass/fail test. Identify relative-entropy data processing as the reason that distinguishability after the test bounds how much distinguishability was present at the input. Wilde §§11.8–11.9 and 19.2. [Clean stream converse](../science/stream.md#clean-stream-as-an-entropy-rate)

### M11 Read conditional mutual information across an interval

*How do we describe correlations between the two ends with the middle as quantum side information?*

Extend M09 to conditional entropy and conditional mutual information. Use strong subadditivity to explain its nonnegativity. Connect the entropy continuity bound to changing the state by a small trace distance while assessing a two-dimensional endpoint. Wilde §§9.1, 11.4, 11.7 and 11.9–11.10. [Contiguous intervals](../science/stream.md#contiguous-intervals-resolve-the-sparse-expansion)

### M12 Assemble the two receiver questions

*What changes when the three given timestamps become an entire sequence of random arrivals?*

Join M04 and M07–M11. State the finite task as success per offered triple at a Bell fidelity target. State the stream task as delivered ebits per elapsed time with vanishing unconditional error. Use the Poisson rate $`\lambda`$ and phase-decay rate $`D`$ to form the dimensionless ratio $`\lambda/D`$, and explain why the long observation limit comes first. [Source, timing and tasks](../science/model.md)

## Narrative and innovation

### M13 Find the coherence that survives count selection

*Why can several singly averaged links still be useful together?*

Apply M03–M05 to two alternatives with the same local excitation count. Compare their phase factors and explain how the unknown collective phase cancels while the phase difference between their time slots remains. The receiver exploits that difference. [Receiver protocol](../science/receiver.md#protocol)

### M14 Label the three-dimensional sectors

*How do the two endpoints agree on a label for the retained three-link state?*

Use M13 to identify a single excitation at one endpoint with the single vacancy at the other. Recover the three-dimensional correlated matrix by assigning the two adjacent visibilities $`a,b`$ and the outer-slot visibility $`ab`$ to the appropriate entries. [Exact success and fidelity](../science/receiver.md#exact-success-and-fidelity)

### M15 Turn a logical qutrit into one logical Bell pair

*How can the nodes retain two slots without finding out which slot is occupied?*

Apply the instrument idea from M06 to the state from M14. Explain why three two-position projectors, each scaled by $`1/\sqrt2`$, form a complete instrument. After its public outcome, identify the two logical basis states and the Bell overlap $`(1+v_{ij})/2`$. [Two-position filter](../science/receiver.md#protocol)

### M16 Calculate acceptance under one false-herald type

*Which triples can still deliver an output when one click might be false?*

With M13–M15, account for genuine triples in sectors $`(1,2)`$ and $`(2,1)`$, and two genuine links plus one hidden $`\lvert00\rangle`$ in the selected $`(1,1)`$ branch. Combine their weights into $`P_3=q^2/2+q^3/4`$, and explain why using the closest two slots in the fallback protects its fidelity. [One-sided acceptance rules](../science/receiver.md#exact-success-and-fidelity)

### M17 Bound every timestamp-selected dyad

*How much can an arbitrary two-input local receiver improve on its starting state?*

Use M08 and M16 to isolate the dyad's entangled $`(1,1)`$ block. Its probability is $`q^2/2`$ and its normalized negativity is $`v/2`$. Multiply them to obtain $`P(F-1/2)\le q^2v/4`$ for any accepted dyad output at $`F>1/2`$. [Best two retained inputs](../science/receiver.md#best-two-retained-inputs-at-matched-fidelity)

### M18 Compare both receivers on one offered triple

*What does the third input buy at the same fidelity target?*

Use M15–M17 with genuine probability $`q=0.8`$ and both dimensionless gaps equal to $`0.05`$. Trace the $`95.24\%`$ target to the furthest pair of slots, the $`44.8\%`$ success to the three-input branches, and the approximate $`33.64\%`$ ceiling to the closest dyad's negativity. The example compares receivers at fixed timestamps. [Worked finite comparison](../science/receiver.md#best-two-retained-inputs-at-matched-fidelity)

### M19 Charge raw-memory time to coherence

*Why can the oldest input cost fidelity even if the two selected clicks are close?*

Take the two-slot coherence from M15 and account for its loss in both stored raw links. Explain why the visibility depends on the elapsed time to decoding at each slot as well as the optical gap between them. Use the dephasing factor to compare timestamp selection under storage loss and under ideal storage. [Storage until a declared time](../science/robustness.md#storage-until-a-declared-time)

### M20 Verify a noisy advantage at a fidelity threshold

*How can a third link still help when the receiver itself is imperfect?*

Build on M17–M19 by tracking both false-click products $`\lvert00\rangle`$ and $`\lvert11\rangle`$. Identify receiver branches that pass the flags but are orthogonal to the target. Apply the success bound $`P-\delta`$ and explain how the Bell-overlap condition $`J-F_*P\ge\delta`$ certifies the fidelity target under a half-diamond instrument error $`\delta`$. Reproduce the $`44.64\%`$ lower bound at $`95\%`$ target fidelity and compare it with the ideal-memory two-input ceiling of $`33.74\%`$ in the declared example. Wilde §§9.1–9.3 supply the trace-distance context. [Certified noisy operating region](../science/robustness.md#a-certified-noisy-operating-region)

### M21 Pay for empty windows and decoding

*When does a per-triple advantage translate into a count of delivered pairs per time?*

Use M12 and M18–M20 to explain how exactly-three Poisson arrivals in a fixed admission window and its processing time enter the finite-clock guarantee. Identify the visibility floor for any triple in the window. This completes the finite receiver and prepares the move to a stream optimum. [Counting wall-clock time](../science/robustness.md#counting-wall-clock-time)

### M22 Compress the description of a clean block

*Why can a block of bipartite links be represented by one auxiliary phase-state matrix?*

Apply M09 and M13 to a block after Bob flips each raw bit. Identify the matching basis labels on the two endpoints and use the map $`\lvert x\rangle\mapsto\lvert x,x\rangle`$ to preserve the spectrum. With uniform diagonal and endpoint marginal, read the entropy score as $`n-S(\sigma)`$. Wilde §§11.1–11.2 and 11.4–11.5. [Clean stream as an entropy rate](../science/stream.md#clean-stream-as-an-entropy-rate)

### M23 Bound the entire clean stream from above

*Why does the clean-block entropy score limit even collective timestamp-aware decoding?*

Apply M10 to the block in M22. Choose its diagonal separable state as the comparison input. An $`m`$-ebit test can pass there with probability at most $`2^{-m}`$, so data processing turns the relative entropy to this comparison state into an upper bound on reliable output size. Wilde §§11.8–11.9, 19.2 and 24.9. [Clean stream converse](../science/stream.md#clean-stream-as-an-entropy-rate)

### M24 Attain the clean block score by hashing

*How can hashing use correlated arrivals without assuming that the raw links are independent?*

Build on M04, M09 and M22–M23 by twirling the local total excitation phase separately in each fixed-time block. Explain why only within-block increments remain and how finite bins of timestamp configurations produce repeated states for one-way hashing. Link the resulting achievable score to the converse and the long-time limit. Wilde §§11.5 and 24.9. [Clean stream achievability](../science/stream.md#clean-stream-as-an-entropy-rate)

### M25 Resolve the score into contiguous intervals

*Which entropy contributions belong to dyads, triplets and longer intervals?*

Use M11 and M22–M24 to subtract adjoining subinterval scores. The difference is the conditional mutual information of the endpoints given the middle, and summing it telescopes to the clean block score. For the stream, associate each interval size with an expectation over its dimensionless Poisson gaps. Wilde §§11.7 and 11.9. [Contiguous interval expansion](../science/stream.md#contiguous-intervals-resolve-the-sparse-expansion)

### M26 Control the contribution of long intervals

*Why can the sparse expansion stop after the first few cluster sizes?*

Combine M04, M11 and M25. Reset the phase across the largest gap to split the record into independent parts. Brownian phase mixing bounds the trace-distance change, and continuity for the two-dimensional endpoint bounds the resulting conditional mutual information uniformly in the interval length. Relate the largest-gap law to the order of the summed remainder. Wilde §§9.1 and 11.10. [Sparse expansion tail](../science/stream.md#contiguous-intervals-resolve-the-sparse-expansion)

### M27 Derive the leading sparse rate from dyads

*Why does the leading useful rate count two nearby genuine clicks?*

Use M16, M25 and M26 to read the dyad yield $`Y_2`$ as the weight-one acceptance probability times its coherent information. Integrate this yield over the rescaled Poisson gap to obtain $`C\simeq0.20336`$. With fixed one-sided false-herald probability $`1-q`$, explain how the true-click genie bounds the rate from above and odd-weight filtering supplies the matching factor $`q^2`$ from below. [Two-click yield](../science/stream.md#two-and-three-clicks) · [One-sided false heralds](../science/stream.md#one-sided-false-heralds)

### M28 Locate the first clean three-click correction

*What does the third click contribute beyond the two shorter intervals?*

Use the qutrit in M14 and the interval expansion in M25–M27. Compute the triplet's weighted entropy deficit $`Y_3`$, then remove the two adjacent dyad contributions to obtain $`G_3`$. Identify the positive integral of $`G_3`$ and the negative gap-density correction that together give the clean coefficient $`C_2`$. [Two- and three-click coefficients](../science/stream.md#two-and-three-clicks)

### M29 Match the clean expansion with three raw memories

*Which processing schedule recovers the first two terms as the stream becomes sparse?*

Use M24 and M26–M28 to follow the short-gap cluster rule through one, two, three and at least four arrivals. Explain why three raw memories per endpoint suffice for the front end, why preserving the full qutrit sectors is useful for hashing, and how the ideal rate still requires downstream block storage. Identify the additive dyad score as a separate benchmark within the clean-stream analysis. [Three raw memories](../science/stream.md#three-raw-memories-attain-both-clean-coefficients) · [Best additive dyad score](../science/stream.md#best-additive-dyad-score)

### M30 State what triplets add across both tasks

*Where does the third herald change the receiver's capability, and what assumptions decide whether to use it?*

Bring M18–M21 and M27–M29 together. Explain the finite reliability gain at fixed timestamps, the leading optimal stream rate supplied by dyads, and the clean next-order rate recovered by the triplet receiver. Keep the finite noise guarantee, ideal stream assumptions, time accounting and downstream memory requirements visible when comparing these results. [Scientific account](../science/README.md) · [Verification](../verification/README.md)
