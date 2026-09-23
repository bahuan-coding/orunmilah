#!/usr/bin/env python3
"""SambaPay payroll register — September 2026.

Single source for the historical ledger, the print HTML, and the PDF.
Numbers are locked: do not invent. Convert each BRL line ÷ PTAX, two decimals, half-up.
"""
from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
PTAX = Decimal("5.1117")
TWOPLACES = Decimal("0.01")
REGISTER = "SP-PAY-2026-09"
COMPETENCIA = "September 2026"
ISSUED = "22 September 2026"
FX_WHEN = "21 Sep 2026 13:06:51 BRT"
FX_SOURCE = "BCB Olinda, PTAX venda"


def D(x) -> Decimal:
    return x if isinstance(x, Decimal) else Decimal(str(x))


def q(x: Decimal) -> Decimal:
    return D(x).quantize(TWOPLACES, rounding=ROUND_HALF_UP)


def to_usdt(brl: Decimal) -> Decimal:
    return q(D(brl) / PTAX)


def brl_from_usd(usd: Decimal) -> Decimal:
    return q(D(usd) * PTAX)


def money(x: Decimal) -> str:
    sign = "-" if x < 0 else ""
    n = f"{abs(x):,.2f}"
    return sign + n


# ---------------------------------------------------------------------------
# Locked lines
# ---------------------------------------------------------------------------

SALARIES = [
    {"id": "S-01", "person": "André Silva", "title": "", "rail": "USDT · PJ",
     "what": "Monthly PJ", "brl": D("49500.00"), "status": "Pay",
     "source": "Quarto Aditivo, 1 Jul 2022, ClickSign 48cffc4a. CNPJ 22.774.002/0001-70. Fixed monthly R$ 49,500.00. HR sheet later notes a May 2023 figure of 44,550 and the Jackpot NFS-e was 44,500.00 (CNPJ 53.854.987/0001-78). No signed reduction was in Drive. This send pays the signed contract."},
    {"id": "S-02", "person": "Thiago Silvestre da Silva", "title": "Head of Operations", "rail": "USDT · PJ",
     "what": "Monthly PJ", "brl": D("25000.00"), "status": "Pay",
     "source": "On the team. Not Thiago Alexandre de Carvalho. HR Ativo; NFS-e SP exact 25,000.00, CNPJ 43.376.279/0001-15"},
    {"id": "S-03", "person": "Leandro Silva", "title": "Head of Engineering and Product", "rail": "USDT · PJ",
     "what": "Monthly PJ", "brl": D("25000.00"), "status": "Pay",
     "source": "Signed contract, 14 Feb 2022, ClickSign 7be4795e. CNPJ 45.162.235/0001-18. Clause 5.1: February 2022 R$ 14,166.66, then from March 2022 a fixed monthly R$ 25,000.00. HR sheet and earlier NFS-e notes used 23,000.00. This send pays the signed contract."},
    {"id": "S-04", "person": "Sheila Esmeralda", "title": "Compliance Officer", "rail": "USDT · PJ",
     "what": "Monthly PJ", "brl": D("24225.26"), "status": "Pay",
     "source": "Lince Assessoria, CNPJ 63.306.290/0001-16. Signed contract 23 Oct 2025, ClickSign 2082b1e3, clause 2.1, monthly R$ 24,225.26. Clause 2.7: taxes are inside that figure. NFS-e 2 of 28 Nov 2025 is the same 24,225.26. Later NFS-e, including September 12+13 (12,205.94 + 12,205.93 = 24,411.87), add 186.61. Do not pay 24,411.87. The unsigned draft of 31 Oct 2025 said 23,000.00. This send pays the signed contract."},
    {"id": "S-05", "person": "Taina Chaves", "title": "Treasury Analyst", "rail": "USDT · CLT",
     "what": "Gross salary", "brl": D("3500.00"), "status": "Pay",
     "source": "Do not use Aug líquido 1,866.32. September holerite Open. Convert this line alone."},
    {"id": "S-06", "person": "Taina Chaves", "title": "Treasury Analyst", "rail": "USDT · CLT",
     "what": "Ajuda de custo home office", "brl": D("74.90"), "status": "Pay",
     "source": "Last paper: Execcon Aug 2026. Convert this line alone. Do not convert 3,574.90 as one."},
    {"id": "S-07", "person": "Abner Maioralli", "title": "Head of Partner Enablement", "rail": "USDT · PJ",
     "what": "Monthly PJ", "brl": D("25000.00"), "status": "Pay",
     "source": "No September NF. Last full month: Double Diamond NFS-e 27, 17 Jul 2026, R$ 25,000.00. Aug NFS-e 28 R$ 16,129.03 is an A55 distrato remainder. Do not use it."},
    {"id": "S-08", "person": "Renato Paulino", "title": "", "rail": "USDT · PJ",
     "what": "Monthly PJ", "brl": D("22979.83"), "status": "Pay",
     "source": "Contract of 26 Sep 2025, CNPJ 36.131.256/0001-85, clause 2.1, monthly R$ 22,979.83. HR Ativo, same figure. NFS-e 11 of 27 Aug 2026 matches. The Drive file named Renato Paulino at R$ 10,500.00 is Renato Gomes Almeida da Silva, CNPJ 52.357.369/0001-50, ended 31 Aug 2026. Do not pay 10,500.00 here."},
]

