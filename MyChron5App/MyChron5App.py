import ac
import acsys
from third_party.sim_info import *
import math

appName = "MyChron5App"
width, height = 1500, 1500
timerFlag = 0
timer60perSecond = 0
timer10perSecond = 0
timer1perSecond = 0
simInfo = SimInfo()

# RPM Gauge Settings
MAX_RPM = simInfo.static.maxRpm  # Maximum RPM, adjust according to your car's max RPM
BAR_COUNT = 50  # Number of bars in the RPM gauge
BAR_WIDTH = 4  # Width of each bar
BAR_SPACING = 1.8  # Space between bars
BAR_HEIGHT = 50  # Height of the bar (when filled)


def acMain(ac_version):
    global appWindow, gear_label, lap_label, speed_label, best_label, laptime_label, pedal_label

    appWindow = ac.newApp(appName)
    ac.setTitle(appWindow, appName)
    ac.setSize(appWindow, 402, 192)
    ac.setBackgroundOpacity(appWindow, 0.5)
    ac.setBackgroundTexture(appWindow, "apps/python/MyChron5App/img.png")

    # Gear Label
    gear_label = ac.addLabel(appWindow, 'N')
    ac.setCustomFont(gear_label, 'EuroStyle', 0, 1)
    ac.setFontSize(gear_label, 90)
    ac.setFontColor(gear_label, 0, 0, 0, 1)
    ac.setFontAlignment(gear_label, 'center')
    ac.setPosition(gear_label, 63, 12.5)

    # Lap Text
    lap_text = ac.addLabel(appWindow, 'LAP')
    ac.setCustomFont(lap_text, 'EuroStyle', 0, 1)
    ac.setFontSize(lap_text, 15)
    ac.setFontColor(lap_text, 0, 0, 0, 1)
    ac.setPosition(lap_text, 47, 85)

    # Lap Label
    lap_label = ac.addLabel(appWindow, '1')
    ac.setCustomFont(lap_label, 'EuroStyle', 0, 1)
    ac.setFontSize(lap_label, 45)
    ac.setFontColor(lap_label, 0, 0, 0, 1)
    ac.setFontAlignment(lap_label, 'center')
    ac.setPosition(lap_label, 55, 97)

    # Speed Text
    speed_text = ac.addLabel(appWindow, 'km/h')
    ac.setCustomFont(speed_text, 'EuroStyle', 0, 1)
    ac.setFontSize(speed_text, 13.5)
    ac.setFontColor(speed_text, 0, 0, 0, 1)
    ac.setFontAlignment(speed_text, 'center')
    ac.setPosition(speed_text, 256, 88)

    # Speed Label
    speed_label = ac.addLabel(appWindow, '0')
    ac.setCustomFont(speed_label, 'EuroStyle', 0, 1)
    ac.setFontSize(speed_label, 45)
    ac.setFontColor(speed_label, 0, 0, 0, 1)
    ac.setFontAlignment(speed_label, 'center')
    ac.setPosition(speed_label, 200, 67)

    # Best Lap Text
    best_text = ac.addLabel(appWindow, 'BEST')
    ac.setCustomFont(best_text, 'EuroStyle', 0, 1)
    ac.setFontSize(best_text, 13.5)
    ac.setFontColor(best_text, 0, 0, 0, 1)
    ac.setFontAlignment(best_text, 'center')
    ac.setPosition(best_text, 111, 85.5)

    # Best Lap
    best_label = ac.addLabel(appWindow, '0')
    ac.setCustomFont(best_label, 'EuroStyle', 0, 1)
    ac.setFontSize(best_label, 45)
    ac.setFontColor(best_label, 0, 0, 0, 1)
    ac.setFontAlignment(best_label, 'center')
    ac.setPosition(best_label, 170, 97)

    # Laptime
    laptime_label = ac.addLabel(appWindow, '0')
    ac.setCustomFont(laptime_label, 'EuroStyle', 0, 1)
    ac.setFontSize(laptime_label, 73)
    ac.setFontColor(laptime_label, 0, 0, 0, 1)
    ac.setFontAlignment(laptime_label, 'center')
    ac.setPosition(laptime_label, 130, 127)

    # RPM
    r_label = ac.addLabel(appWindow, 'R')
    ac.setCustomFont(r_label, 'EuroStyle', 0, 1)
    ac.setFontSize(r_label, 15)
    ac.setFontColor(r_label, 0, 0, 0, 1)
    ac.setPosition(r_label, 97, 17)
    p_label = ac.addLabel(appWindow, 'P')
    ac.setCustomFont(p_label, 'EuroStyle', 0, 1)
    ac.setFontSize(p_label, 15)
    ac.setFontColor(p_label, 0, 0, 0, 1)
    ac.setPosition(p_label, 97, 29)
    m_label = ac.addLabel(appWindow, 'M')
    ac.setCustomFont(m_label, 'EuroStyle', 0, 1)
    ac.setFontSize(m_label, 15)
    ac.setFontColor(m_label, 0, 0, 0, 1)
    ac.setPosition(m_label, 96, 41)

    # Pedal Text
    pedal_text = ac.addLabel(appWindow, 'PEDAL %')
    ac.setCustomFont(pedal_text, 'EuroStyle', 0, 1)
    ac.setFontSize(pedal_text, 11)
    ac.setFontColor(pedal_text, 0, 0, 0, 1)
    ac.setPosition(pedal_text, 335, 108)

    # Pedal Label
    pedal_label = ac.addLabel(appWindow, '0')
    ac.setCustomFont(pedal_label, 'EuroStyle', 0, 1)
    ac.setFontSize(pedal_label, 23)
    ac.setFontColor(pedal_label, 0, 0, 0, 1)
    ac.setPosition(pedal_label, 354, 121)

    # WaterTemp Text
    water_text = ac.addLabel(appWindow, 'WATER °C')
    ac.setCustomFont(water_text, 'EuroStyle', 0, 1)
    ac.setFontSize(water_text, 11)
    ac.setFontColor(water_text, 0, 0, 0, 1)
    ac.setPosition(water_text, 335, 150)

    # WaterTemp Label
    water_label = ac.addLabel(appWindow, '69')
    ac.setCustomFont(water_label, 'EuroStyle', 0, 1)
    ac.setFontSize(water_label, 23)
    ac.setFontColor(water_label, 0, 0, 0, 1)
    ac.setPosition(water_label, 345, 165)

    # ExhaustTemp Text
    exhaust_text = ac.addLabel(appWindow, 'EXHAUST °C')
    ac.setCustomFont(exhaust_text, 'EuroStyle', 0, 1)
    ac.setFontSize(exhaust_text, 11)
    ac.setFontColor(exhaust_text, 0, 0, 0, 1)
    ac.setPosition(exhaust_text, 250, 150)

    # ExhaustTemp Label
    water_label = ac.addLabel(appWindow, '69.0')
    ac.setCustomFont(water_label, 'EuroStyle', 0, 1)
    ac.setFontSize(water_label, 23)
    ac.setFontColor(water_label, 0, 0, 0, 1)
    ac.setPosition(water_label, 256, 164)

    # Lambda Text
    lambda_text = ac.addLabel(appWindow, 'LAMBDA %')
    ac.setCustomFont(lambda_text, 'EuroStyle', 0, 1)
    ac.setFontSize(lambda_text, 11)
    ac.setFontColor(lambda_text, 0, 0, 0, 1)
    ac.setPosition(lambda_text, 254, 108)

    # Lambda Label
    lambda_label = ac.addLabel(appWindow, '0.93')
    ac.setCustomFont(lambda_label, 'EuroStyle', 0, 1)
    ac.setFontSize(lambda_label, 23)
    ac.setFontColor(lambda_label, 0, 0, 0, 1)
    ac.setPosition(lambda_label, 256, 121)

    ac.addRenderCallback(appWindow, appGL)  # Link to the OpenGL render function

    return appName


