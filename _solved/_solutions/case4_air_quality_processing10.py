def read_airbase_file(filename, station):
    """
    Read hourly AirBase data files.
    
    Parameters
    ----------
    filename : string
        Path to the data file.
    station : string
        Name of the station.
       
    Returns
    -------
    DataFrame
        Processed dataframe.
    """
    
    # construct the column names    
    hours = ["{:02d}".format(i) for i in range(24)]
    flags = ['flag' + str(i) for i in range(24)]
    colnames = ['date'] + [item for pair in zip(hours, flags) for item in pair]
    
    # read the actual data
    data = pd.read_csv(filename, sep='\t', header=None, na_values=[-999, -9999], names=colnames)
    
    # drop the 'flag' columns
    data = data.drop([col for col in data.columns if 'flag' in col], axis=1)

    # reshape
    data_stacked = pd.melt(data, id_vars=['date'], var_name='hour')
    
    # parse to datetime and remove redundant columns 
    data_stacked.index = pd.to_datetime(data_stacked['date'] + data_stacked['hour'], format="%Y-%m-%d%H")
    data_stacked = data_stacked.drop(['date', 'hour'], axis=1)
    data_stacked = data_stacked.rename(columns={'value': station})
    
    return data_stacked