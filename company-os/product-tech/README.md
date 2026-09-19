# Product and technology

Purpose: the payment engine, the acquirer integrations, the Website Factory.
Owner: Leandro. Operating desk and secrets: Thiago.
Cadence: integrations register updated on every change; incidents reported the hour they appear.
Registers: `integrations.md`.

## What we run

- Payment engine in code: processors, authorisation, tokenisation, 3DS, acquirer performance, Chargeback API.
- Merchant portal: onboarding, KYB, proposals (Clayton operates).
- Operating desk: queues, credit, identity, custody, Key Vault.
- Stack named in internal PCI documentation (verify what is live for SambaPay): Azure Container Apps, PostgreSQL Flexible Server, Redis, Key Vault; Cloudflare WAF; Netlify-hosted checkout page; AWS Cognito SSO; CyberSource tokenisation; Braspag 3DS.

## Website Factory (objective 3)

- Template-based storefronts for cross-border merchants and online-service players; our checkout embedded; merchant runs fulfilment (post office for now).
- Build owner: Leandro (D4). Commercial owner: Open. Success: SimilarWeb and online page validators read every storefront as genuine, high-quality ("top A").

## Acceptance criterion for any new rail (objective 5)

Processes 3DS and 2D card traffic originated in Europe and the United States; accepts international BINs; settles on a documented window; passes the KYB and PCI requirements of the acquirer.

## Horizontal scaling (objective 1 and beyond)

Volume grows by integrating several acquirers per market side by side, never by depending on one. DD2, the secondary entity template in Brazil built on Double Diamond's requirements, starts with three acquirers and two OTC partners. Every new market repeats the pattern: entity, then several rails, then merchants spread across them. The engine routes each transaction to the rail with the best approval at the best cost.

## Open

Partner MoR is Cielo; Double Diamond fee and date; which stack components are live; Website Factory commercial owner; Factoring process owner (internal, P29).
