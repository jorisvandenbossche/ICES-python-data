fl_motowar_20s = casualties[(casualties["region"]=="Flemish Region") & 
                            (casualties["road_type"] == "Motorway") &
                            (casualties["road_user_type"] =="Passenger car") &
                            (casualties["victim_type"] =="Driver") &
                            (casualties["age"].isin(["30 - 34", "35 - 39"]))
                           ]