def appGL(deltaT):
    global simInfo

    # Get the current RPM from the telemetry
    current_rpm = ac.getCarState(0, acsys.CS.RPM)

    # Calculate the number of filled bars based on RPM
    filled_bars = math.floor((current_rpm / MAX_RPM) * BAR_COUNT)

    # Draw each bar in the RPM gauge
    for i in range(BAR_COUNT):

        # Position of the bar
        x_pos = 20 + (BAR_WIDTH + BAR_SPACING) * i

        # Set color based on whether the bar is filled or empty
        if i < filled_bars:
            ac.glColor3f(0.0, 0.0, 0.0)  # Filled bar color (green)
        elif i == 7 or i == 14 or i == 20 or i == 26 or i == 32 or i == 39 or i == 45:
            ac.glColor3f(0, 0, 0)
        else:
            ac.glColor3f(0.6980392156862747, 0.6980392156862747, 0.6980392156862747)  # Empty bar color (gray)

        if i == 7 or i == 14 or i == 21 or i == 28:
            ac.glQuad(x_pos + 90, 15, 3, 37)

        elif i == 36:
            ac.glQuad(x_pos + 90, 15, 3, 44)

        elif i == 39:
            ac.glQuad(x_pos + 90, 15, 3, 52)

        elif i == 45:
            ac.glQuad(x_pos + 90, 15, 3, 60)

        elif 1 <= i <= 29:
            ac.glQuad(x_pos + 90, 15, 3, 33.75)
        elif 30 <= i <= 36:
            ac.glQuad(x_pos + 90, 15, 3, 42)
        elif 37 <= i <= 43:
            ac.glQuad(x_pos + 90, 15, 3, 50)
        elif 44 <= i <= 50:
            ac.glQuad(x_pos + 90, 15, 3, 57)


def acUpdate(deltaT):
    global gear_label, lap_label, speed_label, best_label, laptime_label, pedal_label
    global timer1perSecond

    timer1perSecond += deltaT

    if timer1perSecond > 0.2:
        timer1perSecond = 0  # Reset timer

        lap = ac.getCarState(0, acsys.CS.LapCount)
        laptime = ac.getCarState(0, acsys.CS.LapTime)
        best_lap = ac.getCarState(0, acsys.CS.BestLap)
        gear = ac.getCarState(0, acsys.CS.Gear)
        speed = ac.getCarState(0, acsys.CS.SpeedKMH)
        pedal = ac.getCarState(0, acsys.CS.Gas)

        if speed >= 100:
            ac.setPosition(speed_label, 205, 66)

        elif 10 < speed < 100:
            ac.setPosition(speed_label, 215, 66)
        elif 0 < speed < 10:
            ac.setPosition(speed_label, 225, 66)

        if (pedal * 100) < 10:
            ac.setPosition(pedal_label, 354, 121)
        elif (pedal * 100) >= 10:
            ac.setPosition(pedal_label, 345, 121)
        elif (pedal * 100) >= 100:
            ac.setPosition(pedal_label, 330, 121)

        ac.setText(pedal_label, format_pedal(pedal))
        ac.setText(laptime_label, str(round(laptime / 1000, 2)))
        ac.setText(speed_label, str(round(speed)))
        ac.setText(gear_label, str(form_gear(gear - 1)))
        ac.setText(lap_label, str(lap + 1))
        ac.setText(best_label, str(round(best_lap / 1000, 2)))


def form_gear(gear):
    if gear == 0:
        return 'N'
    if gear == -1:
        return 'R'
    return str(gear)


def format_pedal(pedal):
    pedal = round(pedal * 100)
    return str(pedal)
