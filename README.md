# Splashless

**Maximum-rate, zero-splash filling of a standard 8 oz cup** — physics theory, custom simulation
engines, CAD, optimization, and a validated mechanism design.

The problem: drop the maximum number of ounces of water into a standard eight-ounce cup as close
to instantaneously as possible, with zero splash-out, under realistic water physics.

## Layout

| Path | Contents |
|---|---|
| `docs/CUP_SPEC.md` | Frozen reference cup + fluid spec and acceptance criteria |
| `docs/research/` | Literature briefs: splash physics, industrial filling, SPH/PBF methods, capillarity, optimization |
| `theory/` | First-principles theory: splash-limited flow, optimal release profile, fill-time bounds |
| `concepts/` | Candidate mechanism designs + judged downselect |
| `sph-rs/` | Custom Rust SPH (weakly-compressible) fluid engine, TDD, rayon-parallel |
| `sim/warp/` | NVIDIA Warp GPU simulation (position-based fluids lineage) |
| `sim/blender/` | Blender/Mantaflow FLIP high-fidelity scenes + animation renders |
| `model/` | Fast quasi-1D fill model + optimal-control / CMA-ES design optimization |
| `cad/` | Parametric OpenSCAD device CAD → STL → renders |
| `paper/` | LaTeX paper: theory, methods, results |
| `results/` | Metrics (JSON), plots, convergence + validation tables |
| `media/` | Rendered animations and stills |

## Toolchain

Rust (rayon), Python (NumPy/SciPy/Matplotlib, NVIDIA Warp), Blender headless (Mantaflow FLIP),
OpenSCAD, LaTeX. Issue tracking via beads (`bd ready`).
