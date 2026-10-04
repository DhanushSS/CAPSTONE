# Project proposal

## Title

**VerdictTrace- Tamper-Evident, Byzantine-Robust Cross-Layer Drift Attribution for Connected Vehicle Fleets**

## Problem statement

Connected vehicles depend on internal Controller Area Network (CAN) traffic and external Vehicle-to-Everything (V2X) communication. Software updates, operating conditions, driver behaviour and sensor ageing can change observed traffic. Attackers can also induce changes that resemble ordinary drift. Detecting a distribution change therefore does not, by itself, establish an attack or its cause.

After an alert, missing records introduce a second uncertainty: evidence may have been altered, delayed by connectivity loss or lost from storage. Changes in a model's performance introduce a separate issue that must not be confused with log tampering. The project will investigate these distinctions using controlled scenarios and preserved evidence.

## Proposed approach

VerdictTrace will analyse CAN and V2X independently and combine their evidence through a shared attribution policy. Timing correlation will modify confidence while preserving single-layer detections. DYNOTEARS will be evaluated as a graph-based context extension against the timing baseline; its benefit and cost remain hypotheses.

Vehicles will exchange signed, event-matched verdicts and confidence values rather than raw model weights. A documented minimum-quorum rule will determine when fleet corroboration is available. Local detection will remain active when the rule cannot be satisfied.

GhostTrace will preserve chained records, signed witness receipts and selected independently retained evidence. A deterministic verifier will distinguish supported cryptographic inconsistencies from delayed, unavailable and unresolved evidence. These distinctions depend on explicit key, witness, retention and fault assumptions.

A bounded Agentic AI investigator will retrieve verified evidence, reconstruct timelines and generate cited root-cause hypotheses for analysts. Its tools will be read-only with respect to canonical verdicts and evidence. It will not directly control vehicles or perform autonomous remediation.

## Planned outputs

- A local verdict with affected communication layer, confidence and supporting evidence references.
- Separate fleet-corroboration status, including insufficient quorum and disagreement.
- Forensic status distinguishing verified alteration, available evidence and unresolved gaps.
- Human-reviewed investigative summaries and a SOC dashboard.
- An experimental cause-labelled CAN+V2X dataset and a separate audit-tampering/outage dataset.
- A reproducible evaluation and research manuscript, subject to demonstrated results.

## Applications and use cases

1. Assess whether a post-update traffic change is consistent with benign drift or attack-like behaviour.
2. Retain a CAN-only attack alert when V2X observations remain normal or unavailable.
3. Investigate a V2X anomaly alongside internal vehicle events without assuming correlation proves cause.
4. Preserve and reconcile evidence after a vehicle reconnects.
5. Identify cryptographically supported log alteration while avoiding false tampering claims during ordinary outages.
6. Help an analyst compare competing explanations and locate the records supporting each one.

## Scope and status

This is a laboratory research proposal. Four existing M4 MacBook Air machines and a planned Pi 4-class node will support simulation, edge measurements and dashboard development. Simulated V2X and experimental synchronization will be documented explicitly. No production readiness, functional-safety certification, accuracy, latency or formal isolation result has been demonstrated.
