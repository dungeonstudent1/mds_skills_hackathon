from df_engine.core import Actor, Context
from scenario.label import eng_employees_label, eng_jobs_label, ru_employees_label, ru_jobs_label, english, russian, start_label

def check_in(req, labels):
    req = req.lower()
    for label in labels:
        if label in req:
            return True
    return False

def employees_search(ctx: Context, actor: Actor, *args, **kwargs) -> bool:
    request = ctx.last_request
    return check_in(request, eng_employees_label) or check_in(request, ru_employees_label)

def job_search(ctx: Context, actor: Actor, *args, **kwargs) -> bool:
    request = ctx.last_request
    return check_in(request, eng_jobs_label) or check_in(request, ru_jobs_label)

def true(ctx: Context, actor: Actor, *args, **kwargs) -> bool:
    return True

def choosed_en(ctx: Context, actor: Actor, *args, **kwargs) -> bool:
    request = ctx.last_request
    return check_in(request, english)

def choosed_ru(ctx: Context, actor: Actor, *args, **kwargs) -> bool:
    request = ctx.last_request
    return check_in(request, russian)

def start(ctx: Context, actor: Actor, *args, **kwargs) -> bool:
    request = ctx.last_request
    return check_in(request, start_label)