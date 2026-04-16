#!/usr/bin/env python3
"""Numerical verification for the exponential 2-cycle construction.

This script uses mpmath only. It refines a period-2 point c of exp,
forms d = exp(c), constructs the logarithm branches and the two-slice
interpolation germ from Section 6 of the paper, and prints residuals.
"""

from __future__ import annotations

import mpmath as mp


mp.mp.dps = 80

# Initial approximation for the 2-cycle point c.
C0 = mp.mpc(
    "3.7567652815725784678422918566083452574054174644127706123003482385112402345226397403",
    "-11.053007865057470597615332650377142253422199135213883318285370741089406031920099591",
)


def refine_cycle(c: mp.mpc, steps: int = 10) -> tuple[mp.mpc, mp.mpc]:
    """Refine c as a root of exp(exp(z)) - z and return (c, d)."""
    for _ in range(steps):
        f = mp.e ** (mp.e ** c) - c
        df = mp.e ** (mp.e ** c) * mp.e ** c - 1
        c -= f / df
    d = mp.e ** c
    return c, d


c, d = refine_cycle(C0)
cycle_residual = abs(mp.e ** d - c)

print("Refined 2-cycle:")
print(f"c = {c!s}")
print(f"d = {d!s}")
print(f"|exp(d) - c| = {cycle_residual}")

# Local logarithm branches along the two components.
log_c = mp.log(c)
log_d = mp.log(d)
n = int(mp.nint((mp.im(d) - mp.im(log_c)) / (2 * mp.pi)))
m = int(mp.nint((mp.im(c) - mp.im(log_d)) / (2 * mp.pi)))
branch_residual_c = abs(log_c + 2 * n * mp.pi * 1j - d)
branch_residual_d = abs(log_d + 2 * m * mp.pi * 1j - c)
print()
print("Branch checks:")
print(f"n = {n}, m = {m}")
print(f"|Log(c) + {2*n}*pi*i - d| = {branch_residual_c}")
print(f"|Log(d) + {2*m}*pi*i - c| = {branch_residual_d}")

mu = d + 1 / c
print()
print(f"mu = d + 1/c = {mu!s}")


def phi(z: mp.mpc) -> mp.mpc:
    return (z - c) / (d - c)


def g_mu(w: mp.mpc) -> mp.mpc:
    return (1 - w) / (1 - (1 + mu) * w)


def D_mu(z: mp.mpc) -> mp.mpc:
    return c + (d - c) * g_mu(phi(z))


# Piecewise logarithm germ B.
def B(z: mp.mpc, component: str) -> mp.mpc:
    if component == "c":
        return mp.log(z) + 2 * n * mp.pi * 1j
    if component == "d":
        return mp.log(z) + 2 * m * mp.pi * 1j
    raise ValueError("component must be 'c' or 'd'")


# Base reset lift.
def L_D(u: mp.mpc, v: mp.mpc) -> mp.mpc:
    Du = D_mu(u)
    return c + (v - Du) / (u - Du) * (Du - c)


# Quotients from the two-slice theorem.
Q_c = (mp.e ** c - mu - 1) / (d - c)
S_c = (1 / c + 1) / (c - d)
Q_d = (mp.e ** d) * mu / (d - c)
S_d = (1 / d + 1) / (d - c)


# Analytic quotients evaluated componentwise.
def Q_formula(u: mp.mpc) -> mp.mpc:
    return (mp.e ** u - L_D(u, c)) / ((c - u) * (c - D_mu(u)))


def S_formula(v: mp.mpc, component: str) -> mp.mpc:
    return (B(v, component) - L_D(c, v)) / ((v - c) * (v - d))


def Q(u: mp.mpc) -> mp.mpc:
    if u == c:
        return Q_c
    if u == d:
        return Q_d
    return Q_formula(u)


def S(v: mp.mpc, component: str) -> mp.mpc:
    if v == c:
        return S_c
    if v == d:
        return S_d
    return S_formula(v, component)


# Two-slice interpolation formula using the idempotent e_c.
def R(u: mp.mpc, v: mp.mpc, comp_u: str, comp_v: str) -> mp.mpc:
    e_c_u = 1 if comp_u == "c" else 0
    e_c_v = 1 if comp_v == "c" else 0
    return Q(u) * e_c_v + S(v, comp_v) * e_c_u - Q_c * e_c_u * e_c_v


# Final binary germ.
def f(u: mp.mpc, v: mp.mpc, comp_u: str, comp_v: str) -> mp.mpc:
    return L_D(u, v) + (v - u) * (v - D_mu(u)) * R(u, v, comp_u, comp_v)


samples = [
    ("c", c + (1 + 1j) * mp.mpf("1e-12")),
    ("d", d + (1 + 1j) * mp.mpf("1e-12")),
]


print()
print("Corner quotient checks:")
eps = mp.mpf("1e-40")
corner_checks = [
    ("Q near c vs Q_c", abs(Q_formula(c + eps) - Q_c)),
    ("Q near d vs Q_d", abs(Q_formula(d + eps) - Q_d)),
    ("S near c vs S_c", abs(S_formula(c + eps, "c") - S_c)),
    ("S near d vs S_d", abs(S_formula(d + eps, "d") - S_d)),
]
for name, value in corner_checks:
    print(f"{name}: {value}")

print()
print("Sample residuals:")
residuals: list[tuple[str, mp.mpf]] = []
for comp, u in samples:
    comp_D = "d" if comp == "c" else "c"
    residuals.append((f"diag at {comp}", abs(f(u, u, comp, comp) - D_mu(u))))
    residuals.append(
        (f"reset at {comp}", abs(f(u, D_mu(u), comp, comp_D) - c))
    )
    residuals.append((f"vertical slice at {comp}", abs(f(u, c, comp, "c") - mp.e ** u)))

for comp, v in samples:
    residuals.append(
        (f"horizontal slice at {comp}", abs(f(c, v, "c", comp) - B(v, comp)))
    )

for name, value in residuals:
    print(f"{name}: {value}")

print()
print("Maximum sample residual:")
print(max(value for _, value in residuals))
