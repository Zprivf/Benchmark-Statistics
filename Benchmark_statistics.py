##############################
# Python code to make statistical comparison between USGS and model outputs. 
# Fitsume Wolkeba
# fwolkeba@crimson.ua.edu
# Last edited: 3/26/2024
#############################


# !pip install hydroeval
import pandas as pd
import hydroeval as he
import matplotlib.dates
from datetime import datetime
from dataretrieval import nwis
from IPython.display import display
from datetime import date
pd.options.mode.chained_assignment = None

def stat_eval_at_point(file1_path,file2_path):
    df1_r = pd.read_csv(file1_path)
    df2_r = pd.read_csv(file2_path,encoding='latin1')
    df1_r['Datetime']=pd.to_datetime(df1_r['Datetime'])
    df1_r['Datetime']=df1_r['Datetime'].dt.strftime('%Y-%m-%d')
    df2_r['Datetime']=pd.to_datetime(df2_r['Datetime'])
    df2_r['Datetime']=df2_r['Datetime'].dt.strftime('%Y-%m-%d')
    df1_r = pd.DataFrame(df1_r)
    df2_r = pd.DataFrame(df2_r)
    df1_r_name = df1_r.columns[6]
    df2_r_name = df2_r.columns[1]
    df=pd.merge(left=df1_r, right=df2_r,on='Datetime',how='inner')
    df.dropna ()
    data_1=df[df1_r_name]
    data_2=df[df2_r_name]
    nse_cpc=he.evaluator(he.nse,data_1,data_2)
    kge_cpc, r_cpc, alpha_cpc, beta_cpc = he.evaluator(he.kge, data_1,data_2)
    print("NWM vs USGS","NSE=",nse_cpc,"KGE=",kge_cpc, "r=",r_cpc)
    
    return

# Set the parameters needed for the web service call

def Get_USGS_and_compute_statistics(siteID,startDate,endDate,NWM_data_path):
    # Get the data
    discharge = nwis.get_iv(sites=siteID, parameterCd="00060", start=startDate, end=endDate)
    site = pd.DataFrame(discharge[0])
    site.reset_index(inplace=True)                                        
    site['Datetime'] = pd.to_datetime(site['datetime'], utc=True,format='%Y-%m-%d %H:%M:%S')   
    site_copy = site.copy()
    site_copy['Datetime'] = pd.to_datetime(site_copy['datetime'],utc=True, format='%Y-%m-%d %H:%M:%S')                                        
    site_copy.index = site_copy['Datetime']                                         
    site_avg = site_copy['00060'].resample('d').mean()
    site_avg_num=site_avg.apply(pd.to_numeric)
    usgs_df = site_avg_num.to_frame(name='USGS_flow')
    usgs_df.reset_index(inplace=True)
    df1_r = pd.read_csv(NWM_data_path) # NWM or other
    df2_r = usgs_df                # USGS from nwis


    df1_r['Datetime']=pd.to_datetime(df1_r['Datetime'])#,format='%m/%d/%Y')
    df1_r['Datetime']=df1_r['Datetime'].dt.strftime('%Y-%m-%d')
    df2_r['Datetime']=pd.to_datetime(df2_r['Datetime'])
    df2_r['Datetime']=df2_r['Datetime'].dt.strftime('%Y-%m-%d')
    df1_r = pd.DataFrame(df1_r)
    df2_r = pd.DataFrame(df2_r)
    
    df1_r_name = df1_r.columns[6]
    df2_r_name = df2_r.columns[1]


    df=pd.merge(left=df1_r, right=df2_r,on='Datetime',how='inner')
    df.dropna ()

    data_1=df[df1_r_name]
    data_2=df[df2_r_name]
    nse_cpc=he.evaluator(he.nse,data_1,data_2)
    kge_cpc, r_cpc, alpha_cpc, beta_cpc = he.evaluator(he.kge, data_1,data_2)
    print("data 1 (NWM) vs USGS","NSE=",nse_cpc,"KGE=",kge_cpc, "r=",r_cpc)
    return
