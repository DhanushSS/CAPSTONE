# Phase 1 Review 1: slide text and speaker notes


Text snapshot of the editable presentation. This records the proposal-stage deck; the research guide and CAN/V2X integration note include subsequent literature clarification.


## Slide 1

- UE24CS320A - Capstone Project Approval
- VerdictTrace-
- Tamper-Evident, Byzantine-Robust
- Cross-Layer Drift Attribution for
- Connected Vehicle Fleets
- Project Guide: Prof. Saravanaraj S
- Batch 51
- Dhanush Sai Suprapadha
- PES2UG24CS154
- Gurubelli Yekambar Eshwar Rao
- PES2UG24CS173
- Shreya R D
- PES2UG24CS680
- Amruta Karoshi
- PES2UG24CS675
- Phase I / Review 1

### Speaker notes

Opening (about 35 seconds). Introduce VerdictTrace as a proposed detection, attribution and evidence-preservation system for connected fleets. The project is at the proposal stage. State the two main goals: discriminate benign changes from suspicious behavior across CAN and V2X, and retain evidence that can be independently checked. Agentic AI supports investigation after deterministic decisions. It does not control a vehicle. Introduce the guide and team. No experimental performance results are claimed in this review.

References

## Slide 2

- Outline
- 02
- 01
- Problem statement
- Security question and intended outputs
- 02
- Scope and feasibility
- Testbed, budget and operating limits
- 03
- Background work
- Prior research and contribution to test
- 04
- Applications / use cases
- Fleet monitoring and forensic review
- 05
- Proposed architecture
- Attribution, GhostTrace and Agentic AI
- 06
- Deliverables and timeline
- Three-phase plan and evaluation

### Speaker notes

Roadmap (about 25 seconds). The presentation first defines the security problem and shows how the proposed prototype fits the available resources. Then it compares related research, walks through scenarios and architecture, and finishes with deliverables, phase milestones and the bounded AI investigation workflow. The four review criteria are addressed directly: problem statement, applications, background work and feasibility.

References

## Slide 3

- Problem Statement
- 03
- Distinguish benign change from suspicious CAN / V2X behavior,
- attribute the likely cause, and preserve independently verifiable evidence.
- Software update /
- benign behavior change
- Gradual injection /
- falsified vehicle message
- Similar-looking
- telemetry change
- Benign
- Suspicious
- Insufficient evidence
- A quiet V2X layer must not clear a suspicious CAN event.

### Speaker notes

Problem (about 75 seconds). A detector can observe a change without knowing its cause. Our controlled scenarios include legitimate updates, changes in driving conditions and gradual malicious injection. Each CAN and V2X detector must retain an independent judgment. Cross-layer timing contributes context but cannot serve as a rule that makes all single-layer changes benign. The output is a calibrated assessment with an affected layer and ranked cause hypothesis. An insufficient-evidence outcome is essential when observation alone cannot distinguish causes. Distribution shift is not automatically concept drift or malicious intent; the dataset protocol will define the exact shift being tested. Forensics adds a second challenge: after an alert, local records or model behavior may change. The project must preserve what was observed and which evidence remains independently verifiable.

References

[1] S. Fuhrman, O. Gungor and T. Rosing, "CND-IDS: Continual Novelty Detection for Intrusion Detection Systems," 62nd ACM/IEEE Design Automation Conference (DAC), 2025. DOI: 10.1109/DAC63849.2025.11132541. https://ieeexplore.ieee.org/document/11132541/ . Open author version: https://arxiv.org/abs/2502.14094

Dataset reference: K. Verma et al., "A comprehensive guide to CAN IDS data and introduction of the ROAD dataset," PLoS ONE 19(1), 2024. https://www.ornl.gov/publication/comprehensive-guide-can-ids-data-and-introduction-road-dataset . Dataset: https://zenodo.org/records/10462796

## Slide 4