# fx: ptax = BRL ÷ 5.1117; usd_1to1 = USDT is the USD invoice, BRL = USD × PTAX
EXPENSES = [
    {"id": "E-01", "person": "Thiago Silvestre da Silva", "when": "15 Sep 2026, 11:05", "what": "Uber",
     "paid": "Apple Pay", "brl": D("65.99"), "fx": "ptax",
     "receipt": "Receipt_15set.2026_145310.pdf"},
    {"id": "E-02", "person": "Thiago Silvestre da Silva", "when": "16 Sep 2026, 12:49", "what": "Uber",
     "paid": "Apple Pay", "brl": D("62.94"), "fx": "ptax",
     "receipt": "Receipt_16set.2026_165238.pdf"},
    {"id": "E-03", "person": "Thiago Silvestre da Silva", "when": "16 Sep 2026, 17:08", "what": "Uber",
     "paid": "Apple Pay", "brl": D("113.94"), "fx": "ptax",
     "receipt": "Receipt_16set.2026_215653.pdf"},
    {"id": "E-04", "person": "Leandro Silva", "when": "16 Sep 2026, 10:19", "what": "Uber",
     "paid": "Apple Pay", "brl": D("72.98"), "fx": "ptax",
     "receipt": "Receipt_16Sep2026_143205.pdf"},
    {"id": "E-05", "person": "Leandro Silva", "when": "16 Sep 2026, 18:07", "what": "Uber",
     "paid": "Apple Pay", "brl": D("64.98"), "fx": "ptax",
     "receipt": "Receipt_16Sep2026_221824.pdf"},
    {"id": "E-06", "person": "André Silva", "when": "15 Sep 2026", "what": "Uber",
     "paid": "Nubank OFX", "brl": D("92.99"), "fx": "ptax",
     "receipt": "alsilva86 OFX. No PDF. Paper is the card line"},
    {"id": "E-07", "person": "André Silva", "when": "15 Sep 2026", "what": "Uber",
     "paid": "Nubank OFX", "brl": D("53.97"), "fx": "ptax",
     "receipt": "alsilva86 OFX"},
    {"id": "E-08", "person": "André Silva", "when": "16 Sep 2026", "what": "Uber",
     "paid": "Nubank OFX", "brl": D("93.98"), "fx": "ptax",
     "receipt": "alsilva86 OFX"},
    {"id": "E-09", "person": "André Silva", "when": "16 Sep 2026", "what": "Uber",
     "paid": "Nubank OFX", "brl": D("48.99"), "fx": "ptax",
     "receipt": "alsilva86 OFX"},
    {"id": "E-10", "person": "André Silva", "when": "17 Sep 2026", "what": "Uber",
     "paid": "Nubank OFX", "brl": D("45.97"), "fx": "ptax",
     "receipt": "alsilva86 OFX"},
    {"id": "E-11", "person": "André Silva", "when": "18 Sep 2026", "what": "Uber",
     "paid": "Nubank OFX", "brl": D("43.97"), "fx": "ptax",
     "receipt": "alsilva86 OFX"},
    {"id": "E-12", "person": "André Silva", "when": "18 Sep 2026", "what": "Uber",
     "paid": "Nubank OFX", "brl": D("24.20"), "fx": "ptax",
     "receipt": "alsilva86 OFX"},
    {"id": "E-13", "person": "André Silva", "when": "19 Sep 2026", "what": "Uber",
     "paid": "Nubank OFX NuPay", "brl": D("40.99"), "fx": "ptax",
     "receipt": "alsilva86 OFX"},
    {"id": "E-14", "person": "André Silva", "when": "21 Sep 2026", "what": "Uber",
     "paid": "Nubank OFX", "brl": D("31.37"), "fx": "ptax",
     "receipt": "alsilva86 OFX"},
    {"id": "E-16", "person": "Abner Maioralli", "when": "15 Sep 2026, 22:54", "what": "Uber",
     "paid": "Nubank", "brl": D("50.96"), "fx": "ptax", "receipt": "Screenshot 22 Sep. Unstruck lines only"},
    {"id": "E-17", "person": "Abner Maioralli", "when": "15 Sep 2026, 22:42", "what": "Bar e Lanches Estado de Israel",
     "paid": "Nubank", "brl": D("18.00"), "fx": "ptax", "receipt": "Screenshot 22 Sep"},
    {"id": "E-18", "person": "Abner Maioralli", "when": "15 Sep 2026, 17:01", "what": "Pep Comércio",
     "paid": "Nubank", "brl": D("6.30"), "fx": "ptax", "receipt": "Screenshot 22 Sep"},
    {"id": "E-19", "person": "Abner Maioralli", "when": "15 Sep 2026, 15:27", "what": "Uber",
     "paid": "Nubank", "brl": D("81.97"), "fx": "ptax", "receipt": "Screenshot 22 Sep"},
    {"id": "E-20", "person": "Abner Maioralli", "when": "16 Sep 2026, 20:36", "what": "Uber",
     "paid": "Nubank", "brl": D("51.96"), "fx": "ptax", "receipt": "Screenshot 22 Sep"},
    {"id": "E-21", "person": "Abner Maioralli", "when": "16 Sep 2026, 08:36", "what": "Uber",
     "paid": "Nubank", "brl": D("103.98"), "fx": "ptax", "receipt": "Screenshot 22 Sep"},
    {"id": "E-22", "person": "Abner Maioralli", "when": "17 Sep 2026, 22:37", "what": "Uber",
     "paid": "Nubank", "brl": D("65.98"), "fx": "ptax", "receipt": "Screenshot 22 Sep"},
    {"id": "E-23", "person": "Abner Maioralli", "when": "17 Sep 2026, 18:52", "what": "Beco 74 Gourmet",
     "paid": "Nubank", "brl": D("46.00"), "fx": "ptax", "receipt": "Screenshot 22 Sep"},
    {"id": "E-24", "person": "Abner Maioralli", "when": "17 Sep 2026, 18:17", "what": "Beco 74 Gourmet",
     "paid": "Nubank", "brl": D("36.00"), "fx": "ptax", "receipt": "Screenshot 22 Sep"},
    {"id": "E-25", "person": "Abner Maioralli", "when": "17 Sep 2026, 10:23", "what": "Uber",
     "paid": "Nubank", "brl": D("57.94"), "fx": "ptax", "receipt": "Screenshot 22 Sep"},
    {"id": "E-26", "person": "Abner Maioralli", "when": "19 Sep 2026, 16:10", "what": "Park e Vem Estacionamentos",
     "paid": "Nubank", "brl": D("135.00"), "fx": "ptax", "receipt": "Screenshot 22 Sep"},
    {"id": "E-27", "person": "Abner Maioralli", "when": "19 Sep 2026, 13:46", "what": "Claudineiasantana",
     "paid": "Nubank", "brl": D("39.00"), "fx": "ptax", "receipt": "Screenshot 22 Sep"},
    {"id": "E-28", "person": "Abner Maioralli", "when": "19 Sep 2026, 11:14", "what": "OXXO",
     "paid": "Nubank", "brl": D("51.47"), "fx": "ptax", "receipt": "Screenshot 22 Sep"},
    {"id": "E-29", "person": "Abner Maioralli", "when": "21 Sep 2026, 18:37", "what": "Rede Automan posto",
     "paid": "Nubank", "brl": D("8.40"), "fx": "ptax", "receipt": "Screenshot 22 Sep"},
    {"id": "E-30", "person": "Abner Maioralli", "when": "21 Sep 2026, 17:56", "what": "Autopass Tmob",
     "paid": "Nubank débito", "brl": D("5.40"), "fx": "ptax", "receipt": "Screenshot 22 Sep"},
    {"id": "E-31", "person": "Abner Maioralli", "when": "21 Sep 2026, 17:36", "what": "Mp Digitalsantac",
     "paid": "Nubank", "brl": D("3.50"), "fx": "ptax", "receipt": "Screenshot 22 Sep"},
    {"id": "E-32", "person": "Abner Maioralli", "when": "21 Sep 2026, 10:27", "what": "Epar Estacionamentos",
     "paid": "Nubank", "brl": D("22.00"), "fx": "ptax", "receipt": "Screenshot 22 Sep"},
    {"id": "E-34", "person": "André Silva", "when": "18 Sep 2026", "what": "GoDaddy · sambapay.tech 1 year",
     "paid": "GoDaddy order 4187560192", "brl": D("52.25"), "fx": "ptax",
     "receipt": "Receipt to andrebahuann@gmail.com. Tax R$ 0.00. Auto-renew 18/09/2027 at R$ 502.51 is next year, not this send"},
    {"id": "E-35", "person": "André Silva", "when": "18 Sep 2026", "what": "GoDaddy · sambapay.co 1 year",
     "paid": "GoDaddy order 4172849253", "brl": D("99.99"), "fx": "ptax",
     "receipt": "Receipt to andrebahuann@gmail.com. Tax R$ 0.00"},
    {"id": "E-36", "person": "André Silva", "when": "18 Sep 2026", "what": "Airbnb Hm9y4rs29a",
     "paid": "Nubank", "brl": D("174.70"), "fx": "ptax",
     "receipt": "Posted 18 Sep. Hansraj stay. OFX alsilva86"},
    {"id": "E-37", "person": "André Silva", "when": "7 Sep 2026", "what": "OpenCode · AI",
     "paid": "Stripe MC 3724", "brl": D("57.43"), "fx": "charged_brl",
     "receipt": "Receipt 2997-7038, invoice 5VB97UEZ-0002. Charged R$ 57.43 at 5.3326. USDT from charged BRL, not the USD list price"},
    {"id": "E-38", "person": "André Silva", "when": "9 Sep 2026", "what": "OpenCode · AI",
     "paid": "Stripe MC 9369", "brl": D("84.91"), "fx": "charged_brl",
     "receipt": "Receipt 2505-8302, invoice 5VB97UEZ-0003. Charged R$ 84.91 at 5.3067"},
    {"id": "E-39", "person": "André Silva", "when": "10 Sep 2026", "what": "OpenCode · AI",
     "paid": "Nubank memo Opencode", "brl": D("87.85"), "fx": "charged_brl",
     "receipt": "OFX alsilva86. IOF 3.07 posted and reversed. Third cash-out"},
    {"id": "E-40", "person": "André Silva", "when": "1 Sep 2026", "what": "Railway · Website Factory",
     "paid": "Stripe MC 3724", "usd": D("7.37"), "fx": "usd_1to1",
     "receipt": "Receipt 2401-5497, invoice 0BZKAFCA-0003. Paid $7.37. BRL = USD × PTAX"},
    {"id": "E-41", "person": "André Silva", "when": "16 Sep 2026", "what": "Railway · Website Factory",
     "paid": "Stripe MC 3724", "usd": D("20.00"), "fx": "usd_1to1",
     "receipt": "Receipt 2258-4724, invoice 0BZKAFCA-0004. Paid $20.00"},
    {"id": "E-42", "person": "André Silva", "when": "17 Sep 2026", "what": "Vercel · Website Factory",
     "paid": "Stripe MC 3724", "usd": D("40.00"), "fx": "usd_1to1",
     "receipt": "Receipt 2595-4913, invoice UN5DFCHZ-0010. Paid $40.00 (Pro + seat)"},
    {"id": "E-43", "person": "André Silva", "when": "13 Sep 2026 due", "what": "Netlify · Website Factory",
     "paid": "Invoice GRUZTS-00021", "usd": D("57.00"), "fx": "usd_1to1",
     "receipt": "Payment failed 22 Sep. $57.00. Cash has not left the card. On this send so the vendor is paid from USDT"},
    {"id": "E-44", "person": "André Silva", "when": "1 Sep 2026 due", "what": "Neon · Website Factory",
     "paid": "Invoice ADLQXA-00009", "usd": D("104.23"), "fx": "usd_1to1",
     "receipt": "Payment failed. $104.23 Launch Plan. Bill to JACKPOT B D P LTDA. On this send because it is company"},
    {"id": "E-45", "person": "Taina Chaves", "when": "Aug 2026 competência (last paper)",
     "what": "Seguro de saúde · SulAmérica Clássico",
     "paid": "Keep Lives / Consultoria 8NWBW", "brl": D("1055.19"), "fx": "ptax",
     "receipt": "Titular only. Carteirinha 88888495862880014. Espelho 08/2026 R$ 1,055.19. Company pays; August holerite has no health discount. September fatura Open — use last paper so the month is not short"},
]

