import cairo
import re
import argh

import cons
import vow
import sec

unitsize = 100

char_re_str = "(?P<char>\
(?P<cons>[pbtdkgmnNBrRvwszjHyYlL]*)?\
(?P<vow>[iïüuöeëoäéaá]+)\
(\\[(?P<sec>([1234567]([\\-iüu]('+(\\([0-9]+\\))?)?)+)+)\\])?)"
char_re = re.compile(char_re_str)


def get_char_size(str):
    match = char_re.match(str)
    cons_match = match.group("cons")
    num_cons = len(cons_match) if cons_match is not None else 0
    num_vow = len(match.group("vow"))
    num_sec = 0
    if match.group("sec") is not None:
        sec_match = sec.sec_re.findall(match.group("sec"))
        if sec_match is not None:
            num_sec = sum(map(sec.get_height, map(lambda x: x[0], sec_match)))

    height = max(num_cons, num_vow + (0.5 * num_sec))
    width = 3 if num_cons > 0 else 2

    return (width, height)


def draw_comp(ctx, char):
    if char in cons.draw_funcs:
        cons.draw_funcs[char](ctx)
    elif char in vow.draw_funcs:
        vow.draw_funcs[char](ctx)


def draw_char(ctx, str):
    print("constructing character " + str)
    match = char_re.match(str)
    height = 0
    if match.group("cons") is not None:
        for con in match.group("cons"):
            draw_comp(ctx, con)
            ctx.translate(0, 1)
            height += 1
        ctx.translate(1 if len(match.group("cons")) > 0 else 0, -height)
    height = 0
    for vo in match.group("vow"):
        draw_comp(ctx, vo)
        ctx.translate(0, 1)
        height += 1
    if match.group("sec") is not None:
        for sv in map(lambda x: x[0], sec.sec_re.findall(match.group("sec"))):
            sec.draw(ctx, sv)
            svh = 0.5 * sec.get_height(sv)
            ctx.translate(0, svh)
            height += svh
    ctx.translate(2, -height)


def draw_string(str, filename="test.png", mode="png"):
    chars = list(map(lambda x: x[0], char_re.findall(str)))
    # print(chars)
    sizes = list(map(get_char_size, chars))
    size_x = sum(map(lambda x: x[0], sizes))
    size_y = max(map(lambda x: x[1], sizes))

    print(f"computed size: {size_x}, {size_y}")

    surface = cairo.ImageSurface(
        cairo.FORMAT_ARGB32,
        int(size_x * unitsize),
        int(size_y * unitsize)
    )

    ctx = cairo.Context(surface)
    ctx.scale(unitsize, -unitsize)  # flip y-axis to make it easier to stack
    ctx.translate(0, -size_y)

    ctx.set_line_width(0.1)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.set_line_join(cairo.LINE_JOIN_ROUND)
    ctx.set_source_rgb(1.0, 1.0, 1.0)

    for char in chars:
        draw_char(ctx, char)

    surface.write_to_png(filename)


if __name__ == '__main__':
    argh.dispatch_command(draw_string)
    # char_str = "vjé[1u'(8)3i''] miö[3i'ü'(9)]"
    # char_str = "tdu"

    # draw_string(char_str, "test.png", "png")
