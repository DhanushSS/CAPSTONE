# Proposed architecture and assumptions

## Communication domains and shared analysis

CAN and V2X remain separate communication domains. Each has its own ingestion, feature extraction and detector output. A shared security-analysis layer associates relevant events and adjusts attribution confidence. It must retain the origin of each observation and the uncertainty introduced by missing data or clock alignment.

The baseline will use timing correlation. DYNOTEARS will be an evaluated extension rather than a prerequisite for producing a local verdict. A quiet or unavailable second domain must not automatically classify a first-domain anomaly as benign.

## Fleet corroboration

The initial experiment proposes four registered clients and at most one faulty client. Three matching, eligible, signed verdicts for the same event and policy epoch will be required for fleet corroboration. The implementation must specify membership, identity uniqueness, event matching, vote freshness and honest non-equivocation. Replayed, invalid or duplicate votes must not count.

Insufficient votes or unresolved disagreement will produce a local-only result with explicit fleet status. Different vehicles may legitimately observe different things; their votes cannot be combined merely because their timestamps are close.

This is a proposed corroboration rule. It is not automatically a complete PBFT implementation and does not prove that the underlying attack label is true. Any claim of replicated-state consensus needs a full protocol and a separate safety/liveness argument.

## GhostTrace evidence preservation

Planned components:

- Versioned event records and detector outputs linked by cryptographic hashes.
- Signed witness receipts binding an external witness to a specific commitment.
- Local buffering during disconnection and reconciliation after reconnection.
- Selected encrypted evidence retained independently under a defined retention policy.
- A deterministic verifier that checks signatures, chain continuity, identifiers and available commitments.

Integrity and availability are measured separately. A receipt cannot recover a deleted payload. An unwitnessed gap can remain ambiguous. A correctly signed record can still contain an incorrect sensor observation.

## Bounded Agentic AI

The investigator will operate after deterministic detection and evidence verification. It may retrieve verified records, organize timelines, compare hypotheses and draft cited reports. It must expose unsupported or missing evidence and preserve uncertainty.

The implementation will deny the agent write access to canonical verdicts and evidence commitments. Vehicle-control and autonomous-remediation tools are outside scope. Analysts review alerts and any response. An unavailable AI API will delay investigation assistance without stopping local detection or logging.

## Deployment allocation

| Component | Planned host |
|---|---|
| Edge detection, logging and resource measurements | Pi 4-class node |
| V2X and fleet-client simulation | Existing Macs |
| Model development and initial DYNOTEARS fitting | Existing Macs |
| Witness/evidence coordination and SOC dashboard | Separate Mac processes or machines |
| Investigation agent | Mac orchestration with an allowed API or feasible local fallback |

## Open decisions

Detector selection, exact label taxonomy, time-synchronization tolerance, event-key construction, witness trust, key storage, retention policy, adaptation gates and response workflow remain implementation decisions. These must be documented before experiments are presented as evidence of robustness.
