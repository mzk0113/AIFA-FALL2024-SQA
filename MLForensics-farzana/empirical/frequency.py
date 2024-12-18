'''
Akond Rahman 
Nov 15, 2020
Frequency: RQ2
'''
import numpy as np 
import os 
import pandas as pd 
import time 
import datetime

#Import logging for forensics
import logging

def initializeLogger():
    format_str = '%(asctime)s - %(levelname)s - %(message)s'
    file_name = 'mining.log'
    logging.basicConfig(format=format_str, filename=file_name, level=logging.INFO)
    return logging.getLogger('forensics-logger')

def giveTimeStamp():
  tsObj = time.time()
  strToret = datetime.datetime.fromtimestamp(tsObj).strftime( '%Y-%m-%d %H:%M:%S' ) 
  return strToret


def getAllSLOC(df_param, csv_encoding='latin-1' ):
    #Logs start of getAllSLOC
    logger.info("Starting SLOC calculation")
    total_sloc = 0
    all_files = np.unique( df_param['FILE_FULL_PATH'].tolist() ) 
    for file_ in all_files:
        total_sloc = total_sloc + sum(1 for line in open(file_, encoding=csv_encoding))

    #Logs completion of getAllSLOC and result
    logger.info(f"Total SLOC: {total_sloc}")
    return total_sloc

def reportProportion( res_file, output_file ):
    #Logs start of reportProportion and input 
    logger.info(f"Starting reportProportion with res_file: {res_file}, output_file: {output_file}")
    res_df = pd.read_csv( res_file )
    repo_names   = np.unique( res_df['REPO_FULL_PATH'].tolist() )
    
    fields2explore = ['DATA_LOAD_COUNT', 'MODEL_LOAD_COUNT', 'DATA_DOWNLOAD_COUNT',	'MODEL_LABEL_COUNT', 'MODEL_OUTPUT_COUNT',	
                    'DATA_PIPELINE_COUNT', 'ENVIRONMENT_COUNT', 'STATE_OBSERVE_COUNT',  'TOTAL_EVENT_COUNT'
                    ]
    df_list = [] 
    
    for repo in repo_names:
        print('-'*50) 
        print(repo)
        #Logs current repo processing
        logger.info(f"Processing repo: {repo}")
        repo_entity = res_df[res_df['REPO_FULL_PATH'] == repo ]           
        all_py_files   = np.unique( repo_entity['FILE_FULL_PATH'].tolist() )
        for field in fields2explore:
            field_atleast_one_df = repo_entity[repo_entity[field] > 0 ]
            atleast_one_files    = np.unique( field_atleast_one_df['FILE_FULL_PATH'].tolist() )
            prop_metric          = round(float(len( atleast_one_files ) )/float(len(all_py_files)) , 5) * 100
            logger.info(f"Repo: {repo}, Field: {field}, Prop_metric: {prop_metric}")
            print('TOTAL_FILES:{}, CATEGORY:{}, ATLEASTONE:{}, PROP_VAL:{}'.format( len(all_py_files), field, len(atleast_one_files) , prop_metric  ))
            print('-'*50) 
            
            the_tup = ( repo, len(all_py_files), field, len(atleast_one_files), prop_metric )
            df_list.append( the_tup )
            
    CSV_HEADER = ['REPO_NAME', 'TOTAL_FILES', 'CATEGORY', 'ATLEASTONE', 'PROP_VAL']
    full_df = pd.DataFrame( df_list ) 
    full_df.to_csv(output_file, header= CSV_HEADER, index=False, encoding= 'utf-8') 

    #Logs completion
    logger.info(f"Proportion report saved to {output_file}")


def reportEventDensity(res_file, output_file): 
    #Logs start
    logger.info(f"Starting reportEventDensity with res_file: {res_file}, output_file: {output_file}")
    
    res_df = pd.read_csv(res_file) 
    repo_names   = np.unique( res_df['REPO_FULL_PATH'].tolist() )
    fields2explore = ['DATA_LOAD_COUNT', 'MODEL_LOAD_COUNT', 'DATA_DOWNLOAD_COUNT',	'MODEL_LABEL_COUNT', 'MODEL_OUTPUT_COUNT',	
                      'DATA_PIPELINE_COUNT', 'ENVIRONMENT_COUNT', 'STATE_OBSERVE_COUNT',  'TOTAL_EVENT_COUNT'
                     ]
  
    df_list = [] 
    
    for repo in repo_names:
        print('-'*50) 
        print(repo)
        repo_entity = res_df[res_df['REPO_FULL_PATH'] == repo ]                         
        all_py_files   = np.unique( repo_entity['FILE_FULL_PATH'].tolist() )  
        all_py_size    = getAllSLOC(repo_entity) 
  
  
        for field in fields2explore:
            field_res_list  = repo_entity[field].tolist() 
            field_res_count = sum( field_res_list ) 
            event_density   = round( float(field_res_count * 1000 ) / float(all_py_size)  , 5) 
            print('TOTAL_LOC:{}, CATEGORY:{}, TOTAL_EVENT_COUNT:{}, EVENT_DENSITY:{}'.format( all_py_size, field, field_res_count, event_density )  )
            print('-'*25)
            
            the_tup = ( repo, all_py_size, field, field_res_count, event_density )
            df_list.append( the_tup )
            
    CSV_HEADER = ['REPO_NAME', 'TOTAL_LOC', 'CATEGORY', 'TOTAL_EVENT_COUNT', 'EVENT_DENSITY']
    full_df = pd.DataFrame( df_list ) 
    full_df.to_csv(output_file, header= CSV_HEADER, index=False, encoding= 'utf-8')

    #Logs info on output file
    logger.info(f"Event density report saved to {output_file}")

if __name__=='__main__': 

    #Creates logger
    logger = initializeLogger()

    #Logs correct initialization
    logger.info("frequency.py started")
  
    print('*'*100 )
    t1 = time.time()
    print('Started at:', giveTimeStamp() )
    print('*'*100 )


    # DATASET_NAME = 'TEST'
    # RESULTS_FILE = '/Users/arahman/Documents/OneDriveWingUp/OneDrive-TennesseeTechUniversity/Research/VulnStrategyMining/ForensicsinML/Output/V5_OUTPUT_TEST.csv'

#     RESULTS_FILE = 'V5_OUTPUT_MODELZOO.csv' 
#     PROPORTION_FILE = 'PROPORTION_MODELZOO.csv'   
#     DENSITY_FILE = 'DENSITY_MODELZOO.csv' 
    
#     RESULTS_FILE = 'V5_OUTPUT_GITLAB.csv' 
#     PROPORTION_FILE = 'PROPORTION_GITLAB.csv'   
#     DENSITY_FILE = 'DENSITY_GITLAB.csv' 
     
#     RESULTS_FILE = 'V5_OUTPUT_GITHUB.csv' 
#     PROPORTION_FILE = 'PROPORTION_GITHUB.csv'   
#     DENSITY_FILE = 'DENSITY_GITHUB.csv'   
    
    reportProportion( RESULTS_FILE, PROPORTION_FILE )
    print('*'*100) 
    reportEventDensity( RESULTS_FILE, DENSITY_FILE )
    print('*'*100) 

    print('*'*100 )
    print('Ended at:', giveTimeStamp() )
    print('*'*100 )
