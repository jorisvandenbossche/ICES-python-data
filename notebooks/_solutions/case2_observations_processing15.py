species_data.loc[species_data["species_id"] == "NE", "species_id"] = "NA"

# note: for such a 1:1 replacement, we could also use the "replace()" method
# species_data["species_id"] = species_data["species_id"].replace({"NE": "NA"})