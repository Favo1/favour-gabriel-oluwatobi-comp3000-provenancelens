"""Evaluation metrics."""

import numpy as np


def expected_calibration_error(probs, labels, n_bins: int = 10) -> float:
    """Expected calibration error (Guo et al., 2017) for a binary detector.

    probs:  predicted probability that each image is fake (class 1).
    labels: ground truth, 1 for fake and 0 for real.
    A well-calibrated detector has confidence that matches its accuracy.
    """
    probs = np.asarray(probs, dtype=float)
    labels = np.asarray(labels, dtype=int)
    if probs.shape != labels.shape or probs.size == 0:
        raise ValueError("probs and labels must be non-empty and the same shape")

    predicted = (probs >= 0.5).astype(int)
    confidence = np.where(predicted == 1, probs, 1.0 - probs)
    correct = (predicted == labels).astype(float)

    bin_ids = np.minimum((confidence * n_bins).astype(int), n_bins - 1)
    ece = 0.0
    for b in range(n_bins):
        mask = bin_ids == b
        if mask.any():
            gap = abs(correct[mask].mean() - confidence[mask].mean())
            ece += gap * mask.mean()
    return float(ece)
