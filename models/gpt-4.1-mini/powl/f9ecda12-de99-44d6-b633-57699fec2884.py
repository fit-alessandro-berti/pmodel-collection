# Generated from: f9ecda12-de99-44d6-b633-57699fec2884.json
# Description: This process details the complex and highly customized workflow for planning, designing, fabricating, and installing large-scale art installations in public spaces. It involves multiple stakeholders including artists, engineers, city planners, and logistics teams. The process begins with concept approval and budget alignment, followed by iterative design reviews and structural simulations. Procurement of unique materials and specialized fabrication techniques are coordinated with artisans and vendors. Permitting requires coordination with municipal authorities and compliance with safety regulations. Installation involves precise scheduling, site preparation, and on-site assembly with contingency plans for weather or technical setbacks. Post-installation includes inspections, maintenance planning, and public unveiling events, ensuring the artwork remains sustainable and engaging for the community over time.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Concept_Approve = Transition(label='Concept Approve')
Budget_Align = Transition(label='Budget Align')
Design_Review = Transition(label='Design Review')
Structure_Simulate = Transition(label='Structure Simulate')
Material_Procure = Transition(label='Material Procure')
Vendor_Select = Transition(label='Vendor Select')
Permit_Apply = Transition(label='Permit Apply')
Safety_Check = Transition(label='Safety Check')
Site_Prep = Transition(label='Site Prep')
Logistics_Plan = Transition(label='Logistics Plan')
Fabricate_Parts = Transition(label='Fabricate Parts')
Assemble_Onsite = Transition(label='Assemble Onsite')
Quality_Inspect = Transition(label='Quality Inspect')
Weather_Monitor = Transition(label='Weather Monitor')
Public_Unveil = Transition(label='Public Unveil')
Maintenance_Plan = Transition(label='Maintenance Plan')
Stakeholder_Meet = Transition(label='Stakeholder Meet')

# Iterative Design Reviews and Structure Simulations: loop on Design_Review then Structure_Simulate
design_loop = OperatorPOWL(operator=Operator.LOOP, children=[Design_Review, Structure_Simulate])

# Procurement subprocess: Material Procure and Vendor Select (can be concurrent)
procurement = StrictPartialOrder(nodes=[Material_Procure, Vendor_Select])

# Permitting subprocess: Permit Apply then Safety Check
permitting = StrictPartialOrder(nodes=[Permit_Apply, Safety_Check])
permitting.order.add_edge(Permit_Apply, Safety_Check)

# Installation subprocess:
# Weather Monitor is parallel control node for contingency
# Site Prep and Logistics Plan can be concurrent before Fabricate Parts and Assemble Onsite
install_po = StrictPartialOrder(nodes=[Site_Prep, Logistics_Plan])
# Fabricate Parts after Site Prep and Logistics Plan
install = StrictPartialOrder(nodes=[install_po, Fabricate_Parts, Assemble_Onsite, Weather_Monitor])
install.order.add_edge(install_po, Fabricate_Parts)
install.order.add_edge(Fabricate_Parts, Assemble_Onsite)
# Weather Monitor concurrent but before Assemble Onsite (monitor ongoing before assembly)
install.order.add_edge(Weather_Monitor, Assemble_Onsite)

# Post-installation subprocess: Quality Inspect, Maintenance Plan, Public Unveil
post_install = StrictPartialOrder(nodes=[Quality_Inspect, Maintenance_Plan, Public_Unveil])
post_install.order.add_edge(Quality_Inspect, Maintenance_Plan)
post_install.order.add_edge(Maintenance_Plan, Public_Unveil)

# Stakeholder meetings can be concurrent with procurement and permitting, but after design loop
# We define Stakeholder Meet as concurrent with procurement and permitting
stakeholder_conc = StrictPartialOrder(nodes=[Stakeholder_Meet])

# Start: Concept Approve then Budget Align
start = StrictPartialOrder(nodes=[Concept_Approve, Budget_Align])
start.order.add_edge(Concept_Approve, Budget_Align)

# After Budget Align goes design loop
# Then Stakeholder Meet, Procurement, Permitting in parallel (concurrent)
parallel_procure_permit_stake = StrictPartialOrder(nodes=[stakeholder_conc, procurement, permitting])

# Define order edges for parallel_procure_permit_stake: no edges because all concurrent

# Then installation subprocess after procurement and permitting and stakeholder meet done
# So parallel_procure_permit_stake --> install
# We'll model the whole process with strict partial orders and order edges
root = StrictPartialOrder(nodes=[start, design_loop, parallel_procure_permit_stake, install, post_install])

# Ordering edges:
# Complete start before design_loop
root.order.add_edge(start, design_loop)
# design_loop before parallel (stakeholder, procurement, permitting)
root.order.add_edge(design_loop, parallel_procure_permit_stake)
# parallel before install
root.order.add_edge(parallel_procure_permit_stake, install)
# install before post_install
root.order.add_edge(install, post_install)