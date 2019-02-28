
class Photo:
    def __init__(self, id, tags):
        self.id = id
        self.tags = tags

class Slide:
    def __init__(self, *photos):
        if len(photos) == 1:
            self.id = [photos[0].id]
            self.tags = photos[0].tags
        else:
            self.id = [photos[0].id, photos[1].id]
            self.tags = list(set(photos[0].tags) | set(photos[1].tags))
    
def tr_score(s_prev, s_next):
    common = set(s_prev.tags)&set(s_next.tags)
    l_prev = set(s_prev.tags) - common
    l_next = set(s_next.tags) - common
    return min(len(common), len(l_prev), len(l_next))

def total_score(slides):
    score = 0
    for i in range(len(slides)):
        #print(slides[i].tags)
        if i > 0:
            score += tr_score(slides[i-1], slides[i])
    return score
    
def opt_step(slides):
    #slides_bak = slides.copy()
    is_opt = False
    for i in range(len(slides)-1):
        #print(slides[i].tags, slides[i+1].tags)
        orig_score, swap_score = 0,0
        if(i>0):
            orig_score += tr_score(slides[i-1],slides[i]) 
            swap_score += tr_score(slides[i-1],slides[i+1]) 
        if(i+2<len(slides)):
            orig_score += tr_score(slides[i+1],slides[i+2]) 
            swap_score += tr_score(slides[i],slides[i+2]) 
        #print(orig_score, swap_score)
        if swap_score > orig_score:
            slides[i], slides[i+1] = slides[i+1], slides[i]
            is_opt = True
    # cannot optimize anymore
    return is_opt

if __name__ == '__main__':
    f = open('a_example.txt')
    o = open('o', 'w')

    h_photos = []
    v_photos = []
    slides = []

    content = f.readlines()
    num_photos = content[0]

    content.pop(0)

    id = 0
    for photo in content:
        attrs = photo.split()

        if attrs[0] == 'H':
            h_photos.append(Photo(id, attrs[2:2 + int(attrs[1])]))
        else:
            v_photos.append(Photo(id, attrs[2:2 + int(attrs[1])]))

        id += 1

    for p in h_photos:
        slides.append(Slide(p))

    v_photos.sort(key=lambda x: len(x.tags), reverse=True)

    if len(v_photos) % 2 != 0:
        v_photos.pop()

    while len(v_photos) != 0:
        p1 = v_photos.pop(0)
        p2 = v_photos.pop()

        slides.append(Slide(p1, p2))

    #slides.sort(key=lambda x: len(x.tags), reverse=False)
    print(total_score(slides))
    opt_step(slides)
    print(total_score(slides))


