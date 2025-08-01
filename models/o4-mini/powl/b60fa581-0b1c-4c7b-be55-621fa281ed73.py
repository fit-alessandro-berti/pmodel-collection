# Generated from: b60fa581-0b1c-4c7b-be55-621fa281ed73.json
# Description: This process outlines the setup of an urban vertical farming system within a repurposed industrial building. It involves site assessment, structural modifications, installation of hydroponic systems, integration of IoT sensors, and optimization of environmental controls. The process also includes staff training on automated nutrient delivery, pest management without chemicals, and continuous data monitoring to maximize crop yield and sustainability in an urban environment. Coordination with local authorities for zoning compliance and energy sourcing from renewable providers is essential to ensure regulatory adherence and minimize carbon footprint. The final phases focus on pilot crop cultivation, harvesting workflows, and market distribution planning tailored for urban consumers seeking fresh, locally grown produce.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_assess      = Transition(label='Site Assess')
struct_mod       = Transition(label='Structural Mod')
hydro_fit        = Transition(label='Hydroponic Fit')
iot_setup        = Transition(label='IoT Setup')
env_control      = Transition(label='Env Control')
nutrient_plan    = Transition(label='Nutrient Plan')
pest_monitor     = Transition(label='Pest Monitor')
data_review      = Transition(label='Data Review')
staff_train      = Transition(label='Staff Train')
energy_audit     = Transition(label='Energy Audit')
compliance_check = Transition(label='Compliance Check')
crop_pilot       = Transition(label='Crop Pilot')
harvest_prep     = Transition(label='Harvest Prep')
market_plan      = Transition(label='Market Plan')
waste_manage     = Transition(label='Waste Manage')
distribution     = Transition(label='Distribution')

# A silent transition to serve as the "exit" branch of the loop
skip = SilentTransition()

# Build a small partial‐order for one monitoring cycle: Nutrient Plan -> Pest Monitor -> Data Review
monitor_cycle = StrictPartialOrder(nodes=[nutrient_plan, pest_monitor, data_review])
monitor_cycle.order.add_edge(nutrient_plan, pest_monitor)
monitor_cycle.order.add_edge(pest_monitor, data_review)

# Wrap that in a LOOP operator: run one cycle, then either exit or repeat
loop_monitor = OperatorPOWL(operator=Operator.LOOP, children=[monitor_cycle, skip])

# Build the top‐level partial order
root = StrictPartialOrder(
    nodes=[
        site_assess,
        struct_mod,
        hydro_fit,
        iot_setup,
        env_control,
        energy_audit,
        compliance_check,
        staff_train,
        waste_manage,
        loop_monitor,
        crop_pilot,
        harvest_prep,
        market_plan,
        distribution
    ]
)

# Sequential setup up to environment control
root.order.add_edge(site_assess, struct_mod)
root.order.add_edge(struct_mod, hydro_fit)
root.order.add_edge(hydro_fit, iot_setup)
root.order.add_edge(iot_setup, env_control)

# After Env Control, five branches execute concurrently:
#   - Energy Audit
#   - Compliance Check
#   - Staff Training
#   - Waste Management
#   - Continuous Monitoring Loop
for nxt in [energy_audit, compliance_check, staff_train, waste_manage, loop_monitor]:
    root.order.add_edge(env_control, nxt)

# All five branches must complete before the pilot crop phase
for prev in [energy_audit, compliance_check, staff_train, waste_manage, loop_monitor]:
    root.order.add_edge(prev, crop_pilot)

# Final linear phases: Pilot -> Harvest Prep -> Market Plan -> Distribution
root.order.add_edge(crop_pilot, harvest_prep)
root.order.add_edge(harvest_prep, market_plan)
root.order.add_edge(market_plan, distribution)