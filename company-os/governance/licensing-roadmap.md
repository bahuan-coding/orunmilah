# Licensing roadmap: sub-acquiring in our own name, then a payment institution

Owner: André Silva (decides).
Design: a committee of **agents**, not people (D19): the CEO Agent plus `sambapay-governance`, `sambapay-finance`, `sambapay-opportunities` and the personal PCI / AML / security skills. Implementation still has named people as workstream owners (Abner signup, Taina desks, Sheila obligations). Reviewed whenever a Stage-1 gate moves. Every regulatory statement here is a working hypothesis until a lawyer confirms it for a filing; dates are brutally honest.

## Where we stand

- Stage 0, today: an operating partner is the Merchant of Record and carries merchant risk and the rolling reserve (PCI SAQ-D assessed). A55 Payments operates as the payment facilitator. Volume today is zero. Remittance to PaySecure by the partner PIX path or the OTC on-ramp (reais → same-day PIX to a desk → USDC into our own wallet → PaySecure).
- Goal A (ASAP): everything required to operate as a **sub-acquirer**, serving cross-border businesses at the lowest possible fees. Own MIDs at Cielo, Asaas and EFI.
- Goal B (after Goal A is live): payment institution authorised by the Central Bank of Brazil. Filing starts the day Goal A closes. Grant date is the Central Bank's.

## The committee (agents)

| Seat | Who | Mandate | First deliverable |
|---|---|---|---|
| Chair (decides) | André Silva | Decides what only the company can decide | — |
| Design | CEO Agent (`sambapay-ceo`) | Cuts the path into slices; holds the honest dates | This file, refreshed |
| Regulatory and governance design | `sambapay-governance` plus personal legal/PCI/AML skills | Modality, dossier index, obligations, never quoting unverified thresholds | Sub-acquirer checklist with "verify" marks |
| Finance design | `sambapay-finance` | Capital premise (minimum for the elected modality); cost of the path | Capital line in `model.md` |
| Rails design | `sambapay-opportunities` | Cielo, Asaas, EFI signup order; second on-ramp desk | Signup questionnaire per acquirer |
| Implementation: acquirer signup | Abner Maioralli | Production of each new integration | Signup plan per acquirer |
| Implementation: obligations file | Sheila Esmeralda | Keeps `obligations.md` and letters | Stage-1 obligations with dates |
| Implementation: desks | Taina Chaves | MIPPO addendum, protocols, second desk | On-ramp memo |
| Implementation: own-MID ops | Thiago Silva | Reconciliation and settlement for own MIDs | Operator windows filled |
| Implementation: engine | Leandro Silva | Own-MID technical readiness | Technical plan |

Rules: the agents design; André Silva decides. No external lawyers to name for this committee. A human lawyer is still required when a filing or an SPA reading is in hand (Part 7). Workstreams execute one slice at a time. Every decision goes to `decision-log.md`.

## Stages and deadlines (brutally honest)

| Stage | Window | Done when | Depends on |
|---|---|---|---|
| 0 Today | Sep 2026 | — | — |
| 1 Sub-acquiring in our own name | From now. Account-open target **1 Oct 2026** at Cielo, Asaas, EFI. That date is brutal and is **not** volume go-live. First live merchant = the day the slowest of the three is actually live | Each of Cielo, Asaas, EFI has an account we can transact on; first own-MID merchant reconciled end to end; every Stage-1 obligation evidenced | Objective 1 (DD2), KYB stack (D7), Chargeblast (D8), PCI scope |
| 2 Authorisation readiness | Starts the day Stage 1 closes. No promised filing date | Request filed with the Central Bank of Brazil | SPA signed; capital paid in (premise: the minimum); Stage-1 evidence |
| 3 Regulator's analysis | Starts the day we file. Length is the Central Bank's | Authorisation granted | Filing quality; fast answers |
| 4 Payment institution live | After grant, within the start-of-operations deadline the regulator sets | First month reported to London under the new status | Stage 3 |
| Parallel: cross-border and FX | From Sep 2026 | MIPPO addendum this week; one desk (MIPPO/GFS) usable; second desk chosen (BRX candidate); protocol check closed by 30 Oct 2026 | Objective 1; Resolução BCB 561/2026 and the PSAV calendar |
| Parallel: Colombia and Mexico | After Brazil Stage 1 is moving | Counsel memos; first registration live in one country | Objective 6 |

## Stage 1 checklist (sub-acquiring in our own name)

- [ ] DD2 entity opened on Double Diamond's requirements; accounts at **Cielo, Asaas and EFI** (P31, P33)
- [ ] Entity stand-up: indicative all-in about R$ 5,000 (lawyer; digitising including 2-step on mobile for bank and acquirer apps; CNPJ; three acquirer accounts; no contract signed)
- [ ] Factoring in force on the volumes we run: all volume anticipated at a competitive price; nobody sells this as a vendor
- [ ] Payment facilitator / sub-acquirer registration with Visa and Mastercard through each of Cielo, Asaas and EFI
- [ ] AML/CFT programme written and in force; KYB stack live (Global Pass first)
- [ ] PCI scope statement for own MIDs; assessment date set
- [ ] Card-receivables registration and settlement-grid participation arranged where thresholds apply (verify)
- [ ] Chargeblast configured; CAID per merchant before go-live
- [ ] Reconciliation and remittance designed for own MIDs; operator windows filled
- [ ] One on-ramp desk live (MIPPO/GFS); second desk chosen; MIPPO addendum signed
- [ ] First merchant live on our own MIDs and reconciled end to end (when the slowest of Cielo, Asaas, EFI is live)

## Stage 2 dossier index (authorisation readiness)

- [ ] Filing entity decided (D20). Modality: everything required to have been a sub-acquirer first; then the payment-institution modality the agents recommend
- [ ] Capital paid in (D22 premise: the minimum for the elected modality)
- [ ] Controllers' documentation, including the foreign controller, complete; SPA signed
- [ ] Directors appointed; fit-and-proper documentation
- [ ] Business plan with projections; governance structure; internal controls
- [ ] AML/CFT policy and responsible director; cyber-security policy; ombudsman arrangement (verify applicability)
- [ ] Request filed; protocol number recorded here

## Instruments the committee verifies (never quoted as fact before a lawyer confirms)

Lei 12.865/2013; Resolução BCB 80/2021 (payment-institution constitution and authorisation; modalities); Circular BCB 3.886/2018 (sub-acquirer); Circular BCB 3.952/2019 (sub-acquirers in centralised settlement); Resolução CMN 4.734/2019 (card-receivables registration); Circular BCB 3.978/2020 and Carta-Circular BCB 4.001/2020 (AML/CFT); Resolução BCB 85/2021 (cyber-security); Resolução CMN 4.860/2020 (ombudsman); Lei 14.286/2021, Resolução BCB 277/2022 as amended by Resolução BCB 561/2026 (FX, eFX); Lei 14.478/2022, Resolução BCB 520 and IN BCB 704 (virtual assets, PSAV); PCI DSS 4.0.1; Visa and Mastercard payment-facilitator rules.

## Risks tracked

Regulator timing; foreign-controller documentation waiting on the SPA; 1 Oct account-open is already brutal; dependence on the partner MoR until Stage 1 closes; scheme registration clocks per acquirer; desks losing their PIX rail after 30 Oct 2026 without a protocol; eight people carrying implementation as a second job.

## Decisions taken

See `decision-log.md`. D19 closed (agents). D20 closed as to sub-acquirer-first; filing entity Open. D22 closed as a capital premise.
