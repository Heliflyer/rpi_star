from time import sleep
from star import Star

# importing enum for enumerations 
from enum import Enum 
  
# creating enumerations using class 
class Direction(Enum): 
    Clockwise = 1
    Anticlockwise = 2

def pulsing_line(number_of_leds_in_line, time_for_fade):
    i = 1
    fade_time = time_for_fade / 2
    sleep_time = time_for_fade / number_of_leds_in_line
    while (i<26):
        star.leds[i].pulse(fade_in_time = fade_time, fade_out_time = fade_time, n = 1)
        sleep(sleep_time)
        i+=1

step_default = 0.5
reducer = 0.95
direction = Direction.Clockwise

current_iteration = 0
number_of_iterations_to_do = 2

step = step_default
count = 0
star = Star(pwm=True)
leds = star.leds

run_up = True

pattern = 1

try:
    
#     star.inner.pulse(fade_in_time = 2, fade_out_time = 2.5)
#     sleep(5)
#     star.outer.pulse(fade_in_time = 2, fade_out_time = 2.5)
# 
#     while True:
#         print("")   

    while True:
    
        if (pattern==1):
            # WORKS
            
            while (current_iteration < number_of_iterations_to_do):
                completed = False
                while (completed==False):
            
                    if(count%26!=0):
                        leds[count%26].on()
                        #leds[count%13+13].on()
                        sleep(step)
                        leds[count%26].off()
                        #leds[count%13+13].off()
                        
                    count += 1
                    step = step*reducer
                    
                    if(step <= 0.0001):
                        star.outer.on()
                        star.inner.pulse(fade_in_time=0.5,fade_out_time=0.5,n=5)
                       
                        sleep(5)
                        count = 0
                        step = 1
                        star.outer.pulse(fade_in_time=0.5,fade_out_time=0.5,n=1)
                        sleep(2)
                        completed = True
                    
                current_iteration += 1
                
            pattern = 2
                
        if (pattern==2):
            print("Doing Pattern ",pattern)

            
            star.inner.blink(on_time=1.0,off_time=1.0,fade_in_time=1.0,fade_out_time=1.0,n = number_of_iterations_to_do)

            sleep(number_of_iterations_to_do)
            pattern = 3
            print("Pattern=",pattern)
            
        if (pattern==3):
            print("Doing Pattern ",pattern)
            pattern = 4
            
        if (pattern==4):
            print("Doing Pattern ",pattern)
            #star.inner.pulse()
            #sleep(2)
            star.off()

            star.outer.pulse()
            sleep(10)
            count = 0
            pattern = 5
            
        if (pattern==5):
            # simple Chaser
            while (current_iteration < number_of_iterations_to_do):
                completed = False
                while (completed==False):
                    step = 0.02
            
                    if(count%13!=0):
                        leds[count%13].on()
                        leds[count%13+13].on()
                        sleep(step)
                        leds[count%13].off()
                        leds[count%13+13].off()
            
                    count += 1
                    
                    if(count>25):
                        count = 0
                        completed = True
                        
                current_iteration += 1
            
            current_iteration = 0
            count = 0
            step = step_default
            star.off()
            pattern = 6           
 
        if (pattern==6):
            # WORKS
            # simple Chaser - starts slow, speeds up, then reverses direction

            while (current_iteration < number_of_iterations_to_do):
                completed = False
                while (completed==False):
    
                    if (direction == Direction.Clockwise):            
                        if(count%26!=0):
                            leds[count%26].on()
                            #leds[count%26-1].on()
                            sleep(step)
                            leds[count%26].off()
                            #leds[count%26-1].off()
                        
                        count += 1
                        if(run_up==True):
                            step = step*reducer
                        if(run_up==False):
                            step = step/reducer
                        
                        if(step <= 0.0001):
                            run_up=False
                            
                        if (step >=step_default):
                            run_up=True
                            direction = Direction.Anticlockwise
                            leds[count%26].on()
                        
                    if (direction == Direction.Anticlockwise):            
                        if(count%26!=0):
                            leds[count%26].on()
                            #leds[count%26-1].on()
                            sleep(step)
                            leds[count%26].off()
                            #leds[count%26-1].off()
                        
                        count -= 1
                        if (count<0):
                            count = 25
                            
                        if(run_up==True):
                            step = step*reducer
                        if(run_up==False):
                            step = step/reducer
                        
                        if(step <= 0.0001):
                            run_up=False
                            
                        if (step >=step_default):
                            run_up=True
                            direction = Direction.Clockwise
                            leds[count%26].on()
                            completed = True
                    
                current_iteration += 1
            
            print ("FINISHED 6")
            # Set up for next pattern
            pattern = 7
            run_up=True
            count = 1
            current_iteration = 0
            
        if (pattern==7):
            # Build up, build down
           
            
            step = step_default / 3
            leds[0].off()
            while (current_iteration < number_of_iterations_to_do):
                completed = False
                while (completed==False):
                    
                    if (run_up==True):
                        leds[count].on()
                        sleep(step)
                        count += 1
                    
                        if (count == 25):
                            run_up = False
                            
                    if (run_up==False):
                        leds[count].off()
                        sleep(step)
                        count -= 1
                    
                        if (count < 1):
                            count = 1
                            run_up = True
                            completed = True
                            
                current_iteration += 1
            
            print ("Finished 7")
            pattern = 8
        
        if (pattern==8):
            i=1
            number_of_seconds_for_one_led = 1
            star.inner.pulse(fade_in_time = number_of_seconds_for_one_led / 2, fade_out_time = number_of_seconds_for_one_led / 2)
            while(i<5):
                pulsing_line(4,number_of_seconds_for_one_led)
                number_of_seconds_for_one_led = number_of_seconds_for_one_led * .75
                i+=1
                
            count = 0
            step = step_default
            star.off()
            pattern=1
            
except KeyboardInterrupt:
    star.close()
