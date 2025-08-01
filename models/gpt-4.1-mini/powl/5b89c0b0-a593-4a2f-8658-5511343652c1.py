# Generated from: 5b89c0b0-a593-4a2f-8658-5511343652c1.json
# Description: This process describes the setup and optimization of an urban vertical farm, integrating hydroponic systems with IoT sensors and AI-driven environmental controls. It involves site analysis, modular rack assembly, nutrient solution formulation, seed selection, sensor calibration, and continuous monitoring to maximize crop yield while minimizing resource consumption. The process also includes staff training, compliance checks with urban agricultural regulations, pest management using biocontrol agents, and data analytics for predictive harvest scheduling. Additionally, it covers the marketing strategy for local distribution channels and sustainability reporting for stakeholders.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey = Transition(label='Site Survey')
rack_assembly = Transition(label='Rack Assembly')
nutrient_mix = Transition(label='Nutrient Mix')
seed_choice = Transition(label='Seed Choice')
sensor_setup = Transition(label='Sensor Setup')
system_config = Transition(label='System Config')
water_testing = Transition(label='Water Testing')
lighting_tune = Transition(label='Lighting Tune')
growth_monitor = Transition(label='Growth Monitor')
pest_control = Transition(label='Pest Control')
staff_train = Transition(label='Staff Train')
regulation_audit = Transition(label='Regulation Audit')
yield_forecast = Transition(label='Yield Forecast')
data_review = Transition(label='Data Review')
market_plan = Transition(label='Market Plan')
sustain_report = Transition(label='Sustain Report')

# Setup phase: Site Survey --> Rack Assembly --> Nutrient Mix & Seed Choice (concurrent)
setup_po = StrictPartialOrder(nodes=[site_survey, rack_assembly, nutrient_mix, seed_choice])
setup_po.order.add_edge(site_survey, rack_assembly)
setup_po.order.add_edge(rack_assembly, nutrient_mix)
setup_po.order.add_edge(rack_assembly, seed_choice)

# Sensor & system configuration: Sensor Setup --> System Config --> Water Testing & Lighting Tune (concurrent)
sensor_po = StrictPartialOrder(nodes=[sensor_setup, system_config, water_testing, lighting_tune])
sensor_po.order.add_edge(sensor_setup, system_config)
sensor_po.order.add_edge(system_config, water_testing)
sensor_po.order.add_edge(system_config, lighting_tune)

# Monitoring loop: (* (Growth Monitor, Pest Control))
# Execute Growth Monitor, then choose to exit or do Pest Control and repeat
monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, pest_control])

# Staff and compliance parallel after monitoring start: Staff Train & Regulation Audit (concurrent)
staff_compliance_po = StrictPartialOrder(nodes=[staff_train, regulation_audit])

# Data analytics chain: Yield Forecast --> Data Review
data_analytics_po = StrictPartialOrder(nodes=[yield_forecast, data_review])
data_analytics_po.order.add_edge(yield_forecast, data_review)

# Marketing and sustainability parallel (concurrent)
market_sustain_po = StrictPartialOrder(nodes=[market_plan, sustain_report])

# Compose main partial order combining all

# Order dependencies:
# setup_po --> sensor_po --> monitoring_loop
# monitoring_loop --> staff_compliance_po and data_analytics_po (concurrent)
# data_analytics_po --> market_sustain_po

nodes_all = [
    setup_po,
    sensor_po,
    monitoring_loop,
    staff_compliance_po,
    data_analytics_po,
    market_sustain_po
]

root = StrictPartialOrder(nodes=nodes_all)
root.order.add_edge(setup_po, sensor_po)
root.order.add_edge(sensor_po, monitoring_loop)
root.order.add_edge(monitoring_loop, staff_compliance_po)
root.order.add_edge(monitoring_loop, data_analytics_po)
root.order.add_edge(data_analytics_po, market_sustain_po)