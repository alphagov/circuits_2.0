# from app.main.exercises import exercises
from app.main.get_data import get_workout_type, get_exercises
import random


def get(type, effort):
    print(effort)
    workouts = get_workout_type()
    workout_type = workouts[type]['New name']
    exercises = get_exercises()
    type_dict = [x for x in exercises if x[workout_type] == 'Y']

    for exercise in type_dict:
        if exercise['Difficulty'].lower() == effort:
            exercise['Weight'] = 10
        else:
            exercise['Weight'] = 2

    weights = [ex['Weight'] for ex in type_dict]

    workout_exercises_objects = random.choices(type_dict, weights=weights, k=workouts[type]['Number'])
    for x in workout_exercises_objects:
        i = workout_exercises_objects.index(x)
        workout_exercises_objects[i]['work'] = workouts[type]['Work']
        workout_exercises_objects[i]['rest'] = workouts[type]['Rest']

    return workout_exercises_objects