- Scope and Feasibility Study
- 04
- Proposed laboratory testbed
- CAN replay +
- simulated V2X
- Pi 4-class edge
- Detection + logging
- Four existing M4 Macs
- Simulation, training, SOC and AI tools
- Total team ceiling: INR 20,000
- Pi and essentials
- 9,000
- CAN and bench
- 4,000
- Storage / cables
- 2,000
- API / testing
- 2,000
- Contingency
- 3,000
- Total (INR)
- 20,000
- Planning allocations, subject to quotations
- Sparse fleet: local-only verdicts
- API outage: queue AI investigations
- Experimental validation
- Human-reviewed responses only

### Speaker notes

Feasibility (about 75 seconds). Use a single purchased Pi-class edge node and a CAN interface for the hardware path. Fleet members are simulated software clients on the existing Macs; one physical node does not represent a deployed fleet. Macs host V2X generation, model development, DYNOTEARS fitting, evidence coordination, dashboard and AI orchestration. Benchmark local inference, logging and any graph-based scoring on the Pi. The listed amounts are expenditure ceilings chosen to sum to INR 20,000, not verified vendor quotations. NVIDIA hosted APIs are the initial candidate for the investigator, with bounded calls, caching and retry. No NVIDIA GPU is required on a Mac to call a hosted endpoint. If the API is unavailable, deterministic detection and logging continue. Insufficient fleet participation triggers a local-only status. Dataset realism and witness density are explicit experimental limitations. Vehicle-control intervention and autonomous remediation are outside scope.

References

NVIDIA prototyping API access is subject to model-specific rate limits and load; free availability is not a service-level guarantee. https://forums.developer.nvidia.com/t/nvidia-nim-faq/300317

## Slide 5

- Background
- 05
- CAN
- Internal control traffic
- ECUs and vehicle signals
- V2X
- External cooperation
- Vehicle and roadside messages
- Both layers can change
- for legitimate or adversarial reasons.
- Conceptual illustration

### Speaker notes

Domain setting (about 65 seconds). CAN is the in-vehicle communication surface connecting electronic control units. V2X carries information between vehicles and external participants. The illustration shows these two surfaces conceptually; it is not a wiring design or a photograph of our prototype. Changes in operating conditions may shift the observed distributions. Our data protocol will implement documented benign-change scenarios and adversarial counterparts. The principal question is whether evidence from both layers improves attribution while retaining sensitivity to attacks on only one layer. Recorded CAN traffic and simulated V2X require a controlled shared scenario, not merely matching timestamps on unrelated datasets. Public ROAD and VeReMi resources provide independent benchmark and scenario references.

Visual provenance: generated with the built-in ImageGen tool for this deck. Prompt: a restrained 3D technical illustration on white, silver foreground vehicle with a conceptual ECU bus, two background vehicles and roadside wireless links, blue/turquoise accents, no text or labels.

References

Dataset reference: K. Verma et al., "A comprehensive guide to CAN IDS data and introduction of the ROAD dataset," PLoS ONE 19(1), 2024. https://www.ornl.gov/publication/comprehensive-guide-can-ids-data-and-introduction-road-dataset . Dataset: https://zenodo.org/records/10462796

V2X dataset reference: VeReMi Extension, IEEE ICC 2020. https://github.com/VeReMi-dataset/VeReMi-dataset.github.io/blob/main/veremi-extension.md

Additional close work: M. Golam, J.-M. Lee and D.-S. Kim, "Language Agent Model-Driven Distributed Consensus for Advanced IoV Threat Response Management," APCC 2025. https://www.ieice.org/publications/proceedings/bin/pdf_link.php?fname=W4-3-6.pdf&iconf=APCC&lang=E&number=W4-3-6&vol=97&year=2025

## Slide 6

- Background Work and Research Gap
- 06
- Prior work
- Established contribution
- VerdictTrace evaluation focus
- CND-IDS [1]
- IEEE/ACM DAC, 2025
- Continual novelty
- detection
- Cause-labeled benign /
- suspicious drift
- Block4Forensic [2]
- IEEE ComMag, 2018
- Vehicular evidence
- provenance
- Witnessed IDS records
- under connectivity gaps
- Language-agent IoV IDS [3]
- ICTC, 2025
- Language-agent detection
- with blockchain logging
- AI investigation isolated
- from recorded verdicts
- DYNOTEARS [4]
- AISTATS, 2020
- Temporal structure
- learning
- Attribution gain and cost
- against timing correlation
- Forensic hash validity [5]
- IEEE ICCES, 2020
- Integrity background
- C-ISFCR-listed paper
- Signed anchors and
- independent receipts
- Proposed contribution: uncertainty-aware attribution with witnessed
- evidence and a bounded AI investigator.

