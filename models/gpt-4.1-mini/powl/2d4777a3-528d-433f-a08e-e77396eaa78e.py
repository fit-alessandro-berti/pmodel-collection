# Generated from: 2d4777a3-528d-433f-a08e-e77396eaa78e.json
# Description: This process involves sourcing rare and exotic ingredients from multiple remote regions worldwide, requiring intricate coordination between local suppliers, customs authorities, and quality assurance teams. The process includes verifying authenticity, negotiating exclusive contracts, managing complex logistics involving temperature control and legal compliance, and ensuring sustainable and ethical harvesting methods. Additionally, real-time tracking and risk mitigation strategies are implemented to handle geopolitical or environmental disruptions, while maintaining continuous communication with research and development to align ingredient specifications with emerging market trends and regulatory changes.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
supplier_vetting = Transition(label='Supplier Vetting')
contract_drafting = Transition(label='Contract Drafting')
customs_clearance = Transition(label='Customs Clearance')
quality_testing = Transition(label='Quality Testing')
logistics_planning = Transition(label='Logistics Planning')
temperature_control = Transition(label='Temperature Control')
sustainability_audit = Transition(label='Sustainability Audit')
ethical_review = Transition(label='Ethical Review')
risk_assessment = Transition(label='Risk Assessment')
realtime_tracking = Transition(label='Real-time Tracking')
market_analysis = Transition(label='Market Analysis')
rnd_coordination = Transition(label='R&D Coordination')
compliance_check = Transition(label='Compliance Check')
inventory_update = Transition(label='Inventory Update')
payment_processing = Transition(label='Payment Processing')

# Build sub-partial orders to reflect process structure and partial orders

# Supplier vetting and contract drafting precede customs clearance and quality testing
supplier_contract = StrictPartialOrder(nodes=[supplier_vetting, contract_drafting])
supplier_contract.order.add_edge(supplier_vetting, contract_drafting)

customs_quality = StrictPartialOrder(nodes=[customs_clearance, quality_testing])
customs_quality.order.add_edge(customs_clearance, quality_testing)

# Logistics planning followed by temperature control and compliance check
logistics_sub = StrictPartialOrder(nodes=[logistics_planning, temperature_control, compliance_check])
logistics_sub.order.add_edge(logistics_planning, temperature_control)
logistics_sub.order.add_edge(temperature_control, compliance_check)

# Sustainability audit and ethical review proceed together (concurrent)
sustainability_ethical = StrictPartialOrder(nodes=[sustainability_audit, ethical_review])

# Risk assessment loops with realtime_tracking until exit
# LOOP: execute Risk Assessment, then choice to exit or execute Realtime Tracking then repeat
risk_loop = OperatorPOWL(operator=Operator.LOOP, children=[risk_assessment, realtime_tracking])

# Market analysis and R&D coordination happen concurrently and precede inventory update
market_rnd = StrictPartialOrder(nodes=[market_analysis, rnd_coordination])

# Inventory update followed by payment processing
inventory_payment = StrictPartialOrder(nodes=[inventory_update, payment_processing])
inventory_payment.order.add_edge(inventory_update, payment_processing)

# Overall structure:
# Supplier vetting -> Contract drafting -> Customs clearance -> Quality testing
# These feed into Logistics planning etc.
# Sustainability and ethical are parallel and independent but must complete before risk assessment loop
# Market analysis and rnd coordination are parallel and precede inventory update
# Risk loop before inventory update+payment

# Combine supplier_contract and customs_quality in sequence
supplier_to_quality = StrictPartialOrder(nodes=[supplier_contract, customs_quality])
supplier_to_quality.order.add_edge(supplier_contract, customs_quality)

# logistics depends on quality testing
quality_logistics = StrictPartialOrder(nodes=[customs_quality, logistics_sub])
quality_logistics.order.add_edge(customs_quality, logistics_sub)

# sustainability_ethical must happen before risk_loop
sustainability_risk = StrictPartialOrder(nodes=[sustainability_ethical, risk_loop])
sustainability_risk.order.add_edge(sustainability_ethical, risk_loop)

# logistics and sustainability are concurrent, both must finish before risk loop
logistics_sustainability_risk = StrictPartialOrder(nodes=[logistics_sub, sustainability_risk])
logistics_sustainability_risk.order.add_edge(logistics_sub, sustainability_risk)

# market_rnd precedes inventory update then payment processing
market_inventory = StrictPartialOrder(nodes=[market_rnd, inventory_payment])
market_inventory.order.add_edge(market_rnd, inventory_payment)

# risk loop precedes inventory/payment
risk_inventory = StrictPartialOrder(nodes=[risk_loop, inventory_payment])
risk_inventory.order.add_edge(risk_loop, inventory_payment)

# Final root with concurrency among supplier_to_quality, logistics_sustainability_risk, market_rnd
root = StrictPartialOrder(nodes=[supplier_to_quality, logistics_sustainability_risk, market_inventory])

# Order dependency supplier_to_quality --> logistics_sustainability_risk (logistics depends indirectly on quality)
root.order.add_edge(supplier_to_quality, logistics_sustainability_risk)
# After logistics_sustainability_risk and market_inventory is ordered by risk_inventory:
# Note that market_inventory also depends on risk_loop via risk_inventory,
# but here risk_loop is inside logistics_sustainability_risk, so we add ordering accordingly:
root.order.add_edge(logistics_sustainability_risk, market_inventory)