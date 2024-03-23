from django.db import models
#VueJS
import oracledb
from web import models
def recipeListData(page):
    try:
        conn=models.getConnection()
        cursor=conn.cursor()
        rowSize=20
        start=(rowSize*page)-(rowSize-1)
        end=(rowSize*page)
        sql=f"""
             SELECT no,title,poster,chef,num 
             FROM (SELECT no,title,poster,chef,rownum as num
             FROM (SELECT no,title,poster,chef 
             FROM recipe WHERE no IN(SELECT no FROM recipe 
             INTERSECT SELECT no FROM recipeDetail)
             ORDER BY no ASC ))
             WHERE num BETWEEN {start} AND {end}
             
             """
        cursor.execute(sql)
        recipe_list=cursor.fetchall()
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)
    return recipe_list

def recipeTotalPage():
        try:
            conn=models.getConnection()
            cursor=conn.cursor()
            sql="""
                SELECT CEIL(COUNT(*)/20.0) FROM recipe
                WHERE no IN(SELECT no FROM recipe 
                INTERSECT SELECT no FROM recipeDetail)
                """
            cursor.execute(sql)
            total=cursor.fetchone()
            cursor.close()
            conn.close()
        except Exception as e:
            print(e)
        return total