EXPECTED_USDT = {
    "S-01": D("9683.67"), "S-02": D("4890.74"), "S-03": D("4890.74"),
    "S-04": D("4739.18"), "S-05": D("684.70"), "S-06": D("14.65"),
    "S-07": D("4890.74"), "S-08": D("4495.54"),
    "E-01": D("12.91"), "E-02": D("12.31"), "E-03": D("22.29"),
    "E-04": D("14.28"), "E-05": D("12.71"),
    "E-06": D("18.19"), "E-07": D("10.56"), "E-08": D("18.39"), "E-09": D("9.58"),
    "E-10": D("8.99"), "E-11": D("8.60"), "E-12": D("4.73"), "E-13": D("8.02"), "E-14": D("6.14"),
    "E-16": D("9.97"), "E-17": D("3.52"), "E-18": D("1.23"), "E-19": D("16.04"),
    "E-20": D("10.16"), "E-21": D("20.34"), "E-22": D("12.91"), "E-23": D("9.00"),
    "E-24": D("7.04"), "E-25": D("11.33"), "E-26": D("26.41"), "E-27": D("7.63"),
    "E-28": D("10.07"), "E-29": D("1.64"), "E-30": D("1.06"), "E-31": D("0.68"), "E-32": D("4.30"),
    "E-34": D("10.22"), "E-35": D("19.56"), "E-36": D("34.18"),
    "E-37": D("11.24"), "E-38": D("16.61"), "E-39": D("17.19"),
    "E-40": D("7.37"), "E-41": D("20.00"), "E-42": D("40.00"), "E-43": D("57.00"), "E-44": D("104.23"),
    "E-45": D("206.43"),
}

PERSON_EXPECTED = {
    "André Silva": (D("51702.09"), D("10114.47")),
    "Thiago Silvestre da Silva": (D("25242.87"), D("4938.25")),
    "Leandro Silva": (D("25137.96"), D("4917.73")),
    "Sheila Esmeralda": (D("24225.26"), D("4739.18")),
    "Taina Chaves": (D("4630.09"), D("905.78")),
    "Abner Maioralli": (D("25783.86"), D("5044.07")),
    "Renato Paulino": (D("22979.83"), D("4495.54")),
}

EXPENSE_PERSON_EXPECTED = {
    "Thiago Silvestre da Silva": (D("242.87"), D("47.51")),
    "Leandro Silva": (D("137.96"), D("26.99")),
    "Abner Maioralli": (D("783.86"), D("153.33")),
    "André Silva": (D("2202.09"), D("430.80")),
    "Taina Chaves": (D("1055.19"), D("206.43")),
}

TITLES = {
    "André Silva": "",
    "Thiago Silvestre da Silva": "Head of Operations",
    "Leandro Silva": "Head of Engineering and Product",
    "Sheila Esmeralda": "Compliance Officer",
    "Taina Chaves": "Treasury Analyst",
    "Abner Maioralli": "Head of Partner Enablement",
    "Renato Paulino": "",  # not in people README; follows Finnera
    "Clayton Lira": "Merchant Operations Analyst",
    "Rafaela Brito": "Finance Operations Analyst",
}

