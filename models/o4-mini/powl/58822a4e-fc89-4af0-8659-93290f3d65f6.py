# Generated from: 58822a4e-fc89-4af0-8659-93290f3d65f6.json
# Description: This process outlines the complex and atypical steps involved in establishing an urban rooftop farm on a commercial building. It starts with structural assessments to ensure roof load capacity, proceeds through soil substrate preparation and irrigation system design tailored for limited space. The workflow includes obtaining multiple permits from city agencies, integrating smart sensors for climate control, selecting crop varieties suited to microclimates, and coordinating with local suppliers for organic inputs. The process further involves community engagement for educational programs, continuous monitoring of plant health via IoT devices, and finally, harvest logistics optimized for direct-to-consumer delivery. This multifaceted approach balances agricultural innovation, urban infrastructure limitations, and regulatory compliance to create a sustainable rooftop farming operation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
roof_survey   = Transition(label='Roof Survey')
load_test     = Transition(label='Load Test')
soil_mix      = Transition(label='Soil Mix')
irrigation_map= Transition(label='Irrigation Map')
permit_apply  = Transition(label='Permit Apply')
organic_cert  = Transition(label='Organic Cert')
sensor_install= Transition(label='Sensor Install')
climate_tune  = Transition(label='Climate Tune')
crop_select   = Transition(label='Crop Select')
supplier_vet  = Transition(label='Supplier Vet')
community_meet= Transition(label='Community Meet')
plant_setup   = Transition(label='Plant Setup')
health_monitor= Transition(label='Health Monitor')
data_analyze  = Transition(label='Data Analyze')
harvest_plan  = Transition(label='Harvest Plan')
delivery_prep = Transition(label='Delivery Prep')
waste_manage  = Transition(label='Waste Manage')

# Parallel branches
soil_irrigation_po = StrictPartialOrder(nodes=[soil_mix, irrigation_map])
permits_po         = StrictPartialOrder(nodes=[permit_apply, organic_cert])
community_plant_po = StrictPartialOrder(nodes=[community_meet, plant_setup])

# Monitoring loop: health_monitor then repeat data_analyze -> health_monitor
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[health_monitor, data_analyze])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    roof_survey, load_test,
    soil_irrigation_po, permits_po,
    sensor_install, climate_tune,
    crop_select, supplier_vet,
    community_plant_po,
    monitor_loop,
    harvest_plan, delivery_prep, waste_manage
])

# Define the control-flow dependencies
root.order.add_edge(roof_survey, load_test)
root.order.add_edge(load_test, soil_irrigation_po)
root.order.add_edge(soil_irrigation_po, permits_po)
root.order.add_edge(permits_po, sensor_install)
root.order.add_edge(sensor_install, climate_tune)
root.order.add_edge(climate_tune, crop_select)
root.order.add_edge(crop_select, supplier_vet)
root.order.add_edge(supplier_vet, community_plant_po)
root.order.add_edge(community_plant_po, monitor_loop)
root.order.add_edge(monitor_loop, harvest_plan)
root.order.add_edge(harvest_plan, delivery_prep)
root.order.add_edge(delivery_prep, waste_manage)