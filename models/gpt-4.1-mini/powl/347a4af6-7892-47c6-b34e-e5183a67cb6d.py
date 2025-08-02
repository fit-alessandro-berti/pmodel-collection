# Generated from: 347a4af6-7892-47c6-b34e-e5183a67cb6d.json
# Description: This process outlines the comprehensive steps required to establish an urban vertical farming operation within a city environment. It involves site analysis, modular system design, nutrient solution formulation, climate control calibration, and integration of IoT sensors for real-time monitoring. The process also includes workforce training on hydroponic techniques, pest management using biological controls, automated harvesting scheduling, and supply chain coordination for local distribution. Additionally, it ensures compliance with municipal regulations, sustainability reporting, and continuous improvement through data analytics to optimize yield and reduce resource consumption.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
System_Build = Transition(label='System Build')
Nutrient_Mix = Transition(label='Nutrient Mix')
Climate_Set = Transition(label='Climate Set')
Sensor_Install = Transition(label='Sensor Install')
IoT_Sync = Transition(label='IoT Sync')
Staff_Train = Transition(label='Staff Train')
Seed_Plant = Transition(label='Seed Plant')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Control = Transition(label='Pest Control')
Harvest_Plan = Transition(label='Harvest Plan')
Packaging_Prep = Transition(label='Packaging Prep')
Local_Ship = Transition(label='Local Ship')
Reg_Compliance = Transition(label='Reg Compliance')
Data_Review = Transition(label='Data Review')
Yield_Adjust = Transition(label='Yield Adjust')

# Build partial orders for sub-processes

# Subprocess 1: Site analysis and system design
design_po = StrictPartialOrder(nodes=[Site_Survey, Design_Layout, System_Build])
design_po.order.add_edge(Site_Survey, Design_Layout)
design_po.order.add_edge(Design_Layout, System_Build)

# Subprocess 2: Preparation of nutrient and climate systems + sensor integration
nutrient_po = StrictPartialOrder(nodes=[Nutrient_Mix, Climate_Set, Sensor_Install, IoT_Sync])
nutrient_po.order.add_edge(Nutrient_Mix, Climate_Set)
nutrient_po.order.add_edge(Climate_Set, Sensor_Install)
nutrient_po.order.add_edge(Sensor_Install, IoT_Sync)

# Subprocess 3: Workforce training
training_po = StrictPartialOrder(nodes=[Staff_Train])

# Subprocess 4: Planting and monitoring including pest control
plant_monitor_po = StrictPartialOrder(nodes=[Seed_Plant, Growth_Monitor, Pest_Control])
plant_monitor_po.order.add_edge(Seed_Plant, Growth_Monitor)
plant_monitor_po.order.add_edge(Growth_Monitor, Pest_Control)

# Subprocess 5: Harvesting and packaging with shipping
harvest_po = StrictPartialOrder(nodes=[Harvest_Plan, Packaging_Prep, Local_Ship])
harvest_po.order.add_edge(Harvest_Plan, Packaging_Prep)
harvest_po.order.add_edge(Packaging_Prep, Local_Ship)

# Subprocess 6: Compliance and reporting
comply_po = StrictPartialOrder(nodes=[Reg_Compliance])

# Subprocess 7: Continuous improvement loop: Data review then yield adjust, repeatable loop
data_review = Data_Review
yield_adjust = Yield_Adjust
improve_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_review, yield_adjust])

# Construct the overall process as a partial order combining these subprocesses
root = StrictPartialOrder(nodes=[design_po, nutrient_po, training_po, plant_monitor_po, harvest_po, comply_po, improve_loop])

# Define precedence to represent a sensible flow:
# Design must precede nutrient system and training
root.order.add_edge(design_po, nutrient_po)
root.order.add_edge(design_po, training_po)

# Nutrient system and training precede planting, monitoring, and pest control
root.order.add_edge(nutrient_po, plant_monitor_po)
root.order.add_edge(training_po, plant_monitor_po)

# Planting, monitoring and pest control precede harvesting process
root.order.add_edge(plant_monitor_po, harvest_po)

# Harvesting precedes shipment compliance check
root.order.add_edge(harvest_po, comply_po)

# Compliance precedes continuous improvement loop
root.order.add_edge(comply_po, improve_loop)