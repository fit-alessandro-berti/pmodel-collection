# Generated from: 42a73b56-90b8-4824-8853-9c8d3e41d154.json
# Description: This process outlines the complex steps required to establish a fully operational urban vertical farming facility in a metropolitan area. It involves site analysis, modular system design, climate control integration, crop selection based on microclimate data, automated nutrient delivery calibration, pest management without pesticides, staff training on hydroponics, real-time growth monitoring using IoT sensors, supply chain coordination for local distribution, sustainability assessment, community engagement programs, regulatory compliance checks, continuous yield optimization, and post-launch performance review to ensure scalability and profitability within the urban agriculture sector.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as transitions
site_survey        = Transition(label='Site Survey')
design_modules     = Transition(label='Design Modules')
climate_setup      = Transition(label='Climate Setup')
crop_select        = Transition(label='Crop Select')
nutrient_calibrate = Transition(label='Nutrient Calibrate')
pest_control       = Transition(label='Pest Control')
staff_training     = Transition(label='Staff Training')
sensor_deploy      = Transition(label='Sensor Deploy')
growth_monitor     = Transition(label='Growth Monitor')
supply_align       = Transition(label='Supply Align')
sustainability_chk = Transition(label='Sustainability Check')
community_outreach = Transition(label='Community Outreach')
compliance_audit   = Transition(label='Compliance Audit')
yield_optimize     = Transition(label='Yield Optimize')
performance_review = Transition(label='Performance Review')

# Create the partial order with all nodes
root = StrictPartialOrder(nodes=[
    site_survey,
    design_modules,
    climate_setup,
    crop_select,
    nutrient_calibrate,
    pest_control,
    staff_training,
    sensor_deploy,
    growth_monitor,
    supply_align,
    sustainability_chk,
    community_outreach,
    compliance_audit,
    yield_optimize,
    performance_review
])

# Add edges to enforce the intended sequence
sequence = [
    site_survey,
    design_modules,
    climate_setup,
    crop_select,
    nutrient_calibrate,
    pest_control,
    staff_training,
    sensor_deploy,
    growth_monitor,
    supply_align,
    sustainability_chk,
    community_outreach,
    compliance_audit,
    yield_optimize,
    performance_review
]
for src, tgt in zip(sequence, sequence[1:]):
    root.order.add_edge(src, tgt)