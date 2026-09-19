# 07 · How the Business Works

Status: In discussion

Written for everyone: the developer should finish it understanding the money, the finance operator understanding the flow.

## A payment, in eight steps

1. A shopper pays at the merchant's checkout: a Website Factory storefront, or the merchant's own site using our checkout.
2. Our engine captures the transaction and routes it to the right rail for the method: card (3DS or 2D), PIX, boleto.
3. The acquirer or rail authorises. The approval rate is measured here. Approval times margin is the number we live on.
4. The acquirer settles funds into our local account on its window (D+n). Every operator has a cut-off; the operator windows register in the Company OS holds them. Open: the register is being filled.
5. Reconciliation. The acquirer's file is tied to our ledger line by line. Nothing downstream is trusted until it ties. Hansraj (PaySecure) confirms.
6. Fees, rolling reserve, refunds and chargebacks net out.
7. Remittance: local bank to PaySecure, by one of two paths. The partner's tokenized-PIX rail; or an OTC desk that takes our reais by same-day PIX and sells us USDC into our own wallet, which we then send to PaySecure. The desk's cost is measured against PTAX, the official daily rate. Open: the remittance contract.
8. PaySecure pays the merchant.

## Where the money is made

We price as a margin over cost: ICC++. Acquirer, scheme and FX costs pass through at cost, with no markup. Our fee is the spread above cost. The take rate is defined by Sridhar (Sri Amit). Until he names the number, the working structure is 1% ICC++.

A rolling reserve of 15% is held back from the merchant's settlements going forward, to cover refunds and chargebacks, and released as it matures. Legacy books used 10% on BRL (gross) and about 9.58% on CLP (net). Operational cash we hold ourselves is zero.

Volume times margin rules everything. Our clients run on thin margins and high volume; a small rate change moves their whole result and ours. Brazil is our cheapest product, and keeping it cheap is the strategy.

## Who carries the risk today

**Cielo** acts as Merchant of Record: it carries the merchant risk and the rolling reserve, is PCI SAQ-D assessed, and is connected to a growing set of local acquirers. We bring the rails, the relationships and the merchants; PaySecure brings the flow. Sub-acquiring in our own name is the next step; the payment-institution licence follows.

## Money in motion, every day

Reconciliation is the first job of every business day. Then money moves: refunds and cancels (Clayton), payouts, reserve and FX (Taina), collections and payables (Rafaela). Factoring: cover all volumes with 100% anticipation, even where Brazilian credit would take D+30; nothing more; the price must be competitive. Nobody sells this to us as a vendor.

## How a merchant is created

1 Document validation: KYB screening (Global Pass, Jumio, G2) and the checklist of all three DD2 acquirers. 2 Site creation in the Website Factory. 3 MID creation at the acquirers, and the merchant's CAID. 4 Go live, only after the CAID is registered with Chargeblast; the merchant joins the daily reconciliation.
