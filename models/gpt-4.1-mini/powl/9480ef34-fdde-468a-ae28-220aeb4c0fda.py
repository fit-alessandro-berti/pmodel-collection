# Generated from: 9480ef34-fdde-468a-ae28-220aeb4c0fda.json
# Description: This process outlines the establishment of an urban vertical farming system within a constrained city environment. It involves selecting appropriate modular structures, integrating smart IoT sensors for environmental control, sourcing sustainable nutrient solutions, and implementing automated seeding and harvesting mechanisms. The process further includes regulatory compliance checks, community engagement for local support, and post-deployment monitoring to optimize crop yield and energy efficiency. Each phase requires coordination between architects, agronomists, engineers, and urban planners to ensure the farm operates sustainably while maximizing limited urban space and reducing carbon footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Site_Survey = Transition(label='Site Survey')
Design_Planning = Transition(label='Design Planning')
Modular_Build = Transition(label='Modular Build')
Sensor_Install = Transition(label='Sensor Install')
Nutrient_Prep = Transition(label='Nutrient Prep')
Seed_Loading = Transition(label='Seed Loading')
Climate_Setup = Transition(label='Climate Setup')
Automation_Config = Transition(label='Automation Config')
Regulation_Check = Transition(label='Regulation Check')
Staff_Training = Transition(label='Staff Training')
Community_Meet = Transition(label='Community Meet')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Control = Transition(label='Pest Control')
Harvest_Cycle = Transition(label='Harvest Cycle')
Waste_Manage = Transition(label='Waste Manage')
Energy_Audit = Transition(label='Energy Audit')

# Phases (based on process description and logical grouping)

# Initial Planning Phase: Site Survey -> Design Planning
planning_po = StrictPartialOrder(nodes=[Site_Survey, Design_Planning])
planning_po.order.add_edge(Site_Survey, Design_Planning)

# Modular construction and sensor setup are mostly sequential but some concurrency possible:
# Modular Build precedes Sensor Install and Nutrient Prep which are done in parallel
build_po = StrictPartialOrder(nodes=[Modular_Build, Sensor_Install, Nutrient_Prep])
build_po.order.add_edge(Modular_Build, Sensor_Install)
build_po.order.add_edge(Modular_Build, Nutrient_Prep)

# Seed loading, climate setup and automation config are next:
# Seed Loading precedes Climate Setup and Automation Config, which can proceed concurrently
setup_po = StrictPartialOrder(nodes=[Seed_Loading, Climate_Setup, Automation_Config])
setup_po.order.add_edge(Seed_Loading, Climate_Setup)
setup_po.order.add_edge(Seed_Loading, Automation_Config)

# Compliance and training:
# Regulation Check followed by Staff Training
compliance_po = StrictPartialOrder(nodes=[Regulation_Check, Staff_Training])
compliance_po.order.add_edge(Regulation_Check, Staff_Training)

# Community engagement typically happens after training (or could be parallel with monitoring)
community_monitor_po = StrictPartialOrder(nodes=[Community_Meet, Growth_Monitor])
# no order edge between these two - concurrent

# Maintenance Phase with repeated Harvest Cycle, Pest Control, Waste Manage, Energy Audit
# We model this as a loop:
# Loop body: Harvest Cycle -> Pest Control -> Waste Manage -> Energy Audit (sequential)
harvest_cycle_po = StrictPartialOrder(nodes=[Harvest_Cycle, Pest_Control, Waste_Manage, Energy_Audit])
harvest_cycle_po.order.add_edge(Harvest_Cycle, Pest_Control)
harvest_cycle_po.order.add_edge(Pest_Control, Waste_Manage)
harvest_cycle_po.order.add_edge(Waste_Manage, Energy_Audit)

# Loop operator: body followed by silent transition representing exit
silent = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_cycle_po, silent])

# Compose overall partial order stepwise.

# Phase1: planning_po --> build_po
phase1 = StrictPartialOrder(nodes=[planning_po, build_po])
phase1.order.add_edge(planning_po, build_po)

# Phase2: phase1 --> setup_po
phase2 = StrictPartialOrder(nodes=[phase1, setup_po])
phase2.order.add_edge(phase1, setup_po)

# Phase3: phase2 --> compliance_po
phase3 = StrictPartialOrder(nodes=[phase2, compliance_po])
phase3.order.add_edge(phase2, compliance_po)

# Phase4: phase3 --> community_monitor_po
phase4 = StrictPartialOrder(nodes=[phase3, community_monitor_po])
phase4.order.add_edge(phase3, community_monitor_po)

# Phase5: phase4 --> loop (Maintenance loop)
phase5 = StrictPartialOrder(nodes=[phase4, loop])
phase5.order.add_edge(phase4, loop)

root = phase5