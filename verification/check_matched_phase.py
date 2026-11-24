"""Finite checks for the two matched Lévy phase laws on a herald stream."""

from itertools import product
from math import exp, log2

import numpy as np
from scipy.integrate import quad
from scipy.special import xlogy


def state(gaps, kappa, jump_arm):
    words = np.array(list(product((0, 1), repeat=len(gaps) + 1)))
    differences = words[:, None] - words[None, :]
    neutral = differences.sum(axis=-1) == 0
    charges = np.cumsum(differences[..., ::-1], axis=-1)[..., -2::-1]
    variance = kappa**4 if jump_arm else kappa + kappa**4
    exponents = -variance * charges**2 / 2
    if jump_arm:
        exponents -= (kappa / 2) * (charges % 2)
    return neutral * np.exp(exponents @ gaps) / len(words)


def entropy(sigma):
    eigenvalues = np.linalg.eigvalsh(sigma)
    assert min(eigenvalues) > -2e-15
    eigenvalues = np.maximum(eigenvalues, 0)
    return -np.sum(xlogy(eigenvalues, eigenvalues)) / np.log(2)


for time_gaps in (np.array([0.25, 0.65, 0.7]), np.array([1.0, 1500.0, 1.0])):
    for size in range(1, 4):
        gaps = time_gaps[: size - 1]
        np.testing.assert_allclose(state(gaps, 0.01, False), state(gaps, 0.01, True), atol=2e-16)
    arm_a = state(time_gaps, 0.01, False)
    arm_b = state(time_gaps, 0.01, True)
    delta = arm_b - arm_a
    assert set(map(tuple, np.argwhere(abs(delta) > 2e-16))) == {(3, 12), (12, 3)}
    outer_left, middle, outer_right = time_gaps
    kappa = 0.01
    visibility_b = exp(-(kappa + kappa**4) * (outer_left + outer_right) / 2 - 2 * kappa**4 * middle)
    visibility_a = visibility_b * exp(-2 * kappa * middle)
    helstrom = 0.5 + np.abs(np.linalg.eigvalsh(delta)).sum() / 4
    np.testing.assert_allclose(helstrom, 0.5 + (visibility_b - visibility_a) / 32)

scores = (4 - entropy(arm_a), 4 - entropy(arm_b))
np.testing.assert_allclose(scores, (0.974842246305347, 1.094174991084831), atol=2e-14)


def parity_rate(intensity, kappa):
    def integrand(gap_at_unit_intensity):
        probability = -np.expm1(-kappa * gap_at_unit_intensity / (2 * intensity)) / 2
        entropy_bit = -(xlogy(probability, probability)
                        + xlogy(1 - probability, 1 - probability)) / np.log(2)
        return exp(-gap_at_unit_intensity) * entropy_bit

    return intensity * quad(integrand, 0, np.inf, epsabs=1e-16)[0]


ratios = []
for kappa in (1e-3, 1e-6, 1e-9):
    leading_term = (kappa / 4) * log2(1 / kappa)
    ratios.append(parity_rate(1, kappa) / leading_term)
assert 1 < ratios[-1] < ratios[-2] < ratios[0]
assert abs(ratios[-1] - 1) < 0.1
print(f"Matched through three heralds; four-herald scores {scores[0]:.10f} and {scores[1]:.10f}.")
print(f"Parity-rate ratios to the leading term: {', '.join(f'{x:.6f}' for x in ratios)}.")
