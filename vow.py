import math


def draw_base(ctx):
    ctx.new_path()
    ctx.move_to(0.1, 0.1)
    ctx.line_to(1.9, 0.1)
    ctx.stroke()


def draw_swoosh(ctx):
    ctx.new_path()
    ctx.move_to(0.3, 0.9)
    ctx.line_to(1.7, 0.9)
    ctx.line_to(1.23, 0.1)
    ctx.stroke()


def draw_i(ctx):
    draw_base(ctx)
    ctx.new_path()
    ctx.arc(1, 0.5, 0.4, 0, 2 * math.pi)
    ctx.stroke()


def draw_i2(ctx):
    draw_base(ctx)
    draw_swoosh(ctx)


def draw_u2(ctx):
    draw_base(ctx)
    ctx.new_path()
    ctx.move_to(0.3, 0.9)
    ctx.line_to(1.7, 0.9)
    ctx.move_to(1, 0.9)
    ctx.line_to(1, 0.1)
    ctx.stroke()


def draw_u(ctx):
    ctx.new_path()
    ctx.move_to(0.1, 0.9)
    ctx.line_to(0.1, 0.1)
    ctx.line_to(1.9, 0.1)
    ctx.line_to(1.9, 0.9)
    ctx.stroke()


def draw_o2(ctx):
    draw_base(ctx)
    ctx.new_path()
    ctx.move_to(0.6, 0.1)
    ctx.line_to(0.6, 0.9)
    ctx.line_to(1.4, 0.9)
    ctx.line_to(1.4, 0.1)
    ctx.stroke()


def draw_e(ctx):
    draw_o2(ctx)
    ctx.new_path()
    ctx.move_to(1.4, 0.9)
    ctx.line_to(1.9, 0.9)
    ctx.line_to(1.4, 0.1)
    ctx.stroke()


def draw_e2(ctx):
    draw_i(ctx)
    ctx.new_path()
    ctx.move_to(0.3, 0.5)
    ctx.line_to(1.7, 0.5)
    ctx.stroke()


def draw_o(ctx):
    draw_i(ctx)
    draw_swoosh(ctx)


def draw_a2(ctx):
    draw_base(ctx)
    ctx.new_path()
    ctx.move_to(1.3, 0.9)
    ctx.line_to(1.3, 0.1)
    ctx.line_to(1.7, 0.5)
    ctx.stroke()


def draw_e1(ctx):
    draw_base(ctx)
    ctx.new_path()
    ctx.arc(1, 0.5, 0.4, math.pi, 2 * math.pi)
    ctx.stroke()


def draw_a(ctx):
    draw_u(ctx)
    draw_swoosh(ctx)


def draw_a1(ctx):
    draw_u(ctx)
    ctx.new_path()
    ctx.move_to(0.1, 0.9)
    ctx.line_to(1.9, 0.9)
    ctx.stroke()


draw_funcs = {
    "i": draw_i,
    "ï": draw_i2,
    "ü": draw_u2,
    "u": draw_u,
    "ö": draw_o2,
    "e": draw_e,
    "ë": draw_e2,
    "o": draw_o,
    "ä": draw_a2,
    "é": draw_e1,
    "a": draw_a,
    "á": draw_a1
}
