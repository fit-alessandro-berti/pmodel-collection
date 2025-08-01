# Generated from: 5b89c0b0-a593-4a2f-8658-5511343652c1.json
# Description: This process describes the setup and optimization of an urban vertical farm, integrating hydroponic systems with IoT sensors and AI-driven environmental controls. It involves site analysis, modular rack assembly, nutrient solution formulation, seed selection, sensor calibration, and continuous monitoring to maximize crop yield while minimizing resource consumption. The process also includes staff training, compliance checks with urban agricultural regulations, pest management using biocontrol agents, and data analytics for predictive harvest scheduling. Additionally, it covers the marketing strategy for local distribution channels and sustainability reporting for stakeholders.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
tsurvey   = Transition(label="Site Survey")
rassembly = Transition(label="Rack Assembly")
nmix      = Transition(label="Nutrient Mix")
schoice   = Transition(label="Seed Choice")
sensor    = Transition(label="Sensor Setup")
sysconfig = Transition(label="System Config")
wtest     = Transition(label="Water Testing")
ltune     = Transition(label="Lighting Tune")
gmonitor  = Transition(label="Growth Monitor")
pcontrol  = Transition(label="Pest Control")
strain    = Transition(label="Staff Train")
raudit    = Transition(label="Regulation Audit")
yforecast = Transition(label="Yield Forecast")
dreview   = Transition(label="Data Review")
mplan     = Transition(label="Market Plan")
sreport   = Transition(label="Sustain Report")

# Silent transition for loop second child
skip = SilentTransition()

# Build the monitoring & control loop body: Water Testing → Lighting Tune → Growth Monitor → Pest Control
monitor_body = StrictPartialOrder(nodes=[wtest, ltune, gmonitor, pcontrol])
monitor_body.order.add_edge(wtest, ltune)
monitor_body.order.add_edge(ltune, gmonitor)
monitor_body.order.add_edge(gmonitor, pcontrol)

# LOOP operator: execute monitor_body, then either exit or skip→monitor_body again
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_body, skip])

# Root partial order: describes the entire process
root = StrictPartialOrder(
    nodes=[
        tsurvey,
        rassembly, nmix, schoice, strain,
        sensor, sysconfig,
        raudit,
        monitor_loop,
        yforecast, dreview, mplan, sreport
    ]
)

# 1. Site Survey → {Rack Assembly, Nutrient Mix, Seed Choice, Staff Train} (all in parallel)
root.order.add_edge(tsurvey, rassembly)
root.order.add_edge(tsurvey, nmix)
root.order.add_edge(tsurvey, schoice)
root.order.add_edge(tsurvey, strain)

# 2. After assembly/mix/choice/train → Sensor Setup & System Config
for pred in [rassembly, nmix, schoice, strain]:
    root.order.add_edge(pred, sensor)
    root.order.add_edge(pred, sysconfig)

# 3. Sensor Setup & System Config → Regulation Audit
root.order.add_edge(sensor, raudit)
root.order.add_edge(sysconfig, raudit)

# 4. Regulation Audit → Monitoring & Control Loop
root.order.add_edge(raudit, monitor_loop)

# 5. After loop → Yield Forecast → Data Review → Market Plan → Sustain Report
root.order.add_edge(monitor_loop, yforecast)
root.order.add_edge(yforecast, dreview)
root.order.add_edge(dreview, mplan)
root.order.add_edge(mplan, sreport)