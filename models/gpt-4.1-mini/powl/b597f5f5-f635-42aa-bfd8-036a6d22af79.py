# Generated from: b597f5f5-f635-42aa-bfd8-036a6d22af79.json
# Description: This process involves acquiring, validating, encrypting, and trading ultra-high-frequency quantum-generated datasets between multinational entities. It includes dynamic risk assessment based on quantum encryption integrity, adaptive pricing models influenced by quantum market fluctuations, and compliance checks with emerging international quantum data regulations. The workflow ensures secure data transfer using entangled key distribution, continuous monitoring of quantum noise interference, and real-time contract negotiation through AI-mediated smart contracts. Final settlement occurs via decentralized quantum ledger technology, with post-trade analytics to optimize future transactions and maintain system integrity in a highly volatile quantum data environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
DataAcq = Transition(label='Data Acquisition')
IntegrityChk = Transition(label='Integrity Check')
QuantumEnc = Transition(label='Quantum Encrypt')

RiskAssess = Transition(label='Risk Assess')
PriceAdjust = Transition(label='Price Adjust')
ComplianceScan = Transition(label='Compliance Scan')

KeyDist = Transition(label='Key Distribution')
NoiseMonitor = Transition(label='Noise Monitor')

ContractDraft = Transition(label='Contract Draft')
AINegotiate = Transition(label='AI Negotiate')

DataTransfer = Transition(label='Data Transfer')

LedgerUpdate = Transition(label='Ledger Update')
TradeSettle = Transition(label='Trade Settle')

PostAnalysis = Transition(label='Post Analysis')
SystemAudit = Transition(label='System Audit')

MarketSync = Transition(label='Market Sync')

# Modeling the workflow according to description:

# 1) Start with Data Acquisition -> Integrity Check -> Quantum Encrypt (sequential)
po1 = StrictPartialOrder(nodes=[DataAcq, IntegrityChk, QuantumEnc])
po1.order.add_edge(DataAcq, IntegrityChk)
po1.order.add_edge(IntegrityChk, QuantumEnc)

# 2) Parallel dynamic evaluation after encryption:
#    Risk Assess, Price Adjust, Compliance Scan run in parallel after Quantum Encrypt
#    Model these three as concurrent nodes dependent on Quantum Encrypt:
po2 = StrictPartialOrder(nodes=[RiskAssess, PriceAdjust, ComplianceScan])
# They start concurrently after Quantum Encrypt - ordering edges will come later

# 3) Secure data transfer setup: Key Distribution and Noise Monitor run in parallel
secure_setup = StrictPartialOrder(nodes=[KeyDist, NoiseMonitor])

# 4) Contract negotiation involves Contract Draft and AI Negotiate sequentially
contract_neg = StrictPartialOrder(nodes=[ContractDraft, AINegotiate])
contract_neg.order.add_edge(ContractDraft, AINegotiate)

# 5) Data Transfer waits for:
#    - secure_setup (KeyDist & NoiseMonitor)
#    - contract_neg (ContractDraft -> AI Negotiate)
data_transfer = DataTransfer

# 6) Ledger Update and Trade Settle sequential after Data Transfer
ledger_trade = StrictPartialOrder(nodes=[LedgerUpdate, TradeSettle])
ledger_trade.order.add_edge(LedgerUpdate, TradeSettle)

# 7) Post Analysis and System Audit run in parallel after Trade Settle
post_audit = StrictPartialOrder(nodes=[PostAnalysis, SystemAudit])

# 8) Market Sync runs at the end independently (sync with Post Analysis & System Audit)

# Now assemble the partial orders with appropriate ordering

# Combine po2 (RiskAssess, PriceAdjust, ComplianceScan) in parallel, after QuantumEnc:
# We create a PO with po2 nodes and QuantumEnc with edges QuantumEnc-->each of po2 nodes
po2_full = StrictPartialOrder(nodes=[QuantumEnc, RiskAssess, PriceAdjust, ComplianceScan])
po2_full.order.add_edge(QuantumEnc, RiskAssess)
po2_full.order.add_edge(QuantumEnc, PriceAdjust)
po2_full.order.add_edge(QuantumEnc, ComplianceScan)

# Combine secure_setup (KeyDist, NoiseMonitor) and contract_neg (ContractDraft->AINegotiate) as concurrent nodes
# but both must finish before DataTransfer

# Create a PO that has all these nodes:
# key_dist, noise_monitor, contract_draft, ai_negotiate, DataTransfer
blocks_before_data_transfer_nodes = [KeyDist, NoiseMonitor, ContractDraft, AINegotiate, DataTransfer]

blocks_before_data_transfer = StrictPartialOrder(nodes=blocks_before_data_transfer_nodes)

# Add contract_neg edge:
blocks_before_data_transfer.order.add_edge(ContractDraft, AINegotiate)
# DataTransfer depends on KeyDist, NoiseMonitor and AINegotiate (the last negotiation step)
blocks_before_data_transfer.order.add_edge(KeyDist, DataTransfer)
blocks_before_data_transfer.order.add_edge(NoiseMonitor, DataTransfer)
blocks_before_data_transfer.order.add_edge(AINegotiate, DataTransfer)

# Now combine ledger_trade and data_transfer:
# ledger_trade after DataTransfer
ledger_trade_full = StrictPartialOrder(nodes=[DataTransfer, LedgerUpdate, TradeSettle])
ledger_trade_full.order.add_edge(DataTransfer, LedgerUpdate)
ledger_trade_full.order.add_edge(LedgerUpdate, TradeSettle)

# Combine post_audit after Trade Settle
post_audit_full = StrictPartialOrder(nodes=[TradeSettle, PostAnalysis, SystemAudit])
post_audit_full.order.add_edge(TradeSettle, PostAnalysis)
post_audit_full.order.add_edge(TradeSettle, SystemAudit)

# Finally Market Sync after post analysis and system audit:
root_nodes = [
    DataAcq, IntegrityChk, QuantumEnc,
    RiskAssess, PriceAdjust, ComplianceScan,
    KeyDist, NoiseMonitor,
    ContractDraft, AINegotiate,
    DataTransfer,
    LedgerUpdate, TradeSettle,
    PostAnalysis, SystemAudit,
    MarketSync
]

root = StrictPartialOrder(nodes=root_nodes)

# Add edges from po1
root.order.add_edge(DataAcq, IntegrityChk)
root.order.add_edge(IntegrityChk, QuantumEnc)

# From po2_full: QuantumEnc --> RiskAssess/PriceAdjust/ComplianceScan
root.order.add_edge(QuantumEnc, RiskAssess)
root.order.add_edge(QuantumEnc, PriceAdjust)
root.order.add_edge(QuantumEnc, ComplianceScan)

# From contract_neg and secure setup to DataTransfer
root.order.add_edge(ContractDraft, AINegotiate)
root.order.add_edge(KeyDist, DataTransfer)
root.order.add_edge(NoiseMonitor, DataTransfer)
root.order.add_edge(AINegotiate, DataTransfer)

# ledger_trade edges
root.order.add_edge(DataTransfer, LedgerUpdate)
root.order.add_edge(LedgerUpdate, TradeSettle)

# post_audit edges
root.order.add_edge(TradeSettle, PostAnalysis)
root.order.add_edge(TradeSettle, SystemAudit)

# finally, Market Sync after both Post Analysis and System Audit
root.order.add_edge(PostAnalysis, MarketSync)
root.order.add_edge(SystemAudit, MarketSync)