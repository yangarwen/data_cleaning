'''以下為關於六種將DataFrame做型變的範例'''

# 創建一個dataframe (build a dataframe)
data = {
    'Product': ['A', 'A', 'A', 'B', 'B', 'B'],
    'Year': [2021, 2022, 2023, 2021, 2022, 2023],
    'Cost': [150, 200, 3999, 413, 574, 665],
    'Price': [600, 1000, 5000, 2500, 1460, 1000]
}
df = pd.DataFrame(data)

# 創建1:假設遇到的dataframe內有類似項目, 但不同名稱的情況
df_rn = df.rename(columns={"Cost": "Price_Cost", "Selling": "Price_Selling"})


# 創建2:假設遇到的dataframe是MultiIndex 狀況
df_si = df.set_index(['Product', 'Year'])

###-------------------------------------------------------------------

# 1.pivot()
df_pivot = df.pivot(index='Product', columns='Year', values='Cost')


# 2.pivot_table() 可做運算
pivot_df = df.pivot_table(index='Product', columns='Year', values='Cost', aggfunc='mean')


# 3.stack() 
df_stack = df_si.stack()


# 4.unstack() 
df_stack_unstack = df_stack.unstack()


# 5.melt()
df_melt = df.melt(id_vars=['Product', 'Year'], var_name='Type', value_name='Price')


# 6.wide_to_long()
df_wtl = pd.wide_to_long(df_rn, stubnames='Price', i=['Product','Year'], j='Type',  sep='_', suffix=r'\w+')











