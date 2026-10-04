# CAN and V2X integration: what is already known

**VerdictTrace should not claim to be the first system combining CAN and V2X.** Published architectures already bring those inputs into shared security analysis.

| Prior work | Relevant overlap | Location |
|---|---|---|
| [Language Agent Model-Driven Distributed Consensus, APCC 2025](https://doi.org/10.34385/proc.97.w4-3-6) | CAN, V2X and GPS inputs, feature fusion, a language agent, consensus and logging | Figure 1 and Section II-A |
| [Blockchain-Empowered Lightweight Language Agent, ICTC 2025](https://d2j16w31g89z0j.cloudfront.net/site/ictc2025/abs/E02-6.pdf) | Multi-source collection, timestamp alignment, normalization and attention-based analysis | PDF page 2, Section II-A |
| [Securing autonomous vehicles: a dual-domain intrusion detection system for intra-vehicle and external networks, 2026](https://doi.org/10.1007/s12083-026-02214-w) | A unified CAN/V2X IDS evaluated using synthetic datasets representing the domains | Section 1.3 and Figure 1 |

These are published descriptions, not independent reproductions or verified production deployments. The third paper was identified after the 13-paper evidence PDF was prepared and is included here as an additional comparison.

## Three different meanings of integration

1. **One platform:** separate CAN and V2X detectors share a dashboard and evidence store.
2. **Feature-level fusion:** features from both domains enter a shared model.
3. **Shared attribution:** independent detector outputs are combined with bounded cross-domain context and explicit missing-data handling.

The proposal currently follows the third approach. A single shared model is a useful experimental comparison, but adopting it as the sole detector would change the original independent-detection requirement.

## Proposed contribution to test

Evaluate whether independent CAN and V2X detection, combined through bounded evidence correlation, improves benign-versus-malicious drift attribution while preserving verifiable evidence during outages and compromised participation.

Compare CAN-only, V2X-only, shared-feature-model, independent-plus-timing and independent-plus-DYNOTEARS configurations. Use matched data splits and report false alarms, attack recall, attribution accuracy, missing-stream behaviour and computational cost. Existing integration work rules out a broad first-integration claim; it does not preclude a specific, experimentally supported contribution.
