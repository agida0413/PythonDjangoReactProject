#render = > forward => "경로명/jsp명"
import recipe_models
from django.shortcuts import render,redirect

from django.http import JsonResponse
def recipe_llist(request):
    try:
        page=request.GET('page')
    except Exception as e:
        page="1"

    curpage=int(page)
    recipeList=recipe_models.recipeListData(curpage)
    totalpage=recipe_models.recipeTotalPage()

    BLOCK=10
    startPage=((curpage-1)/BLOCK*BLOCK)+1
    endPage=((curpage-1)/BLOCK*BLOCK)+BLOCK

    if endPage>totalpage:
        endPage=totalpage

    rd=[]
    """
    [
        (1,"","",""),
        (),
        ().....
    ]
    """
    for recipe in recipeList:
        rdata={"no":recipe[0],"title":recipe[1],"poster":recipe[2],"chef":recipe[3]}
        rd.append(rdata)

    recipt_data={
        "recipe_list":rd,
        "curpage":int(curpage),
        "totalpage":int(totalpage),
        "startPage":int(startPage),
        "endPage":int(endPage)
    }
    return JsonResponse(recipt_data)

def recipe_list_view(request):
    return render(request,"recipe/list.html")