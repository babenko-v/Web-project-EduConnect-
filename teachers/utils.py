from django.db.models import Q

from users.models import Teacher_profile

def search_query(query):
    query_split = query.split()

    keyword = [word for word in query_split if len(word)>2]
    q_object = Q()

    for token in keyword:
        q_object |= Q(first_name=token)
        q_object |= Q(last_name=token)
        q_object |= Q(info_about_teacher__contains=token)
    return Teacher_profile.objects.filter(q_object)