from invoke import task


@task
def start(ctx):
    ctx.run("python3 src/index.py")

# Joillain järjestelmillä tämä toimii
# @task
# def start(ctx):
#     ctx.run("python3 src/index.py", pty=True)


@task
def test(ctx):
    ctx.run("pytest src")

# Joillain järjestelmillä tämä toimii
# @task
# def test(ctx):
#     ctx.run("pytest src", pty=True)


@task
def coverage_report(ctx):
    ctx.run("coverage run --branch -m pytest src")
    ctx.run("coverage html")

# Joillain järjestelmillä tämä toimii
# @task
# def coverage_report(ctx):
#     ctx.run("coverage run --branch -m pytest src", pty=True)
#     ctx.run("coverage html", pty=True)


@task
def lint(ctx):
    ctx.run("pylint src")

# Joillain järjestelmillä tämä toimii
# @task
# def lint(ctx):
#     ctx.run("pylint src", pty=True)