### Speaker notes

Related work (about 85 seconds). These papers establish the components we build on. CND-IDS motivates continual detection. Block4Forensic establishes prior vehicular evidence sharing. The ICTC language-agent paper is an especially important close comparison, and related APCC work already discusses CAN, V2X and GPS. Therefore neither a multi-layer detector nor adding an agent to logging is sufficient to establish novelty. Our contribution must be demonstrated through cause-labeled drift experiments, explicit below-quorum behavior, connectivity-aware evidence verification and an investigator separated from canonical verdict storage. DYNOTEARS is essential to our evaluation, but faster or more accurate performance is a hypothesis, not a known result for this task. C-ISFCR is the research centre listing the forensic hash paper; IEEE ICCES is its publication venue. We verified this listing but have not reproduced that paper. The research gap is provisional pending a deeper systematic comparison. No first-ever claim is made.

References

[1] S. Fuhrman, O. Gungor and T. Rosing, "CND-IDS: Continual Novelty Detection for Intrusion Detection Systems," 62nd ACM/IEEE Design Automation Conference (DAC), 2025. DOI: 10.1109/DAC63849.2025.11132541. https://ieeexplore.ieee.org/document/11132541/ . Open author version: https://arxiv.org/abs/2502.14094

[2] M. Cebe, E. Erdin, K. Akkaya, H. Aksu and S. Uluagac, "Block4Forensic: An Integrated Lightweight Blockchain Framework for Forensics Applications of Connected Vehicles," IEEE Communications Magazine, 56(10), pp. 50–57, 2018. DOI: 10.1109/MCOM.2018.1800137. https://arxiv.org/abs/1802.00561

[3] M. Golam, J.-M. Lee and D.-S. Kim, "Leveraging Blockchain-Empowered Lightweight Language Agent for Efficient Distributed DoS Detection in IoV Networks," ICTC 2025, pp. 286–291, IEEE proceedings. https://d2j16w31g89z0j.cloudfront.net/site/ictc2025/abs/E02-6.pdf

[4] R. Pamfil et al., "DYNOTEARS: Structure Learning from Time-Series Data," AISTATS, PMLR 108, pp. 1595–1605, 2020. https://proceedings.mlr.press/v108/pamfil20a.html

[5] P. K. C., R. Soman and P. Honnavalli, "Validity of Forensic Evidence using Hash Function," IEEE ICCES, pp. 823–826, 2020. DOI: 10.1109/ICCES48766.2020.9138061. https://ieeexplore.ieee.org/document/9138061 . Bibliographic inclusion verified through PES C-ISFCR: https://www.isfcr.pes.edu/research . Full methods were not accessible during preparation; this is a background reference, not a reproduced baseline.

[6] A. Z. Md Jalal Uddin, A. Nayeem and T. Bhuiyan, "Robust Federated Learning for Anomaly Detection in Connected Autonomous Vehicle Networks Under Adversarial Attacks," Automation 7(3), 80, 2026. DOI: 10.3390/automation7030080. https://www.mdpi.com/2673-4052/7/3/80

Additional close work: M. Golam, J.-M. Lee and D.-S. Kim, "Language Agent Model-Driven Distributed Consensus for Advanced IoV Threat Response Management," APCC 2025. https://www.ieice.org/publications/proceedings/bin/pdf_link.php?fname=W4-3-6.pdf&iconf=APCC&lang=E&number=W4-3-6&vol=97&year=2025

## Slide 7

