# Generated from: 87e0ba80-3d37-4eee-80ae-bc3dc971130a.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farming system within a repurposed industrial building. It starts with site evaluation and environmental analysis, followed by modular farm design and infrastructure retrofitting. Subsequent activities include hydroponic system installation, automated climate control setup, nutrient solution calibration, and crop selection based on urban demand analytics. The process further involves staff training for system operation, IoT sensor integration for real-time monitoring, pest control strategy implementation, and energy consumption optimization. It concludes with market launch preparations, ongoing yield assessment, and iterative process improvements to ensure sustainable, high-efficiency urban food production in constrained spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

SiteEval = Transition(label='Site Eval')
EnvAnalysis = Transition(label='Env Analysis')

DesignModules = Transition(label='Design Modules')
RetrofitBuild = Transition(label='Retrofit Build')

InstallHydroponics = Transition(label='Install Hydroponics')
SetupClimate = Transition(label='Setup Climate')
CalibrateNutrients = Transition(label='Calibrate Nutrients')
SelectCrops = Transition(label='Select Crops')

TrainStaff = Transition(label='Train Staff')
IntegrateSensors = Transition(label='Integrate Sensors')
ImplementPest = Transition(label='Implement Pest')
OptimizeEnergy = Transition(label='Optimize Energy')

LaunchMarket = Transition(label='Launch Market')
AssessYield = Transition(label='Assess Yield')
ImproveProcess = Transition(label='Improve Process')

# Phase 1: Site Eval -> Env Analysis
phase1 = StrictPartialOrder(nodes=[SiteEval, EnvAnalysis])
phase1.order.add_edge(SiteEval, EnvAnalysis)

# Phase 2: Design Modules -> Retrofit Build
phase2 = StrictPartialOrder(nodes=[DesignModules, RetrofitBuild])
phase2.order.add_edge(DesignModules, RetrofitBuild)

# Phase 3: hydroponics installation and related steps in sequence:
phase3 = StrictPartialOrder(
    nodes=[InstallHydroponics, SetupClimate, CalibrateNutrients, SelectCrops]
)
phase3.order.add_edge(InstallHydroponics, SetupClimate)
phase3.order.add_edge(SetupClimate, CalibrateNutrients)
phase3.order.add_edge(CalibrateNutrients, SelectCrops)

# Phase 4: Staff training and sensor integration in parallel, followed by pest control and energy optimization in parallel
# The description says: staff training, IoT sensor integration, pest control, and energy optimization
# The last two can be parallel, but order is not stated explicit - we assume training & sensor are parallel, pest & energy parallel, 
# and both groups end before market launch
# So, create two partial orders for these sets

# Staff Training and Sensor Integration concurrent
staff_sensors = StrictPartialOrder(nodes=[TrainStaff, IntegrateSensors])
# no edges: concurrent

# Pest control and energy optimization concurrent
pest_energy = StrictPartialOrder(nodes=[ImplementPest, OptimizeEnergy])
# no edges: concurrent

# Combine staff_sensors and pest_energy in one PO with no order between them (concurrent)
phase4 = StrictPartialOrder(nodes=[staff_sensors, pest_energy])
# They are concurrent so no edges between staff_sensors and pest_energy, but their nodes are composite POWL nodes.
# To combine them properly, flatten nodes:
# This is not allowed because StrictPartialOrder expects Transition/Silent/OperatorPOWL nodes, staff_sensors and pest_energy are StrictPartialOrders.
# Instead, define phase4 as a single StrictPartialOrder with all 4 individual transitions, no order:

phase4 = StrictPartialOrder(nodes=[TrainStaff, IntegrateSensors, ImplementPest, OptimizeEnergy])
# no edges: fully concurrent

# Phase 5: Launch Market -> Assess Yield -> Improve Process
phase5 = StrictPartialOrder(nodes=[LaunchMarket, AssessYield, ImproveProcess])
phase5.order.add_edge(LaunchMarket, AssessYield)
phase5.order.add_edge(AssessYield, ImproveProcess)

# Now we compose the global process partial order over the phases

# The overall order:
# phase1 -> phase2 -> phase3 -> phase4 -> phase5

# Combine phases as nodes and enforce the order as edges

root = StrictPartialOrder(nodes=[phase1, phase2, phase3, phase4, phase5])
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, phase3)
root.order.add_edge(phase3, phase4)
root.order.add_edge(phase4, phase5)