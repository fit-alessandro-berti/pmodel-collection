# Generated from: 31a830f1-222f-4901-bc4f-3d2d0b59f89c.json
# Description: This process outlines the complex setup and operational planning required for establishing an urban vertical farm within a dense metropolitan area. It involves site assessment, modular system design, climate control calibration, integration of IoT sensors, crop selection based on market trends, automated nutrient delivery programming, waste recycling setup, energy optimization, staff training on novel agricultural technologies, marketing strategy development targeting local consumers, regulatory compliance auditing, supply chain synchronization with local vendors, continuous yield monitoring, adaptive crop rotation scheduling, and community engagement initiatives to promote urban sustainable farming practices. The process requires multidisciplinary coordination between agronomists, engineers, marketers, and urban planners to ensure both ecological sustainability and profitability in a constrained urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Activities as transitions
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Sensor_Setup = Transition(label='Sensor Setup')
Climate_Tune = Transition(label='Climate Tune')
Crop_Select = Transition(label='Crop Select')
Nutrient_Program = Transition(label='Nutrient Program')
Waste_Cycle = Transition(label='Waste Cycle')
Energy_Audit = Transition(label='Energy Audit')
Staff_Train = Transition(label='Staff Train')
Market_Plan = Transition(label='Market Plan')
Regulation_Check = Transition(label='Regulation Check')
Vendor_Sync = Transition(label='Vendor Sync')
Yield_Monitor = Transition(label='Yield Monitor')
Rotation_Plan = Transition(label='Rotation Plan')
Community_Meet = Transition(label='Community Meet')

# Partial orders for logical groupings (partial concurrency)

# Setup phase: Site Survey -> Design Layout -> Sensor Setup and Climate Tune in parallel
setup_PO = StrictPartialOrder(nodes=[Site_Survey, Design_Layout, Sensor_Setup, Climate_Tune])
setup_PO.order.add_edge(Site_Survey, Design_Layout)
setup_PO.order.add_edge(Design_Layout, Sensor_Setup)
setup_PO.order.add_edge(Design_Layout, Climate_Tune)
# Sensor_Setup and Climate_Tune are concurrent (no order between them)

# Crop preparation phase: Crop Select -> Nutrient Program -> Waste Cycle (in sequence)
crop_prep_PO = StrictPartialOrder(nodes=[Crop_Select, Nutrient_Program, Waste_Cycle])
crop_prep_PO.order.add_edge(Crop_Select, Nutrient_Program)
crop_prep_PO.order.add_edge(Nutrient_Program, Waste_Cycle)

# Staff and marketing parallel tasks: Staff Train || Market Plan || Regulation Check
staff_marketing_PO = StrictPartialOrder(nodes=[Staff_Train, Market_Plan, Regulation_Check])
# all concurrent, no edges

# Vendor and energy phase: Vendor Sync and Energy Audit in parallel before yield monitoring
vendor_energy_PO = StrictPartialOrder(nodes=[Vendor_Sync, Energy_Audit])
# parallel, no edges

# Yield monitoring with adaptive loop: Yield Monitor followed by loop of Rotation Plan
# Loop semantics: execute Yield Monitor, then choose to exit or do Rotation Plan followed by Yield Monitor again
loop_rotation = OperatorPOWL(operator=Operator.LOOP, children=[Yield_Monitor, Rotation_Plan])

# Connect vendor_energy_PO to loop_rotation
vendor_energy_to_loop_PO = StrictPartialOrder(nodes=[vendor_energy_PO, loop_rotation])
vendor_energy_to_loop_PO.order.add_edge(vendor_energy_PO, loop_rotation)

# Community engagement after the loop
community_phase_PO = StrictPartialOrder(nodes=[vendor_energy_to_loop_PO, Community_Meet])
community_phase_PO.order.add_edge(vendor_energy_to_loop_PO, Community_Meet)

# Combine big phases in partial order, reflecting some concurrency:
# setup_PO --> crop_prep_PO --> staff_marketing_PO --> community_phase_PO
root = StrictPartialOrder(nodes=[setup_PO, crop_prep_PO, staff_marketing_PO, community_phase_PO])
root.order.add_edge(setup_PO, crop_prep_PO)
root.order.add_edge(crop_prep_PO, staff_marketing_PO)
root.order.add_edge(staff_marketing_PO, community_phase_PO)