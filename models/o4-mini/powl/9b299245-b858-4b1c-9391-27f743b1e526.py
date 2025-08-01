# Generated from: 9b299245-b858-4b1c-9391-27f743b1e526.json
# Description: This process outlines the establishment of a vertical farming facility in an urban environment, integrating advanced hydroponic systems with IoT monitoring and renewable energy sources. It involves site selection considering zoning laws, procuring modular grow units, installing climate control, and integrating AI-driven nutrient delivery. The workflow includes stakeholder coordination, regulatory compliance verification, staff training for automated systems, and launching pilot crop cycles. Continuous monitoring and iterative adjustments optimize yield and energy usage, while waste recycling strategies enhance sustainability. The process culminates in establishing distribution partnerships for fresh produce within local markets, ensuring a closed-loop urban agriculture model that addresses food security and environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey   = Transition(label="Site Survey")
permit_check  = Transition(label="Permit Check")
module_order  = Transition(label="Module Order")
foundation_prep = Transition(label="Foundation Prep")
unit_install  = Transition(label="Unit Install")
hydro_setup   = Transition(label="Hydro Setup")
climate_config = Transition(label="Climate Config")
iot_deploy    = Transition(label="IoT Deploy")
ai_integrate  = Transition(label="AI Integrate")
system_test   = Transition(label="System Test")
staff_train   = Transition(label="Staff Train")
pilot_plant   = Transition(label="Pilot Plant")
monitor_data  = Transition(label="Monitor Data")
yield_adjust  = Transition(label="Yield Adjust")
waste_cycle   = Transition(label="Waste Cycle")
market_link   = Transition(label="Market Link")
report_review = Transition(label="Report Review")

# Loop body: yield adjust then waste cycle
loop_body = StrictPartialOrder(
    nodes=[yield_adjust, waste_cycle]
)
loop_body.order.add_edge(yield_adjust, waste_cycle)

# Loop: monitor data, then optionally (yield_adjust -> waste_cycle) and back
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitor_data, loop_body]
)

# Main partial order
root = StrictPartialOrder(
    nodes=[
        site_survey,
        permit_check,
        module_order,
        foundation_prep,
        unit_install,
        hydro_setup,
        climate_config,
        iot_deploy,
        ai_integrate,
        system_test,
        staff_train,
        pilot_plant,
        monitor_loop,
        market_link,
        report_review
    ]
)

# Define the control-flow edges
root.order.add_edge(site_survey,   permit_check)
root.order.add_edge(permit_check,  module_order)
root.order.add_edge(permit_check,  foundation_prep)
root.order.add_edge(module_order,  unit_install)
root.order.add_edge(foundation_prep, unit_install)
root.order.add_edge(unit_install,  hydro_setup)
root.order.add_edge(hydro_setup,   climate_config)
root.order.add_edge(climate_config, iot_deploy)
root.order.add_edge(iot_deploy,    ai_integrate)
root.order.add_edge(ai_integrate,  system_test)
root.order.add_edge(system_test,   staff_train)
root.order.add_edge(staff_train,   pilot_plant)
root.order.add_edge(pilot_plant,   monitor_loop)
root.order.add_edge(monitor_loop,  market_link)
root.order.add_edge(market_link,   report_review)