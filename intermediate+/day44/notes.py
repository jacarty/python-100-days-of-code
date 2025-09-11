"""
CSS Properties

colorhunt.co
fonts.google.com
"""

############################
# Colour
############################

# html {
# background-color: blue
# }
#
# h1 {
# color: blue
# }
#
# h2 {
# color: 0D1164
# }

############################
# Font Property Examples
############################

# 1 px = 1/96th Inch
# 1 px = 0.26 mm

# 1 pt = 1/72nd Inch
# 1 pt = 0.35 mm

# 1 em = 100% of parent
# 1 rem = 100% of root

# #color {
#     color: coral;
#     font-size: 2rem; # 2x parent size
#     font-weight: 900;
#     font-family: 'Caveat', cursive;
#     text-align: right;
# }

############################
# Margin, Padding & Border
############################

# borders expand out; they dont reduce the box
# border: thickness style colour
# border-top: value
# border-width: top right bottom left
# border-width: top-bottom right-left
#
# padding pushes out border by value; box stays same size
# padding: value
#
# margin is the bit outside the border
# margin: value

# ┌─────────────────────────────────────────────────────────────────┐
# │                           MARGIN                                │
# │  ┌───────────────────────────────────────────────────────────┐  │
# │  │                        BORDER                             │  │
# │  │  ┌─────────────────────────────────────────────────────┐  │  │
# │  │  │                    PADDING                          │  │  │
# │  │  │  ┌───────────────────────────────────────────────┐  │  │  │
# │  │  │  │                                               │  │  │  │
# │  │  │  │                                               │  │  │  │
# │  │  │  │                 CONTENT                       │  │  │  │
# │  │  │  │                                               │  │  │  │
# │  │  │  │            (Your actual element               │  │  │  │
# │  │  │  │             text, images, etc.)               │  │  │  │
# │  │  │  │                                               │  │  │  │
# │  │  │  └───────────────────────────────────────────────┘  │  │  │
# │  │  │                                                     │  │  │
# │  │  └─────────────────────────────────────────────────────┘  │  │
# │  │                                                           │  │
# │  └───────────────────────────────────────────────────────────┘  │
# │                                                                 │
# └─────────────────────────────────────────────────────────────────┘

#                         Box Model Layers:
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# 1. CONTENT   - The actual content (text, images, etc.)
# 2. PADDING   - Space between content and border (inside border)
# 3. BORDER    - The border surrounding padding and content
# 4. MARGIN    - Space outside the border (between elements)

# Example CSS:
# ───────────
# .box {
#     margin: 20px;      /* Outermost spacing */
#     border: 5px solid; /* Border thickness & style */
#     padding: 15px;     /* Inner spacing */
#     width: 200px;      /* Content width */
#     height: 100px;     /* Content height */
# }

# Total Width  = margin + border + padding + content + padding + border + margin
# Total Height = margin + border + padding + content + padding + border + margin

############################
# HTML Div
############################

# A <div> (division) is a generic HTML container element that groups content together. 
# By itself, it's invisible and has no visual styling—it's like an empty box waiting to be decorated.

# Class Selector example

# <div class="my-box">Content here</div>

# .my-box {
#     background-color: lightgray;
#     padding: 20px;
#     border: 2px solid black;
# }