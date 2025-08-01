# Generated from: c6d42a5d-ca5f-4764-9112-9ededeb4528b.json
# Description: This process outlines the detailed steps involved in establishing an urban rooftop farm on a commercial building. It begins with site evaluation and structural assessment to ensure the roof can support the load. Subsequent activities include soil testing, selecting appropriate crops for microclimate conditions, and designing irrigation systems tailored to limited water resources. The process also involves obtaining necessary permits, sourcing sustainable materials, and coordinating with local suppliers for organic seeds and fertilizers. Installation phases cover creating raised beds, integrating pest management solutions, and setting up renewable energy sources like solar panels to power automated watering. The final stages focus on staff training, marketing the farm's produce to local restaurants, and implementing a digital monitoring system for crop health and growth optimization.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Site_Survey = Transition(label='Site Survey')
Load_Test = Transition(label='Load Test')
Soil_Sample = Transition(label='Soil Sample')
Crop_Select = Transition(label='Crop Select')
Irrigation_Plan = Transition(label='Irrigation Plan')
Permit_Apply = Transition(label='Permit Apply')
Material_Order = Transition(label='Material Order')
Supplier_Contact = Transition(label='Supplier Contact')
Bed_Install = Transition(label='Bed Install')
Pest_Control = Transition(label='Pest Control')
Solar_Setup = Transition(label='Solar Setup')
Staff_Train = Transition(label='Staff Train')
Market_Outreach = Transition(label='Market Outreach')
System_Setup = Transition(label='System Setup')
Health_Monitor = Transition(label='Health Monitor')

# Create partial orders for clustered steps

# 1) Site evaluation and structural assessment (Site Survey -> Load Test)
site_eval = StrictPartialOrder(nodes=[Site_Survey, Load_Test])
site_eval.order.add_edge(Site_Survey, Load_Test)

# 2) Soil testing, crop selection, irrigation plan (serial)
soil_crop_irrigation = StrictPartialOrder(nodes=[Soil_Sample, Crop_Select, Irrigation_Plan])
soil_crop_irrigation.order.add_edge(Soil_Sample, Crop_Select)
soil_crop_irrigation.order.add_edge(Crop_Select, Irrigation_Plan)

# 3) Permits and material/supplier coordination in parallel
permits = Permit_Apply
materials_suppliers = StrictPartialOrder(nodes=[Material_Order, Supplier_Contact])
# no order between Material_Order and Supplier_Contact, so concurrent

permits_and_supply = StrictPartialOrder(nodes=[permits, materials_suppliers])

permits_and_supply.order.add_edge(permits, materials_suppliers)  # permits before materials/suppliers makes sense to order permits first
# But actually Permits do not have to happen strictly before materials/suppliers, coordinates?

# The description suggests "obtaining permits" and "sourcing sustainable materials and coordinating suppliers"
# These can be concurrent or permits before? Usually permits required before install, materials and suppliers happen in parallel somewhat.
# Keep them in parallel (no order edges):
permits_and_supply = StrictPartialOrder(nodes=[permits, Material_Order, Supplier_Contact])
# no orders means concurrent

# 4) Installation phases: Bed Install, Pest Control, Solar Setup (probably can be concurrent/partial order)
installation = StrictPartialOrder(nodes=[Bed_Install, Pest_Control, Solar_Setup])
# These might be done in parallel; no order edges -> totally concurrent

# 5) Final stages: Staff Train -> Market Outreach -> System Setup -> Health Monitor (serial)
final_stages = StrictPartialOrder(nodes=[Staff_Train, Market_Outreach, System_Setup, Health_Monitor])
final_stages.order.add_edge(Staff_Train, Market_Outreach)
final_stages.order.add_edge(Market_Outreach, System_Setup)
final_stages.order.add_edge(System_Setup, Health_Monitor)

# Overall process ordering according to description
# Step 1 (site_eval) -> Step 2 (soil_crop_irrigation) -> Step 3 (permits_and_supply) -> Step 4 (installation) -> Step 5 (final_stages)

root = StrictPartialOrder(nodes=[site_eval, soil_crop_irrigation, permits_and_supply, installation, final_stages])

root.order.add_edge(site_eval, soil_crop_irrigation)
root.order.add_edge(soil_crop_irrigation, permits_and_supply)
root.order.add_edge(permits_and_supply, installation)
root.order.add_edge(installation, final_stages)