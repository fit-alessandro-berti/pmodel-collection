# Generated from: bad30472-856a-4e8e-9330-a743762f8d33.json
# Description: This process outlines the establishment of an urban vertical farm within a repurposed industrial building. It includes site assessment, modular system design, nutrient cycling integration, climate control calibration, automated seeding, continuous environmental monitoring, pest bio-control application, energy consumption optimization, waste recycling protocols, data-driven yield forecasting, community engagement for local produce distribution, regulatory compliance verification, and adaptive scaling strategies to maximize sustainable food production in dense urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_assess      = Transition(label="Site Assess")
design_modules   = Transition(label="Design Modules")
install_systems  = Transition(label="Install Systems")
calibrate_climate= Transition(label="Calibrate Climate")
seed_automation  = Transition(label="Seed Automation")

monitor_sensors  = Transition(label="Monitor Sensors")
apply_biocontrols= Transition(label="Apply Biocontrols")
optimize_energy  = Transition(label="Optimize Energy")
recycle_waste    = Transition(label="Recycle Waste")
forecast_yield   = Transition(label="Forecast Yield")
report_metrics   = Transition(label="Report Metrics")

verify_compliance= Transition(label="Verify Compliance")
train_staff      = Transition(label="Train Staff")
scale_operations = Transition(label="Scale Operations")
engage_community = Transition(label="Engage Community")

# Build the operational cycle as a strict partial order
operational_cycle = StrictPartialOrder(nodes=[
    monitor_sensors,
    apply_biocontrols,
    optimize_energy,
    recycle_waste,
    forecast_yield,
    report_metrics
])
operational_cycle.order.add_edge(monitor_sensors, apply_biocontrols)
operational_cycle.order.add_edge(apply_biocontrols, optimize_energy)
operational_cycle.order.add_edge(optimize_energy, recycle_waste)
operational_cycle.order.add_edge(recycle_waste, forecast_yield)
operational_cycle.order.add_edge(forecast_yield, report_metrics)

# Define the LOOP operator: perform the operational cycle repeatedly
skip = SilentTransition()
operation_loop = OperatorPOWL(operator=Operator.LOOP, children=[operational_cycle, skip])

# Assemble the whole process in a top‐level strict partial order
root = StrictPartialOrder(nodes=[
    site_assess,
    design_modules,
    install_systems,
    calibrate_climate,
    seed_automation,
    operation_loop,
    verify_compliance,
    train_staff,
    scale_operations,
    engage_community
])
root.order.add_edge(site_assess, design_modules)
root.order.add_edge(design_modules, install_systems)
root.order.add_edge(install_systems, calibrate_climate)
root.order.add_edge(calibrate_climate, seed_automation)
root.order.add_edge(seed_automation, operation_loop)
root.order.add_edge(operation_loop, verify_compliance)
root.order.add_edge(verify_compliance, train_staff)
root.order.add_edge(train_staff, scale_operations)
root.order.add_edge(scale_operations, engage_community)