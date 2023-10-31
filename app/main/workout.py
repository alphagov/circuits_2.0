# from app.main.exercises import exercises
from app.main.get_data import get_workout_type, get_exercises
import random


def get(type):
    workouts = get_workout_type()
    workout_type = workouts[type]['New name']
    exercises = get_exercises()
    type_dict = [x for x in exercises if x[workout_type] == 'Y']

    workout_exercises_objects = random.sample(type_dict, workouts[type]['Number'])
    for x in workout_exercises_objects:
        i = workout_exercises_objects.index(x)
        workout_exercises_objects[i]['work'] = workouts[type]['Work']
        workout_exercises_objects[i]['rest'] = workouts[type]['Rest']

    # workout_exercises = [d['exercise'] for d in workout_exercises_objects]

    return workout_exercises_objects
