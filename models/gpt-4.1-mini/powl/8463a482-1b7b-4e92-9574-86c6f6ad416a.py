# Generated from: 8463a482-1b7b-4e92-9574-86c6f6ad416a.json
# Description: This process involves managing a multi-level urban vertical farm that integrates hydroponic and aeroponic systems to optimize crop yield within limited city spaces. It covers seed selection based on seasonal data, nutrient solution preparation, automated climate control adjustments, pest detection through AI imaging, and yield forecasting. Additionally, it includes waste recycling mechanisms, labor scheduling, real-time monitoring dashboards, and coordination with local markets for distribution. The process ensures sustainability by balancing energy consumption with renewable sources and maintaining strict quality standards through continuous sensor feedback and manual inspections.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Seed_Selection = Transition(label='Seed Selection')
Nutrient_Mix = Transition(label='Nutrient Mix')
Climate_Setup = Transition(label='Climate Setup')
Planting_Cycle = Transition(label='Planting Cycle')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Scan = Transition(label='Pest Scan')
Waste_Sorting = Transition(label='Waste Sorting')
Energy_Audit = Transition(label='Energy Audit')
Water_Recycle = Transition(label='Water Recycle')
Yield_Forecast = Transition(label='Yield Forecast')
Labor_Assign = Transition(label='Labor Assign')
Market_Sync = Transition(label='Market Sync')
Quality_Check = Transition(label='Quality Check')
Inventory_Log = Transition(label='Inventory Log')
Data_Backup = Transition(label='Data Backup')

# Model the loop of Planting Cycle and Growth Monitor, Pest Scan (monitor + pest scan repeated)
monitor_pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[Planting_Cycle, OperatorPOWL(operator=Operator.XOR, children=[Growth_Monitor, Pest_Scan])])

# Quality Check loop with continuous sensor feedback and manual inspection combined
# Represented as a partial order of Quality_Check, Inventory_Log, Data_Backup executed concurrently and repeated as a loop
qc_monitor = StrictPartialOrder(nodes=[Quality_Check, Inventory_Log, Data_Backup])
# No order edges here: these three activities are concurrent during quality control

quality_loop = OperatorPOWL(operator=Operator.LOOP, children=[qc_monitor, SilentTransition()])  # loop with silent transition for exit

# Waste recycling and energy audit concurrent with water recycle
waste_energy_water = StrictPartialOrder(nodes=[Waste_Sorting, Energy_Audit, Water_Recycle])
# no explicit order, concurrent

# Labor assign and Market sync concurrent, representing scheduling and distribution coordination
labor_market = StrictPartialOrder(nodes=[Labor_Assign, Market_Sync])
# no explicit order here, concurrent

# Sequence for initial steps: Seed Selection -> Nutrient Mix -> Climate Setup
initial_seq = StrictPartialOrder(nodes=[Seed_Selection, Nutrient_Mix, Climate_Setup])
initial_seq.order.add_edge(Seed_Selection, Nutrient_Mix)
initial_seq.order.add_edge(Nutrient_Mix, Climate_Setup)

# Yield Forecast happens after Growth Monitor and Pest Scan (after monitor_pest_loop)
# We model the yield forecast after finishing the loop
post_growth = StrictPartialOrder(nodes=[monitor_pest_loop, Yield_Forecast])
post_growth.order.add_edge(monitor_pest_loop, Yield_Forecast)

# Combine the parallel blocks after initial sequence and post growth/yield:
# - waste_energy_water
# - labor_market
# - quality_loop
# - Yield_Forecast (depends on monitor_pest_loop)
post_growth_and_parallel = StrictPartialOrder(nodes=[post_growth, waste_energy_water, labor_market, quality_loop])
# Yield Forecast depends on monitor_pest_loop inside post_growth already
# The parallel waste/energy/water, labor/market, and quality loop can proceed concurrently with Yield Forecast after growth

# To reflect that Yield_Forecast depends on post growth loop monitor,
# and that the three activities sets run in parallel with Yield_Forecast,
# no edges needed from yield to those sets; they're concurrent after monitor_pest_loop.

# Finally, connect initial_seq to post_growth_and_parallel: initial_seq --> post_growth_and_parallel
root = StrictPartialOrder(nodes=[initial_seq, post_growth_and_parallel])
root.order.add_edge(initial_seq, post_growth_and_parallel)