# 08 · Rules We Live By

Status: Settled

Regulation and the engine in plain language. Where a lawyer must confirm, we mark it. This page is what every one of us must know.

## 1. We are regulated

We move other people's money. Today a partner is the Merchant of Record and carries the risk. We operate as the payment facilitator. We will be a sub-acquirer: own merchant IDs under the acquirers, not yet a payment institution. After that, payment-institution and cross-border authorisation from the Central Bank of Brazil. Everything we promise a merchant must fit what we are licensed to do today.

## 2. The engine stays up

The culture is obsessively online. The engine is not allowed to go down. Traffic runs twenty-four hours a day, every day, from everywhere. An incident is reported the hour it appears, to Thiago and Leandro.

## 3. Card data is radioactive (PCI DSS)

Card numbers exist only inside PaySecure's white label, tokenised. Never in email, chat, a spreadsheet or a screenshot. If you see a card number where it should not be, stop and tell Thiago or Leandro. André Silva is accountable for PCI DSS. The PCI structure we operate under is PaySecure's, because we run on its white label.

## 4. Know the merchant before anyone else does (KYB)

No merchant reaches an acquirer before we have checked who it is, who owns it, and whether any person is politically exposed or sanctioned. Tools: Global Pass, Jumio, G2. The checklist of every acquirer on the template is complete before go-live. Speed never buys an exception.

## 5. Anti-money-laundering

We never onboard what we cannot explain: the business, the owners, the source of volume. Anything suspicious is reported to André Silva, who decides on reporting to the authorities. Nobody stops a merchant or holds funds except André Silva.

## 6. Personal data (LGPD)

Shoppers' and merchants' personal data is used only for the payment and kept only as long as needed. Requests from data subjects go to dpo@sambapay.tech.

## 7. Card scheme rules

Visa and Mastercard rules bind us through the acquirers. Merchant category codes are honest; high-risk volume runs on the partner's production rail so ordinary rails stay clean. Disputes are managed early through Chargeblast with each merchant's CAID. A letter from Visa, Mastercard or an acquirer is the moment that tells whether this business works. We are responsive and we are coherent. The facts reach André Silva as soon as they exist, so partners can use that speed in our defence and in any risk we have to mitigate. Payments carry every kind of risk.

## 8. Money moves only when the book ties

Reconciliation first. No remittance, release or payout before the day's figure ties and Hansraj has confirmed.

## 9. What each of us never does

- Sends card data outside the white label.
- Treats an engine drop as something to mention later.
- Promises a merchant a go-live date before its checklist and CAID are done.
- Moves money that has not been reconciled.
- Takes a client's merchants or disputes a client's accounts.
- Hides an open question. Open is honest.
