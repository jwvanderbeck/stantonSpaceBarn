from django import forms

class SubmitBuildForm(forms.Form):
	role = forms.ChoiceField((
    ('Interdiction', 'Interdiction'),
    ('Exploration', 'Exploration'),
    ('Piracy', 'Piracy'),
    ('Transport', 'Transport'),
    ('Racing', 'Racing'),
    ('Escort', 'Escort'),
    ('Bounty Hunting', 'Bounty Hunting'),
	))
	name = forms.CharField(max_length=30)
