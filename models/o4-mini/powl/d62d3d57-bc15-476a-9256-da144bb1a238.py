# Generated from: d62d3d57-bc15-476a-9256-da144bb1a238.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farming operation within a repurposed industrial building. It includes site evaluation, structural modification, environmental system integration, crop selection based on market trends, automated nutrient delivery configuration, pest monitoring via AI sensors, workforce training in hydroponic techniques, regulatory compliance checks, and continuous yield optimization. The process culminates in launching a sustainable, tech-driven farm that maximizes space efficiency and produces high-quality crops year-round for local distribution, catering to both retail and wholesale clients while minimizing environmental impact and operational costs.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
site_survey    = Transition(label='Site Survey')
structure      = Transition(label='Structure Assess')
system_design  = Transition(label='System Design')
permit_obtain  = Transition(label='Permit Obtain')
enviro_setup   = Transition(label='Enviro Setup')
irrigation     = Transition(label='Irrigation Plan')
sensor_install = Transition(label='Sensor Install')
ai_calibrate   = Transition(label='AI Calibration')
nutrient_mix   = Transition(label='Nutrient Mix')
staff_train    = Transition(label='Staff Train')
market_align   = Transition(label='Market Align')
crop_select    = Transition(label='Crop Select')
pest_monitor   = Transition(label='Pest Monitor')
yield_analyze  = Transition(label='Yield Analyze')
launch_farm    = Transition(label='Launch Farm')

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, structure, system_design, permit_obtain,
    enviro_setup, irrigation, sensor_install, ai_calibrate,
    nutrient_mix, staff_train, market_align, crop_select,
    pest_monitor, yield_analyze, launch_farm
])

# Add sequential dependencies
order = [
    (site_survey, structure),
    (structure, system_design),
    (system_design, permit_obtain),
    (permit_obtain, enviro_setup),
    (enviro_setup, irrigation),
    (irrigation, sensor_install),
    (sensor_install, ai_calibrate),
    (ai_calibrate, nutrient_mix),
    (nutrient_mix, staff_train),
    (staff_train, market_align),
    (market_align, crop_select),
    (crop_select, pest_monitor),
    (pest_monitor, yield_analyze),
    (yield_analyze, launch_farm)
]

for src, tgt in order:
    root.order.add_edge(src, tgt)