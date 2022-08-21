import numpy as np
def calculate(List):
    lst = np.array(List)
    print(lst)
    mean_row = [lst[[0,1,2]].mean(),lst[[3,4,5]].mean(),lst[[6,7,8]].mean()]
    mean_col = [lst[[0,3,5]].mean(),lst[[1,4,6]].mean(),lst[[2,5,8]].mean()]

    variance_row = [lst[[0,1,2]].var(),lst[[3,4,5]].var(),lst[[6,7,8]].var()]
    variance_col = [lst[[0,3,5]].var(),lst[[1,4,6]].var(),lst[[2,5,8]].var()]

    std_row = [lst[[0,1,2]].std(),lst[[3,4,5]].std(),lst[[6,7,8]].std()]
    std_col = [lst[[0,3,5]].std(),lst[[1,4,6]].std(),lst[[2,5,8]].std()]

    max_row = [lst[[0,1,2]].max(),lst[[3,4,5]].max(),lst[[6,7,8]].max()]
    max_col = [lst[[0,3,5]].max(),lst[[1,4,6]].max(),lst[[2,5,8]].max()]

    min_row = [lst[[0,1,2]].min(),lst[[3,4,5]].min(),lst[[6,7,8]].min()]
    min_col = [lst[[0,3,5]].min(),lst[[1,4,6]].min(),lst[[2,5,8]].min()]
    
    sum_row = [lst[[0,1,2]].sum(),lst[[3,4,5]].sum(),lst[[6,7,8]].sum()]
    sum_col = [lst[[0,3,5]].sum(),lst[[1,4,6]].sum(),lst[[2,5,8]].sum()]

    return {
  'mean': [mean_row, mean_col, lst.mean()],
  'variance': [variance_row, variance_col, lst.var()],
  'standard deviation': [std_row, std_col, lst.std()],
  'max': [max_row, max_col, lst.max()],
  'min': [min_row, min_col, lst.min()],
  'sum': [sum_row, sum_col, lst.sum()]
}

print(calculate([1,2,3,4,5,6,7,8,9]))

