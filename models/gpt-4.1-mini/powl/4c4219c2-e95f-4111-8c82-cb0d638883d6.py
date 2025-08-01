# Generated from: 4c4219c2-e95f-4111-8c82-cb0d638883d6.json
# Description: This process outlines the establishment of an urban vertical farm within a repurposed industrial building. It involves site analysis, environmental impact assessment, modular hydroponic system design, installation of climate control units, integration of IoT sensors for real-time monitoring, and automated nutrient delivery setup. The process further includes staff training on system operation, regulatory compliance checks, pilot crop cultivation, data-driven yield optimization, waste recycling implementation, energy consumption analysis, marketing strategy development for local produce, and continuous system maintenance planning to ensure sustainability and scalability of the farm operation in an urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Survey = Transition(label='Site Survey')
Impact_Review = Transition(label='Impact Review')
System_Design = Transition(label='System Design')
Climate_Setup = Transition(label='Climate Setup')
Sensor_Install = Transition(label='Sensor Install')
Nutrient_Setup = Transition(label='Nutrient Setup')
Staff_Training = Transition(label='Staff Training')
Compliance_Check = Transition(label='Compliance Check')
Pilot_Grow = Transition(label='Pilot Grow')
Yield_Analyze = Transition(label='Yield Analyze')
Waste_Manage = Transition(label='Waste Manage')
Energy_Audit = Transition(label='Energy Audit')
Marketing_Plan = Transition(label='Marketing Plan')
Maintenance_Plan = Transition(label='Maintenance Plan')
Scale_Strategy = Transition(label='Scale Strategy')

# Define the structure reflecting the description:
# - Initial site analysis: Site Survey --> Impact Review
# - Design and setup phase: System Design --> Climate Setup --> Sensor Install --> Nutrient Setup
# - Staff and compliance: Staff Training --> Compliance Check
# - Pilot and analyze: Pilot Grow --> Yield Analyze
# - Waste and energy in parallel with marketing strategy
# - Maintenance and scaling loop (continuous maintenance and scaling planning)

# Waste Manage, Energy Audit, Marketing Plan can run concurrently after Yield Analyze and Compliance Check

# Partial order for initial parts
po1 = StrictPartialOrder(nodes=[Site_Survey, Impact_Review])
po1.order.add_edge(Site_Survey, Impact_Review)

# Partial order for system setup
po2 = StrictPartialOrder(nodes=[System_Design, Climate_Setup, Sensor_Install, Nutrient_Setup])
po2.order.add_edge(System_Design, Climate_Setup)
po2.order.add_edge(Climate_Setup, Sensor_Install)
po2.order.add_edge(Sensor_Install, Nutrient_Setup)

# Partial order for training and compliance
po3 = StrictPartialOrder(nodes=[Staff_Training, Compliance_Check])
po3.order.add_edge(Staff_Training, Compliance_Check)

# Partial order for pilot and analysis
po4 = StrictPartialOrder(nodes=[Pilot_Grow, Yield_Analyze])
po4.order.add_edge(Pilot_Grow, Yield_Analyze)

# Parallel waste, energy audit, marketing after compliance and yield analysis
# We combine these 3 into a PO without edges to symbolize concurrency
concurrent_after = StrictPartialOrder(nodes=[Waste_Manage, Energy_Audit, Marketing_Plan])

# We join all above parts with edges to enforce correct ordering:
# Impact Review --> System Design (start of setup)
# Nutrient Setup --> Staff Training (training after setup)
# Compliance Check --> Pilot Grow (pilot after compliance)
# Yield Analyze --> Waste, Energy, Marketing (these three concurrent after yield)
po_main = StrictPartialOrder(
    nodes=[po1, po2, po3, po4, concurrent_after]
)
po_main.order.add_edge(po1, po2)  # Impact Review --> System Design
po_main.order.add_edge(po2, po3)  # Nutrient Setup --> Staff Training
po_main.order.add_edge(po3, po4)  # Compliance Check --> Pilot Grow
po_main.order.add_edge(po4, concurrent_after)  # Yield Analyze --> Waste, Energy, Marketing

# Maintenance and Scale Strategy form a loop: maintenance plan and scaling strategy are repeated for continuous improvement
loop_maintenance = OperatorPOWL(operator=Operator.LOOP, children=[Maintenance_Plan, Scale_Strategy])

# Final root: all above + loop_maintenance, maintenance loop starts after concurrent_after (waste, energy, marketing)
root = StrictPartialOrder(
    nodes=[po_main, loop_maintenance]
)
root.order.add_edge(po_main, loop_maintenance)