- Applications / Use Cases
- 07
- Planned scenarios for fleet security analysts
- Scenario
- Expected assessment to test
- Analyst value
- Legitimate update
- Benign change supported
- by context and evidence
- Fewer nuisance alerts
- CAN-only injection
- Suspicious CAN behavior
- without a V2X veto
- Retain local attack evidence
- Falsified V2X message
- Suspicious V2X behavior
- checked against vehicle context
- Prioritize fleet investigation
- Log deletion + outage
- Integrity conflict or
- insufficient evidence
- Separate contradiction
- from missing records
- Applications: fleet SOC monitoring, incident reconstruction and IDS research.

### Speaker notes

Applications (about 75 seconds). Walk through a concrete example: a legitimate software update changes message timing, while an attacker slowly injects CAN frames. The desired system uses separate layer evidence and documented context to distinguish these cases where possible. If V2X remains normal, the CAN alert is still preserved. A second scenario tests falsified V2X information against local vehicle context. The final scenario deletes or changes local records around a connection outage. A missing receipt alone is not evidence of tampering. A verified independent commitment that conflicts with the presented local history can support an integrity alert. These are intended experimental outcomes and use cases, not observed results. Users are fleet SOC analysts and researchers. The dashboard supports acknowledgment, annotations, additional evidence queries and report export; it does not actuate the vehicle.

References

Dataset reference: K. Verma et al., "A comprehensive guide to CAN IDS data and introduction of the ROAD dataset," PLoS ONE 19(1), 2024. https://www.ornl.gov/publication/comprehensive-guide-can-ids-data-and-introduction-road-dataset . Dataset: https://zenodo.org/records/10462796

V2X dataset reference: VeReMi Extension, IEEE ICC 2020. https://github.com/VeReMi-dataset/VeReMi-dataset.github.io/blob/main/veremi-extension.md

[2] M. Cebe, E. Erdin, K. Akkaya, H. Aksu and S. Uluagac, "Block4Forensic: An Integrated Lightweight Blockchain Framework for Forensics Applications of Connected Vehicles," IEEE Communications Magazine, 56(10), pp. 50–57, 2018. DOI: 10.1109/MCOM.2018.1800137. https://arxiv.org/abs/1802.00561

## Slide 8

- Proposed Architecture
- 08
- CAN detector
- Local evidence
- V2X detector
- Local evidence
- Local attribution
- Layer + hypothesis
- + confidence
- Timing / DYNOTEARS
- Confidence modifier
- Fleet corroboration
- Signed verdict + score
- Local-only assessment
- Fleet support unavailable
- GhostTrace
- Verdict + evidence status
- Quorum met
- Below quorum
- or conflicting
- votes
- Proposed test: 4 registered clients, at most 1 faulty; require 3 matching signed votes. Weights stay local.

### Speaker notes

Architecture (about 95 seconds). Local CAN and V2X detectors generate independent evidence. A versioned attribution policy preserves each detector assessment while using timing and DYNOTEARS-derived relationships as confidence modifiers. DYNOTEARS fitting initially runs on a Mac. Evaluate exported graph-based features or scores on the edge only after measuring their cost. The graph provides hypotheses under modeling assumptions; it does not prove causation. Vehicles share only event-matched signed verdicts, confidence and authentication metadata, not model weights. Honest observations from different events must never be combined into one vote. The initial experiment uses four registered clients and at most one Byzantine client. Require three matching signed labels for the same event and policy epoch before declaring fleet corroboration. The verifier rejects duplicate identities, stale votes and invalid signatures, and honest clients must not sign contradictory labels for an epoch. This threshold limits the influence of one arbitrary voter; it does not guarantee detection truth or establish a complete distributed consensus protocol. Honest observations may differ, so unresolved disagreement must remain visible. Below three matching votes it retains the local verdict and marks fleet support unavailable. Generalizing beyond this configuration requires a documented protocol and fault-model justification. The title refers to robustness under stated assumptions; neither a high vote count nor confidence weighting alone establishes Byzantine agreement. All local and fleet outcomes are recorded through GhostTrace. The agent reads evidence later and cannot rewrite this decision path.

References

[4] R. Pamfil et al., "DYNOTEARS: Structure Learning from Time-Series Data," AISTATS, PMLR 108, pp. 1595–1605, 2020. https://proceedings.mlr.press/v108/pamfil20a.html

