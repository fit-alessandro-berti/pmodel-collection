# Generated from: 9cc12842-5f5e-40bb-bde3-8852a9154108.json
# Description: This process outlines the establishment of an urban vertical farm within a repurposed commercial building. It involves site analysis, modular rack installation, hydroponic system integration, nutrient cycling optimization, environmental control calibration, automated pest detection, crop scheduling, data-driven yield forecasting, waste recycling, energy consumption monitoring, and community engagement to ensure sustainability and profitability in a constrained urban environment. The process balances technology deployment with ecological principles and local regulations to create a scalable food production model that addresses urban food deserts and reduces supply chain emissions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
rack_setup = Transition(label='Rack Setup')
install_hydroponics = Transition(label='Install Hydroponics')
calibrate_sensors = Transition(label='Calibrate Sensors')
optimize_nutrients = Transition(label='Optimize Nutrients')
configure_lighting = Transition(label='Configure Lighting')
pest_detection = Transition(label='Pest Detection')
crop_scheduling = Transition(label='Crop Scheduling')
data_analysis = Transition(label='Data Analysis')
waste_processing = Transition(label='Waste Processing')
energy_monitoring = Transition(label='Energy Monitoring')
staff_training = Transition(label='Staff Training')
quality_check = Transition(label='Quality Check')
community_outreach = Transition(label='Community Outreach')

# Partial order for initial setup steps: site survey -> design layout -> rack setup -> install hydroponics
setup_po = StrictPartialOrder(
    nodes=[site_survey, design_layout, rack_setup, install_hydroponics]
)
setup_po.order.add_edge(site_survey, design_layout)
setup_po.order.add_edge(design_layout, rack_setup)
setup_po.order.add_edge(rack_setup, install_hydroponics)

# Partial order for calibration and optimization steps in parallel (concurrent)
# Calibrate Sensors, Optimize Nutrients, Configure Lighting happen concurrently after hydroponics installed
calib_opt_po = StrictPartialOrder(
    nodes=[calibrate_sensors, optimize_nutrients, configure_lighting]
)

# Partial order for monitoring and detection steps in parallel after calibration and optimization
# Pest Detection, Crop Scheduling, Data Analysis, Waste Processing, Energy Monitoring
monitor_nodes = [
    pest_detection,
    crop_scheduling,
    data_analysis,
    waste_processing,
    energy_monitoring,
]
monitor_po = StrictPartialOrder(nodes=monitor_nodes)

# Staff Training and Quality Check after monitoring activities - partial order
train_quality_po = StrictPartialOrder(nodes=[staff_training, quality_check])
train_quality_po.order.add_edge(staff_training, quality_check)

# Community Outreach last
# We model community outreach to occur after quality check
community_po = StrictPartialOrder(nodes=[community_outreach])

# Build overall ordering between blocks:
# setup_po --> calib_opt_po --> monitor_po --> train_quality_po --> community_po
root = StrictPartialOrder(
    nodes=[
        setup_po,
        calib_opt_po,
        monitor_po,
        train_quality_po,
        community_po,
    ]
)

root.order.add_edge(setup_po, calib_opt_po)
root.order.add_edge(calib_opt_po, monitor_po)
root.order.add_edge(monitor_po, train_quality_po)
root.order.add_edge(train_quality_po, community_po)