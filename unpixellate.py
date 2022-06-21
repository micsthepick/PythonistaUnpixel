import ui
from scene import *
from PIL import Image

rect_size_x = 18
rect_size_y = 29

charset = '0123456789'

bg_color = '#000000'
text_color = '#ffffff'
pad_color = '#ff0000'

font_size = 60

custom_sytling = 'text-shadow: 6px 6px 0 ' + '#bbbbbb' + ';'

longest_guess = 8

font = 'Minecraft'

#bgcolor = bgcolor.replace('#', '\%23')
#textcolor = textcolor.replace('#', '\%23')
#padcolor = padcolor.replace('#', '\%23')
#customsytling.replace('#')

redacted_image = Image.open('secret.png')

render_window = ui.WebView()#hidden=True)

render_window.width = 200

def gen_redacted(s: str, cb: callable):
    html_string = ''.join([
        '<html><head></head><body style="padding: ',
        str(rect_size_x+1),
        'px 0px 0px ',
        str(rect_size_y+1),
        'px; background-color: ',
        bg_color,
        ';"><span style="padding 0px 0px 0px 0px; ',
        'font-weight: normal; ',
        'line-spacing: 0px; ',
        'word-spacing: 0px; ',
        'white-space: pre; ',
        'margin: 0; ',
        'font-size: ',
        str(font_size),
        'px; font-family: ',
        repr(font),
        '; color: ',
        text_color,
        '; ',
        custom_sytling,
        '">',
        s,
        '</span><span style="0px 0px 0px 1px; ',
        'margin: 0; ',
        'color: ',
        pad_color,
        '; font-size: ',
        str(font_size),
        ';">█</span></body></html>'
    ])
    
    class OnLoadDelegate(object):
        def webview_should_start_load(self, webview, url, nav_type):
            return True
        
        def webview_did_start_load(self, webview):
            pass
        
        def webview_did_finish_load(self, webview):
            with ui.ImageContext(200, 30) as context:
                render_window.draw_snapshot()
                im = context.get_image()
            cb(im)
        
        def webview_did_fail_load(self, webview, error_code, error_msg):
            pass
    
    render_window.delegate = OnLoadDelegate()
    render_window.load_html(html_string)

class Main(Scene):
    def setup(self):
        gen_redacted(
            'UNPIXELLATE',
            lambda x:
            self.add_child(
                SpriteNode(Texture(x), anchor_point=(0, 0))
            )
        )


def check_string(s):
    pass

if __name__ == '__main__':
    run(Main())
