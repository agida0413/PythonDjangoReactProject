from django.shortcuts import render,redirect
from web import food_models
from django.http import JsonResponse

def food_list(request):
    try:
        page=request.GET['page']
    except Exception as e:
        page="1"

    curpage = int(page)
    food_list=food_models.foodListData(curpage)
    totalpage=food_models.foodTotalPage()
    count=food_models.foodCount()

    BLOCK=10

    startpage=((curpage-1)/BLOCK*BLOCK)+1
    endpage=((curpage-1)/BLOCK*BLOCK)+BLOCK

    if(endpage>totalpage):
        endpage=totalpage
    fl=[]
    for f in food_list:
        fdata = {"fno": f[0], "name": f[1], "poster": f[2]}
        fl.append(fdata)
    food_data={
        "food_list":fl,
        "curpage":int(curpage),
        "totalpage":int(totalpage),
        "startpage":int(startpage),
        "endpage":int(endpage),
        "count":int(count),
        "range":range(int(startpage),int(endpage))
    }
    return render(request,"food/list.html",food_data)
    #return JsonResponse(food_data)

def food_find(request):
    try:
         page=request.GET['page']
    except Exception as e:
         page="1"
    try:
        address=request.GET['address']
    except Exception as e:
         address="마포"
    curpage = int(page)
    food_list = food_models.foodFindData(curpage,address)
    totalpage = food_models.foodfindTotalPage(address)
    count = food_models.foodfindCount(address)

    BLOCK = 10

    startpage = ((curpage - 1) / BLOCK * BLOCK) + 1
    endpage = ((curpage - 1) / BLOCK * BLOCK) + BLOCK

    if (endpage > totalpage):
        endpage = totalpage
    fl = []
    for f in food_list:
        fdata = {"fno": f[0], "name": f[1], "poster": f[2]}
        fl.append(fdata)
    food_data = {
        "food_list": fl,
        "curpage": int(curpage),
        "totalpage": int(totalpage),
        "startpage": int(startpage),
        "endpage": int(endpage),
        "count": int(count),
        "range": range(int(startpage), int(endpage)),
        "address": address
    }

    return render(request, "food/find.html",food_data)
