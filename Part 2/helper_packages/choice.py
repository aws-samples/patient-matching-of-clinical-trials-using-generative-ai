from ipywidgets import widgets


class Prompt:
    def __init__(self, data) -> None:
        self.data = data
        self.choice = self.data[list(data)[0]]

    def get_buttons(self):
        buttons = [widgets.Button(description=str(i))
                   for i in list(self.data.keys())]
        for i in buttons:
            i.on_click(self.onclick)
        outputs = widgets.HBox([items for items in buttons])
        return outputs

    def onclick(self, click):
        if len(click.description) < 14:
            print(
                f'<a href="https://clinicaltrials.gov/study/{click.description}">{click.description}</a> is selected')
        else:
            print(
                f'Patient <a href="patient_records/{click.description}">{click.description}</a> is selected')

        # print(f"{click.description}: ")
        self.choice = self.data[click.description]

    def get_choice(self):
        return self.choice
