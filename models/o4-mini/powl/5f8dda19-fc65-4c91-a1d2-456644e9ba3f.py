# Generated from: 5f8dda19-fc65-4c91-a1d2-456644e9ba3f.json
# Description: This process outlines the establishment of a fully automated urban vertical farming system that integrates IoT sensors, renewable energy sources, and AI-driven crop management. It begins with site assessment and design planning, followed by modular farm assembly and installation of hydroponic and aeroponic units. The system is then calibrated with environmental sensors for humidity, temperature, and nutrient monitoring. Renewable energy solutions like solar panels and wind turbines are integrated to ensure sustainable operation. AI algorithms are trained to optimize growth cycles and detect plant diseases early. The process concludes with staff training, compliance checks, and launch of a real-time monitoring dashboard for continuous performance analysis and yield forecasting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
site_assess     = Transition(label='Site Assess')
design_plan     = Transition(label='Design Plan')
module_build    = Transition(label='Module Build')
unit_install    = Transition(label='Unit Install')
sensor_setup    = Transition(label='Sensor Setup')
calibrate_env   = Transition(label='Calibrate Enviro')
system_test     = Transition(label='System Test')
energy_integrate= Transition(label='Energy Integrate')
ai_train        = Transition(label='AI Train')
disease_detect  = Transition(label='Disease Detect')
growth_optimize = Transition(label='Growth Optimize')
staff_train     = Transition(label='Staff Train')
compliance_ch   = Transition(label='Compliance Check')
dashboard_launch= Transition(label='Dashboard Launch')
yield_forecast  = Transition(label='Yield Forecast')

# Build partial order
root = StrictPartialOrder(nodes=[
    site_assess, design_plan, module_build, unit_install,
    sensor_setup, calibrate_env, system_test, energy_integrate,
    ai_train, disease_detect, growth_optimize,
    staff_train, compliance_ch, dashboard_launch, yield_forecast
])

# Sequence edges
root.order.add_edge(site_assess,     design_plan)
root.order.add_edge(design_plan,     module_build)
root.order.add_edge(module_build,    unit_install)
root.order.add_edge(unit_install,    sensor_setup)
root.order.add_edge(sensor_setup,    calibrate_env)
root.order.add_edge(calibrate_env,   system_test)
root.order.add_edge(system_test,     energy_integrate)
root.order.add_edge(energy_integrate,ai_train)

# AI outputs run in parallel
root.order.add_edge(ai_train,        disease_detect)
root.order.add_edge(ai_train,        growth_optimize)

# Both AI tasks must complete before staff training
root.order.add_edge(disease_detect,  staff_train)
root.order.add_edge(growth_optimize, staff_train)

# Final sequence
root.order.add_edge(staff_train,     compliance_ch)
root.order.add_edge(compliance_ch,   dashboard_launch)
root.order.add_edge(dashboard_launch,yield_forecast)