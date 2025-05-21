# functions for converting filepaths between different systems

def correct_path(path, path_type):
    if path_type == "server":
        return path
    if path_type == "mac":
        newpath = path.replace('/mnt/external.data/','/Volumes/external.data/')
        return newpath
    if path_type == "wsl":
        newpath = path.replace('/mnt/external.data/','/mnt/izbkingston/')
        return newpath
    
def correct_save_path(df, path_type, col_names=['raw_filepath', 'denoised_filepath']):
    if path_type == "server":
        return df
    if path_type == "mac":
        for col in col_names:
            df[col] = df[col].str.replace('/Volumes/external.data/','/mnt/external.data/')
        return df
    if path_type == "wsl":
        for col in col_names:
            df[col] = df[col].str.replace('/mnt/izbkingston/','/mnt/external.data/')
        return df

def correct_loaded_path(df, path_type, col_names=['raw_filepath', 'denoised_filepath']):
    if path_type == "server":
        return df
    if path_type == "mac":
        for col in col_names:
            df[col] = df[col].str.replace('/mnt/external.data/','/Volumes/external.data/')
        return df
    if path_type == "wsl":
        for col in col_names:
            df[col] = df[col].str.replace('/mnt/external.data/','/mnt/izbkingston/')
        return df