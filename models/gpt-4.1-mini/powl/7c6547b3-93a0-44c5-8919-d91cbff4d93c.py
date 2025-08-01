# Generated from: 7c6547b3-93a0-44c5-8919-d91cbff4d93c.json
# Description: This process outlines the complex steps involved in establishing a vertical farming operation within an urban environment. It includes site selection based on environmental and logistical factors, integration of advanced hydroponic systems, and deployment of automated climate control technologies. Regulatory compliance and community engagement ensure sustainable and socially responsible development. Continuous monitoring and data analytics optimize crop yield and resource efficiency, while supply chain coordination facilitates timely distribution to local markets. The process concludes with staff training and iterative system improvements to adapt to changing urban conditions and consumer demands.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Site_Survey = Transition(label='Site Survey')
Regulation_Check = Transition(label='Regulation Check')
Design_Layout = Transition(label='Design Layout')
Tech_Integration = Transition(label='Tech Integration')
Hydroponic_Setup = Transition(label='Hydroponic Setup')
Climate_Control = Transition(label='Climate Control')
Sensor_Install = Transition(label='Sensor Install')
Water_Testing = Transition(label='Water Testing')
Energy_Audit = Transition(label='Energy Audit')
Supplier_Vetting = Transition(label='Supplier Vetting')
Community_Meet = Transition(label='Community Meet')
Staff_Hiring = Transition(label='Staff Hiring')
Training_Session = Transition(label='Training Session')
Crop_Planning = Transition(label='Crop Planning')
Yield_Monitoring = Transition(label='Yield Monitoring')
Data_Analysis = Transition(label='Data Analysis')
Market_Prep = Transition(label='Market Prep')
Logistics_Plan = Transition(label='Logistics Plan')
Feedback_Review = Transition(label='Feedback Review')
System_Upgrade = Transition(label='System Upgrade')

skip = SilentTransition()

# Step 1: Site Survey and Regulation Check (presumably sequential)
site_reg = StrictPartialOrder(nodes=[Site_Survey, Regulation_Check])
site_reg.order.add_edge(Site_Survey, Regulation_Check)

# Step 2: Design Layout after Regulation Check
design = StrictPartialOrder(nodes=[Regulation_Check, Design_Layout])
design.order.add_edge(Regulation_Check, Design_Layout)

# Step 3: Tech Integration after Design Layout
tech = StrictPartialOrder(nodes=[Design_Layout, Tech_Integration])
tech.order.add_edge(Design_Layout, Tech_Integration)

# Step 4: Hydroponic Setup after Tech Integration
hydro = StrictPartialOrder(nodes=[Tech_Integration, Hydroponic_Setup])
hydro.order.add_edge(Tech_Integration, Hydroponic_Setup)

# Step 5: Climate Control & Sensor Install & Water Testing & Energy Audit concurrent after Hydroponic Setup
climate = Climate_Control
sensor = Sensor_Install
water = Water_Testing
energy = Energy_Audit

env_nodes = [Hydroponic_Setup, climate, sensor, water, energy]
env = StrictPartialOrder(nodes=env_nodes)
env.order.add_edge(Hydroponic_Setup, climate)
env.order.add_edge(Hydroponic_Setup, sensor)
env.order.add_edge(Hydroponic_Setup, water)
env.order.add_edge(Hydroponic_Setup, energy)

# Step 6: Supplier Vetting and Community Meet concurrent but must start after Regulation Check and partially after Energy Audit 
# For simplicity, start after Regulation Check and Energy Audit (assuming they represent compliance and audit)
supplier_community = StrictPartialOrder(nodes=[Regulation_Check, Energy_Audit, Supplier_Vetting, Community_Meet])
supplier_community.order.add_edge(Regulation_Check, Supplier_Vetting)
supplier_community.order.add_edge(Regulation_Check, Community_Meet)
supplier_community.order.add_edge(Energy_Audit, Supplier_Vetting)
supplier_community.order.add_edge(Energy_Audit, Community_Meet)

# Combine Environmental setup and supplier-community in parallel after Hydroponic_Setup
# But Supplier_Vetting and Community_Meet depend on Regulation_Check and Energy_Audit (already established)

