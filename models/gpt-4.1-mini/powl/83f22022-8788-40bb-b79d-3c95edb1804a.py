# Generated from: 83f22022-8788-40bb-b79d-3c95edb1804a.json
# Description: This process outlines the complex steps required to establish an urban vertical farming system within a high-density city environment. It involves site assessment, environmental analysis, modular unit design, resource integration including water recycling and renewable energy, plant species selection based on local climate, installation of automated monitoring systems, and community engagement for sustainable food distribution. Coordination between architects, agronomists, engineers, and local authorities ensures compliance with regulations and maximizes yield efficiency while minimizing ecological footprint. The process further includes continuous maintenance protocols, data-driven growth optimization, and adaptive marketing strategies tailored for urban consumers seeking fresh, locally grown produce.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Site_Assess = Transition(label='Site Assess')
Climate_Study = Transition(label='Climate Study')
Unit_Design = Transition(label='Unit Design')

Resource_Plan = Transition(label='Resource Plan')
Water_Setup = Transition(label='Water Setup')
Energy_Integrate = Transition(label='Energy Integrate')

Plant_Select = Transition(label='Plant Select')

Sensor_Install = Transition(label='Sensor Install')
Automation_Config = Transition(label='Automation Config')

Regulation_Check = Transition(label='Regulation Check')
Stakeholder_Meet = Transition(label='Stakeholder Meet')

Growth_Monitor = Transition(label='Growth Monitor')
Maintenance_Plan = Transition(label='Maintenance Plan')
Data_Analyze = Transition(label='Data Analyze')

Market_Launch = Transition(label='Market Launch')
Community_Outreach = Transition(label='Community Outreach')

# Model the concurrency and choices in the process

# Step 1: Site Assess --> Climate Study --> Unit Design
step1 = StrictPartialOrder(nodes=[Site_Assess, Climate_Study, Unit_Design])
step1.order.add_edge(Site_Assess, Climate_Study)
step1.order.add_edge(Climate_Study, Unit_Design)

# Step 2: Resource Plan must be followed by Water Setup and Energy Integrate concurrently
# Water Setup and Energy Integrate happen concurrently after Resource Plan
water_energy = StrictPartialOrder(nodes=[Water_Setup, Energy_Integrate]) # concurrent

resource_plan_and_concurrent = StrictPartialOrder(nodes=[Resource_Plan, water_energy])
resource_plan_and_concurrent.order.add_edge(Resource_Plan, water_energy)

# Step 3: Plant Select after Climate Study and Unit Design
# We'll connect Plant Select after Unit_Design and also after Climate_Study (already before Unit_Design)
# to enforce sequencing Plant_Select after Unit_Design is sufficient
# so later we'll link Unit_Design --> Plant_Select

# Step 4: Sensor Install --> Automation Config sequentially
sensor_automation = StrictPartialOrder(nodes=[Sensor_Install, Automation_Config])
sensor_automation.order.add_edge(Sensor_Install, Automation_Config)

# Step 5: Regulation Check and Stakeholder Meet concurrent (coordination)
coordination = StrictPartialOrder(nodes=[Regulation_Check, Stakeholder_Meet])

# Step 6: Maintenance Plan, Data Analyze, Growth Monitor sequentially
maintenance_sequence = StrictPartialOrder(nodes=[Maintenance_Plan, Data_Analyze, Growth_Monitor])
maintenance_sequence.order.add_edge(Maintenance_Plan, Data_Analyze)
maintenance_sequence.order.add_edge(Data_Analyze, Growth_Monitor)

# Step 7: Market Launch and Community Outreach concurrent
marketing_community = StrictPartialOrder(nodes=[Market_Launch, Community_Outreach])

# Now build the overall process partial order:
# We can aggregate steps and define their order:

# PO nodes (including the inner partial orders and transitions)
nodes = [
    step1,
    resource_plan_and_concurrent,
    Plant_Select,
    sensor_automation,
    coordination,
    maintenance_sequence,
    marketing_community
]

root = StrictPartialOrder(nodes=nodes)

# Order edges:

# From step1 to resource_plan_and_concurrent (planning phase to resource integration)
root.order.add_edge(step1, resource_plan_and_concurrent)

# From Unit_Design (inside step1) to Plant_Select

# Since step1 is a PO, to sequence Plant_Select after Unit_Design, we use order edges:
# We need to expose Unit_Design node from inside step1 and link to Plant_Select

# For correctness, link step1 --> Plant_Select (step1 complete before plant select)
root.order.add_edge(step1, Plant_Select)

# After Plant_Select --> sensor_automation (install & config automation)
root.order.add_edge(Plant_Select, sensor_automation)

# After sensor_automation --> coordination (regulation check and stakeholder meet)
root.order.add_edge(sensor_automation, coordination)

# After coordination --> maintenance_sequence (continuous maintenance and monitoring)
root.order.add_edge(coordination, maintenance_sequence)

# After maintenance_sequence --> marketing_community
root.order.add_edge(maintenance_sequence, marketing_community)