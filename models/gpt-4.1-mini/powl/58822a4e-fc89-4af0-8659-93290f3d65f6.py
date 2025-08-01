# Generated from: 58822a4e-fc89-4af0-8659-93290f3d65f6.json
# Description: This process outlines the complex and atypical steps involved in establishing an urban rooftop farm on a commercial building. It starts with structural assessments to ensure roof load capacity, proceeds through soil substrate preparation and irrigation system design tailored for limited space. The workflow includes obtaining multiple permits from city agencies, integrating smart sensors for climate control, selecting crop varieties suited to microclimates, and coordinating with local suppliers for organic inputs. The process further involves community engagement for educational programs, continuous monitoring of plant health via IoT devices, and finally, harvest logistics optimized for direct-to-consumer delivery. This multifaceted approach balances agricultural innovation, urban infrastructure limitations, and regulatory compliance to create a sustainable rooftop farming operation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Roof_Survey = Transition(label='Roof Survey')
Load_Test = Transition(label='Load Test')
Permit_Apply = Transition(label='Permit Apply')
Soil_Mix = Transition(label='Soil Mix')
Irrigation_Map = Transition(label='Irrigation Map')
Sensor_Install = Transition(label='Sensor Install')
Crop_Select = Transition(label='Crop Select')
Supplier_Vet = Transition(label='Supplier Vet')
Organic_Cert = Transition(label='Organic Cert')
Climate_Tune = Transition(label='Climate Tune')
Community_Meet = Transition(label='Community Meet')
Plant_Setup = Transition(label='Plant Setup')
Health_Monitor = Transition(label='Health Monitor')
Harvest_Plan = Transition(label='Harvest Plan')
Delivery_Prep = Transition(label='Delivery Prep')
Waste_Manage = Transition(label='Waste Manage')
Data_Analyze = Transition(label='Data Analyze')

# Structural assessments sequence: Roof Survey -> Load Test
structural_assessment = StrictPartialOrder(nodes=[Roof_Survey, Load_Test])
structural_assessment.order.add_edge(Roof_Survey, Load_Test)

# Soil substrate and irrigation done concurrently after Load Test
soil_and_irrigation = StrictPartialOrder(nodes=[Soil_Mix, Irrigation_Map])
# No order edges: concurrent

# Permit process: multiple permits to acquire from city agencies
# Represent Permit Apply that may internally include organic cert as an additional permit with vetting concurrent
# (Permit Apply, Supplier Vet, Organic Cert) - Supplier Vet and Organic Cert relate to organic inputs and permits
permit_subprocess = StrictPartialOrder(nodes=[Permit_Apply, Supplier_Vet, Organic_Cert])
# Let's say Supplier Vet and Organic Cert can be done in parallel but must both be finished before progressing
permit_subprocess.order.add_edge(Permit_Apply, Supplier_Vet)
permit_subprocess.order.add_edge(Permit_Apply, Organic_Cert)
# Permit Apply first, then in parallel Supplier Vet and Organic Cert

# Smart sensors and climate control integrated later
sensor_and_climate = StrictPartialOrder(nodes=[Sensor_Install, Climate_Tune])
sensor_and_climate.order.add_edge(Sensor_Install, Climate_Tune)

# Crop selection depends on climate and organic cert
crop_select_process = StrictPartialOrder(nodes=[Crop_Select])
# Crop_Select waits for Climate Tune and Organic Cert
# So combine sensor_and_climate and permit_subprocess first, then crop_select

# Community engagement and plant setup done concurrently after crop selection
community_and_plant = StrictPartialOrder(nodes=[Community_Meet, Plant_Setup])
# concurrent

# Monitoring ongoing: Health Monitor and Data Analyze (IoT devices and analysis)
monitoring = StrictPartialOrder(nodes=[Health_Monitor, Data_Analyze])
monitoring.order.add_edge(Health_Monitor, Data_Analyze)  # Health Monitor feeds Data Analyze

# Harvest logistics: Harvest Plan, Delivery Prep, Waste Manage, after monitoring
harvest_nodes = StrictPartialOrder(nodes=[Harvest_Plan, Delivery_Prep, Waste_Manage])
harvest_nodes.order.add_edge(Harvest_Plan, Delivery_Prep)
harvest_nodes.order.add_edge(Harvest_Plan, Waste_Manage)

# Connecting sequences:
# From structural_assessment -> (soil_and_irrigation && permit_subprocess)
after_structural = StrictPartialOrder(nodes=[soil_and_irrigation, permit_subprocess])
after_structural.order.add_edge(soil_and_irrigation, permit_subprocess)  # Permit after soil+irrigation step

# Then sensor_and_climate after permit_subprocess
permit_and_sensor = StrictPartialOrder(nodes=[permit_subprocess, sensor_and_climate])
permit_and_sensor.order.add_edge(permit_subprocess, sensor_and_climate)

# Crop select after sensor and climate tune + organic cert (organic cert in permit_subprocess)
# Since crop_select depends on permit_subprocess and sensor_and_climate, merge together first
crop_dependencies = StrictPartialOrder(nodes=[permit_subprocess, sensor_and_climate, Crop_Select])
crop_dependencies.order.add_edge(sensor_and_climate, Crop_Select)
crop_dependencies.order.add_edge(permit_subprocess, Crop_Select)

# After crop select: community_and_plant concurrent
after_crop = StrictPartialOrder(nodes=[Crop_Select, community_and_plant])
after_crop.order.add_edge(Crop_Select, community_and_plant)

# After community_and_plant: monitoring
after_community = StrictPartialOrder(nodes=[community_and_plant, monitoring])
after_community.order.add_edge(community_and_plant, monitoring)

# After monitoring: harvest logistics
after_monitoring = StrictPartialOrder(nodes=[monitoring, harvest_nodes])
after_monitoring.order.add_edge(monitoring, harvest_nodes)

# Compose whole flow from structural_assessment
root = StrictPartialOrder(nodes=[
    structural_assessment,
    soil_and_irrigation,
    permit_subprocess,
    sensor_and_climate,
    Crop_Select,
    community_and_plant,
    monitoring,
    harvest_nodes
])

# Order edges connecting big blocks
root.order.add_edge(structural_assessment, soil_and_irrigation)
root.order.add_edge(soil_and_irrigation, permit_subprocess)
root.order.add_edge(permit_subprocess, sensor_and_climate)
root.order.add_edge(sensor_and_climate, Crop_Select)
root.order.add_edge(Crop_Select, community_and_plant)
root.order.add_edge(community_and_plant, monitoring)
root.order.add_edge(monitoring, harvest_nodes)