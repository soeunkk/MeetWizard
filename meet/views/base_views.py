from django.shortcuts import redirect, render, HttpResponsePermanentRedirect
from meet.models import Location, Schedule, Friend, TemporaryFriend, Group, GroupMember
from accounts.models import User
from django.contrib.auth.decorators import login_required

"""
* leftType: 왼쪽 고정창 유형
    0: 없음, 1: 비회원용 프로필, 2: 회원용 프로필, 3: STEP 설명
"""

def index(request):
    param = {
        'leftType':0,   
    }
    return render(request, 'meet/index.html', param)


#비회원용 홈페이지
def nonmemberhome(request):
    param = {
        'leftType':1,       
    }
    if request.method=="POST": 
        return render(request, 'meet/nonmemberhome.html', param)
            # #POST로 전달된 값 변수에 저장
            # group_name = request.POST["group_name"]                 #group_name: 그룹명
            # group_members = request.POST.getlist("group_member")    #group_members: 멤버(친구들 중 체크박스 true인 목록)
    return render(request, 'meet/nonmemberhome.html', param)


#회원용 홈페이지

def home(request):
    if not request.user.is_authenticated:   #로그인되어 있지 않으면 비회원용으로 redirect
        return redirect("nonmemberhome")

    param = {
        'leftType':2,   
        'location':Location.objects.filter(user=request.user).first(),
        'schedules':Schedule.objects.filter(user=request.user),
    }
    return render(request, 'meet/home.html', param)