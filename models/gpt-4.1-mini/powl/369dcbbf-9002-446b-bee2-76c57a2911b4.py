# Generated from: 369dcbbf-9002-446b-bee2-76c57a2911b4.json
# Description: This process outlines the complex steps involved in launching a new cryptocurrency token on a decentralized blockchain platform. It encompasses initial concept validation, smart contract development, rigorous security audits, community engagement, regulatory compliance checks, marketing strategies, liquidity pool creation, token distribution, exchange listings, and ongoing governance mechanisms to ensure project sustainability and adaptability in a rapidly evolving market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
concept_ideation = Transition(label='Concept Ideation')
market_research = Transition(label='Market Research')
tokenomics_design = Transition(label='Tokenomics Design')
smart_contract = Transition(label='Smart Contract')
code_audit = Transition(label='Code Audit')
legal_review = Transition(label='Legal Review')
community_build = Transition(label='Community Build')
marketing_plan = Transition(label='Marketing Plan')
liquidity_setup = Transition(label='Liquidity Setup')
token_minting = Transition(label='Token Minting')
airdrop_launch = Transition(label='Airdrop Launch')
exchange_apply = Transition(label='Exchange Apply')
governance_setup = Transition(label='Governance Setup')
partnerships_form = Transition(label='Partnerships Form')
performance_monitor = Transition(label='Performance Monitor')
upgrade_deployment = Transition(label='Upgrade Deployment')

# Build partial orders reflecting the process description:

# Initial concept validation (Concept Ideation and Market Research concurrent),
# then Tokenomics Design must follow both
concept_stage = StrictPartialOrder(nodes=[concept_ideation, market_research, tokenomics_design])
concept_stage.order.add_edge(concept_ideation, tokenomics_design)
concept_stage.order.add_edge(market_research, tokenomics_design)

# Smart contract development after Tokenomics Design
tech_dev_stage = StrictPartialOrder(nodes=[smart_contract, code_audit])
tech_dev_stage.order.add_edge(smart_contract, code_audit)

# Legal review and community build happen concurrently (after code audit)
# Both must be done before marketing plan and liquidity setup which happen concurrently
legal_and_community = StrictPartialOrder(nodes=[legal_review, community_build])

marketing_and_liquidity = StrictPartialOrder(nodes=[marketing_plan, liquidity_setup])

# Token distribution consists of token minting and airdrop launch in sequence
token_distribution = StrictPartialOrder(nodes=[token_minting, airdrop_launch])
token_distribution.order.add_edge(token_minting, airdrop_launch)

# Exchange apply comes after token distribution
exchange_stage = StrictPartialOrder(nodes=[exchange_apply])

# Governance setup and partnerships form happen concurrently after exchange apply
gov_and_partnerships = StrictPartialOrder(nodes=[governance_setup, partnerships_form])

# Ongoing loop for performance monitoring and upgrade deployment (looped)
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[performance_monitor, upgrade_deployment])

# Compose the workflow:

# Stage 1: from concept_stage to tech dev stage
stage_1_2 = StrictPartialOrder(
    nodes=[concept_stage, tech_dev_stage]
)
stage_1_2.order.add_edge(concept_stage, tech_dev_stage)

# Stage 2: from tech dev -> legal and community concurrent
stage_2_3 = StrictPartialOrder(
    nodes=[tech_dev_stage, legal_and_community]
)
stage_2_3.order.add_edge(tech_dev_stage, legal_and_community)

# Stage 3: from legal and community to marketing and liquidity
stage_3_4 = StrictPartialOrder(
    nodes=[legal_and_community, marketing_and_liquidity]
)
stage_3_4.order.add_edge(legal_and_community, marketing_and_liquidity)

# Stage 4: from marketing and liquidity to token distribution
stage_4_5 = StrictPartialOrder(
    nodes=[marketing_and_liquidity, token_distribution]
)
stage_4_5.order.add_edge(marketing_and_liquidity, token_distribution)

# Stage 5: from token distribution to exchange apply
stage_5_6 = StrictPartialOrder(
    nodes=[token_distribution, exchange_stage]
)
stage_5_6.order.add_edge(token_distribution, exchange_stage)

# Stage 6: from exchange apply to governance and partnerships
stage_6_7 = StrictPartialOrder(
    nodes=[exchange_stage, gov_and_partnerships]
)
stage_6_7.order.add_edge(exchange_stage, gov_and_partnerships)

# Stage 7: from governance & partnerships to monitoring loop
stage_7_8 = StrictPartialOrder(
    nodes=[gov_and_partnerships, monitor_loop]
)
stage_7_8.order.add_edge(gov_and_partnerships, monitor_loop)

# Now nest all stages as nodes in a top-level PO
root = StrictPartialOrder(
    nodes=[stage_1_2, stage_2_3, stage_3_4, stage_4_5, stage_5_6, stage_6_7, stage_7_8]
)
root.order.add_edge(stage_1_2, stage_2_3)
root.order.add_edge(stage_2_3, stage_3_4)
root.order.add_edge(stage_3_4, stage_4_5)
root.order.add_edge(stage_4_5, stage_5_6)
root.order.add_edge(stage_5_6, stage_6_7)
root.order.add_edge(stage_6_7, stage_7_8)