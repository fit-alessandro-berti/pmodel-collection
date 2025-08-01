# Generated from: 2aa06319-01d9-48a2-b083-1a42b680d0c0.json
# Description: This process outlines the complex and highly specialized steps required to establish a fully operational urban vertical farming system. It begins with site analysis and continues through modular assembly, hydroponic system integration, automated climate control calibration, nutrient solution formulation, and real-time crop monitoring. The process also involves managing energy consumption, pest prevention protocols, staff training on vertical farming technology, and the implementation of AI-driven yield optimization. Finally, the system undergoes rigorous testing before commercial crop production begins, ensuring sustainability, efficiency, and high-quality output in an urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
site_analysis    = Transition(label='Site Analysis')
modular_design   = Transition(label='Modular Design')
structure_assembly = Transition(label='Structure Assembly')
hydroponic_setup = Transition(label='Hydroponic Setup')
climate_control  = Transition(label='Climate Control')
nutrient_mixing  = Transition(label='Nutrient Mixing')
water_circulation = Transition(label='Water Circulation')
lighting_config  = Transition(label='Lighting Config')
pest_inspection  = Transition(label='Pest Inspection')
energy_audit     = Transition(label='Energy Audit')
sensor_install   = Transition(label='Sensor Install')
data_integration = Transition(label='Data Integration')
staff_training   = Transition(label='Staff Training')
ai_calibration   = Transition(label='AI Calibration')
yield_testing    = Transition(label='Yield Testing')
system_launch    = Transition(label='System Launch')

# Build the strict partial order (sequential execution)
nodes = [
    site_analysis,
    modular_design,
    structure_assembly,
    hydroponic_setup,
    climate_control,
    nutrient_mixing,
    water_circulation,
    lighting_config,
    pest_inspection,
    energy_audit,
    sensor_install,
    data_integration,
    staff_training,
    ai_calibration,
    yield_testing,
    system_launch
]

root = StrictPartialOrder(nodes=nodes)
# Add sequential dependencies
for i in range(len(nodes) - 1):
    root.order.add_edge(nodes[i], nodes[i+1])