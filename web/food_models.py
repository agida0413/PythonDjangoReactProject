from django.db import models
import oracledb
from web import models
def foodListData(page):
    try:
        conn=models.getConnection()
        cursor=conn.cursor()
        rowSize=20

        start =(rowSize*page)-(rowSize-1)
        end=rowSize*page

        sql=f"""
            SELECT fno,name,poster,num 
            FROM (SELECT fno,name,poster,rownum as num
            FROM (SELECT fno,name,poster 
            FROM food_menu_house ORDER BY fno ASC))
            WHERE num BETWEEN {start} AND {end}
            """
        cursor.execute(sql)

        food_list =cursor.fetchall()
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)

    return food_list

def foodTotalPage():
    try:
        conn=models.getConnection()
        cursor=conn.cursor()
        sql="""
            SELECT CEIL(COUNT(*)/20.0) FROM food_menu_house
            """
        cursor.execute(sql)
        total=cursor.fetchone()
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)
    return total[0]

def foodCount():
    try:
        conn=models.getConnection()
        cursor=conn.cursor()
        sql="""
            SELECT COUNT(*) FROM food_menu_house
            """
        cursor.execute(sql)
        count=cursor.fetchone()
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)
    return count[0]

# 검색
def foodFindData(page,address):
    try:
        conn=models.getConnection()
        cursor=conn.cursor()
        rowSize=20

        start =(rowSize*page)-(rowSize-1)
        end=rowSize*page

        sql=f"""
            SELECT fno,name,poster,num 
            FROM (SELECT fno,name,poster,rownum as num
            FROM (SELECT fno,name,poster 
            FROM food_menu_house WHERE address LIKE '%'||'{address}'||'%' 
            ORDER BY fno ASC))
            WHERE num BETWEEN {start} AND {end}
            """
        cursor.execute(sql)
        food_list = cursor.fetchall()
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)

    return food_list

def foodfindTotalPage(address):
    try:
        conn=models.getConnection()
        cursor=conn.cursor()
        sql=f"""
            SELECT CEIL(COUNT(*)/20.0) FROM food_menu_house 
            WHERE address LIKE '%'||'{address}'||'%'  
            """
        cursor.execute(sql)
        total=cursor.fetchone()
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)
    return total[0]

def foodfindCount(address):
    try:
        conn=models.getConnection()
        cursor=conn.cursor()
        sql=f"""
            SELECT COUNT(*) FROM food_menu_house
            WHERE address LIKE '%'||'{address}'||'%' 
            """
        cursor.execute(sql)
        count=cursor.fetchone()
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)
    return count[0]