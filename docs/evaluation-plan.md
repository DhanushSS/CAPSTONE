# Evaluation and dataset plan

All experiments below are planned. No results are reported in this repository.

## Dataset construction

Use authentic CAN recordings or controlled bench traffic with V2X simulation driven by a documented shared scenario. Timestamp alignment alone is insufficient to establish a meaningful relationship between streams.

Record scenario ID, capture/run ID, vehicle/client ID, timestamps, clock offsets, source provenance, affected layer, injection interval, controlled cause and detector version. Distinguish physically recorded data, replay, synthetic traffic and simulated attacks. Keep ground-truth injection manifests separate from detector inputs.

Construct a second audit dataset containing controlled record edits, truncation, rollback, forged receipts, local deletion, disconnections and delayed delivery. Include deletion before and after external witnessing.

## Scenario families

| Family | Required controls |
|---|---|
| Benign change | Stable baseline, legitimate configuration/update changes and operating-condition shifts |
| Attack-like drift | Gradual controlled injection and matched benign changes |
| Single-domain attack | CAN-only and V2X-only cases, including a quiet second domain |
| Cross-domain context | Related events, unrelated coincident events and clock offsets |
| Fleet failures | One faulty client, false votes, replay, duplicate identity attempts, disagreement and insufficient quorum |
| Evidence failures | Alteration, deletion, delayed records, ordinary outages and missing payloads with retained receipts |
| Model behaviour | Ordinary adaptation/forgetting, poisoning and unchanged-model controls |
| AI investigation | Valid evidence, incomplete evidence and misleading instructions embedded in retrieved text |

## Baselines and ablations

- Independent CAN-only and V2X-only detection.
- A shared feature-fusion model using both domains.
- Independent detectors with bounded timing-based confidence adjustment.
- The same system with DYNOTEARS-derived context.
- Local decisions versus signed fleet corroboration under the declared fault model.
- Local hash chains versus external receipts versus receipts plus independently retained payloads.
- Fixed investigative report templates versus the bounded agent.

## Measures

| Question | Measures |
|---|---|
| Is attribution useful? | Cause-label accuracy/F1, affected-layer accuracy, benign-change false alarms, attack recall, detection delay |
| Is uncertainty handled? | Calibration, abstention/unknown coverage and accuracy conditional on coverage |
| Is fleet support reliable? | Incorrect corroborations, rejected invalid votes, disagreement, local-only coverage and communication cost |
| Is evidence trustworthy and available? | Detectable alterations, recoverable payloads, verification delay and false tampering accusations |
| Does the agent help? | Citation validity, factual support, timeline accuracy, unsupported statements, latency and analyst usefulness |
| Is the testbed feasible? | CPU, RAM, storage, network overhead and latency on the assigned machines |

## Experimental discipline

Use chronological, scenario-disjoint splits where appropriate. Fit preprocessing, thresholds and graph structure only on permitted training/validation data. Do not expose ground-truth attack manifests to the evaluated detector. Retain public CAN benchmark comparisons and repeat runs with documented seeds and configurations.

State cryptographic, membership and witness assumptions. Analyse agreement safety separately from classification accuracy. Report negative results, missing-stream cases and unresolved causes. A publication claim should identify one reproducible improvement under stated conditions rather than rely on the number of integrated components.
