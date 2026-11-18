# Reproduce the numerical checks

Run from the repository root with Python 3.10 or later and NumPy installed.

```sh
python3 verification/check.py
```

The script constructs the two- and three-herald density matrices in the original physical basis by summing over the genuine and false clicks and averaging the Brownian phases. It checks the branch weights and Bell fidelities after excitation-count projection and filtering, including the dephased three-link example with both false-click products. The two-herald negativity comes from diagonalizing the partial transpose. Checks also cover the sign change under two types of false clicks and the equality between the connected three-herald yield and the conditional mutual information of the clean block.

The sparse-rate checks use Gauss–Legendre quadrature in a squared gap coordinate. For the one-dimensional integral the numerical estimate agrees with the analytical coefficient. For the connected three-herald integral and gap moment the script checks agreement between truncating dimensionless gaps at 14 and 24. This is a numerical consistency check on the coefficients and does not bound the quadrature tails or replace the analytical derivations.
