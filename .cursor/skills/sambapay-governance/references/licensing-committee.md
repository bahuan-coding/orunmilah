# The specialist committee: how it runs

Purpose: design the path from payment facilitator on a partner rail to sub-acquiring in our own name, then to a payment institution. Source of truth: `company-os/governance/licensing-roadmap.md`. The words for those statuses: `references/payfac-committee.md`. This is a committee of **agents**, not people. André Silva decides.

## Seats

- Chair (decides): André Silva.
- Design: CEO Agent; `sambapay-governance`; `sambapay-finance`; `sambapay-opportunities`; personal PCI / AML / security skills.
- Implementation (people, not committee members): Abner (Cielo, Asaas, EFI signup); André Silva (obligations and letters while Sheila Esmeralda is on leave); Taina (desks); Thiago (own-MID ops); Leandro (engine).
- No external lawyers to name for this committee. A human lawyer is required when a filing or an SPA reading is in hand.

## Method (André Silva's)

The agents read the whole roadmap, cut the path into slices, each with a "done when" gate, and execute one slice at a time. After each slice they revise the next with what the last taught. They escalate to André Silva what is business or strategy, or irreversible. Perfect closes a slice; acceptable does not.

## Preparing a pass (the model does this)

1. Read `licensing-roadmap.md`, `obligations.md` and `decision-log.md`.
2. List every deadline in the next 30 days with owner and status. First: DD1 Cielo production volume. DD2 accounts in parallel, not the volume gate. 1 Oct is day one of October volume on DD1 Cielo.
3. List every "verify" item still unconfirmed by a lawyer; group by instrument.
4. Draft: decisions needed (with options and a recommendation), deadlines at risk, verify items, next slice.
5. After André Silva decides: update the roadmap the same day; one line per decision in the decision log; blockers into the next weekly pulse.

## Writing rules inside the committee's documents

- Follow `references/payfac-committee.md` for Merchant of Record, payment facilitator, sub-acquirer and payment institution. They are four statuses, not one.
- Never quote a threshold, capital figure or regulator deadline as fact until a lawyer confirms it in writing; write "verify" and name the instrument.
- Do not promise a BCB filing date or a BCB grant date. Production volume on DD1 Cielo. DD2 opens in parallel. 1 Oct is day one of October volume on DD1 Cielo. Do not write that date as a day without volume. Do not write that volume waits for DD2.
- Titles for everyone; André Silva by name only, never on the same line as a title word.
- English. Facts, numbers, dates, asks.

## Stage gates the committee guards

- Stage 1 closes when each of Cielo, Asaas and EFI has an account we can transact on, and the first own-MID merchant has been reconciled end to end.
- Stage 2 closes when the authorisation request is filed and the protocol number is in the roadmap. No promised filing date.
- Stage 3 closes when the authorisation is granted. No promised grant date.
- Stage 4 opens when the first month under the new status is reported to London.

## Depth

PCI: `~/.cursor/skills/pci-specialist/SKILL.md`. AML/CFT: `~/.cursor/skills/legal-counsel/brasil-compliance-pld/SKILL.md`. Sub-acquirer and schemes: `~/.cursor/skills/legal-counsel/mcc-pci-sub-acquirer/SKILL.md`. Sanctions: `~/.cursor/skills/legal-counsel/sanctions-screening/SKILL.md`. Card brand programmes: `~/.cursor/skills/legal-counsel/us-global-compliance/SKILL.md`.
