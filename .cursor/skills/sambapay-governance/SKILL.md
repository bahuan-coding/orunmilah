---
name: sambapay-governance
description: Governance for SambaPay: decision rights, decision log, obligations register, SPA and group-ownership status, regulatory map, and the weekly pulse and monthly pack to PaySecure London. Use when André Silva asks who decides, what to report to London, how to record a decision, what the company owes regulators or counterparties, or how a board-style answer should look.
disable-model-invocation: true
---

# SambaPay governance

## Files this skill owns

- `company-os/governance/README.md` — decision rights, group and ownership status, board material, London counterparts.
- `company-os/governance/decision-log.md` — one line per decision, newest on top.
- `company-os/governance/licensing-roadmap.md` — the path to sub-acquiring in our own name and to payment-institution authorisation; the committee; stages and dates.
- `company-os/governance/ownership-brief.md` — board view of the ownership transaction: facts, what is at stake, decisions D23–D29, questions for the paper and London. Never quoted in the Welcome Kit or to the team.
- `company-os/risk-compliance/obligations.md` — what is owed, to whom, by when, with evidence.
- `company-os/reports/london/weekly-pulse.md` and `monthly-pack.md` — templates.
- `references/london-reporting.md` — how to fill and send them.
- `references/regulatory-map.md` — instruments and what they mean for us; all "verify with counsel".
- `references/licensing-committee.md` — how the specialist committee runs and what it produces.
- `references/payfac-committee.md` — linguistic and business precision of the four statuses. Payment facilitator is not sub-acquirer.

## Licensing path

Read `company-os/governance/licensing-roadmap.md` before answering anything about sub-acquiring, the payment-institution licence, capital, modality or dates. Dates are brutally honest: production volume on DD1 Cielo; DD2 opens in parallel and does not gate volume; 1 Oct is day one of October volume on DD1 Cielo; 31 Oct is breakeven; do not promise a BCB filing or grant date. Never quote a threshold, a capital figure or a regulator deadline as fact; write "verify" and name the instrument. The path committee is agents, not people: `references/licensing-committee.md`. The words for today, next and then are written by the PayFac committee: `references/payfac-committee.md`. October volume words are written by the business committee: `../sambapay-finance/references/business-committee.md`. Today we operate as payment facilitator under a partner Merchant of Record. We will be a sub-acquirer. Payment institution follows. Do not skip the middle status. Do not write that Stage 1 is done. Do not write 1 October as a day without volume.

## Decision rights (from the 30 Aug 2026 chart, adjusted)

- André Silva decides. The test: which option brings us closer to revenue from DD1 Cielo production volume, on the take rate Hansraj proposes, so we cover the company's costs. The team elaborates. Process owners execute (`company-os/people/process-map.md`). They do not close a change of direction. Kit words: `welcome-kit/05-how-we-work.md`.
- Clayton Lira (Merchant Operations Analyst) executes blocks on André Silva's order.
- Sheila Esmeralda (Compliance Officer) is on leave and outside the project. Not in tactical work for now. Correspondence she owned runs through André Silva.
- Leandro Silva (Head of Engineering and Product) opens merchant accounts.
- Thiago Silva (Head of Operations) owns the day's figure.

## Recording a decision

Append to the top of the table in `decision-log.md`: Date | Decision | Options considered | Chosen | Why | Owner | Revisit. One line. Then update the file the decision changes, the same day, and `welcome-kit/00-the-map.md` if a status changed.

## Preparing anything for London

Read `references/london-reporting.md`. Numbers come from registers, never from memory. Every number has a source and a date. Facts, numbers, dates, asks. No adjectives. Signed "André Silva", nothing else.

## Obligations

Every obligation in `obligations.md` has an owner and a next-due date. Review monthly before the pack. A missed date is a blocker in the next pulse.

## Standing governance items

- SPA A55 LLC → PaySecure not signed as of 19 Sep 2026; ask London for status weekly until signed. When André Silva asks about the transaction, his risks or what to decide, read `company-os/governance/ownership-brief.md` and answer with its facts, its nine stakes, D23–D29 and section 7.6 (plain language of Q23–Q28); never add a term that is not in the paper. Never put any of this in the Welcome Kit.
- PaySecure legacy balances (finance README) until remitted and released.
- Sub-acquirer then payment-institution path: counsel plan, dates, owner André Silva. Language of the statuses: `references/payfac-committee.md`.

## Depth

PCI: `~/.cursor/skills/pci-specialist/SKILL.md`. AML/CFT: `~/.cursor/skills/legal-counsel/brasil-compliance-pld/SKILL.md`. Sub-acquirer and schemes: `~/.cursor/skills/legal-counsel/mcc-pci-sub-acquirer/SKILL.md`.
