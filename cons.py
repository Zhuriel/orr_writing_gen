import math


def draw_bigcirc(ctx):
    ctx.new_path()
    ctx.arc(0.5, 0.5, 0.4, 0, 2 * math.pi)
    ctx.stroke()


def draw_p(ctx):
    draw_bigcirc(ctx)
    ctx.new_path()
    ctx.arc(0.5, 0.5, 0.05, 0, 2 * math.pi)
    ctx.stroke()


def draw_b(ctx):
    draw_bigcirc(ctx)
    ctx.new_path()
    ctx.move_to(0.9, 0.9)
    ctx.line_to(0.8, 0.8)
    ctx.stroke()


def draw_t(ctx):
    ctx.move_to(0.1, 0.1)
    ctx.line_to(0.1, 0.9)
    ctx.line_to(0.9, 0.9)
    ctx.stroke()


def draw_d(ctx):
    ctx.move_to(0.1, 0.1)
    ctx.line_to(0.9, 0.1)
    ctx.line_to(0.9, 0.9)
    ctx.stroke()


def draw_k(ctx):
    draw_t(ctx)
    ctx.new_path()
    ctx.arc(0.5, 0.5, 0.2, 0, 2 * math.pi)
    ctx.stroke()


def draw_g(ctx):
    draw_d(ctx)
    ctx.new_path()
    ctx.arc(0.5, 0.5, 0.2, 0, 2 * math.pi)
    ctx.stroke()


def draw_m(ctx):
    ctx.new_path()
    ctx.arc(0.3, 0.3, 0.2, 0, 2 * math.pi)
    ctx.stroke()
    ctx.new_path()
    ctx.arc(0.7, 0.7, 0.2, 0, 2 * math.pi)
    ctx.stroke()
    ctx.new_path()
    ctx.move_to(0.3, 0.3)
    ctx.line_to(0.7, 0.7)
    ctx.stroke()


def draw_n(ctx):
    ctx.new_path()
    ctx.move_to(0.1, 0.1)
    ctx.line_to(0.6, 0.1)
    ctx.line_to(0.9, 0.9)
    ctx.line_to(0.1, 0.9)
    ctx.stroke()
    ctx.new_path()
    ctx.arc(0.85, 0.15, 0.05, 0, 2 * math.pi)
    ctx.stroke()


def draw_N(ctx):
    ctx.new_path()
    ctx.move_to(0.1, 0.1)
    ctx.line_to(0.9, 0.1)
    ctx.line_to(0.6, 0.9)
    ctx.line_to(0.1, 0.9)
    ctx.stroke()
    ctx.new_path()
    ctx.arc(0.3, 0.5, 0.2, 0, 2 * math.pi)
    ctx.stroke()


def draw_B(ctx):
    ctx.new_path()
    ctx.move_to(0.7, 0.7)
    ctx.arc(0.3, 0.5, 0.2, 0.5 * math.pi, 1.5 * math.pi)
    ctx.line_to(0.7, 0.3)
    ctx.stroke()
    ctx.new_path()
    ctx.move_to(0.3, 0.1)
    ctx.line_to(0.9, 0.1)
    ctx.line_to(0.9, 0.9)
    ctx.line_to(0.3, 0.9)
    ctx.stroke()


def draw_r(ctx):
    ctx.new_path()
    ctx.move_to(0.1, 0.5)
    ctx.line_to(0.3, 0.9)
    ctx.line_to(0.5, 0.1)
    ctx.line_to(0.7, 0.9)
    ctx.line_to(0.9, 0.5)
    ctx.stroke()


def draw_R(ctx):
    ctx.new_path()
    ctx.move_to(0.9, 0.1)
    ctx.arc(0.5, 0.5, 0.4, 0, math.pi)
    ctx.line_to(0.1, 0.1)
    ctx.stroke()


def draw_v(ctx):
    ctx.new_path()
    ctx.move_to(0.1, 0.1)
    ctx.line_to(0.9, 0.1)
    ctx.move_to(0.1, 0.5)
    ctx.line_to(0.9, 0.5)
    ctx.move_to(0.1, 0.9)
    ctx.line_to(0.9, 0.9)
    ctx.stroke()


def draw_w(ctx):
    ctx.new_path()
    ctx.move_to(0.1, 0.1)
    ctx.line_to(0.1, 0.9)
    ctx.move_to(0.5, 0.1)
    ctx.line_to(0.5, 0.9)
    ctx.move_to(0.9, 0.1)
    ctx.line_to(0.9, 0.9)
    ctx.stroke()


def draw_s(ctx):
    ctx.new_path()
    ctx.move_to(0.9, 0.1)
    ctx.line_to(0.9, 0.9)
    ctx.arc_negative(0.1, 0.9, 0.8, 2 * math.pi, 1.5 * math.pi)
    ctx.stroke()


def draw_z(ctx):
    ctx.new_path()
    ctx.move_to(0.1, 0.1)
    ctx.line_to(0.1, 0.9)
    ctx.arc(0.9, 0.9, 0.8, math.pi, 1.5 * math.pi)
    ctx.stroke()


def draw_j(ctx):
    ctx.new_path()
    ctx.move_to(0.1, 0.1)
    ctx.line_to(0.1, 0.9)
    ctx.line_to(0.9, 0.9)
    ctx.line_to(0.9, 0.1)
    ctx.close_path()
    ctx.stroke()
    ctx.new_path()
    ctx.move_to(0.1, 0.5)
    ctx.line_to(0.9, 0.5)
    ctx.move_to(0.5, 0.5)
    ctx.line_to(0.5, 0.1)
    ctx.stroke()


def draw_H(ctx):
    ctx.new_path()
    ctx.move_to(0.1, 0.1)
    ctx.line_to(0.1, 0.9)
    ctx.line_to(0.9, 0.9)
    ctx.line_to(0.9, 0.1)
    ctx.close_path()
    ctx.stroke()
    ctx.new_path()
    ctx.arc(0.5, 0.5, 0.2, 0, 2 * math.pi)
    ctx.stroke()


def draw_y(ctx):
    ctx.new_path()
    ctx.arc(0.5, 0.5, 0.05, 0, 2 * math.pi)
    ctx.stroke()


def draw_Y(ctx):
    ctx.new_path()
    ctx.move_to(0.1, 0.1)
    ctx.line_to(0.1, 0.9)
    ctx.line_to(0.9, 0.9)
    ctx.line_to(0.9, 0.1)
    ctx.close_path()
    ctx.stroke()
    for xpos in [0.35, 0.65]:
        for ypos in [0.35, 0.65]:
            ctx.new_path()
            ctx.arc(xpos, ypos, 0.05, 0, 2 * math.pi)
            ctx.stroke()


def draw_l(ctx):
    draw_bigcirc(ctx)


def draw_L(ctx):
    ctx.new_path()
    ctx.move_to(0.5, 0.1)
    ctx.line_to(0.9, 0.5)
    ctx.line_to(0.5, 0.9)
    ctx.line_to(0.1, 0.5)
    ctx.close_path()
    ctx.stroke()


draw_funcs = {
    "p": draw_p,
    "b": draw_b,
    "t": draw_t,
    "d": draw_d,
    "k": draw_k,
    "g": draw_g,
    "m": draw_m,
    "n": draw_n,
    "N": draw_N,
    "B": draw_B,
    "r": draw_r,
    "R": draw_R,
    "v": draw_v,
    "w": draw_w,
    "s": draw_s,
    "z": draw_z,
    "j": draw_j,
    "H": draw_H,
    "y": draw_y,
    "Y": draw_Y,
    "l": draw_l,
    "L": draw_L
}
