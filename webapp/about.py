import justpy as jp
from webapp import layout
from webapp import page

class About(page.Page):

    path = '/about'
    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes = 'bg-gray-200 h-screen')
        jp.Div(a=div, text='This is the about page!', classes='text-4xl n-2')
        jp.Div(a=div, text="""
        sacas asdlkassad aassfdsgfdhttfdfgsdfafdasdavdssadcascasdasdascasascasca
        casdassadasdcascasadascascascacacascascascacascas s asdasca asasd asd asdasfas
        asdasdasdasdasdasda sdasadsd asdafvsdtr das ads asdasdasfaeedasd asda awdada sdawd as dasdaw
        """, classes='text-lg')
        return wp



