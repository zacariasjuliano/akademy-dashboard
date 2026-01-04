from trytond.pool import Pool

def register():
    Pool.register(

        module='akademy_dashboard', type_='model'
    )