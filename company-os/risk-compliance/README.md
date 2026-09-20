# Risk and compliance

Purpose: stay licensed, stay PCI compliant, know every merchant, answer every letter, manage disputes.
Owner: André Silva (accountable, PCI 12.1.4). Correspondence and KYB policy: André Silva while Sheila Esmeralda is on leave and outside the project. KYB operation: Clayton. Disputes: Thiago.
Cadence: obligations reviewed monthly in the pack; every new merchant screened before any acquirer.
Registers: `obligations.md`.

## Regulatory position

- Today: operating partner is Merchant of Record (carries merchant risk and reserve). SambaPay operates as payment facilitator.
- Operations run on PaySecure's white label. Production API keys from the acquirers go to the core team. We configure and reconcile on that instance. Platform PCI is PaySecure's. SambaPay's own SAQ remains Open. Questionnaire type on PaySecure's side: Open to confirm (earlier pages said SAQ-D; spoken as SAQ B).
- Next: we will be a sub-acquirer in our own name (own merchant IDs under the acquirers). Stage 1 is not closed.
- Then: payment-institution authorisation plus cross-border authorisation at the Central Bank of Brazil. Filing starts the day Stage 1 closes.
- Payment facilitator and sub-acquirer are not the same word. Verify with counsel before quoting: Lei 12.865/2013; Circular BCB 3.886/2018; Resolução BCB 80/2021; Circular BCB 3.978/2020; Carta-Circular BCB 4.001/2020; LGPD (Lei 13.709/2018).

## PCI DSS 4.0.1

- Platform PCI: PaySecure's, because we run on its white label. Not Cielo's Merchant of Record role. SambaPay's own SAQ after rebrand: Open. Accountable: André Silva. Sheila is not the PCI officer.
- Rules for eight people: card data only inside the white label, tokenised; 2-step verification on every account; production API keys in the vault only.

## Know the merchant (AML/CFT)

- Stack: Global Pass (KYB, first to contract), Jumio (identity), G2 (merchant risk). Screen PEP and sanctions before any acquirer sees a merchant. Checklist of all three DD2 acquirers complete before go-live.
- Suspicious activity: report to André Silva; he decides on reporting to the authorities (COAF; verify obligations for the current structure).

## Card schemes and disputes

- Visa and Mastercard write to the acquirer. A letter is the moment that tells whether this business works. We are responsive and we are coherent. The facts reach André Silva as soon as they exist. MCC honesty: high-risk volume on the partner's production rail; ordinary-MCC rails stay clean.
- Chargeblast pre-dispute alerts: register each merchant's CAID before go-live. Chargeback API on Thiago's desk. Verify: Visa VIRP/VAMP and Mastercard ECP thresholds.

## Data protection

- DPO: André Silva while Sheila Esmeralda is on leave. dpo@sambapay.tech.

## Open

D7, D8, D14; SambaPay PCI scope; PaySecure SAQ type (page said D; spoken as B); COAF obligations; scheme programme thresholds.
