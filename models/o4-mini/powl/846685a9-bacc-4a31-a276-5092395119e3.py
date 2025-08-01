# Generated from: 846685a9-bacc-4a31-a276-5092395119e3.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban vertical farm within a repurposed commercial building. It includes site assessment, environmental control system design, modular planting unit installation, nutrient solution preparation, and integration of IoT monitoring devices. The process also covers labor scheduling for planting cycles, pest management using biological controls, and data analytics for yield optimization. Additionally, it involves community engagement for local produce distribution, energy consumption audits, and continuous improvement through feedback loops, making it a multifaceted and atypical business operation in the agricultural technology sector.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey        = Transition(label='Site Survey')
design_layout      = Transition(label='Design Layout')
install_modules    = Transition(label='Install Modules')
setup_lighting     = Transition(label='Setup Lighting')
configure_sensors  = Transition(label='Configure Sensors')
prepare_nutrients  = Transition(label='Prepare Nutrients')
seed_planting      = Transition(label='Seed Planting')
monitor_growth     = Transition(label='Monitor Growth')
pest_control       = Transition(label='Pest Control')
data_collection    = Transition(label='Data Collection')
analyze_metrics    = Transition(label='Analyze Metrics')
schedule_labor     = Transition(label='Schedule Labor')
energy_audit       = Transition(label='Energy Audit')
community_outreach = Transition(label='Community Outreach')
feedback_review    = Transition(label='Feedback Review')
# separate instance for rework to avoid reuse in main flow
design_layout_rework = Transition(label='Design Layout')
yield_packaging    = Transition(label='Yield Packaging')
distribution_plan  = Transition(label='Distribution Plan')

# Define the growth cycle partial order
growth_po = StrictPartialOrder(nodes=[
    monitor_growth, pest_control, data_collection, analyze_metrics, schedule_labor
])
growth_po.order.add_edge(monitor_growth, pest_control)
growth_po.order.add_edge(pest_control, data_collection)
growth_po.order.add_edge(data_collection, analyze_metrics)
growth_po.order.add_edge(analyze_metrics, schedule_labor)

# Loop for planting cycles: seed planting then growth cycle repeatedly
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[seed_planting, growth_po])

# Loop for continuous improvement: feedback review then redesign layout
improvement_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_review, design_layout_rework])

# Top‐level partial order of the entire process
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    install_modules,
    setup_lighting,
    configure_sensors,
    prepare_nutrients,
    growth_loop,
    energy_audit,
    community_outreach,
    improvement_loop,
    yield_packaging,
    distribution_plan
])

# Define the control‐flow dependencies
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, install_modules)
root.order.add_edge(install_modules, setup_lighting)
root.order.add_edge(setup_lighting, configure_sensors)
root.order.add_edge(configure_sensors, prepare_nutrients)
root.order.add_edge(prepare_nutrients, growth_loop)
root.order.add_edge(growth_loop, energy_audit)
root.order.add_edge(energy_audit, community_outreach)
root.order.add_edge(community_outreach, improvement_loop)
root.order.add_edge(improvement_loop, yield_packaging)
root.order.add_edge(yield_packaging, distribution_plan)