[6] A. Z. Md Jalal Uddin, A. Nayeem and T. Bhuiyan, "Robust Federated Learning for Anomaly Detection in Connected Autonomous Vehicle Networks Under Adversarial Attacks," Automation 7(3), 80, 2026. DOI: 10.3390/automation7030080. https://www.mdpi.com/2673-4052/7/3/80

## Slide 9

- Expected Deliverables
- 09
- Phase I
- Design and baseline
- Threat model and protocol
- CAN / V2X scenario labels
- Independent baselines
- Phase II
- Integrated prototype
- DYNOTEARS and voting
- Witnesses and memory tests
- AI investigator and SOC
- Phase III
- Evaluation and release
- CAN + V2X drift dataset
- Audit-tampering dataset
- Code and manuscript
- Evaluation evidence
- Attribution
- F1, false alarms, delay
- Integrity
- Tamper recall, gap errors
- Agent and edge
- Grounding, latency, RAM

### Speaker notes

Deliverables and evaluation (about 85 seconds). Phase I produces the study protocol, threat model, controlled scenario generator and basic per-layer detectors. Phase II integrates every essential module, including DYNOTEARS, fleet verdict corroboration, hash-chained logs, independent witnesses, model-memory tests and the bounded agent dashboard. Phase III evaluates and releases the reproducible prototype, two datasets and a manuscript for submission. Dataset 1 contains synchronized experimental CAN and V2X scenarios with cause labels and provenance. Dataset 2 contains deletion, alteration, rollback and replay scenarios with genuine connectivity gaps as negative controls. Controlled forgetting scenarios are separately labeled for model-memory analysis. Publishing a paper is the goal; acceptance is not guaranteed. Use chronological and scenario-disjoint splits, held-out attack families, multiple seeds and uncertainty intervals. Compare per-layer-only detection, timing correlation and DYNOTEARS; local-only and fleet-assisted verdicts; hashes alone and witnessed records; a fixed report template and the agent. Agent evaluation measures evidence citation validity, factual support, unsupported claims, investigation latency and resistance to malicious text in retrieved records. Measure Pi CPU, RAM, throughput and detection/logging delay.

References

[1] S. Fuhrman, O. Gungor and T. Rosing, "CND-IDS: Continual Novelty Detection for Intrusion Detection Systems," 62nd ACM/IEEE Design Automation Conference (DAC), 2025. DOI: 10.1109/DAC63849.2025.11132541. https://ieeexplore.ieee.org/document/11132541/ . Open author version: https://arxiv.org/abs/2502.14094

[4] R. Pamfil et al., "DYNOTEARS: Structure Learning from Time-Series Data," AISTATS, PMLR 108, pp. 1595–1605, 2020. https://proceedings.mlr.press/v108/pamfil20a.html

[7] M. Umer, G. Dawson and R. Polikar, "Targeted Forgetting and False Memory Formation in Continual Learners through Adversarial Backdoor Attacks," 2020. https://arxiv.org/abs/2002.07111 . Experiments concern MNIST-based continual-learning tasks, not automotive data.

Dataset reference: K. Verma et al., "A comprehensive guide to CAN IDS data and introduction of the ROAD dataset," PLoS ONE 19(1), 2024. https://www.ornl.gov/publication/comprehensive-guide-can-ids-data-and-introduction-road-dataset . Dataset: https://zenodo.org/records/10462796

## Slide 10

- Project Timeline: Phases I, II and III
- 10
- Phase I
- Phase II
- Phase III
- Literature and threat model
- Scenario and dataset pipeline
- Per-layer detection + DYNOTEARS
- Verdict sharing + GhostTrace
- Agentic investigation + SOC
- Evaluation, release and paper
- Protocol
- Build and label
- Baseline and integrate
- Implement
- Integrate and test
- Validate and release
- Proposed phase sequence; bar lengths are schematic, not calendar durations.

### Speaker notes

Execution plan (about 60 seconds). This is a phase-based Gantt rather than an invented calendar. Phase I establishes the scope, threat assumptions, dataset protocol and baselines. Phase II performs integration, with the scenario pipeline supporting the detectors, GhostTrace and agent tools. Phase III concentrates on controlled evaluation, ablations, packaging datasets and code, and writing the manuscript. Iteration can cross phases, but implementation and release gates should remain explicit. Calendar dates and personal workload allocations are not asserted here. The review is a proposal review and none of these bars indicate completed implementation.

