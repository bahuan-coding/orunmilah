# 06 · Who Does What

Status: In discussion

Eight people. Every one of us has a title and owns named processes, so a colleague in London, an acquirer or a merchant knows exactly who to reach. One exception: André Silva uses his name only. Titles, reporting lines and ownership below were confirmed on 19 September 2026. The full process map, thirty-three processes with owner and backup, is in the Company OS, people.

## The eight

**André Silva** · andre.silva@sambapay.tech
Direction of the company. The PaySecure and London relationship. Acquirer, OTC and partner relationships, including the DD2 entity with Double Diamond. Pricing and proposals. The only person who stops a merchant, holds funds or offboards. Highest-severity incidents. Accountable for PCI DSS (requirement 12.1.4). London reporting and the decision log.

**Leandro Silva** · Head of Engineering and Product · leandro.silva@sambapay.tech
The payment engine in code: processors, authorisation, tokenisation, 3DS, acquirer performance. Product roadmap. Acquirer integrations and MID creation. Merchant-creation steps 2 and 3. Website Factory build.

**Thiago Silva** · Head of Operations · thiago.silva@sambapay.tech
The day's correct figure: daily reconciliation and the confirmation with Hansraj at PaySecure. Live queues. Credit, identity, custody and secrets (Key Vault). Disputes: Chargeback API, Chargeblast and CAIDs. Incident response with Leandro.

**Sheila Esmeralda** · Compliance Officer · sheila.esmeralda@sambapay.tech
All correspondence with acquirers, Visa, Mastercard and regulators (notices, KYC packs, questionnaires). KYB, AML and sanctions policy. The obligations register. Acquirer document packs for DD2. LGPD contact. Does not hold or offboard.

**Clayton Lira** · Merchant Operations Analyst · clayton.lira@sambapay.tech
The merchant-creation pipeline, steps 1 and 4: documents, KYB screening in Global Pass, acquirer checklists, go-live. Merchant portal and proposals. Refund and cancel tickets. Merchant support. Executes a block when André Silva orders it.

**Taina Chaves** · Treasury Analyst · taina.chaves@sambapay.tech
Money out after reconciliation: payouts and remittances to PaySecure. Rolling reserve tracking and releases. The on-ramp: same-day PIX to the OTC desk, USDC into our wallet, USDC to PaySecure, cost tracked against PTAX.

**Rafaela Brito** · Finance Operations Analyst · rafaela.brito@sambapay.tech
Collections, boletos, due dates, acquirer payables and acquirer portal users. Instruments and statements: ClickSign, bank statements, acquirer administration packs. Purchases, including the five Android phones (operational phones for hiring).

**Abner Maioralli** · Head of Partner Enablement · abner.maioralli@sambapay.tech
Partner signup: getting SambaPay signed up and live on new acquirers directly connected to the central bank. The production of each new integration, whatever it takes, from first contact to first live transaction: requirements, document packs, contracts, credentials, MIDs, go-live. The metrics of that pipeline, reported weekly.

## Reporting lines

Leandro, Thiago, Sheila and Abner report to André Silva. Clayton, Taina and Rafaela report to Thiago.

## Who to call

- Money out, remittance, FX, reserve → Taina
- Collections, payables, statements, admin packs → Rafaela
- A new merchant, a refund or cancel, merchant support → Clayton
- Engine, new processor, integration code, a charge that cannot be built → Leandro
- A new acquirer to sign, its requirements, its go-live, the signup metrics → Abner
- The day's number, a dispute, credit, keys, an incident → Thiago
- A letter from an acquirer, Visa, Mastercard or a regulator; a compliance question → Sheila
- Stop a merchant, hold funds, a decision on price, London → André Silva

## Processes with no owner yet

Factoring (all volume anticipated at a competitive price; nobody sells it). Website Factory commercial side. Brazilian / 2D acquirer restart, until its path is decided. Say so if you want one.

## Outside the eight

Hansraj (PaySecure) confirms our reconciliation every day. Govinda (PaySecure) is on the same thread. The weekly pulse and monthly pack go to Sridhar (Sri Amit), viktoria@paysecure.net and Hansraj. Open: Sridhar's email.
