col_mapping = {name: name.removeprefix("TX_").removesuffix("_DESCR_NL") for name in casualties_nl.columns}
casualties = casualties_nl.rename(columns=col_mapping)
casualties.head()