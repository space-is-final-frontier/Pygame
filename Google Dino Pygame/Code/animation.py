from variables import WALK_LIST

def move(xpos, ypos, dx, dy, frames, img, img_ind):
    
    frames += 1

    if frames == 9:
        img = WALK_LIST[img_ind]

        if img_ind == 5:
            img_ind = 0
            
        else:
            img_ind += 1
        
        frames = 0


    xpos = xpos + dx
    ypos = ypos + dy
    
    return xpos, ypos, frames, img, img_ind