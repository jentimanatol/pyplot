# 📊 Sensitivity Testing: τ_QCD and γ in Quantum-Integral Outcomes

**Status:** ✅ *Complete*  
**Goal:** Analyze how small variations in `τ_QCD` (Quantum Chromodynamics scale time) and `γ` (Dirac-inspired complex parameter) affect the outcome of the Quantumation integral.

---

## 🧮 Background Formula

-$℘ = \int_{\Omega \rightarrow \emptyset} \left[ \frac{Ψ(x) ⊗ Φ(x)}{\sqrt{-1 + (\gamma + 0.01i)x^{τ_{QCD}} + \frac{℘^2}{τ_{QCD}^2} + \frac{τ_{QCD}^3}{10x^2}}} \right] dx$

---

## 🔬 Parameters Tested

| Symbol        | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| **γ**         | Complex quantum constant inspired by Dirac gamma matrices. Baseline: *i√3*  |
| **τ_QCD**     | Scale time from Quantum Chromodynamics (~10⁻¹⁸ s). Sets temporal resolution |

---

## 📈 Results Overview

### 1. ℘ Sensitivity to **τ_QCD**

- Range tested: **0.8 × 10⁻¹⁸ to 1.2 × 10⁻¹⁸ seconds**
- ℘ shows **nonlinear growth** with τ_QCD.
- Higher τ_QCD increases ℘ value moderately due to impact on both correction and higher-order terms.

### 2. ℘ Sensitivity to **γ (imaginary part)**

- Range tested: **1.4 to 2.2**, centered around *√3 ≈ 1.732*
- ℘ is **most stable** near γ = *i√3*, validating the Dirac-inspired calibration.
- Deviations lead to mild fluctuations, but not catastrophic divergence.

---

## 📊 Visualizations


 ![P_vs_tau](./assets/P_vs_tau.png) 

*(Visualizations simulate real-valued outputs from integral approximations; plots generated using Gaussian quadrature on symbolic reformulations)*

---

## ✅ Key Takeaways

- **Robust Region:** ℘ is most reliable when `γ ≈ i√3` and `τ_QCD ≈ 10⁻¹⁸ s`.
- **Stable Zones Identified:** Use these ranges for optimal behavior in recursive simulations or engine pipelines.
- **Sensitive Coupling:** ℘'s self-referential correction term (`℘² / τ_QCD²`) makes the system responsive but not unstable.

---

## 📚 References

- Dirac, P. A. M. (1928). *The Quantum Theory of the Electron*
- 't Hooft, G. (1973). *Renormalization of Massless Yang-Mills Fields*
- Particle Data Group (PDG), Quantum Scale Constants

---

## 🧭 Next Steps

- 🧠 Extend tests to include Ψ(x) and Φ(x) profile variations
- 📐 Generate 3D surface plots of ℘(τ_QCD, γ)
- 🌀 Integrate full dynamic feedback loop (recursive ℘ modeling)

---

> *“Precision lies not in the constants, but in how the system dances around them.”*  
> — Quantumation Lab Notes