References

## Slide 11

- GhostTrace and Agentic Investigation
- 11
- Deterministic evidence checks
- Bounded AI workflow
- Hash-chained
- local records
- Witness receipts
- Delayed sync
- Verify signatures,
- anchors and consistency
- Integrity outcomes
- Consistent with commitments
- Verified integrity conflict
- Gap / insufficient evidence
- Plan evidence queries
- Retrieve and reconcile
- Timeline + cited hypotheses
- Human review
- Read-only
- evidence tools
- Memory regression checks retain an unresolved cause
- when ordinary forgetting and interference cannot be separated.

### Speaker notes

GhostTrace and Agentic AI (about 90 seconds). Explain the boundary first. Deterministic code verifies signatures, hash-chain links and independently retained commitments. Cryptographic consistency establishes consistency with a commitment, not that an original sensor claim or attack verdict was true. Hashes stored only on a fully compromised device can be rewritten, so independent witness receipts and trusted coordinator anchors are important. Receipt absence cannot prove benign connectivity loss or tampering. Outcomes distinguish consistency, a verifiable conflict and insufficient evidence. When the vehicle is isolated before external witnessing, the evidence gap remains visible. Model memory is tested against previously confirmed signatures, but deterioration alone does not establish malicious forgetting. The agent chooses bounded evidence queries through allowlisted read-only tools, reconciles available records, compares hypotheses and writes a report with record IDs and unknowns. Tool permissions and separate credentials prevent writes to canonical verdicts and evidence. Test these restrictions, including prompt injection in retrieved material. A human reviews, annotates and exports a separate report. Record the agent model/version, tool calls and report provenance separately from canonical verdicts. Formal isolation is an objective to verify, not a completed proof.

References

[2] M. Cebe, E. Erdin, K. Akkaya, H. Aksu and S. Uluagac, "Block4Forensic: An Integrated Lightweight Blockchain Framework for Forensics Applications of Connected Vehicles," IEEE Communications Magazine, 56(10), pp. 50–57, 2018. DOI: 10.1109/MCOM.2018.1800137. https://arxiv.org/abs/1802.00561

[5] P. K. C., R. Soman and P. Honnavalli, "Validity of Forensic Evidence using Hash Function," IEEE ICCES, pp. 823–826, 2020. DOI: 10.1109/ICCES48766.2020.9138061. https://ieeexplore.ieee.org/document/9138061 . Bibliographic inclusion verified through PES C-ISFCR: https://www.isfcr.pes.edu/research . Full methods were not accessible during preparation; this is a background reference, not a reproduced baseline.

[7] M. Umer, G. Dawson and R. Polikar, "Targeted Forgetting and False Memory Formation in Continual Learners through Adversarial Backdoor Attacks," 2020. https://arxiv.org/abs/2002.07111 . Experiments concern MNIST-based continual-learning tasks, not automotive data.

[3] M. Golam, J.-M. Lee and D.-S. Kim, "Leveraging Blockchain-Empowered Lightweight Language Agent for Efficient Distributed DoS Detection in IoV Networks," ICTC 2025, pp. 286–291, IEEE proceedings. https://d2j16w31g89z0j.cloudfront.net/site/ictc2025/abs/E02-6.pdf

## Slide 12

- Thank You
- Questions and Discussion
- VerdictTrace
- Batch 51

### Speaker notes

Closing (about 15 seconds). Invite questions about the threat assumptions, feasibility, novelty and evaluation.

Defence notes

1. Why both layers? Each preserves independent attack evidence; the project tests whether cross-layer context improves cause attribution.

2. Why Agentic AI? The agent chooses evidence queries and compares hypotheses, with cited records and human review. It does not issue the detector verdict.

3. Why DYNOTEARS? It is a required comparison of temporal structure learning against a simpler timing baseline. Benefit and runtime are measured, not assumed.

