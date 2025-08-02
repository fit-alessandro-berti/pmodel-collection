# Generated from: f539c9ab-5eb3-445b-9dae-fb136a5c953c.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm within a repurposed industrial building. It includes site assessment, modular system design, hydroponic installation, climate control configuration, nutrient management, automated pest detection, energy optimization, labor training, local market integration, and continuous yield monitoring, all while complying with urban agricultural regulations and sustainability standards. The process ensures maximized crop output in limited space using advanced technology and data analytics to maintain optimal growth conditions and resource efficiency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Site_Survey = Transition(label='Site Survey')
Structural_Audit = Transition(label='Structural Audit')
Modular_Design = Transition(label='Modular Design')
Hydroponic_Setup = Transition(label='Hydroponic Setup')
Climate_Config = Transition(label='Climate Config')
Nutrient_Mix = Transition(label='Nutrient Mix')
Pest_Detect = Transition(label='Pest Detect')
Lighting_Setup = Transition(label='Lighting Setup')
Energy_Audit = Transition(label='Energy Audit')
Automation_Install = Transition(label='Automation Install')
Staff_Training = Transition(label='Staff Training')
Market_Analysis = Transition(label='Market Analysis')
Regulation_Check = Transition(label='Regulation Check')
Yield_Monitor = Transition(label='Yield Monitor')
Waste_Manage = Transition(label='Waste Manage')
Data_Analytics = Transition(label='Data Analytics')

# Build partial orders for natural sub-processes reflecting described dependencies and concurrency

# Site Assessment phase
site_assessment = StrictPartialOrder(nodes=[Site_Survey, Structural_Audit])
site_assessment.order.add_edge(Site_Survey, Structural_Audit)

# Design phase (after site assessment)
# Modular Design depends on Structural Audit
# Hydroponic Setup depends on Modular Design
# Climate Config and Lighting Setup can be parallel after Modular Design
design_phase = StrictPartialOrder(nodes=[Modular_Design, Hydroponic_Setup, Climate_Config, Lighting_Setup])
design_phase.order.add_edge(Modular_Design, Hydroponic_Setup)
design_phase.order.add_edge(Modular_Design, Climate_Config)
design_phase.order.add_edge(Modular_Design, Lighting_Setup)

# Nutrient preparation related; Nutrient Mix, Pest Detect, Waste Manage can be parallel after Hydroponic Setup
nutrient_phase = StrictPartialOrder(nodes=[Nutrient_Mix, Pest_Detect, Waste_Manage])
# no edges = concurrent

# Energy optimization and automation installs after Lighting Setup and Energy Audit
# Energy Audit must precede Automation Install
energy_automation = StrictPartialOrder(nodes=[Energy_Audit, Automation_Install])
energy_automation.order.add_edge(Energy_Audit, Automation_Install)

# Staff Training depends on Automation Install (need systems in place for training)
# Market Analysis and Regulation Check can proceed in parallel after Staff Training
staff_market_regulation = StrictPartialOrder(nodes=[Staff_Training, Market_Analysis, Regulation_Check])
staff_market_regulation.order.add_edge(Staff_Training, Market_Analysis)
staff_market_regulation.order.add_edge(Staff_Training, Regulation_Check)

# Monitoring phase continuous: Yield Monitor and Data Analytics run concurrently after Market Analysis & Regulation Check and Pest Detect
# We model Yield Monitor and Data Analytics concurrent, after Pest Detect, Market Analysis, Regulation Check finish
# We'll create a partial order enforcing their dependencies:
monitoring_pre = StrictPartialOrder(nodes=[Pest_Detect, Market_Analysis, Regulation_Check])
# no edges since they run parallel but must finish before monitoring

monitoring = StrictPartialOrder(nodes=[Yield_Monitor, Data_Analytics])
# no edges = concurrent

# Now connect monitoring dependencies: Pest Detect, Market Analysis, Regulation Check --> Yield Monitor, Data Analytics
# This means add edges from Pest Detect, Market Analysis, Regulation Check to both monitoring nodes
# To do this, create a combined PO including monitoring_pre and monitoring and add edges accordingly

monitoring_all_nodes = [Pest_Detect, Market_Analysis, Regulation_Check, Yield_Monitor, Data_Analytics]
monitoring_full = StrictPartialOrder(nodes=monitoring_all_nodes)
# dependencies to yield monitor and data analytics
for src in [Pest_Detect, Market_Analysis, Regulation_Check]:
    monitoring_full.order.add_edge(src, Yield_Monitor)
    monitoring_full.order.add_edge(src, Data_Analytics)

# Finally, combine all phases into the full process partial order

# Nodes:
# Site Assessment -> Design Phase -> Nutrient Phase & Energy Automation in parallel
# Energy Automation -> Staff Training -> Market & Regulation
# Market & Regulation & Nutrient Phase -> Monitoring

all_nodes = [
    Site_Survey, Structural_Audit,
    Modular_Design, Hydroponic_Setup, Climate_Config, Lighting_Setup,
    Nutrient_Mix, Pest_Detect, Waste_Manage,
    Energy_Audit, Automation_Install,
    Staff_Training, Market_Analysis, Regulation_Check,
    Yield_Monitor, Data_Analytics
]

root = StrictPartialOrder(nodes=all_nodes)

# Site Assessment edges
root.order.add_edge(Site_Survey, Structural_Audit)

# Design Phase edges
root.order.add_edge(Structural_Audit, Modular_Design)
root.order.add_edge(Modular_Design, Hydroponic_Setup)
root.order.add_edge(Modular_Design, Climate_Config)
root.order.add_edge(Modular_Design, Lighting_Setup)

# Nutrient Phase after Hydroponic Setup
root.order.add_edge(Hydroponic_Setup, Nutrient_Mix)
root.order.add_edge(Hydroponic_Setup, Pest_Detect)
root.order.add_edge(Hydroponic_Setup, Waste_Manage)

# Energy Optimization & Automation after Lighting Setup and Energy Audit must precede Automation Install
root.order.add_edge(Lighting_Setup, Energy_Audit)
root.order.add_edge(Energy_Audit, Automation_Install)

# Staff Training after Automation Install
root.order.add_edge(Automation_Install, Staff_Training)

# Market Analysis and Regulation Check after Staff Training
root.order.add_edge(Staff_Training, Market_Analysis)
root.order.add_edge(Staff_Training, Regulation_Check)

# Monitoring depends on Pest Detect, Market Analysis, Regulation Check
root.order.add_edge(Pest_Detect, Yield_Monitor)
root.order.add_edge(Pest_Detect, Data_Analytics)
root.order.add_edge(Market_Analysis, Yield_Monitor)
root.order.add_edge(Market_Analysis, Data_Analytics)
root.order.add_edge(Regulation_Check, Yield_Monitor)
root.order.add_edge(Regulation_Check, Data_Analytics)