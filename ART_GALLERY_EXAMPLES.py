### EXAMPLES FOR ART GALLERY ###
### BY: OWEN FOSTER ###

### simply run this code to start the program, there will be a menu to choose examples
### IMPORTANT: make sure that the ART_GALLERY.py file is in the same folder/directory as this file when you run 

import ART_GALLERY as ag

def bookex1_bipartite():
    art_gallery1 = ag.gallery(6)
    art_gallery1.add_edge(0,3)
    art_gallery1.add_edge(0,4)
    art_gallery1.add_edge(0,5)
    art_gallery1.add_edge(1,3)
    art_gallery1.add_edge(1,4)
    art_gallery1.add_edge(1,5)
    art_gallery1.add_edge(2,3)
    art_gallery1.add_edge(2,4)
    art_gallery1.add_edge(2,5)
    art_gallery1.color()
    return

def slides_wout_tri():
    art_g = ag.gallery(14)
    art_g.add_edge(0,1)
    art_g.add_edge(0,13)
    art_g.add_edge(1,2)
    art_g.add_edge(2,3)
    art_g.add_edge(3,4)
    art_g.add_edge(4,5)
    art_g.add_edge(5,6)
    art_g.add_edge(6,7)
    art_g.add_edge(7,8)
    art_g.add_edge(8,9)
    art_g.add_edge(9,10)
    art_g.add_edge(10,11)
    art_g.add_edge(11,12)
    art_g.add_edge(12,13)
    art_g.color()
    return

def slides_w_tri():
    art_g = ag.gallery(14)
    art_g.add_edge(0,1)
    art_g.add_edge(0,11)
    art_g.add_edge(0,13)
    art_g.add_edge(1,2)
    art_g.add_edge(1,10)
    art_g.add_edge(1,11)
    art_g.add_edge(1,7)
    art_g.add_edge(2,3)
    art_g.add_edge(2,6)
    art_g.add_edge(2,7)
    art_g.add_edge(3,4)
    art_g.add_edge(3,6)
    art_g.add_edge(4,5)
    art_g.add_edge(4,6)
    art_g.add_edge(5,6)
    art_g.add_edge(6,7)
    art_g.add_edge(7,8)
    art_g.add_edge(7,9)
    art_g.add_edge(7,10)
    art_g.add_edge(8,9)
    art_g.add_edge(9,10)
    art_g.add_edge(10,11)
    art_g.add_edge(11,12)
    art_g.add_edge(12,13)
    art_g.add_edge(13,11)
    art_g.color()
    return

def wolf_ex():
    art_g = ag.gallery(11)
    art_g.add_edge(0,1)
    art_g.add_edge(0,10)
    art_g.add_edge(1,2)
    art_g.add_edge(1,10)
    art_g.add_edge(2,3)
    art_g.add_edge(2,10)
    art_g.add_edge(3,10)
    art_g.add_edge(3,9)
    art_g.add_edge(3,4)
    art_g.add_edge(3,8)
    art_g.add_edge(4,5)
    art_g.add_edge(4,8)
    art_g.add_edge(5,6)
    art_g.add_edge(5,8)
    art_g.add_edge(5,7)
    art_g.add_edge(6,7)
    art_g.add_edge(7,8)
    art_g.add_edge(8,9)
    art_g.add_edge(9,10)
    art_g.color()
    return

def k5complete():
    art_gallery1 = ag.gallery(5)
    art_gallery1.add_edge(0,1)
    art_gallery1.add_edge(0,2)
    art_gallery1.add_edge(0,3)
    art_gallery1.add_edge(0,4)
    art_gallery1.add_edge(1,2)
    art_gallery1.add_edge(1,3)
    art_gallery1.add_edge(1,4)
    art_gallery1.add_edge(2,3)
    art_gallery1.add_edge(2,4)
    art_gallery1.add_edge(3,4)
    art_gallery1.color()
    return
    
    
### RUN EXAMPLES
finput = -1
while finput != 0:
    print("Which example to run?")
    print("---------")
    print("0 - Quit :(")
    print("1 - Bipartite graph")
    print("2 - K5 Complete Graph")
    print("3 - Slides example without trianglulation")
    print("4 - Slides example with triangulation")
    print("5 - Wolfram example")
    finput = int(input())
    print("---------")
    if finput == 1:
        bookex1_bipartite()
        print("---------")
    elif finput == 2:
        k5complete()
        print("---------")
    elif finput == 3:
        slides_wout_tri()
        print("---------")
    elif finput == 4:
        slides_w_tri()
        print("---------")
    elif finput == 5:
        wolf_ex()
        print("---------")

