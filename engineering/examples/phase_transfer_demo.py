"""Illustrative algebraic plot. Not a receiver performance prediction."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from coherent_receiver.phase_transfer import (
    differential_delay_magnitude_squared, small_offset_approximation
)


def main():
    f = np.linspace(0, 1, 401)
    exact = differential_delay_magnitude_squared(f, 1.0)
    approximation = small_offset_approximation(f, 1.0)
    fig, ax = plt.subplots()
    ax.plot(f, exact, label="Exact pure-delay identity")
    ax.plot(f, approximation, "--", label="Small-offset approximation")
    ax.set_xlabel(r"Normalized offset $f|\Delta\tau|$")
    ax.set_ylabel(r"Differential magnitude squared")
    ax.set_title("Illustrative mathematical transfer; no receiver validation")
    ax.legend()
    fig.tight_layout()
    target = Path("build/figures/phase-transfer-demo.png")
    target.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(target, dpi=160)
    print(target)


if __name__ == "__main__":
    main()
