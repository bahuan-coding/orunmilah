# 08 · Rules We Live By

Status: Settled

Regulation in plain language. The detail lives in the Company OS, risk-compliance, marked "verify with counsel" where it must be. This page is what every one of us must know.

## 1. We are regulated

We move other people's money. Today an operating partner is the Merchant of Record and carries the risk; we operate as the payment facilitator and are walking toward our own payment-institution and cross-border authorisation from the Central Bank of Brazil. Everything we promise a merchant must fit what we are licensed to do today.

## 2. Card data is radioactive (PCI DSS)

Card numbers exist only inside the engine, tokenised. Never in email, chat, Drive, a spreadsheet or a screenshot. If you see a card number where it should not be, stop and tell Thiago or Leandro. André Silva is accountable for PCI DSS; the partner Merchant of Record is SAQ-D assessed.

## 3. Know the merchant before anyone else does (KYB)

No merchant reaches an acquirer before we have checked who it is, who owns it, and whether any person is politically exposed or sanctioned. Tools: Global Pass, Jumio, G2. The checklist of every acquirer on the template is complete before go-live. Speed never buys an exception.

## 4. Anti-money-laundering

We never onboard what we cannot explain: the business, the owners, the source of volume. Anything suspicious is reported to Sheila and André Silva, who decide on reporting to the authorities. Nobody stops a merchant or holds funds except André Silva.

## 5. Personal data (LGPD)

Shoppers' and merchants' personal data is used only for the payment and kept only as long as needed. Requests from data subjects go to dpo@sambapay.tech.

## 6. Card scheme rules

Visa and Mastercard rules bind us through the acquirers. Merchant category codes are honest; high-risk volume runs on the partner's production rail so ordinary rails stay clean. Disputes are managed early through Chargeblast with each merchant's CAID. When Visa, Mastercard or an acquirer writes, Sheila answers; nobody else does.

## 7. Money moves only when the book ties

Reconciliation first. No remittance, release or payout before the day's figure ties and Hansraj has confirmed. The rolling reserve is released only as it matures and only net of refunds and chargebacks.

## 8. What each of us never does

- Shares a password or turns off 2-step verification.
- Sends card data outside the engine.
- Promises a merchant a go-live date before its checklist and CAID are done.
- Speaks for the company to a regulator, a scheme or an acquirer without Sheila or André Silva.
- Moves money that has not been reconciled.
- Hides an open question. Open is honest.
