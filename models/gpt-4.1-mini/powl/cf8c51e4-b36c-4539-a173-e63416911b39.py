# Generated from: cf8c51e4-b36c-4539-a173-e63416911b39.json
# Description: This process outlines the detailed steps involved in establishing an urban vertical farm within a repurposed multi-story building. It begins with site analysis and zoning approvals, followed by structural assessments and retrofitting. Next, hydroponic system installation, climate control calibration, and nutrient cycle design take place. Staff recruitment and training are conducted alongside software integration for automated monitoring. Finally, initial crop planting, growth monitoring, pest management, and harvest scheduling ensure operational readiness and sustainability in an unconventional agricultural environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Site_Analysis = Transition(label='Site Analysis')
Zoning_Approval = Transition(label='Zoning Approval')

Structural_Check = Transition(label='Structural Check')
Building_Retrofit = Transition(label='Building Retrofit')

Hydroponic_Setup = Transition(label='Hydroponic Setup')
Climate_Control = Transition(label='Climate Control')
Nutrient_Design = Transition(label='Nutrient Design')

Staff_Hiring = Transition(label='Staff Hiring')
Staff_Training = Transition(label='Staff Training')

Software_Install = Transition(label='Software Install')
System_Testing = Transition(label='System Testing')

Crop_Planting = Transition(label='Crop Planting')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Control = Transition(label='Pest Control')
Harvest_Plan = Transition(label='Harvest Plan')

# Staff activities (Hiring and Training) in sequence
staff_seq = StrictPartialOrder(nodes=[Staff_Hiring, Staff_Training])
staff_seq.order.add_edge(Staff_Hiring, Staff_Training)

# Software activities (Install and Test) in sequence
software_seq = StrictPartialOrder(nodes=[Software_Install, System_Testing])
software_seq.order.add_edge(Software_Install, System_Testing)

# Staff and Software can proceed in parallel (no order edges)
staff_software_po = StrictPartialOrder(nodes=[staff_seq, software_seq])

# Hydroponic activities in sequence
hydro_seq = StrictPartialOrder(nodes=[Hydroponic_Setup, Climate_Control, Nutrient_Design])
hydro_seq.order.add_edge(Hydroponic_Setup, Climate_Control)
hydro_seq.order.add_edge(Climate_Control, Nutrient_Design)

# Crop related activities in sequence
crop_seq = StrictPartialOrder(nodes=[Crop_Planting, Growth_Monitor, Pest_Control, Harvest_Plan])
crop_seq.order.add_edge(Crop_Planting, Growth_Monitor)
crop_seq.order.add_edge(Growth_Monitor, Pest_Control)
crop_seq.order.add_edge(Pest_Control, Harvest_Plan)

# Structural activities in sequence
struct_seq = StrictPartialOrder(nodes=[Structural_Check, Building_Retrofit])
struct_seq.order.add_edge(Structural_Check, Building_Retrofit)

# Initial site phases sequence:
# Site Analysis --> Zoning Approval --> Structural Seq --> Hydroponic Seq --> (staff_software_po in parallel) --> Crop Seq

# Compose phases into nodes for overall partial order
phase_nodes = [Site_Analysis, Zoning_Approval, struct_seq, hydro_seq, staff_software_po, crop_seq]

root = StrictPartialOrder(nodes=phase_nodes)
root.order.add_edge(Site_Analysis, Zoning_Approval)
root.order.add_edge(Zoning_Approval, struct_seq)
root.order.add_edge(struct_seq, hydro_seq)
root.order.add_edge(hydro_seq, staff_software_po)
root.order.add_edge(staff_software_po, crop_seq)