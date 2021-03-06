import seaborn as sns
from matplotlib.font_manager import FontProperties
sns.set(font=['sans-serif'])
sns.set_style("whitegrid",{"font.sans-serif":['Microsoft JhengHei']})
plt.figure(figsize=(12,7))
sns.barplot(x="INDUSTRY_NAME_2", y="AVG_ACC_YOY", data=df_2018_growth.head(10))
plt.xlabel('產業名', fontsize=15)
plt.ylabel('營收年增率(%)', fontsize=15)
