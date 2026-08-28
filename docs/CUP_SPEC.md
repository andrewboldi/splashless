# Reference Cup Specification (FROZEN — all theory, sims, and CAD use these numbers)

The target vessel is a standard rigid 8-US-fluid-ounce cup (polypropylene, smooth interior),
modeled as a truncated cone, sitting on a rigid horizontal table. The cup is NOT modified —
the device may only occupy space above the rim and may transiently insert thin elements
through the open top (they must fully retract by end of fill).

## Interior geometry (frustum)

| Parameter | Symbol | Value |
|---|---|---|
| Interior bottom radius | r_b | 27.5 mm |
| Interior top (rim) radius | r_t | 35.0 mm |
| Interior height (floor → rim plane) | H | 77.0 mm |
| Wall half-angle from vertical | α | atan((35−27.5)/77) = 5.56° |
| Rim edge radius (sharp-ish rolled rim) | r_rim | 1.0 mm |

Brim-full volume: V = (πH/3)(r_t² + r_t·r_b + r_b²) = (π·77/3)(1225 + 962.5 + 756.25) mm³
= **237.37 mL = 8.026 US fl oz** (1 US fl oz = 29.5735 mL).

Radius at fill height z (z from floor): r(z) = 27.5 + (7.5/77)·z  [mm].
Volume to height z: V(z) = (π z/3)(r(z)² + r(z)·27.5 + 27.5²)  [mm³].

## Fluid properties (water, 20 °C)

| Property | Value |
|---|---|
| Density ρ | 998.2 kg/m³ |
| Dynamic viscosity μ | 1.002×10⁻³ Pa·s |
| Surface tension σ (water–air) | 0.0728 N/m |
| Capillary length λ = √(σ/ρg) | 2.73 mm |
| g | 9.81 m/s² |

## Success criteria (device acceptance tests)

1. **Delivered volume:** ≥ 236.6 mL (8.000 fl oz) resting inside the cup at t_end + 2 s.
   Stretch goal: additional meniscus overfill above the rim (quasi-static crown), target ≥ 8.3 fl oz total.
2. **Zero splash-out:** no liquid volume ends up outside the cup (outside rim radius, below rim plane,
   or on the table). Simulation tolerance: spilled volume < 0.5 mL (≈ resolution floor), target 0.
3. **Fill time:** minimize T (first water release → 99% of target volume delivered).
   Target T ≤ 0.5 s; stretch T ≤ 0.30 s. ("Instantaneous" to a human observer.)
4. **No residual contact:** device parts that entered the cup airspace are clear of the liquid at t_end.

## Definitions

- **Rim plane:** z = 77.0 mm.
- **Spill:** any liquid crossing the rim plane at radius > r_t moving outward/downward, or found
  outside the cup interior at end state.
- **Fill time T:** from first liquid crossing the rim plane (or valve opening if device pre-inserted)
  until delivered-in-cup volume first reaches 99% of final resting volume.
