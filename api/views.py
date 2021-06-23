from django.http import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import pickle
import numpy as np
# Create your views here.

MODEL = pickle.load(open("Model\model.pkl", 'rb'))

@api_view(['GET'])
def apiBase(request):
    routes = {
        'Questions':'/questions',
        'Predict':'/predict',
        'All Questions':'/all_questions',
        'Question To Predict':'/question_to_predict'
    }
    return Response(routes)

@api_view(['GET'])
def questions(request):
    qs = {
    'GN':'Gender',
    'AG':'Age (in years)',
    'MS': 'Marital status',
    'RS':'Area of residence',
    'ES':'Employment status',
    'FI':'Monthly Family Income',
    'ED':'Level of Education',
    'CI':'Do you know any of your friend or family member who is infected with COVID-19?',
    'F1':'I am most afraid of Corona (COVID-19)',
    'F2':'It makes me uncomfortable to think about Corona',
    'F3':'My hands become clammy when I think about Corona',
    'F4':'I am afraid of losing my life because of Corona',
    'F5':'When I watch news and stories about Corona on social media, I become nervous or anxious',
    'F6':'I cannot sleep because Im worrying about getting Corona',
    'F7':'My heart races or palpitates when I think about getting Corona',
    'P1':'I regularly wash my hands for 20 seconds',
    'P2':'I wear mask when go outside',
    'P3':'I avoid handshake and physical gestures of greetings',
    'P4':'I maintain social/physical distance while meeting others',
    'P5':'I do not meet (or avoid) people who have cough or flue',
    'P6':'I do not touch my face (mouth, nose, eyes) without washing my hands',
    'P7':'When water is not available, I use sanitizer to clean my hands',
    'A1':'I am often a carefree and good spirit',
    'A2':'I enjoy my life',
    'A3':'All in all, I am satisfied with my life',
    'A4':'In general, I am confident',
    'A5':'I manage well to fulfil my needs',
    'A6':'I am in good physical and emotional condition',
    'A7':'I feel that I am actually well equipped to deal with life and its activities',
    'A8':'Much of what I do brings me joy',
    'A9':'I am a calm, balanced human being',
    'M1':'Are you satisfied with the steps taken by the government authorities to control the spread of Coronavirus?',
    'M2':'Are you satisfied with your familys safety from COVID-19?',
    'M3':'Are you satisfied with your studies during the prevailing situation of COVID-19?',
    'D2':'Over the last two weeks, not being able to stop or control worrying',
    'D3':'Over the last two weeks, worrying too much about different things',
    'D4':'Over the last two weeks, trouble relaxing',
    'D5':'Over the last two weeks, being so restless that it is hard to sit still',
    'D6':'Over the last two weeks, becoming easily annoyed or irritable',
    'D7':'Over the last two weeks, feeling afraid, as if something awful might happen'
}
    
    return Response(qs)


    # 'D1':'Over the last two weeks, feeling nervous, anxious, or on edge',

@api_view(['GET'])
def allquestions(request):
    all = questions = {
    'GN':'Gender',
    'AG':'Age (in years)',
    'MS': 'Marital status',
    'RS':'Area of residence',
    'ES':'Employment status',
    'FI':'Monthly Family Income',
    'ED':'Level of Education',
    'CI':'Do you know any of your friend or family member who is infected with COVID-19?',
    'F1':'I am most afraid of Corona (COVID-19)',
    'F2':'It makes me uncomfortable to think about Corona',
    'F3':'My hands become clammy when I think about Corona',
    'F4':'I am afraid of losing my life because of Corona',
    'F5':'When I watch news and stories about Corona on social media, I become nervous or anxious',
    'F6':'I cannot sleep because Im worrying about getting Corona',
    'F7':'My heart races or palpitates when I think about getting Corona',
    'P1':'I regularly wash my hands for 20 seconds',
    'P2':'I wear mask when go outside',
    'P3':'I avoid handshake and physical gestures of greetings',
    'P4':'I maintain social/physical distance while meeting others',
    'P5':'I do not meet (or avoid) people who have cough or flue',
    'P6':'I do not touch my face (mouth, nose, eyes) without washing my hands',
    'P7':'When water is not available, I use sanitizer to clean my hands',
    'A1':'I am often a carefree and good spirit',
    'A2':'I enjoy my life',
    'A3':'All in all, I am satisfied with my life',
    'A4':'In general, I am confident',
    'A5':'I manage well to fulfil my needs',
    'A6':'I am in good physical and emotional condition',
    'A7':'I feel that I am actually well equipped to deal with life and its activities',
    'A8':'Much of what I do brings me joy',
    'A9':'I am a calm, balanced human being',
    'M1':'Are you satisfied with the steps taken by the government authorities to control the spread of Coronavirus?',
    'M2':'Are you satisfied with your familys safety from COVID-19?',
    'M3':'Are you satisfied with your studies during the prevailing situation of COVID-19?',
    'D1':'Over the last two weeks, feeling nervous, anxious, or on edge',
    'D2':'Over the last two weeks, not being able to stop or control worrying',
    'D3':'Over the last two weeks, worrying too much about different things',
    'D4':'Over the last two weeks, trouble relaxing',
    'D5':'Over the last two weeks, being so restless that it is hard to sit still',
    'D6':'Over the last two weeks, becoming easily annoyed or irritable',
    'D7':'Over the last two weeks, feeling afraid, as if something awful might happen'
}
    return Response(all)

@api_view(['GET'])
def to_predict(request):
    t = {'Question to predict':'Over the last two weeks, feeling nervous, anxious, or on edge'}
    return Response(t)

@api_view(['POST'])
def predict(request):
    ans = np.array(request.data['data'])
    ans = ans.reshape(1,-1)
    result = MODEL.predict(ans)
    r = {'result':result[0]}
    return Response(r)