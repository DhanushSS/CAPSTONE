# Phase 1 ESA references

The numbers below match the November 2026 ESA report. The last column describes experiments proposed by the team.

## CAN and V2X security

| Report ref. | Paper | Published contribution | Proposed test |
|---|---|---|---|
| [1] | [IntentProv-IoV: Causally Grounded Provenance for Traffic-Intent Preservation in Explainable Vehicular Security](https://doi.org/10.3390/sym18091430) (2026) | Links traffic intent, response and provenance. | Compare CAN and V2X from the same braking event. |
| [2] | [An Endogenous Threat Recognition and Hazard Mitigation Framework for Intelligent Connected Vehicles Network Security](https://doi.org/10.1016/j.adhoc.2026.104362) (2026) | Combines CAN, V2X and application evidence for mitigation. | Count genuine warnings rejected by the policy. |
| [3] | [SCIMI: Semantic-Aware Collaborative Intrusion Detection for Multi-domain In-Vehicle Networks](https://repository.essex.ac.uk/43158/) (2026) | Models dependencies within in-vehicle networks. | Test whether external observations change a cause decision. |
| [4] | [Deep Reinforcement Learning for Misbehavior Detection Under Partially Observable V2X Data](https://arxiv.org/abs/2609.31217) (2026) | Studies misbehavior detection with missing observations. | Measure abstention as selected observations disappear. |
| [5] | [MIRAGE: Detecting Fake Emergency Electronic Brake Light Attacks in V2X Networks via Event-Gated Behavioral Analysis](https://www.usenix.org/conference/vehiclesec26/presentation/ka) (2026) | Checks trajectories after a braking warning and limits the response. | Keep genuine braking and sensor faults in the test set. |
| [6] | [Distinguishing Sensor Faults and Malicious Attacks in Connected Vehicles Using Machine Learning](https://doi.org/10.1109/CCNC65079.2026.11366546) (2026) | Classifies sensor faults and attacks in safety messages. | Compare false blocks at matched attack-block rates. |
| [7] | [Securing Autonomous Vehicles: A Dual-Domain Intrusion Detection System for Intra-Vehicle and External Networks](https://doi.org/10.1007/s12083-026-02214-w) (2026) | Detects threats across internal and external traffic. | Verify each action at the receiving endpoint. |
| [8] | [Language Agent Model-Driven Distributed Consensus for Advanced IoV Threat Response Management](https://doi.org/10.34385/proc.97.W4-3-6) (2025) | Combines language agents and distributed agreement for response. | Check that agent narratives cannot change a verdict. |

## GhostTrace and vehicle forensics

| Report ref. | Paper | Published contribution | Proposed test |
|---|---|---|---|
| [9] | [Federated-Trust Sharded Blockchain for Real-Time Forensics and Secure Data Collaboration in Cooperative V2X](https://doi.org/10.1007/s44443-026-00813-4) (2026) | Anchors evidence and scores trust across cooperating nodes. | Retain local evidence when signed reports disagree. |
| [10] | [Verifiable Event Evidence Sharing in VANETs via Threshold Multi-Witness Endorsement and Controlled Verification](https://doi.org/10.1007/s12083-026-02285-9) (2026) | Uses threshold endorsements for event evidence. | Measure evidence status when a witness disconnects. |
| [11] | [PSVDF: A Data Protection Framework for Vehicle Digital Forensics Utilizing Blockchain View and Cross-Platform Secure Space](https://doi.org/10.1016/j.bcra.2025.100393) (2026) | Links an on-chain commitment to protected off-chain content. | Recover bytes from an independent copy and verify the digest. |
| [12] | [Empowering Hyperledger Fabric Blockchain for Vehicular Forensics](https://doi.org/10.1016/j.adhoc.2026.104303) (2026) | Manages forensic records through a permissioned ledger. | Compare local verification during a ledger outage. |
| [13] | [GVDF-PIA: Group-Based Vehicular Digital Forensics and Proxy-Assisted Integrity Auditing for Intelligent Transportation](https://doi.org/10.1109/JIOT.2025.3624488) (2025) | Supports proxy integrity audits while vehicles are offline. | Separate pending upload from an inconsistent commitment. |
| [14] | [WIP: A Black Box System for Automotive Digital Forensics](https://www.usenix.org/conference/vehiclesec25/presentation/setiadji) (2025) | Uses GPS timing and continuous ECU authentication. | Reconstruct event order with bounded clock error. |
| [15] | [In-Vehicle Digital Forensics for Connected and Automated Vehicles With Public Auditing](https://doi.org/10.1109/JIOT.2023.3310578) (2024) | Uses public auditing for vehicle records. | Identify which omissions occurred before a checkpoint. |
| [16] | [TB-Logger: Secure Vehicle Data Logging Method Using Trusted Execution Environment and Blockchain](https://doi.org/10.1109/ACCESS.2023.3253626) (2023) | Protects vehicle logs with trusted execution and blockchain. | Characterize evidence loss after an abrupt bench shutdown. |

## Supporting references

17. [DYNOTEARS, Pamfil et al. (2020)](https://proceedings.mlr.press/v108/pamfil20a.html) — time-series structure learning.
18. [CICIoV2024](https://www.unb.ca/cic/datasets/iovdataset-2024.html) — dataset documentation.
19. [VeReMi NextGen](https://veremi-dataset.github.io/veremi-nextgen) — simulated V2X dataset documentation.
20. [Espressif ESP32 TWAI driver](https://docs.espressif.com/projects/esp-idf/en/v5.3.3/esp32/api-reference/peripherals/twai.html) — hardware interface documentation.
21. [Verma et al. (2024), ROAD dataset paper](https://doi.org/10.1371/journal.pone.0296879) — CAN intrusion-detection data.

## Further reading

The [97-entry search catalog](master-catalog.md) records the broader search as of 16 November 2026. Its numbering is independent of the ESA report. The team’s evidence notes cover the [eight VerdictTrace studies](verdicttrace-evidence.pdf) and [eight GhostTrace studies](ghosttrace-evidence.pdf).
