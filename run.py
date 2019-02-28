from hc import Photo, Slide, opt_step, total_score

def run(filename):
    f = open(filename+'.txt')
    o = open(filename+'.o', 'w')

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

    slides.sort(key=lambda x: len(x.tags), reverse=True)

    print(total_score(slides))
    while opt_step(slides):
        print(total_score(slides))

    o.write(str(len(slides)) + '\n')
    for s in slides:
        if len(s.id) > 1:
            o.write('%d %d\n' % (s.id[0], s.id[1]))
        else:
            o.write(str(s.id[0]) + '\n')

if __name__ == '__main__':
    run('a_example')
    print('a')
    run('b_lovely_landscapes')
    print('b')
    run('c_memorable_moments')
    print('c')
    run('d_pet_pictures')
    print('d')
    run('e_shiny_selfies')
    print('e')
