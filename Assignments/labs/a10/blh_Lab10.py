class Pattern:
    def __init__(self, data):
        self.data = data

    def make_image(self, filename):
        with open(filename, 'w') as file:
            #create header
            print(f"P2 {len(self.data[0])} {len(self.data)} 255", file=file)

            #create grid
            for row in self.data:
                for col in row:
                    print(col, end=' ', file=file)
                print(file=file)


class Light_to_Dark(Pattern):
    def __init__(self):
        data = [[i for i in range(255, -1, -1)] for j in range(255)]
        super().__init__(data)


class Triangle_Fades(Pattern):
    def __init__(self):
        data = []
        for i in range(256):
            l = []
            for j in range(256):
                if j <= i:
                    l.append(i + j)
                else:
                    l.append(256 - j + i - 1)
            data.append(l)
        super().__init__(data)


class Center_Light_Fade(Pattern):
    def __init__(self):
        data = []
        for i in range(256):
            row = []
            k = i
            while len(row) < 256:
                if k < 256:
                    row.append(k)
                    k += 1
                elif k == 256:
                    k -= 1
                    while len(row) < 256:
                        k -=1
                        row.append(k)
            data.append(row)
        super().__init__(data)


light_to_dark = Light_to_Dark()
light_to_dark.make_image('light_to_dark.pgm')
light_to_dark.make_image('light_to_dark.txt')

triangle_fades = Triangle_Fades()
triangle_fades.make_image('triangle_fades.txt')
triangle_fades.make_image('triangle_fades.pgm')

center_light_fade = Center_Light_Fade()
center_light_fade.make_image('center_light_fade.txt')
center_light_fade.make_image('center_light_fade.pgm')