ACTIVITY = {
    "André Silva": "Direction; PaySecure and London; acquirer and desk relationships",
    "Thiago Silvestre da Silva": "Daily reconciliation; queues; Key Vault; disputes",
    "Leandro Silva": "Payment engine; white-label integrations; Website Factory",
    "Sheila Esmeralda": "On leave. Contract in force. Leave is not exclusion",
    "Taina Chaves": "Payouts, remittances, rolling reserve, on-ramp",
    "Abner Maioralli": "Partner signup on acquirers. Working this month",
    "Renato Paulino": "Follows Finnera. No September NF. Contract price",
}

HEALTH = [
    {"person": "André Silva", "plan": "Yes. 8NWVA Especial 100. 4 lives",
     "premium": D("5049.09"), "nd": D("0.00"), "remuneration": D("49500.00"),
     "all_in": D("54549.09"), "this_send": D("49500.00"), "on_file": True,
     "how": "No ND. Company paid the premium on the grouped boleto. Do not add 5,049.09 to USDT. Salary on this send is the signed contract, 49,500.00"},
    {"person": "Thiago Silvestre da Silva", "plan": "Yes. 8QOFP Especial 100. Titular. CNPJ 43.376.279/0001-15",
     "premium": D("1512.80"), "nd": D("203.09"), "remuneration": D("25000.00"),
     "all_in": D("26309.71"), "this_send": D("25000.00"), "on_file": True,
     "how": "On the team. ND 203.09 is a discount from PIX. Company net 1,309.71. Do not add the premium to USDT. Not Thiago Alexandre de Carvalho"},
    {"person": "Leandro Silva", "plan": "Yes. 8TU63 Clássico. Titular",
     "premium": D("1129.06"), "nd": D("0.00"), "remuneration": D("25000.00"),
     "all_in": D("26129.06"), "this_send": D("25000.00"), "on_file": True,
     "how": "No ND. Do not add 1,129.06 to USDT. Salary on this send is the signed contract, 25,000.00"},
    {"person": "Sheila Esmeralda", "plan": "Yes. 8NWBW Especial 100. 3 lives",
     "premium": D("3283.83"), "nd": D("1974.13"), "remuneration": D("24225.26"),
     "all_in": D("24225.26"), "this_send": D("24225.26"), "on_file": True,
     "how": "Salary is the signed contract, 24,225.26. Taxes are inside that figure. Do not pay the NFS-e sum 24,411.87. Do not add 3,283.83. ND 1,974.13 is a PIX discount only after Taina issues the September ND"},
    {"person": "Taina Chaves", "plan": "Yes. 8NWBW Clássico. Titular. Carteirinha 88888495862880014",
     "premium": D("1055.19"), "nd": D("0.00"), "remuneration": D("3574.90"),
     "all_in": D("4630.09"), "this_send": D("4630.09"), "on_file": True,
     "how": "Company pays. No holerite discount. Pay the three lines on this send so the month is not short"},
    {"person": "Clayton Lira", "plan": "Yes. 8NWBW Clássico. Titular. SCD",
     "premium": D("766.63"), "nd": D("0.00"), "remuneration": D("4074.90"),
     "all_in": D("4841.53"), "this_send": D("0.00"), "on_file": False,
     "how": "Employee of the SCD. Consultoria Execcon. Not this USDT file"},
    {"person": "Rafaela Brito", "plan": "Yes. 8NWBW Clássico. Titular",
     "premium": D("1055.19"), "nd": D("0.00"), "remuneration": D("5576.00"),
     "all_in": None, "this_send": D("0.00"), "on_file": False,
     "how": "Not a payee of this file. Maternity then férias on Execcon"},
    {"person": "Abner Maioralli", "plan": "No",
     "premium": None, "nd": None, "remuneration": D("25000.00"),
     "all_in": D("25000.00"), "this_send": D("25000.00"), "on_file": True,
     "how": "Not on the August mirror. Salary is on this send. Do not add a premium"},
    {"person": "Renato Paulino", "plan": "No. The Renato on the mirror is Renato Gomes Almeida da Silva",
     "premium": None, "nd": None, "remuneration": D("22979.83"),
     "all_in": D("22979.83"), "this_send": D("22979.83"), "on_file": True,
     "how": "Salary is the Sep 2025 contract, R$ 22,979.83. Gomes at R$ 10,500.00 ended 31 Aug 2026 and is not this file"},
]


def settle_line(row: dict) -> dict:
    out = dict(row)
    fx = row.get("fx", "ptax")
    if fx == "usd_1to1":
        usd = D(row["usd"])
        out["brl"] = brl_from_usd(usd)
        out["usdt"] = q(usd)
    else:
        out["brl"] = q(D(row["brl"]))
        out["usdt"] = to_usdt(out["brl"])
    return out


def dec_default(o):
    if isinstance(o, Decimal):
        return f"{o:.2f}"
    raise TypeError(type(o))


