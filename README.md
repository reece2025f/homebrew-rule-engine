 

1.0 Issue statement

. The client has disabilities affecting their energy levels and ability to function with extended tasks and has reported difficulties with manual overhead and cognitive strain, leading to a degradation of quality or avoidance altogether. This is what the project will attempt to solve by providing a bespoke solution to reduce friction, time and cognitive load.

. The client experiences issues most notably at scale. In the worst reported situations, the client can spend far over an hour a day on manual overhead; this can occur 2+ times a week. An example situation given was 5 minutes a character if 20 are in the scenario then this evaluates to (5*20=100) 

2.0 Project Purpose

To create a program to reduce the time spent on manual calculations 
reducing prep time, increasing efficiency, and reducing miscalculations

3.0 Program Requirements

A program to replace the inputting of the following homebrew ruleset 

.  Ability to input classes and levels for classes and multiclasses.

. Ability to input Constitution (Con) modifier

. Scalability in the number of classes to ensure long-term applicability

.  Calculate total health according to the formula

. Ensure readability to reduce friction upon displaying results.

4.0 Calculation Rules

. A character can have only 1 class active at a time.

. A character can have any number of (multi)classes at a given time.

Classes have a die assigned to them consisting of d6, d8, d10 and d12.

. A character can switch to any class at any given time, which requires recalculation.

. Any multiclasses are added as: main class health + (1/2 ) the average of the multiclass hit die, rounded down to a whole number ; for example, 3.5 becomes 3.

. The contribution of a multiclass is functionally unable to give more than the current  class's level; for example, if in a level 1 class, then every multiclass only contributes half the average of 1 hit die.

. A multiclass cannot contribute more than its total level in hit die; for example, if the current class is level 4 and a multiclass level 1, then it can only contribute half of 1 hit die, rounded down.

. Con bonus should not propagate down out of the current class; the multiclasses only contribute the hit die without a Con modifier attached.





5.0 Health Calculation Formulae
The formula is
[Main]
l1 (Main_HP_Base = Main_Hit_Die_Max + Con_Bonus)
l2+ (Main_HP_Progression = (Main_Hit_Die_Full_Avg + Con_Bonus) * (Main_Class_Level - 1))

[Multi]
Capped_Level = min(Multiclass_Level, Main_Class_Level)
Multiclass_HP = Multiclass_Hit_Die_Half_Avg * Capped_Level

[Total]
(Total_Health = max(1, Main_HP_Base + Main_HP_Progression + Sum(All_Multiclass_HP)))





6.0 Future Revision



. Ensure separation of concerns in functions.

. Migrate to a web application, with profiling, searchability, and JSON storage

. Make the web application automatically update other classes, e.g. if class 1 gains a level, display every class's new total HP next to their names, making level-ups only a single click.










