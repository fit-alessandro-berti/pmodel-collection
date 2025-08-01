# Generated from: 09e4cbf7-12fe-451f-9877-cdd9ac6a819d.json
# Description: This process outlines the complex implementation of an urban vertical farming system within a densely populated city environment. It involves site evaluation, modular farm design, environmental control integration, resource logistics, crop selection based on microclimate data, advanced automation setup, continuous monitoring, and community engagement. The process also incorporates adaptive pest management strategies, energy optimization protocols, and real-time data analytics to ensure sustainable crop production. Additionally, it integrates waste recycling loops and supply chain coordination with local markets to maximize efficiency and reduce environmental impact. Coordination among multidisciplinary teams including agronomists, engineers, urban planners, and IT specialists is critical for successful deployment and scalability of the farming system.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey     = Transition(label='Site Survey')
design_layout   = Transition(label='Design Layout')
climate_study   = Transition(label='Climate Study')
resource_plan   = Transition(label='Resource Plan')
modular_build   = Transition(label='Modular Build')
sensor_install  = Transition(label='Sensor Install')
automation_setup= Transition(label='Automation Setup')
crop_select     = Transition(label='Crop Select')
irrigation_tune = Transition(label='Irrigation Tune')
pest_control    = Transition(label='Pest Control')
data_monitor    = Transition(label='Data Monitor')
waste_cycle     = Transition(label='Waste Cycle')
energy_audit    = Transition(label='Energy Audit')
market_link     = Transition(label='Market Link')
team_sync       = Transition(label='Team Sync')
feedback_loop   = Transition(label='Feedback Loop')
scale_review    = Transition(label='Scale Review')

# Loop for continuous monitoring and feedback
monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_monitor, feedback_loop])

# Build the partial order model
root = StrictPartialOrder(nodes=[
    site_survey, design_layout, climate_study, resource_plan,
    modular_build, sensor_install, automation_setup,
    crop_select, irrigation_tune, pest_control,
    waste_cycle, energy_audit, market_link,
    monitoring_loop, team_sync, scale_review
])

# 1. Initial site survey leads to design, climate study, and resource planning (can run in parallel)
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(site_survey, climate_study)
root.order.add_edge(site_survey, resource_plan)

# 2. Once design, climate study, and resource plan are done, begin modular build
root.order.add_edge(design_layout, modular_build)
root.order.add_edge(climate_study, modular_build)
root.order.add_edge(resource_plan, modular_build)

# 3. Build leads to sensor installation then automation setup
root.order.add_edge(modular_build, sensor_install)
root.order.add_edge(sensor_install, automation_setup)

# 4. Climate study informs crop selection
root.order.add_edge(climate_study, crop_select)

# 5. Automation setup informs irrigation tuning
root.order.add_edge(automation_setup, irrigation_tune)

# 6. Crop selection and irrigation tuning inform pest control
root.order.add_edge(crop_select, pest_control)
root.order.add_edge(irrigation_tune, pest_control)

# 7. Pest control enables waste cycling, energy audits, and market linking (can run in parallel)
root.order.add_edge(pest_control, waste_cycle)
root.order.add_edge(pest_control, energy_audit)
root.order.add_edge(pest_control, market_link)

# 8. After those, enter the monitoring-feedback loop
root.order.add_edge(waste_cycle, monitoring_loop)
root.order.add_edge(energy_audit, monitoring_loop)
root.order.add_edge(market_link, monitoring_loop)

# 9. After the loop finishes, sync teams and perform scale review
root.order.add_edge(monitoring_loop, team_sync)
root.order.add_edge(team_sync, scale_review)