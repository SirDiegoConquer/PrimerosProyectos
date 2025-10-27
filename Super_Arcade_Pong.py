###--- Reproduce el clásico juego de arcade Pong. Para ello puedes 
###--- usar el módulo "turtle" para crear los componentes del juego y 
###--- detectar las colisiones de la pelota con las paletas de los jugadores.
###--- También puedes definir una serie de asignaciones de teclas para 
###--- establecer los controles del usuario para las paletas 
###--- de los jugadores izquierda y derecha.

import turtle
import os
import time
import random
import math
import winsound
import threading
import sys
import pygame
import pygame.mixer
from pygame.locals import *
import tkinter as tk
from tkinter import messagebox
import ctypes
import platform
import webbrowser
import json
import requests
import sqlite3
import hashlib
import base64
import zlib
import difflib

# Configuración de la ventana del juego

wn = turtle.Screen()
wn.title("Super Arcade Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
wn.listen()
# Marcadores
score_a = 0
score_b = 0
# Paleta A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
# Paleta B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
# Pelota
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2
# Marcador
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Jugador A: 0  Jugador B: 0", align="center", font=("Courier", 24, "normal"))
# Funciones
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += 20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    if y > -250:
        y -= 20
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    if y > -250:
        y -= 20
    paddle_b.sety(y)
# Asignación de teclas
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
# Bucle principal del juego
while True:
    wn.update()
    # Movimiento de la pelota
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # Colisiones con los bordes
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Jugador A: {}  Jugador B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Jugador A: {}  Jugador B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    # Colisiones con las paletas
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    time.sleep(0.01)
wn.mainloop()   
# Fin del código