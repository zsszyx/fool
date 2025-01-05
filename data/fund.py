import akshare as ak

def fund_report_asset_allocation_cninfo():
    fund_report_asset_allocation_cninfo_df = ak.fund_report_asset_allocation_cninfo()
    return fund_report_asset_allocation_cninfo_df.iloc[0]

print(fund_report_asset_allocation_cninfo())