# Generated from: 55c0c56a-0802-4b3e-98c6-728edca09fde.json
# Description: This process involves establishing a vertical farm within an urban environment, integrating advanced hydroponics and IoT technologies to optimize crop yields in limited spaces. Activities include site evaluation, environmental analysis, modular system design, nutrient solution formulation, automated climate control setup, and crop cycle monitoring. The process requires coordination between architects, agronomists, engineers, and data analysts to ensure sustainable resource use, energy efficiency, and minimal environmental impact while maximizing productivity and profitability in a non-traditional farming context.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
Site_Survey = Transition(label='Site Survey')
Soil_Testing = Transition(label='Soil Testing')
Design_Layout = Transition(label='Design Layout')
System_Procure = Transition(label='System Procure')
Install_Modules = Transition(label='Install Modules')
Setup_Sensors = Transition(label='Setup Sensors')
Calibrate_Climate = Transition(label='Calibrate Climate')
Mix_Nutrients = Transition(label='Mix Nutrients')
Plant_Seeds = Transition(label='Plant Seeds')
Automate_Water = Transition(label='Automate Water')
Monitor_Growth = Transition(label='Monitor Growth')
Analyze_Data = Transition(label='Analyze Data')
Adjust_Conditions = Transition(label='Adjust Conditions')
Harvest_Crops = Transition(label='Harvest Crops')
Waste_Disposal = Transition(label='Waste Disposal')
Market_Produce = Transition(label='Market Produce')

# Build the process as a partial order with some sequences and concurrency aligning with description

# Phase 1: Site evaluation and analysis
phase1 = StrictPartialOrder(nodes=[Site_Survey, Soil_Testing])
phase1.order.add_edge(Site_Survey, Soil_Testing)

# Phase 2: Design and procurement
phase2 = StrictPartialOrder(nodes=[Design_Layout, System_Procure])
phase2.order.add_edge(Design_Layout, System_Procure)

# Phase 3: Installation and setup
install_setup = StrictPartialOrder(nodes=[Install_Modules, Setup_Sensors, Calibrate_Climate])
install_setup.order.add_edge(Install_Modules, Setup_Sensors)
install_setup.order.add_edge(Setup_Sensors, Calibrate_Climate)

# Phase 4: Nutrient formulation & water automation (can be concurrent with installation setup)
nutrient_water = StrictPartialOrder(nodes=[Mix_Nutrients, Automate_Water])
# No direct order between Mix_Nutrients and Automate_Water (concurrent)

# Phase 5: Planting and monitoring with adjustment loop
planting_monitoring = StrictPartialOrder(nodes=[Plant_Seeds, Monitor_Growth, Analyze_Data, Adjust_Conditions])
planting_monitoring.order.add_edge(Plant_Seeds, Monitor_Growth)
planting_monitoring.order.add_edge(Monitor_Growth, Analyze_Data)
planting_monitoring.order.add_edge(Analyze_Data, Adjust_Conditions)

# Loop: after adjusting conditions go back to monitoring growth repeatedly until harvest
loop = OperatorPOWL(operator=Operator.LOOP, children=[Adjust_Conditions, Monitor_Growth])

# Add the loop edges (creating a loop involves Adjust_Conditions then choose to exit or Monitor_Growth and again Adjust_Conditions)
# For the structure here, Monitor_Growth will be inside the loop repeatedly after Adjust_Conditions.

# Phase 6: Harvest and post-harvest activities
harvest_post = StrictPartialOrder(nodes=[Harvest_Crops, Waste_Disposal, Market_Produce])
harvest_post.order.add_edge(Harvest_Crops, Waste_Disposal)
harvest_post.order.add_edge(Waste_Disposal, Market_Produce)

# Combine phases with partial order
root = StrictPartialOrder(
    nodes=[
        phase1,
        phase2,
        install_setup,
        nutrient_water,
        Plant_Seeds,
        Monitor_Growth,
        Analyze_Data,
        loop,
        Harvest_Crops,
        Waste_Disposal,
        Market_Produce,
    ]
)

# Define order between phases, assuming sequential core phases while allowing some concurrency:
# phase1 -> phase2 -> (install_setup || nutrient_water) -> Plant_Seeds -> Monitor_Growth -> Analyze_Data -> loop -> Harvest_Crops -> Waste_Disposal -> Market_Produce

root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, install_setup)
root.order.add_edge(phase2, nutrient_water)

root.order.add_edge(install_setup, Plant_Seeds)
root.order.add_edge(nutrient_water, Plant_Seeds)

root.order.add_edge(Plant_Seeds, Monitor_Growth)
root.order.add_edge(Monitor_Growth, Analyze_Data)
root.order.add_edge(Analyze_Data, loop)

root.order.add_edge(loop, Harvest_Crops)
root.order.add_edge(Harvest_Crops, Waste_Disposal)
root.order.add_edge(Waste_Disposal, Market_Produce)