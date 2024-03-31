data = {
  'employment_types': {
    'data_struct_name': 'employment_types',
    'file_names': {
      'small'   : 'Data/small-employments_types.csv',
      'medium'  : 'Data/medium-employments_types.csv',
      'large'   : 'Data/large-employments_types.csv',
    },
    'key': 'id',
    'field_names':['type','id','currency_salary','salary_from','salary_to']
  },
  'jobs': {
    'data_struct_name': 'jobs',
    'file_names': {
      'small'   : 'Data/small-jobs.csv',
      'medium'  : 'Data/medium-jobs.csv',
      'large'   : 'Data/large-jobs.csv',
    },
    'key': 'id',
    'field_names': None
  },
  'multilocations': {
    'data_struct_name': 'multilocations',
    'file_names': {
      'small'   : 'Data/small-multilocations.csv',
      'medium'  : 'Data/medium-multilocations.csv',
      'large'   : 'Data/large-multilocations.csv',
    },
    'key': 'id',
    'field_names':['city','street','id']
  },
  'skills': {
    'data_struct_name': 'skills',
    'file_names': {
      'small'   : 'Data/small-skills.csv',
      'medium'  : 'Data/medium-skills.csv',
      'large'   : 'Data/large-skills.csv',
    },
    'key': 'id',
    'field_names':['name','level','id']
  }
}

def get_csv_data(id,size):
    csv_data = data[id]
    csv_data['file_name'] = csv_data['file_names'][size]
    return csv_data