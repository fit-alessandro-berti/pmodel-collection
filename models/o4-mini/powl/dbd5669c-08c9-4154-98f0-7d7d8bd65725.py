# Generated from: dbd5669c-08c9-4154-98f0-7d7d8bd65725.json
# Description: This process outlines the intricate steps involved in establishing an urban vertical farm within a confined city environment. It integrates advanced hydroponic and aeroponic systems, sustainable energy solutions, and IoT sensors for real-time monitoring. The workflow includes site assessment, modular unit assembly, nutrient solution calibration, seed selection based on microclimate data, pest control via biological agents, and continuous yield optimization using AI-driven analytics. The process further encompasses community engagement, regulatory compliance checks, and scalable expansion planning to ensure sustainable urban agriculture that minimizes resource usage and maximizes output in limited spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
design_layout    = Transition(label='Design Layout')
material_sourcing= Transition(label='Material Sourcing')
unit_assembly    = Transition(label='Unit Assembly')
system_wiring    = Transition(label='System Wiring')
sensor_install   = Transition(label='Sensor Install')
water_testing    = Transition(label='Water Testing')
nutrient_mix     = Transition(label='Nutrient Mix')
seed_selection   = Transition(label='Seed Selection')
planting_setup   = Transition(label='Planting Setup')
climate_control  = Transition(label='Climate Control')
pest_management  = Transition(label='Pest Management')
data_calibration = Transition(label='Data Calibration')
yield_analysis   = Transition(label='Yield Analysis')
community_meet   = Transition(label='Community Meet')
compliance_check = Transition(label='Compliance Check')
expansion_plan   = Transition(label='Expansion Plan')

# Build the optimization loop: calibration -> yield analysis, then optionally pest management, repeat
opt_seq = StrictPartialOrder(nodes=[data_calibration, yield_analysis])
opt_seq.order.add_edge(data_calibration, yield_analysis)

skip = SilentTransition()
xor_pm = OperatorPOWL(operator=Operator.XOR, children=[pest_management, skip])

opt_loop = OperatorPOWL(operator=Operator.LOOP, children=[opt_seq, xor_pm])

# Assemble the full workflow in a strict partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    material_sourcing,
    unit_assembly,
    system_wiring,
    sensor_install,
    water_testing,
    nutrient_mix,
    seed_selection,
    planting_setup,
    climate_control,
    opt_loop,
    community_meet,
    compliance_check,
    expansion_plan
])

# Define the control-flow edges
edges = [
    (site_survey, design_layout),
    (design_layout, material_sourcing),
    (material_sourcing, unit_assembly),
    (unit_assembly, system_wiring),
    (system_wiring, sensor_install),
    (sensor_install, water_testing),
    (water_testing, nutrient_mix),
    (nutrient_mix, seed_selection),
    (seed_selection, planting_setup),
    (planting_setup, climate_control),
    (climate_control, opt_loop),
    (opt_loop, community_meet),
    (community_meet, compliance_check),
    (compliance_check, expansion_plan)
]

for src, tgt in edges:
    root.order.add_edge(src, tgt)