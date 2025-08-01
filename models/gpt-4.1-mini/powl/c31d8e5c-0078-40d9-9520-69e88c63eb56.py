# Generated from: c31d8e5c-0078-40d9-9520-69e88c63eb56.json
# Description: This process outlines the complex steps involved in establishing an urban rooftop farming project within a metropolitan environment. It includes initial site assessment, structural analysis, securing permits, soil testing, irrigation system design, sourcing organic seeds, installing hydroponic units, integrating renewable energy sources, implementing pest control measures, setting up monitoring sensors, training staff, marketing produce, managing harvest cycles, waste recycling, and final reporting. The process requires coordination among architects, agronomists, city officials, and marketing teams to ensure a sustainable and profitable urban agriculture venture that maximizes limited rooftop space while adhering to city regulations and environmental standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Load_Test = Transition(label='Load Test')
Permit_Apply = Transition(label='Permit Apply')
Soil_Sample = Transition(label='Soil Sample')

Seed_Order = Transition(label='Seed Order')
Irrigation_Plan = Transition(label='Irrigation Plan')

Install_Units = Transition(label='Install Units')
Energy_Setup = Transition(label='Energy Setup')

Pest_Control = Transition(label='Pest Control')
Sensor_Setup = Transition(label='Sensor Setup')

Staff_Training = Transition(label='Staff Training')
Crop_Planting = Transition(label='Crop Planting')

Market_Launch = Transition(label='Market Launch')
Waste_Sort = Transition(label='Waste Sort')
Harvest_Log = Transition(label='Harvest Log')

# Initial partial order: Site Survey -> Load Test -> Permit Apply and Soil Sample concurrently after Permit Apply
init_PO = StrictPartialOrder(nodes=[Site_Survey, Load_Test, Permit_Apply, Soil_Sample])
init_PO.order.add_edge(Site_Survey, Load_Test)
init_PO.order.add_edge(Load_Test, Permit_Apply)

# Permit Apply -> Soil Sample (Permit Apply before Soil Sample)
# But description suggests Soil Sample and Permit Apply are steps before irrigation plan etc.
# We place Soil Sample after Permit Apply
init_PO.order.add_edge(Permit_Apply, Soil_Sample)

# After Soil Sample and Permit Apply, next Seed Order and Irrigation Plan can proceed concurrently
seed_irrig_PO = StrictPartialOrder(nodes=[Seed_Order, Irrigation_Plan])
# no order edges since concurrent

# After Seed Order and Irrigation Plan, Install Units and Energy Setup (concurrent)
install_energy_PO = StrictPartialOrder(nodes=[Install_Units, Energy_Setup])

# Pest Control and Sensor Setup are next, concurrent
pest_sensor_PO = StrictPartialOrder(nodes=[Pest_Control, Sensor_Setup])

# Staff Training then Crop Planting
training_planting_PO = StrictPartialOrder(nodes=[Staff_Training, Crop_Planting])
training_planting_PO.order.add_edge(Staff_Training, Crop_Planting)

# Marketing, Waste Sorting, and Harvest Logging are final activities
final_PO = StrictPartialOrder(nodes=[Market_Launch, Waste_Sort, Harvest_Log])
# Assume Market_Launch concurrent with Waste_Sort; Harvest_Log after Waste_Sort (log harvest after waste sort)
final_PO.order.add_edge(Waste_Sort, Harvest_Log)

# Now compose the process as partial orders connected by edges representing precedence

# Compose initial_PO -> seed_irrig_PO
first_layer = StrictPartialOrder(nodes=[init_PO, seed_irrig_PO])
first_layer.order.add_edge(init_PO, seed_irrig_PO)

# seed_irrig_PO -> install_energy_PO
second_layer = StrictPartialOrder(nodes=[first_layer, install_energy_PO])
second_layer.order.add_edge(first_layer, install_energy_PO)

# install_energy_PO -> pest_sensor_PO
third_layer = StrictPartialOrder(nodes=[second_layer, pest_sensor_PO])
third_layer.order.add_edge(second_layer, pest_sensor_PO)

# pest_sensor_PO -> training_planting_PO
fourth_layer = StrictPartialOrder(nodes=[third_layer, training_planting_PO])
fourth_layer.order.add_edge(third_layer, training_planting_PO)

# training_planting_PO -> final_PO
root = StrictPartialOrder(nodes=[fourth_layer, final_PO])
root.order.add_edge(fourth_layer, final_PO)