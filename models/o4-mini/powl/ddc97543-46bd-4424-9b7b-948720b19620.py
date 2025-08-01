# Generated from: ddc97543-46bd-4424-9b7b-948720b19620.json
# Description: This process outlines the establishment of an urban vertical farm designed to maximize crop yield in limited city spaces using innovative hydroponic systems. It includes site assessment, structural retrofitting, environmental control calibration, nutrient solution formulation, crop selection based on climate resilience, and integration of AI-driven monitoring. The workflow further involves worker training on specialized equipment, implementation of pest management strategies without pesticides, scheduling automated irrigation cycles, and establishing supply chain logistics to deliver fresh produce to local markets efficiently. Continuous data collection and analysis ensure optimization of growth conditions and energy consumption, promoting sustainability and profitability in an unconventional agricultural model within urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the labeled transitions for each activity
site_survey    = Transition(label='Site Survey')
structure_prep = Transition(label='Structure Prep')
system_install = Transition(label='System Install')
env_control    = Transition(label='Env Control')
nutrient_mix   = Transition(label='Nutrient Mix')
crop_select    = Transition(label='Crop Select')
ai_setup       = Transition(label='AI Setup')
worker_train   = Transition(label='Worker Train')
pest_control   = Transition(label='Pest Control')
irrigation_pl  = Transition(label='Irrigation Plan')
market_setup   = Transition(label='Market Setup')
logistics_pl   = Transition(label='Logistics Plan')

data_monitor   = Transition(label='Data Monitor')
yield_forecast = Transition(label='Yield Forecast')
energy_audit   = Transition(label='Energy Audit')
waste_manage   = Transition(label='Waste Manage')

# 1) Initial deployment and setup in a strict sequence
initial_setup = StrictPartialOrder(nodes=[
    site_survey, structure_prep, system_install,
    env_control, nutrient_mix, crop_select,
    ai_setup, worker_train, pest_control,
    irrigation_pl, market_setup, logistics_pl
])
# add edges to enforce the sequence
seq = [
    (site_survey, structure_prep),
    (structure_prep, system_install),
    (system_install, env_control),
    (env_control, nutrient_mix),
    (nutrient_mix, crop_select),
    (crop_select, ai_setup),
    (ai_setup, worker_train),
    (worker_train, pest_control),
    (pest_control, irrigation_pl),
    (irrigation_pl, market_setup),
    (market_setup, logistics_pl)
]
for src, tgt in seq:
    initial_setup.order.add_edge(src, tgt)

# 2) Continuous analysis cycle (data collection & optimization)
analysis = StrictPartialOrder(nodes=[
    data_monitor, yield_forecast, energy_audit, waste_manage
])
# enforce the analysis order
analysis.order.add_edge(data_monitor, yield_forecast)
analysis.order.add_edge(yield_forecast, energy_audit)
analysis.order.add_edge(energy_audit, waste_manage)

# a silent transition to allow the loop to exit
skip = SilentTransition()

# the LOOP operator: run 'analysis' at least once, then either exit or repeat
analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[analysis, skip])

# 3) Assemble the root: the setup followed by the repeating analysis loop
root = StrictPartialOrder(nodes=[initial_setup, analysis_loop])
root.order.add_edge(initial_setup, analysis_loop)