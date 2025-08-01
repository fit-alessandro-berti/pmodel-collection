# Generated from: 51a84714-4aa4-4eed-8538-31b99405f0e6.json
# Description: This process describes the complex setup and operational launch of an urban vertical farm integrating hydroponics, IoT monitoring, and sustainable energy systems. It involves site analysis, modular infrastructure assembly, nutrient solution formulation, environmental calibration, and continuous crop monitoring. The process also includes stakeholder coordination, regulatory compliance checks, and iterative optimization of growth parameters to maximize yield and minimize resource consumption in a confined urban environment. Post-launch activities encompass data analytics integration, pest control automation, and community engagement to ensure long-term sustainability and scalability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey      = Transition(label='Site Survey')
design_layout    = Transition(label='Design Layout')
procure_modules  = Transition(label='Procure Modules')
assemble_fw      = Transition(label='Assemble Framework')
install_sensors  = Transition(label='Install Sensors')
energy_sync      = Transition(label='Energy Sync')
setup_irrigation = Transition(label='Setup Irrigation')
stakeholder_meet = Transition(label='Stakeholder Meet')
compliance_chk   = Transition(label='Compliance Check')
formulate_nut    = Transition(label='Formulate Nutrients')
calibrate_clim   = Transition(label='Calibrate Climate')
seed_planting    = Transition(label='Seed Planting')
mon_growth       = Transition(label='Monitor Growth')
pest_inspect     = Transition(label='Pest Inspection')
data_integrate   = Transition(label='Data Integration')
yield_analysis   = Transition(label='Yield Analysis')
sys_optimize     = Transition(label='System Optimization')

# Define loops
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[mon_growth, pest_inspect])
opt_loop    = OperatorPOWL(operator=Operator.LOOP, children=[yield_analysis, sys_optimize])

# Build the overall partial order model
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    procure_modules,
    assemble_fw,
    install_sensors,
    energy_sync,
    setup_irrigation,
    stakeholder_meet,
    compliance_chk,
    formulate_nut,
    calibrate_clim,
    seed_planting,
    growth_loop,
    data_integrate,
    opt_loop
])

# Define the control-flow/order relations
root.order.add_edge(site_survey,      design_layout)
root.order.add_edge(design_layout,    procure_modules)
root.order.add_edge(procure_modules,  assemble_fw)
root.order.add_edge(assemble_fw,      install_sensors)
root.order.add_edge(install_sensors,  energy_sync)
root.order.add_edge(energy_sync,      setup_irrigation)

# Stakeholder coordination and compliance in parallel
root.order.add_edge(setup_irrigation, stakeholder_meet)
root.order.add_edge(setup_irrigation, compliance_chk)
# Join before nutrient formulation
root.order.add_edge(stakeholder_meet, formulate_nut)
root.order.add_edge(compliance_chk,   formulate_nut)

root.order.add_edge(formulate_nut,    calibrate_clim)
root.order.add_edge(calibrate_clim,   seed_planting)

# Launch loop of growth monitoring and pest inspection
root.order.add_edge(seed_planting,    growth_loop)

# Post-launch data integration and optimization loop
root.order.add_edge(growth_loop,      data_integrate)
root.order.add_edge(data_integrate,   opt_loop)