# Generated from: 5d1785c7-b7a5-4ae9-96f8-8e7bd1e5e8de.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farm in a dense metropolitan area. It includes securing permits, designing modular grow units optimized for limited spaces, integrating automated nutrient delivery systems, and implementing advanced climate controls. The process also covers sourcing heirloom seeds, training staff on hydroponic techniques, and establishing partnerships with local restaurants for produce distribution. Continuous monitoring through IoT sensors ensures optimal plant health, while waste recycling loops convert organic matter into compost. Marketing efforts target eco-conscious consumers, and periodic audits maintain regulatory compliance and sustainability certifications. This atypical process blends agriculture, technology, and urban planning to create a self-sustaining food production ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
Permit_Securing = Transition(label='Permit Securing')
Site_Survey = Transition(label='Site Survey')
Unit_Design = Transition(label='Unit Design')
Seed_Sourcing = Transition(label='Seed Sourcing')
System_Setup = Transition(label='System Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Climate_Tune = Transition(label='Climate Tune')
Staff_Training = Transition(label='Staff Training')
IoT_Install = Transition(label='IoT Install')
Waste_Cycle = Transition(label='Waste Cycle')
Planting_Phase = Transition(label='Planting Phase')
Growth_Monitor = Transition(label='Growth Monitor')
Quality_Audit = Transition(label='Quality Audit')
Market_Launch = Transition(label='Market Launch')
Partner_Align = Transition(label='Partner Align')
Compliance_Check = Transition(label='Compliance Check')
Feedback_Loop = Transition(label='Feedback Loop')

# Loop for Waste Recycling: convert organic waste into compost repeatedly
waste_loop = OperatorPOWL(operator=Operator.LOOP, children=[Waste_Cycle, Feedback_Loop])

# Loop for audits and compliance maintaining sustainability (Quality Audit and Compliance Check repeated)
audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[Quality_Audit, Compliance_Check])

# Partial order describing the main process steps before distribution and marketing
preparation_po = StrictPartialOrder(
    nodes=[
        Permit_Securing,
        Site_Survey,
        Unit_Design,
        Seed_Sourcing,
        System_Setup,
        Nutrient_Mix,
        Climate_Tune,
        Staff_Training,
        IoT_Install,
        Planting_Phase,
        Growth_Monitor,
        Partner_Align,
        market_launch := Market_Launch,
        waste_loop,
        audit_loop,
    ]
)
# Define order constraints to capture dependencies:
# Permit & Site Survey first
preparation_po.order.add_edge(Permit_Securing, Site_Survey)
# Unit Design after Site Survey
preparation_po.order.add_edge(Site_Survey, Unit_Design)
# Seed Sourcing, System Setup, Nutrient Mix, Climate Tune after Unit Design
preparation_po.order.add_edge(Unit_Design, Seed_Sourcing)
preparation_po.order.add_edge(Unit_Design, System_Setup)
preparation_po.order.add_edge(Unit_Design, Nutrient_Mix)
preparation_po.order.add_edge(Unit_Design, Climate_Tune)
# Staff Training after Seed Sourcing and Nutrient Mix (staff must be trained after knowing seeds and nutrients)
preparation_po.order.add_edge(Seed_Sourcing, Staff_Training)
preparation_po.order.add_edge(Nutrient_Mix, Staff_Training)
# IoT Install after System Setup and Climate Tune
preparation_po.order.add_edge(System_Setup, IoT_Install)
preparation_po.order.add_edge(Climate_Tune, IoT_Install)
# Planting Phase after Staff Training and IoT Install
preparation_po.order.add_edge(Staff_Training, Planting_Phase)
preparation_po.order.add_edge(IoT_Install, Planting_Phase)
# Growth Monitor after Planting Phase
preparation_po.order.add_edge(Planting_Phase, Growth_Monitor)
# Partner Align can be concurrent but before Market Launch 
preparation_po.order.add_edge(Growth_Monitor, Partner_Align)
# Market Launch after Partner Alignment and Growth Monitor
preparation_po.order.add_edge(Partner_Align, market_launch)
# Waste cycling and audits can run concurrently with Partner Align and Market Launch but started after Planting_Phase
preparation_po.order.add_edge(Planting_Phase, waste_loop)
preparation_po.order.add_edge(Planting_Phase, audit_loop)
# Audit loop feeds back quality control to Waste cycle and vice versa are inside loops so no cross-edge needed

root = preparation_po