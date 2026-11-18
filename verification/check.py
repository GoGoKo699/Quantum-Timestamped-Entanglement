"""Finite receiver and sparse-stream diagnostics. Requires NumPy only."""

from itertools import combinations, product
from math import exp, log, log2, pi, prod, sqrt

import numpy as np
from numpy.polynomial.legendre import leggauss


def raw_state(gaps, genuine, false_one=0.0, storage=None):
    """Construct the full bipartite density matrix from click labels and phases."""
    clicks = len(gaps) + 1
    dim = 1 << clicks
    state = np.zeros((dim**2, dim**2))
    label_probabilities = (genuine, 1.0 - genuine - false_one, false_one)
    if storage is None:
        storage = (0.0,) * clicks

    for labels in product(range(3), repeat=clicks):
        weight = prod(label_probabilities[label] for label in labels)
        if weight == 0:
            continue
        true_slots = [slot for slot, label in enumerate(labels) if label == 0]
        true_mask = sum(1 << slot for slot in true_slots)
        false_one_mask = sum(1 << slot for slot, label in enumerate(labels) if label == 2)
        terms = []
        for alice_values in product((0, 1), repeat=len(true_slots)):
            alice_mask = sum(value << slot for slot, value in zip(true_slots, alice_values))
            alice = false_one_mask | alice_mask
            bob = false_one_mask | (true_mask ^ alice_mask)
            terms.append((dim * alice + bob, alice_mask))

        for row, left in terms:
            for col, right in terms:
                charges = [(left >> slot & 1) - (right >> slot & 1) for slot in range(clicks)]
                if sum(charges) == 0:
                    # Increments beyond each gap occur in the phases of all later clicks.
                    decay = sum(gap * sum(charges[i + 1 :]) ** 2 for i, gap in enumerate(gaps))
                    decay += sum(age * abs(charge) for age, charge in zip(storage, charges))
                    state[row, col] += weight * exp(-decay) / len(terms)

    np.testing.assert_allclose(np.trace(state), 1, atol=2e-15)
    return state


def extract(state, dim, locations):
    positions = [alice * dim + bob for alice, bob in locations]
    return state[np.ix_(positions, positions)]


def bell_overlap(block):
    return float(block.sum()) / (2 * np.trace(block))


def verify_triplet(q, x, y):
    state = raw_state((x, y), q)
    a, b = exp(-x), exp(-y)
    target = (1 + a * b) / 2
    full_mask = 0b111
    all_true_success = 0.0
    for alice_masks in ((1, 2, 4), (6, 5, 3)):
        locations = [(mask, full_mask ^ mask) for mask in alice_masks]
        sector = extract(state, 8, locations)
        np.testing.assert_allclose(np.trace(sector), 3 * q**3 / 8, atol=2e-15)
        # Each two-level Kraus operator applies amplitude 1/sqrt(2) in its support.
        for i, j in combinations(range(3), 2):
            filtered = sector[np.ix_([i, j], [i, j])] / 2
            np.testing.assert_allclose(np.trace(filtered), q**3 / 8, atol=2e-15)
            visibility = exp(-sum((x, y)[i:j]))
            np.testing.assert_allclose(bell_overlap(filtered), (1 + visibility) / 2, atol=2e-15)
            assert bell_overlap(filtered) >= target - 2e-15
            all_true_success += np.trace(filtered)

    best_positions = (1, 2) if x <= y else (2, 4)
    left, right = best_positions
    selected_dyad = extract(state, 8, [(left, right), (right, left)])
    if q < 1:
        np.testing.assert_allclose(bell_overlap(selected_dyad), (1 + max(a, b)) / 2, atol=2e-15)
    np.testing.assert_allclose(np.trace(selected_dyad), q**2 * (1 - q) / 2, atol=2e-15)
    success = all_true_success + np.trace(selected_dyad)
    np.testing.assert_allclose(success, q**2 / 2 + q**3 / 4, atol=2e-15)
    return success, target


def verify_dyad(q, gap):
    state = raw_state((gap,), q)
    partial_transpose = state.reshape(4, 4, 4, 4).transpose(0, 3, 2, 1).reshape(16, 16)
    eigenvalues = np.linalg.eigvalsh(partial_transpose)
    negativity = -sum(eigenvalues[eigenvalues < 0])
    np.testing.assert_allclose(negativity, q**2 * exp(-gap) / 4, atol=2e-15)
    return negativity


def verify_two_sided(q, false_one, gap):
    state = raw_state((gap,), q, false_one)
    keep = [(alice, bob) for alice in (1, 2) for bob in (1, 2)]
    accepted = extract(state, 4, keep)
    partial_transpose = accepted.reshape(2, 2, 2, 2).transpose(0, 3, 2, 1).reshape(4, 4)
    false_zero = 1 - q - false_one
    expected = false_zero * false_one - q**2 * exp(-gap) / 4
    np.testing.assert_allclose(np.linalg.eigvalsh(partial_transpose)[0], expected, atol=2e-15)


