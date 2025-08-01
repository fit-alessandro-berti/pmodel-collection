# Generated from: 287d9d16-74c6-4664-ac93-7d9ec2db2f22.json
# Description: This process outlines the comprehensive steps required to establish an urban vertical farming facility within a repurposed industrial building. It involves initial site assessment for structural integrity and sunlight exposure, followed by modular system design tailored to crop types. Activities include sourcing sustainable materials, installing hydroponic and aeroponic systems, integrating IoT sensors for climate and nutrient monitoring, implementing automated lighting and irrigation controls, staff training on crop management, and establishing supply chain logistics for fresh produce distribution to local markets. The process concludes with continuous system optimization based on data analytics to maximize yield and resource efficiency while minimizing environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Assess = Transition(label='Site Assess')
Design_Layout = Transition(label='Design Layout')
Material_Sourcing = Transition(label='Material Sourcing')
System_Setup = Transition(label='System Setup')
Install_Hydroponics = Transition(label='Install Hydroponics')
Install_Aeroponics = Transition(label='Install Aeroponics')
Sensor_Integrate = Transition(label='Sensor Integrate')
Lighting_Setup = Transition(label='Lighting Setup')
Irrigation_Setup = Transition(label='Irrigation Setup')
Staff_Training = Transition(label='Staff Training')
Crop_Seeding = Transition(label='Crop Seeding')
Climate_Control = Transition(label='Climate Control')
Data_Monitoring = Transition(label='Data Monitoring')
Supply_Planning = Transition(label='Supply Planning')
Market_Delivery = Transition(label='Market Delivery')
Yield_Review = Transition(label='Yield Review')
System_Optimize = Transition(label='System Optimize')

# Design Layout partial order: Install Hydroponics and Install Aeroponics in parallel after System Setup
install_choice = OperatorPOWL(operator=Operator.XOR, children=[Install_Hydroponics, Install_Aeroponics])

design_layout_PO = StrictPartialOrder(
    nodes=[System_Setup, install_choice],
)
design_layout_PO.order.add_edge(System_Setup, install_choice)

# Setup partial order including Sensor Integrate, Lighting Setup, Irrigation Setup in parallel after install_choice
setup_PO = StrictPartialOrder(
    nodes=[design_layout_PO, Sensor_Integrate, Lighting_Setup, Irrigation_Setup],
)
setup_PO.order.add_edge(design_layout_PO, Sensor_Integrate)
setup_PO.order.add_edge(design_layout_PO, Lighting_Setup)
setup_PO.order.add_edge(design_layout_PO, Irrigation_Setup)

# Crop Management partial order: Staff Training then Crop Seeding then Climate Control, Data Monitoring in parallel
crop_management_PO = StrictPartialOrder(
    nodes=[Staff_Training, Crop_Seeding, Climate_Control, Data_Monitoring],
)
crop_management_PO.order.add_edge(Staff_Training, Crop_Seeding)
crop_management_PO.order.add_edge(Crop_Seeding, Climate_Control)
crop_management_PO.order.add_edge(Crop_Seeding, Data_Monitoring)

# Supply chain partial order: Supply Planning then Market Delivery
supply_chain_PO = StrictPartialOrder(
    nodes=[Supply_Planning, Market_Delivery],
)
supply_chain_PO.order.add_edge(Supply_Planning, Market_Delivery)

# Yield review and system optimize loop after supply chain and crop management
review_optimize_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Yield_Review, System_Optimize]
)

# Connect all parts in partial order
root = StrictPartialOrder(
    nodes=[
        Site_Assess,
        Design_Layout,
        Material_Sourcing,
        setup_PO,
        crop_management_PO,
        supply_chain_PO,
        review_optimize_loop,
    ]
)

# Define ordering
# Site Assess --> Design Layout and Material Sourcing (in parallel)
root.order.add_edge(Site_Assess, Design_Layout)
root.order.add_edge(Site_Assess, Material_Sourcing)

# Design Layout and Material Sourcing --> setup_PO
root.order.add_edge(Design_Layout, setup_PO)
root.order.add_edge(Material_Sourcing, setup_PO)

# setup_PO --> crop_management_PO
root.order.add_edge(setup_PO, crop_management_PO)

# crop_management_PO --> supply_chain_PO
root.order.add_edge(crop_management_PO, supply_chain_PO)

# supply_chain_PO --> review_optimize_loop
root.order.add_edge(supply_chain_PO, review_optimize_loop)