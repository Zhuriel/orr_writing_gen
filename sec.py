import re
import math


sec_re_str = "(\
(?P<num>[1234567])\
(?P<vow>([\\-iüu]('+(\\([0-9]+\\))?)?)+)\
)"
sec_re = re.compile(sec_re_str)

sec_vow_re_str = "((?P<vow>[\\-iüu])(?P<stp>'+(\\((?P<num>[0-9]+)\\))?)?)"
sec_vow_re = re.compile(sec_vow_re_str)


def draw_1i(ctx):
    ctx.new_path()
    ctx.move_to(0.1, 0.4)
    ctx.line_to(0.4, 0.4)
    ctx.line_to(0.2, 0.1)


def draw_1u2(ctx):
    ctx.new_path()
    ctx.arc(0.25, 0.25, 0.15, 0.5 * math.pi, 1.5 * math.pi)


def draw_1u(ctx):
    ctx.new_path()
    ctx.move_to(0.4, 0.1)
    ctx.line_to(0.4, 0.4)
    ctx.line_to(0.1, 0.4)
    ctx.line_to(0.1, 0.1)


def draw_2i(ctx):
    ctx.new_path()
    ctx.move_to(0.4, 0.4)
    ctx.line_to(0.1, 0.1)


def draw_2u2(ctx):
    ctx.new_path()
    ctx.arc_negative(0.1, 0.25, 0.15, 0.5 * math.pi, 1.5 * math.pi)


def draw_2u(ctx):
    ctx.new_path()
    ctx.move_to(0.1, 0.25)
    ctx.line_to(0.4, 0.25)
    ctx.stroke()
    ctx.new_path()
    ctx.arc_negative(0.1, 0.25, 0.15, 0.5 * math.pi, 1.5 * math.pi)


def draw_3i(ctx):
    ctx.new_path()
    ctx.move_to(0.1, 0.25)
    ctx.line_to(0.4, 0.25)
    ctx.stroke()
    ctx.new_path()
    ctx.move_to(0.1, 0.1)


def draw_3u2(ctx):
    ctx.new_path()
    ctx.move_to(0.1, 0.4)
    ctx.line_to(0.4, 0.4)
    ctx.stroke()
    draw_3i(ctx)


def draw_3u(ctx):
    ctx.new_path()
    ctx.move_to(0.3, 0.4)
    ctx.line_to(0.2, 0.1)
    ctx.stroke()
    draw_3i(ctx)


def draw_4i(ctx):
    ctx.new_path()
    ctx.move_to(0.4, 0.4)
    ctx.line_to(0.2, 0.4)
    ctx.line_to(0.3, 0.1)
    ctx.stroke()
    ctx.new_path()
    ctx.move_to(0.1, 0.1)


def draw_4u2(ctx):
    ctx.new_path()
    ctx.move_to(0.1, 0.4)
    ctx.line_to(0.1, 0.1)
    ctx.line_to(0.25, 0.25)
    ctx.line_to(0.4, 0.1)


def draw_4u(ctx):
    ctx.new_path()
    ctx.move_to(0.3, 0.4)
    ctx.line_to(0.4, 0.25)
    ctx.line_to(0.1, 0.25)
    ctx.stroke()
    ctx.new_path()
    ctx.move_to(0.1, 0.1)


def draw_5i(ctx):
    ctx.new_path()
    ctx.arc(0.2, 0.25, 0.01, 0, 2 * math.pi)
    ctx.stroke()
    ctx.new_path()
    ctx.move_to(0.1, 0.1)


def draw_5u2(ctx):
    draw_5i(ctx)
    ctx.move_to(0.3, 0.4)
    ctx.line_to(0.4, 0.1)
    ctx.stroke()
    ctx.new_path()
    ctx.move_to(0.1, 0.1)


def draw_5u(ctx):
    ctx.new_path()
    ctx.arc(0.1, 0.1, 0.3, 0, 0.5 * math.pi)
    ctx.stroke()
    ctx.new_path()
    ctx.move_to(0.1, 0.1)


def draw_6i(ctx):
    ctx.new_path()
    ctx.arc(0.25, 0.25, 0.15, 0, math.pi)
    ctx.stroke()
    ctx.new_path()
    ctx.move_to(0.1, 0.1)


def draw_6u2(ctx):
    ctx.new_path()
    ctx.arc(0.25, 0.25, 0.15, 0, math.pi)
    ctx.stroke()
    ctx.new_path()
    ctx.move_to(0.25, 0.25)
    ctx.line_to(0.25, 0.1)
    ctx.move_to(0.1, 0.1)


def draw_6u(ctx):
    ctx.new_path()
    ctx.move_to(0.4, 0.1)
    ctx.arc(0.25, 0.25, 0.15, 0, math.pi)
    ctx.line_to(0.1, 0.1)


def draw_7i(ctx):
    ctx.new_path()
    ctx.move_to(0.1, 0.4)
    ctx.line_to(0.1, 0.25)
    ctx.line_to(0.4, 0.325)
    ctx.line_to(0.4, 0.4)
    ctx.stroke()
    ctx.new_path()
    ctx.move_to(0.1, 0.1)


