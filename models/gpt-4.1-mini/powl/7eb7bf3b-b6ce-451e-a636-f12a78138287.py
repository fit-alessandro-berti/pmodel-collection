# Generated from: 7eb7bf3b-b6ce-451e-a636-f12a78138287.json
# Description: This process outlines the establishment of an urban rooftop farm in a dense metropolitan area, integrating sustainable practices with modern technology. It involves assessing structural integrity, securing permits, designing modular grow systems, sourcing organic seeds, installing automated irrigation, and setting up solar-powered climate control. The process continues with soil preparation, planting, monitoring plant health through IoT sensors, managing pest control organically, harvesting, packaging for local distribution, and conducting community workshops on urban agriculture. Each step requires coordination with city officials, engineers, suppliers, and local residents to ensure environmental compliance and community engagement, fostering a sustainable food source within the urban ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Survey = Transition(label='Site Survey')
Permit_Check = Transition(label='Permit Check')
Load_Test = Transition(label='Load Test')
Design_Plan = Transition(label='Design Plan')
Seed_Order = Transition(label='Seed Order')
Irrigation_Setup = Transition(label='Irrigation Setup')
Solar_Install = Transition(label='Solar Install')
Soil_Prep = Transition(label='Soil Prep')
Plant_Seeds = Transition(label='Plant Seeds')
Sensor_Deploy = Transition(label='Sensor Deploy')
Health_Monitor = Transition(label='Health Monitor')
Pest_Control = Transition(label='Pest Control')
Harvest_Crop = Transition(label='Harvest Crop')
Package_Goods = Transition(label='Package Goods')
Host_Workshop = Transition(label='Host Workshop')

# Initial assessment partial order: Site Survey -> (Permit Check and Load Test in parallel) -> Design Plan
initial_assessment = StrictPartialOrder(
    nodes=[Site_Survey, Permit_Check, Load_Test, Design_Plan]
)
initial_assessment.order.add_edge(Site_Survey, Permit_Check)
initial_assessment.order.add_edge(Site_Survey, Load_Test)
initial_assessment.order.add_edge(Permit_Check, Design_Plan)
initial_assessment.order.add_edge(Load_Test, Design_Plan)

# After design: Seed Order, Irrigation Setup, Solar Install can be done in parallel
# These three activities happen concurrently after Design Plan
setup_parallel = StrictPartialOrder(
    nodes=[Seed_Order, Irrigation_Setup, Solar_Install]
)
# Design Plan must come before them; modelled in overall PO by edges from Design Plan

# Prepare soil, plant, deploy sensors and monitor health follow in partial order
soil_prep_and_monitoring = StrictPartialOrder(
    nodes=[Soil_Prep, Plant_Seeds, Sensor_Deploy, Health_Monitor]
)
soil_prep_and_monitoring.order.add_edge(Soil_Prep, Plant_Seeds)
soil_prep_and_monitoring.order.add_edge(Plant_Seeds, Sensor_Deploy)
soil_prep_and_monitoring.order.add_edge(Sensor_Deploy, Health_Monitor)

# Pest control can happen concurrently with health monitoring, so no edge between Pest Control and Health Monitor
# But Pest Control must come after Plant Seeds to be relevant, so edge Plant Seeds -> Pest Control
pest_control_stage = StrictPartialOrder(
    nodes=[Pest_Control]
)
# We'll link Plant Seeds -> Pest Control later

# Harvest Crop must wait for Health Monitor and Pest Control
harvest_and_package = StrictPartialOrder(
    nodes=[Harvest_Crop, Package_Goods]
)
harvest_and_package.order.add_edge(Harvest_Crop, Package_Goods)

# Host Workshop can be concurrent with or after package goods; we place it after packaging
# To follow description where workshops are final workshops on urban agriculture
workshop_stage = StrictPartialOrder(
    nodes=[Host_Workshop]
)

# Now compose the entire process as a strict partial order with all activities and partial orders
root = StrictPartialOrder(
    nodes=[
        initial_assessment,
        setup_parallel,
        soil_prep_and_monitoring,
        pest_control_stage,
        harvest_and_package,
        workshop_stage
    ]
)

# Add edges between sub-processes according to dependencies

# Initial assessment end → setup parallel start (Design Plan → Seed Order, Irrigation Setup, Solar Install)
root.order.add_edge(initial_assessment, setup_parallel)
# To be more precise, add edges from Design Plan to Seed Order, Irrigation Setup, Solar Install inside root.order
# Because subnodes are embedded inside StrictPartialOrder, add edges from initial_assessment node to setup_parallel node.
# That's appropriate at this level.

# Setup parallel → soil prep and monitoring (all setup activities must complete before Soil Prep)
root.order.add_edge(setup_parallel, soil_prep_and_monitoring)

# Inside soil_prep_and_monitoring, Plant Seeds is before Pest Control, so add edge soil_prep_and_monitoring -> pest_control_stage 
root.order.add_edge(soil_prep_and_monitoring, pest_control_stage)

# Pest Control and Health Monitor run in parallel after Plant Seeds, no edge between Health Monitor and Pest Control themselves,
# handled inside partial orders and partial order relations above.

# harvest_and_package after both Health Monitor and Pest Control, so add edges from both soil_prep_and_monitoring and pest_control_stage to harvest_and_package
root.order.add_edge(soil_prep_and_monitoring, harvest_and_package)
root.order.add_edge(pest_control_stage, harvest_and_package)

# Workshop after packaging
root.order.add_edge(harvest_and_package, workshop_stage)