def industry_growth(yyyymm):
    text = '''select B.INDUSTRY_NAME_1
        ,B.INDUSTRY_NAME_2
        ,ROUND(AVG(A.MOM), 2) AS AVG_MOM
        ,ROUND(AVG(A.YOY), 2) AS AVG_YOY
        ,ROUND(AVG(A.ACC_YOY), 2) AS AVG_ACC_YOY
        ,COUNT(*) AS CNT
    from SII_REV_{} A
    left join TEJ_STOCK_DATA_BASIC B
    on A.ID = B.ID
    where B.MKT = 'TSE'
    group by B.INDUSTRY_NAME_1, B.INDUSTRY_NAME_2
    order by AVG_ACC_YOY desc
    ;'''
    df = pd.read_sql_query(text.format(yyyymm), con=engine)
    return df
