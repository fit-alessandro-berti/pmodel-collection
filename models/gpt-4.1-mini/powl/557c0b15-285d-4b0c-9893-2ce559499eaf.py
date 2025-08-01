# Generated from: 557c0b15-285d-4b0c-9893-2ce559499eaf.json
# Description: This process outlines the planning, implementation, and optimization of an urban vertical farming system designed to maximize crop yield in limited city spaces. It begins with site analysis and environmental assessment, followed by modular unit design and material sourcing. Installation involves setting up hydroponic systems, lighting, and climate control, with ongoing monitoring of plant health and resource consumption. The process further includes automated nutrient adjustments, pest control strategies without chemicals, data analytics for yield prediction, and integration with local distribution networks. Continuous improvement cycles ensure sustainability, cost efficiency, and adaptability to changing urban conditions and crop varieties.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Survey = Transition(label='Site Survey')
Env_Assess = Transition(label='Env Assess')
Modular_Design = Transition(label='Modular Design')
Material_Procure = Transition(label='Material Procure')
Hydroponic_Install = Transition(label='Hydroponic Install')
Light_Setup = Transition(label='Light Setup')
Climate_Control = Transition(label='Climate Control')
Plant_Seeding = Transition(label='Plant Seeding')
Nutrient_Mix = Transition(label='Nutrient Mix')
Pest_Monitor = Transition(label='Pest Monitor')
Data_Capture = Transition(label='Data Capture')
Yield_Analyze = Transition(label='Yield Analyze')
Waste_Manage = Transition(label='Waste Manage')
Local_Partner = Transition(label='Local Partner')
System_Upgrade = Transition(label='System Upgrade')
Cost_Review = Transition(label='Cost Review')

# Planning phase partial order
planning = StrictPartialOrder(nodes=[Site_Survey, Env_Assess])
planning.order.add_edge(Site_Survey, Env_Assess)

# Design and procurement parallel partial order
design_procure = StrictPartialOrder(nodes=[Modular_Design, Material_Procure])

# Installation partial order
installation = StrictPartialOrder(
    nodes=[Hydroponic_Install, Light_Setup, Climate_Control])
installation.order.add_edge(Hydroponic_Install, Light_Setup)
installation.order.add_edge(Hydroponic_Install, Climate_Control)

# Monitoring partial order (Plant Seeding, Nutrient Mix, Pest Monitor)
monitoring = StrictPartialOrder(
    nodes=[Plant_Seeding, Nutrient_Mix, Pest_Monitor])
monitoring.order.add_edge(Plant_Seeding, Nutrient_Mix)
monitoring.order.add_edge(Plant_Seeding, Pest_Monitor)

# Analytics partial order (Data Capture, Yield Analyze)
analytics = StrictPartialOrder(nodes=[Data_Capture, Yield_Analyze])
analytics.order.add_edge(Data_Capture, Yield_Analyze)

# Distribution partial order (Waste Manage, Local Partner)
distribution = StrictPartialOrder(nodes=[Waste_Manage, Local_Partner])

# Continuous improvement loop: loop body is System_Upgrade then Cost_Review
improvement_body = StrictPartialOrder(nodes=[System_Upgrade, Cost_Review])
improvement_body.order.add_edge(System_Upgrade, Cost_Review)
improvement = OperatorPOWL(operator=Operator.LOOP, children=[improvement_body, improvement_body])

# Combine all main phases partially ordered
root = StrictPartialOrder(nodes=[
    planning, design_procure, installation, monitoring, analytics,
    distribution, improvement
])

# Define order edges between phases - logical flow
root.order.add_edge(planning, design_procure)
root.order.add_edge(planning, installation)
root.order.add_edge(design_procure, installation)
root.order.add_edge(installation, monitoring)
root.order.add_edge(monitoring, analytics)
root.order.add_edge(analytics, distribution)
root.order.add_edge(distribution, improvement)