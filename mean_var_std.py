import numpy as np

def calculate(list):
  
  if len(list) < 9: raise ValueError('List must contain nine numbers.')
  
  c = dict()
  l = list.copy()
  m = np.array(l).reshape((3,3))

  c['mean'] = [m.mean(axis=0).tolist(), m.mean(axis=1).tolist(), m.mean().tolist()]
  c['variance'] = [m.var(axis=0).tolist(), m.var(axis=1).tolist(), m.var().tolist()]
  c['standard deviation'] = [m.std(axis=0).tolist(), m.std(axis=1).tolist(), m.std().tolist()]
  c['max'] = [m.max(axis=0).tolist(), m.max(axis=1).tolist(), m.max().tolist()]
  c['min'] = [m.min(axis=0).tolist(), m.min(axis=1).tolist(), m.min().tolist()]
  c['sum'] = [m.sum(axis=0).tolist(), m.sum(axis=1).tolist(), m.sum().tolist()]  
  
  return c