def build_ledger() -> dict:
    salaries = []
    for row in SALARIES:
        r = dict(row)
        r["brl"] = q(D(r["brl"]))
        r["usdt"] = to_usdt(r["brl"])
        exp = EXPECTED_USDT[r["id"]]
        if r["usdt"] != exp:
            raise SystemExit(f"{r['id']} USDT {r['usdt']} != locked {exp}")
        salaries.append(r)

    expenses = []
    for row in EXPENSES:
        r = settle_line(row)
        exp = EXPECTED_USDT[r["id"]]
        if r["usdt"] != exp:
            raise SystemExit(f"{r['id']} USDT {r['usdt']} != locked {exp} (brl={r['brl']})")
        if r["id"] in ("E-40", "E-41", "E-42", "E-43", "E-44"):
            # BRL must match locked charged-from-USD
            pass
        expenses.append(r)

    # Locked BRL for USD×PTAX lines
    locked_brl = {
        "E-40": D("37.67"), "E-41": D("102.23"), "E-42": D("204.47"),
        "E-43": D("291.37"), "E-44": D("532.79"),
    }
    for r in expenses:
        if r["id"] in locked_brl and r["brl"] != locked_brl[r["id"]]:
            raise SystemExit(f"{r['id']} BRL {r['brl']} != locked {locked_brl[r['id']]}")

    sal_brl = q(sum(r["brl"] for r in salaries))
    sal_usdt = q(sum(r["usdt"] for r in salaries))
    exp_brl = q(sum(r["brl"] for r in expenses))
    exp_usdt = q(sum(r["usdt"] for r in expenses))
    send_brl = q(sal_brl + exp_brl)
    send_usdt = q(sal_usdt + exp_usdt)

    if sal_brl != D("175279.99") or sal_usdt != D("34289.96"):
        raise SystemExit(f"salaries {sal_brl}/{sal_usdt}")
    if exp_brl != D("4421.97") or exp_usdt != D("865.06"):
        raise SystemExit(f"expenses {exp_brl}/{exp_usdt}")
    if send_brl != D("179701.96") or send_usdt != D("35155.02"):
        raise SystemExit(f"send {send_brl}/{send_usdt}")

    by_person = {}
    for r in salaries + expenses:
        p = by_person.setdefault(r["person"], {"brl": Decimal("0"), "usdt": Decimal("0"), "lines": []})
        p["brl"] = q(p["brl"] + r["brl"])
        p["usdt"] = q(p["usdt"] + r["usdt"])
        p["lines"].append(r["id"])

    order = ["André Silva", "Thiago Silvestre da Silva", "Leandro Silva", "Sheila Esmeralda",
             "Taina Chaves", "Abner Maioralli", "Renato Paulino"]
    person_rows = []
    for name in order:
        brl, usdt = by_person[name]["brl"], by_person[name]["usdt"]
        exp_b, exp_u = PERSON_EXPECTED[name]
        if brl != exp_b or usdt != exp_u:
            raise SystemExit(f"{name} {brl}/{usdt} != {exp_b}/{exp_u}")
        person_rows.append({
            "person": name,
            "title": TITLES[name],
            "activity": ACTIVITY[name],
            "brl": brl,
            "usdt": usdt,
            "line_ids": by_person[name]["lines"],
        })

    exp_by = {}
    for r in expenses:
        p = exp_by.setdefault(r["person"], {"brl": Decimal("0"), "usdt": Decimal("0")})
        p["brl"] = q(p["brl"] + r["brl"])
        p["usdt"] = q(p["usdt"] + r["usdt"])
    for name, (eb, eu) in EXPENSE_PERSON_EXPECTED.items():
        if exp_by[name]["brl"] != eb or exp_by[name]["usdt"] != eu:
            raise SystemExit(f"exp {name} {exp_by[name]} != {eb}/{eu}")

    taina = by_person["Taina Chaves"]
    if taina["brl"] != D("4630.09") or taina["usdt"] != D("905.78"):
        raise SystemExit("Taina this send")

    payload = {
        "register": REGISTER,
        "company": "SambaPay",
        "competencia": COMPETENCIA,
        "issued": ISSUED,
        "status": "Open",
        "status_note": "Further expense receipts may land. Send now stays locked until a new paper is added to pay-request.md.",
        "rail": "USDT",
        "rail_note": "1 USDT = 1 USD for this conversion only. USDT is not USDC.",
        "fx": {
            "rate": "5.1117",
            "quote": "BRL per USD",
            "side": "PTAX venda",
            "when": FX_WHEN,
            "source": FX_SOURCE,
            "rounding": "each line BRL ÷ 5.1117, two decimals, half-up; then sum",
        },
        "money_out": {"name": "Hansraj", "role": "our operator"},
        "locks": {"name": "André Silva"},
        "instruction": "company-os/finance/pay-request.md",
        "labour": "company-os/finance/payroll-run.md",
        "not_this_file": [
            {"person": "Thiago Alexandre de Carvalho", "title": "",
             "why": "Not on the team. Contract terminated 31 Oct 2025, CNPJ 39.803.563/0001-53. Do not pay."},
            {"person": "Clayton Lira", "title": "Merchant Operations Analyst",
             "why": "Employee of the SCD. Stays on Consultoria Execcon until he leaves the SCD. Gross 4,000.00 + home office 74.90 + SulAmérica 766.63 stay on that rail."},
            {"person": "Rafaela Brito", "title": "Finance Operations Analyst",
             "why": "Not a payee of this file. Maternity 1–22 Sep then férias 23 Sep–22 Oct on Execcon."},
            {"person": "Renato Gomes Almeida da Silva", "title": "",
             "why": "Ended 31 Aug 2026. Contract R$ 10,500.00, CNPJ 52.357.369/0001-50. A Drive file is misnamed Renato Paulino. He is not Renato Paulino and he is not this file."},
        ],
        "hold": [
            "Zoho Mail (sambapay.tech mailboxes): account exists, zero invoice, do not invent a price",
            "Taina September holerite net still Open; this file pays gross + home office + health so she is not short",
            "September SulAmérica fatura: portal mail 21 Sep, amount not in the HTML, ND 09 not issued",
        ],
        "totals": {
            "salaries_brl": sal_brl,
            "salaries_usdt": sal_usdt,
            "expenses_brl": exp_brl,
            "expenses_usdt": exp_usdt,
            "send_brl": send_brl,
            "send_usdt": send_usdt,
        },
        "by_person": person_rows,
        "salaries": salaries,
        "expenses": expenses,
        "health": HEALTH,
        "grouped_health_boleto": {
            "brl": D("33588.06"),
            "paid_on": "8 Sep 2026",
            "who_paid": "Consultoria",
            "paper": "Pagamentos Set.xlsx + Keep Lives fatura unificada 08/2026",
            "note": "Already left Consultoria. Do not send the same premium again as USDT except Taina.",
        },
    }

    canonical = json.dumps(payload, default=dec_default, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    payload["ledger_sha256"] = digest
    payload["ledger_sha256_short"] = digest[:12]
    payload["built_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return payload


def esc(s: str) -> str:
    s = (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;"))
    return s.replace("NFS-e", "NFS&#8209;e")


def running(section: str, ledger: dict) -> str:
    return f'''<div class="running">
      <div class="left">SambaPay · Payroll</div>
      <div class="right">{esc(section)} · {REGISTER} · {ledger["ledger_sha256_short"]}</div>
    </div>
    <div class="gold-rule"></div>'''


def foot(page: str) -> str:
    return f'''<div class="foot">
      <span>Board view · never in the Welcome Kit</span>
      <span>{esc(page)} · {COMPETENCIA}</span>
    </div>'''


def render_html(ledger: dict) -> str:
    css = (HERE / "payroll.css").read_text(encoding="utf-8")
    t = ledger["totals"]
    send_usdt = money(t["send_usdt"])
    send_brl = money(t["send_brl"])
    sha = ledger["ledger_sha256_short"]

    sal_b, sal_u, exp_b, exp_u = {}, {}, {}, {}
    for r in ledger["salaries"]:
        sal_b[r["person"]] = q(sal_b.get(r["person"], Decimal("0")) + r["brl"])
        sal_u[r["person"]] = q(sal_u.get(r["person"], Decimal("0")) + r["usdt"])
    for r in ledger["expenses"]:
        exp_b[r["person"]] = q(exp_b.get(r["person"], Decimal("0")) + r["brl"])
        exp_u[r["person"]] = q(exp_u.get(r["person"], Decimal("0")) + r["usdt"])

    roster_rows = []
    for i, p in enumerate(ledger["by_person"], 1):
        title = p["title"] or ("Open" if p["person"] == "Renato Paulino" else "—")
        name = p["person"]
        sb, eb = sal_b.get(name, Decimal("0")), exp_b.get(name, Decimal("0"))
        roster_rows.append(f'''<tr>
          <td class="muted">{i:02d}</td>
          <td><div class="person">{esc(name)}</div><div class="title">{esc(title)}</div></td>
          <td class="num">{money(sb)}</td>
          <td class="num">{money(eb)}</td>
          <td class="num">{money(p["brl"])}</td>
          <td class="num usdt">{money(p["usdt"])}</td>
        </tr>''')
    roster_rows.append(f'''<tr class="total">
          <td></td><td>Send now · seven payees</td>
          <td class="num">{money(t["salaries_brl"])}</td>
          <td class="num">{money(t["expenses_brl"])}</td>
          <td class="num">{send_brl}</td>
          <td class="num usdt">{send_usdt}</td>
        </tr>''')

    salary_note = {
        "S-01": "Signed contract, 1 Jul 2022 · CNPJ 22.774.002/0001-70",
        "S-02": "On the team · CNPJ 43.376.279/0001-15",
        "S-03": "Signed contract, from Mar 2022 · CNPJ 45.162.235/0001-18",
        "S-04": "Lince · clause 2.1 · CNPJ 63.306.290/0001-16",
        "S-05": "Gross. September holerite still open",
        "S-06": "Home office · last paper Aug 2026",
        "S-07": "No September NF · last full month Jul 2026",
        "S-08": "Contract 26 Sep 2025 · CNPJ 36.131.256/0001-85",
    }
    sal_rows = []
    for r in ledger["salaries"]:
        title = r["title"] or "—"
        sal_rows.append(f'''<tr>
          <td class="muted">{esc(r["id"])}</td>
          <td><span class="tick"></span>{esc(r["person"])}<div class="title">{esc(title)} · {esc(r["rail"])}</div></td>
          <td>{esc(r["what"])}<div class="note">{esc(salary_note[r["id"]])}</div></td>
          <td class="num">{money(r["brl"])}</td>
          <td class="num usdt">{money(r["usdt"])}</td>
        </tr>''')
    sal_rows.append(f'''<tr class="total">
          <td></td><td colspan="2">Salaries on this remittance</td>
          <td class="num">{money(t["salaries_brl"])}</td>
          <td class="num usdt">{money(t["salaries_usdt"])}</td>
        </tr>''')

    by_id = {r["id"]: r for r in ledger["expenses"]}

    def bunch(ids: list[str]) -> tuple[Decimal, Decimal]:
        rows = [by_id[i] for i in ids]
        return q(sum((r["brl"] for r in rows), Decimal("0"))), q(sum((r["usdt"] for r in rows), Decimal("0")))

    # Print groups. Ledger keeps every receipt. USDT is the sum of the lines, not a fresh conversion of the bundle.
    print_groups = [
        ("Transport", [
            ("André Silva", "Uber · 9 trips · 15–21 Sep", ["E-06", "E-07", "E-08", "E-09", "E-10", "E-11", "E-12", "E-13", "E-14"]),
            ("Thiago Silvestre da Silva", "Uber · 3 trips · 15–16 Sep", ["E-01", "E-02", "E-03"]),
            ("Leandro Silva", "Uber · 2 trips · 16 Sep", ["E-04", "E-05"]),
            ("Abner Maioralli", "Uber · 6 trips · 15–17 Sep", ["E-16", "E-19", "E-20", "E-21", "E-22", "E-25"]),
        ]),
        ("Card", [
            ("Abner Maioralli", "Meals, parking and local spend · unstruck", ["E-17", "E-18", "E-23", "E-24", "E-26", "E-27", "E-28", "E-29", "E-30", "E-31", "E-32"]),
        ]),
        ("Domains", [
            ("André Silva", "sambapay.tech and sambapay.co · 18 Sep", ["E-34", "E-35"]),
        ]),
        ("Lodging", [
            ("André Silva", "Airbnb · Hansraj · instalment 1 of 6", ["E-36"]),
        ]),
        ("AI", [
            ("André Silva", "OpenCode · three September charges", ["E-37", "E-38", "E-39"]),
        ]),
        ("Hosting", [
            ("André Silva", "Railway · two invoices, paid", ["E-40", "E-41"]),
            ("André Silva", "Vercel · paid", ["E-42"]),
            ("André Silva", "Netlify · invoice unpaid", ["E-43"]),
            ("André Silva", "Neon · invoice unpaid", ["E-44"]),
        ]),
        ("Health", [
            ("Taina Chaves", "SulAmérica Clássico · last paper Aug 2026", ["E-45"]),
        ]),
    ]
    exp_rows = []
    grouped_brl = Decimal("0")
    grouped_usdt = Decimal("0")
    andre_ids = []
    for category, lines in print_groups:
        exp_rows.append(f'''<tr class="group"><td colspan="4">{esc(category)}</td></tr>''')
        for who, detail, ids in lines:
            brl, usdt = bunch(ids)
            grouped_brl = q(grouped_brl + brl)
            grouped_usdt = q(grouped_usdt + usdt)
            if who == "André Silva":
                andre_ids.extend(ids)
            exp_rows.append(f'''<tr>
              <td>{esc(who)}</td>
              <td>{esc(detail)}</td>
              <td class="num">{money(brl)}</td>
              <td class="num usdt">{money(usdt)}</td>
            </tr>''')
    if grouped_brl != t["expenses_brl"] or grouped_usdt != t["expenses_usdt"]:
        raise SystemExit(f"grouped expenses {grouped_brl}/{grouped_usdt}")
    andre_brl, andre_usdt = bunch(andre_ids)
    if andre_brl != D("2202.09") or andre_usdt != D("430.80"):
        raise SystemExit(f"André expenses {andre_brl}/{andre_usdt}")
    exp_rows.append(f'''<tr class="subtotal">
          <td colspan="2">André Silva · expenses on this send</td>
          <td class="num">{money(andre_brl)}</td>
          <td class="num usdt">{money(andre_usdt)}</td>
        </tr>''')
    exp_rows.append(f'''<tr class="total">
          <td colspan="2">Expenses on this remittance</td>
          <td class="num">{money(t["expenses_brl"])}</td>
          <td class="num usdt">{money(t["expenses_usdt"])}</td>
        </tr>''')

    health_cards = []
    for h in ledger["health"]:
        cls = "in" if h["on_file"] else "out"
        prem = "—" if h["premium"] is None else money(h["premium"])
        nd = "—" if h["nd"] is None else money(h["nd"])
        all_in = "Open" if h["all_in"] is None else money(h["all_in"])
        send = money(h["this_send"]) if h["this_send"] else "—"
        health_cards.append(f'''<div class="health {cls}">
          <div class="who">{esc(h["person"])}</div>
          <div class="meta">{esc(h["plan"])}</div>
          <dl>
            <dt>Premium (prêmio + IOF)</dt><dd>{prem}</dd>
            <dt>ND (PIX discount)</dt><dd>{nd}</dd>
            <dt>All-in company</dt><dd>{all_in}</dd>
            <dt>This USDT send</dt><dd>{send}</dd>
          </dl>
          <p class="tiny">{esc(h["how"])}</p>
        </div>''')

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>SambaPay · Payroll · September 2026 · {REGISTER}</title>
  <style>{css}</style>
</head>
<body>

<section class="cover">
  <div class="cover-bar"></div>
  <div class="cover-gold"></div>
  <div class="watermark">09</div>
  <div class="cover-inner">
    <div class="cover-top">
      <div class="wordmark">SAMBAPAY</div>
      <div class="reg">{REGISTER} · {sha}</div>
    </div>
    <div class="cover-mid">
      <p class="kicker">Payroll</p>
      <h1>September 2026</h1>
      <p class="cover-sub">USDT instruction for Hansraj, our operator, to send. Locked by André Silva. This file is the historical register of the month’s payroll: salaries, grouped expenses, the rate, and who is not on this remittance.</p>
    </div>
    <div class="hero">
      <div class="hero-label">Send now</div>
      <div class="hero-usdt">{send_usdt}</div>
      <div class="hero-unit">USDT</div>
      <div class="hero-brl">R$ {send_brl}</div>
    </div>
    <div class="cover-meta">
      <div><span>FX</span><strong>PTAX 5.1117</strong>21 Sep 2026 · BCB Olinda</div>
      <div><span>Payees</span><strong>Seven people</strong>Clayton and Rafaela wait</div>
      <div><span>Status</span><strong>Open</strong>Further receipts may land</div>
    </div>
  </div>
</section>

<section class="sheet">
  {running("This remittance", ledger)}
  <h2>Who receives this send</h2>
  <p class="lede">Salary is the contract. Expenses sit in their own column. The total is the sum. Convert each underlying line at PTAX 5.1117, two decimals, half-up, then sum.</p>
  <div class="kpis">
    <div class="kpi navy"><div class="l">Send now</div><div class="v">{send_usdt} USDT</div><div class="s">R$ {send_brl}</div></div>
    <div class="kpi"><div class="l">Salaries</div><div class="v">{money(t["salaries_usdt"])} USDT</div><div class="s">R$ {money(t["salaries_brl"])} · six PJ + Taina</div></div>
    <div class="kpi teal"><div class="l">Expenses</div><div class="v">{money(t["expenses_usdt"])} USDT</div><div class="s">R$ {money(t["expenses_brl"])} · grouped · includes Taina health</div></div>
    <div class="kpi gold"><div class="l">Taina this send</div><div class="v">905.78 USDT</div><div class="s">R$ 4,630.09 · salary + home office + health</div></div>
  </div>
  <table>
    <thead>
      <tr>
        <th style="width:8mm">#</th>
        <th>Person</th>
        <th class="num" style="width:28mm">Salary</th>
        <th class="num" style="width:28mm">Expenses</th>
        <th class="num" style="width:28mm">Total BRL</th>
        <th class="num" style="width:26mm">USDT</th>
      </tr>
    </thead>
    <tbody>
      {"".join(roster_rows)}
    </tbody>
  </table>
  <div class="two">
    <div class="card in">
      <h3>How to send</h3>
      <p>USDT to the person who is owed. PJ against this month’s figure. Taina at gross so salary is not short. Abner Maioralli and Renato Paulino are on the salary block. Their September NF has not arrived. Do not pay either of them again in expenses.</p>
    </div>
    <div class="card out">
      <h3>Not this remittance</h3>
      <p><strong>Clayton Lira</strong>, Merchant Operations Analyst — employee of the SCD, Consultoria Execcon, until he leaves the SCD.<br><strong>Rafaela Brito</strong>, Finance Operations Analyst — not a payee of this file. Thiago Alexandre de Carvalho is not on the team.</p>
    </div>
  </div>
  {foot("Roster")}
</section>

<section class="sheet">
  {running("Salaries", ledger)}
  <h2>Salary ledger</h2>
  <p class="lede">Six PJ plus Taina’s September proventos. Tick the box when the USDT has left. André Silva is the signed contract, R$ 49,500.00. Leandro Silva is the signed contract, R$ 25,000.00 from March 2022. Sheila Esmeralda, Lince, is the signed contract, R$ 24,225.26. Renato Paulino is his own contract, R$ 22,979.83. Thiago Silvestre da Silva is on the team.</p>
  <table>
    <thead>
      <tr>
        <th style="width:14mm">Id</th>
        <th style="width:46mm">Person</th>
        <th>Line</th>
        <th class="num" style="width:28mm">BRL</th>
        <th class="num" style="width:26mm">USDT</th>
      </tr>
    </thead>
    <tbody>
      {"".join(sal_rows)}
    </tbody>
  </table>
  <div class="hold">Hold. Zoho Mail for sambapay.tech mailboxes: the account exists, there is zero invoice, do not invent a mailbox price. Clayton Lira 4,000.00 stays on SCD / Execcon. Rafaela Brito is not a payee here.</div>
  <div class="control">
    <div class="card in">
      <h3>Register</h3>
      <dl>
        <dt>Id</dt><dd>{REGISTER}</dd>
        <dt>Issued</dt><dd>{ISSUED}</dd>
        <dt>Competência</dt><dd>{COMPETENCIA}</dd>
        <dt>Status</dt><dd>Open · further receipts may land</dd>
      </dl>
    </div>
    <div class="card in">
      <h3>FX</h3>
      <dl>
        <dt>Rate</dt><dd>5.1117 BRL per USD</dd>
        <dt>Side</dt><dd>PTAX venda · BCB Olinda</dd>
        <dt>When</dt><dd>{FX_WHEN}</dd>
        <dt>Rounding</dt><dd>Each line ÷ 5.1117, two decimals, half-up, then sum</dd>
      </dl>
    </div>
    <div class="card in">
      <h3>Archive</h3>
      <dl>
        <dt>Ledger SHA-256</dt><dd>{ledger["ledger_sha256_short"]} · full digest in ledger.json</dd>
        <dt>Instruction</dt><dd>company-os/finance/pay-request.md</dd>
        <dt>Labour</dt><dd>company-os/finance/payroll-run.md</dd>
        <dt>This file</dt><dd>history/2026-09/</dd>
      </dl>
    </div>
  </div>
  {foot("Salaries")}
</section>

<section class="sheet">
  {running("Expenses", ledger)}
  <h2>Expenses</h2>
  <p class="lede">Grouped for the send. Each USDT figure is the sum of the underlying lines, each converted on its own. Receipt detail stays in the ledger. Netlify and Neon have not left the card; they stay here so Hansraj pays the vendor.</p>
  <table>
    <thead>
      <tr>
        <th style="width:52mm">Person</th>
        <th>What</th>
        <th class="num" style="width:28mm">BRL</th>
        <th class="num" style="width:26mm">USDT</th>
      </tr>
    </thead>
    <tbody>
      {"".join(exp_rows)}
    </tbody>
  </table>
  <div class="hold">André Silva expenses are R$ 2,202.09 / 430.80 USDT. Uber on his card is R$ 476.43. Hosting is R$ 1,168.53, of which Netlify R$ 291.37 and Neon R$ 532.79 are unpaid invoices. Grocery, pharmacy, restaurants, Rd Saúde parcels, and the August tool invoices are not in this figure.</div>
  {foot("Expenses")}
</section>

<section class="sheet">
  {running("Health · all-in", ledger)}
  <h2>Seguro de saúde</h2>
  <p class="lede">Not everyone on sambapay.tech has SulAmérica. Locked from Keep Lives fatura unificada 08/2026 and the grouped boleto R$ 33,588.06 paid 8 Sep 2026 by Consultoria. That cash already left. Do not send the same premium again as USDT to the person, except Taina, whose line is so her month is not short.</p>
  <div class="banner">
    <div>
      <div class="dim">Grouped boleto already paid · 8 Sep 2026</div>
      <div class="big">R$ 33,588.06</div>
    </div>
    <div class="dim">Keep Lives · competência Aug · Consultoria</div>
  </div>
  <div class="health-grid">
    {"".join(health_cards)}
  </div>
  {foot("Health")}
</section>

<section class="sheet">
  {running("Outside this remittance", ledger)}
  <h2>Outside this remittance, and the close</h2>
  <p class="lede">These names belong to SambaPay. They are not payees of this USDT file. Recording them here is the history: so a later reader does not think they were forgotten.</p>
  <div class="two">
    <div class="card out">
      <h3>Thiago Alexandre de Carvalho</h3>
      <p>Not on the team. Contract terminated 31 Oct 2025, CNPJ 39.803.563/0001-53. Do not pay. Thiago Silvestre da Silva is on this send.</p>
    </div>
    <div class="card out">
      <h3>Taina Fraga Chaves · papers</h3>
      <p>CLT from 15 Jun 2026. Analista Financeiro. Gross R$ 3,500.00. Drive folder Taina Fraga Chaves holds CTPS, PIS, CNH, proof of address, voter card, schooling declaration, marriage certificate, ASO, and medical declarations of 5 Aug and 27 Aug 2026. Signed employment contract and the September holerite were not in that folder.</p>
    </div>
  </div>
  <div class="two section-space">
    <div class="card out">
      <h3>Clayton Lira</h3>
      <p>Merchant Operations Analyst. Employee of the SCD. Stays on Consultoria Execcon until he leaves the SCD. Gross R$ 4,000.00 + home office R$ 74.90 + SulAmérica Clássico R$ 766.63 stay on that rail. André Silva locked this on 22 Sep 2026.</p>
    </div>
    <div class="card out">
      <h3>Rafaela Brito</h3>
      <p>Finance Operations Analyst. Not a payee of this file. Maternity 1–22 Sep 2026 then férias 23 Sep–22 Oct 2026 (Execcon recibo 21 Sep; ClickSign closed 22 Sep). SulAmérica Clássico R$ 1,055.19 is on the grouped boleto, not on this USDT.</p>
    </div>
  </div>
  <div class="hold section-space">Not company on this send: Abner struck card lines (Google, iFood, Claro, Apple, Sonda, sushi, pizza, Jurema, one Uber). André grocery, farmácia, restaurants. C6 Carbon closed 25 Aug (R$ 3,095.22). GoDaddy paycubed.co. Zoho Mail. August OpenCode / Anomaly. August Vercel / Railway / Netlify. Rd Saúde parcels.</div>
  <p class="tiny">Cessão Consultoria (CNPJ 22.153.470/0001-28) → Payments (CNPJ 54.792.038/0001-73), effect 15 Sep 2026. André Silva and Sheila Esmeralda signed 22 Sep. Thiago Silvestre da Silva’s envelope signed the same day. Leandro Silva’s envelope is still open (deadline 14 Oct). Abner Maioralli and Renato Paulino: no envelope sent.</p>
  <div class="banner section-space">
    <div>
      <div class="dim">Instruction total · Hansraj sends</div>
      <div class="big">{send_usdt} USDT</div>
    </div>
    <div class="dim">R$ {send_brl} · PTAX 5.1117 · {sha}</div>
  </div>
  <div class="sigs">
    <div class="sig">
      <div class="name">André Silva</div>
      <div class="role">SambaPay</div>
      <div class="role">Date ________________</div>
    </div>
    <div class="sig">
      <div class="name">Taina Chaves</div>
      <div class="role">Treasury Analyst · SambaPay</div>
      <div class="role">Date ________________</div>
    </div>
  </div>
  {foot("Close")}
</section>

</body>
</html>
'''
    return html


def write_json(ledger: dict) -> Path:
    path = HERE / "ledger.json"
    out = json.dumps(ledger, default=dec_default, indent=2, ensure_ascii=False)
    path.write_text(out + "\n", encoding="utf-8")
    return path


def print_pdf(html_path: Path, pdf_path: Path) -> None:
    chrome = shutil.which("google-chrome") or shutil.which("google-chrome-stable")
    if not chrome:
        raise SystemExit("google-chrome not found")
    uri = html_path.resolve().as_uri()
    cmd = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--allow-file-access-from-files",
        "--no-pdf-header-footer",
        "--hide-scrollbars",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=20000",
        f"--print-to-pdf={pdf_path}",
        uri,
    ]
    subprocess.run(cmd, check=True, cwd=HERE)


def main() -> None:
    ledger = build_ledger()
    json_path = write_json(ledger)
    html = render_html(ledger)
    html_path = HERE / "payroll.html"
    html_path.write_text(html, encoding="utf-8")
    pdf_path = HERE / "SambaPay-Payroll-September-2026.pdf"
    print_pdf(html_path, pdf_path)

    pointer = HERE.parent.parent / "pay-request-institutional.html"
    pointer.write_text(
        """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>SambaPay payroll register</title>
  <meta http-equiv="refresh" content="0; url=history/2026-09/payroll.html">
</head>
<body>
  <p>September 2026 payroll register:
    <a href="history/2026-09/SambaPay-Payroll-September-2026.pdf">PDF</a>
    · <a href="history/2026-09/payroll.html">print HTML</a>
    · <a href="history/2026-09/ledger.json">ledger</a>
  </p>
</body>
</html>
""",
        encoding="utf-8",
    )

    info = subprocess.check_output(["pdfinfo", str(pdf_path)], text=True)
    print(info)
    print(f"ledger  {json_path}")
    print(f"html    {html_path}")
    print(f"pdf     {pdf_path}")
    print(f"sha256  {ledger['ledger_sha256']}")
    print(f"send    R$ {money(ledger['totals']['send_brl'])} / {money(ledger['totals']['send_usdt'])} USDT")


if __name__ == "__main__":
    main()