4. Does a hash prove the record is true? No. Integrity is checked relative to external commitments under stated key and witness assumptions.

5. Can isolation be completely solved? No. Missing independent witnesses may leave an unresolved evidence gap.

6. Does a quorum guarantee correctness? No. It depends on event alignment, authenticated membership, fault assumptions and honest detection quality.

7. What is completed? Proposal definition and initial literature review; prototype and experiments remain planned.

8. What is novel? The proposed combined treatment of cause-labeled drift, fleet uncertainty, witnessed IDS evidence and isolated agent investigation. This must be demonstrated by evaluation and a detailed prior-work comparison.

Full reference list

References

[1] S. Fuhrman, O. Gungor and T. Rosing, "CND-IDS: Continual Novelty Detection for Intrusion Detection Systems," 62nd ACM/IEEE Design Automation Conference (DAC), 2025. DOI: 10.1109/DAC63849.2025.11132541. https://ieeexplore.ieee.org/document/11132541/ . Open author version: https://arxiv.org/abs/2502.14094

[2] M. Cebe, E. Erdin, K. Akkaya, H. Aksu and S. Uluagac, "Block4Forensic: An Integrated Lightweight Blockchain Framework for Forensics Applications of Connected Vehicles," IEEE Communications Magazine, 56(10), pp. 50–57, 2018. DOI: 10.1109/MCOM.2018.1800137. https://arxiv.org/abs/1802.00561

[3] M. Golam, J.-M. Lee and D.-S. Kim, "Leveraging Blockchain-Empowered Lightweight Language Agent for Efficient Distributed DoS Detection in IoV Networks," ICTC 2025, pp. 286–291, IEEE proceedings. https://d2j16w31g89z0j.cloudfront.net/site/ictc2025/abs/E02-6.pdf

[4] R. Pamfil et al., "DYNOTEARS: Structure Learning from Time-Series Data," AISTATS, PMLR 108, pp. 1595–1605, 2020. https://proceedings.mlr.press/v108/pamfil20a.html

[5] P. K. C., R. Soman and P. Honnavalli, "Validity of Forensic Evidence using Hash Function," IEEE ICCES, pp. 823–826, 2020. DOI: 10.1109/ICCES48766.2020.9138061. https://ieeexplore.ieee.org/document/9138061 . Bibliographic inclusion verified through PES C-ISFCR: https://www.isfcr.pes.edu/research . Full methods were not accessible during preparation; this is a background reference, not a reproduced baseline.

[6] A. Z. Md Jalal Uddin, A. Nayeem and T. Bhuiyan, "Robust Federated Learning for Anomaly Detection in Connected Autonomous Vehicle Networks Under Adversarial Attacks," Automation 7(3), 80, 2026. DOI: 10.3390/automation7030080. https://www.mdpi.com/2673-4052/7/3/80

[7] M. Umer, G. Dawson and R. Polikar, "Targeted Forgetting and False Memory Formation in Continual Learners through Adversarial Backdoor Attacks," 2020. https://arxiv.org/abs/2002.07111 . Experiments concern MNIST-based continual-learning tasks, not automotive data.

Additional close work: M. Golam, J.-M. Lee and D.-S. Kim, "Language Agent Model-Driven Distributed Consensus for Advanced IoV Threat Response Management," APCC 2025. https://www.ieice.org/publications/proceedings/bin/pdf_link.php?fname=W4-3-6.pdf&iconf=APCC&lang=E&number=W4-3-6&vol=97&year=2025

Dataset reference: K. Verma et al., "A comprehensive guide to CAN IDS data and introduction of the ROAD dataset," PLoS ONE 19(1), 2024. https://www.ornl.gov/publication/comprehensive-guide-can-ids-data-and-introduction-road-dataset . Dataset: https://zenodo.org/records/10462796

V2X dataset reference: VeReMi Extension, IEEE ICC 2020. https://github.com/VeReMi-dataset/VeReMi-dataset.github.io/blob/main/veremi-extension.md

NVIDIA prototyping API access is subject to model-specific rate limits and load; free availability is not a service-level guarantee. https://forums.developer.nvidia.com/t/nvidia-nim-faq/300317
