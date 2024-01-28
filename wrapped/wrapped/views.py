from django.shortcuts import render
from new_account.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

@login_required
def wrapped_view(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)  # Adjust if UserProfile is accessed differently
   
    #delete this later
    number = '49'
    user_profile.tearsq1 += ',' + number
    user_profile.save()
    user_profile.tearsq2 = '100'
    user_profile.save()
    user_profile.tearsq2 += ',' + number
    user_profile.save()
    user_profile.tearsq3 = 'private,public,public,public,private,public,private'
    user_profile.save()
    #^delete

    user_tears1 = user_profile.tearsq1.split(',') if user_profile.tearsq1 else []
    user_tears2 = user_profile.tearsq2.split(',') if user_profile.tearsq2 else []
    user_tears3 = user_profile.tearsq3.split(',') if user_profile.tearsq3 else []
    user_tears4 = user_profile.tearsq4.split(',') if user_profile.tearsq4 else []
    user_tears5 = user_profile.tearsq5.split(',') if user_profile.tearsq5 else []
    user_tears6 = user_profile.tearsq6.split(',') if user_profile.tearsq6 else []

    all_tears = []
    for amount in user_tears1:
        all_tears.append(int(amount))
    if len(all_tears) == 0:
        length_at = 1
    else: length_at = len(all_tears)

    time_tears = []
    for time in user_tears2:
        time_tears.append(int(time))
    if len(time_tears) == 0:
        length_tt = 1
    else: length_tt = len(time_tears)


    pub_num = user_tears3.count('public')
    priv_num = user_tears3.count('private')
    if pub_num > priv_num:
        pub_or_priv = 'public'
    elif priv_num > pub_num:
        pub_or_priv = 'private'
    else: pub_or_priv = 'both equal'

    pub_or_priv_num = max(pub_num, priv_num)
    
    tr1 = user_tears4.count('1')
    tr2 = user_tears4.count('2')
    tr3 = user_tears4.count('3')
    tr4 = user_tears4.count('4')
    tr5 = user_tears4.count('5')
    mostreason_num = max(tr1,tr2,tr3,tr4,tr5)
    if mostreason_num == tr1:
        tears_reason = 'Happy tears ftw!'
    elif mostreason_num == tr2:
        tears_reason = 'Something you watched made you cry'
    elif mostreason_num == tr3:
        tears_reason = 'Someone hurted you :('
    elif mostreason_num == tr4:
        tears_reason = 'School is being rough and tough'
    elif mostreason_num == tr5:
        tears_reason = 'You cried for absolutely no reason'

    rank_tears = []
    for rank in user_tears5:
        rank_tears.append(int(rank))
    if len(rank_tears) == 0:
        length_rt = 1
    else:
        length_rt = len(rank_tears)



    user_party1 = user_profile.partyq1
    categories = user_profile.categories.split(',') if user_profile.categories else []
    return render(request, 'wrapped/wrapped.html', {
        'username': user.username,
        'email': user.email,
        'categories': categories,
        'tears': max(all_tears),
        'tears_average': sum(all_tears)/length_at,
        'tears_time_average': sum(time_tears)/length_tt,
        'tears_pub_or_priv': pub_or_priv,
        'tears_pub_or_priv_num': pub_or_priv_num,
        'tears_reason': tears_reason,
        'tears_reason_num': mostreason_num,
        'tears_rank_ave': sum(rank_tears)/length_rt,
        'tears_people_watch': len(user_tears6),
        'party': user_party1
    })