def verify_noisy_triplet():
    q, alpha, beta = 0.8, 0.198, 0.002
    gaps = (0.05, 0.05)
    storage = (0.011, 0.006, 0.001)
    state = raw_state(gaps, q, beta, storage)
    decoded = np.zeros((4, 4))

    for alice_masks, bob_masks in (((1, 2, 4), (6, 5, 3)), ((6, 5, 3), (1, 2, 4))):
        for i, j in combinations(range(3), 2):
            locations = list(product((alice_masks[i], alice_masks[j]), (bob_masks[i], bob_masks[j])))
            decoded += extract(state, 8, locations) / 2

    # Use the later dyad in the tie, reversing Bob's excitation labels.
    decoded += extract(state, 8, list(product((2, 4), (4, 2))))
    success = float(np.trace(decoded))
    overlap = float((decoded[0, 0] + decoded[3, 3] + 2 * decoded[0, 3]) / 2)
    visibilities = [exp(-sum(gaps[i:j]) - storage[i] - storage[j]) for i, j in combinations(range(3), 2)]
    expected_success = (q**2 + 4 * alpha * beta) * (3 * q / 4 + alpha / 2)
    expected_overlap = 3 * q**3 / 4 * (1 + np.mean(visibilities)) / 2
    expected_overlap += q**2 * alpha / 2 * (1 + visibilities[-1]) / 2
    np.testing.assert_allclose(success, expected_success, atol=2e-15)
    np.testing.assert_allclose(overlap, expected_overlap, atol=2e-15)

    delta, target = 0.002, 0.95
    fidelity_lower = (overlap - delta) / success
    dyad_upper = (q**2 * exp(-min(gaps)) / 4 - alpha * beta) / (target - 0.5)
    assert fidelity_lower >= target and success - delta > dyad_upper
    print(f"Noisy example, success >= {success - delta:.8f}, fidelity >= {fidelity_lower:.8f}")
    print(f"  At target {target:.2f}, ideal dyad success <= {dyad_upper:.8f}")


def entropy(probabilities):
    # Exact zero eigenvalues can be slightly negative after diagonalization.
    nonnegative = np.maximum(probabilities, 0)
    log_argument = np.maximum(nonnegative, np.finfo(float).tiny)
    return -(nonnegative * np.log2(log_argument)).sum(axis=-1)


def dyad_yield(gap):
    v = np.exp(-gap)
    p = np.stack(((1 + v) / 2, (1 - v) / 2), axis=-1)
    return (1 - entropy(p)) / 2


def compare_triplet_marginals(x, y):
    x, y = np.broadcast_arrays(x, y)
    a, b = np.exp(-x), np.exp(-y)
    ones = np.ones_like(a)
    sector = np.stack((ones, a, a * b, a, ones, b, a * b, b, ones), axis=-1)
    sector = sector.reshape(x.shape + (3, 3)) / 3
    triplet = 3 * (log2(3) - entropy(np.linalg.eigvalsh(sector))) / 4
    return triplet - dyad_yield(x) - dyad_yield(y)


def verify_entropic_identity(x, y):
    block = raw_state((x, y), 1.0)
    phase_state = extract(block, 8, [(mask, 7 ^ mask) for mask in range(8)])
    phase_state = phase_state.reshape((2,) * 6)
    left_middle = np.trace(phase_state, axis1=0, axis2=3).reshape(4, 4)
    middle_right = np.trace(phase_state, axis1=2, axis2=5).reshape(4, 4)
    middle = np.trace(left_middle.reshape((2,) * 4), axis1=0, axis2=2)
    conditional_mutual_information = (
        entropy(np.linalg.eigvalsh(left_middle))
        + entropy(np.linalg.eigvalsh(middle_right))
        - entropy(np.linalg.eigvalsh(middle))
        - entropy(np.linalg.eigvalsh(phase_state.reshape(8, 8)))
    )
    np.testing.assert_allclose(
        conditional_mutual_information, compare_triplet_marginals(x, y), atol=2e-15
    )


def quadrature(box, order):
    nodes, weights = leggauss(order)
    # Squaring the coordinate softens the logarithmic slope at a zero gap.
    root_x = (nodes + 1) * sqrt(box) / 2
    x, w = root_x**2, weights * sqrt(box) * root_x
    leading = w @ dyad_yield(x)
    gap_moment = w @ (x * dyad_yield(x))
    conditional_mutual_information = compare_triplet_marginals(x[:, None], x[None, :])
    connected_triplet = w @ conditional_mutual_information @ w
    assert conditional_mutual_information.min() > -2e-14
    return leading, connected_triplet, gap_moment


def main():
    for q in (0.2, 0.8, 1.0):
        for x, y in ((0.05, 0.05), (0.1, 1.2), (1.2, 0.1), (0.0, 0.4)):
            verify_triplet(q, x, y)
            verify_dyad(q, x)
            verify_dyad(q, y)
    for x in (0.1, 1.2):
        verify_two_sided(0.6, 0.2, x)
    verify_noisy_triplet()
    for x, y in ((0, 0), (0.05, 0.9), (0.9, 0.05), (2.1, 7.0)):
        verify_entropic_identity(x, y)

    success, target = verify_triplet(0.8, 0.05, 0.05)
    best_dyad_ceiling = verify_dyad(0.8, 0.05) / (target - 0.5)
    assert success > best_dyad_ceiling
    print(f"Finite example, target fidelity {target:.8f}")
    print(f"  Three-click success {success:.8f}; any selected dyad <= {best_dyad_ceiling:.8f}")

    exact = (log(2) - pi**2 / 24) / (2 * log(2))
    leading, connected, moment = quadrature(24, 128)
    np.testing.assert_allclose(leading, exact, rtol=0, atol=2e-10)
    _, connected_smaller, moment_smaller = quadrature(14, 128)
    np.testing.assert_allclose(connected, connected_smaller, rtol=0, atol=2e-10)
    np.testing.assert_allclose(moment, moment_smaller, rtol=0, atol=2e-10)
    assert connected > 0
    print(f"Sparse coefficient {exact:.10f} (quadrature {leading:.10f})")
    print(f"Connected triplet integral {connected:.8f}; dyad gap moment {moment:.8f}")
    print(f"Numerical clean second-order coefficient {connected - moment:.8f}")


if __name__ == "__main__":
    main()
