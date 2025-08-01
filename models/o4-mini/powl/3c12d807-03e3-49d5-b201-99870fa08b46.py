# Generated from: 3c12d807-03e3-49d5-b201-99870fa08b46.json
# Description: This process outlines the complex steps involved in establishing a vertical farming operation within an urban environment. It includes site analysis for structural suitability, environmental impact assessment, resource logistics coordination, specialized equipment procurement, modular farm assembly, hydroponic system calibration, nutrient solution formulation, integrated pest management planning, real-time monitoring setup using IoT sensors, staff training in crop management, regulatory compliance verification, community engagement initiatives, yield forecasting, and continuous optimization based on data analytics to ensure sustainable production and profitability in constrained urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey     = Transition(label='Site Survey')
impact_study    = Transition(label='Impact Study')
resource_plan   = Transition(label='Resource Plan')
vendor_select   = Transition(label='Vendor Select')
equipment_order = Transition(label='Equipment Order')
module_build    = Transition(label='Module Build')
hydroponic_setup= Transition(label='Hydroponic Setup')
solution_mix    = Transition(label='Solution Mix')
pest_control    = Transition(label='Pest Control')
sensor_setup    = Transition(label='Sensor Setup')
staff_train     = Transition(label='Staff Train')
compliance_check= Transition(label='Compliance Check')
community_meet  = Transition(label='Community Meet')
yield_forecast  = Transition(label='Yield Forecast')
data_review     = Transition(label='Data Review')

# Build the main sequence as a strict partial order
seq = StrictPartialOrder(nodes=[
    site_survey,
    impact_study,
    resource_plan,
    vendor_select,
    equipment_order,
    module_build,
    hydroponic_setup,
    solution_mix,
    pest_control,
    sensor_setup,
    staff_train,
    compliance_check,
    community_meet,
    yield_forecast,
    data_review
])
# Add sequential dependencies
seq.order.add_edge(site_survey, impact_study)
seq.order.add_edge(impact_study, resource_plan)
seq.order.add_edge(resource_plan, vendor_select)
seq.order.add_edge(vendor_select, equipment_order)
seq.order.add_edge(equipment_order, module_build)
seq.order.add_edge(module_build, hydroponic_setup)
seq.order.add_edge(hydroponic_setup, solution_mix)
seq.order.add_edge(solution_mix, pest_control)
seq.order.add_edge(pest_control, sensor_setup)
seq.order.add_edge(sensor_setup, staff_train)
seq.order.add_edge(staff_train, compliance_check)
seq.order.add_edge(compliance_check, community_meet)
seq.order.add_edge(community_meet, yield_forecast)
seq.order.add_edge(yield_forecast, data_review)

# Silent transition to enable repeated optimization cycles
skip = SilentTransition()

# Wrap in a loop: run the full sequence, then either exit or repeat
root = OperatorPOWL(operator=Operator.LOOP, children=[seq, skip])