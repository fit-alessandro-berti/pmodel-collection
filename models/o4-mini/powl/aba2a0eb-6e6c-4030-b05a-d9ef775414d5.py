# Generated from: aba2a0eb-6e6c-4030-b05a-d9ef775414d5.json
# Description: This process involves the complex orchestration of establishing an urban vertical farm within a constrained city environment. It starts with site assessment and zoning compliance, followed by modular infrastructure design and procurement. The process continues with climate system integration, hydroponic nutrient programming, and automated lighting calibration. Concurrently, staff training on biosecurity and crop monitoring is conducted. Post-installation, the process includes iterative testing of growth cycles, data analytics for yield optimization, pest control protocols, and community engagement for local distribution. Finally, the operation undergoes sustainability auditing and scalability planning to ensure long-term viability within urban agriculture paradigms.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey      = Transition(label='Site Survey')
zoning_check     = Transition(label='Zoning Check')
design_layout    = Transition(label='Design Layout')
material_order   = Transition(label='Material Order')
climate_setup    = Transition(label='Climate Setup')
nutrient_mix     = Transition(label='Nutrient Mix')
light_calibrate  = Transition(label='Light Calibrate')
staff_training   = Transition(label='Staff Training')
biosecurity_audit= Transition(label='Biosecurity Audit')
growth_testing   = Transition(label='Growth Testing')
data_analysis    = Transition(label='Data Analysis')
pest_control     = Transition(label='Pest Control')
community_meet   = Transition(label='Community Meet')
sustain_audit    = Transition(label='Sustain Audit')
scale_planning   = Transition(label='Scale Planning')

# Define the growth-testing loop: do Growth Testing, then Data Analysis, then optionally repeat
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_testing, data_analysis])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    zoning_check,
    design_layout,
    material_order,
    climate_setup,
    nutrient_mix,
    light_calibrate,
    staff_training,
    biosecurity_audit,
    growth_loop,
    pest_control,
    community_meet,
    sustain_audit,
    scale_planning
])

# Sequential setup up to calibration
root.order.add_edge(site_survey, zoning_check)
root.order.add_edge(zoning_check, design_layout)
root.order.add_edge(design_layout, material_order)
root.order.add_edge(material_order, climate_setup)
root.order.add_edge(climate_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, light_calibrate)

# Concurrent staff training and biosecurity after calibration
root.order.add_edge(light_calibrate, staff_training)
root.order.add_edge(light_calibrate, biosecurity_audit)

# Both must complete before starting the iterative growth-testing loop
root.order.add_edge(staff_training, growth_loop)
root.order.add_edge(biosecurity_audit, growth_loop)

# After loop, proceed with pest control, community meet, sustainability audit, and scalability planning
root.order.add_edge(growth_loop, pest_control)
root.order.add_edge(pest_control, community_meet)
root.order.add_edge(community_meet, sustain_audit)
root.order.add_edge(sustain_audit, scale_planning)