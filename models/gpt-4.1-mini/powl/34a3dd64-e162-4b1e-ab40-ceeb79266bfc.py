# Generated from: 34a3dd64-e162-4b1e-ab40-ceeb79266bfc.json
# Description: This process involves the design, installation, and optimization of a vertical farming system within an urban environment. It begins with site analysis and ends with continuous yield monitoring. The workflow includes integrating IoT sensors for environment control, sourcing sustainable materials, coordinating with local authorities for permits, and establishing supply chain logistics for fresh produce delivery. The process also addresses energy-efficient lighting installation, water recycling systems, automated nutrient delivery, and staff training on high-tech farming equipment. It ensures compliance with urban agriculture regulations and incorporates community engagement programs to promote awareness and adoption of vertical farming solutions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Site_Survey = Transition(label='Site Survey')
Permit_Check = Transition(label='Permit Check')
Design_Layout = Transition(label='Design Layout')
Material_Sourcing = Transition(label='Material Sourcing')
Install_Sensors = Transition(label='Install Sensors')
Setup_Lighting = Transition(label='Setup Lighting')
Water_System = Transition(label='Water System')
Nutrient_Mix = Transition(label='Nutrient Mix')
IoT_Integration = Transition(label='IoT Integration')
Energy_Audit = Transition(label='Energy Audit')
Staff_Training = Transition(label='Staff Training')
Test_Run = Transition(label='Test Run')
Compliance_Review = Transition(label='Compliance Review')
Community_Meet = Transition(label='Community Meet')
Yield_Monitor = Transition(label='Yield Monitor')
Supply_Setup = Transition(label='Supply Setup')

# Define main design and permit PO
design_permit_PO = StrictPartialOrder(
    nodes=[Site_Survey, Permit_Check, Design_Layout, Material_Sourcing]
)
design_permit_PO.order.add_edge(Site_Survey, Permit_Check)
design_permit_PO.order.add_edge(Permit_Check, Design_Layout)
design_permit_PO.order.add_edge(Design_Layout, Material_Sourcing)

# Installation and setup partial order for tech installs and audits
install_PO = StrictPartialOrder(
    nodes=[Install_Sensors, Setup_Lighting, Water_System, Nutrient_Mix, IoT_Integration, Energy_Audit]
)
# All installation related activities are concurrent except Energy_Audit which happens after others
install_PO.order.add_edge(Install_Sensors, Energy_Audit)
install_PO.order.add_edge(Setup_Lighting, Energy_Audit)
install_PO.order.add_edge(Water_System, Energy_Audit)
install_PO.order.add_edge(Nutrient_Mix, Energy_Audit)
install_PO.order.add_edge(IoT_Integration, Energy_Audit)

# Staff training before test run
training_PO = StrictPartialOrder(
    nodes=[Staff_Training, Test_Run]
)
training_PO.order.add_edge(Staff_Training, Test_Run)

# Compliance review and community meeting after test run
post_test_PO = StrictPartialOrder(
    nodes=[Compliance_Review, Community_Meet]
)
# Compliance review and community meet can happen concurrently
# No order edges between them -> concurrent

# Setup supply and yield monitoring concurrently after installation and training phases
supply_yield_PO = StrictPartialOrder(
    nodes=[Supply_Setup, Yield_Monitor]
)

# Build process flow partial order connecting main phases
root = StrictPartialOrder(
    nodes=[design_permit_PO, install_PO, training_PO, post_test_PO, supply_yield_PO]
)

# Edges to enforce partial order of phases:
# design_permit_PO before install_PO and training_PO
root.order.add_edge(design_permit_PO, install_PO)
root.order.add_edge(design_permit_PO, training_PO)
# install_PO and training_PO before post_test_PO and supply_yield_PO
root.order.add_edge(install_PO, post_test_PO)
root.order.add_edge(training_PO, post_test_PO)
root.order.add_edge(install_PO, supply_yield_PO)
root.order.add_edge(training_PO, supply_yield_PO)
# post_test_PO before yield monitor can be considered but yield monitor runs continuously - keep supply_yield_PO nodes concurrent

# 'Yield Monitor' is continuous monitoring and may start at the end, so it is a separate node in supply_yield_PO group with Supply_Setup
