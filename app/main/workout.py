from app.main.exercises import exercises
import random

def get(type):
    type_map = {'hiit': {'name':'40X20', 'number':24, 'work':'40 seconds', 'rest':'20 seconds'},
            'twelve':{'name':'reps_12', 'number':12, 'work':'12 reps', 'rest':'2 minutes'},
            'oneby6':{'name':'1minX6', 'number':18, 'work':'1 minute', 'rest':'2 minutes'}}
    
    workout_type = type_map[type]['name']
    type_dict = [x for x in exercises if x[workout_type] == 'Y']
    workout_exercises_objects = random.sample(type_dict, type_map[type]['number'])
    for x in workout_exercises_objects:
        i = workout_exercises_objects.index(x)
        workout_exercises_objects[i]['work'] = type_map[type]['work']
        workout_exercises_objects[i]['rest'] = type_map[type]['rest']

    workout_exercises = [d['exercise'] for d in workout_exercises_objects]

    return workout_exercises_objects


