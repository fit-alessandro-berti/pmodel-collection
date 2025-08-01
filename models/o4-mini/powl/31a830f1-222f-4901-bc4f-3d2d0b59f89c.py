# Generated from: 31a830f1-222f-4901-bc4f-3d2d0b59f89c.json
# Description: This process outlines the complex setup and operational planning required for establishing an urban vertical farm within a dense metropolitan area. It involves site assessment, modular system design, climate control calibration, integration of IoT sensors, crop selection based on market trends, automated nutrient delivery programming, waste recycling setup, energy optimization, staff training on novel agricultural technologies, marketing strategy development targeting local consumers, regulatory compliance auditing, supply chain synchronization with local vendors, continuous yield monitoring, adaptive crop rotation scheduling, and community engagement initiatives to promote urban sustainable farming practices. The process requires multidisciplinary coordination between agronomists, engineers, marketers, and urban planners to ensure both ecological sustainability and profitability in a constrained urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
Site_Survey      = Transition(label='Site Survey')
Design_Layout    = Transition(label='Design Layout')
Sensor_Setup     = Transition(label='Sensor Setup')
Climate_Tune     = Transition(label='Climate Tune')
Crop_Select      = Transition(label='Crop Select')
Nutrient_Program = Transition(label='Nutrient Program')
Waste_Cycle      = Transition(label='Waste Cycle')
Energy_Audit     = Transition(label='Energy Audit')
Staff_Train      = Transition(label='Staff Train')
Market_Plan      = Transition(label='Market Plan')
Regulation_Check = Transition(label='Regulation Check')
Vendor_Sync      = Transition(label='Vendor Sync')
Yield_Monitor    = Transition(label='Yield Monitor')
Rotation_Plan    = Transition(label='Rotation Plan')
Community_Meet   = Transition(label='Community Meet')

# Build the partial order
root = StrictPartialOrder(nodes=[
    Site_Survey, Design_Layout, Sensor_Setup, Climate_Tune,
    Crop_Select, Nutrient_Program, Waste_Cycle, Energy_Audit,
    Staff_Train, Market_Plan, Regulation_Check, Vendor_Sync,
    Yield_Monitor, Rotation_Plan, Community_Meet
])

# 1. Site Survey -> Design Layout
root.order.add_edge(Site_Survey, Design_Layout)

# 2. Design Layout -> Sensor Setup & Climate Tune (parallel)
root.order.add_edge(Design_Layout, Sensor_Setup)
root.order.add_edge(Design_Layout, Climate_Tune)

# 3. Sensor & Climate integration -> Core system tasks
for src in (Sensor_Setup, Climate_Tune):
    root.order.add_edge(src, Crop_Select)
    root.order.add_edge(src, Nutrient_Program)
    root.order.add_edge(src, Waste_Cycle)
    root.order.add_edge(src, Energy_Audit)

# 4. Core system tasks -> Coordination tasks (parallel)
for src in (Crop_Select, Nutrient_Program, Waste_Cycle, Energy_Audit):
    root.order.add_edge(src, Staff_Train)
    root.order.add_edge(src, Market_Plan)
    root.order.add_edge(src, Regulation_Check)
    root.order.add_edge(src, Vendor_Sync)

# 5. Coordination tasks -> Monitoring & rotation (parallel)
for src in (Staff_Train, Market_Plan, Regulation_Check, Vendor_Sync):
    root.order.add_edge(src, Yield_Monitor)
    root.order.add_edge(src, Rotation_Plan)

# 6. Monitoring & rotation -> Community engagement
root.order.add_edge(Yield_Monitor, Community_Meet)
root.order.add_edge(Rotation_Plan, Community_Meet)