def draw_7u2(ctx):
    ctx.new_path()
    ctx.move_to(0.1, 0.25)
    ctx.line_to(0.4, 0.25)
    ctx.line_to(0.3, 0.4)
    ctx.line_to(0.1, 0.4)
    ctx.stroke()
    ctx.new_path()
    ctx.move_to(0.1, 0.1)


def draw_7u(ctx):
    ctx.new_path()
    ctx.move_to(0.1, 0.25)
    ctx.line_to(0.1, 0.4)
    ctx.line_to(0.4, 0.325)
    ctx.line_to(0.4, 0.25)
    ctx.stroke()
    ctx.new_path()
    ctx.move_to(0.1, 0.1)


draw_funcs = {
    "1": {
        "i": draw_1i,
        "ü": draw_1u2,
        "u": draw_1u
    },
    "2": {
        "i": draw_2i,
        "ü": draw_2u2,
        "u": draw_2u
    },
    "3": {
        "i": draw_3i,
        "ü": draw_3u2,
        "u": draw_3u
    },
    "4": {
        "i": draw_4i,
        "ü": draw_4u2,
        "u": draw_4u
    },
    "5": {
        "i": draw_5i,
        "ü": draw_5u2,
        "u": draw_5u
    },
    "6": {
        "i": draw_6i,
        "ü": draw_6u2,
        "u": draw_6u
    },
    "7": {
        "i": draw_7i,
        "ü": draw_7u2,
        "u": draw_7u
    }
}


def draw_head(ctx, pitch, vowel):
    draw_funcs[pitch][vowel](ctx)


def draw_1(ctx):
    ctx.new_path()
    ctx.move_to(0.05, 0.25)
    ctx.line_to(0, 0.1)
    ctx.stroke()
    return 1


def draw_2(ctx):
    ctx.new_path()
    ctx.move_to(0.1, 0.4)
    ctx.line_to(0, 0.1)
    ctx.stroke()
    return 1


def draw_5(ctx):
    ctx.new_path()
    ctx.move_to(0, 0.1)
    ctx.line_to(0.05, 0.25)
    ctx.line_to(0.25, 0.25)
    ctx.line_to(0.2, 0.1)
    ctx.stroke()
    return 2


def draw_10(ctx):
    ctx.new_path()
    ctx.move_to(0, 0.1)
    ctx.line_to(0.1, 0.4)
    ctx.line_to(0.3, 0.4)
    ctx.line_to(0.2, 0.1)
    ctx.stroke()
    return 2


def draw_15(ctx):
    ctx.new_path()
    ctx.move_to(0, 0.1)
    ctx.line_to(0.1, 0.4)
    ctx.line_to(0.3, 0.4)
    ctx.line_to(0.2, 0.1)
    ctx.move_to(0.05, 0.25)
    ctx.line_to(0.25, 0.25)
    ctx.stroke()
    return 2


draw_num_funcs = {
    15: draw_15,
    10: draw_10,
    5: draw_5,
    2: draw_2,
    1: draw_1
}


def draw_num(ctx, num):
    offset = 0.6
    ctx.translate(0.6, 0)
    for i, num_func in draw_num_funcs.items():
        while num >= i:
            width = num_func(ctx) * 0.2
            offset += width
            ctx.translate(width, 0)
            num -= i
    ctx.translate(-offset, 0)


def draw(ctx, str):
    print("adding secondary voice " + str)
    match = sec_re.match(str)
    pitch = match.group("num")
    vow = match.group("vow")
    vow_split = list(map(lambda x: x[0], sec_vow_re.findall(vow)))

    if len(vow_split) < 1:
        print("error parsing secondary voice string" + str)
        return
    if len(vow_split) > 2:
        print("too many vowels in secondary voice string" + str)
        return

    first_match = sec_vow_re.match(vow_split[0])
    has_firstvow = False
    if not first_match.group("vow") == "-":
        draw_head(ctx, pitch, first_match.group("vow"))
        has_firstvow = True
    ctx.line_to(1.9, 0.1)
    ctx.stroke()

    if first_match.group("stp") is not None:
        if first_match.group("num") is not None:
            draw_num(ctx, int(first_match.group("num")))
        else:
            draw_num(ctx, len(first_match.group("stp")))

    if len(vow_split) == 2:
        second_match = sec_vow_re.match(vow_split[1])
        if second_match.group("vow") == "-":
            return
        if has_firstvow:
            ctx.translate(0.5, 0.5)
        else:
            ctx.translate(0.5, 0)
        draw_head(ctx, pitch, second_match.group("vow"))
        ctx.line_to(1.4, 0.1)
        ctx.stroke()

        if second_match.group("stp") is not None:
            if second_match.group("num") is not None:
                draw_num(ctx, int(second_match.group("num")))
            else:
                draw_num(ctx, len(second_match.group("stp")))

        if has_firstvow:
            ctx.translate(-0.5, -0.5)
        else:
            ctx.translate(-0.5, 0)


def get_height(str):
    match = sec_re.match(str)
    vow = match.group("vow")
    vow_split = list(map(lambda x: x[0], sec_vow_re.findall(vow)))
    return len(vow_split) - len([c for c in vow_split if "-" in c])
