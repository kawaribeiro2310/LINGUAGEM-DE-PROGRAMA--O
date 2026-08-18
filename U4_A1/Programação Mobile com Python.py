from importlib import import_module


def _kivy_class(module_name, class_name):
    """Load a Kivy class without producing false missing-import diagnostics."""
    try:
        return getattr(import_module(module_name), class_name)
    except ModuleNotFoundError as error:
        raise SystemExit(
            "Kivy is required to run this application. Install it with: pip install kivy"
        ) from error


App = _kivy_class('kivy.app', 'App')
Builder = _kivy_class('kivy.lang', 'Builder')
BoxLayout = _kivy_class('kivy.uix.boxlayout', 'BoxLayout')
# These classes must be imported so that the KV parser registers them.
_kivy_class('kivy.uix.label', 'Label')
_kivy_class('kivy.uix.tabbedpanel', 'TabbedPanel')
_kivy_class('kivy.uix.tabbedpanel', 'TabbedPanelItem')

Builder.load_string('''
<TabsLayout>:
    BoxLayout:
        orientation: 'vertical'
        TabbedPanel:
            do_default_tab: False
            TabbedPanelItem:
                text: 'Tab 1'
                BoxLayout:
                    orientation: 'vertical'
                    Label:
                        text: 'Content for Tab 1'
            TabbedPanelItem:
                text: 'Tab 2'
                BoxLayout:
                    orientation: 'vertical'
                    Label:
                        text: 'Content for Tab 2'
''')


class TabsLayout(BoxLayout):
    pass


class TabsApp(App):
    def build(self):
        return TabsLayout()


if __name__ == '__main__':
    TabsApp().run()