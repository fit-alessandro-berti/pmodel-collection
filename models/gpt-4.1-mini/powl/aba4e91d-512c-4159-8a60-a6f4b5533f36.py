# Generated from: aba4e91d-512c-4159-8a60-a6f4b5533f36.json
# Description: This process outlines the comprehensive steps required to establish an urban rooftop farming system on a commercial building. It starts with assessing rooftop structural integrity and environmental factors, followed by designing modular planting units tailored for limited space. The process includes selecting optimal crop varieties for urban microclimates, acquiring sustainable soil and nutrient sources, and integrating automated irrigation and monitoring systems. Coordination with local authorities for permits and compliance with zoning laws is essential. The workflow also involves staff training on hydroponic techniques, pest management without chemicals, and harvest logistics to ensure fresh produce delivery. Finally, continuous performance evaluation and adaptation strategies are implemented to maintain crop yield and sustainability in an urban context.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Roof_Assess = Transition(label='Roof Assess')
Design_Layout = Transition(label='Design Layout')
Crop_Select = Transition(label='Crop Select')
Material_Sourcing = Transition(label='Material Sourcing')
Permit_Filing = Transition(label='Permit Filing')
Unit_Assembly = Transition(label='Unit Assembly')
Soil_Prep = Transition(label='Soil Prep')
Irrigation_Setup = Transition(label='Irrigation Setup')
System_Integrate = Transition(label='System Integrate')
Staff_Train = Transition(label='Staff Train')
Pest_Control = Transition(label='Pest Control')
Growth_Monitor = Transition(label='Growth Monitor')
Harvest_Plan = Transition(label='Harvest Plan')
Delivery_Schedule = Transition(label='Delivery Schedule')
Yield_Review = Transition(label='Yield Review')
Compliance_Check = Transition(label='Compliance Check')
Waste_Manage = Transition(label='Waste Manage')

# Step 1 and 2: Roof Assess --> Design Layout
initial_PO = StrictPartialOrder(nodes=[Roof_Assess, Design_Layout])
initial_PO.order.add_edge(Roof_Assess, Design_Layout)

# Step 3-6 are modular planting units preparation:
# Crop Select --> Material Sourcing --> Unit Assembly --> Soil Prep
crop_material_PO = StrictPartialOrder(nodes=[Crop_Select, Material_Sourcing, Unit_Assembly, Soil_Prep])
crop_material_PO.order.add_edge(Crop_Select, Material_Sourcing)
crop_material_PO.order.add_edge(Material_Sourcing, Unit_Assembly)
crop_material_PO.order.add_edge(Unit_Assembly, Soil_Prep)

# Step 7-9 irrigation and system integration:
# Irrigation Setup --> System Integrate
irrigation_PO = StrictPartialOrder(nodes=[Irrigation_Setup, System_Integrate])
irrigation_PO.order.add_edge(Irrigation_Setup, System_Integrate)

# Step 10-12 staff training, pest control, growth monitor are concurrent:
staff_training_PO = StrictPartialOrder(nodes=[Staff_Train, Pest_Control, Growth_Monitor])

# Step 13-14 harvest and delivery planning:
harvest_PO = StrictPartialOrder(nodes=[Harvest_Plan, Delivery_Schedule])
harvest_PO.order.add_edge(Harvest_Plan, Delivery_Schedule)

# Step 15-17 final review and compliance and waste manage:
final_review_PO = StrictPartialOrder(nodes=[Yield_Review, Compliance_Check, Waste_Manage])
final_review_PO.order.add_edge(Yield_Review, Compliance_Check)
final_review_PO.order.add_edge(Compliance_Check, Waste_Manage)

# Compose the mid section: 
# Crop/Material preparation -> Irrigation/System integrate -> Staff training group
mid_PO = StrictPartialOrder(
    nodes=[crop_material_PO, irrigation_PO, staff_training_PO]
)
# Crop material --> Irrigation
mid_PO.order.add_edge(crop_material_PO, irrigation_PO)
# Irrigation --> Staff training concurrent activities
mid_PO.order.add_edge(irrigation_PO, staff_training_PO)

# Compose second final section: harvest followed by review
final_PO = StrictPartialOrder(nodes=[harvest_PO, final_review_PO])
final_PO.order.add_edge(harvest_PO, final_review_PO)

# Compose second main partial order:
# permit filing must be coordinated near compliance and delivery
# Permit Filing and Compliance_Check conservative choice parallel to Delivery_Schedule

permit_compliance_PO = StrictPartialOrder(nodes=[Permit_Filing, Compliance_Check])
# Permit filing precedes Compliance_Check as a dependency
permit_compliance_PO.order.add_edge(Permit_Filing, Compliance_Check)

# Delivery schedule and permit filing coordination (Permit_Filing before Delivery is logical)
permit_delivery_PO = StrictPartialOrder(nodes=[Permit_Filing, Delivery_Schedule])
permit_delivery_PO.order.add_edge(Permit_Filing, Delivery_Schedule)

# Combine relevant final nodes with permit filing
final_extended_PO = StrictPartialOrder(nodes=[final_PO, permit_compliance_PO])
final_extended_PO.order.add_edge(final_PO, permit_compliance_PO)

# Overall process combining all parts:
# Roof Assess --> Design Layout --> mid_PO --> permit filing & final_PO concurrency
root = StrictPartialOrder(
    nodes=[initial_PO, mid_PO, permit_compliance_PO, final_PO]
)
root.order.add_edge(initial_PO, mid_PO)
root.order.add_edge(mid_PO, permit_compliance_PO)
root.order.add_edge(permit_compliance_PO, final_PO)