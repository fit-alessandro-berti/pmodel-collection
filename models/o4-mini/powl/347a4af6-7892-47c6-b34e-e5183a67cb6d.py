# Generated from: 347a4af6-7892-47c6-b34e-e5183a67cb6d.json
# Description: This process outlines the comprehensive steps required to establish an urban vertical farming operation within a city environment. It involves site analysis, modular system design, nutrient solution formulation, climate control calibration, and integration of IoT sensors for real-time monitoring. The process also includes workforce training on hydroponic techniques, pest management using biological controls, automated harvesting scheduling, and supply chain coordination for local distribution. Additionally, it ensures compliance with municipal regulations, sustainability reporting, and continuous improvement through data analytics to optimize yield and reduce resource consumption.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_survey   = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
system_build  = Transition(label='System Build')
nutrient_mix  = Transition(label='Nutrient Mix')
climate_set   = Transition(label='Climate Set')
sensor_install= Transition(label='Sensor Install')
iot_sync      = Transition(label='IoT Sync')
staff_train   = Transition(label='Staff Train')
seed_plant    = Transition(label='Seed Plant')
growth_monitor= Transition(label='Growth Monitor')
pest_control  = Transition(label='Pest Control')
harvest_plan  = Transition(label='Harvest Plan')
packaging_prep= Transition(label='Packaging Prep')
local_ship    = Transition(label='Local Ship')
reg_compliance= Transition(label='Reg Compliance')
data_review   = Transition(label='Data Review')
yield_adjust  = Transition(label='Yield Adjust')

# Define the continuous improvement loop: review then adjust repeatedly
improvement_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[data_review, yield_adjust]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    system_build,
    nutrient_mix,
    climate_set,
    sensor_install,
    iot_sync,
    staff_train,
    seed_plant,
    growth_monitor,
    pest_control,
    harvest_plan,
    packaging_prep,
    local_ship,
    reg_compliance,
    improvement_loop
])

# Add the sequential dependencies
edges = [
    (site_survey, design_layout),
    (design_layout, system_build),
    (system_build, nutrient_mix),
    (nutrient_mix, climate_set),
    (climate_set, sensor_install),
    (sensor_install, iot_sync),
    (iot_sync, staff_train),
    (staff_train, seed_plant),
    (seed_plant, growth_monitor),
    (growth_monitor, pest_control),
    (pest_control, harvest_plan),
    (harvest_plan, packaging_prep),
    (packaging_prep, local_ship),
    (local_ship, reg_compliance),
    (reg_compliance, improvement_loop)
]

for src, tgt in edges:
    root.order.add_edge(src, tgt)