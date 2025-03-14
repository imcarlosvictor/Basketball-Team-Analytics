import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import court_coordinates as cc
from matplotlib.patches import Circle, Rectangle, Arc


def fiba_court_coordinate(cc):
    cc.court_length = 91.86            # FIBA court length is 28 meters (91.86 feet)
    cc.court_width = 49.21             # FIBA court width is 15 meters (49.21 feet)
    cc.hoop_loc_x = 24.605             # Adjusted for FIBA court width
    cc.hoop_loc_y = 4.92               # Hoop is 1.5 meters (4.92 feet) from the baseline
    cc.hoop_loc_z = 10                 # Hoop height remains 10 feet (same as NCAA)
    cc.hoop_radius = 0.75              # Hoop radius remains unchanged
    cc.three_arc_distance = 22.15       # FIBA 3-point arc is 6.75 meters (22.15 feet)
    cc.three_straight_distance = 21.65  # FIBA three-point straight distance is 6.6 meters (21.65 feet)
    cc.three_straight_length = 10.33    # FIBA three-point straight section length is 3.15 meters (10.33 feet)
    cc.backboard_width = 5.91           # FIBA backboard width is 1.8 meters (5.91 feet)
    cc.backboard_height = 3.94          # FIBA backboard height is 1.2 meters (3.94 feet)
    cc.backboard_baseline_offset = 4.92 # FIBA backboard is 1.5 meters (4.92 feet) from the baseline
    cc.backboard_floor_offset = 9       # Same 9-foot height from the floor

def draw_court(ax=None, color='black', lw=1.2, outer_lines=False):
    # If an axes object isn't provided to plot onto, just get current one
    plt.figure(facecolor='#efefef')
    if ax is None:
        ax = plt.gca()

        # Create the various parts of an NBA basketball court

        # Create the basketball hoop
        # Diameter of a hoop is 18" so it has a radius of 9", which is a value
        # 7.5 in our coordinate system
        hoop = Circle((0, 0), radius=7.5, linewidth=lw, color=color, fill=False)

        # Create backboard
        backboard = Rectangle((-30, -7.5), 60, -1, linewidth=lw, color=color)

        # The paint
        # Create the outer box 0f the paint, width=16ft, height=19ft
        outer_box = Rectangle((-80, -47.5), 160, 190, linewidth=lw, color=color,
                              fill=False)
        # Create the inner box of the paint, widt=12ft, height=19ft
        inner_box = Rectangle((-60, -47.5), 120, 190, linewidth=lw, color=color,
                              fill=False)

        # Create free throw top arc
        top_free_throw = Arc((0, 142.5), 120, 120, theta1=0, theta2=180,
                             linewidth=lw, color=color, fill=False)
        # Create free throw bottom arc
        bottom_free_throw = Arc((0, 142.5), 120, 120, theta1=180, theta2=0,
                                linewidth=lw, color=color, linestyle='dashed')
        # Restricted Zone, it is an arc with 4ft radius from center of the hoop
        restricted = Arc((0, 0), 80, 80, theta1=0, theta2=180, linewidth=lw,
                         color=color)

        # Three point line
        # Create the side 3pt lines, they are 14ft long before they begin to arc
        corner_three_a = Rectangle((-220, -47.5), 0, 140, linewidth=lw,
                                   color=color)
        corner_three_b = Rectangle((220, -47.5), 0, 140, linewidth=lw, color=color)
        # 3pt arc - center of arc will be the hoop, arc is 23'9" away from hoop
        # I just played around with the theta values until they lined up with the 
        # threes
        three_arc = Arc((0, 0), 475, 475, theta1=22, theta2=158, linewidth=lw,
                        color=color)

        # Center Court
        center_outer_arc = Arc((0, 422.5), 120, 120, theta1=180, theta2=0,
                               linewidth=lw, color=color)
        center_inner_arc = Arc((0, 422.5), 40, 40, theta1=180, theta2=0,
                               linewidth=lw, color=color)

        # List of the court elements to be plotted onto the axes
        court_elements = [hoop, backboard, outer_box, inner_box, top_free_throw,
                          bottom_free_throw, restricted, corner_three_a,
                          corner_three_b, three_arc, center_outer_arc,
                          center_inner_arc]

        if outer_lines:
            # Draw the half court line, baseline and side out bound lines
            outer_lines = Rectangle(
                (-250, -47.5),
                500,
                470,
                linewidth=lw,
                color=color, fill=False
            )
            court_elements.append(outer_lines)

            # Add the court elements onto the axes
            for element in court_elements:
                ax.add_patch(element)

    # Update plot
    # plt.gca().set_facecolor('#f8f8ff')
    plt.gca().set_facecolor('#efefef')
    plt.axis('off')
    plt.subplots_adjust(left=1, right=2, top=2, bottom=1)

    return ax
