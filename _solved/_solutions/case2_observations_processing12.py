(survey_data_decoupled
     .groupby(survey_data_decoupled["eventDate"].dt.year)
     .size()
     .plot(kind='barh', color="#00007f", figsize=(10, 10)))