# Step 7: Staff Hiring after Supplier Vetting and Community Meet (socially responsible development)
staff = StrictPartialOrder(nodes=[Supplier_Vetting, Community_Meet, Staff_Hiring])
staff.order.add_edge(Supplier_Vetting, Staff_Hiring)
staff.order.add_edge(Community_Meet, Staff_Hiring)

# Step 8: Training Session after Staff Hiring
training = StrictPartialOrder(nodes=[Staff_Hiring, Training_Session])
training.order.add_edge(Staff_Hiring, Training_Session)

# Step 9: Crop Planning after Climate Control and Sensor Install
crop = StrictPartialOrder(nodes=[climate, sensor, Crop_Planning])
crop.order.add_edge(climate, Crop_Planning)
crop.order.add_edge(sensor, Crop_Planning)

# Step 10: Yield Monitoring and Data Analysis concurrent after Crop Planning
yield_data = StrictPartialOrder(nodes=[Crop_Planning, Yield_Monitoring, Data_Analysis])
yield_data.order.add_edge(Crop_Planning, Yield_Monitoring)
yield_data.order.add_edge(Crop_Planning, Data_Analysis)

# Step 11: Market Prep and Logistics Plan concurrent after Yield Monitoring and Data Analysis
market_logistics = StrictPartialOrder(nodes=[Yield_Monitoring, Data_Analysis, Market_Prep, Logistics_Plan])
market_logistics.order.add_edge(Yield_Monitoring, Market_Prep)
market_logistics.order.add_edge(Yield_Monitoring, Logistics_Plan)
market_logistics.order.add_edge(Data_Analysis, Market_Prep)
market_logistics.order.add_edge(Data_Analysis, Logistics_Plan)

# Step 12: Feedback Review and System Upgrade in a loop with Training Session for iterative improvements
# Loop body: Feedback Review followed by System Upgrade
# Loop condition: after Training Session
loop_body = StrictPartialOrder(nodes=[Feedback_Review, System_Upgrade])
loop_body.order.add_edge(Feedback_Review, System_Upgrade)

# Construct loop: execute Training Session, then optionally repeat Feedback Review + System Upgrade then Training Session
loop = OperatorPOWL(operator=Operator.LOOP, children=[Training_Session, loop_body])

# Now build the full partial order:

# First group: site_reg, design, tech, hydro, env
sdth_nodes = [site_reg, design, tech, hydro, env]
sdth = StrictPartialOrder(nodes=sdth_nodes)
sdth.order.add_edge(site_reg, design)
sdth.order.add_edge(design, tech)
sdth.order.add_edge(tech, hydro)
sdth.order.add_edge(hydro, env)

# Then supplier_community and staff (supplier_community depends on Regulation_Check and Energy_Audit inside env)
# For simplicity, supplier_community after env, staff after supplier_community
scs_nodes = [env, supplier_community, staff]
scs = StrictPartialOrder(nodes=scs_nodes)
scs.order.add_edge(env, supplier_community)
scs.order.add_edge(supplier_community, staff)

# Crop planning after env (Climate_Control and Sensor_Install inside env)
crop_planning_group = StrictPartialOrder(nodes=[env, crop])
crop_planning_group.order.add_edge(env, crop)

# Yield and data after crop planning
yd_group = StrictPartialOrder(nodes=[crop, yield_data])
yd_group.order.add_edge(crop, yield_data)

# Market and logistics after yield/data
ml_group = StrictPartialOrder(nodes=[yield_data, market_logistics])
ml_group.order.add_edge(yield_data, market_logistics)

# Combine all together in order:
# sdth -> scs -> training loop simultaneously with crop/yield/market chain

# training loop after staff
train_loop_after_staff = StrictPartialOrder(nodes=[staff, loop])
train_loop_after_staff.order.add_edge(staff, loop)

# Combine crop to market chain into one PO
market_chain = StrictPartialOrder(nodes=[crop, yield_data, market_logistics])
market_chain.order.add_edge(crop, yield_data)
market_chain.order.add_edge(yield_data, market_logistics)

# Finally combine train_loop_after_staff and market_chain concurrently after staff/loop

root = StrictPartialOrder(nodes=[sdth, scs, train_loop_after_staff, market_chain])

# Ordering:
root.order.add_edge(sdth, scs)
root.order.add_edge(scs, train_loop_after_staff)
root.order.add_edge(scs, market_chain)
# train_loop_after_staff and market_chain can run concurrently after scs
