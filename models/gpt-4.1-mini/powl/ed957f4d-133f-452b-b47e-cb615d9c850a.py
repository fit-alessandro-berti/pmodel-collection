# Generated from: ed957f4d-133f-452b-b47e-cb615d9c850a.json
# Description: This process manages the end-to-end supply chain for urban beekeeping equipment, integrating sustainable sourcing, community engagement, and adaptive logistics to meet fluctuating local demand. Activities include raw material vetting from urban farms, modular product design for limited spaces, micro-warehousing in city hubs, and dynamic customer feedback loops to refine offerings. The process emphasizes eco-friendly packaging and real-time inventory tracking through IoT sensors, balancing rapid response times with minimizing carbon footprint. Additionally, it incorporates urban pollinator habitat mapping for strategic marketing and partnerships with local environmental groups to enhance brand authenticity and social impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Source_Materials = Transition(label='Source Materials')
Vet_Suppliers = Transition(label='Vet Suppliers')

Design_Modules = Transition(label='Design Modules')
Prototype_Build = Transition(label='Prototype Build')
Test_Durability = Transition(label='Test Durability')

Secure_Permits = Transition(label='Secure Permits')

Map_Habitats = Transition(label='Map Habitats')

Micro_Warehouse = Transition(label='Micro Warehouse')
Inventory_Sync = Transition(label='Inventory Sync')

Pack_Sustainably = Transition(label='Pack Sustainably')

Route_Optimize = Transition(label='Route Optimize')

Engage_Community = Transition(label='Engage Community')
Collect_Feedback = Transition(label='Collect Feedback')
Adjust_Production = Transition(label='Adjust Production')

Partner_NGOs = Transition(label='Partner NGOs')
Launch_Campaign = Transition(label='Launch Campaign')

Monitor_Sensors = Transition(label='Monitor Sensors')
Report_Impact = Transition(label='Report Impact')

# Build partial order for sourcing and vetting
sourcing = StrictPartialOrder(nodes=[Source_Materials, Vet_Suppliers])
sourcing.order.add_edge(Source_Materials, Vet_Suppliers)

# Design and prototype partial order
# Design Modules -> Prototype Build -> Test Durability
design_proto_test = StrictPartialOrder(nodes=[Design_Modules, Prototype_Build, Test_Durability])
design_proto_test.order.add_edge(Design_Modules, Prototype_Build)
design_proto_test.order.add_edge(Prototype_Build, Test_Durability)

# Secure permits is independent initially
# Map Habitats for marketing strategy
# Micro Warehouse and Inventory Sync are logistics activities
logistics = StrictPartialOrder(nodes=[Micro_Warehouse, Inventory_Sync])
# Assume Micro Warehouse before Inventory Sync
logistics.order.add_edge(Micro_Warehouse, Inventory_Sync)

# Packaging and route optimization are sequential (packaging then route)
pack_route = StrictPartialOrder(nodes=[Pack_Sustainably, Route_Optimize])
pack_route.order.add_edge(Pack_Sustainably, Route_Optimize)

# Community engagement includes Engage Community, Collect Feedback, Adjust Production as a loop (dynamic feedback)
# Model a loop: execute Engage Community, then optionally iterate over Collect Feedback + Adjust Production repeatedly
# Loop body B= sequence Collect Feedback -> Adjust Production

collect_adjust = StrictPartialOrder(nodes=[Collect_Feedback, Adjust_Production])
collect_adjust.order.add_edge(Collect_Feedback, Adjust_Production)

# Loop = * (Engage Community, Collect Feedback->Adjust Production)
feedback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Engage_Community, collect_adjust]
)

# Partner NGOs and Launch Campaign sequence to enhance brand/social impact
partner_campaign = StrictPartialOrder(nodes=[Partner_NGOs, Launch_Campaign])
partner_campaign.order.add_edge(Partner_NGOs, Launch_Campaign)

# Monitor Sensors and Report Impact sequence (IoT tracking then reporting)
monitor_report = StrictPartialOrder(nodes=[Monitor_Sensors, Report_Impact])
monitor_report.order.add_edge(Monitor_Sensors, Report_Impact)

# Assemble the top-level partial order (concurrent where possible)
nodes = [
    sourcing,
    design_proto_test,
    Secure_Permits,
    Map_Habitats,
    logistics,
    pack_route,
    feedback_loop,
    partner_campaign,
    monitor_report
]

root = StrictPartialOrder(nodes=nodes)

# Define inter-part order relations to reflect dependencies:

# Vet Suppliers must finish before Design Modules (vet to design)
root.order.add_edge(sourcing, design_proto_test)  # since sourcing nodes completed before design_proto_test

# Design-Prototyping-Test done before Secure Permits (might need permits after prototype)
root.order.add_edge(design_proto_test, Secure_Permits)

# Secure Permits before Map Habitats (permits for marketing?)
root.order.add_edge(Secure_Permits, Map_Habitats)

# Map Habitats before Partner NGOs and Launch Campaign (habitats info influences campaign)
root.order.add_edge(Map_Habitats, partner_campaign)

# Secure Permits before logistics (need permits before warehousing and inventory)
root.order.add_edge(Secure_Permits, logistics)

# Logistics before Packaging and Routing (items warehoused/inventoried before packing)
root.order.add_edge(logistics, pack_route)

# Packaging and Routing before launching community engagement loop (ready products before engaging)
root.order.add_edge(pack_route, feedback_loop)

# Partner campaign happens concurrently with feedback_loop or after (choose after)
root.order.add_edge(feedback_loop, partner_campaign)

# Partner campaign before Monitor Sensors and Report Impact (campaign includes monitoring & reporting)
root.order.add_edge(partner_campaign, monitor_report)