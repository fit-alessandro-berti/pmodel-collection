# Generated from: 228de98b-cc88-4b50-bb0f-76813b1f2567.json
# Description: This process outlines the comprehensive steps involved in launching an urban vertical farm that integrates sustainable agriculture technology with community engagement and real-time data analytics. It begins with site evaluation using environmental sensors and urban zoning regulations, followed by modular infrastructure setup including hydroponic and aeroponic systems. Concurrently, partnerships with local suppliers and distribution networks are established to ensure fresh produce delivery. The process also involves continuous monitoring through IoT devices, adaptive nutrient management based on crop feedback, and workforce training emphasizing both agricultural expertise and technology operation. Additionally, a community outreach program is deployed to promote education, local involvement, and market awareness. Finally, a feedback loop incorporates customer insights and operational data to optimize yield and sustainability, ensuring the farm remains economically viable and environmentally responsible in a dense urban setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
Site_Survey = Transition('Site Survey')
Regulation_Review = Transition('Regulation Review')
Tech_Selection = Transition('Tech Selection')
Modular_Build = Transition('Modular Build')
System_Setup = Transition('System Setup')
Supplier_Vetting = Transition('Supplier Vetting')
Distribution_Plan = Transition('Distribution Plan')
IoT_Install = Transition('IoT Install')
Crop_Monitoring = Transition('Crop Monitoring')
Nutrient_Adjust = Transition('Nutrient Adjust')
Staff_Training = Transition('Staff Training')
Community_Outreach = Transition('Community Outreach')
Market_Launch = Transition('Market Launch')
Feedback_Analyze = Transition('Feedback Analyze')
Yield_Optimize = Transition('Yield Optimize')
Sustainability_Audit = Transition('Sustainability Audit')

# Site evaluation partial order: Site Survey --> Regulation Review --> Tech Selection
site_evaluation = StrictPartialOrder(nodes=[Site_Survey, Regulation_Review, Tech_Selection])
site_evaluation.order.add_edge(Site_Survey, Regulation_Review)
site_evaluation.order.add_edge(Regulation_Review, Tech_Selection)

# Modular infrastructure build: Modular Build --> System Setup
modular_infra = StrictPartialOrder(nodes=[Modular_Build, System_Setup])
modular_infra.order.add_edge(Modular_Build, System_Setup)

# Partnership establishment partial order: Supplier Vetting --> Distribution Plan
partnership = StrictPartialOrder(nodes=[Supplier_Vetting, Distribution_Plan])
partnership.order.add_edge(Supplier_Vetting, Distribution_Plan)

# Workforce training (can be after Nutrient Adjust since it depends on crop feedback and tech operation)
workforce_training = Staff_Training

# Monitoring cycle loop:
# Loop node (* (Feedback Analyze + Yield Optimize + Sustainability Audit, Crop Monitoring + Nutrient Adjust + IoT Install))
# According to description: continuous monitoring (IoT Install, Crop Monitoring), adaptive nutrient management (Nutrient Adjust)
# and a feedback loop (Feedback Analyze, Yield Optimize, Sustainability Audit)
# We will model the loop with A = Feedback & Optimization steps, B = Monitoring & Nutrient Adjust
# But per LOOP definition: execute A once, then either exit or execute B then A again

# Define feedback steps partial order: Feedback Analyze --> Yield Optimize --> Sustainability Audit
feedback_steps = StrictPartialOrder(nodes=[Feedback_Analyze, Yield_Optimize, Sustainability_Audit])
feedback_steps.order.add_edge(Feedback_Analyze, Yield_Optimize)
feedback_steps.order.add_edge(Yield_Optimize, Sustainability_Audit)

# Define monitoring steps partial order with nutrient adjust and IoT install:
# IoT Install --> Crop Monitoring --> Nutrient Adjust (since nutrient adjust is adaptive based on monitoring)
monitoring_steps = StrictPartialOrder(nodes=[IoT_Install, Crop_Monitoring, Nutrient_Adjust])
monitoring_steps.order.add_edge(IoT_Install, Crop_Monitoring)
monitoring_steps.order.add_edge(Crop_Monitoring, Nutrient_Adjust)

# Construct loop: * (feedback_steps, monitoring_steps)
loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_steps, monitoring_steps])

# Community outreach and market launch sequence:
community_and_market = StrictPartialOrder(nodes=[Community_Outreach, Market_Launch])
community_and_market.order.add_edge(Community_Outreach, Market_Launch)

# The big picture order:
# 1) site_evaluation --> modular_infra
# 2) modular_infra and partnership run concurrently (no order between modular_infra and partnership)
# 3) after modular_infra and partnership, loop and workforce_training start concurrently (loop and Staff Training concurrent)
# 4) after workforce_training, community_and_market
# 5) after community_and_market, loop continues? No, feedback loop is modeled inside loop already at step 3.
# Actually, loop includes continuous/feedback activities, so we model loop available after initial build and partnerships.
# Workforce training is emphasized both on agri and tech, so place workforce_training parallel to loop
# Place workforce training to happen concurrent with loop or slightly before community?

# From description: workforce training involved during process, place it concurrent with loop
# community outreach and market launch happen after workforce training, but independent of loop mentioned explicitly

# Construct top-level partial order:
# Nodes: site_evaluation, modular_infra, partnership, loop, workforce_training, community_and_market

# Assemble top-level nodes
workforce_training_po = StrictPartialOrder(nodes=[workforce_training])  # single node as PO for consistency

top_nodes = [site_evaluation, modular_infra, partnership, loop, workforce_training_po, community_and_market]
root = StrictPartialOrder(nodes=top_nodes)

# Add edges:
# site_evaluation --> modular_infra
root.order.add_edge(site_evaluation, modular_infra)

# modular_infra and partnership concurrent (no edge)

# modular_infra and partnership --> loop
root.order.add_edge(modular_infra, loop)
root.order.add_edge(partnership, loop)

# modular_infra and partnership --> workforce_training_po
root.order.add_edge(modular_infra, workforce_training_po)
root.order.add_edge(partnership, workforce_training_po)

# workforce_training_po --> community_and_market
root.order.add_edge(workforce_training_po, community_and_market)

# No direct order between loop and community_and_market (loop ongoing continuous monitoring)

# Final root holds complete process model
