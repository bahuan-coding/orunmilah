# Risk and compliance

Purpose: stay licensed, stay PCI compliant, know every merchant, answer every letter, manage disputes.
Owner: André Silva (accountable, PCI 12.1.4). Correspondence and KYB policy: Sheila. KYB operation: Clayton. Disputes: Thiago.
Cadence: obligations reviewed monthly in the pack; every new merchant screened before any acquirer.
Registers: `obligations.md`.

## Regulatory position

- Today: operating partner is Merchant of Record (carries merchant risk and reserve; PCI SAQ-D assessed). SambaPay operates as payment facilitator.
- Path: payment-institution authorisation plus cross-border authorisation at the Central Bank of Brazil.
- Verify with counsel before quoting: Lei 12.865/2013; Circular BCB 3.886/2018; Resolução BCB 80/2021; Circular BCB 3.978/2020; Carta-Circular BCB 4.001/2020; LGPD (Lei 13.709/2018).

## PCI DSS 4.0.1

- Partner MoR: SAQ-D assessed. SambaPay scope after rebrand: Open (SAQ-D for Service Providers assumed). Accountable: André Silva. Sheila is not the PCI officer.
- Rules for eight people: card data only inside the engine, tokenised; 2-step verification on every account; credentials in the vault only.

## Know the merchant (AML/CFT)

- Stack: Global Pass (KYB, first to contract), Jumio (identity), G2 (merchant risk). Screen PEP and sanctions before any acquirer sees a merchant. Checklist of all three DD2 acquirers complete before go-live.
- Suspicious activity: report to Sheila and André Silva; they decide on reporting to the authorities (COAF; verify obligations for the current structure).

## Card schemes and disputes

- Visa and Mastercard write to the acquirer; Sheila answers. MCC honesty: high-risk volume on the partner's production rail; ordinary-MCC rails stay clean.
- Chargeblast pre-dispute alerts: register each merchant's CAID before go-live. Chargeback API on Thiago's desk. Verify: Visa VIRP/VAMP and Mastercard ECP thresholds.

## Data protection

- DPO: Sheila. dpo@sambapay.tech.

## Open

D7, D8, D14; SambaPay PCI scope; COAF obligations; scheme programme thresholds.
