import sys

INVALID_PARAMETER = -1
INVALID_NUMBER = -2
INVALID_PARAMS_AMOUNT = -3

def calculate_panels(arguments):
    if len(arguments) == 4:
        try:
            x_panel = float(arguments[0])
            y_panel = float(arguments[1])
            x_ruuf = float(arguments[2])
            y_ruuf = float(arguments[3])
        except:
            print('Invalid Dimensions: Enter Numerical Arguments')
            return INVALID_PARAMETER

        if x_panel > 0 and  y_panel > 0 and  x_ruuf > 0 and y_ruuf > 0:
            ## arguments are correct
            ## Considering that the orientation does not impact the outcome, the convention will be height >= width
            panel_height = max(x_panel, y_panel)
            panel_width = min(x_panel, y_panel)
            ruuf_height = max(x_ruuf, y_ruuf)
            ruuf_width = min(x_ruuf, y_ruuf)

            '''From now on, panels that are oriented in the same way as the ruuf (short sides on the same axis) 
            will be considererd 'straight' and when rotated in 180 degrees will be referred as 'rotated'  '''

            ## case 1: the ruuf is filled with straight panels, then the remaining area is filled (if possible) with rotated panels
            straight_panels_height = ruuf_height // panel_height
            straight_panels_width = ruuf_width // panel_width

            remaining_height = ruuf_height % panel_height

            rotated_panels_height = remaining_height // panel_width
            rotated_panels_width = ruuf_width // panel_height

            panels_number_case_1 = int(straight_panels_height * straight_panels_width + rotated_panels_height * rotated_panels_width)

            ## case 2: the ruuf is filled with rotated panels, then the remaining area is filled (if possible) with straight panels
            rotated_panels_height = ruuf_height // panel_width
            rotated_panels_width = ruuf_width // panel_height

            remaining_width = ruuf_width % panel_height

            straight_panels_height = ruuf_height // panel_height
            straight_panels_width = remaining_width // panel_width

            panels_number_case_2 = int(straight_panels_height * straight_panels_width + rotated_panels_height * rotated_panels_width)
            
            return max(panels_number_case_1, panels_number_case_2)

                
        else: 
            print('Invalid Dimensions: Dimensions must be > 0')
            return INVALID_NUMBER 
    else:
        print('Invalid Arguments: Enter Four Dimensions')
        return INVALID_PARAMS_AMOUNT

if __name__ == "__main__":

    print(calculate_panels(sys.argv[1:])) 
    
