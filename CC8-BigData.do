clear all

import delimited "/Users/rosario/Downloads/db_prices.csv", clear 


//We are going to work with SMOKELESS FUEL 50KG(420103) and KEROSENE - 1000L DELIVERED (420405)

keep if item_id== 420405 | item_id==420103

gen date_stata = date(date2, "DMY")

format date_stata %td

scatter price date_stata if item_id==420103

scatter price date_stata if item_id==420405

collapse (mean) price, by(item_id region date_stata)
 
export delimited using /Users/rosario/Downloads/db_final.csv
