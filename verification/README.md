# Reproduce the numerical checks

Run from the repository root with Python 3.10 or later. Install NumPy for both scripts and SciPy for the matched-clock check.

```sh
python3 verification/check.py
python3 verification/check_matched_phase.py
```

The script constructs the two- and three-herald density matrices in the original physical basis by summing over the genuine and false clicks and averaging the Brownian phases. It checks the branch weights and Bell fidelities after excitation-count projection and filtering, including the dephased three-link example with both false-click products. The two-herald negativity comes from diagonalizing the partial transpose. Checks also cover the sign change under two types of false clicks and the equality between the connected three-herald yield and the conditional mutual information of the clean block.

The sparse-rate checks use Gauss–Legendre quadrature in a squared gap coordinate. For the one-dimensional integral the numerical estimate agrees with the analytical coefficient. For the connected three-herald integral and gap moment the script checks agreement between truncating dimensionless gaps at 14 and 24. This is a numerical consistency check on the coefficients and does not bound the quadrature tails or replace the analytical derivations.

The matched-clock script checks equality of the complete clean source states up to three heralds, the four-herald coherence that gives the exact discrimination probability, and the jump-parity entropy integral. See the [proof](../science/matched-phase-diagnostics.md) for the long-record rate bounds.
