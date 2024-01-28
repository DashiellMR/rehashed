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

    user_tears1 = user_profile.tearsq1.split(',') if user_profile.tearsq1 else []
    user_tears2 = user_profile.tearsq2.split(',') if user_profile.tearsq2 else []
    user_tears3 = user_profile.tearsq3.split(',') if user_profile.tearsq3 else []
    user_tears4 = user_profile.tearsq4.split(',') if user_profile.tearsq4 else []
    user_tears5 = user_profile.tearsq5.split(',') if user_profile.tearsq5 else []
    user_tears6 = user_profile.tearsq6.split(',') if user_profile.tearsq6 else []

    user_party1 = user_profile.partyq1.split(',') if user_profile.partyq1 else []
    user_party2 = user_profile.partyq2.split(',') if user_profile.partyq2 else []
    user_party3 = user_profile.partyq3.split(',') if user_profile.partyq3 else []
    user_party4 = user_profile.partyq4.split(',') if user_profile.partyq4 else []

    user_gaming1 = user_profile.gamingq1.split(',') if user_profile.gamingq1 else []
    user_gaming2 = user_profile.gamingq1.split(',') if user_profile.gamingq1 else []

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


    time_party = []
    for time in user_party1:
        time_party.append(int(time))
    if len(time_party) == 0:
        length_tp = 1
    else: length_tp = len(time_party)

    drink_num = []
    for drink in user_party2:
        drink_num.append(int(drink))
    if len(drink_num)==0:
        length_dn = 1
    else: length_dn = len(drink_num)

    pl1 = user_party3.count('1')
    pl2 = user_party3.count('2')
    pl3 = user_party3.count('3')
    most_loc_num = max(pl1,pl2,pl3)
    if most_loc_num == pl1:
        party_loc = 'frat house'
    if most_loc_num == pl2:
        party_loc = 'club'
    if most_loc_num == pl3:
        party_loc = 'house party'

    pr1 = user_party4.count('1')
    pr2 = user_party4.count('2')
    pr3 = user_party4.count('3')
    pr4 = user_party4.count('4')
    pr5 = user_party4.count('5')
    mostreason_party = max(pr1,pr2,pr3,pr4,pr5)
    if mostreason_party == pr1:
        party_reason = 'Ceeeeelleebrate good times cmon!'
    elif mostreason_party == pr2:
        party_reason = 'Needed to party out the pain'
    elif mostreason_party == pr3:
        party_reason = 'You were peer-pressurered to going out'
    elif mostreason_party == pr4:
        party_reason = 'Drink to forget about school'
    elif mostreason_party == pr5:
        party_reason = 'You partied for absolutely no reason'

    gaming_hours = []
    for time in user_gaming1:
        gaming_hours.append(int(time))
    if len(gaming_hours) == 0:
        length_gh = 1
    else: length_gh = len(gaming_hours)

    total_league = []
    for game in user_gaming2:
        total_league.append(int(game))

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
        'party_hour_total': sum(time_party),
        'party_hour_ave': sum(time_party)/length_tp,
        'drink_num_total': sum(drink_num),
        'drink_num_ave': sum(drink_num)/length_dn,
        'party_location': party_loc,
        'party_reason': party_reason,
        'gaming_hours_total': sum(gaming_hours),
        'gaming_hours_ave': sum(gaming_hours)/length_gh,
        'total_league': sum(total_league)
    })
